[![Last Sync](https://github.com/fartbagxp/gov-domains/actions/workflows/update_sites_raw.yml/badge.svg)](https://github.com/fartbagxp/gov-domains/actions/workflows/update_sites_raw.yml)

# Overview

This repository answers a couple questions about public government domains.

    What technology do public government websites use?
    What is already allowed?
    What can I use, based on precedence?

The intention is to understand what federal agencies or state or city government are using as their technology stack, including edge technologies, network setup, and backend hosting.

## Sources of Information

- https://ipinfo.io/countries/us
- RADB - `whois -h whois.radb.net -- '-i origin AS32934' | grep ^route`
