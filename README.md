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
_Last updated: 2026-06-23 10:07 UTC_
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
| Category                      | Organizations |          ASNs | IPv4 Prefixes | IPv6 Prefixes | Est. IPv4 Addresses |
| :---                          | ---:          | ---:          | ---:          | ---:          | ---:                |
| **Federal Agencies**          |            87 |            37 |         7,729 |           184 |              320.3M |
| **State Governments**         |            70 |            15 |         1,040 |            36 |                6.0M |
| **City Governments**          |            53 |  _53 tracked_ |             — |             — |                   — |
| **Hospital Systems**          |           544 | _544 tracked_ |             — |             — |                   — |
| **Health Insurers**           |            76 |  _76 tracked_ |             — |             — |                   — |
| **Pharmacy Benefit Managers** |            13 |  _13 tracked_ |             — |             — |                   — |
| **Health IT Vendors**         |            40 |  _40 tracked_ |             — |             — |                   — |
| **Academic Institutions**     |            20 |            20 |         1,231 |           107 |               27.3M |
<!-- END:overview-table -->

---

## Federal Agencies

Tracked in [`data/us-fed-gov-agencies.csv`](data/us-fed-gov-agencies.csv). Prefix data collected in [`data/asn/fed-gov-prefixes.csv`](data/asn/fed-gov-prefixes.csv).

<!-- BEGIN:fed-gov-table -->
| Abbrev  | Agency                                                 | ASNs | IPv4 Prefixes | IPv6 Prefixes | Est. IPv4 Addresses |
| :---    | :---                                                   | ---: | ---:          | ---:          | ---:                |
| AF      | Air Force Systems Networking                           |    2 |             — |             — |                   — |
| CBO     | Congressional Budget Office                            |    — |             — |             — |                   — |
| CDC     | Centers for Disease Control and Prevention (CDC)       |    1 |             2 |             — |               73.7K |
| CIA     | Central Intelligence Agency                            |    — |             — |             — |                   — |
| CNCS    | AmeriCorps                                             |    — |             — |             — |                   — |
| DHS     | Department of Homeland Security                        |    1 |             9 |             1 |               14.1K |
| DOC     | Department of Commerce - Bureau of Economic Analysis   |    2 |             3 |             3 |               66.0K |
| DOS-OIG | Department of State - Office of Inspector General      |    — |             — |             — |                   — |
| DoD     | Department of Defense - Network Information Center     |   10 |         7,261 |            95 |              314.9M |
| DoL     | U.S. Department of Labor                               |    — |             — |             — |                   — |
| DoT     | US Department of Transportation                        |    1 |            20 |            30 |              269.3K |
| EOP     | Executive Office of the President                      |    — |             — |             — |                   — |
| EPA     | Environmental Protection Agency (EPA)                  |    2 |             4 |             1 |              262.4K |
| EXIM    | Export-Import Bank of the United States                |    — |             — |             — |                   — |
| FAA     | Federal Aviation Administration                        |    — |             — |             — |                   — |
| FBI     | Federal Bureau of Investigation - CJIS Division        |    — |             — |             — |                   — |
| FDA     | Food and Drug Administration                           |    — |             — |             — |                   — |
| FDIC    | Federal Deposit Insurance Corporation                  |    — |             — |             — |                   — |
| FEC     | Federal Election Commission                            |    — |             — |             — |                   — |
| FERC    | Federal Energy Regulatory Commission                   |    — |             — |             — |                   — |
| FMSHRC  | Federal Mine Safety and Health Review Commission       |    — |             — |             — |                   — |
| FRB     | Federal Reserve Bank                                   |    — |             — |             — |                   — |
| FTC     | Federal Trade Commission                               |    — |             — |             — |                   — |
| GAO     | Government Accountability Office                       |    — |             — |             — |                   — |
| GPO     | Government Publishing Office                           |    — |             — |             — |                   — |
| GSA     | General Services Administration (GSA)                  |    1 |             — |             — |                   — |
| HHS     | US Department of Health and Human Services             |    2 |            28 |             6 |              381.7K |
| HHS-OIG | HHS Office of Inspector General                        |    — |             — |             — |                   — |
| HUD-OIG | HUD Office of Inspector General                        |    — |             — |             — |                   — |
| IHS     | Indian Health Service                                  |    — |             — |             — |                   — |
| IRS     | Internal Revenue Service                               |    1 |            13 |             4 |               13.6K |
| LOC     | Library of Congress                                    |    — |             — |             — |                   — |
| NARA    | National Archives and Records Administration           |    — |             — |             — |                   — |
| NASA    | National Aeronautics and Space Administration (NASA)   |    2 |           217 |             1 |                2.9M |
| NCUA    | National Credit Union Administration                   |    — |             — |             — |                   — |
| NGA     | National Gallery of Art                                |    — |             — |             — |                   — |
| NIH     | National Institutes of Health                          |    1 |            15 |             1 |              345.9K |
| NIST    | National Institute of Standards and Technology         |    — |             — |             — |                   — |
| NOAA    | National Oceanic and Atmospheric Administration (NOAA) |    2 |            85 |            26 |              337.9K |
| NRC     | Nuclear Regulatory Commission                          |    — |             — |             — |                   — |
| NSF     | National Science Foundation                            |    — |             — |             — |                   — |
| OPM     | Office of Personnel Management                         |    — |             — |             — |                   — |
| PBGC    | Pension Benefit Guaranty Corporation                   |    — |             — |             — |                   — |
| PC      | Peace Corps                                            |    — |             — |             — |                   — |
| SBA     | Small Business Administration                          |    — |             — |             — |                   — |
| SEC     | U.S. Securities and Exchange Commission                |    — |             — |             — |                   — |
| SI      | Smithsonian Institution                                |    — |             — |             — |                   — |
| SSA     | Social Security Administration                         |    1 |            13 |             6 |               54.0K |
| SSS     | Selective Service System                               |    — |             — |             — |                   — |
| STB     | Surface Transportation Board                           |    — |             — |             — |                   — |
| USAID   | U.S. Agency for International Development              |    — |             — |             — |                   — |
| USAISC  | United States (USAISC)                                 |    3 |             — |             — |                   — |
| USDA    | Department of Agriculture                              |    1 |             — |             — |                   — |
| USHMM   | United States Holocaust Memorial Museum                |    — |             — |             — |                   — |
| USPS    | United States Postal Service (USPS)                    |    3 |            34 |             2 |              335.4K |
| USPTO   | United States Patent and Trademark Office              |    — |             — |             — |                   — |
| VA      | Department of Veterans Affairs                         |    1 |            25 |             8 |              332.8K |
<!-- END:fed-gov-table -->

---

## State Governments

Tracked in [`data/us-state-gov-agencies.csv`](data/us-state-gov-agencies.csv). Prefix data in [`data/asn/state-gov-prefixes.csv`](data/asn/state-gov-prefixes.csv).

