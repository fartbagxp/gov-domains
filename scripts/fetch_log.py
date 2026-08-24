#!/usr/bin/env python3
"""
Track when each domain was last successfully fetched from crt.sh.

The weekly pipeline needs to know which domains to revisit mid-week. Git history
cannot answer that: `git log` reports when a raw file last *changed*, and a
domain whose certificates were stable produces no commit even though the fetch
succeeded. So successful fetches are recorded explicitly in a small JSON log
that lives alongside the data.

  --record <artifacts-dir>  stamp every domain present in the dir as fetched now
  --stale                   print domains that are missing or older than the window
"""

import argparse
import json
import os
import sys
from datetime import UTC, datetime, timedelta

FETCH_LOG = "data/raw/fetch-log.json"
RAW_DIR = "data/raw"

def load_log(path=FETCH_LOG):
  """Read the fetch log, tolerating a missing or corrupt file."""
  if not os.path.exists(path):
    return {}
  try:
    with open(path, encoding='utf-8') as f:
      data = json.load(f)
    return data if isinstance(data, dict) else {}
  except json.JSONDecodeError:
    print(f"[!] {path} is not valid JSON; starting a fresh log", file=sys.stderr)
    return {}

def save_log(log, path=FETCH_LOG):
  os.makedirs(os.path.dirname(path), exist_ok=True)
  with open(path, 'w', encoding='utf-8') as f:
    json.dump(dict(sorted(log.items())), f, indent=2)
    f.write("\n")

def read_domains(path):
  """Read the tracked domain list, skipping blanks and comments."""
  domains = []
  with open(path, encoding='utf-8') as f:
    for line in f:
      line = line.strip()
      if line and not line.startswith('#'):
        domains.append(line)
  return domains

def record(artifacts_dir):
  """Stamp every domain whose file landed in artifacts_dir as fetched now."""
  log = load_log()
  now = datetime.now(UTC).replace(microsecond=0).isoformat()

  recorded = 0
  for name in sorted(os.listdir(artifacts_dir)) if os.path.isdir(artifacts_dir) else []:
    if not (name.startswith("domain.") and name.endswith(".json")):
      continue
    domain = name[len("domain."):-len(".json")]
    log[domain] = now
    recorded += 1

  save_log(log)
  print(f"[+] Recorded {recorded} successful fetch(es) in {FETCH_LOG}")

def stale(domains_file, stale_after_days):
  """Print the domains that need re-fetching, one per line."""
  log = load_log()
  cutoff = datetime.now(UTC) - timedelta(days=stale_after_days)

  for domain in read_domains(domains_file):
    raw_file = os.path.join(RAW_DIR, f"domain.{domain}.json")
    last_fetched = log.get(domain)

    if not os.path.exists(raw_file):
      reason = "no data file"
    elif last_fetched is None:
      reason = "never recorded"
    else:
      try:
        if datetime.fromisoformat(last_fetched) >= cutoff:
          continue
        reason = f"last fetched {last_fetched}"
      except ValueError:
        reason = f"unparseable timestamp {last_fetched!r}"

    print(domain)
    print(f"  {domain}: {reason}", file=sys.stderr)

def main():
  parser = argparse.ArgumentParser(description=__doc__,
    formatter_class=argparse.RawDescriptionHelpFormatter)
  group = parser.add_mutually_exclusive_group(required=True)
  group.add_argument('--record', metavar='ARTIFACTS_DIR',
    help='Mark every domain file found in this directory as freshly fetched')
  group.add_argument('--stale', action='store_true',
    help='List domains that are missing or older than the staleness window')
  parser.add_argument('--domains-file', default='config/domains.txt',
    help='Domain list to check against (default: config/domains.txt)')
  parser.add_argument('--stale-after-days', type=float, default=4.0,
    help='Age in days past which a domain counts as stale (default: 4)')
  args = parser.parse_args()

  if args.record:
    record(args.record)
  else:
    stale(args.domains_file, args.stale_after_days)

if __name__ == '__main__':
  main()
