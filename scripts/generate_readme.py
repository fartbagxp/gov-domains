#!/usr/bin/env python3
"""
Reads collected ASN prefix CSVs and httpx tech CSVs, then updates the
auto-generated sections of README.md between <!-- BEGIN:name --> markers.
"""

import csv
import ipaddress
import json
import os
import re
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
README_PATH = REPO_ROOT / "README.md"
ASN_DIR = REPO_ROOT / "data" / "asn"
TECH_DIR = REPO_ROOT / "data" / "tech"

CATEGORIES = {
    "fed-gov":   ("data/us-fed-gov-agencies.csv",           "Federal Agencies"),
    "state-gov": ("data/us-state-gov-agencies.csv",         "State Governments"),
    "city-gov":  ("data/us-city-gov-agencies.csv",          "City Governments"),
    "hospitals": ("data/us-hospital-systems.csv",           "Hospital Systems"),
    "insurance": ("data/us-health-insurance.csv",           "Health Insurers"),
    "pbm":       ("data/us-pharmacy-benefit-managers.csv",  "Pharmacy Benefit Managers"),
    "health-it": ("data/us-health-it-vendors.csv",          "Health IT Vendors"),
    "academic":  ("data/us-academics.csv",                  "Academic Institutions"),
}


# ── Helpers ───────────────────────────────────────────────────────────────────

def ipv4_size(prefix: str) -> int:
    try:
        return ipaddress.ip_network(prefix, strict=False).num_addresses
    except ValueError:
        return 0


def fmt(n: int) -> str:
    if n == 0:
        return "—"
    if n >= 1_000_000_000:
        return f"{n / 1_000_000_000:.1f}B"
    if n >= 1_000_000:
        return f"{n / 1_000_000:.1f}M"
    if n >= 1_000:
        return f"{n / 1_000:.1f}K"
    return str(n)


def fmt_exact(n: int) -> str:
    return f"{n:,}" if n else "—"


def md_table(headers: list[str], rows: list[list], alignments: list[str] | None = None) -> str:
    if not rows:
        return "_No data yet._\n"
    alignments = alignments or ["left"] * len(headers)
    sep_map = {"left": ":---", "right": "---:", "center": ":---:"}
    seps = [sep_map.get(a, ":---") for a in alignments]

    col_widths = [max(len(str(h)), len(seps[i])) for i, h in enumerate(headers)]
    for row in rows:
        for i, cell in enumerate(row):
            col_widths[i] = max(col_widths[i], len(str(cell)))

    def pad(s: str, width: int, align: str) -> str:
        if align == "right":
            return s.rjust(width)
        if align == "center":
            return s.center(width)
        return s.ljust(width)

    def fmt_row(cells: list) -> str:
        return "| " + " | ".join(
            pad(str(c), col_widths[i], alignments[i]) for i, c in enumerate(cells)
        ) + " |"

    lines = [
        fmt_row(headers),
        "| " + " | ".join(s.ljust(col_widths[i]) for i, s in enumerate(seps)) + " |",
    ]
    for row in rows:
        lines.append(fmt_row(row))
    return "\n".join(lines) + "\n"


# ── Data loading ──────────────────────────────────────────────────────────────

def load_prefix_csv(category: str) -> list[dict]:
    path = ASN_DIR / f"{category}-prefixes.csv"
    if not path.exists():
        return []
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def load_source_csv(rel_path: str) -> list[dict]:
    path = REPO_ROOT / rel_path
    if not path.exists():
        return []
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def _empty_bucket() -> dict:
    return {"asns": set(), "ipv4": 0, "ipv6": 0, "ipv4_size": 0, "has_data": False}


def _accumulate(bucket: dict, r: dict) -> None:
    bucket["has_data"] = True
    asn = r.get("asn", "")
    prefix = r.get("prefix", "")
    ip_ver = r.get("ip_version", "")
    if asn:
        bucket["asns"].add(asn)
    if prefix and ip_ver == "ipv4":
        bucket["ipv4"] += 1
        bucket["ipv4_size"] += ipv4_size(prefix)
    elif prefix and ip_ver == "ipv6":
        bucket["ipv6"] += 1


def _stats_cells(d: dict) -> list:
    if not d["has_data"]:
        return ["—", "—", "—", "—"]
    return [
        fmt_exact(len(d["asns"])),
        fmt_exact(d["ipv4"]),
        fmt_exact(d["ipv6"]),
        fmt(d["ipv4_size"]),
    ]