<!-- BEGIN:state-gov-table -->
| Organization                                              | ASNs | IPv4 Prefixes | IPv6 Prefixes | Est. IPv4 Addresses |
| :---                                                      | ---: | ---:          | ---:          | ---:                |
| California Department of Technology                       |    1 |            20 |             — |              135.7K |
| Commonwealth of Massachusetts                             |    — |             — |             — |                   — |
| Commonwealth of Virginia                                  |    — |             — |             — |                   — |
| Commonwealth of Virginia Office of the Attorney General   |    — |             — |             — |                   — |
| Florida Department of Management Services                 |    1 |           805 |            22 |              896.8K |
| Georgia Technology Authority                              |    — |             — |             — |                   — |
| Indiana Office of Technology                              |    — |             — |             — |                   — |
| Iowa Communications Network                               |    1 |            14 |             3 |              386.8K |
| Maryland Administrative Office of the Courts              |    — |             — |             — |                   — |
| Maryland Information Technology Center                    |    — |             — |             — |                   — |
| Michigan State Government                                 |    1 |             9 |             — |              508.2K |
| Mississippi Department of Information Technology Services |    — |             — |             — |                   — |
| NJOIT New Jersey Office of Information Technology         |    — |             — |             — |                   — |
| Network Nebraska                                          |    1 |            32 |             2 |              294.7K |
| North Carolina Administrative Office of the Courts        |    — |             — |             — |                   — |
| State of Alabama Office of Information Technology         |    — |             — |             — |                   — |
| State of Alaska                                           |    — |             — |             — |                   — |
| State of Arizona                                          |    — |             — |             — |                   — |
| State of Arkansas                                         |    1 |            12 |             — |              370.4K |
| State of California Department of Food and Agriculture    |    — |             — |             — |                   — |
| State of California Department of Motor Vehicles          |    — |             — |             — |                   — |
| State of California Department of Technology              |    — |             — |             — |                   — |
| State of Connecticut Department of Information Technology |    — |             — |             — |                   — |
| State of Connecticut Judicial Branch                      |    — |             — |             — |                   — |
| State of Delaware                                         |    — |             — |             — |                   — |
| State of Hawaii                                           |    1 |            10 |             — |                6.1K |
| State of Idaho                                            |    — |             — |             — |                   — |
| State of Idaho Department of Health and Welfare           |    — |             — |             — |                   — |
| State of Indiana                                          |    — |             — |             — |                   — |
| State of Iowa OCIO                                        |    — |             — |             — |                   — |
| State of Kansas                                           |    — |             — |             — |                   — |
| State of Louisiana Office of Technology Services          |    — |             — |             — |                   — |
| State of Louisiana Supreme Court                          |    — |             — |             — |                   — |
| State of Maine                                            |    — |             — |             — |                   — |
| State of Minnesota                                        |    1 |            10 |             1 |              230.9K |
| State of Missouri Office of Administration                |    — |             — |             — |                   — |
| State of Montana                                          |    — |             — |             — |                   — |
| State of Nebraska Office of the CIO                       |    — |             — |             — |                   — |
| State of Nevada                                           |    — |             — |             — |                   — |
| State of Nevada Legislature                               |    — |             — |             — |                   — |
| State of New Hampshire                                    |    — |             — |             — |                   — |
| State of New Jersey Judiciary                             |    — |             — |             — |                   — |
| State of New Mexico                                       |    — |             — |             — |                   — |
| State of North Carolina                                   |    1 |             9 |             — |              410.4K |
| State of North Dakota ITD                                 |    — |             — |             — |                   — |
| State of North Dakota Information Technology Department   |    — |             — |             — |                   — |
| State of Oregon                                           |    — |             — |             — |                   — |
| State of Rhode Island                                     |    — |             — |             — |                   — |
| State of Rhode Island General Assembly                    |    — |             — |             — |                   — |
| State of South Carolina                                   |    — |             — |             — |                   — |
| State of Tennessee                                        |    — |             — |             — |                   — |
| State of Utah                                             |    1 |             9 |             — |              395.8K |
| State of Utah Courts                                      |    — |             — |             — |                   — |
| State of WI Dept. of Administration                       |    1 |            39 |             1 |              786.2K |
| State of Washington                                       |    1 |            32 |             1 |              656.9K |
| State of Washington Legislative Service Center            |    — |             — |             — |                   — |
| State of Wisconsin Investment Board                       |    — |             — |             — |                   — |
| State of Wyoming Department                               |    1 |            15 |             1 |              595.2K |
| Tennessee Valley Authority                                |    1 |            15 |             1 |              264.4K |
| University of Maryland                                    |    1 |             9 |             4 |               12.5K |
| Virginia Information Technologies Agency                  |    — |             — |             — |                   — |
<!-- END:state-gov-table -->

---

## City Governments

Tracked in [`data/us-city-gov-agencies.csv`](data/us-city-gov-agencies.csv). Prefix data in [`data/asn/city-gov-prefixes.csv`](data/asn/city-gov-prefixes.csv).

<!-- BEGIN:city-gov-table -->
| City / Organization                                      | State | ASNs | IPv4 Prefixes | IPv6 Prefixes | Est. IPv4 Addresses |
| :---                                                     | :---  | ---: | ---:          | ---:          | ---:                |
| City and County of Denver                                | CO    |    — |             — |             — |                   — |
| City and County of Honolulu                              | HI    |    — |             — |             — |                   — |
| City and County of San Francisco                         | CA    |    — |             — |             — |                   — |
| City of Albuquerque                                      | NM    |    — |             — |             — |                   — |
| City of Austin                                           | TX    |    — |             — |             — |                   — |
| City of Austin Public Safety                             | TX    |    — |             — |             — |                   — |
| City of Baltimore Mayor Office of Information Technology | MD    |    — |             — |             — |                   — |
| City of Boston                                           | MA    |    — |             — |             — |                   — |
| City of Charlotte                                        | NC    |    — |             — |             — |                   — |
| City of Chicago                                          | IL    |    — |             — |             — |                   — |
| City of Columbus                                         | OH    |    — |             — |             — |                   — |
| City of Dallas                                           | TX    |    — |             — |             — |                   — |
| City of Detroit                                          | MI    |    — |             — |             — |                   — |
| City of Houston                                          | TX    |    — |             — |             — |                   — |
| City of Houston Public Works                             | TX    |    — |             — |             — |                   — |
| City of Indianapolis                                     | IN    |    — |             — |             — |                   — |
| City of Jacksonville                                     | FL    |    — |             — |             — |                   — |
| City of Kansas City                                      | MO    |    — |             — |             — |                   — |
| City of Las Vegas                                        | NV    |    — |             — |             — |                   — |
| City of Los Angeles                                      | CA    |    — |             — |             — |                   — |
| City of Memphis                                          | TN    |    — |             — |             — |                   — |
| City of Miami                                            | FL    |    — |             — |             — |                   — |
| City of New Orleans                                      | LA    |    — |             — |             — |                   — |
| City of New York                                         | NY    |    — |             — |             — |                   — |
| City of New York Public Safety                           | NY    |    — |             — |             — |                   — |
| City of Philadelphia                                     | PA    |    — |             — |             — |                   — |
| City of Phoenix                                          | AZ    |    — |             — |             — |                   — |
| City of Pittsburgh                                       | PA    |    — |             — |             — |                   — |
| City of Portland                                         | OR    |    — |             — |             — |                   — |
| City of Raleigh                                          | NC    |    — |             — |             — |                   — |
| City of Sacramento                                       | CA    |    — |             — |             — |                   — |
| City of San Antonio                                      | TX    |    — |             — |             — |                   — |
| City of San Diego                                        | CA    |    — |             — |             — |                   — |
| City of San Jose                                         | CA    |    — |             — |             — |                   — |
| City of Seattle                                          | WA    |    — |             — |             — |                   — |
| City of Seattle City Light                               | WA    |    — |             — |             — |                   — |
| City of Tampa                                            | FL    |    — |             — |             — |                   — |
| City of Tucson                                           | AZ    |    — |             — |             — |                   — |
| City of Tucson Wireless                                  | AZ    |    — |             — |             — |                   — |
| Denver International Airport                             | CO    |    — |             — |             — |                   — |
| Government of the District of Columbia                   | DC    |    — |             — |             — |                   — |
| Louisville Jefferson County Metro Government             | KY    |    — |             — |             — |                   — |
| New York City Board of Education                         | NY    |    — |             — |             — |                   — |
| New York City Board of Elections                         | NY    |    — |             — |             — |                   — |
| New York City Employees Retirement System                | NY    |    — |             — |             — |                   — |
| New York City Health and Hospitals Corporation           | NY    |    — |             — |             — |                   — |
| New York City Police Department                          | NY    |    — |             — |             — |                   — |
| Salt Lake City Corporation                               | UT    |    — |             — |             — |                   — |
<!-- END:city-gov-table -->

---

## Health Industry

### Hospital Systems

Tracked in [`data/us-hospital-systems.csv`](data/us-hospital-systems.csv). Prefix data in [`data/asn/hospitals-prefixes.csv`](data/asn/hospitals-prefixes.csv).

