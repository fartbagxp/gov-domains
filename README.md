# gov-domains

Tracking technology stacks, IP address ranges, and autonomous system numbers (ASNs) for US federal agencies, state and city governments, and the broader health industry.

## Pipeline Status

| Workflow | Status |
| :--- | :--- |
| Nightly domain scan | [![Site Update](https://github.com/fartbagxp/gov-domains/actions/workflows/update_sites_raw.yml/badge.svg)](https://github.com/fartbagxp/gov-domains/actions/workflows/update_sites_raw.yml) |
| Technology detection | [![Technology](https://github.com/fartbagxp/gov-domains/actions/workflows/update_technology.yml/badge.svg)](https://github.com/fartbagxp/gov-domains/actions/workflows/update_technology.yml) |
| ASN & IP prefix collection | [![ASN Prefixes](https://github.com/fartbagxp/gov-domains/actions/workflows/update_asn_prefixes.yml/badge.svg)](https://github.com/fartbagxp/gov-domains/actions/workflows/update_asn_prefixes.yml) |
| README update | [![README](https://github.com/fartbagxp/gov-domains/actions/workflows/update_readme.yml/badge.svg)](https://github.com/fartbagxp/gov-domains/actions/workflows/update_readme.yml) |
| Lint | [![Lint](https://github.com/fartbagxp/gov-domains/actions/workflows/lint.yml/badge.svg)](https://github.com/fartbagxp/gov-domains/actions/workflows/lint.yml) |

<!-- BEGIN:timestamp -->
_Last updated: 2026-07-13 09:10 UTC_
<!-- END:timestamp -->

---

## Overview

This repository answers a few questions about public government and health-sector infrastructure:

- What technology stacks do government websites use?
- What IP address ranges do federal, state, and city agencies own?
- How does the health industry (hospitals, insurers, PBMs, EHR vendors) compare in network footprint?

Data is collected automatically on a regular schedule and committed back to this repository.

---

## Data Sources

| Source | Description |
| :--- | :--- |
| [crt.sh](https://crt.sh) | Certificate transparency logs — used to discover subdomains |
| [httpx](https://github.com/projectdiscovery/httpx) | Active HTTP probing — technology fingerprinting per domain |
| [RIPE Stat](https://stat.ripe.net) | BGP-announced IP prefixes per ASN |
| [ARIN / RIR delegation files](https://ftp.arin.net/pub/stats/arin/) | Official ASN registry, org names, assignment dates |
| [bgp.potaroo.net autnums](https://bgp.potaroo.net/cidr/autnums.html) | ASN → organization name lookup |
| [CISA dotgov-data](https://github.com/cisagov/dotgov-data) | Authoritative list of .gov domain registrants |

---

## Coverage Summary

<!-- BEGIN:overview-table -->
| Category                      | Organizations | ASNs | IPv4 Prefixes | IPv6 Prefixes | Est. IPv4 Addresses |
| :---                          | ---:          | ---: | ---:          | ---:          | ---:                |
| **Federal Agencies**          |            87 |   87 |         7,993 |           257 |              321.4M |
| **State Governments**         |            85 |   85 |         1,887 |            56 |               13.8M |
| **City Governments**          |            53 |   53 |           426 |            10 |                1.4M |
| **Hospital Systems**          |           544 |  544 |         1,644 |            18 |                4.9M |
| **Health Insurers**           |            76 |   76 |           456 |             5 |              638.7K |
| **Pharmacy Benefit Managers** |            13 |   13 |            90 |             — |              200.7K |
| **Health IT Vendors**         |            40 |   40 |           116 |             6 |               77.1K |
| **Academic Institutions**     |            20 |   20 |         1,231 |           107 |               27.3M |
<!-- END:overview-table -->

---

## Federal Agencies

Tracked in [`data/us-fed-gov-agencies.csv`](data/us-fed-gov-agencies.csv). Prefix data collected in [`data/asn/fed-gov-prefixes.csv`](data/asn/fed-gov-prefixes.csv).

<!-- BEGIN:fed-gov-table -->
| Abbrev  | Agency                                                 | ASNs | IPv4 Prefixes | IPv6 Prefixes | Est. IPv4 Addresses |
| :---    | :---                                                   | ---: | ---:          | ---:          | ---:                |
| AF      | Air Force Systems Networking                           |    2 |             — |             — |                   — |
| CBO     | Congressional Budget Office                            |    1 |             5 |             — |                1.3K |
| CDC     | Centers for Disease Control and Prevention (CDC)       |    1 |             2 |             — |               73.7K |
| CIA     | Central Intelligence Agency                            |    1 |             — |             — |                   — |
| CNCS    | AmeriCorps                                             |    1 |             — |             — |                   — |
| DHS     | Department of Homeland Security                        |    1 |             9 |             1 |               14.1K |
| DOC     | Department of Commerce - Bureau of Economic Analysis   |    3 |             3 |             3 |               66.0K |
| DOS-OIG | Department of State - Office of Inspector General      |    1 |             — |             1 |                   — |
| DoD     | Department of Defense - Network Information Center     |   10 |         7,269 |            95 |              314.8M |
| DoL     | U.S. Department of Labor                               |    2 |            14 |            13 |                3.8K |
| DoT     | US Department of Transportation                        |    1 |            20 |            30 |              269.3K |
| EOP     | Executive Office of the President                      |    2 |             7 |             4 |               67.3K |
| EPA     | Environmental Protection Agency (EPA)                  |    2 |             4 |             1 |              262.4K |
| EXIM    | Export-Import Bank of the United States                |    1 |             — |             — |                   — |
| FAA     | Federal Aviation Administration                        |    2 |            18 |             6 |              203.5K |
| FBI     | Federal Bureau of Investigation - CJIS Division        |    1 |            29 |            13 |              137.7K |
| FDA     | Food and Drug Administration                           |    1 |             1 |             1 |               65.5K |
| FDIC    | Federal Deposit Insurance Corporation                  |    1 |            13 |             — |                3.3K |
| FEC     | Federal Election Commission                            |    1 |             — |             — |                   — |
| FERC    | Federal Energy Regulatory Commission                   |    1 |             6 |             — |                5.4K |
| FMSHRC  | Federal Mine Safety and Health Review Commission       |    1 |             — |             — |                   — |
| FRB     | Federal Reserve Bank                                   |    2 |             8 |             — |               68.6K |
| FTC     | Federal Trade Commission                               |    1 |            35 |             — |               79.9K |
| GAO     | Government Accountability Office                       |    1 |             — |             — |                   — |
| GPO     | Government Publishing Office                           |    1 |             2 |             — |               67.6K |
| GSA     | General Services Administration (GSA)                  |    1 |             — |             — |                   — |
| HHS     | US Department of Health and Human Services             |    4 |            30 |             6 |              382.2K |
| HHS-OIG | HHS Office of Inspector General                        |    1 |             — |             — |                   — |
| HUD-OIG | HUD Office of Inspector General                        |    1 |             1 |             1 |                 256 |
| IHS     | Indian Health Service                                  |    1 |             9 |             2 |               68.1K |
| IRS     | Internal Revenue Service                               |    1 |            13 |             4 |               13.6K |
| LOC     | Library of Congress                                    |    1 |             1 |             — |               65.5K |
| NARA    | National Archives and Records Administration           |    1 |             5 |             — |               16.9K |
| NASA    | National Aeronautics and Space Administration (NASA)   |    2 |           218 |             1 |                3.0M |
| NCUA    | National Credit Union Administration                   |    1 |             4 |             — |                1.3K |
| NGA     | National Gallery of Art                                |    1 |             1 |             — |                4.1K |
| NIH     | National Institutes of Health                          |    2 |            27 |             1 |              359.2K |
| NIST    | National Institute of Standards and Technology         |    1 |            29 |             7 |               81.7K |
| NOAA    | National Oceanic and Atmospheric Administration (NOAA) |    2 |            85 |            26 |              337.9K |
| NRC     | Nuclear Regulatory Commission                          |    1 |             5 |             8 |                1.5K |
| NSF     | National Science Foundation                            |    2 |             3 |             1 |               66.0K |
| OPM     | Office of Personnel Management                         |    1 |             — |             — |                   — |
| PBGC    | Pension Benefit Guaranty Corporation                   |    1 |             2 |             — |                 512 |
| PC      | Peace Corps                                            |    1 |             1 |             6 |                 256 |
| SBA     | Small Business Administration                          |    1 |             2 |             — |                 512 |
| SEC     | U.S. Securities and Exchange Commission                |    1 |            29 |             1 |               15.1K |
| SI      | Smithsonian Institution                                |    1 |             6 |             1 |               63.7K |
| SSA     | Social Security Administration                         |    1 |            13 |             6 |               54.0K |
| SSS     | Selective Service System                               |    1 |             — |             — |                   — |
| STB     | Surface Transportation Board                           |    1 |             — |             — |                   — |
| USAID   | U.S. Agency for International Development              |    2 |             1 |             1 |                 256 |
| USAISC  | United States (USAISC)                                 |    3 |             — |             — |                   — |
| USDA    | Department of Agriculture                              |    1 |             — |             — |                   — |
| USHMM   | United States Holocaust Memorial Museum                |    1 |             1 |             — |                 256 |
| USPS    | United States Postal Service (USPS)                    |    3 |            34 |             2 |              335.4K |
| USPTO   | United States Patent and Trademark Office              |    1 |             3 |             7 |                6.1K |
| VA      | Department of Veterans Affairs                         |    2 |            25 |             8 |              332.8K |
<!-- END:fed-gov-table -->

---

## State Governments

Tracked in [`data/us-state-gov-agencies.csv`](data/us-state-gov-agencies.csv). Prefix data in [`data/asn/state-gov-prefixes.csv`](data/asn/state-gov-prefixes.csv).

<!-- BEGIN:state-gov-table -->
| St   | Organization                                               | ASNs | IPv4 Prefixes | IPv6 Prefixes | Est. IPv4 Addresses |
| :--- | :---                                                       | ---: | ---:          | ---:          | ---:                |
| AK   | State of Alaska                                            |    1 |            14 |             — |              134.3K |
| AL   | State of Alabama Office of Information Technology          |    1 |            16 |             — |                4.1K |
| AR   | State of Arkansas                                          |    1 |            12 |             — |              370.4K |
| AZ   | State of Arizona                                           |    1 |            17 |             — |              265.2K |
| CA   | California Department of Technology                        |    1 |             — |             — |                   — |
| CA   | State of California Department of Food and Agriculture     |    1 |             — |             — |                   — |
| CA   | State of California Department of Motor Vehicles           |    1 |             — |             — |                   — |
| CA   | State of California Department of Technology               |    3 |            35 |             1 |                1.0M |
| CO   | Governor's Office of Information Technology                |    1 |             4 |             — |              131.6K |
| CT   | State of Connecticut Department of Information Technology  |    1 |            16 |             — |               63.2K |
| CT   | State of Connecticut Judicial Branch                       |    1 |            15 |             1 |                3.8K |
| DE   | State of Delaware                                          |    1 |             2 |             1 |               65.5K |
| FL   | Florida Department of Management Services                  |    1 |           806 |            22 |              897.0K |
| GA   | Georgia Technology Authority                               |    2 |             7 |             — |              591.1K |
| HI   | State of Hawaii                                            |    1 |            10 |             — |                6.1K |
| IA   | Iowa Communications Network                                |    1 |            14 |             3 |              386.8K |
| IA   | State of Iowa OCIO                                         |    1 |             2 |             — |                2.0K |
| ID   | State of Idaho                                             |    3 |            12 |             1 |              132.4K |
| ID   | State of Idaho Department of Health and Welfare            |    1 |             1 |             — |                 512 |
| IL   | Illinois Century Network                                   |    1 |            81 |             5 |                1.7M |
| IN   | Indiana Office of Technology                               |    1 |             4 |             1 |                8.2K |
| IN   | State of Indiana                                           |    1 |             — |             — |                   — |
| KS   | State of Kansas                                            |    1 |             2 |             — |               65.8K |
| KY   | Commonwealth of Kentucky Department of Information Systems |    1 |             7 |             — |              164.9K |
| KY   | Kentucky Communications Network Authority                  |    1 |             4 |             — |                1.8K |
| LA   | State of Louisiana Office of Technology Services           |    2 |           100 |             — |              314.1K |
| LA   | State of Louisiana Supreme Court                           |    1 |             1 |             — |                 512 |
| MA   | Commonwealth of Massachusetts                              |    1 |            13 |             — |              230.4K |
| MD   | Maryland Administrative Office of the Courts               |    1 |            15 |             — |               69.1K |
| MD   | Maryland Information Technology Center                     |    1 |             — |             — |                   — |
| MD   | University of Maryland                                     |    1 |             9 |             4 |               12.5K |
| ME   | State of Maine                                             |    1 |             1 |             — |                 256 |
| MI   | Michigan State Government                                  |    1 |             9 |             — |              508.2K |
| MN   | State of Minnesota                                         |    1 |            10 |             1 |              230.9K |
| MO   | State of Missouri Office of Administration                 |    1 |             4 |             2 |               70.7K |
| MS   | Mississippi Department of Information Technology Services  |    1 |             9 |             — |               22.3K |
| MT   | State of Montana                                           |    1 |             3 |             — |               66.0K |
| NC   | North Carolina Administrative Office of the Courts         |    1 |             4 |             — |                2.0K |
| NC   | State of North Carolina                                    |    1 |             9 |             — |              410.4K |
| ND   | State of North Dakota ITD                                  |    2 |             2 |             1 |              131.1K |
| ND   | State of North Dakota Information Technology Department    |    1 |             — |             — |                   — |
| NE   | Network Nebraska                                           |    1 |            32 |             2 |              294.7K |
| NE   | State of Nebraska Office of the CIO                        |    1 |             1 |             — |               65.5K |
| NH   | State of New Hampshire                                     |    1 |             3 |             — |                3.3K |
| NJ   | NJOIT New Jersey Office of Information Technology          |    1 |            85 |             — |               21.8K |
| NJ   | State of New Jersey Judiciary                              |    1 |             1 |             — |                 256 |
| NM   | State of New Mexico                                        |    1 |           143 |             1 |              109.6K |
| NV   | State of Nevada                                            |    1 |             3 |             — |              131.1K |
| NV   | State of Nevada Legislature                                |    1 |             2 |             1 |                2.3K |
| NY   | New York State                                             |    1 |            20 |             — |              145.4K |
| NY   | New York State Department of Health                        |    1 |             2 |             — |               65.8K |
| NY   | New York State Department of Transportation                |    1 |             — |             — |                   — |
| OH   | Department of Administrative Services                      |    1 |             6 |             — |              263.7K |
| OK   | Oklahoma Office of Management & Enterprise Services        |    1 |            13 |             — |               28.4K |
| OR   | State of Oregon                                            |    2 |            20 |             2 |              218.6K |
| PA   | Commonwealth of PA                                         |    1 |             — |             — |                   — |
| RI   | State of Rhode Island                                      |    1 |             3 |             — |               35.3K |
| RI   | State of Rhode Island General Assembly                     |    1 |             1 |             — |                 256 |
| SC   | State of South Carolina                                    |    1 |            20 |             — |              103.7K |
| SD   | South Dakota State Government                              |    2 |             9 |             1 |              114.9K |
| TN   | State of Tennessee                                         |    1 |            28 |             — |              525.3K |
| TN   | Tennessee Valley Authority                                 |    1 |            15 |             1 |              264.4K |
| TX   | Texas Department of Information Resources                  |    1 |            92 |             2 |              321.3K |
| UT   | State of Utah                                              |    1 |             9 |             — |              395.8K |
| UT   | State of Utah Courts                                       |    1 |             3 |             — |                2.0K |
| VA   | Commonwealth of Virginia                                   |    1 |             — |             — |                   — |
| VA   | Commonwealth of Virginia Office of the Attorney General    |    1 |             4 |             — |                1.0K |
| VA   | Virginia Information Technologies Agency                   |    2 |             2 |             — |                1.0K |
| VT   | Vermont Agency of Digital Services                         |    1 |             7 |             — |              262.4K |
| WA   | State of Washington                                        |    1 |            32 |             1 |              656.9K |
| WA   | State of Washington Legislative Service Center             |    1 |             — |             — |                   — |
| WI   | State of WI Dept. of Administration                        |    1 |            39 |             1 |              786.2K |
| WI   | State of Wisconsin Investment Board                        |    1 |             1 |             — |                 256 |
| WV   | West Virginia Network for Educational Telecomputing        |    1 |             6 |             — |              262.1K |
| WY   | State of Wyoming Department                                |    1 |            15 |             1 |              595.2K |
<!-- END:state-gov-table -->

---

## City Governments

Tracked in [`data/us-city-gov-agencies.csv`](data/us-city-gov-agencies.csv). Prefix data in [`data/asn/city-gov-prefixes.csv`](data/asn/city-gov-prefixes.csv).

<!-- BEGIN:city-gov-table -->
| St   | City / Organization                                      | ASNs | IPv4 Prefixes | IPv6 Prefixes | Est. IPv4 Addresses |
| :--- | :---                                                     | ---: | ---:          | ---:          | ---:                |
| AZ   | City of Phoenix                                          |    3 |            35 |             — |               23.8K |
| AZ   | City of Tucson                                           |    1 |             3 |             — |               66.0K |
| AZ   | City of Tucson Wireless                                  |    1 |             — |             — |                   — |
| CA   | City and County of San Francisco                         |    1 |             1 |             1 |                 256 |
| CA   | City of Los Angeles                                      |    1 |            19 |             — |                4.9K |
| CA   | City of Sacramento                                       |    1 |             4 |             — |                1.0K |
| CA   | City of San Diego                                        |    1 |             6 |             — |                1.5K |
| CA   | City of San Jose                                         |    1 |            25 |             1 |               10.8K |
| CO   | City and County of Denver                                |    1 |             3 |             — |               66.0K |
| CO   | Denver International Airport                             |    1 |             8 |             — |                2.3K |
| DC   | Government of the District of Columbia                   |    1 |            14 |             — |                5.9K |
| FL   | City of Jacksonville                                     |    1 |            30 |             — |               72.8K |
| FL   | City of Miami                                            |    1 |             1 |             — |                 256 |
| FL   | City of Tampa                                            |    1 |             3 |             — |                 768 |
| HI   | City and County of Honolulu                              |    1 |             7 |             — |                1.8K |
| IL   | City of Chicago                                          |    1 |            11 |             — |              134.4K |
| IN   | City of Indianapolis                                     |    1 |             2 |             — |               67.6K |
| KY   | Louisville Jefferson County Metro Government             |    1 |             2 |             — |                 768 |
| LA   | City of New Orleans                                      |    1 |             1 |             — |                 512 |
| MA   | City of Boston                                           |    1 |            14 |             — |               77.8K |
| MD   | City of Baltimore Mayor Office of Information Technology |    2 |             2 |             — |                 512 |
| MI   | City of Detroit                                          |    1 |             1 |             — |                 256 |
| MO   | City of Kansas City                                      |    2 |             2 |             — |                 512 |
| NC   | City of Charlotte                                        |    1 |             1 |             1 |               16.4K |
| NC   | City of Raleigh                                          |    1 |             3 |             — |                1.0K |
| NM   | City of Albuquerque                                      |    1 |            13 |             — |              129.0K |
| NV   | City of Las Vegas                                        |    2 |             2 |             1 |                1.3K |
| NY   | City of New York                                         |    1 |            23 |             — |              336.4K |
| NY   | City of New York Public Safety                           |    1 |            12 |             6 |                3.8K |
| NY   | New York City Board of Education                         |    1 |            58 |             — |              148.7K |
| NY   | New York City Board of Elections                         |    1 |             1 |             — |                2.0K |
| NY   | New York City Employees Retirement System                |    1 |             — |             — |                   — |
| NY   | New York City Health and Hospitals Corporation           |    1 |            15 |             — |               15.1K |
| NY   | New York City Police Department                          |    1 |             3 |             — |               16.9K |
| OH   | City of Columbus                                         |    1 |             3 |             — |               16.4K |
| OR   | City of Portland                                         |    1 |             1 |             — |                1.0K |
| PA   | City of Philadelphia                                     |    1 |             3 |             — |               66.3K |
| PA   | City of Pittsburgh                                       |    1 |             1 |             — |               16.4K |
| TN   | City of Memphis                                          |    1 |             — |             — |                   — |
| TX   | City of Austin                                           |    1 |            20 |             — |                9.0K |
| TX   | City of Austin Public Safety                             |    1 |             — |             — |                   — |
| TX   | City of Dallas                                           |    1 |             — |             — |                   — |
| TX   | City of Houston                                          |    1 |            14 |             — |                3.6K |
| TX   | City of Houston Public Works                             |    1 |             1 |             — |                 256 |
| TX   | City of San Antonio                                      |    1 |            37 |             — |               75.8K |
| UT   | Salt Lake City Corporation                               |    1 |            18 |             — |                4.6K |
| WA   | City of Seattle                                          |    1 |             3 |             — |                4.1K |
| WA   | City of Seattle City Light                               |    1 |             — |             — |                   — |
<!-- END:city-gov-table -->

---

## Health Industry

### Hospital Systems

Tracked in [`data/us-hospital-systems.csv`](data/us-hospital-systems.csv). Prefix data in [`data/asn/hospitals-prefixes.csv`](data/asn/hospitals-prefixes.csv).

<!-- BEGIN:hospitals-table -->
| Organization                                                                                            | ASNs | IPv4 Prefixes | IPv6 Prefixes | Est. IPv4 Addresses |
| :---                                                                                                    | ---: | ---:          | ---:          | ---:                |
| NewYork-Presbyterian Hospital                                                                           |    2 |            31 |             — |              672.8K |
| UPMC                                                                                                    |    5 |            16 |             1 |              272.6K |
| Mass General Brigham Incorporated                                                                       |    1 |             5 |             — |              197.1K |
| Spectrum Health                                                                                         |    1 |             8 |             — |              140.3K |
| Cleveland Clinic Foundation                                                                             |    1 |            13 |             — |              135.4K |
| Danbury Hospital - ITG                                                                                  |    1 |            10 |             — |              134.4K |
| Connecticut Hospital Assoc.                                                                             |    1 |            12 |             1 |              134.1K |
| Mayo Foundation for Medical Education and Research                                                      |    1 |            11 |             — |              134.1K |
| Memorial Sloan-Kettering Cancer Center                                                                  |    1 |             7 |             — |              132.1K |
| Intermountain Health Care, Inc.                                                                         |    2 |             4 |             — |              131.8K |
| Univeristy of Chicago Hospitals & Health System                                                         |    1 |             4 |             — |              131.3K |
| Loma Linda University Medical Center                                                                    |    1 |             8 |             — |              131.1K |
| University of Tennessee Medical Center                                                                  |    1 |            10 |             — |              115.2K |
| University of Kansas Medical Center                                                                     |    1 |             8 |             — |              108.3K |
| Joan and Sanford I. Weill Medical College and Graduate School of Medical Sciences of Cornell University |    1 |             4 |             — |               98.8K |
| University of Texas Southwestern Medical Center                                                         |    1 |            13 |             1 |               86.0K |
| Wellmont Health System                                                                                  |    1 |            14 |             — |               83.5K |
| Temple University Health System, Inc.                                                                   |    2 |            17 |             — |               80.4K |
| Sentara Healthcare                                                                                      |    1 |            23 |             — |               73.2K |
| SSM Health Care                                                                                         |    1 |             9 |             1 |               70.1K |
| The Children's Hospital of Philadelphia                                                                 |    1 |             4 |             — |               69.9K |
| Wellstar Health System                                                                                  |    1 |            10 |             — |               68.9K |
| Rush University Medical Center                                                                          |    1 |             5 |             — |               68.6K |
| Childrens Hospital and Regional Medical Center                                                          |    1 |            12 |             — |               68.4K |
| Allina Health System, Inc.                                                                              |    1 |             5 |             — |               67.3K |
| Geisinger System Services                                                                               |    2 |             3 |             1 |               66.8K |
| Medical College of Wisconsin                                                                            |    1 |             6 |             1 |               66.8K |
| The University Of Texas M.D. Anderson Cancer Center                                                     |    1 |             5 |             — |               66.6K |
| Unity Health System                                                                                     |    2 |             5 |             — |               66.6K |
| Texas Tech University Health Sciences Center                                                            |    1 |             4 |             1 |               66.0K |
| Harris County Hospital District                                                                         |    1 |             2 |             — |               65.8K |
| BJC HEALTH SYSTEM                                                                                       |    1 |             1 |             — |               65.5K |
| Dartmouth-Hitchcock Medical Center                                                                      |    1 |             1 |             — |               65.5K |
| Erie County Medical Center                                                                              |    1 |             1 |             — |               65.5K |
| Vanderbilt University Medical Center                                                                    |    1 |             1 |             1 |               65.5K |
| Detroit Medical Center                                                                                  |    1 |            30 |             — |               53.0K |
| Eisenhower Medical Center                                                                               |    1 |             3 |             — |               33.3K |
| University of New Mexico Health Sciences Center                                                         |    1 |             2 |             — |               32.8K |
| Kaiser Foundation Health Plan, Inc.                                                                     |    2 |            42 |             1 |               31.0K |
| Allegheny Health Network                                                                                |    1 |            18 |             — |               26.1K |
| Adventist Health System Sunbelt Healthcare Corporation                                                  |    1 |            13 |             — |               23.3K |
| USC-University Hospital                                                                                 |    1 |            45 |             — |               21.8K |
| MultiCare Health System                                                                                 |    1 |             6 |             — |               19.5K |
| City of Hope Medical Center                                                                             |    1 |             4 |             — |               16.9K |
| University Hospitals Health System                                                                      |    1 |             3 |             — |               16.4K |
| LSU Health Sciences Center                                                                              |    1 |            27 |             — |               14.8K |
| Texas Tech University Health Sciences Center at El Paso                                                 |    1 |             2 |             1 |               12.3K |
| Columbia/HCA Healthcare, Inc.                                                                           |    1 |            44 |             — |               11.8K |
| CommonSpirit Health                                                                                     |    2 |            18 |             — |               11.5K |
| Christus Health                                                                                         |    1 |            22 |             — |                9.5K |
| Froedtert Memorial Lutheran Hospital, Inc.                                                              |    1 |             4 |             — |                9.2K |
| Providence Health & Services                                                                            |    4 |            25 |             — |                9.0K |
| Dignity Health                                                                                          |    1 |             4 |             — |                8.7K |
| Scripps Health                                                                                          |    1 |             3 |             — |                8.7K |
| Baylor Health Care System                                                                               |    2 |            11 |             — |                8.4K |
| Community Hospital of the Monterey Peninsula                                                            |    1 |             2 |             — |                8.4K |
| Hospital Sisters Health Systems                                                                         |    1 |             1 |             — |                8.2K |
| LSU Health Sciences Center - Shreveport                                                                 |    1 |             1 |             — |                8.2K |
| Sisters of Mercy Health System                                                                          |    1 |            15 |             — |                8.2K |
| The Methodist Hospital                                                                                  |    1 |             4 |             — |                8.2K |
| University of Nebraska Medical Center                                                                   |    1 |             9 |             — |                7.9K |
| Yale-New Haven Health Services Corporation                                                              |    1 |            30 |             — |                7.7K |
| MaineHealth Maine Medical Center                                                                        |    1 |            13 |             — |                7.2K |
| BANNER HEALTH                                                                                           |    1 |            11 |             — |                6.7K |
| Sutter Health                                                                                           |    4 |             4 |             — |                6.7K |
| New York Medical College                                                                                |    1 |             3 |             — |                6.1K |
| The Toledo Hospital                                                                                     |    1 |            20 |             1 |                6.1K |
| Children's Hospital Colorado                                                                            |    1 |             8 |             — |                5.9K |
| Virginia Mason Medical Center                                                                           |    1 |             3 |             — |                5.4K |
| Prisma Health                                                                                           |    3 |            17 |             — |                5.1K |
| Tarrant County Hospital District                                                                        |    1 |            11 |             — |                5.1K |
| Stanford Hospital and Clinics                                                                           |    1 |            14 |             — |                4.9K |
| Steward Health Care System LLC                                                                          |    1 |            18 |             — |                4.9K |
| Summa Health System                                                                                     |    1 |             4 |             — |                4.9K |
| The University of Vermont Medical Center Inc                                                            |    1 |            19 |             — |                4.9K |
| CAMC Health System, Inc.                                                                                |    1 |             4 |             — |                4.6K |
| Marshfield Clinic Inc.                                                                                  |    2 |            10 |             — |                4.4K |
| Nationwide Children's Hospital                                                                          |    1 |             2 |             — |                4.4K |
| Richmond Memorial Hospital                                                                              |    1 |             2 |             — |                4.4K |
| Androscoggin Valley Hospital                                                                            |    1 |             1 |             — |                4.1K |
| Henry Ford Health System                                                                                |    1 |            16 |             — |                4.1K |
| Maimonides Medical Center                                                                               |    1 |             4 |             — |                4.1K |
| RWJBarnabas Health, Inc.                                                                                |    1 |             8 |             — |                4.1K |
| Texas Children's Hospital                                                                               |    1 |             6 |             — |                4.1K |
| Weill Cornell Medical College in Qatar                                                                  |    1 |             1 |             1 |                4.1K |
| Memorial Medical Center                                                                                 |    1 |            15 |             — |                3.8K |
| North Shore Long Island Jewish Health System                                                            |    1 |            11 |             — |                3.6K |
| Benefis Health System                                                                                   |    1 |             7 |             — |                3.3K |
| Inova Health System Foundation                                                                          |    1 |             4 |             — |                3.3K |
| St. Joseph Health System                                                                                |    1 |            11 |             — |                3.3K |
| Comanche County Memorial Hospital                                                                       |    1 |             2 |             — |                3.1K |
| Hartford Hospital                                                                                       |    1 |            12 |             — |                3.1K |
| St. Elizabeth Medical Center, Inc.                                                                      |    1 |            12 |             — |                3.1K |
| Cincinnati Children's Hospital Medical Center                                                           |    1 |             7 |             — |                2.8K |
| Northside Hospital                                                                                      |    1 |             6 |             — |                2.8K |
| Concord Hospital                                                                                        |    1 |             6 |             — |                2.6K |
| IMMANUEL MEDICAL CENTER                                                                                 |    1 |             2 |             — |                2.6K |
| Ann & Robert H. Lurie Children's Hospital of Chicago                                                    |    1 |             9 |             — |                2.3K |
| St. Luke's Roosevelt Hospital Center                                                                    |    1 |             8 |             — |                2.3K |
| Baptist Healthcare System                                                                               |    1 |             8 |             — |                2.0K |
| Bartlett Regional Hospital                                                                              |    1 |             1 |             — |                2.0K |
| Beacon Health System, Inc.                                                                              |    1 |             2 |             — |                2.0K |
| Children's Hospital & Health System, Inc.                                                               |    1 |             5 |             — |                2.0K |
| Denver Health and Hospital Authority                                                                    |    1 |             5 |             — |                2.0K |
| H. Lee Moffitt Cancer Center & Research Institute, Inc.                                                 |    1 |             5 |             — |                2.0K |
| PHOENIX CHILDREN'S HOSPITAL                                                                             |    1 |             5 |             — |                2.0K |
| Parkland Health & Hospital System                                                                       |    1 |             5 |             — |                2.0K |
| Valley Health System                                                                                    |    2 |             5 |             — |                2.0K |
| Yuma Regional Medical Center                                                                            |    1 |             4 |             — |                2.0K |
| BRISTOL HOSPITAL INCORPORATED                                                                           |    1 |             4 |             — |                1.8K |
| Connecticut Children's Medical Center                                                                   |    2 |             4 |             — |                1.8K |
| Grady Memorial Hospital                                                                                 |    1 |             7 |             — |                1.8K |
| Holzer Health System                                                                                    |    1 |             7 |             — |                1.8K |
| ST. LUKE'S HEALTH SYSTEM, LTD.                                                                          |    1 |             7 |             — |                1.8K |
| Saint Luke's Health System                                                                              |    1 |             4 |             — |                1.8K |
| Sanford Health                                                                                          |    2 |             7 |             — |                1.8K |
| The Brooklyn Hospital Center                                                                            |    1 |             3 |             — |                1.8K |
| University of Mississippi Medical Center                                                                |    1 |             7 |             — |                1.8K |
| VCU HEALTH SYSTEM AUTHORITY                                                                             |    1 |             7 |             — |                1.8K |
| Children's Hospital Los Angeles                                                                         |    1 |             4 |             — |                1.5K |
| Greater Baltimore Medical Center Inc                                                                    |    1 |             4 |             — |                1.5K |
| Kettering Medical Center                                                                                |    1 |             6 |             — |                1.5K |
| Northwest Community Hospital                                                                            |    1 |             6 |             — |                1.5K |
| OhioHealth Corporation                                                                                  |    1 |             5 |             — |                1.5K |
| Saint Francis Hospital and Medical Center                                                               |    1 |             3 |             — |                1.5K |
| Tampa General Hospital                                                                                  |    1 |             6 |             — |                1.5K |
| UC Health, LLC                                                                                          |    1 |             6 |             — |                1.5K |
| York Hospital                                                                                           |    2 |             6 |             — |                1.5K |
| CHILDRENS HOSPITAL OF ORANGE COUNTY                                                                     |    1 |             5 |             — |                1.3K |
| DEACONESS HOSPITAL, Inc.                                                                                |    1 |             5 |             — |                1.3K |
| Elliot Health System                                                                                    |    1 |             2 |             — |                1.3K |
| Gundersen Lutheran Medical Center, Inc.                                                                 |    1 |             5 |             — |                1.3K |
| Hospital Billing and Collection Service, LTD                                                            |    1 |             2 |             — |                1.3K |
| LUCILE SALTER PACKARD CHILDREN'S HOSPITAL AT STANFORD                                                   |    1 |             2 |             — |                1.3K |
| MERCY MEDICAL CENTER                                                                                    |    2 |             5 |             — |                1.3K |
| Memorial Hermann Health System                                                                          |    1 |             5 |             — |                1.3K |
| Parkview Hospital                                                                                       |    1 |             2 |             — |                1.3K |
| ST. VINCENT HOSPITAL OF THE HOSPITAL SISTERS OF THE THIRD ORDER OF ST. FRANCIS                          |    1 |             3 |             — |                1.3K |
| The Moses H. Cone Memorial Hospital                                                                     |    1 |             5 |             — |                1.3K |
| University Health System                                                                                |    1 |             5 |             — |                1.3K |
| University of Colorado Hospital                                                                         |    1 |             4 |             — |                1.3K |
| ADVENTIST HEALTH SYSTEM/SUNBELT, INC.                                                                   |    1 |             3 |             — |                1.0K |
| Alaska Native Medical Center                                                                            |    1 |             1 |             — |                1.0K |
| Asante Health System                                                                                    |    1 |             1 |             — |                1.0K |
| Bellin Memorial Hospital, Inc.                                                                          |    1 |             3 |             — |                1.0K |
| Boston Medical Center                                                                                   |    1 |             4 |             — |                1.0K |
| Brockton Hospital                                                                                       |    1 |             4 |             — |                1.0K |
| Carolinas Healthcare System                                                                             |    1 |             2 |             — |                1.0K |
| Cooper University Hospital                                                                              |    1 |             2 |             — |                1.0K |
| Covenant Medical Center, Inc.                                                                           |    1 |             1 |             — |                1.0K |
| ECTOR COUNTY HOSPITAL DISTRICT                                                                          |    1 |             1 |             — |                1.0K |
| Essentia Health East                                                                                    |    1 |             4 |             — |                1.0K |
| Froedtert South, Inc.                                                                                   |    2 |             3 |             — |                1.0K |
| Hackensack University Medical Center                                                                    |    1 |             4 |             — |                1.0K |
| Hospital for Special Surgery                                                                            |    1 |             3 |             — |                1.0K |
| Huntsville Hospital                                                                                     |    1 |             4 |             1 |                1.0K |
| Hutchinson Regional Medical Center                                                                      |    1 |             1 |             — |                1.0K |
| Jackson Memorial Hospital, Public Health                                                                |    2 |             3 |             — |                1.0K |
| Maricopa Integrated Health System                                                                       |    1 |             3 |             — |                1.0K |
| Maury Regional Hospital                                                                                 |    1 |             1 |             — |                1.0K |
| Meridian Health System                                                                                  |    1 |             1 |             — |                1.0K |
| Meritus Medical Center, Inc.                                                                            |    1 |             3 |             — |                1.0K |
| Montefiore Medical Center                                                                               |    1 |             4 |             — |                1.0K |
| Morris Hospital                                                                                         |    1 |             3 |             — |                1.0K |
| Nebraska Methodist Health System, Inc.                                                                  |    1 |             3 |             — |                1.0K |
| North Kansas City Hospital Auxiliary                                                                    |    1 |             4 |             — |                1.0K |
| Northwestern Memorial Hospital                                                                          |    2 |             4 |             — |                1.0K |
| OSF Healthcare System                                                                                   |    1 |             4 |             — |                1.0K |
| Orange Regional Medical Center                                                                          |    1 |             4 |             — |                1.0K |
| Orlando Health, INC                                                                                     |    1 |             1 |             — |                1.0K |
| Pagosa Springs Medical Center                                                                           |    1 |             1 |             — |                1.0K |
| Presence Health Network                                                                                 |    1 |             4 |             — |                1.0K |
| Renown Health                                                                                           |    1 |             1 |             1 |                1.0K |
| St. Joseph's Medical Center                                                                             |    1 |             1 |             — |                1.0K |
| Straub Clinic & Hospital                                                                                |    1 |             4 |             — |                1.0K |
| University Medical Center                                                                               |    1 |             2 |             — |                1.0K |
| ANNE ARUNDEL MEDICAL CENTER                                                                             |    1 |             3 |             — |                 768 |
| Capital Health System, Inc                                                                              |    1 |             3 |             — |                 768 |
| Children's Medical Center of Dallas                                                                     |    1 |             3 |             — |                 768 |
| Cook Children's Health Care System                                                                      |    1 |             2 |             — |                 768 |
| Dayton Children's Hospital                                                                              |    1 |             2 |             — |                 768 |
| DuBois Regional Medical Center                                                                          |    2 |             2 |             — |                 768 |
| HEALTH AND HOSPITAL CORPORATION OF MARION COUNTY                                                        |    1 |             3 |             — |                 768 |
| Hennepin County Medical Center                                                                          |    1 |             3 |             — |                 768 |
| La Rabida Hospital                                                                                      |    1 |             3 |             — |                 768 |
| MJHS Health System                                                                                      |    1 |             2 |             — |                 768 |
| Mary Washington Hospital, Inc.                                                                          |    1 |             3 |             — |                 768 |
| Oklahoma Heart Hospital, LLC                                                                            |    1 |             3 |             — |                 768 |
| Peninsula Regional Medical Center                                                                       |    1 |             3 |             — |                 768 |
| Providence Hospital                                                                                     |    1 |             3 |             — |                 768 |
| Rady Children's Hospital - San Diego                                                                    |    1 |             3 |             — |                 768 |
| Thorek Memorial Hospital                                                                                |    1 |             3 |             — |                 768 |
| Tri-City Medical Center                                                                                 |    1 |             2 |             — |                 768 |
| Willis-Knighton Medical Center                                                                          |    1 |             3 |             — |                 768 |
| American Hospital Association                                                                           |    1 |             2 |             — |                 512 |
| Atlantic Health System                                                                                  |    1 |             2 |             — |                 512 |
| BAXTER COUNTY REGIONAL HOSPITAL, INC                                                                    |    1 |             2 |             — |                 512 |
| Baycare Health System, Inc.                                                                             |    1 |             1 |             — |                 512 |
| Blessing Hospital                                                                                       |    1 |             2 |             — |                 512 |
| Blythedale Children's Hospital                                                                          |    1 |             2 |             — |                 512 |
| Butler Memorial Hospital                                                                                |    1 |             2 |             — |                 512 |
| CARE NEW ENGLAND HEALTH SYSTEM                                                                          |    1 |             2 |             — |                 512 |
| Catawba Valley Medical Center                                                                           |    1 |             2 |             — |                 512 |
| Catholic Medical Center                                                                                 |    1 |             1 |             — |                 512 |
| Children's Hospital Medical Center of Akron                                                             |    1 |             2 |             — |                 512 |
| Driscoll Children's Hospital                                                                            |    1 |             2 |             — |                 512 |
| ENLOE MEDICAL CENTER                                                                                    |    1 |             1 |             — |                 512 |
| Ephrata Community Hospital                                                                              |    1 |             2 |             — |                 512 |
| FAIRFIELD MEDICAL CENTER                                                                                |    1 |             2 |             — |                 512 |
| Freeman Health System                                                                                   |    1 |             2 |             — |                 512 |
| Good Samaritan Hospital                                                                                 |    1 |             1 |             — |                 512 |
| Halifax Regional Hospital                                                                               |    1 |             2 |             — |                 512 |
| Hays Medical Center                                                                                     |    1 |             2 |             — |                 512 |
| Howard University Hospital                                                                              |    1 |             2 |             — |                 512 |
| Huntington Memorial Hospital                                                                            |    1 |             2 |             — |                 512 |
| Kootenai Medical Center                                                                                 |    1 |             2 |             — |                 512 |
| Lake Charles Memorial Hospital                                                                          |    1 |             2 |             — |                 512 |
| Lee Memorial Health System                                                                              |    1 |             2 |             — |                 512 |
| Lexington Medical Center                                                                                |    1 |             2 |             — |                 512 |
| Licking Memorial Hospital                                                                               |    1 |             1 |             — |                 512 |
| Logan Health Medical Center                                                                             |    1 |             2 |             — |                 512 |
| Massachusetts Health & Hospital Association, Inc.                                                       |    1 |             2 |             — |                 512 |
| Medisys Health Network, Inc.                                                                            |    1 |             2 |             — |                 512 |
| Memorial Health Care System                                                                             |    1 |             2 |             — |                 512 |
| Memorial Hospital at Gulfport                                                                           |    1 |             2 |             — |                 512 |
| MemorialCare Health System                                                                              |    1 |             2 |             — |                 512 |
| Mercy Medical Center                                                                                    |    1 |             2 |             — |                 512 |
| Miami Children's Hospital                                                                               |    1 |             1 |             — |                 512 |
| Montgomery County Hospital District                                                                     |    1 |             2 |             — |                 512 |
| Mount Nittany Medical Center                                                                            |    1 |             2 |             — |                 512 |
| NCH Healthcare System, Inc.                                                                             |    1 |             2 |             — |                 512 |
| Norman Regional Health System                                                                           |    1 |             1 |             — |                 512 |
| North Broward Hospital District                                                                         |    1 |             2 |             — |                 512 |
| Penn Medicine                                                                                           |    1 |             2 |             — |                 512 |
| Pomona Valley Hospital Medical Center                                                                   |    1 |             2 |             — |                 512 |
| Providence Health Plan                                                                                  |    1 |             2 |             — |                 512 |
| RIVERVIEW HOSPITAL                                                                                      |    1 |             2 |             — |                 512 |
| Sacred Heart Hospital                                                                                   |    1 |             2 |             — |                 512 |
| Saint Francis Health System                                                                             |    1 |             1 |             — |                 512 |
| San Juan Regional Medical Center Inc.                                                                   |    1 |             2 |             — |                 512 |
| Sarasota Memorial Hospital                                                                              |    1 |             2 |             — |                 512 |
| Sisters of Charity Hospital                                                                             |    1 |             1 |             — |                 512 |
| Sky Lakes Medical Center, Inc.                                                                          |    1 |             1 |             — |                 512 |
| Southcoast Health System, Inc.                                                                          |    1 |             2 |             — |                 512 |
| Southern Maine Medical Center                                                                           |    1 |             2 |             — |                 512 |
| Southern New Hampshire Health System                                                                    |    1 |             2 |             — |                 512 |
| Stamford Hospital                                                                                       |    1 |             2 |             — |                 512 |
| Swedish Covenant Hospital                                                                               |    1 |             2 |             — |                 512 |
| Tanner Medical Center, Inc.                                                                             |    1 |             2 |             — |                 512 |
| Texas Medical Center                                                                                    |    1 |             2 |             — |                 512 |
| Torrance Memorial Medical Center                                                                        |    1 |             2 |             — |                 512 |
| University of California Davis Medical Center                                                           |    1 |             2 |             — |                 512 |
| University of Wisconsin Hospital and Clinics                                                            |    1 |             2 |             — |                 512 |
| Virginia Hospital Center                                                                                |    1 |             2 |             — |                 512 |
| Washington Hospital Healthcare Sysem                                                                    |    1 |             2 |             — |                 512 |
| ACMH Hospital                                                                                           |    1 |             1 |             — |                 256 |
| ARKANSAS HEART HOSPITAL ENCORE                                                                          |    1 |             1 |             — |                 256 |
| Adena Health System                                                                                     |    1 |             1 |             — |                 256 |
| Alameda Health System                                                                                   |    1 |             1 |             — |                 256 |
| Anderson Hospital                                                                                       |    1 |             1 |             — |                 256 |
| Arkansas Children's Hospital                                                                            |    1 |             1 |             — |                 256 |
| Aspen Valley Hospital                                                                                   |    1 |             1 |             — |                 256 |
| Atlanticare Health System Inc.                                                                          |    1 |             1 |             — |                 256 |
| BARRETT HOSPITAL AND HEALHCARE                                                                          |    1 |             1 |             — |                 256 |
| BROADLAWNS MEDICAL CENTER                                                                               |    1 |             1 |             — |                 256 |
| Baptist Health System                                                                                   |    1 |             1 |             — |                 256 |
| Baptist Health System of Alabama                                                                        |    1 |             1 |             — |                 256 |
| Bassett Medical Center                                                                                  |    1 |             1 |             — |                 256 |
| Bayhealth Medical Center, Inc.                                                                          |    1 |             1 |             — |                 256 |
| Beebe Medical Center Inc.                                                                               |    1 |             1 |             — |                 256 |
| Beloit Health System, Inc.                                                                              |    1 |             1 |             — |                 256 |
| Bingham Memorial Hospital                                                                               |    1 |             1 |             1 |                 256 |
| Boulder Community Hospital                                                                              |    1 |             1 |             — |                 256 |
| CARILION HEALTH SYSTEM                                                                                  |    1 |             1 |             — |                 256 |
| CGH Medical Center                                                                                      |    1 |             1 |             — |                 256 |
| CHAMPLAIN VALLEY PHYSICIANS HOSPITAL MEDICAL CENTER                                                     |    1 |             1 |             — |                 256 |
| Cameron Memorial Community Hospital Inc                                                                 |    1 |             1 |             — |                 256 |
| Cape Fear Valley Medical Center                                                                         |    1 |             1 |             — |                 256 |
| Cape Regional Medical Center, Inc.                                                                      |    1 |             1 |             — |                 256 |
| CarolinaEast Medical Center                                                                             |    1 |             1 |             — |                 256 |
| Carson Tahoe Health System                                                                              |    1 |             1 |             — |                 256 |
| Cass Regional Medical Center                                                                            |    1 |             1 |             — |                 256 |
| Central Vermont Medical Center                                                                          |    1 |             1 |             — |                 256 |
| Centrastate Medical Center, Inc.                                                                        |    1 |             1 |             — |                 256 |
| Chesapeake General Hospital                                                                             |    1 |             1 |             — |                 256 |
| Children's Hospital & Medical Center                                                                    |    1 |             1 |             — |                 256 |
| Columbia Basin Hospital                                                                                 |    1 |             1 |             — |                 256 |
| Columbia Memorial Hospital                                                                              |    1 |             1 |             — |                 256 |
| Columbus Community Hospital, Inc.                                                                       |    1 |             1 |             — |                 256 |
| Columbus Regional Hospital                                                                              |    1 |             1 |             — |                 256 |
| Community Health Network of Connecticut                                                                 |    1 |             1 |             — |                 256 |
| Community Medical Center, Inc                                                                           |    1 |             1 |             — |                 256 |
| Community Memorial Health System                                                                        |    1 |             1 |             — |                 256 |
| Cooley Dickinson Hospital                                                                               |    1 |             1 |             — |                 256 |
| Crouse Hospital                                                                                         |    1 |             1 |             — |                 256 |
| Dartmouth Hitchcock Medical Center                                                                      |    1 |             1 |             — |                 256 |
| Day Kimball Hospital                                                                                    |    1 |             1 |             — |                 256 |
| Dayton General Hospital                                                                                 |    1 |             1 |             — |                 256 |
| Dekalb Medical Center                                                                                   |    1 |             1 |             — |                 256 |
| Delta County Memorial Hospital                                                                          |    1 |             1 |             — |                 256 |
| Dignity Health, Yavapai Regional Medical Center                                                         |    1 |             1 |             — |                 256 |
| Doylestown Hospital                                                                                     |    1 |             1 |             — |                 256 |
| East Alabama Medical Center                                                                             |    1 |             1 |             — |                 256 |
| Englewood Hospital and Medical Center                                                                   |    1 |             1 |             — |                 256 |
| Evangelical Community Hospital                                                                          |    1 |             1 |             — |                 256 |
| Exeter Hospital                                                                                         |    1 |             1 |             — |                 256 |
| Finger Lakes Regional Health System, Inc.                                                               |    1 |             1 |             — |                 256 |
| Firelands Regional Medical Center                                                                       |    1 |             1 |             — |                 256 |
| Fisher-Titus Medical Center                                                                             |    1 |             1 |             — |                 256 |
| Flagler Hospital, Inc                                                                                   |    1 |             1 |             — |                 256 |
| Forrest County General Hospital                                                                         |    1 |             1 |             — |                 256 |
| Frederick Memorial Healthcare System                                                                    |    1 |             1 |             — |                 256 |
| Fulton County Medical Center                                                                            |    1 |             1 |             — |                 256 |
| GENERAL HEALTH SYSTEM                                                                                   |    1 |             1 |             — |                 256 |
| GUADALUPE REGIONAL MEDICAL CENTER                                                                       |    1 |             1 |             — |                 256 |
| Genesis Health System                                                                                   |    1 |             1 |             — |                 256 |
| Genesis Healthcare System                                                                               |    1 |             1 |             — |                 256 |
| Gila Regional Medical Center                                                                            |    1 |             1 |             — |                 256 |
| Glens Falls Hospital                                                                                    |    1 |             1 |             — |                 256 |
| Good Shepherd Medical Center                                                                            |    1 |             1 |             — |                 256 |
| Graham Health System                                                                                    |    1 |             1 |             — |                 256 |
| Grand Island Regional Medical Center                                                                    |    1 |             1 |             — |                 256 |
| Grande Ronde Hospital, Inc.                                                                             |    1 |             1 |             — |                 256 |
| Greater Regional Medical Center                                                                         |    1 |             1 |             — |                 256 |
| Gunnison Valley Hospital                                                                                |    1 |             1 |             — |                 256 |
| Guthrie Healthcare System                                                                               |    1 |             1 |             — |                 256 |
| HUNTSVILLE MEMORIAL HOSPITAL                                                                            |    1 |             1 |             — |                 256 |
| Harbor Regional Health Community Hospital                                                               |    1 |             1 |             — |                 256 |
| Harlan County Health System                                                                             |    1 |             1 |             — |                 256 |
| Heart of the Rockies Regional Medical Center                                                            |    1 |             1 |             — |                 256 |
| Heartland Regional Medical Center                                                                       |    1 |             1 |             — |                 256 |
| Hendrick Medical Center                                                                                 |    1 |             1 |             — |                 256 |
| Henry Mayo Newhall Memorial Hospital                                                                    |    1 |             1 |             — |                 256 |
| Heritage Valley Health System                                                                           |    1 |             1 |             — |                 256 |
| Hospital for Special Care                                                                               |    1 |             1 |             — |                 256 |
| Houlton Regional Hospital                                                                               |    1 |             1 |             — |                 256 |
| Hugh Chatham Memorial Hospital, Inc.                                                                    |    1 |             1 |             — |                 256 |
| Hurley Medical Center                                                                                   |    1 |             1 |             — |                 256 |
| Indiana Regional Medical Center                                                                         |    1 |             1 |             — |                 256 |
| Infirmary Health System, Inc.                                                                           |    1 |             1 |             — |                 256 |
| Jackson County Memorial Hospital                                                                        |    1 |             1 |             — |                 256 |
| Kearney Regional Medical Center LLC                                                                     |    1 |             1 |             — |                 256 |
| Kingman Regional Medical Center                                                                         |    1 |             1 |             — |                 256 |
| Kings Daughters Medical Center                                                                          |    2 |             1 |             — |                 256 |
| Kuakini Medical Center                                                                                  |    1 |             1 |             — |                 256 |
| Lane Regional Medical Center                                                                            |    1 |             1 |             — |                 256 |
| Lima Memorial Hospital                                                                                  |    1 |             1 |             — |                 256 |
| Littleton Regional Hospital                                                                             |    1 |             1 |             — |                 256 |
| MARY GREELEY MEDICAL CENTER                                                                             |    1 |             1 |             — |                 256 |
| MIDDLESEX HEALTH SYSTEM, INC.                                                                           |    1 |             1 |             — |                 256 |
| Madison Co Memorial Hospital                                                                            |    1 |             1 |             — |                 256 |
| Madonna Rehabilitation Hospital                                                                         |    1 |             1 |             — |                 256 |
| Marcus Daly Memorial Hospital Corporation                                                               |    1 |             1 |             — |                 256 |
| Marin General Hospital                                                                                  |    1 |             1 |             — |                 256 |
| Marion General Hospital, Inc.                                                                           |    1 |             1 |             — |                 256 |
| Meadville Medical Center                                                                                |    1 |             1 |             — |                 256 |
| Meharry Medical College                                                                                 |    1 |             1 |             — |                 256 |
| Melissa Memorial Hospital                                                                               |    1 |             1 |             — |                 256 |
| Memorial Hospital and Health Care Center                                                                |    1 |             1 |             — |                 256 |
| Memorial Hospital of Sweetwater County Foundation                                                       |    1 |             1 |             — |                 256 |
| Methodist Health System                                                                                 |    1 |             1 |             — |                 256 |
| Methodist Hospital of Memphis                                                                           |    1 |             1 |             — |                 256 |
| Methodist Hospital of Southern California                                                               |    1 |             1 |             — |                 256 |
| Midland County Hospital District                                                                        |    1 |             1 |             — |                 256 |
| Milford Regional Medical Center Inc.                                                                    |    1 |             1 |             — |                 256 |
| Montrose Memorial Hospital                                                                              |    2 |             1 |             — |                 256 |
| Monument Health Rapid City Hospital, Inc.                                                               |    1 |             1 |             — |                 256 |
| Mount Sinai Medical Center of Florida, Inc.                                                             |    1 |             1 |             — |                 256 |
| Mt San Rafael Hospital                                                                                  |    1 |             1 |             — |                 256 |
| Murray-Calloway County Hospital                                                                         |    1 |             1 |             — |                 256 |
| NORTHEASTERN VERMONT REGIONAL HOSPITAL, INC.                                                            |    1 |             1 |             — |                 256 |
| Nanticoke Memorial Hospital INC                                                                         |    1 |             1 |             — |                 256 |
| Natividad Medical Center                                                                                |    1 |             1 |             — |                 256 |
| New Bridge Medical Center                                                                               |    1 |             1 |             — |                 256 |
| New England Baptist Hospital                                                                            |    1 |             1 |             — |                 256 |
| New Liberty Hospital District of Clay County, Missouri                                                  |    1 |             1 |             — |                 256 |
| North Mississippi Medical Center Inc.                                                                   |    1 |             1 |             — |                 256 |
| North Oaks Health System                                                                                |    1 |             1 |             — |                 256 |
| NorthWestern Medical Center                                                                             |    1 |             1 |             — |                 256 |
| Northeast Alabama Regional Medical Center                                                               |    1 |             1 |             — |                 256 |
| Northeast Georgia Medical Center, Inc.                                                                  |    1 |             1 |             — |                 256 |
| Northern Hospital District of Surry County                                                              |    1 |             1 |             — |                 256 |
| OLEAN GENERAL HOSPITAL                                                                                  |    1 |             1 |             — |                 256 |
| Overlake Hospital Medical Center                                                                        |    1 |             1 |             — |                 256 |
| Phelps County Regional Medical Center                                                                   |    1 |             1 |             — |                 256 |
| Pikeville Medical Center                                                                                |    1 |             1 |             — |                 256 |
| Porter Hospital                                                                                         |    1 |             1 |             — |                 256 |
| Pratt Regional Medical Center                                                                           |    1 |             1 |             — |                 256 |
| Punxsutawney Area Hospital                                                                              |    1 |             1 |             — |                 256 |
| RIVERSIDE HEALTH SYSTEM                                                                                 |    1 |             1 |             — |                 256 |
| Reading Hospital                                                                                        |    1 |             1 |             — |                 256 |
| Redlands Community Hospital                                                                             |    1 |             1 |             — |                 256 |
| Reedsburg Area Medical Center Inc.                                                                      |    1 |             1 |             — |                 256 |
| Ridgeview Medical Center                                                                                |    1 |             1 |             — |                 256 |
| Rockford Health System                                                                                  |    1 |             1 |             — |                 256 |
| SHORE MEMORIAL HOSPITAL                                                                                 |    1 |             1 |             — |                 256 |
| ST JOSEPH HOSPITAL                                                                                      |    1 |             1 |             — |                 256 |
| SWEDISHAMERICAN HEALTH SYSTEM CORPORATION                                                               |    1 |             1 |             — |                 256 |
| Saint Bernard Hospital                                                                                  |    2 |             1 |             — |                 256 |
| Saint Francis Medical Center                                                                            |    1 |             1 |             — |                 256 |
| Saint Mary's Hospital, Inc.                                                                             |    1 |             1 |             — |                 256 |
| Salem Hospital                                                                                          |    1 |             1 |             — |                 256 |
| Salinas Valley Memorial Hospital                                                                        |    1 |             1 |             — |                 256 |
| San Antonio Regional Hospital                                                                           |    1 |             1 |             — |                 256 |
| San Luis Valley Regional Medical Center                                                                 |    1 |             1 |             1 |                 256 |
| Saratoga Hospital                                                                                       |    1 |             1 |             — |                 256 |
| Schneck Medical Center                                                                                  |    1 |             1 |             — |                 256 |
| Scottish Rite Hospital for Children                                                                     |    1 |             1 |             — |                 256 |
| Shannon Medical Center                                                                                  |    1 |             1 |             — |                 256 |
| Sierra View District Hospital                                                                           |    1 |             1 |             — |                 256 |
| Southeast Alabama Medical Center                                                                        |    1 |             1 |             — |                 256 |
| Southern Illinois Hospital Services                                                                     |    1 |             1 |             — |                 256 |
| Southern Tennessee Regional Health System Winchester                                                    |    1 |             1 |             — |                 256 |
| Sparrow Health System                                                                                   |    1 |             1 |             — |                 256 |
| Sparta Community Hospital                                                                               |    1 |             1 |             — |                 256 |
| Spring View Hospital                                                                                    |    1 |             1 |             — |                 256 |
| St Francis Healthcare System of Hawaii                                                                  |    1 |             1 |             — |                 256 |
| St. Charles Health System, Inc.                                                                         |    1 |             1 |             — |                 256 |
| St. Clair Memorial Hospital                                                                             |    1 |             1 |             — |                 256 |
| St. John's Riverside Hospital                                                                           |    1 |             1 |             — |                 256 |
| St. Josephs/Candler Health System, Inc.                                                                 |    1 |             1 |             — |                 256 |
| St. Jude Children's Research Hospital                                                                   |    1 |             1 |             — |                 256 |
| St. Luke's Hospital                                                                                     |    1 |             1 |             — |                 256 |
| St. Mary's Health System                                                                                |    1 |             1 |             — |                 256 |
| St. Vincent Hospital                                                                                    |    1 |             1 |             — |                 256 |
| Summit Healthcare Regional Medical Center                                                               |    1 |             1 |             — |                 256 |
| THE GOOD SAMARITAN HOSPITAL OF LEBANON, PENNSYLVANIA                                                    |    1 |             1 |             — |                 256 |
| Tahoe Forest Hospital District                                                                          |    1 |             1 |             — |                 256 |
| Telluride Medical Center                                                                                |    1 |             1 |             — |                 256 |
| Teton County Hospital District                                                                          |    1 |             1 |             — |                 256 |
| The Children's Hospital of Alabama                                                                      |    1 |             1 |             — |                 256 |
| The Children's Mercy Hospital                                                                           |    1 |             1 |             — |                 256 |
| The Harrison Memorrial Hospital, Inc.                                                                   |    1 |             1 |             — |                 256 |
| The Health Care Authority for Baptist Health, An Affiliate of UAB Health System                         |    1 |             1 |             — |                 256 |
| The New London Hospital Association, Inc                                                                |    1 |             1 |             — |                 256 |
| The Queen's Medical Center                                                                              |    1 |             1 |             — |                 256 |
| Thibodaux Regional Medical Center                                                                       |    1 |             1 |             — |                 256 |
| Tift Regional Health System, Inc.                                                                       |    1 |             1 |             — |                 256 |
| Titusville Area Hospital                                                                                |    1 |             1 |             — |                 256 |
| Touro Infirmary Hospital                                                                                |    1 |             1 |             — |                 256 |
| Tufts Medical Center Inc.                                                                               |    1 |             1 |             — |                 256 |
| UP Health System - Marquette                                                                            |    1 |             1 |             — |                 256 |
| Union Hospital, Inc.                                                                                    |    1 |             1 |             — |                 256 |
| University Medical Center of Southern Nevada                                                            |    1 |             1 |             — |                 256 |
| University Medical Center, Inc                                                                          |    1 |             1 |             — |                 256 |
| VALLEY VIEW HOSPITAL ASSOCIATION                                                                        |    1 |             1 |             — |                 256 |
| Valley Children's Hospital                                                                              |    1 |             1 |             — |                 256 |
| Valley County Health System                                                                             |    1 |             1 |             — |                 256 |
| WITHAM HOSPITAL                                                                                         |    1 |             1 |             — |                 256 |
| WakeMed                                                                                                 |    1 |             1 |             — |                 256 |
| Warren General Hospital                                                                                 |    1 |             1 |             — |                 256 |
| Weeks Medical Center                                                                                    |    1 |             1 |             — |                 256 |
| Wentworth-Douglass Hospital                                                                             |    1 |             1 |             — |                 256 |
| West Holt Memorial Hospital                                                                             |    1 |             1 |             — |                 256 |
| White Plains Hospital                                                                                   |    1 |             1 |             — |                 256 |
| White Wilson Medical Center, P.A.                                                                       |    1 |             1 |             — |                 256 |
| Williamson Medical Center                                                                               |    1 |             1 |             — |                 256 |
| AMERICAN SOCIETY OF HEALTH SYSTEM PHARMACISTS                                                           |    1 |             — |             — |                   — |
| Akron General Medical Center                                                                            |    1 |             — |             — |                   — |
| Beatrice Community Hospital and Health Center, Inc.                                                     |    1 |             — |             — |                   — |
| Beth Israel Deaconess Medical Center                                                                    |    1 |             — |             — |                   — |
| Boca Raton Regional Hospital Inc.                                                                       |    1 |             — |             — |                   — |
| Bradford Regional Medical Center                                                                        |    1 |             — |             — |                   — |
| CalvertHealth Medical Center                                                                            |    1 |             — |             — |                   — |
| Catskill Regional Medical Center                                                                        |    1 |             — |             — |                   — |
| Chan Soon-Shiong Medical Center at Windber                                                              |    1 |             — |             — |                   — |
| Children's Hospital of The King's Daughters Health System                                               |    1 |             — |             — |                   — |
| Children's National Hospital                                                                            |    1 |             — |             — |                   — |
| Citizens Medical Center                                                                                 |    1 |             — |             — |                   — |
| Concord Hospital - Laconia                                                                              |    1 |             — |             — |                   — |
| EMANUEL MEDICAL CENTER, INC                                                                             |    1 |             — |             — |                   — |
| Egleston Children's Hospital                                                                            |    1 |             — |             — |                   — |
| F.F. Thompson Health System, Inc.                                                                       |    1 |             — |             — |                   — |
| Geisinger Jersey Shore Hospital                                                                         |    1 |             — |             — |                   — |
| Independent Health Network, Inc.                                                                        |    1 |             — |             — |                   — |
| Kadlec Regional Medical Center                                                                          |    1 |             — |             — |                   — |
| Lower Umpqua Hospital District                                                                          |    1 |             — |             — |                   — |
| Luthern General Health System                                                                           |    1 |             — |             — |                   — |
| Memorial Hospital                                                                                       |    1 |             — |             — |                   — |
| Mille Lacs Health System                                                                                |    1 |             — |             — |                   — |
| Mother Frances Hospital Regional Health Care Center                                                     |    1 |             — |             — |                   — |
| Nashville General Hospital                                                                              |    1 |             — |             — |                   — |
| North Valley Hospital                                                                                   |    1 |             — |             1 |                   — |
| Oregon Health Network, Inc.                                                                             |    1 |             — |             — |                   — |
| Parrish Medical Center                                                                                  |    1 |             — |             — |                   — |
| Pender Community Hospital District                                                                      |    1 |             — |             — |                   — |
| Robert Wood Johnson University Hospital                                                                 |    1 |             — |             — |                   — |
| SWEDISH MEDICAL CENTER                                                                                  |    1 |             — |             — |                   — |
| Saint Joseph's Hospital & Medical Center                                                                |    1 |             — |             — |                   — |
| Saint Joseph's Hospital of Atlanta, Inc.                                                                |    1 |             — |             — |                   — |
| Sapient Health Network                                                                                  |    1 |             — |             — |                   — |
| Silver Cross Hospital                                                                                   |    1 |             — |             — |                   — |
| Springhill Memorial Hospital                                                                            |    1 |             — |             — |                   — |
| St. Joseph Hospital                                                                                     |    1 |             — |             — |                   — |
| St. Mary's Medical Center, Inc.                                                                         |    2 |             — |             — |                   — |
| THE HARDIN MEMORIAL HOSPITAL FOUNDATION, INC.                                                           |    1 |             — |             — |                   — |
| The Children's Hospital Corporation                                                                     |    1 |             — |             1 |                   — |
| The Milton S. Hershey Medical Center                                                                    |    1 |             — |             — |                   — |
| The Union Hospital of Cecil County, Inc.                                                                |    1 |             — |             — |                   — |
| UC HEALTH                                                                                               |    1 |             — |             — |                   — |
| United Hospital Center                                                                                  |    1 |             — |             — |                   — |
| University Hospital                                                                                     |    1 |             — |             — |                   — |
| University of Alabama at Birmingham Medical Center                                                      |    1 |             — |             — |                   — |
| University of Calif. S.F. - Hospital Info Sys                                                           |    1 |             — |             — |                   — |
| Wabash General Hospital District                                                                        |    1 |             — |             — |                   — |
| Waianae District Comprehensive Health & Hospital Board Inc                                              |    1 |             — |             — |                   — |
| West Jefferson Medical Center                                                                           |    1 |             — |             — |                   — |
| William Beaumont Hospital                                                                               |    2 |             — |             — |                   — |
| Zangmeister cancer Center                                                                               |    1 |             — |             — |                   — |
<!-- END:hospitals-table -->

### Health Insurers

Tracked in [`data/us-health-insurance.csv`](data/us-health-insurance.csv). Prefix data in [`data/asn/insurance-prefixes.csv`](data/asn/insurance-prefixes.csv).

<!-- BEGIN:insurance-table -->
| Organization                                                          | ASNs | IPv4 Prefixes | IPv6 Prefixes | Est. IPv4 Addresses |
| :---                                                                  | ---: | ---:          | ---:          | ---:                |
| Blue Cross Blue Shield of Michigan Mutual Insurance                   |    1 |             9 |             — |              100.1K |
| Anthem Broadband                                                      |    4 |            44 |             3 |               76.5K |
| Independence Blue Cross                                               |    1 |             3 |             — |               66.0K |
| HealthPlan Services, Inc.                                             |    1 |             2 |             — |               65.8K |
| CIGNA                                                                 |    2 |            47 |             — |               61.4K |
| Aetna, Inc.                                                           |    1 |            20 |             — |               37.1K |
| Centene Corporation                                                   |    4 |            44 |             — |               34.0K |
| HUMANA                                                                |    1 |            59 |             — |               33.0K |
| Kaiser Foundation Health Plan, Inc.                                   |    2 |            42 |             1 |               31.0K |
| Blue Cross and Blue Shield of North Carolina                          |    1 |             6 |             — |               29.4K |
| Magellan Health Services                                              |    1 |            14 |             — |               20.2K |
| Elevance Health, Inc.                                                 |    1 |            12 |             — |               16.4K |
| Blue Cross and Blue Shield of Alabama                                 |    1 |             6 |             — |               13.6K |
| Blue Cross & Blue Shield of Minnesota                                 |    1 |            17 |             — |                7.9K |
| Highmark Inc                                                          |    1 |            22 |             — |                5.6K |
| Premera Blue Cross                                                    |    3 |             9 |             — |                5.4K |
| Blue Cross Blue Shield of South Carolina                              |    1 |             7 |             — |                4.9K |
| WELLMARK BLUE CROSS AND BLUE SHIELD                                   |    1 |            11 |             — |                4.9K |
| Blue Shield of California                                             |    4 |            13 |             — |                3.6K |
| Blue Cross Blue Shield of Illinois or Blue Cross Blue Shield of Texas |    7 |             9 |             — |                2.3K |
| Blue Cross Blue Shield of Nebraska                                    |    1 |             3 |             — |                2.3K |
| HORIZON BLUE CROSS BLUE SHIELD OF NJ                                  |    1 |             9 |             — |                2.3K |
| Blue Cross Blue Shield of North Dakota                                |    1 |             1 |             — |                2.0K |
| Blue Cross and Blue Shield of Massachusetts, Inc.                     |    1 |             7 |             — |                1.8K |
| Dean Health Plan, Inc.                                                |    1 |             5 |             — |                1.5K |
| BlueCross BlueShield of Tennessee                                     |    1 |             3 |             — |                 768 |
| Excellus Health Plan, Inc.                                            |    1 |             3 |             — |                 768 |
| MVP Health Plan Inc.                                                  |    1 |             2 |             — |                 768 |
| Blue Cross Blue Shield Association                                    |    1 |             2 |             — |                 512 |
| Blue Cross Blue Shield of Kansas, Inc.                                |    1 |             2 |             — |                 512 |
| CareFirst Management Company, LLC                                     |    1 |             1 |             — |                 512 |
| Inland Empire Health Plan                                             |    2 |             2 |             — |                 512 |
| Keystone Mercy Health Plan                                            |    1 |             2 |             — |                 512 |
| METROPLUS HEALTH PLAN, INC.                                           |    1 |             2 |             — |                 512 |
| Providence Health Plan                                                |    1 |             2 |             — |                 512 |
| SCAN Health Plan                                                      |    1 |             2 |             — |                 512 |
| San Francisco Health Plan                                             |    1 |             2 |             — |                 512 |
| UnitedHealth Group Incorporated                                       |    6 |             2 |             — |                 512 |
| Vantage Health Plan, Inc.                                             |    1 |             1 |             1 |                 512 |
| Blue Cross Blue Shield Of Louisiana                                   |    1 |             2 |             — |                 264 |
| Blue Cross and Blue Shield of Kansas City                             |    1 |             1 |             — |                 256 |
| Capital Health Plan, Inc.                                             |    1 |             1 |             — |                 256 |
| PARTNERSHIP HEALTHPLAN OF CALIFORNIA                                  |    1 |             1 |             — |                 256 |
| Prominence Health Plan                                                |    1 |             1 |             — |                 256 |
| United Health Services Hospitals, Inc.                                |    1 |             1 |             — |                 256 |
| American Postal Workers Union, AFL-CIO Health Plan                    |    1 |             — |             — |                   — |
| BLUE CROSS & BLUE SHIELD OF MISSISSIPPI, A MUTUAL INSURANCE COMPANY   |    1 |             — |             — |                   — |
| Blue Cross and Blue Shield of Arizona Inc                             |    1 |             — |             — |                   — |
| Harvard Pilgrim Health Care, Inc.                                     |    1 |             — |             — |                   — |
| Molina Healthcare Inc.                                                |    1 |             — |             — |                   — |
| SUMMACARE HEALTH PLAN                                                 |    1 |             — |             — |                   — |
<!-- END:insurance-table -->

### Pharmacy Benefit Managers

Tracked in [`data/us-pharmacy-benefit-managers.csv`](data/us-pharmacy-benefit-managers.csv). Prefix data in [`data/asn/pbm-prefixes.csv`](data/asn/pbm-prefixes.csv).

<!-- BEGIN:pbm-table -->
| Organization                       | ASNs | IPv4 Prefixes | IPv6 Prefixes | Est. IPv4 Addresses |
| :---                               | ---: | ---:          | ---:          | ---:                |
| Express Scripts Incorporated       |    2 |            45 |             — |              152.3K |
| Omnicare, Inc.                     |    2 |            20 |             — |               39.4K |
| Prime Therapeutics LLC             |    3 |             8 |             — |                4.1K |
| MedImpact Healthcare Systems, Inc. |    1 |             8 |             — |                2.6K |
| Walgreens Co                       |    1 |             6 |             — |                1.5K |
| Navitus Health Solutions, LLC      |    1 |             2 |             — |                 512 |
| Diplomat Pharmacy, Inc             |    1 |             1 |             — |                 256 |
| Medco Health Solutions, Inc        |    1 |             — |             — |                   — |
| Rite Aid Corporation               |    1 |             — |             — |                   — |
<!-- END:pbm-table -->

### Health IT Vendors

Includes EHR systems (Epic, Cerner/Oracle), clinical networks, and health data platforms. Tracked in [`data/us-health-it-vendors.csv`](data/us-health-it-vendors.csv). Prefix data in [`data/asn/health-it-prefixes.csv`](data/asn/health-it-prefixes.csv).

<!-- BEGIN:health-it-table -->
| Organization                                 | ASNs | IPv4 Prefixes | IPv6 Prefixes | Est. IPv4 Addresses |
| :---                                         | ---: | ---:          | ---:          | ---:                |
| Cerner Corporation                           |    5 |            27 |             — |               38.7K |
| Cardinal Health, Inc.                        |    4 |            29 |             2 |                8.4K |
| Athenahealth                                 |    7 |            16 |             — |                7.9K |
| Netsmart Technologies                        |    2 |             4 |             — |                4.6K |
| Microsoft Corporation                        |    4 |             8 |             3 |                3.8K |
| Carelon Behavioral Health, Inc.              |    1 |             7 |             — |                3.6K |
| Inovalon Inc.                                |    1 |             5 |             — |                3.1K |
| WebMD Health Services Group, Inc.            |    1 |             6 |             — |                2.0K |
| Epic Systems Corporation                     |    2 |             2 |             1 |                1.3K |
| Greenway Health, LLC                         |    1 |             4 |             — |                1.3K |
| Surescripts, LLC                             |    2 |             4 |             — |                1.3K |
| ECLINICALWORKS, LLC                          |    1 |             1 |             — |                 256 |
| Medical Information Technology, Inc.         |    1 |             1 |             — |                 256 |
| Netsmart Technologies Inc.                   |    1 |             1 |             — |                 256 |
| Omnicell                                     |    1 |             1 |             — |                 256 |
| Availity                                     |    1 |             — |             — |                   — |
| Evolent Health LLC                           |    1 |             — |             — |                   — |
| Guidehouse Inc.                              |    1 |             — |             — |                   — |
| Health Catalyst, Inc.                        |    1 |             — |             — |                   — |
| NextGen Healthcare Information Systems, LLC. |    2 |             — |             — |                   — |
<!-- END:health-it-table -->

---

## Technology Stack (Active Domain Scan)

Top technologies detected across actively scanned government domains via httpx fingerprinting.

<!-- BEGIN:tech-table -->
| Technology                  | Domains | Example Domains                           |
| :---                        | ---:    | :---                                      |
| HSTS                        |    2141 | archives.gov, atf.gov, bjs.gov            |
| Cloudflare                  |     473 | americabydesign.gov, atf.gov, bis.gov     |
| Amazon Web Services         |     406 | acf.gov, archives.gov, atf.gov            |
| HTTP/3                      |     361 | americabydesign.gov, cancer.gov, cdc.gov  |
| Cloudflare Bot Management   |     308 | atf.gov, bis.gov, census.gov              |
| Amazon CloudFront           |     268 | archives.gov, atf.gov, cancer.gov         |
| Cloudflare Browser Insights |     189 | americabydesign.gov, census.gov, cisa.gov |
| Apache HTTP Server          |     162 | cancer.gov, commerce.gov, doi.gov         |
| Nginx                       |     119 | archives.gov, atf.gov, cancer.gov         |
| jQuery                      |     106 | cancer.gov, cdc.gov, census.gov           |
| Google Tag Manager          |      94 | archives.gov, cancer.gov, data.gov        |
| Akamai                      |      90 | dot.gov, faa.gov, fws.gov                 |
| PHP                         |      86 | atf.gov, cancer.gov, commerce.gov         |
| Google Analytics            |      80 | archives.gov, cancer.gov, commerce.gov    |
| Amazon ELB                  |      76 | acf.gov, archives.gov, cisa.gov           |
| IIS:10.0                    |      70 | atf.gov, bis.gov, cancer.gov              |
| Windows Server              |      70 | atf.gov, bis.gov, cancer.gov              |
| Azure                       |      67 | cdc.gov, ed.gov, gpo.gov                  |
| Microsoft ASP.NET           |      62 | atf.gov, cdc.gov, commerce.gov            |
| Amazon S3                   |      59 | archives.gov, atf.gov, cancer.gov         |
| Azure Front Door            |      58 | cdc.gov, ed.gov, gpo.gov                  |
| Akamai Bot Manager          |      57 | healthcare.gov, irs.gov, medicare.gov     |
| Amazon ALB                  |      56 | cancer.gov, epa.gov, fema.gov             |
| Drupal:10                   |      47 | atf.gov, cancer.gov, doi.gov              |
| USWDS                       |      42 | data.gov, energy.gov, epa.gov             |
| Bootstrap                   |      42 | archives.gov, cancer.gov, cdc.gov         |
| Acquia Cloud Platform:next  |      40 | atf.gov, cancer.gov, doi.gov              |
| jsDelivr                    |      39 | cancer.gov, data.gov, doi.gov             |
| Java                        |      39 | atf.gov, cancer.gov, cisa.gov             |
| Varnish                     |      36 | atf.gov, hiv.gov, justice.gov             |
| F5 BigIP                    |      36 | bjs.gov, cancer.gov, commerce.gov         |
| cdnjs                       |      35 | cancer.gov, energy.gov, epa.gov           |
| jQuery CDN                  |      27 | cancer.gov, energy.gov, fws.gov           |
| Microsoft HTTPAPI:2.0       |      25 | cdc.gov, doe.gov, dot.gov                 |
| Google Cloud                |      24 | cancer.gov, clinicaltrials.gov, doe.gov   |
| Microsoft ASP.NET:4.0.30319 |      22 | cdc.gov, energy.gov, epa.gov              |
| DataTables                  |      22 | cdc.gov, data.gov, nist.gov               |
| Ruby                        |      20 | commerce.gov, energy.gov, login.gov       |
| Ruby on Rails               |      20 | commerce.gov, energy.gov, login.gov       |
| Google Cloud CDN            |      20 | clinicaltrials.gov, doe.gov, doi.gov      |
<!-- END:tech-table -->

---

## Repository Structure

```
data/
├── us-fed-gov-agencies.csv         Federal agency ASN list
├── us-state-gov-agencies.csv       State government ASN list
├── us-city-gov-agencies.csv        City government ASN list
├── us-academics.csv                Academic institution ASN list
├── us-hospital-systems.csv         Hospital system ASN list
├── us-health-insurance.csv         Health insurer ASN list
├── us-pharmacy-benefit-managers.csv  PBM ASN list
├── us-health-it-vendors.csv        Health IT vendor ASN list
├── asn/
│   ├── fed-gov-prefixes.csv        Announced IP prefixes — federal
│   ├── state-gov-prefixes.csv      Announced IP prefixes — states
│   ├── city-gov-prefixes.csv       Announced IP prefixes — cities
│   ├── hospitals-prefixes.csv      Announced IP prefixes — hospitals
│   ├── insurance-prefixes.csv      Announced IP prefixes — insurers
│   ├── pbm-prefixes.csv            Announced IP prefixes — PBMs
│   ├── health-it-prefixes.csv      Announced IP prefixes — health IT
│   └── academic-prefixes.csv       Announced IP prefixes — academia
├── raw/                            Raw crt.sh JSON per domain
├── csv/                            Parsed domain lists per agency
└── tech/                           httpx technology fingerprints per domain
scripts/
├── fetch_asn_prefixes.py           Fetches BGP prefix data from RIPE Stat
└── generate_readme.py              Regenerates auto-updated README sections
```

## Related Resources

- [ARIN Whois](https://search.arin.net/rdap/)
- [RIPE Stat](https://stat.ripe.net)
- [bgp.potaroo.net ASN list](https://bgp.potaroo.net/cidr/autnums.html)
- [Cloudflare Radar ASN lookup](https://radar.cloudflare.com/routing)
- [RADB route lookup](https://www.radb.net/query)
- [CISA .gov domain registry](https://github.com/cisagov/dotgov-data)