def build_category_stats(category: str) -> dict:
    rows = load_prefix_csv(category)
    asns: set = set()
    ipv4_total = 0
    ipv6_prefixes = 0
    ipv4_prefixes = 0

    for r in rows:
        asn = r.get("asn", "")
        prefix = r.get("prefix", "")
        ip_ver = r.get("ip_version", "")
        if asn:
            asns.add(asn)
        if prefix:
            if ip_ver == "ipv4":
                ipv4_prefixes += 1
                ipv4_total += ipv4_size(prefix)
            elif ip_ver == "ipv6":
                ipv6_prefixes += 1

    return {
        "asns": len(asns),
        "ipv4_prefixes": ipv4_prefixes,
        "ipv6_prefixes": ipv6_prefixes,
        "ipv4_addresses": ipv4_total,
    }


# ── Section generators ────────────────────────────────────────────────────────

def section_overview_table() -> str:
    headers = ["Category", "Organizations", "ASNs", "IPv4 Prefixes", "IPv6 Prefixes", "Est. IPv4 Addresses"]
    alignments = ["left", "right", "right", "right", "right", "right"]
    rows = []
    for cat, (src, label) in CATEGORIES.items():
        src_rows = load_source_csv(src)
        src_asns = {r.get("asn", "") for r in src_rows if r.get("asn", "").lstrip("AS").isdigit()}
        stats = build_category_stats(cat)
        rows.append([
            f"**{label}**",
            fmt_exact(len(src_asns)),
            fmt_exact(stats["asns"]) if stats["asns"] else f"_{len(src_asns)} tracked_",
            fmt_exact(stats["ipv4_prefixes"]),
            fmt_exact(stats["ipv6_prefixes"]),
            fmt(stats["ipv4_addresses"]),
        ])
    return md_table(headers, rows, alignments)


def section_fed_gov_table() -> str:
    src_rows = load_source_csv("data/us-fed-gov-agencies.csv")
    if not src_rows:
        return "_Source data not found._\n"

    # Build dict keyed by abbreviation; first occurrence wins for agency name
    by_abbrev: dict[str, dict] = {}
    for r in src_rows:
        abbrev = r.get("abbrievations", "").strip()
        agency = r.get("fedagency", "").strip()
        if abbrev and abbrev not in by_abbrev:
            by_abbrev[abbrev] = {"agency": agency, **_empty_bucket()}

    # Overlay collected prefix data
    for r in load_prefix_csv("fed-gov"):
        abbrev = r.get("abbreviation", "")
        if abbrev in by_abbrev:
            _accumulate(by_abbrev[abbrev], r)

    headers = ["Abbrev", "Agency", "ASNs", "IPv4 Prefixes", "IPv6 Prefixes", "Est. IPv4 Addresses"]
    alignments = ["left", "left", "right", "right", "right", "right"]
    table_rows = [
        [abbrev, d["agency"]] + _stats_cells(d)
        for abbrev, d in sorted(by_abbrev.items())
    ]
    return md_table(headers, table_rows, alignments)


def section_state_gov_table() -> str:
    src_rows = load_source_csv("data/us-state-gov-agencies.csv")
    if not src_rows:
        return "_Source data not found._\n"

    by_org: dict[str, dict] = {}
    org_state: dict[str, str] = {}
    for r in src_rows:
        org = r.get("stategov", "").strip()
        state = r.get("state", "").strip()
        if org:
            org_state[org] = state
            if org not in by_org:
                by_org[org] = _empty_bucket()

    for r in load_prefix_csv("state-gov"):
        org = r.get("agency") or r.get("abbreviation", "")
        if org in by_org:
            _accumulate(by_org[org], r)

    headers = ["St", "Organization", "ASNs", "IPv4 Prefixes", "IPv6 Prefixes", "Est. IPv4 Addresses"]
    alignments = ["left", "left", "right", "right", "right", "right"]
    table_rows = [
        [org_state.get(org, ""), org] + _stats_cells(d)
        for org, d in sorted(by_org.items(), key=lambda x: (org_state.get(x[0], ""), x[0]))
    ]
    return md_table(headers, table_rows, alignments)


def section_city_gov_table() -> str:
    src_rows = load_source_csv("data/us-city-gov-agencies.csv")
    if not src_rows:
        return "_Source data not found._\n"

    by_org: dict[str, dict] = {}
    city_state: dict[str, str] = {}
    for r in src_rows:
        org = r.get("citygov", "").strip()
        state = r.get("state", "").strip()
        if org:
            city_state[org] = state
            if org not in by_org:
                by_org[org] = _empty_bucket()

    for r in load_prefix_csv("city-gov"):
        org = r.get("agency") or r.get("abbreviation", "")
        if org in by_org:
            _accumulate(by_org[org], r)

    headers = ["St", "City / Organization", "ASNs", "IPv4 Prefixes", "IPv6 Prefixes", "Est. IPv4 Addresses"]
    alignments = ["left", "left", "right", "right", "right", "right"]
    table_rows = [
        [city_state.get(org, ""), org] + _stats_cells(d)
        for org, d in sorted(by_org.items(), key=lambda x: (city_state.get(x[0], ""), x[0]))
    ]
    return md_table(headers, table_rows, alignments)


