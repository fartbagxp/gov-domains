#!/usr/bin/env python3

import json
import random
import time
from datetime import UTC, datetime

import requests


class CrtshError(Exception):
  """Raised when crt.sh could not be reached after exhausting all retries."""

class CrtshClient:
  """A Python client for interacting with the crt.sh certificate search service."""

  # crt.sh regularly times out, resets the connection mid-response, or answers
  # with an HTML error page instead of JSON. None of those mean "this domain has
  # no certificates", so every one of them is retried with exponential backoff
  # before the lookup is allowed to fail.
  MAX_ATTEMPTS = 5
  BACKOFF_BASE = 3
  RETRY_STATUS = frozenset({408, 429, 500, 502, 503, 504})
  TIMEOUT = 60

  def __init__(self, max_attempts=MAX_ATTEMPTS):
    self.base_url = "https://crt.sh"
    self.max_attempts = max_attempts
    self.session = requests.Session()

  def _backoff(self, attempt):
    """Sleep before the next attempt, with jitter so parallel jobs desynchronise."""
    delay = self.BACKOFF_BASE ** attempt + random.uniform(0, 1)
    print(f"[!] Retrying in {delay:.1f}s")
    time.sleep(delay)

  def search_domain(self, domain):
    """
    Search for certificates associated with a domain.

    Args:
      domain: The domain name to search for.

    Returns:
      A list of certificate dictionaries, empty if the domain genuinely has none.

    Raises:
      CrtshError: If crt.sh could not be reached after MAX_ATTEMPTS attempts.
    """
    url = f"{self.base_url}?q=%.{domain}&output=json&exclude=expired"
    last_error = None

    for attempt in range(1, self.max_attempts + 1):
      print(f"[*] Querying crt.sh for {domain} (attempt {attempt}/{self.max_attempts})")
      try:
        response = self.session.get(url, timeout=self.TIMEOUT)

        if response.status_code in self.RETRY_STATUS:
          last_error = f"status code {response.status_code}"
        elif response.status_code != 200:
          # A 4xx that is not throttling will not fix itself on a retry.
          raise CrtshError(f"crt.sh returned status code {response.status_code} for {domain}")
        else:
          data = response.json()
          if not isinstance(data, list):
            last_error = "response was not a JSON list"
          else:
            return data
      except json.JSONDecodeError:
        last_error = "malformed JSON response"
      except requests.exceptions.RequestException as e:
        last_error = str(e)

      print(f"[!] Attempt {attempt} failed for {domain}: {last_error}")
      if attempt < self.max_attempts:
        self._backoff(attempt)

    raise CrtshError(
      f"crt.sh unreachable for {domain} after {self.max_attempts} attempts: {last_error}"
    )

  def filter_expired_certificates(self, certificates):
    """
    Filter certificates to include only those that have not expired.

    Args:
      certificates: List of certificate dictionaries from crt.sh.

    Returns:
      List of non-expired certificate dictionaries.
    """
    now = datetime.now(UTC)
    unexpired_certificates = []

    for cert in certificates:
      if 'not_after' in cert:
        try:
          expiry_date = datetime.strptime(
            cert['not_after'], '%Y-%m-%dT%H:%M:%S').replace(tzinfo=UTC)
          if expiry_date > now:
            unexpired_certificates.append(cert)
        except ValueError:
          # If date parsing fails, skip this certificate
          continue
    print(f"Found {len(unexpired_certificates)} valid certificates out of {len(certificates)} total")
    return unexpired_certificates
