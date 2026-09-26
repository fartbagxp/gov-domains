#!/usr/bin/env python3
"""
Builds lists of GitHub organizations run by US federal agencies and US states.

Org discovery:
  GitHub's curated government list (the source for government.github.com)
    https://github.com/github/government.github.com/blob/gh-pages/_data/governments.yml
  CMS's allowlist of federal GitHub orgs (federal only)
    https://github.com/DSACMS/automated-codejson-generator
  Agency-published inventories of their own orgs (AGENCY_LISTS below)
  GitHub org search over agency names and acronyms (DISCOVERY_* below); a hit
  is kept only if its profile names a federal .gov/.mil domain

Agency attribution:
  Each org's profile website/email is matched against the CISA .gov registry,
  so federal orgs group under the registry's agency name and state orgs under
  the registry's state code. Orgs whose profile names no .gov/.mil domain fall
  back to OVERRIDES below.

Outputs:
  data/github/federal-orgs.csv, data/github/state-orgs.csv
  docs/github-orgs-federal.md,  docs/github-orgs-state.md
"""

import argparse
import csv
import json
import os
import re
import subprocess
import sys
import time
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor
from datetime import UTC, datetime
from urllib.parse import urlparse

import requests

GOVERNMENTS_YML_URL = "https://raw.githubusercontent.com/github/government.github.com/gh-pages/_data/governments.yml"
CMS_ALLOWLIST_URL = "https://raw.githubusercontent.com/DSACMS/automated-codejson-generator/dev/src/gov-update/allowlist.json"
# Inventories an agency publishes of its own GitHub orgs. Every org in the list
# is attributed to that agency regardless of its profile. "markdown" reads
# '| Github.com | [org] |' table rows; "json" reads a top-level "orgs" array.
AGENCY_LISTS = [
    {
        "source": "cdc-shareit",
        "url": "https://raw.githubusercontent.com/CDCgov/ShareIT-Act/main/docs/sources.md",
        "format": "markdown",
        "agency": "Department of Health and Human Services",
        "sub_organization": "Centers for Disease Control and Prevention",
    },
    {
        "source": "cms-metrics",
        "url": "https://raw.githubusercontent.com/DSACMS/metrics/main/scripts/_metadata/projects_tracked.json",
        "format": "json",
        "agency": "Department of Health and Human Services",
        "sub_organization": "Centers for Medicare and Medicaid Services",
    },
]
DOTGOV_URL = "https://raw.githubusercontent.com/cisagov/dotgov-data/main/current-full.csv"
API = "https://api.github.com"
REQUEST_TIMEOUT = 60
WORKERS = 8

FEDERAL_SECTIONS = ("U.S. Federal", "U.S. Military and Intelligence")
STATE_SECTIONS = ("U.S. States",)

UNRESOLVED = "Unresolved"
DOD = "Department of Defense"

STATES = {
    "AL": "Alabama", "AK": "Alaska", "AZ": "Arizona", "AR": "Arkansas", "CA": "California",
    "CO": "Colorado", "CT": "Connecticut", "DE": "Delaware", "DC": "District of Columbia",
    "FL": "Florida", "GA": "Georgia", "HI": "Hawaii", "ID": "Idaho", "IL": "Illinois",
    "IN": "Indiana", "IA": "Iowa", "KS": "Kansas", "KY": "Kentucky", "LA": "Louisiana",
    "ME": "Maine", "MD": "Maryland", "MA": "Massachusetts", "MI": "Michigan", "MN": "Minnesota",
    "MS": "Mississippi", "MO": "Missouri", "MT": "Montana", "NE": "Nebraska", "NV": "Nevada",
    "NH": "New Hampshire", "NJ": "New Jersey", "NM": "New Mexico", "NY": "New York",
    "NC": "North Carolina", "ND": "North Dakota", "OH": "Ohio", "OK": "Oklahoma", "OR": "Oregon",
    "PA": "Pennsylvania", "RI": "Rhode Island", "SC": "South Carolina", "SD": "South Dakota",
    "TN": "Tennessee", "TX": "Texas", "UT": "Utah", "VT": "Vermont", "VA": "Virginia",
    "WA": "Washington", "WV": "West Virginia", "WI": "Wisconsin", "WY": "Wyoming",
    "AS": "American Samoa", "GU": "Guam", "MP": "Northern Mariana Islands",
    "PR": "Puerto Rico", "VI": "U.S. Virgin Islands",
}

