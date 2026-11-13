# Enterprise Campus Switch Spec Finder

Search and compare campus/data-center Ethernet switches by requirement:

- **Cisco Catalyst** 9200 / 9200L / 9200CX, 9300 / 9300L / 9300X, 9400, 9500 / 9500X
- **HPE Aruba Networking CX** 6000, 6100, 6200F / 6200M, 6300M / 6300F, 6400
- **Juniper (HPE Networking) EX** 2300 / 2300-C, 3400, 4100 / 4100-F, 4300, 4400, 4650, 9200

**Live page:** https://mrevelino.github.io/switch-spec-finder/

## What you can do

- Filter by access port count and speed (1G, mGig 2.5/5/10G, 25G, 100G), uplink speed, PoE class and budget, switching capacity, DRAM, flash, MAC table size, IPv4 routes and form factor.
- Require features: stacking / Virtual Chassis, OSPF, BGP, EVPN-VXLAN, MACsec, MPLS, redundant PSU.
- Sort the results table, tick up to four models and compare them side by side. The best value in each numeric row is highlighted.
- Show only rows fully verified against the vendor datasheet.

## Data

| File | Contents |
|---|---|
| [`data/switch_specs.json`](data/switch_specs.json) | 69 models, one object per model (`rows`) |
| [`data/switch_specs.csv`](data/switch_specs.csv) | The same rows as CSV |
| [`scripts/make_specs.py`](scripts/make_specs.py) | The script that generates the JSON: `python scripts/make_specs.py data/switch_specs.json` |

Key columns: `ports`, `port_speed`, `port_max_gbps`, `uplinks`, `uplink_max_gbps`, `poe`, `poe_w_port`, `poe_budget_w`, `switching_gbps`, `fwd_mpps`, `dram_gb`, `flash_gb`, `mac`, `ipv4_routes`, `stacking`, `stack_max`, the feature flags (`ospf`, `bgp`, `evpn_vxlan`, `macsec`, `mpls`, `redundant_psu`), plus `verified`, `notes` and `datasheet`. An empty value means the datasheet does not state it.

## Sources and verification

Checked on 13 November 2026 against:

- Cisco Catalyst [9200](https://www.cisco.com/c/en/us/products/collateral/switches/catalyst-9200-series-switches/nb-06-cat9200-ser-data-sheet-cte-en.html), [9300](https://www.cisco.com/c/en/us/products/collateral/switches/catalyst-9300-series-switches/nb-06-cat9300-ser-data-sheet-cte-en.html), [9400](https://www.cisco.com/c/en/us/products/collateral/switches/catalyst-9400-series-switches/nb-06-cat9400-ser-data-sheet-cte-en.html) and [9500](https://www.cisco.com/c/en/us/products/collateral/switches/catalyst-9500-series-switches/nb-06-cat9500-ser-data-sheet-cte-en.html) datasheets
- HPE Aruba Networking QuickSpecs: [CX 6000](https://www.hpe.com/us/en/collaterals/collateral.a50002592enw.html), [CX 6100](https://www.hpe.com/us/en/collaterals/collateral.a00021859enw.html), [CX 6200](https://www.hpe.com/us/en/collaterals/collateral.a00059762enw.html), [CX 6300](https://www.hpe.com/us/en/collaterals/collateral.a00073540enw.html), [CX 6400](https://www.hpe.com/us/en/collaterals/collateral.a00073541enw.html)
- HPE-hosted Juniper datasheets: [EX2300](https://www.hpe.com/psnow/doc/a00151236enw), [EX2300-C](https://www.hpe.com/psnow/doc/a50014094enw), [EX3400](https://www.hpe.com/psnow/doc/a50014095enw), [EX4100](https://www.hpe.com/psnow/doc/a00150781enw), [EX4100-F](https://www.hpe.com/psnow/doc/a00150847enw), [EX4400](https://www.hpe.com/psnow/doc/a00150783enw), [EX4650](https://www.hpe.com/psnow/doc/a00150780enw), [EX9200](https://www.hpe.com/psnow/doc/a00150784enw)

Each row's `verified` field says how much was confirmed:

- **Verified (54 rows):** every figure matches the datasheet.
- **Partly verified (13 rows):** Catalyst 9300 switching/forwarding figures and routing-feature flags could not be confirmed in the datasheet text; the Catalyst 9400 datasheet does not list supervisor DRAM, MAC or route scale.
- **Not verified (2 rows):** Juniper EX4300 is no longer published by Juniper or HPE.

### Read with care

- **PoE budget** is quoted differently by each vendor. Cisco 9300 figures are for one PSU with the largest PSU option; Cisco 9200, Juniper EX3400/EX4100/EX4400 and Aruba 6300M figures assume two PSUs. The `notes` field says which.
- **Switching capacity** uses each vendor's headline figure (Juniper's bidirectional figure is used), so small differences across vendors are not meaningful.
- **Chassis rows** (Catalyst 9400, CX 6400, EX9200) show the chassis maximum with full line cards.
- Aruba has no CX 6001, 6002 or 6003 models; the CX 6000 family is the 6000, 6100, 6200, 6300 and 6400 series.

Specifications change between software releases and hardware revisions. Always confirm a figure on the linked datasheet before quoting or buying. Product and company names are trademarks of their respective owners; this project is not affiliated with Cisco, HPE or Juniper.

## Run locally

```bash
python -m http.server 8000
```

Then open http://localhost:8000. Opening `index.html` directly as a file will not load the data.
