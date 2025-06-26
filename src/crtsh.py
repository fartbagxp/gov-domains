#!/usr/bin/env python3

import json
import requests
from datetime import datetime

class CrtshClient:
  """A Python client for interacting with the crt.sh certificate search service."""

  def __init__(self):
    self.base_url = "https://crt.sh"

  def search_domain(self, domain):
    """
    Search for certificates associated with a domain.

    Args:
      domain: The domain name to search for.

    Returns:
      A list of unique domain names.
    """
    url = f"{self.base_url}?q=%.{domain}&output=json&exclude=expired"
    try:
      response = requests.get(url, timeout=30)
      if response.status_code != 200:
        print(f"Error: Received status code {response.status_code}")
        return []
      data = response.json()
      if not data:
        print(f"No results found for domain {domain}")
        return []
      return data
    except requests.exceptions.RequestException as e:
      print(f"Error making request: {e}")
      return []
    except json.JSONDecodeError:
      print("Error decoding JSON response")
      return []

  def filter_expired_certificates(self, certificates):
    """
    Filter certificates to include only those that have not expired.

    Args:
      certificates: List of certificate dictionaries from crt.sh.

    Returns:
      List of non-expired certificate dictionaries.
    """
    now = datetime.now(datetime.timezone.utc)
    unexpired_certificates = []

    for cert in certificates:
      if 'not_after' in cert:
        try:
          expiry_date = datetime.strptime(cert['not_after'], '%Y-%m-%dT%H:%M:%S')
          if expiry_date > now:
            unexpired_certificates.append(cert)
        except ValueError:
          # If date parsing fails, skip this certificate
          continue
    print(f"Found {len(unexpired_certificates)} valid certificates out of {len(certificates)} total")
    return unexpired_certificates
