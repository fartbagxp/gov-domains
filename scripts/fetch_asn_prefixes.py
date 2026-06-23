#!/usr/bin/env python3
"""
Fetches announced IP prefixes for each ASN listed in the agency CSV files.

Primary source: RIPE Stat announced-prefixes API (BGP-visible prefixes).
Enrichment (optional, via --rir-data-dir): RIR delegation files and
  bgp.potaroo.net autnums.html for official org name, registry, and status.

Outputs per-category CSVs to data/asn/.
"""

import csv
import os
import re
import sys
import time
import argparse
from datetime import datetime, timezone

import requests

RIPE_STAT_URL = "https://stat.ripe.net/data/announced-prefixes/data.json"
REQUEST_DELAY = 1.0
REQUEST_TIMEOUT = 30

SOURCE_FILES = {
    "fed-gov":    "data/us-fed-gov-agencies.csv",
    "state-gov":  "data/us-state-gov-agencies.csv",
    "city-gov":   "data/us-city-gov-agencies.csv",
    "academic":   "data/us-academics.csv",
    "hospitals":  "data/us-hospital-systems.csv",
    "insurance":  "data/us-health-insurance.csv",
    "pbm":        "data/us-pharmacy-benefit-managers.csv",
    "health-it":  "data/us-health-it-vendors.csv",
}

# (abbreviation_col, name_col, asn_col) — None means same as abbreviation
COLUMN_MAPS = {
    "fed-gov":   ("abbrievations", "fedagency", "asn"),
    "state-gov": ("stategov", None, "asn"),
    "city-gov":  ("citygov", "citygov", "asn"),
    "academic":  ("academic", None, "asn"),
    "hospitals": ("hospital", "hospital", "asn"),
    "insurance": ("insurer", "insurer", "asn"),
    "pbm":       ("pbm", "pbm", "asn"),
    "health-it": ("vendor", "vendor", "asn"),
}

RIR_DELEGATION_FILES = [
    "delegated-arin-extended-latest.txt",
    "delegated-ripencc-extended-latest.txt",
    "delegated-apnic-extended-latest.txt",
    "delegated-lacnic-extended-latest.txt",
    "delegated-afrinic-extended-latest.txt",
]