<!-- BEGIN:hospitals-table -->
| Organization                                                                                            | ASNs | IPv4 Prefixes | IPv6 Prefixes | Est. IPv4 Addresses |
| :---                                                                                                    | ---: | ---:          | ---:          | ---:                |
| ACMH Hospital                                                                                           |    — |             — |             — |                   — |
| ADVENTIST HEALTH SYSTEM/SUNBELT, INC.                                                                   |    — |             — |             — |                   — |
| AMERICAN SOCIETY OF HEALTH SYSTEM PHARMACISTS                                                           |    — |             — |             — |                   — |
| ANNE ARUNDEL MEDICAL CENTER                                                                             |    — |             — |             — |                   — |
| ARKANSAS HEART HOSPITAL ENCORE                                                                          |    — |             — |             — |                   — |
| Adena Health System                                                                                     |    — |             — |             — |                   — |
| Adventist Health System Sunbelt Healthcare Corporation                                                  |    — |             — |             — |                   — |
| Akron General Medical Center                                                                            |    — |             — |             — |                   — |
| Alameda Health System                                                                                   |    — |             — |             — |                   — |
| Alaska Native Medical Center                                                                            |    — |             — |             — |                   — |
| Allegheny Health Network                                                                                |    — |             — |             — |                   — |
| Allina Health System, Inc.                                                                              |    — |             — |             — |                   — |
| American Hospital Association                                                                           |    — |             — |             — |                   — |
| Anderson Hospital                                                                                       |    — |             — |             — |                   — |
| Androscoggin Valley Hospital                                                                            |    — |             — |             — |                   — |
| Ann & Robert H. Lurie Children's Hospital of Chicago                                                    |    — |             — |             — |                   — |
| Arkansas Children's Hospital                                                                            |    — |             — |             — |                   — |
| Asante Health System                                                                                    |    — |             — |             — |                   — |
| Aspen Valley Hospital                                                                                   |    — |             — |             — |                   — |
| Atlantic Health System                                                                                  |    — |             — |             — |                   — |
| Atlanticare Health System Inc.                                                                          |    — |             — |             — |                   — |
| BANNER HEALTH                                                                                           |    — |             — |             — |                   — |
| BARRETT HOSPITAL AND HEALHCARE                                                                          |    — |             — |             — |                   — |
| BAXTER COUNTY REGIONAL HOSPITAL, INC                                                                    |    — |             — |             — |                   — |
| BJC HEALTH SYSTEM                                                                                       |    — |             — |             — |                   — |
| BRISTOL HOSPITAL INCORPORATED                                                                           |    — |             — |             — |                   — |
| BROADLAWNS MEDICAL CENTER                                                                               |    — |             — |             — |                   — |
| Baptist Health System                                                                                   |    — |             — |             — |                   — |
| Baptist Health System of Alabama                                                                        |    — |             — |             — |                   — |
| Baptist Healthcare System                                                                               |    — |             — |             — |                   — |
| Bartlett Regional Hospital                                                                              |    — |             — |             — |                   — |
| Bassett Medical Center                                                                                  |    — |             — |             — |                   — |
| Baycare Health System, Inc.                                                                             |    — |             — |             — |                   — |
| Bayhealth Medical Center, Inc.                                                                          |    — |             — |             — |                   — |
| Baylor Health Care System                                                                               |    — |             — |             — |                   — |
| Beacon Health System, Inc.                                                                              |    — |             — |             — |                   — |
| Beatrice Community Hospital and Health Center, Inc.                                                     |    — |             — |             — |                   — |
| Beebe Medical Center Inc.                                                                               |    — |             — |             — |                   — |
| Bellin Memorial Hospital, Inc.                                                                          |    — |             — |             — |                   — |
| Beloit Health System, Inc.                                                                              |    — |             — |             — |                   — |
| Benefis Health System                                                                                   |    — |             — |             — |                   — |
| Beth Israel Deaconess Medical Center                                                                    |    — |             — |             — |                   — |
| Bingham Memorial Hospital                                                                               |    — |             — |             — |                   — |
| Blessing Hospital                                                                                       |    — |             — |             — |                   — |
| Blythedale Children's Hospital                                                                          |    — |             — |             — |                   — |
| Boca Raton Regional Hospital Inc.                                                                       |    — |             — |             — |                   — |
| Boston Medical Center                                                                                   |    — |             — |             — |                   — |
| Boulder Community Hospital                                                                              |    — |             — |             — |                   — |
| Bradford Regional Medical Center                                                                        |    — |             — |             — |                   — |
| Brockton Hospital                                                                                       |    — |             — |             — |                   — |
| Butler Memorial Hospital                                                                                |    — |             — |             — |                   — |
| CAMC Health System, Inc.                                                                                |    — |             — |             — |                   — |
| CARE NEW ENGLAND HEALTH SYSTEM                                                                          |    — |             — |             — |                   — |
| CARILION HEALTH SYSTEM                                                                                  |    — |             — |             — |                   — |
| CGH Medical Center                                                                                      |    — |             — |             — |                   — |
| CHAMPLAIN VALLEY PHYSICIANS HOSPITAL MEDICAL CENTER                                                     |    — |             — |             — |                   — |
| CHILDRENS HOSPITAL OF ORANGE COUNTY                                                                     |    — |             — |             — |                   — |
| CalvertHealth Medical Center                                                                            |    — |             — |             — |                   — |
| Cameron Memorial Community Hospital Inc                                                                 |    — |             — |             — |                   — |
| Cape Fear Valley Medical Center                                                                         |    — |             — |             — |                   — |
| Cape Regional Medical Center, Inc.                                                                      |    — |             — |             — |                   — |
| Capital Health System, Inc                                                                              |    — |             — |             — |                   — |
| CarolinaEast Medical Center                                                                             |    — |             — |             — |                   — |
| Carolinas Healthcare System                                                                             |    — |             — |             — |                   — |
| Carson Tahoe Health System                                                                              |    — |             — |             — |                   — |
| Cass Regional Medical Center                                                                            |    — |             — |             — |                   — |
| Catawba Valley Medical Center                                                                           |    — |             — |             — |                   — |
| Catholic Medical Center                                                                                 |    — |             — |             — |                   — |
| Catskill Regional Medical Center                                                                        |    — |             — |             — |                   — |
| Central Vermont Medical Center                                                                          |    — |             — |             — |                   — |
| Centrastate Medical Center, Inc.                                                                        |    — |             — |             — |                   — |
| Chan Soon-Shiong Medical Center at Windber                                                              |    — |             — |             — |                   — |
| Chesapeake General Hospital                                                                             |    — |             — |             — |                   — |
| Children's Hospital & Health System, Inc.                                                               |    — |             — |             — |                   — |
| Children's Hospital & Medical Center                                                                    |    — |             — |             — |                   — |
| Children's Hospital Colorado                                                                            |    — |             — |             — |                   — |
| Children's Hospital Los Angeles                                                                         |    — |             — |             — |                   — |
| Children's Hospital Medical Center of Akron                                                             |    — |             — |             — |                   — |
| Children's Hospital of The King's Daughters Health System                                               |    — |             — |             — |                   — |
| Children's Medical Center of Dallas                                                                     |    — |             — |             — |                   — |
| Children's National Hospital                                                                            |    — |             — |             — |                   — |
| Childrens Hospital and Regional Medical Center                                                          |    — |             — |             — |                   — |
| Christus Health                                                                                         |    — |             — |             — |                   — |
| Cincinnati Children's Hospital Medical Center                                                           |    — |             — |             — |                   — |
| Citizens Medical Center                                                                                 |    — |             — |             — |                   — |
| City of Hope Medical Center                                                                             |    — |             — |             — |                   — |
| Cleveland Clinic Foundation                                                                             |    — |             — |             — |                   — |
| Columbia Basin Hospital                                                                                 |    — |             — |             — |                   — |
| Columbia Memorial Hospital                                                                              |    — |             — |             — |                   — |
| Columbia/HCA Healthcare, Inc.                                                                           |    — |             — |             — |                   — |
| Columbus Community Hospital, Inc.                                                                       |    — |             — |             — |                   — |
| Columbus Regional Hospital                                                                              |    — |             — |             — |                   — |
| Comanche County Memorial Hospital                                                                       |    — |             — |             — |                   — |
| CommonSpirit Health                                                                                     |    — |             — |             — |                   — |
| Community Health Network of Connecticut                                                                 |    — |             — |             — |                   — |
| Community Hospital of the Monterey Peninsula                                                            |    — |             — |             — |                   — |
| Community Medical Center, Inc                                                                           |    — |             — |             — |                   — |
| Community Memorial Health System                                                                        |    — |             — |             — |                   — |
| Concord Hospital                                                                                        |    — |             — |             — |                   — |
| Concord Hospital - Laconia                                                                              |    — |             — |             — |                   — |
| Connecticut Children's Medical Center                                                                   |    — |             — |             — |                   — |
| Connecticut Hospital Assoc.                                                                             |    — |             — |             — |                   — |
| Cook Children's Health Care System                                                                      |    — |             — |             — |                   — |
| Cooley Dickinson Hospital                                                                               |    — |             — |             — |                   — |
| Cooper University Hospital                                                                              |    — |             — |             — |                   — |
| Covenant Medical Center, Inc.                                                                           |    — |             — |             — |                   — |
| Crouse Hospital                                                                                         |    — |             — |             — |                   — |
| DEACONESS HOSPITAL, Inc.                                                                                |    — |             — |             — |                   — |
| Danbury Hospital - ITG                                                                                  |    — |             — |             — |                   — |
| Dartmouth Hitchcock Medical Center                                                                      |    — |             — |             — |                   — |
| Dartmouth-Hitchcock Medical Center                                                                      |    — |             — |             — |                   — |
| Day Kimball Hospital                                                                                    |    — |             — |             — |                   — |
| Dayton Children's Hospital                                                                              |    — |             — |             — |                   — |
| Dayton General Hospital                                                                                 |    — |             — |             — |                   — |
| Dekalb Medical Center                                                                                   |    — |             — |             — |                   — |
| Delta County Memorial Hospital                                                                          |    — |             — |             — |                   — |
| Denver Health and Hospital Authority                                                                    |    — |             — |             — |                   — |
| Detroit Medical Center                                                                                  |    — |             — |             — |                   — |
| Dignity Health                                                                                          |    — |             — |             — |                   — |
| Dignity Health, Yavapai Regional Medical Center                                                         |    — |             — |             — |                   — |
| Doylestown Hospital                                                                                     |    — |             — |             — |                   — |
| Driscoll Children's Hospital                                                                            |    — |             — |             — |                   — |
| DuBois Regional Medical Center                                                                          |    — |             — |             — |                   — |
| ECTOR COUNTY HOSPITAL DISTRICT                                                                          |    — |             — |             — |                   — |
| EMANUEL MEDICAL CENTER, INC                                                                             |    — |             — |             — |                   — |
| ENLOE MEDICAL CENTER                                                                                    |    — |             — |             — |                   — |
| East Alabama Medical Center                                                                             |    — |             — |             — |                   — |
| Egleston Children's Hospital                                                                            |    — |             — |             — |                   — |
| Eisenhower Medical Center                                                                               |    — |             — |             — |                   — |
| Elliot Health System                                                                                    |    — |             — |             — |                   — |
| Englewood Hospital and Medical Center                                                                   |    — |             — |             — |                   — |
| Ephrata Community Hospital                                                                              |    — |             — |             — |                   — |
| Erie County Medical Center                                                                              |    — |             — |             — |                   — |
| Essentia Health East                                                                                    |    — |             — |             — |                   — |
| Evangelical Community Hospital                                                                          |    — |             — |             — |                   — |
| Exeter Hospital                                                                                         |    — |             — |             — |                   — |
| F.F. Thompson Health System, Inc.                                                                       |    — |             — |             — |                   — |
| FAIRFIELD MEDICAL CENTER                                                                                |    — |             — |             — |                   — |
| Finger Lakes Regional Health System, Inc.                                                               |    — |             — |             — |                   — |
| Firelands Regional Medical Center                                                                       |    — |             — |             — |                   — |
| Fisher-Titus Medical Center                                                                             |    — |             — |             — |                   — |
| Flagler Hospital, Inc                                                                                   |    — |             — |             — |                   — |
| Forrest County General Hospital                                                                         |    — |             — |             — |                   — |
| Frederick Memorial Healthcare System                                                                    |    — |             — |             — |                   — |
| Freeman Health System                                                                                   |    — |             — |             — |                   — |
| Froedtert Memorial Lutheran Hospital, Inc.                                                              |    — |             — |             — |                   — |
| Froedtert South, Inc.                                                                                   |    — |             — |             — |                   — |
| Fulton County Medical Center                                                                            |    — |             — |             — |                   — |
| GENERAL HEALTH SYSTEM                                                                                   |    — |             — |             — |                   — |
| GUADALUPE REGIONAL MEDICAL CENTER                                                                       |    — |             — |             — |                   — |
| Geisinger Jersey Shore Hospital                                                                         |    — |             — |             — |                   — |
| Geisinger System Services                                                                               |    — |             — |             — |                   — |
| Genesis Health System                                                                                   |    — |             — |             — |                   — |
| Genesis Healthcare System                                                                               |    — |             — |             — |                   — |
| Gila Regional Medical Center                                                                            |    — |             — |             — |                   — |
| Glens Falls Hospital                                                                                    |    — |             — |             — |                   — |
| Good Samaritan Hospital                                                                                 |    — |             — |             — |                   — |
| Good Shepherd Medical Center                                                                            |    — |             — |             — |                   — |
| Grady Memorial Hospital                                                                                 |    — |             — |             — |                   — |
| Graham Health System                                                                                    |    — |             — |             — |                   — |
| Grand Island Regional Medical Center                                                                    |    — |             — |             — |                   — |
| Grande Ronde Hospital, Inc.                                                                             |    — |             — |             — |                   — |
| Greater Baltimore Medical Center Inc                                                                    |    — |             — |             — |                   — |
| Greater Regional Medical Center                                                                         |    — |             — |             — |                   — |
| Gundersen Lutheran Medical Center, Inc.                                                                 |    — |             — |             — |                   — |
| Gunnison Valley Hospital                                                                                |    — |             — |             — |                   — |
| Guthrie Healthcare System                                                                               |    — |             — |             — |                   — |
| H. Lee Moffitt Cancer Center & Research Institute, Inc.                                                 |    — |             — |             — |                   — |
| HEALTH AND HOSPITAL CORPORATION OF MARION COUNTY                                                        |    — |             — |             — |                   — |
| HUNTSVILLE MEMORIAL HOSPITAL                                                                            |    — |             — |             — |                   — |
| Hackensack University Medical Center                                                                    |    — |             — |             — |                   — |
| Halifax Regional Hospital                                                                               |    — |             — |             — |                   — |
| Harbor Regional Health Community Hospital                                                               |    — |             — |             — |                   — |
| Harlan County Health System                                                                             |    — |             — |             — |                   — |
| Harris County Hospital District                                                                         |    — |             — |             — |                   — |
| Hartford Hospital                                                                                       |    — |             — |             — |                   — |
| Hays Medical Center                                                                                     |    — |             — |             — |                   — |
| Heart of the Rockies Regional Medical Center                                                            |    — |             — |             — |                   — |
| Heartland Regional Medical Center                                                                       |    — |             — |             — |                   — |
| Hendrick Medical Center                                                                                 |    — |             — |             — |                   — |
| Hennepin County Medical Center                                                                          |    — |             — |             — |                   — |
| Henry Ford Health System                                                                                |    — |             — |             — |                   — |
| Henry Mayo Newhall Memorial Hospital                                                                    |    — |             — |             — |                   — |
| Heritage Valley Health System                                                                           |    — |             — |             — |                   — |
| Holzer Health System                                                                                    |    — |             — |             — |                   — |
| Hospital Billing and Collection Service, LTD                                                            |    — |             — |             — |                   — |
| Hospital Sisters Health Systems                                                                         |    — |             — |             — |                   — |
| Hospital for Special Care                                                                               |    — |             — |             — |                   — |
| Hospital for Special Surgery                                                                            |    — |             — |             — |                   — |
| Houlton Regional Hospital                                                                               |    — |             — |             — |                   — |
| Howard University Hospital                                                                              |    — |             — |             — |                   — |
| Hugh Chatham Memorial Hospital, Inc.                                                                    |    — |             — |             — |                   — |
| Huntington Memorial Hospital                                                                            |    — |             — |             — |                   — |
| Huntsville Hospital                                                                                     |    — |             — |             — |                   — |
| Hurley Medical Center                                                                                   |    — |             — |             — |                   — |
| Hutchinson Regional Medical Center                                                                      |    — |             — |             — |                   — |
| IMMANUEL MEDICAL CENTER                                                                                 |    — |             — |             — |                   — |
| Independent Health Network, Inc.                                                                        |    — |             — |             — |                   — |
| Indiana Regional Medical Center                                                                         |    — |             — |             — |                   — |
| Infirmary Health System, Inc.                                                                           |    — |             — |             — |                   — |
| Inova Health System Foundation                                                                          |    — |             — |             — |                   — |
| Intermountain Health Care, Inc.                                                                         |    — |             — |             — |                   — |
| Jackson County Memorial Hospital                                                                        |    — |             — |             — |                   — |
| Jackson Memorial Hospital, Public Health                                                                |    — |             — |             — |                   — |
| Joan and Sanford I. Weill Medical College and Graduate School of Medical Sciences of Cornell University |    — |             — |             — |                   — |
| Kadlec Regional Medical Center                                                                          |    — |             — |             — |                   — |
| Kaiser Foundation Health Plan, Inc.                                                                     |    — |             — |             — |                   — |
| Kearney Regional Medical Center LLC                                                                     |    — |             — |             — |                   — |
| Kettering Medical Center                                                                                |    — |             — |             — |                   — |
| Kingman Regional Medical Center                                                                         |    — |             — |             — |                   — |
| Kings Daughters Medical Center                                                                          |    — |             — |             — |                   — |
| Kootenai Medical Center                                                                                 |    — |             — |             — |                   — |
| Kuakini Medical Center                                                                                  |    — |             — |             — |                   — |
| LSU Health Sciences Center                                                                              |    — |             — |             — |                   — |
| LSU Health Sciences Center - Shreveport                                                                 |    — |             — |             — |                   — |
| LUCILE SALTER PACKARD CHILDREN'S HOSPITAL AT STANFORD                                                   |    — |             — |             — |                   — |
| La Rabida Hospital                                                                                      |    — |             — |             — |                   — |
| Lake Charles Memorial Hospital                                                                          |    — |             — |             — |                   — |
| Lane Regional Medical Center                                                                            |    — |             — |             — |                   — |
| Lee Memorial Health System                                                                              |    — |             — |             — |                   — |
| Lexington Medical Center                                                                                |    — |             — |             — |                   — |
| Licking Memorial Hospital                                                                               |    — |             — |             — |                   — |
| Lima Memorial Hospital                                                                                  |    — |             — |             — |                   — |
| Littleton Regional Hospital                                                                             |    — |             — |             — |                   — |
| Logan Health Medical Center                                                                             |    — |             — |             — |                   — |
| Loma Linda University Medical Center                                                                    |    — |             — |             — |                   — |
| Lower Umpqua Hospital District                                                                          |    — |             — |             — |                   — |
| Luthern General Health System                                                                           |    — |             — |             — |                   — |
| MARY GREELEY MEDICAL CENTER                                                                             |    — |             — |             — |                   — |
| MERCY MEDICAL CENTER                                                                                    |    — |             — |             — |                   — |
| MIDDLESEX HEALTH SYSTEM, INC.                                                                           |    — |             — |             — |                   — |
| MJHS Health System                                                                                      |    — |             — |             — |                   — |
| Madison Co Memorial Hospital                                                                            |    — |             — |             — |                   — |
| Madonna Rehabilitation Hospital                                                                         |    — |             — |             — |                   — |
| Maimonides Medical Center                                                                               |    — |             — |             — |                   — |
| MaineHealth Maine Medical Center                                                                        |    — |             — |             — |                   — |
| Marcus Daly Memorial Hospital Corporation                                                               |    — |             — |             — |                   — |
| Maricopa Integrated Health System                                                                       |    — |             — |             — |                   — |
| Marin General Hospital                                                                                  |    — |             — |             — |                   — |
| Marion General Hospital, Inc.                                                                           |    — |             — |             — |                   — |
| Marshfield Clinic Inc.                                                                                  |    — |             — |             — |                   — |
| Mary Washington Hospital, Inc.                                                                          |    — |             — |             — |                   — |
| Mass General Brigham Incorporated                                                                       |    — |             — |             — |                   — |
| Massachusetts Health & Hospital Association, Inc.                                                       |    — |             — |             — |                   — |
| Maury Regional Hospital                                                                                 |    — |             — |             — |                   — |
| Mayo Foundation for Medical Education and Research                                                      |    — |             — |             — |                   — |
| Meadville Medical Center                                                                                |    — |             — |             — |                   — |
| Medical College of Wisconsin                                                                            |    — |             — |             — |                   — |
| Medisys Health Network, Inc.                                                                            |    — |             — |             — |                   — |
| Meharry Medical College                                                                                 |    — |             — |             — |                   — |
| Melissa Memorial Hospital                                                                               |    — |             — |             — |                   — |
| Memorial Health Care System                                                                             |    — |             — |             — |                   — |
| Memorial Hermann Health System                                                                          |    — |             — |             — |                   — |
| Memorial Hospital                                                                                       |    — |             — |             — |                   — |
| Memorial Hospital and Health Care Center                                                                |    — |             — |             — |                   — |
| Memorial Hospital at Gulfport                                                                           |    — |             — |             — |                   — |
| Memorial Hospital of Sweetwater County Foundation                                                       |    — |             — |             — |                   — |
| Memorial Medical Center                                                                                 |    — |             — |             — |                   — |
| Memorial Sloan-Kettering Cancer Center                                                                  |    — |             — |             — |                   — |
| MemorialCare Health System                                                                              |    — |             — |             — |                   — |
| Mercy Medical Center                                                                                    |    — |             — |             — |                   — |
| Meridian Health System                                                                                  |    — |             — |             — |                   — |
| Meritus Medical Center, Inc.                                                                            |    — |             — |             — |                   — |
| Methodist Health System                                                                                 |    — |             — |             — |                   — |
| Methodist Hospital of Memphis                                                                           |    — |             — |             — |                   — |
| Methodist Hospital of Southern California                                                               |    — |             — |             — |                   — |
| Miami Children's Hospital                                                                               |    — |             — |             — |                   — |
| Midland County Hospital District                                                                        |    — |             — |             — |                   — |
| Milford Regional Medical Center Inc.                                                                    |    — |             — |             — |                   — |
| Mille Lacs Health System                                                                                |    — |             — |             — |                   — |
| Montefiore Medical Center                                                                               |    — |             — |             — |                   — |
| Montgomery County Hospital District                                                                     |    — |             — |             — |                   — |
| Montrose Memorial Hospital                                                                              |    — |             — |             — |                   — |
| Monument Health Rapid City Hospital, Inc.                                                               |    — |             — |             — |                   — |
| Morris Hospital                                                                                         |    — |             — |             — |                   — |
| Mother Frances Hospital Regional Health Care Center                                                     |    — |             — |             — |                   — |
| Mount Nittany Medical Center                                                                            |    — |             — |             — |                   — |
| Mount Sinai Medical Center of Florida, Inc.                                                             |    — |             — |             — |                   — |
| Mt San Rafael Hospital                                                                                  |    — |             — |             — |                   — |
| MultiCare Health System                                                                                 |    — |             — |             — |                   — |
| Murray-Calloway County Hospital                                                                         |    — |             — |             — |                   — |
| NCH Healthcare System, Inc.                                                                             |    — |             — |             — |                   — |
| NORTHEASTERN VERMONT REGIONAL HOSPITAL, INC.                                                            |    — |             — |             — |                   — |
| Nanticoke Memorial Hospital INC                                                                         |    — |             — |             — |                   — |
| Nashville General Hospital                                                                              |    — |             — |             — |                   — |
| Nationwide Children's Hospital                                                                          |    — |             — |             — |                   — |
| Natividad Medical Center                                                                                |    — |             — |             — |                   — |
| Nebraska Methodist Health System, Inc.                                                                  |    — |             — |             — |                   — |
| New Bridge Medical Center                                                                               |    — |             — |             — |                   — |
| New England Baptist Hospital                                                                            |    — |             — |             — |                   — |
| New Liberty Hospital District of Clay County, Missouri                                                  |    — |             — |             — |                   — |
| New York Medical College                                                                                |    — |             — |             — |                   — |
| NewYork-Presbyterian Hospital                                                                           |    — |             — |             — |                   — |
| Norman Regional Health System                                                                           |    — |             — |             — |                   — |
| North Broward Hospital District                                                                         |    — |             — |             — |                   — |
| North Kansas City Hospital Auxiliary                                                                    |    — |             — |             — |                   — |
| North Mississippi Medical Center Inc.                                                                   |    — |             — |             — |                   — |
| North Oaks Health System                                                                                |    — |             — |             — |                   — |
| North Shore Long Island Jewish Health System                                                            |    — |             — |             — |                   — |
| North Valley Hospital                                                                                   |    — |             — |             — |                   — |
| NorthWestern Medical Center                                                                             |    — |             — |             — |                   — |
| Northeast Alabama Regional Medical Center                                                               |    — |             — |             — |                   — |
| Northeast Georgia Medical Center, Inc.                                                                  |    — |             — |             — |                   — |
| Northern Hospital District of Surry County                                                              |    — |             — |             — |                   — |
| Northside Hospital                                                                                      |    — |             — |             — |                   — |
| Northwest Community Hospital                                                                            |    — |             — |             — |                   — |
| Northwestern Memorial Hospital                                                                          |    — |             — |             — |                   — |
| OLEAN GENERAL HOSPITAL                                                                                  |    — |             — |             — |                   — |
| OSF Healthcare System                                                                                   |    — |             — |             — |                   — |
| OhioHealth Corporation                                                                                  |    — |             — |             — |                   — |
| Oklahoma Heart Hospital, LLC                                                                            |    — |             — |             — |                   — |
| Orange Regional Medical Center                                                                          |    — |             — |             — |                   — |
| Oregon Health Network, Inc.                                                                             |    — |             — |             — |                   — |
| Orlando Health, INC                                                                                     |    — |             — |             — |                   — |
| Overlake Hospital Medical Center                                                                        |    — |             — |             — |                   — |
| PHOENIX CHILDREN'S HOSPITAL                                                                             |    — |             — |             — |                   — |
| Pagosa Springs Medical Center                                                                           |    — |             — |             — |                   — |
| Parkland Health & Hospital System                                                                       |    — |             — |             — |                   — |
| Parkview Hospital                                                                                       |    — |             — |             — |                   — |
| Parrish Medical Center                                                                                  |    — |             — |             — |                   — |
| Pender Community Hospital District                                                                      |    — |             — |             — |                   — |
| Peninsula Regional Medical Center                                                                       |    — |             — |             — |                   — |
| Penn Medicine                                                                                           |    — |             — |             — |                   — |
| Phelps County Regional Medical Center                                                                   |    — |             — |             — |                   — |
| Pikeville Medical Center                                                                                |    — |             — |             — |                   — |
| Pomona Valley Hospital Medical Center                                                                   |    — |             — |             — |                   — |
| Porter Hospital                                                                                         |    — |             — |             — |                   — |
| Pratt Regional Medical Center                                                                           |    — |             — |             — |                   — |
| Presence Health Network                                                                                 |    — |             — |             — |                   — |
| Prisma Health                                                                                           |    — |             — |             — |                   — |
| Providence Health & Services                                                                            |    — |             — |             — |                   — |
| Providence Health Plan                                                                                  |    — |             — |             — |                   — |
| Providence Hospital                                                                                     |    — |             — |             — |                   — |
| Punxsutawney Area Hospital                                                                              |    — |             — |             — |                   — |
| RIVERSIDE HEALTH SYSTEM                                                                                 |    — |             — |             — |                   — |
| RIVERVIEW HOSPITAL                                                                                      |    — |             — |             — |                   — |
| RWJBarnabas Health, Inc.                                                                                |    — |             — |             — |                   — |
| Rady Children's Hospital - San Diego                                                                    |    — |             — |             — |                   — |
| Reading Hospital                                                                                        |    — |             — |             — |                   — |
| Redlands Community Hospital                                                                             |    — |             — |             — |                   — |
| Reedsburg Area Medical Center Inc.                                                                      |    — |             — |             — |                   — |
| Renown Health                                                                                           |    — |             — |             — |                   — |
| Richmond Memorial Hospital                                                                              |    — |             — |             — |                   — |
| Ridgeview Medical Center                                                                                |    — |             — |             — |                   — |
| Robert Wood Johnson University Hospital                                                                 |    — |             — |             — |                   — |
| Rockford Health System                                                                                  |    — |             — |             — |                   — |
| Rush University Medical Center                                                                          |    — |             — |             — |                   — |
| SHORE MEMORIAL HOSPITAL                                                                                 |    — |             — |             — |                   — |
| SSM Health Care                                                                                         |    — |             — |             — |                   — |
| ST JOSEPH HOSPITAL                                                                                      |    — |             — |             — |                   — |
| ST. LUKE'S HEALTH SYSTEM, LTD.                                                                          |    — |             — |             — |                   — |
| ST. VINCENT HOSPITAL OF THE HOSPITAL SISTERS OF THE THIRD ORDER OF ST. FRANCIS                          |    — |             — |             — |                   — |
| SWEDISH MEDICAL CENTER                                                                                  |    — |             — |             — |                   — |
| SWEDISHAMERICAN HEALTH SYSTEM CORPORATION                                                               |    — |             — |             — |                   — |
| Sacred Heart Hospital                                                                                   |    — |             — |             — |                   — |
| Saint Bernard Hospital                                                                                  |    — |             — |             — |                   — |
| Saint Francis Health System                                                                             |    — |             — |             — |                   — |
| Saint Francis Hospital and Medical Center                                                               |    — |             — |             — |                   — |
| Saint Francis Medical Center                                                                            |    — |             — |             — |                   — |
| Saint Joseph's Hospital & Medical Center                                                                |    — |             — |             — |                   — |
| Saint Joseph's Hospital of Atlanta, Inc.                                                                |    — |             — |             — |                   — |
| Saint Luke's Health System                                                                              |    — |             — |             — |                   — |
| Saint Mary's Hospital, Inc.                                                                             |    — |             — |             — |                   — |
| Salem Hospital                                                                                          |    — |             — |             — |                   — |
| Salinas Valley Memorial Hospital                                                                        |    — |             — |             — |                   — |
| San Antonio Regional Hospital                                                                           |    — |             — |             — |                   — |
| San Juan Regional Medical Center Inc.                                                                   |    — |             — |             — |                   — |
| San Luis Valley Regional Medical Center                                                                 |    — |             — |             — |                   — |
| Sanford Health                                                                                          |    — |             — |             — |                   — |
| Sapient Health Network                                                                                  |    — |             — |             — |                   — |
| Sarasota Memorial Hospital                                                                              |    — |             — |             — |                   — |
| Saratoga Hospital                                                                                       |    — |             — |             — |                   — |
| Schneck Medical Center                                                                                  |    — |             — |             — |                   — |
| Scottish Rite Hospital for Children                                                                     |    — |             — |             — |                   — |
| Scripps Health                                                                                          |    — |             — |             — |                   — |
| Sentara Healthcare                                                                                      |    — |             — |             — |                   — |
| Shannon Medical Center                                                                                  |    — |             — |             — |                   — |
| Sierra View District Hospital                                                                           |    — |             — |             — |                   — |
| Silver Cross Hospital                                                                                   |    — |             — |             — |                   — |
| Sisters of Charity Hospital                                                                             |    — |             — |             — |                   — |
| Sisters of Mercy Health System                                                                          |    — |             — |             — |                   — |
| Sky Lakes Medical Center, Inc.                                                                          |    — |             — |             — |                   — |
| Southcoast Health System, Inc.                                                                          |    — |             — |             — |                   — |
| Southeast Alabama Medical Center                                                                        |    — |             — |             — |                   — |
| Southern Illinois Hospital Services                                                                     |    — |             — |             — |                   — |
| Southern Maine Medical Center                                                                           |    — |             — |             — |                   — |
| Southern New Hampshire Health System                                                                    |    — |             — |             — |                   — |
| Southern Tennessee Regional Health System Winchester                                                    |    — |             — |             — |                   — |
| Sparrow Health System                                                                                   |    — |             — |             — |                   — |
| Sparta Community Hospital                                                                               |    — |             — |             — |                   — |
| Spectrum Health                                                                                         |    — |             — |             — |                   — |
| Spring View Hospital                                                                                    |    — |             — |             — |                   — |
| Springhill Memorial Hospital                                                                            |    — |             — |             — |                   — |
| St Francis Healthcare System of Hawaii                                                                  |    — |             — |             — |                   — |
| St. Charles Health System, Inc.                                                                         |    — |             — |             — |                   — |
| St. Clair Memorial Hospital                                                                             |    — |             — |             — |                   — |
| St. Elizabeth Medical Center, Inc.                                                                      |    — |             — |             — |                   — |
| St. John's Riverside Hospital                                                                           |    — |             — |             — |                   — |
| St. Joseph Health System                                                                                |    — |             — |             — |                   — |
| St. Joseph Hospital                                                                                     |    — |             — |             — |                   — |
| St. Joseph's Medical Center                                                                             |    — |             — |             — |                   — |
| St. Josephs/Candler Health System, Inc.                                                                 |    — |             — |             — |                   — |
| St. Jude Children's Research Hospital                                                                   |    — |             — |             — |                   — |
| St. Luke's Hospital                                                                                     |    — |             — |             — |                   — |
| St. Luke's Roosevelt Hospital Center                                                                    |    — |             — |             — |                   — |
| St. Mary's Health System                                                                                |    — |             — |             — |                   — |
| St. Mary's Medical Center, Inc.                                                                         |    — |             — |             — |                   — |
| St. Vincent Hospital                                                                                    |    — |             — |             — |                   — |
| Stamford Hospital                                                                                       |    — |             — |             — |                   — |
| Stanford Hospital and Clinics                                                                           |    — |             — |             — |                   — |
| Steward Health Care System LLC                                                                          |    — |             — |             — |                   — |
| Straub Clinic & Hospital                                                                                |    — |             — |             — |                   — |
| Summa Health System                                                                                     |    — |             — |             — |                   — |
| Summit Healthcare Regional Medical Center                                                               |    — |             — |             — |                   — |
| Sutter Health                                                                                           |    — |             — |             — |                   — |
| Swedish Covenant Hospital                                                                               |    — |             — |             — |                   — |
| THE GOOD SAMARITAN HOSPITAL OF LEBANON, PENNSYLVANIA                                                    |    — |             — |             — |                   — |
| THE HARDIN MEMORIAL HOSPITAL FOUNDATION, INC.                                                           |    — |             — |             — |                   — |
| Tahoe Forest Hospital District                                                                          |    — |             — |             — |                   — |
| Tampa General Hospital                                                                                  |    — |             — |             — |                   — |
| Tanner Medical Center, Inc.                                                                             |    — |             — |             — |                   — |
| Tarrant County Hospital District                                                                        |    — |             — |             — |                   — |
| Telluride Medical Center                                                                                |    — |             — |             — |                   — |
| Temple University Health System, Inc.                                                                   |    — |             — |             — |                   — |
| Teton County Hospital District                                                                          |    — |             — |             — |                   — |
| Texas Children's Hospital                                                                               |    — |             — |             — |                   — |
| Texas Medical Center                                                                                    |    — |             — |             — |                   — |
| Texas Tech University Health Sciences Center                                                            |    — |             — |             — |                   — |
| Texas Tech University Health Sciences Center at El Paso                                                 |    — |             — |             — |                   — |
| The Brooklyn Hospital Center                                                                            |    — |             — |             — |                   — |
| The Children's Hospital Corporation                                                                     |    — |             — |             — |                   — |
| The Children's Hospital of Alabama                                                                      |    — |             — |             — |                   — |
| The Children's Hospital of Philadelphia                                                                 |    — |             — |             — |                   — |
| The Children's Mercy Hospital                                                                           |    — |             — |             — |                   — |
| The Harrison Memorrial Hospital, Inc.                                                                   |    — |             — |             — |                   — |
| The Health Care Authority for Baptist Health, An Affiliate of UAB Health System                         |    — |             — |             — |                   — |
| The Methodist Hospital                                                                                  |    — |             — |             — |                   — |
| The Milton S. Hershey Medical Center                                                                    |    — |             — |             — |                   — |
| The Moses H. Cone Memorial Hospital                                                                     |    — |             — |             — |                   — |
| The New London Hospital Association, Inc                                                                |    — |             — |             — |                   — |
| The Queen's Medical Center                                                                              |    — |             — |             — |                   — |
| The Toledo Hospital                                                                                     |    — |             — |             — |                   — |
| The Union Hospital of Cecil County, Inc.                                                                |    — |             — |             — |                   — |
| The University Of Texas M.D. Anderson Cancer Center                                                     |    — |             — |             — |                   — |
| The University of Vermont Medical Center Inc                                                            |    — |             — |             — |                   — |
| Thibodaux Regional Medical Center                                                                       |    — |             — |             — |                   — |
| Thorek Memorial Hospital                                                                                |    — |             — |             — |                   — |
| Tift Regional Health System, Inc.                                                                       |    — |             — |             — |                   — |
| Titusville Area Hospital                                                                                |    — |             — |             — |                   — |
| Torrance Memorial Medical Center                                                                        |    — |             — |             — |                   — |
| Touro Infirmary Hospital                                                                                |    — |             — |             — |                   — |
| Tri-City Medical Center                                                                                 |    — |             — |             — |                   — |
| Tufts Medical Center Inc.                                                                               |    — |             — |             — |                   — |
| UC HEALTH                                                                                               |    — |             — |             — |                   — |
| UC Health, LLC                                                                                          |    — |             — |             — |                   — |
| UP Health System - Marquette                                                                            |    — |             — |             — |                   — |
| UPMC                                                                                                    |    — |             — |             — |                   — |
| USC-University Hospital                                                                                 |    — |             — |             — |                   — |
| Union Hospital, Inc.                                                                                    |    — |             — |             — |                   — |
| United Hospital Center                                                                                  |    — |             — |             — |                   — |
| Unity Health System                                                                                     |    — |             — |             — |                   — |
| Univeristy of Chicago Hospitals & Health System                                                         |    — |             — |             — |                   — |
| University Health System                                                                                |    — |             — |             — |                   — |
| University Hospital                                                                                     |    — |             — |             — |                   — |
| University Hospitals Health System                                                                      |    — |             — |             — |                   — |
| University Medical Center                                                                               |    — |             — |             — |                   — |
| University Medical Center of Southern Nevada                                                            |    — |             — |             — |                   — |
| University Medical Center, Inc                                                                          |    — |             — |             — |                   — |
| University of Alabama at Birmingham Medical Center                                                      |    — |             — |             — |                   — |
| University of Calif. S.F. - Hospital Info Sys                                                           |    — |             — |             — |                   — |
| University of California Davis Medical Center                                                           |    — |             — |             — |                   — |
| University of Colorado Hospital                                                                         |    — |             — |             — |                   — |
| University of Kansas Medical Center                                                                     |    — |             — |             — |                   — |
| University of Mississippi Medical Center                                                                |    — |             — |             — |                   — |
| University of Nebraska Medical Center                                                                   |    — |             — |             — |                   — |
| University of New Mexico Health Sciences Center                                                         |    — |             — |             — |                   — |
| University of Tennessee Medical Center                                                                  |    — |             — |             — |                   — |
| University of Texas Southwestern Medical Center                                                         |    — |             — |             — |                   — |
| University of Wisconsin Hospital and Clinics                                                            |    — |             — |             — |                   — |
| VALLEY VIEW HOSPITAL ASSOCIATION                                                                        |    — |             — |             — |                   — |
| VCU HEALTH SYSTEM AUTHORITY                                                                             |    — |             — |             — |                   — |
| Valley Children's Hospital                                                                              |    — |             — |             — |                   — |
| Valley County Health System                                                                             |    — |             — |             — |                   — |
| Valley Health System                                                                                    |    — |             — |             — |                   — |
| Vanderbilt University Medical Center                                                                    |    — |             — |             — |                   — |
| Virginia Hospital Center                                                                                |    — |             — |             — |                   — |
| Virginia Mason Medical Center                                                                           |    — |             — |             — |                   — |
| WITHAM HOSPITAL                                                                                         |    — |             — |             — |                   — |
| Wabash General Hospital District                                                                        |    — |             — |             — |                   — |
| Waianae District Comprehensive Health & Hospital Board Inc                                              |    — |             — |             — |                   — |
| WakeMed                                                                                                 |    — |             — |             — |                   — |
| Warren General Hospital                                                                                 |    — |             — |             — |                   — |
| Washington Hospital Healthcare Sysem                                                                    |    — |             — |             — |                   — |
| Weeks Medical Center                                                                                    |    — |             — |             — |                   — |
| Weill Cornell Medical College in Qatar                                                                  |    — |             — |             — |                   — |
| Wellmont Health System                                                                                  |    — |             — |             — |                   — |
| Wellstar Health System                                                                                  |    — |             — |             — |                   — |
| Wentworth-Douglass Hospital                                                                             |    — |             — |             — |                   — |
| West Holt Memorial Hospital                                                                             |    — |             — |             — |                   — |
| West Jefferson Medical Center                                                                           |    — |             — |             — |                   — |
| White Plains Hospital                                                                                   |    — |             — |             — |                   — |
| White Wilson Medical Center, P.A.                                                                       |    — |             — |             — |                   — |
| William Beaumont Hospital                                                                               |    — |             — |             — |                   — |
| Williamson Medical Center                                                                               |    — |             — |             — |                   — |
| Willis-Knighton Medical Center                                                                          |    — |             — |             — |                   — |
| Yale-New Haven Health Services Corporation                                                              |    — |             — |             — |                   — |
| York Hospital                                                                                           |    — |             — |             — |                   — |
| Yuma Regional Medical Center                                                                            |    — |             — |             — |                   — |
| Zangmeister cancer Center                                                                               |    — |             — |             — |                   — |
<!-- END:hospitals-table -->

