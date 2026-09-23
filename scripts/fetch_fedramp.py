#!/usr/bin/env python3
"""
Fetches FedRAMP Marketplace authorization data.

Source: the FedRAMP-operated public data repository that backs
marketplace.fedramp.gov (refreshed daily, 2-3 AM ET).
  https://github.com/FedRAMP/marketplace-fedramp-gov-data

Outputs three CSVs to data/fedramp/:
  products.csv              — one row per cloud service offering
  agencies.csv              — one row per agency on the Marketplace
  agency-authorizations.csv — one row per agency<->product relationship

The relationship table is the useful one: it records which agency authorized,
reused, or is in process on which product, so a given product can be cited
back to the agencies that already accepted it.
"""

import argparse
import csv
import json
import os
import sys
from datetime import UTC, datetime

import requests

DATA_URL = "https://raw.githubusercontent.com/FedRAMP/marketplace-fedramp-gov-data/main/data.json"
PRODUCT_URL_PREFIX = "https://www.fedramp.gov/marketplace/products/"
REQUEST_TIMEOUT = 120

# Multi-valued fields are flattened with this separator, matching the
# certificate_ids convention already used in data/csv/.
LIST_SEP = ";"

# FedRAMP uses these sentinels in date fields instead of leaving them empty.
DATE_SENTINELS = {"not active", "not in process", "n/a", "none", ""}


# ── Helpers ───────────────────────────────────────────────────────────────────

def normalize_date(value):
    """
    FedRAMP emits dates as ISO timestamps ('2017-02-02T20:00:00.000Z') or as
    status sentinels ('Not Active'). Return YYYY-MM-DD, or '' for sentinels.
    """
    if not isinstance(value, str):
        return ""
    value = value.strip()
    if value.lower() in DATE_SENTINELS:
        return ""
    if len(value) >= 10 and value[4] == "-" and value[7] == "-":
        return value[:10]
    return ""


def join_list(value):
    """Flatten a list field to a separator-joined string, dropping blanks."""
    if not isinstance(value, list):
        return str(value).strip() if value else ""
    return LIST_SEP.join(str(v).strip() for v in value if str(v).strip())


def collapse(value):
    """Collapse whitespace so free text stays on one CSV line and greps cleanly."""
    if not isinstance(value, str):
        return ""
    return " ".join(value.split())


def product_url(product_id):
    return f"{PRODUCT_URL_PREFIX}{product_id}" if product_id else ""


def agency_label(record):
    """Agency display name: parent agency, or 'Parent - Sub' when a sub exists."""
    parent = (record.get("parent") or "").strip()
    sub = (record.get("sub") or "").strip()
    if parent and sub and sub != parent:
        return f"{parent} - {sub}"
    return parent or sub


# ── Source fetch ──────────────────────────────────────────────────────────────

def fetch_data(input_path=None):
    """Load the Marketplace export from a local file or the FedRAMP data repo."""
    if input_path:
        print(f"[*] Reading local export: {input_path}")
        try:
            with open(input_path, encoding="utf-8") as f:
                return json.load(f)
        except (OSError, ValueError) as e:
            print(f"[!] Could not read {input_path}: {e}", file=sys.stderr)
            return None

    print(f"[*] Fetching {DATA_URL}")
    try:
        resp = requests.get(DATA_URL, timeout=REQUEST_TIMEOUT)
        resp.raise_for_status()
        return resp.json()
    except requests.RequestException as e:
        print(f"[!] Request failed: {e}", file=sys.stderr)
        return None
    except ValueError as e:
        print(f"[!] JSON parse error: {e}", file=sys.stderr)
        return None


# ── Row builders ──────────────────────────────────────────────────────────────