# Orgs whose GitHub profile names no .gov/.mil domain, attributed by hand.
# Federal values are CISA registry agency names; state values are state codes.
OVERRIDES = {
    # Federal
    "18f": "General Services Administration",
    "afrl": DOD,
    "afseo": DOD,
    "crrel": DOD,
    "m-o-s-e-s": DOD,
    "missioncommand": DOD,
    "nsacyber": DOD,
    "ozoneplatform": DOD,
    "psns-imf": DOD,
    "virtual-world-framework": DOD,
    "blue-button": "Department of Health and Human Services",
    "demand-driven-open-data": "Department of Health and Human Services",
    "hhsdigitalmediaapiplatform": "Department of Health and Human Services",
    "innovation-toolkit": "Department of Health and Human Services",
    "cfpb": "Consumer Financial Protection Bureau",
    "eregs": "Consumer Financial Protection Bureau",
    "businessusa": "Department of Commerce",
    "commercedataservice": "Department of Commerce",
    "noaa-epic": "Department of Commerce",
    "noaa-ocs-hydrography": "Department of Commerce",
    "selectusa": "Department of Commerce",
    "useda": "Department of Commerce",
    "ca-cst-library": "Department of State",
    "iip-design": "Department of State",
    "usstatedept": "Department of State",
    "navadmc": "Department of Agriculture",
    "usda-ars-ltar": "Department of Agriculture",
    "usda-ars-nwrc": "Department of Agriculture",
    "usda-ars-wmsru": "Department of Agriculture",
    "usda-fsa": "Department of Agriculture",
    "usda-nifa-b-team": "Department of Agriculture",
    "arcticlcc": "Department of the Interior",
    "imdprojects": "Department of the Interior",
    "usgs-owi": "Department of the Interior",
    "nasa-rdt": "National Aeronautics and Space Administration",
    "neogeographytoolkit": "National Aeronautics and Space Administration",
    "servir": "National Aeronautics and Space Administration",
    "petsc": "Department of Energy",
    "fedspendingtransparency": "Department of the Treasury",
    "usdepartmentoflabor": "Department of Labor",
    "usdoj": "Department of Justice",
    "nmb-dev": "National Mediation Board",
    "sbstusa": "Executive Office of the President",
    "radiofreeasia": "United States Agency for Global Media",
    "gopleader": "United States House of Representatives",
    # State
    "azgs": "AZ",
    "massgov": "MA",
    "mfwp-gis": "MT",
    "njstatelibrary": "NJ",
    "okcareertech": "OK",
    "twdb": "TX",
}

