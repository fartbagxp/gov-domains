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