### Health Insurers

Tracked in [`data/us-health-insurance.csv`](data/us-health-insurance.csv). Prefix data in [`data/asn/insurance-prefixes.csv`](data/asn/insurance-prefixes.csv).

<!-- BEGIN:insurance-table -->
| Organization                                                          | ASNs | IPv4 Prefixes | IPv6 Prefixes | Est. IPv4 Addresses |
| :---                                                                  | ---: | ---:          | ---:          | ---:                |
| Aetna, Inc.                                                           |    — |             — |             — |                   — |
| American Postal Workers Union, AFL-CIO Health Plan                    |    — |             — |             — |                   — |
| Anthem Broadband                                                      |    — |             — |             — |                   — |
| BLUE CROSS & BLUE SHIELD OF MISSISSIPPI, A MUTUAL INSURANCE COMPANY   |    — |             — |             — |                   — |
| Blue Cross & Blue Shield of Minnesota                                 |    — |             — |             — |                   — |
| Blue Cross Blue Shield Association                                    |    — |             — |             — |                   — |
| Blue Cross Blue Shield Of Louisiana                                   |    — |             — |             — |                   — |
| Blue Cross Blue Shield of Illinois or Blue Cross Blue Shield of Texas |    — |             — |             — |                   — |
| Blue Cross Blue Shield of Kansas, Inc.                                |    — |             — |             — |                   — |
| Blue Cross Blue Shield of Michigan Mutual Insurance                   |    — |             — |             — |                   — |
| Blue Cross Blue Shield of Nebraska                                    |    — |             — |             — |                   — |
| Blue Cross Blue Shield of North Dakota                                |    — |             — |             — |                   — |
| Blue Cross Blue Shield of South Carolina                              |    — |             — |             — |                   — |
| Blue Cross and Blue Shield of Alabama                                 |    — |             — |             — |                   — |
| Blue Cross and Blue Shield of Arizona Inc                             |    — |             — |             — |                   — |
| Blue Cross and Blue Shield of Kansas City                             |    — |             — |             — |                   — |
| Blue Cross and Blue Shield of Massachusetts, Inc.                     |    — |             — |             — |                   — |
| Blue Cross and Blue Shield of North Carolina                          |    — |             — |             — |                   — |
| Blue Shield of California                                             |    — |             — |             — |                   — |
| BlueCross BlueShield of Tennessee                                     |    — |             — |             — |                   — |
| CIGNA                                                                 |    — |             — |             — |                   — |
| Capital Health Plan, Inc.                                             |    — |             — |             — |                   — |
| CareFirst Management Company, LLC                                     |    — |             — |             — |                   — |
| Centene Corporation                                                   |    — |             — |             — |                   — |
| Dean Health Plan, Inc.                                                |    — |             — |             — |                   — |
| Elevance Health, Inc.                                                 |    — |             — |             — |                   — |
| Excellus Health Plan, Inc.                                            |    — |             — |             — |                   — |
| HORIZON BLUE CROSS BLUE SHIELD OF NJ                                  |    — |             — |             — |                   — |
| HUMANA                                                                |    — |             — |             — |                   — |
| Harvard Pilgrim Health Care, Inc.                                     |    — |             — |             — |                   — |
| HealthPlan Services, Inc.                                             |    — |             — |             — |                   — |
| Highmark Inc                                                          |    — |             — |             — |                   — |
| Independence Blue Cross                                               |    — |             — |             — |                   — |
| Inland Empire Health Plan                                             |    — |             — |             — |                   — |
| Kaiser Foundation Health Plan, Inc.                                   |    — |             — |             — |                   — |
| Keystone Mercy Health Plan                                            |    — |             — |             — |                   — |
| METROPLUS HEALTH PLAN, INC.                                           |    — |             — |             — |                   — |
| MVP Health Plan Inc.                                                  |    — |             — |             — |                   — |
| Magellan Health Services                                              |    — |             — |             — |                   — |
| Molina Healthcare Inc.                                                |    — |             — |             — |                   — |
| PARTNERSHIP HEALTHPLAN OF CALIFORNIA                                  |    — |             — |             — |                   — |
| Premera Blue Cross                                                    |    — |             — |             — |                   — |
| Prominence Health Plan                                                |    — |             — |             — |                   — |
| Providence Health Plan                                                |    — |             — |             — |                   — |
| SCAN Health Plan                                                      |    — |             — |             — |                   — |
| SUMMACARE HEALTH PLAN                                                 |    — |             — |             — |                   — |
| San Francisco Health Plan                                             |    — |             — |             — |                   — |
| United Health Services Hospitals, Inc.                                |    — |             — |             — |                   — |
| UnitedHealth Group Incorporated                                       |    — |             — |             — |                   — |
| Vantage Health Plan, Inc.                                             |    — |             — |             — |                   — |
| WELLMARK BLUE CROSS AND BLUE SHIELD                                   |    — |             — |             — |                   — |
<!-- END:insurance-table -->

