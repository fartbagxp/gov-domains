#!/usr/bin/env bash

bash crt_v2.sh -o cdc.gov | httpx -title -tech-detect -status-code | grep 200
