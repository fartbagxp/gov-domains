import argparse
import csv
import json
import os

from datetime import datetime
from src.crtsh import CrtshClient

def save_raw_json(data, filename):
  os.makedirs(os.path.dirname(filename), exist_ok=True)
  with open(filename, 'w') as f:
    json.dump(data, f, indent=2)
  print(f"[+] Raw JSON data saved to {filename}")

def extract_domains_from_certificates(certificates):
  """
  Extract unique domains from certificates.

  Args:
    certificates: List of certificate dictionaries.

  Returns:
    Dictionary of normalized domain data.
  """
  domains_data = {}

  for cert in certificates:
    cert_id = cert.get('id', 'unknown')
    issuer_name = cert.get('issuer_name', 'unknown')
    not_before = cert.get('not_before', '')
    not_after = cert.get('not_after', '')

    # Extract domains from common_name
    if 'common_name' in cert and cert['common_name']:
      domain = cert['common_name'].replace('*.', '')
      if domain and '@' not in domain:
        if domain not in domains_data:
          domains_data[domain] = {
            'domain': domain,
            'seen_in_common_name': 'Yes',
            'seen_in_name_value': 'No',
            'certificate_ids': set(),
            'issuers': set(),
            'earliest_seen': not_before,
            'latest_expiry': not_after
          }
        domains_data[domain]['certificate_ids'].add(str(cert_id))
        domains_data[domain]['issuers'].add(issuer_name)

        # Update earliest/latest dates if necessary
        if not_before and (not domains_data[domain]['earliest_seen'] or not_before < domains_data[domain]['earliest_seen']):
          domains_data[domain]['earliest_seen'] = not_before
        if not_after and (not domains_data[domain]['latest_expiry'] or not_after > domains_data[domain]['latest_expiry']):
          domains_data[domain]['latest_expiry'] = not_after

    # Extract domains from name_value
    if 'name_value' in cert and cert['name_value']:
      for name in cert['name_value'].split('\n'):
        domain = name.replace('*.', '')
        if domain and '@' not in domain:
          if domain not in domains_data:
            domains_data[domain] = {
              'domain': domain,
              'seen_in_common_name': 'No',
              'seen_in_name_value': 'Yes',
              'certificate_ids': set(),
              'issuers': set(),
              'earliest_seen': not_before,
              'latest_expiry': not_after
            }
          else:
            domains_data[domain]['seen_in_name_value'] = 'Yes'

          domains_data[domain]['certificate_ids'].add(str(cert_id))
          domains_data[domain]['issuers'].add(issuer_name)

          # Update earliest/latest dates if necessary
          if not_before and (not domains_data[domain]['earliest_seen'] or not_before < domains_data[domain]['earliest_seen']):
            domains_data[domain]['earliest_seen'] = not_before
          if not_after and (not domains_data[domain]['latest_expiry'] or not_after > domains_data[domain]['latest_expiry']):
            domains_data[domain]['latest_expiry'] = not_after

  return domains_data

def save_domains_to_csv(domains_data, filename):
  """
  Save normalized domain data to CSV.

  Args:
    domains_data: Dictionary of domain information.
    filename: Path to save the CSV file to.
  """
  os.makedirs(os.path.dirname(filename), exist_ok=True)

  with open(filename, 'w', newline='') as csvfile:
    fieldnames = ['domain', 'seen_in_common_name', 'seen_in_name_value',
                  'certificate_count', 'issuer_count', 'earliest_seen', 'latest_expiry',
                  'certificate_ids', 'issuers']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for domain, data in sorted(domains_data.items()):
      row = {
        'domain': data['domain'],
        'seen_in_common_name': data['seen_in_common_name'],
        'seen_in_name_value': data['seen_in_name_value'],
        'certificate_count': len(data['certificate_ids']),
        'issuer_count': len(data['issuers']),
        'earliest_seen': data['earliest_seen'],
        'latest_expiry': data['latest_expiry'],
        'certificate_ids': ';'.join(data['certificate_ids']),
        'issuers': ';'.join(data['issuers'])
      }
      writer.writerow(row)

  print(f"[+] Normalized domain data saved to {filename}")
  print(f"[+] Total domains: {len(domains_data)}")

def filter_valid_certificates(certificates):
  """
  Filter certificates to include only those that have not expired.

  Args:
    certificates: List of certificate dictionaries from crt.sh.

  Returns:
    List of non-expired certificate dictionaries.
  """
  now = datetime.utcnow()
  valid_certificates = []

  for cert in certificates:
    if 'not_after' in cert:
      try:
        expiry_date = datetime.strptime(cert['not_after'], '%Y-%m-%dT%H:%M:%S')
        if expiry_date > now:
          valid_certificates.append(cert)
      except ValueError:
        # If date parsing fails, skip this certificate
        continue

  print(f"Found {len(valid_certificates)} valid certificates out of {len(certificates)} total")
  return valid_certificates

def process_raw_json_file(input_file):
  """
  Process a raw JSON file, filter for valid certificates, and extract domains.

  Args:
    input_file: Path to the raw JSON file.

  Returns:
    Dictionary of normalized domain data.
  """
  try:
    with open(input_file, 'r') as f:
      data = json.load(f)

    print(f"Loaded {len(data)} certificates from {input_file}")

    # Filter for valid certificates
    valid_certs = filter_valid_certificates(data)

    # Extract domains
    domains_data = extract_domains_from_certificates(valid_certs)

    return domains_data

  except (json.JSONDecodeError, FileNotFoundError) as e:
    print(f"Error processing file {input_file}: {str(e)}")
    return {}


def main():
  parser = argparse.ArgumentParser(description='crt.sh Certificate Search Client')
  group = parser.add_mutually_exclusive_group(required=True)
  group.add_argument('-d', '--domain', help='Search for a domain name')
  group.add_argument('-p', '--process-file', help='Process an existing raw JSON file')
  args = parser.parse_args()

  client = CrtshClient()
  if args.domain:
    results = client.search_domain(args.domain)
    if results:
      output_file = f"data/raw/domain.{args.domain}.json"
      save_raw_json(results, output_file)

  elif args.process_file:
    input_file = args.process_file
    base_filename = os.path.splitext(os.path.basename(input_file))[0]

    domains_data = process_raw_json_file(input_file)

    if domains_data:
      csv_output = f"data/processed/{base_filename}.csv"
      save_domains_to_csv(domains_data, csv_output)

if __name__ == '__main__':
  main()