# Org search terms for federal discovery. A hit is kept only when its profile
# website/email is a federal .gov/.mil domain. Hits with no domain whose login
# starts with one of DISCOVERY_ACRONYMS (e.g. NIH-NEI, HRSA-OIT) are written out
# as review candidates instead; ambiguous acronyms and phrases never are.
DISCOVERY_ACRONYMS = [
    # HHS
    "HHS", "CDC", "FDA", "NIH", "HRSA", "SAMHSA", "AHRQ", "ACF", "ASPR", "ASPE",
    "NCI", "NLM", "NCBI", "NIAID", "NHLBI", "NCATS", "NIEHS", "NHGRI", "NIMH",
    "NIDDK", "NICHD", "NINDS", "NIDA", "CMCS", "HealthIT",
    # Commerce
    "NOAA", "NIST", "USPTO", "NTIA", "NMFS", "NESDIS", "USCensus",
    # Interior, USDA
    "USGS", "USFWS", "BOEM", "DOI", "USDA", "USFS", "NRCS", "APHIS",
    # Science, energy, space
    "NASA", "JPL", "GSFC", "NSF", "DOE", "LLNL", "ORNL", "PNNL", "LANL", "NREL",
    "LBNL", "NETL", "OSTI",
    # Defense and intelligence
    "DoD", "DARPA", "DISA", "USACE", "AFRL", "DTRA", "DLA", "NGA", "USAF", "USArmy", "USNavy",
    # Everyone else
    "EPA", "USDOT", "FAA", "FHWA", "NHTSA", "DHS", "FEMA", "CISA", "USCIS", "CBP",
    "TSA", "USCG", "IRS", "DOJ", "FBI", "DOL", "BLS", "OSHA", "HUD", "SSA", "OPM",
    "GSA", "USDS", "NARA", "GPO", "USAID", "USPS", "FCC", "FTC", "CFPB", "FDIC",
    "USGov",
]
DISCOVERY_AMBIGUOUS = [
    "CMS", "IHS", "ACL", "ONC", "VA", "SEC", "NPS", "BLM", "ARS", "NWS", "BEA",
    "army", "navy", "sandia", "argonne", "fermilab", "brookhaven", "gov",
]
DISCOVERY_PHRASES = [
    "Centers for Medicare", "Medicaid", "Administration for Children",
    "Administration for Community Living", "Indian Health Service",
    "Health Resources and Services", "Substance Abuse and Mental Health",
    "National Institutes of Health", "National Cancer Institute",
    "Food and Drug Administration", "Centers for Disease Control",
    "Health and Human Services", "National Oceanic", "National Weather Service",
    "NOAA Fisheries", "Census Bureau", "Geological Survey", "Fish and Wildlife",
    "National Park Service", "Forest Service", "Bureau of", "Department of",
    "Veterans Affairs", "Air Force", "Space Force", "Coast Guard", "Naval",
    "Army Corps", "National Laboratory", "Federal", "U.S.", "US Department",
    "United States",
]
# Review candidates must also say something government-like in their name or
# description; login prefix alone matches thousands of unrelated orgs.
GOV_WORDING = re.compile(
    r"\b(?:u\.?s\.?|united states|federal|national|department|dept|agency|administration"
    r"|bureau|office of|government|gov)\b|\.gov\b",
    re.IGNORECASE,
)
DISCOVERY_PAGES = 20  # 50 per page; GitHub search stops at 1,000 results
SEARCH_WORKERS = 4

# Listed as US federal in the source lists but not a US government org.
NOT_US_GOV = {
    "nci-agency",  # NATO Communications and Information Agency
}


# ── Fetching ──────────────────────────────────────────────────────────────────

def github_token():
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    if token:
        return token
    try:
        return subprocess.run(
            ["gh", "auth", "token"], capture_output=True, text=True, check=True
        ).stdout.strip()
    except (OSError, subprocess.CalledProcessError):
        return ""


def parse_governments_yml(text):
    """The file is a flat 'Section:' -> '  - login' mapping; no YAML lib needed."""
    sections = defaultdict(list)
    current = None
    for line in text.splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if not line[0].isspace() and line.rstrip().endswith(":"):
            current = line.rstrip()[:-1].strip()
        elif current and line.lstrip().startswith("- "):
            sections[current].append(line.lstrip()[2:].strip())
    return sections


def fetch_agency_list(session, url, fmt):
    """Org logins from an agency-published list (see AGENCY_LISTS)."""
    response = session.get(url, timeout=REQUEST_TIMEOUT)
    response.raise_for_status()
    if fmt == "json":
        return response.json()["orgs"]
    return re.findall(r"^\|\s*github\.com\s*\|\s*\[([^\]]+)\]", response.text, re.IGNORECASE | re.MULTILINE)


def load_dotgov(session):
    """Map domain -> registry row from the CISA .gov registry."""
    response = session.get(DOTGOV_URL, timeout=REQUEST_TIMEOUT)
    response.raise_for_status()
    rows = csv.DictReader(response.text.splitlines())
    return {row["Domain name"].lower(): row for row in rows}