def build_products(products, source_last_change):
    rows = []
    for p in products:
        product_id = (p.get("id") or "").strip()
        rows.append({
            "product_id": product_id,
            "csp": (p.get("csp") or "").strip(),
            "cso": (p.get("cso") or "").strip(),
            "status": (p.get("status") or "").strip(),
            "auth_type": (p.get("auth_type") or "").strip(),
            "impact_level": (p.get("impact_level") or "").strip(),
            "service_model": join_list(p.get("service_model")),
            "deployment_model": (p.get("deployment_model") or "").strip(),
            "business_function": join_list(p.get("business_function")),
            "reported_authorizations": p.get("authorization") or 0,
            "reported_reuses": p.get("reuse") or 0,
            "auth_date": normalize_date(p.get("auth_date")),
            "ready_date": normalize_date(p.get("ready_date")),
            "independent_assessor": (p.get("independent_assessor") or "").strip(),
            "small_business": (p.get("small_business") or "").strip(),
            "leveraged_systems": join_list(
                [s.get("cso") for s in (p.get("leveraged_systems") or []) if isinstance(s, dict)]
            ),
            "website": (p.get("website") or "").strip(),
            # The taxonomy in business_function is coarse (36 values, blank for
            # ~1 in 4 products), so the description is what makes a product
            # findable by what it actually does.
            "service_desc": collapse(p.get("service_desc")),
            "marketplace_url": product_url(product_id),
            "source_last_change": source_last_change,
        })
    rows.sort(key=lambda r: (r["csp"].lower(), r["cso"].lower()))
    return rows


def build_relationships(data, source_last_change):
    """
    Flatten every agency<->product edge in the export.

    FedRAMP spreads these across four arrays with differing completeness, so
    each row carries the array it came from:
      Agencies[].auths  -> authorization (agency issued an ATO)
      Agencies[].procs  -> in_process    (package under agency review)
      ReuseMapping      -> reuse         (agency reused an existing ATO)
      AtoMapping        -> sponsor_ato   (originating ATO, one per product)

    Only ReuseMapping and AtoMapping carry dates; the others are blank there.
    """
    products = {(p.get("id") or "").strip(): p for p in data.get("Products", [])}
    agencies = {(a.get("id") or "").strip(): a for a in data.get("Agencies", [])}
    rows = []

    def emit(agency_id, agency_record, entry, relationship, source, dates=None):
        product_id = (entry.get("id") or "").strip()
        product = products.get(product_id, {})
        dates = dates or {}
        rows.append({
            "agency_id": agency_id,
            "agency": agency_label(agency_record or entry),
            "sub_agency": (
                (agency_record or {}).get("sub") or entry.get("sub") or ""
            ).strip(),
            "relationship": relationship,
            "source": source,
            "product_id": product_id,
            # Embedded entries carry csp/cso/status; mapping rows need the join.
            "csp": (entry.get("csp") or product.get("csp") or "").strip(),
            "cso": (entry.get("cso") or product.get("cso") or "").strip(),
            "status": (entry.get("status") or product.get("status") or "").strip(),
            "impact_level": (
                entry.get("impact_level") or product.get("impact_level") or ""
            ).strip(),
            "service_model": join_list(product.get("service_model")),
            "business_function": join_list(product.get("business_function")),
            "ato_date": normalize_date(dates.get("ato_date")),
            "auth_date": normalize_date(dates.get("auth_date")),
            "exp_date": normalize_date(dates.get("exp_date")),
            "marketplace_url": product_url(product_id),
            "source_last_change": source_last_change,
        })

    for agency in data.get("Agencies", []):
        agency_id = (agency.get("id") or "").strip()
        for entry in agency.get("auths") or []:
            emit(agency_id, agency, entry, "authorization", "Agencies.auths")
        for entry in agency.get("procs") or []:
            emit(agency_id, agency, entry, "in_process", "Agencies.procs")

    for mapping in data.get("ReuseMapping", []):
        agency_id = (mapping.get("agency_id") or "").strip()
        emit(agency_id, agencies.get(agency_id), mapping, "reuse", "ReuseMapping", mapping)

    for mapping in data.get("AtoMapping", []):
        agency_id = (mapping.get("agency_id") or "").strip()
        emit(agency_id, agencies.get(agency_id), mapping, "sponsor_ato", "AtoMapping", mapping)

    rows.sort(key=lambda r: (r["agency"].lower(), r["relationship"], r["csp"].lower(), r["cso"].lower()))
    return rows