### Pharmacy Benefit Managers

Tracked in [`data/us-pharmacy-benefit-managers.csv`](data/us-pharmacy-benefit-managers.csv). Prefix data in [`data/asn/pbm-prefixes.csv`](data/asn/pbm-prefixes.csv).

<!-- BEGIN:pbm-table -->
| Organization                       | ASNs | IPv4 Prefixes | IPv6 Prefixes | Est. IPv4 Addresses |
| :---                               | ---: | ---:          | ---:          | ---:                |
| Diplomat Pharmacy, Inc             |    — |             — |             — |                   — |
| Express Scripts Incorporated       |    — |             — |             — |                   — |
| MedImpact Healthcare Systems, Inc. |    — |             — |             — |                   — |
| Medco Health Solutions, Inc        |    — |             — |             — |                   — |
| Navitus Health Solutions, LLC      |    — |             — |             — |                   — |
| Omnicare, Inc.                     |    — |             — |             — |                   — |
| Prime Therapeutics LLC             |    — |             — |             — |                   — |
| Rite Aid Corporation               |    — |             — |             — |                   — |
| Walgreens Co                       |    — |             — |             — |                   — |
<!-- END:pbm-table -->

### Health IT Vendors

Includes EHR systems (Epic, Cerner/Oracle), clinical networks, and health data platforms. Tracked in [`data/us-health-it-vendors.csv`](data/us-health-it-vendors.csv). Prefix data in [`data/asn/health-it-prefixes.csv`](data/asn/health-it-prefixes.csv).