def fetch_org(session, login):
    """Profile plus most recent push, or None if the account no longer exists."""
    response = session.get(f"{API}/orgs/{login}", timeout=REQUEST_TIMEOUT)
    if response.status_code == 404:
        response = session.get(f"{API}/users/{login}", timeout=REQUEST_TIMEOUT)
        if response.status_code == 404:
            return None
    response.raise_for_status()
    org = response.json()

    repos = session.get(
        f"{API}/users/{org['login']}/repos",
        params={"sort": "pushed", "per_page": 1, "type": "owner"},
        timeout=REQUEST_TIMEOUT,
    )
    repos.raise_for_status()
    latest = repos.json()
    org["last_push"] = latest[0]["pushed_at"][:10] if latest and latest[0].get("pushed_at") else ""
    return org


SEARCH_QUERY = """
query($q: String!, $after: String) {
  search(type: USER, query: $q, first: 50, after: $after) {
    pageInfo { hasNextPage endCursor }
    nodes {
      ... on Organization {
        login name url websiteUrl email isVerified description createdAt
        repositories(privacy: PUBLIC) { totalCount }
        latest: repositories(first: 1, privacy: PUBLIC, orderBy: {field: PUSHED_AT, direction: DESC}) {
          nodes { pushedAt }
        }
      }
    }
  }
}
"""


def graphql(session, query, variables):
    for attempt in range(5):
        response = session.post(f"{API}/graphql", json={"query": query, "variables": variables},
                                timeout=REQUEST_TIMEOUT)
        if response.status_code in (403, 429, 502, 504) and attempt < 4:
            time.sleep(int(response.headers.get("Retry-After", 30 * (attempt + 1))))
            continue
        response.raise_for_status()
        body = response.json()
        if body.get("errors") and not body.get("data"):
            raise RuntimeError(body["errors"])
        return body["data"]
    raise RuntimeError(f"GraphQL retries exhausted for {variables}")


def search_orgs(session, term):
    """Org profiles matching a search term, shaped like the REST /orgs response."""
    query = f'"{term}" type:org' if " " in term else f"{term} type:org"
    orgs, after = [], None
    for _ in range(DISCOVERY_PAGES):
        result = graphql(session, SEARCH_QUERY, {"q": query, "after": after})["search"]
        for node in result["nodes"]:
            if not node:
                continue
            pushed = node["latest"]["nodes"]
            orgs.append({
                "login": node["login"],
                "html_url": node["url"],
                "name": node["name"],
                "description": node["description"],
                "blog": node["websiteUrl"],
                "email": node["email"],
                "is_verified": node["isVerified"],
                "created_at": node["createdAt"],
                "public_repos": node["repositories"]["totalCount"],
                "last_push": pushed[0]["pushedAt"][:10] if pushed and pushed[0]["pushedAt"] else "",
            })
        if not result["pageInfo"]["hasNextPage"]:
            break
        after = result["pageInfo"]["endCursor"]
        time.sleep(1)
    return orgs


def is_federal_profile(org, dotgov):
    hosts = profile_domains(org)
    row, _ = match_dotgov(hosts, dotgov)
    if row:
        return row["Domain type"].startswith("Federal")
    return any(h.endswith(".mil") for h in hosts)


def discover_federal(session, dotgov, cache_path=None):
    """
    Search GitHub for federal orgs. Returns (found, candidates): found maps login
    -> (profile, [search terms]) for orgs with a federal domain; candidates are
    domainless orgs whose login starts with a distinctive agency acronym.
    """
    prefix = re.compile(
        r"^(?:" + "|".join(map(re.escape, DISCOVERY_ACRONYMS)) + r")(?:[-_.]|gov|$)", re.IGNORECASE
    )
    found, candidates = {}, {}
    terms = DISCOVERY_ACRONYMS + DISCOVERY_AMBIGUOUS + DISCOVERY_PHRASES
    if cache_path and os.path.exists(cache_path):
        with open(cache_path) as f:
            cached = json.load(f)
        results = [(t, cached[t]) for t in terms if t in cached]
        missing = [t for t in terms if t not in cached]
    else:
        results, missing = [], terms
    if missing:
        with ThreadPoolExecutor(SEARCH_WORKERS) as pool:
            results += list(pool.map(lambda t: (t, search_orgs(session, t)), missing))
        if cache_path:
            with open(cache_path, "w") as f:
                json.dump(dict(results), f)
    for i, (term, hits) in enumerate(results, 1):
        print(f"  [{i}/{len(terms)}] {term}: {len(hits)} results", file=sys.stderr)
        for org in hits:
            key = org["login"].lower()
            if is_federal_profile(org, dotgov):
                found.setdefault(key, (org, []))[1].append(f"search:{term}")
            elif (
                not profile_domains(org)
                and prefix.match(org["login"])
                and GOV_WORDING.search(f"{org['name'] or ''} {org['description'] or ''}")
            ):
                candidates[key] = org
    for key in found:
        candidates.pop(key, None)
    return found, candidates


