# ASN Lookup

- [Cloudflare](https://radar.cloudflare.com/routing/as13611)

- [Potaroo.net's Autnums](https://bgp.potaroo.net/cidr/autnums.html)

## FedRAMP Marketplace (`fedramp/`)

Collected by `scripts/fetch_fedramp.py` from the FedRAMP-operated
[public data repository](https://github.com/FedRAMP/marketplace-fedramp-gov-data)
behind marketplace.fedramp.gov.

| File                        |   Rows | Contents                                                                                                                                                                               |
| :-------------------------- | -----: | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `products.csv`              |   ~660 | One row per cloud service offering. `service_desc` is the free-text field to search — the `business_function` taxonomy is only 36 values and is blank for about a quarter of products. |
| `agencies.csv`              |   ~250 | One row per agency, with edge counts tallied from the relationship table.                                                                                                              |
| `agency-authorizations.csv` | ~6,700 | One row per agency↔product relationship. This is the table that answers "who already accepted this?"                                                                                   |

Join on `product_id` and `agency_id`. Every product row carries a
`marketplace_url` for citation.

## `relationship` values

FedRAMP spreads these edges across four arrays with differing completeness, so
each row records the array it came from in `source`:

| `relationship`  | `source`         | Meaning                                     | Has dates |
| :-------------- | :--------------- | :------------------------------------------ | :-------- |
| `authorization` | `Agencies.auths` | Agency issued its own ATO                   | no        |
| `reuse`         | `ReuseMapping`   | Agency reused an existing authorization     | yes       |
| `sponsor_ato`   | `AtoMapping`     | Originating ATO, one per authorized product | yes       |
| `in_process`    | `Agencies.procs` | Package under agency review                 | no        |

Only `reuse` and `sponsor_ato` carry `ato_date` / `auth_date` / `exp_date`;
they are blank elsewhere because the source arrays do not provide them.

The `reported_authorizations` and `reported_reuses` columns are FedRAMP's own
published counters. They disagree with the actual edge counts for a meaningful
share of records, so prefer counting rows in `agency-authorizations.csv`.

Rows are stamped with `source_last_change` (the export's timestamp) rather than
collection time, so the files only change when FedRAMP's data changes.

## GitHub Organizations (`github/`)

Collected by `scripts/fetch_github_orgs.py`. Orgs come from GitHub's curated
[government list](https://github.com/github/government.github.com/blob/gh-pages/_data/governments.yml)
(the U.S. Federal, U.S. Military and Intelligence, and U.S. States sections) plus
CMS's [federal org allowlist](https://github.com/DSACMS/automated-codejson-generator/blob/dev/src/gov-update/allowlist.json)
and inventories agencies publish of their own orgs (`AGENCY_LISTS` in the script;
currently [CDC's](https://github.com/CDCgov/ShareIT-Act/blob/main/docs/sources.md) and
[CMS's](https://github.com/DSACMS/metrics/blob/main/scripts/_metadata/projects_tracked.json)).

Federal orgs are also found by a GitHub org search over agency names and
acronyms (`DISCOVERY_*` in the script). A search hit is kept only when its
profile website or email is a federal .gov/.mil domain. The search takes about
an hour; pass `--search-cache <file>` to reuse results between runs, or
`--no-search` to skip it.
Rendered lists: [`docs/github-orgs-federal.md`](../docs/github-orgs-federal.md) and
[`docs/github-orgs-state.md`](../docs/github-orgs-state.md).

| File                     | Contents                                                                                                                                              |
| :----------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------- |
| `federal-orgs.csv`       | One row per federal org; `group` is the CISA .gov registry agency name                                                                                |
| `state-orgs.csv`         | One row per state org; `group` is the two-letter state code                                                                                           |
| `federal-candidates.csv` | Search hits that look federal by login and wording but name no domain; `group` is the matched acronym. Unconfirmed. Promote real ones via `OVERRIDES` |

`attributed_by` records how the org was placed: the source name (e.g.
`cdc-shareit`) when the agency lists the org itself, `domain:<d>` when the profile's
website or email is a registered .gov/.mil domain, `override` when set by hand in
the script, and blank for orgs left as `Unresolved`.
