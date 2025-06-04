#!/usr/bin/env bash

# subfinder -silent -d cdc.gov | dnsx -silent -a -resp -asn -cname
subfinder -silent -d cdc.gov | httpx -title -tech-detect -status-code | grep 200