def section_health_table(category: str, src_col: str, src_file: str) -> str:
    src_rows = load_source_csv(src_file)
    if not src_rows:
        return "_Source data not found._\n"

    by_org: dict[str, dict] = {}
    for r in src_rows:
        org = r.get(src_col, "").strip()
        if org and org not in by_org:
            by_org[org] = _empty_bucket()

    for r in load_prefix_csv(category):
        org = r.get("agency") or r.get("abbreviation", "")
        if org in by_org:
            _accumulate(by_org[org], r)

    headers = ["Organization", "ASNs", "IPv4 Prefixes", "IPv6 Prefixes", "Est. IPv4 Addresses"]
    alignments = ["left", "right", "right", "right", "right"]

    def sort_key(item: tuple) -> tuple:
        org, d = item
        # Collected entries: sort by IPv4 size descending; uncollected: alphabetical at end
        if d["has_data"]:
            return (0, -d["ipv4_size"], org)
        return (1, 0, org)

    table_rows = [
        [org] + _stats_cells(d)
        for org, d in sorted(by_org.items(), key=sort_key)
    ]
    return md_table(headers, table_rows, alignments)


def section_tech_summary() -> str:
    if not TECH_DIR.exists():
        return "_No technology data collected yet._\n"

    tech_counter: Counter = Counter()
    domain_tech: dict[str, set] = defaultdict(set)

    for csv_file in TECH_DIR.glob("*.csv"):
        domain = csv_file.stem.removeprefix("domain.").removesuffix("_httpx")
        try:
            with open(csv_file, newline="", encoding="utf-8") as f:
                for row in csv.DictReader(f):
                    raw = row.get("tech", "")
                    if not raw or raw in ("[]", ""):
                        continue
                    try:
                        techs = json.loads(raw)
                    except (json.JSONDecodeError, ValueError):
                        techs = [t.strip().strip('"') for t in raw.strip("[]").split(",") if t.strip()]
                    for t in techs:
                        t = t.strip()
                        if t:
                            tech_counter[t] += 1
                            domain_tech[t].add(domain)
        except Exception:
            continue

    if not tech_counter:
        return "_No technology data collected yet._\n"

    headers = ["Technology", "Domains", "Example Domains"]
    alignments = ["left", "right", "left"]
    top = tech_counter.most_common(40)
    table_rows = []
    for tech, count in top:
        examples = sorted(domain_tech[tech])[:3]
        table_rows.append([tech, count, ", ".join(examples)])

    return md_table(headers, table_rows, alignments)


def section_timestamp() -> str:
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    return f"_Last updated: {ts}_\n"


# ── README updater ────────────────────────────────────────────────────────────

MARKER_RE = re.compile(
    r"<!-- BEGIN:(\w[\w-]*) -->(.*?)<!-- END:\1 -->",
    re.DOTALL,
)

SECTION_GENERATORS = {
    "timestamp":        section_timestamp,
    "overview-table":   section_overview_table,
    "fed-gov-table":    section_fed_gov_table,
    "state-gov-table":  section_state_gov_table,
    "city-gov-table":   section_city_gov_table,
    "hospitals-table":  lambda: section_health_table("hospitals",  "hospital",  "data/us-hospital-systems.csv"),
    "insurance-table":  lambda: section_health_table("insurance",  "insurer",   "data/us-health-insurance.csv"),
    "pbm-table":        lambda: section_health_table("pbm",        "pbm",       "data/us-pharmacy-benefit-managers.csv"),
    "health-it-table":  lambda: section_health_table("health-it",  "vendor",    "data/us-health-it-vendors.csv"),
    "tech-table":       section_tech_summary,
}


def update_readme(path: Path) -> None:
    text = path.read_text(encoding="utf-8")

    def replace(m: re.Match) -> str:
        name = m.group(1)
        gen = SECTION_GENERATORS.get(name)
        if gen is None:
            print(f"  [~] Unknown section: {name}", file=sys.stderr)
            return m.group(0)
        content = gen()
        print(f"  [+] Updated section: {name}")
        return f"<!-- BEGIN:{name} -->\n{content}<!-- END:{name} -->"

    updated = MARKER_RE.sub(replace, text)
    path.write_text(updated, encoding="utf-8")


def main():
    print(f"[*] Updating {README_PATH}")
    update_readme(README_PATH)
    print("[+] Done.")


if __name__ == "__main__":
    main()