<!-- BEGIN:health-it-table -->
| Organization                                 | ASNs | IPv4 Prefixes | IPv6 Prefixes | Est. IPv4 Addresses |
| :---                                         | ---: | ---:          | ---:          | ---:                |
| Athenahealth                                 |    — |             — |             — |                   — |
| Availity                                     |    — |             — |             — |                   — |
| Cardinal Health, Inc.                        |    — |             — |             — |                   — |
| Carelon Behavioral Health, Inc.              |    — |             — |             — |                   — |
| Cerner Corporation                           |    — |             — |             — |                   — |
| ECLINICALWORKS, LLC                          |    — |             — |             — |                   — |
| Epic Systems Corporation                     |    — |             — |             — |                   — |
| Evolent Health LLC                           |    — |             — |             — |                   — |
| Greenway Health, LLC                         |    — |             — |             — |                   — |
| Guidehouse Inc.                              |    — |             — |             — |                   — |
| Health Catalyst, Inc.                        |    — |             — |             — |                   — |
| Inovalon Inc.                                |    — |             — |             — |                   — |
| Medical Information Technology, Inc.         |    — |             — |             — |                   — |
| Microsoft Corporation                        |    — |             — |             — |                   — |
| Netsmart Technologies                        |    — |             — |             — |                   — |
| Netsmart Technologies Inc.                   |    — |             — |             — |                   — |
| NextGen Healthcare Information Systems, LLC. |    — |             — |             — |                   — |
| Omnicell                                     |    — |             — |             — |                   — |
| Surescripts, LLC                             |    — |             — |             — |                   — |
| WebMD Health Services Group, Inc.            |    — |             — |             — |                   — |
<!-- END:health-it-table -->

