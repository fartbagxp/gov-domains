from ipwhois import IPWhois
from ipwhois.net import Net
from ipwhois.asn import IPASN
from pprint import pprint

def whois(ip):
  obj = IPWhois(ip)
  results = obj.lookup_rdap(depth=1,retry_count=5,rate_limit_timeout=5)

  results_stripped = {
    "asn": results.get("asn"),
    "asn_cidr": results.get("asn_cidr"),
    "asn_country_code": results.get("asn_country_code"),
    "asn_date": results.get("asn_date"),
    "asn_description": results.get("asn_description"),
    "asn_registry": results.get("asn_registry"),
    "entities": results.get("entities"),
    "net_start_address": results.get("network").get("cidr"),
    "net_end_address": results.get("network").get("end_address"),
    "net_cidr": results.get("network").get("cidr"),
    "net_type": results.get("network").get("type"),
    "net_organization": results.get("network").get("name"),
    "net_ref": results.get("network").get("links"),
    "raw_command": f"whois -h whois.radb.net {ip}"
  }

  if results.get("network") is not None:
    if results.get("network").get("events") is not None:
      for event in results.get("network").get("events"):
        if event.get("action") == "last changed":
          results_stripped["net_updated"] = event["timestamp"]
        elif event.get("action") == "registration":
          results_stripped["registration"] = event["timestamp"]

  return results_stripped

def whois_asn(asn):
  net = Net('2001:1234:1234::')
  obj = IPASN(net)
  results = obj.lookup(asn=asn)
  return results


def main():
  # result = whois('127.0.0.1')
  # pprint(result)
  # result = whois('213.199.183.0')
  # pprint(result)
  # result = whois('35.180.0.0')
  # pprint(result)
  result = whois_asn('AS26810')
  pprint(result)

if __name__ == "__main__":
  main()