# ── Attribution ───────────────────────────────────────────────────────────────

def collapse(value):
    return " ".join(value.split()) if isinstance(value, str) else ""


def profile_domains(org):
    """Hostnames from the org's website and email fields."""
    hosts = []
    blog = collapse(org.get("blog"))
    if blog:
        host = urlparse(blog if "://" in blog else f"https://{blog}").hostname
        if host:
            hosts.append(host.lower().removeprefix("www."))
    email = collapse(org.get("email"))
    if "@" in email:
        hosts.append(email.rsplit("@", 1)[1].lower())
    return hosts


def match_dotgov(hosts, dotgov):
    """First registry row whose domain is a suffix of one of the hosts."""
    for host in hosts:
        labels = host.split(".")
        for i in range(len(labels) - 1):
            row = dotgov.get(".".join(labels[i:]))
            if row:
                return row, ".".join(labels[i:])
    return None, ""


def attribute_federal(org, dotgov, cms_labels, agency_orgs):
    login = org["login"].lower()
    if login in agency_orgs:
        entry = agency_orgs[login]
        return entry["agency"], entry["sub_organization"], entry["source"]
    hosts = profile_domains(org)
    row, domain = match_dotgov(hosts, dotgov)
    if row and row["Domain type"].startswith("Federal"):
        return row["Organization name"], row["Suborganization name"], f"domain:{domain}"
    for host in hosts:
        if host.endswith(".mil"):
            return DOD, "", f"domain:{host}"
    if login in OVERRIDES:
        return OVERRIDES[login], "", "override"
    return UNRESOLVED, cms_labels.get(login, ""), ""


def attribute_state(org, dotgov):
    login = org["login"].lower()
    hosts = profile_domains(org)
    row, domain = match_dotgov(hosts, dotgov)
    if row and row["State"] in STATES:
        return row["State"], row["Organization name"], f"domain:{domain}"
    for host in hosts:
        found = re.search(r"\.(?:state\.)?([a-z]{2})\.us$", host)
        if found and found.group(1).upper() in STATES:
            return found.group(1).upper(), "", f"domain:{host}"
    if login in OVERRIDES:
        return OVERRIDES[login], "", "override"
    return UNRESOLVED, "", ""


# ── Output ────────────────────────────────────────────────────────────────────

FIELDS = [
    "group", "sub_organization", "github_org", "github_url", "display_name",
    "description", "website", "public_repos", "last_push", "created", "verified",
    "listed_in", "attributed_by",
]


def base_row(org, listed_in):
    return {
        "github_org": org["login"],
        "github_url": org["html_url"],
        "display_name": collapse(org.get("name")),
        "description": collapse(org.get("description") or org.get("bio")),
        "website": collapse(org.get("blog")),
        "public_repos": org.get("public_repos", 0),
        "last_push": org.get("last_push", ""),
        "created": (org.get("created_at") or "")[:10],
        "verified": "yes" if org.get("is_verified") else "",
        "listed_in": ";".join(listed_in),
    }


def write_csv(path, rows):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def md_cell(value, limit=None):
    value = str(value).replace("|", "\\|")
    if limit and len(value) > limit:
        value = value[: limit - 1].rstrip() + "…"
    return value


def md_table(columns, rows):
    """
    A column-aligned markdown table. columns is [(header, align)] with align
    'left' or 'right'; rows are lists of cell strings.
    """
    widths = [max([len(h), 4] + [len(str(row[i])) for row in rows]) for i, (h, _) in enumerate(columns)]

    def line(cells):
        padded = [
            str(c).rjust(w) if align == "right" else str(c).ljust(w)
            for c, w, (_, align) in zip(cells, widths, columns)
        ]
        return "| " + " | ".join(padded) + " |"

    rule = [
        ("-" * (w - 1) + ":") if align == "right" else (":" + "-" * (w - 1))
        for w, (_, align) in zip(widths, columns)
    ]
    return [line([h for h, _ in columns]), "| " + " | ".join(rule) + " |"] + [line(r) for r in rows]


