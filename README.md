# gov-domains

This repository will be used to track government domains and AS as an information portal.

The goal of this repository is to be able to quickly understand what federal agencies are using as their edge network environment.

## Sources of Information

- https://ipinfo.io/countries/us
- RADB - `whois -h whois.radb.net -- '-i origin AS32934' | grep ^route`

## Running precommit

`pre-commit run --all-files`