def load_agencies(filepath, abbrev_col, name_col, asn_col):
    agencies = []
    with open(filepath, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            asn_raw = row.get(asn_col, "").strip()
            if not asn_raw:
                continue
            asn_num = asn_raw.lstrip("AS").strip()
            if not asn_num.isdigit():
                continue
            abbrev = row.get(abbrev_col, "").strip() if abbrev_col else ""
            name = row.get(name_col, "").strip() if name_col else abbrev
            agencies.append({
                "abbreviation": abbrev,
                "agency": name,
                "asn": asn_num,
            })
    return agencies


# ── RIR enrichment ────────────────────────────────────────────────────────────

def parse_autnums(filepath):
    """
    Parse bgp.potaroo.net autnums.html into {asn_num_str: (short_name, description)}.
    Line format: <a href="...">AS{num}</a> SHORT_NAME - Description, CC
    """
    pattern = re.compile(r'>AS(\d+)\s*</a>\s+(\S+)\s+-\s+(.+?),\s+\w{2}\s*$')
    result = {}
    try:
        with open(filepath, encoding="latin-1") as f:
            for line in f:
                m = pattern.search(line)
                if m:
                    asn_num, short_name, description = m.group(1), m.group(2), m.group(3).strip()
                    result[asn_num] = (short_name, description)
    except FileNotFoundError:
        print(f"  [~] autnums.html not found at {filepath}", file=sys.stderr)
    return result


def parse_delegation_files(rir_data_dir):
    """
    Parse all delegated-*-extended-latest.txt files.
    Returns {asn_num_str: {"registry": str, "status": str, "date": str}}.

    Delegation ASN record format:
      registry|cc|asn|start_asn|count|date|status|hash
    """
    asn_info = {}
    for filename in RIR_DELEGATION_FILES:
        filepath = os.path.join(rir_data_dir, filename)
        if not os.path.exists(filepath):
            print(f"  [~] Delegation file not found: {filepath}", file=sys.stderr)
            continue
        registry_name = filename.split("-")[1]  # e.g. "arin", "ripencc"
        try:
            with open(filepath, encoding="ascii", errors="replace") as f:
                for line in f:
                    line = line.strip()
                    if not line or line.startswith("#"):
                        continue
                    parts = line.split("|")
                    if len(parts) < 7 or parts[2] != "asn":
                        continue
                    start_asn = parts[3]
                    count = int(parts[4]) if parts[4].isdigit() else 1
                    date_raw = parts[5]
                    status = parts[6]
                    date_str = f"{date_raw[:4]}-{date_raw[4:6]}-{date_raw[6:8]}" if len(date_raw) == 8 and date_raw.isdigit() else ""
                    for i in range(count):
                        asn_key = str(int(start_asn) + i)
                        asn_info[asn_key] = {
                            "registry": registry_name,
                            "status": status,
                            "date": date_str,
                        }
        except (OSError, ValueError) as e:
            print(f"  [!] Error parsing {filepath}: {e}", file=sys.stderr)
    return asn_info


def load_rir_enrichment(rir_data_dir):
    """Load all enrichment data from rir_data_dir. Returns (autnums_map, delegation_map)."""
    print(f"[*] Loading RIR enrichment data from {rir_data_dir}")
    autnums = parse_autnums(os.path.join(rir_data_dir, "autnums.html"))
    print(f"    autnums: {len(autnums)} ASN entries")
    delegation = parse_delegation_files(rir_data_dir)
    print(f"    delegation: {len(delegation)} ASN records")
    return autnums, delegation


# ── RIPE Stat prefix lookup ───────────────────────────────────────────────────

def fetch_prefixes(asn):
    """Query RIPE Stat for announced prefixes. Returns list of (prefix, ip_version)."""
    params = {"resource": f"AS{asn}", "min_peers_seeing": 0}
    try:
        resp = requests.get(RIPE_STAT_URL, params=params, timeout=REQUEST_TIMEOUT)
        resp.raise_for_status()
        data = resp.json()
    except requests.RequestException as e:
        print(f"  [!] Request failed for AS{asn}: {e}", file=sys.stderr)
        return None
    except ValueError as e:
        print(f"  [!] JSON parse error for AS{asn}: {e}", file=sys.stderr)
        return None

    if data.get("status") != "ok":
        print(f"  [!] RIPE Stat status={data.get('status')!r} for AS{asn}", file=sys.stderr)
        return None

    prefixes = []
    for entry in data.get("data", {}).get("prefixes", []):
        prefix = entry.get("prefix", "").strip()
        if prefix:
            ip_version = "ipv6" if ":" in prefix else "ipv4"
            prefixes.append((prefix, ip_version))
    return prefixes


# ── Output ────────────────────────────────────────────────────────────────────

def write_csv(output_path, rows, has_rir):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    fieldnames = ["abbreviation", "agency", "asn", "prefix", "ip_version"]
    if has_rir:
        fieldnames += ["rir_registry", "rir_status", "rir_assigned_date", "rir_short_name", "rir_description"]
    fieldnames.append("collected_at")
    with open(output_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    print(f"[+] Wrote {len(rows)} rows to {output_path}")


# ── Main processing ───────────────────────────────────────────────────────────

def process_category(category, source_path, output_path, autnums, delegation):
    abbrev_col, name_col, asn_col = COLUMN_MAPS[category]
    agencies = load_agencies(source_path, abbrev_col, name_col, asn_col)
    print(f"[*] {category}: {len(agencies)} ASN entries from {source_path}")

    has_rir = autnums is not None or delegation is not None
    autnums = autnums or {}
    delegation = delegation or {}

    seen_asns = set()
    rows = []
    collected_at = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    for entry in agencies:
        asn = entry["asn"]
        if asn in seen_asns:
            continue
        seen_asns.add(asn)

        rir_info = delegation.get(asn, {})
        autnum = autnums.get(asn, ("", ""))

        print(f"  -> Querying AS{asn} ({entry['agency'] or entry['abbreviation']})")
        prefixes = fetch_prefixes(asn)
        if prefixes is None:
            prefixes = []
        print(f"     {len(prefixes)} prefixes")

        if not prefixes:
            # Emit a row with no prefix so the ASN is still recorded
            row = {
                "abbreviation": entry["abbreviation"],
                "agency": entry["agency"],
                "asn": f"AS{asn}",
                "prefix": "",
                "ip_version": "",
            }
            if has_rir:
                row.update({
                    "rir_registry": rir_info.get("registry", ""),
                    "rir_status": rir_info.get("status", ""),
                    "rir_assigned_date": rir_info.get("date", ""),
                    "rir_short_name": autnum[0],
                    "rir_description": autnum[1],
                })
            row["collected_at"] = collected_at
            rows.append(row)
        else:
            for prefix, ip_version in prefixes:
                row = {
                    "abbreviation": entry["abbreviation"],
                    "agency": entry["agency"],
                    "asn": f"AS{asn}",
                    "prefix": prefix,
                    "ip_version": ip_version,
                }
                if has_rir:
                    row.update({
                        "rir_registry": rir_info.get("registry", ""),
                        "rir_status": rir_info.get("status", ""),
                        "rir_assigned_date": rir_info.get("date", ""),
                        "rir_short_name": autnum[0],
                        "rir_description": autnum[1],
                    })
                row["collected_at"] = collected_at
                rows.append(row)

        if prefixes:
            time.sleep(REQUEST_DELAY)

    rows.sort(key=lambda r: (r["abbreviation"], r["asn"], r["prefix"]))
    write_csv(output_path, rows, has_rir)
    return len(rows)


def main():
    parser = argparse.ArgumentParser(description="Fetch AS prefix data from RIPE Stat, optionally enriched from local RIR files")
    parser.add_argument(
        "--category",
        choices=list(SOURCE_FILES.keys()) + ["all"],
        default="all",
        help="Which agency category to process (default: all)",
    )
    parser.add_argument(
        "--data-dir",
        default="data",
        help="Root data directory containing the agency CSVs (default: data)",
    )
    parser.add_argument(
        "--rir-data-dir",
        default=None,
        help="Path to directory containing RIR delegation files and autnums.html for enrichment. "
             "E.g. ../rir-backup/data/raw. If omitted, enrichment columns are skipped.",
    )
    args = parser.parse_args()

    autnums, delegation = None, None
    if args.rir_data_dir:
        if not os.path.isdir(args.rir_data_dir):
            print(f"[!] --rir-data-dir not found: {args.rir_data_dir}", file=sys.stderr)
            sys.exit(1)
        autnums, delegation = load_rir_enrichment(args.rir_data_dir)

    categories = list(SOURCE_FILES.keys()) if args.category == "all" else [args.category]
    total = 0
    for category in categories:
        source = os.path.join(args.data_dir, SOURCE_FILES[category].removeprefix("data/"))
        output = os.path.join(args.data_dir, "asn", f"{category}-prefixes.csv")
        if not os.path.exists(source):
            print(f"[!] Source file not found: {source}", file=sys.stderr)
            continue
        total += process_category(category, source, output, autnums, delegation)

    print(f"\n[+] Done. Total rows written: {total}")


if __name__ == "__main__":
    main()
