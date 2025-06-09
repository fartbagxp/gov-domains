#!/usr/bin/env python3

import argparse
import json
import os
import requests

class CrtShClient:
  """A Python client for interacting with the crt.sh certificate search service."""

  def __init__(self):
    """Initialize the crt.sh client."""
    self.base_url = "https://crt.sh"

  def search_domain(self, domain):
    """
    Search for certificates associated with a domain.

    Args:
      domain: The domain name to search for.

    Returns:
      A list of unique domain names.
    """
    url = f"{self.base_url}?q=%.{domain}&output=json"
    try:
      response = requests.get(url, timeout=30)
      if response.status_code != 200:
        print(f"Error: Received status code {response.status_code}")
        return []

      data = response.json()
      if not data:
        print(f"No results found for domain {domain}")
        return []

      results = set()
      for cert in data:
        # Extract domain names from common_name and name_value fields
        if 'common_name' in cert and cert['common_name']:
          results.add(cert['common_name'])
        if 'name_value' in cert and cert['name_value']:
          for name in cert['name_value'].split('\n'):
            results.add(name)

      # Clean the results
      cleaned_results = self.clean_results(results)
      return cleaned_results

    except requests.exceptions.RequestException as e:
      print(f"Error making request: {e}")
      return []
    except json.JSONDecodeError:
      print("Error decoding JSON response")
      return []

  def search_organization(self, organization):
    """
    Search for certificates associated with an organization.

    Args:
      organization: The organization name to search for.

    Returns:
      A list of unique domain names.
    """
    url = f"{self.base_url}?q={organization}&output=json"
    try:
      response = requests.get(url, timeout=30)
      if response.status_code != 200:
        print(f"Error: Received status code {response.status_code}")
        return []

      data = response.json()
      if not data:
        print(f"No results found for organization {organization}")
        return []

      results = set()
      for cert in data:
        # Extract domain names from common_name field
        if 'common_name' in cert and cert['common_name']:
          results.add(cert['common_name'])

      # Clean the results
      cleaned_results = self.clean_results(results)
      return cleaned_results

    except requests.exceptions.RequestException as e:
      print(f"Error making request: {e}")
      return []
    except json.JSONDecodeError:
      print("Error decoding JSON response")
      return []

  def clean_results(self, results):
    """
    Clean and filter the results.

    Args:
      results: A set of domains to clean.

    Returns:
      A list of cleaned domain names.
    """
    cleaned = set()
    for domain in results:
      # Remove wildcard characters
      domain = domain.replace('*.', '')

      # Skip empty domains
      if not domain:
        continue

      # Skip email addresses
      if '@' in domain:
        continue

      cleaned.add(domain)

    # Return sorted list
    return sorted(cleaned)

  def save_results(self, results, filename):
    """
    Save results to a file.

    Args:
      results: List of domains to save.
      filename: Path to save the results to.
    """
    # Create output directory if it doesn't exist
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    with open(filename, 'w') as f:
      for domain in results:
        f.write(f"{domain}\n")

    print(f"\n[+] Total saved: {len(results)} domains")
    print(f"[+] Output saved in {filename}")


def main():
  """Main function to parse arguments and execute searches."""
  parser = argparse.ArgumentParser(description='crt.sh Certificate Search Client')
  group = parser.add_mutually_exclusive_group(required=True)
  group.add_argument('-d', '--domain', help='Search for a domain name')
  group.add_argument('-o', '--organization', help='Search for an organization name')
  args = parser.parse_args()

  client = CrtShClient()
  if args.domain:
    results = client.search_domain(args.domain)
    if results:
      print("\n".join(results))
      output_file = f"data/raw/domain.{args.domain}.txt"
      client.save_results(results, output_file)
    else:
      print("No valid results found.")

  elif args.organization:
    results = client.search_organization(args.organization)
    if results:
      print("\n".join(results))
      output_file = f"output/org.{args.organization}.txt"
      client.save_results(results, output_file)
    else:
      print("No valid results found.")

if __name__ == '__main__':
  main()