---

## Technology Stack (Active Domain Scan)

Top technologies detected across actively scanned government domains via httpx fingerprinting.

<!-- BEGIN:tech-table -->
| Technology                  | Domains | Example Domains                          |
| :---                        | ---:    | :---                                     |
| HSTS                        |    2193 | archives.gov, atf.gov, bis.gov           |
| Cloudflare                  |     458 | americabydesign.gov, atf.gov, bis.gov    |
| HTTP/3                      |     400 | americabydesign.gov, cancer.gov, cdc.gov |
| Amazon Web Services         |     371 | acf.gov, archives.gov, atf.gov           |
| Cloudflare Bot Management   |     318 | atf.gov, bis.gov, cisa.gov               |
| Amazon CloudFront           |     249 | archives.gov, atf.gov, cancer.gov        |
| Cloudflare Browser Insights |     201 | americabydesign.gov, cisa.gov, doi.gov   |
| Akamai                      |     150 | dhs.gov, faa.gov, fws.gov                |
| Apache HTTP Server          |     131 | cancer.gov, commerce.gov, doi.gov        |
| Nginx                       |      95 | archives.gov, atf.gov, cancer.gov        |
| jQuery                      |      92 | cancer.gov, cdc.gov, commerce.gov        |
| Google Tag Manager          |      87 | archives.gov, cancer.gov, data.gov       |
| Akamai Bot Manager          |      86 | healthcare.gov, irs.gov, medicare.gov    |
| Microsoft ASP.NET           |      79 | atf.gov, cancer.gov, cdc.gov             |
| Google Analytics            |      79 | cancer.gov, commerce.gov, doi.gov        |
| Azure                       |      74 | cdc.gov, ed.gov, gpo.gov                 |
| PHP                         |      72 | cancer.gov, commerce.gov, doi.gov        |
| Amazon ELB                  |      71 | acf.gov, archives.gov, cisa.gov          |
| Azure Front Door            |      69 | cdc.gov, ed.gov, gpo.gov                 |
| Amazon S3                   |      57 | archives.gov, cancer.gov, data.gov       |
| Amazon ALB                  |      49 | archives.gov, cancer.gov, dhs.gov        |
| IIS:10.0                    |      47 | atf.gov, bis.gov, cancer.gov             |
| Windows Server              |      47 | atf.gov, bis.gov, cancer.gov             |
| Java                        |      45 | atf.gov, data.gov, dhs.gov               |
| USWDS                       |      45 | data.gov, energy.gov, gsa.gov            |
| Bootstrap                   |      40 | cancer.gov, cdc.gov, data.gov            |
| jsDelivr                    |      36 | cancer.gov, data.gov, doi.gov            |
| F5 BigIP                    |      35 | bjs.gov, cancer.gov, commerce.gov        |
| Acquia Cloud Platform:next  |      32 | atf.gov, cancer.gov, doi.gov             |
| Drupal:10                   |      31 | cancer.gov, doi.gov, headstart.gov       |
| Dynatrace                   |      30 | hrsa.gov, sba.gov, va.gov                |
| Dynatrace RUM               |      30 | hrsa.gov, sba.gov, va.gov                |
| Varnish                     |      27 | atf.gov, energy.gov, headstart.gov       |
| cdnjs                       |      26 | cancer.gov, energy.gov, ice.gov          |
| Google Cloud                |      25 | cancer.gov, clinicaltrials.gov, doe.gov  |
| jQuery CDN                  |      25 | cancer.gov, energy.gov, fws.gov          |
| Google Cloud CDN            |      21 | clinicaltrials.gov, doe.gov, doi.gov     |
| Font Awesome                |      19 | cancer.gov, cdc.gov, gsa.gov             |
| Ruby                        |      18 | energy.gov, login.gov, nist.gov          |
| Ruby on Rails               |      18 | energy.gov, login.gov, nist.gov          |
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