def org_table(rows):
    columns = [("GitHub Org", "left"), ("Name", "left"), ("Repos", "right"),
               ("Last Push", "left"), ("Description", "left")]
    cells = [
        [
            f"[{md_cell(r['github_org'])}]({r['github_url']})",
            md_cell(r["display_name"] or r["sub_organization"], 60),
            f"{int(r['public_repos']):,}",
            r["last_push"] or "—",
            md_cell(r["description"], 100),
        ]
        for r in sorted(rows, key=lambda r: r["github_org"].lower())
    ]
    return md_table(columns, cells)


def header(title, blurb, generated):
    return [
        f"# {title}",
        "",
        blurb,
        "",
        f"_Generated {generated} by [`scripts/fetch_github_orgs.py`](../scripts/fetch_github_orgs.py)._",
        "",
    ]


def missing_section(missing):
    if not missing:
        return []
    links = ", ".join(f"`{m}`" for m in sorted(missing, key=str.lower))
    return [
        "## Listed but no longer on GitHub",
        "",
        "These logins appear in the source lists but the accounts are gone or renamed.",
        "",
        links,
        "",
    ]


def federal_markdown(rows, candidates, missing, generated):
    by_agency = defaultdict(list)
    for r in rows:
        by_agency[r["group"]].append(r)
    agencies = sorted((a for a in by_agency if a != UNRESOLVED), key=str.lower)

    out = header(
        "Federal Agency GitHub Organizations",
        "GitHub organizations run by US federal agencies, grouped by the agency that "
        "owns the org's .gov/.mil website in the [CISA .gov registry](https://github.com/cisagov/dotgov-data). "
        "Orgs come from GitHub's [government list](https://github.com/github/government.github.com/blob/gh-pages/_data/governments.yml) "
        "and CMS's [federal org allowlist](https://github.com/DSACMS/automated-codejson-generator/blob/dev/src/gov-update/allowlist.json), "
        "plus inventories agencies publish of their own orgs "
        "([CDC](https://github.com/CDCgov/ShareIT-Act/blob/main/docs/sources.md)), "
        "plus a GitHub org search over agency names and acronyms that keeps only orgs whose "
        "profile names a federal .gov/.mil domain. "
        "Data: [`data/github/federal-orgs.csv`](../data/github/federal-orgs.csv).",
        generated,
    )
    out += [
        f"**{len(rows)}** orgs across **{len(agencies)}** agencies.",
        "",
        "## Agencies",
        "",
    ]
    summary = []
    for a in agencies:
        anchor = re.sub(r"[^a-z0-9 -]", "", a.lower()).replace(" ", "-")
        repos = sum(int(r["public_repos"]) for r in by_agency[a])
        summary.append([f"[{a}](#{anchor})", f"{len(by_agency[a]):,}", f"{repos:,}"])
    out += md_table([("Agency", "left"), ("Orgs", "right"), ("Public Repos", "right")], summary)
    out.append("")

    for a in agencies:
        out += [f"### {a}", ""] + org_table(by_agency[a]) + [""]

    if by_agency.get(UNRESOLVED):
        out += [
            "## Unattributed",
            "",
            "Listed as federal, but the profile names no registered .gov/.mil domain.",
            "",
        ] + org_table(by_agency[UNRESOLVED]) + [""]

    if candidates:
        out += [
            "## Needs review",
            "",
            (
                f"{len(candidates)} orgs found by search whose login follows an agency naming pattern "
                "but whose profile names no website or email, so they can't be confirmed as official. "
                "Add real ones to `OVERRIDES` in the script. "
                "Data: [`data/github/federal-candidates.csv`](../data/github/federal-candidates.csv)."
            ),
            "",
        ]
        by_prefix = defaultdict(list)
        for r in candidates:
            by_prefix[r["group"]].append(r)
        for prefix in sorted(by_prefix, key=str.lower):
            out += [f"### {prefix or 'Other'} (review)", ""] + org_table(by_prefix[prefix]) + [""]

    out += missing_section(missing)
    return "\n".join(out)