def build_agencies(data, relationship_rows, source_last_change):
    """Agency roster, with edge counts tallied from the relationship table."""
    tallies = {}
    for row in relationship_rows:
        counts = tallies.setdefault(row["agency_id"], {})
        counts[row["relationship"]] = counts.get(row["relationship"], 0) + 1

    rows = []
    for a in data.get("Agencies", []):
        agency_id = (a.get("id") or "").strip()
        counts = tallies.get(agency_id, {})
        rows.append({
            "agency_id": agency_id,
            "agency": agency_label(a),
            "sub_agency": (a.get("sub") or "").strip(),
            "authorized_products": counts.get("authorization", 0),
            "reused_products": counts.get("reuse", 0),
            "in_process_products": counts.get("in_process", 0),
            "sponsored_atos": counts.get("sponsor_ato", 0),
            "reported_authorizations": a.get("authorization") or 0,
            "reported_reuses": a.get("reuse") or 0,
            "website": (a.get("website") or "").strip(),
            "source_last_change": source_last_change,
        })
    rows.sort(key=lambda r: r["agency"].lower())
    return rows


# ── Output ────────────────────────────────────────────────────────────────────

def write_csv(output_path, rows, fieldnames):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    print(f"[+] Wrote {len(rows)} rows to {output_path}")


PRODUCT_FIELDS = [
    "product_id", "csp", "cso", "status", "auth_type", "impact_level",
    "service_model", "deployment_model", "business_function",
    "reported_authorizations", "reported_reuses", "auth_date", "ready_date",
    "independent_assessor", "small_business", "leveraged_systems", "website",
    "service_desc", "marketplace_url", "source_last_change",
]

AGENCY_FIELDS = [
    "agency_id", "agency", "sub_agency", "authorized_products", "reused_products",
    "in_process_products", "sponsored_atos", "reported_authorizations",
    "reported_reuses", "website", "source_last_change",
]

RELATIONSHIP_FIELDS = [
    "agency_id", "agency", "sub_agency", "relationship", "source", "product_id",
    "csp", "cso", "status", "impact_level", "service_model", "business_function",
    "ato_date", "auth_date", "exp_date", "marketplace_url", "source_last_change",
]


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Fetch FedRAMP Marketplace authorization data")
    parser.add_argument(
        "--data-dir",
        default="data",
        help="Root data directory to write into (default: data)",
    )
    parser.add_argument(
        "--input",
        default=None,
        help="Path to a local data.json export instead of downloading it",
    )
    args = parser.parse_args()

    payload = fetch_data(args.input)
    if payload is None:
        sys.exit(1)

    data = payload.get("data")
    if not data:
        print("[!] Export contained no 'data' object", file=sys.stderr)
        sys.exit(1)

    meta = payload.get("meta", {})
    print(f"[*] Export last changed {meta.get('last_change', 'unknown')} "
          f"(produced by {meta.get('produced_by', 'unknown')})")

    # Stamping rows with the export's own timestamp rather than the run time
    # keeps the CSVs byte-identical on days FedRAMP publishes no change, so the
    # daily job produces no commit unless the data actually moved.
    source_last_change = normalize_date(meta.get("last_change")) or datetime.now(UTC).strftime("%Y-%m-%d")
    out_dir = os.path.join(args.data_dir, "fedramp")

    product_rows = build_products(data.get("Products", []), source_last_change)
    relationship_rows = build_relationships(data, source_last_change)
    agency_rows = build_agencies(data, relationship_rows, source_last_change)

    write_csv(os.path.join(out_dir, "products.csv"), product_rows, PRODUCT_FIELDS)
    write_csv(os.path.join(out_dir, "agencies.csv"), agency_rows, AGENCY_FIELDS)
    write_csv(os.path.join(out_dir, "agency-authorizations.csv"), relationship_rows, RELATIONSHIP_FIELDS)

    breakdown = {}
    for row in relationship_rows:
        breakdown[row["relationship"]] = breakdown.get(row["relationship"], 0) + 1
    summary = ", ".join(f"{k}={v}" for k, v in sorted(breakdown.items()))
    print(f"\n[+] Done. {len(product_rows)} products, {len(agency_rows)} agencies, "
          f"{len(relationship_rows)} relationships ({summary})")


if __name__ == "__main__":
    main()