def state_markdown(rows, missing, generated):
    by_state = defaultdict(list)
    for r in rows:
        by_state[r["group"]].append(r)
    with_orgs = [c for c in STATES if by_state.get(c)]

    out = header(
        "State Government GitHub Organizations",
        "GitHub organizations run by US state and territory governments, from GitHub's "
        "[government list](https://github.com/github/government.github.com/blob/gh-pages/_data/governments.yml) "
        "(U.S. States section). Each org is placed by the state of its .gov website in the "
        "[CISA .gov registry](https://github.com/cisagov/dotgov-data). "
        "Data: [`data/github/state-orgs.csv`](../data/github/state-orgs.csv).",
        generated,
    )
    out += [
        f"**{len(rows)}** orgs across **{len(with_orgs)}** of {len(STATES)} states and territories.",
        "",
        "## Coverage",
        "",
    ]
    coverage = []
    for code, name in sorted(STATES.items(), key=lambda kv: kv[1]):
        orgs = sorted(by_state.get(code, []), key=lambda r: r["github_org"].lower())
        links = ", ".join(f"[{r['github_org']}]({r['github_url']})" for r in orgs) or "—"
        coverage.append([f"{name} ({code})", f"{len(orgs)}", links])
    out += md_table([("State", "left"), ("Count", "right"), ("Orgs", "left")], coverage)
    out.append("")

    for code in sorted(with_orgs, key=STATES.get):
        out += [f"### {STATES[code]}", ""] + org_table(by_state[code]) + [""]

    if by_state.get(UNRESOLVED):
        out += [
            "## Unattributed",
            "",
            "Listed under U.S. States, but no state could be determined from the profile.",
            "",
        ] + org_table(by_state[UNRESOLVED]) + [""]
    out += missing_section(missing)
    return "\n".join(out)


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Build federal and state GitHub org lists")
    parser.add_argument("--data-dir", default="data/github")
    parser.add_argument("--docs-dir", default="docs")
    parser.add_argument("--no-search", action="store_true", help="skip GitHub org search discovery")
    parser.add_argument(
        "--search-cache",
        help="JSON file of raw search results; reused if present, written otherwise (search takes ~1 hour)",
    )
    args = parser.parse_args()

    session = requests.Session()
    session.headers["Accept"] = "application/vnd.github+json"
    token = github_token()
    if token:
        session.headers["Authorization"] = f"Bearer {token}"
    else:
        print("warning: no GitHub token; unauthenticated rate limit is 60/hour", file=sys.stderr)

    response = session.get(GOVERNMENTS_YML_URL, timeout=REQUEST_TIMEOUT)
    response.raise_for_status()
    sections = parse_governments_yml(response.text)

    response = session.get(CMS_ALLOWLIST_URL, timeout=REQUEST_TIMEOUT)
    response.raise_for_status()
    cms_labels = {k.lower(): v for k, v in response.json()["githubOrgs"].items()}

    dotgov = load_dotgov(session)

    # login (lowercased) -> (login as listed, [sources])
    federal, state = {}, {}
    for section in FEDERAL_SECTIONS:
        for login in sections.get(section, []):
            federal.setdefault(login.lower(), (login, []))[1].append("governments.yml")
    for login in cms_labels:
        federal.setdefault(login, (login, []))[1].append("cms-allowlist")
    agency_orgs = {}
    for entry in AGENCY_LISTS:
        for login in fetch_agency_list(session, entry["url"], entry["format"]):
            agency_orgs[login.lower()] = entry
            federal.setdefault(login.lower(), (login, []))[1].append(entry["source"])
    found, candidates = {}, {}
    if not args.no_search:
        print("Searching GitHub for federal orgs...", file=sys.stderr)
        found, candidates = discover_federal(session, dotgov, args.search_cache)
        # Candidates confirmed by hand in OVERRIDES join the main list.
        for key in [k for k in candidates if k in OVERRIDES]:
            found[key] = (candidates.pop(key), ["override"])
    for key, (org, _terms) in found.items():
        federal.setdefault(key, (org["login"], []))[1].append("search")
    for login in NOT_US_GOV:
        federal.pop(login, None)
        candidates.pop(login, None)
    for section in STATE_SECTIONS:
        for login in sections.get(section, []):
            state.setdefault(login.lower(), (login, []))[1].append("governments.yml")

    # Search results already carry full profiles; fetch only the listed orgs.
    profiles = {key: org for key, (org, _terms) in found.items()}
    logins = sorted(
        {v[0] for v in federal.values()} | {v[0] for v in state.values()}, key=str.lower
    )
    logins = [login for login in logins if login.lower() not in profiles]
    print(f"Fetching {len(logins)} GitHub accounts...", file=sys.stderr)
    with ThreadPoolExecutor(WORKERS) as pool:
        profiles.update(zip((l.lower() for l in logins), pool.map(lambda l: fetch_org(session, l), logins)))

    generated = datetime.now(UTC).strftime("%Y-%m-%d")

    # Renamed orgs can surface twice (old and new login); keep the first.
    fed_rows, fed_missing, seen = [], [], set()
    for key, (login, sources) in sorted(federal.items()):
        org = profiles[key]
        if org is None:
            fed_missing.append(login)
            continue
        if org["login"].lower() in seen:
            continue
        seen.add(org["login"].lower())
        agency, sub, how = attribute_federal(org, dotgov, cms_labels, agency_orgs)
        fed_rows.append({"group": agency, "sub_organization": sub, "attributed_by": how, **base_row(org, sources)})

    acronym = {a.lower(): a for a in DISCOVERY_ACRONYMS}
    candidate_rows = []
    for key, org in candidates.items():
        if key in seen:
            continue
        head = re.match(r"[a-z]+", key).group(0)
        group = next((acronym[p] for p in sorted(acronym, key=len, reverse=True) if head.startswith(p)), "")
        candidate_rows.append({"group": group, "sub_organization": "", "attributed_by": "",
                               **base_row(org, ["search"])})

    state_rows, state_missing, seen = [], [], set()
    for key, (login, sources) in sorted(state.items()):
        org = profiles[key]
        if org is None:
            state_missing.append(login)
            continue
        if org["login"].lower() in seen:
            continue
        seen.add(org["login"].lower())
        code, sub, how = attribute_state(org, dotgov)
        state_rows.append({"group": code, "sub_organization": sub, "attributed_by": how, **base_row(org, sources)})

    def sort_key(r):
        return (r["group"] == UNRESOLVED, r["group"].lower(), r["github_org"].lower())

    fed_rows.sort(key=sort_key)
    candidate_rows.sort(key=sort_key)
    state_rows.sort(key=sort_key)

    write_csv(os.path.join(args.data_dir, "federal-orgs.csv"), fed_rows)
    write_csv(os.path.join(args.data_dir, "state-orgs.csv"), state_rows)
    if not args.no_search:
        write_csv(os.path.join(args.data_dir, "federal-candidates.csv"), candidate_rows)
    os.makedirs(args.docs_dir, exist_ok=True)
    with open(os.path.join(args.docs_dir, "github-orgs-federal.md"), "w") as f:
        f.write(federal_markdown(fed_rows, candidate_rows, fed_missing, generated))
    with open(os.path.join(args.docs_dir, "github-orgs-state.md"), "w") as f:
        f.write(state_markdown(state_rows, state_missing, generated))

    for label, rows, missing in (("federal", fed_rows, fed_missing), ("state", state_rows, state_missing)):
        unresolved = [r["github_org"] for r in rows if r["group"] == UNRESOLVED]
        print(f"{label}: {len(rows)} orgs, {len(unresolved)} unattributed, {len(missing)} missing", file=sys.stderr)
        if label == "federal":
            print(f"  {len(found)} found by search, {len(candidate_rows)} review candidates", file=sys.stderr)
        if unresolved:
            print(f"  unattributed: {' '.join(unresolved)}", file=sys.stderr)


if __name__ == "__main__":
    main()
