# Enterprise Campus Switch Spec Finder

Search and compare campus/data-center Ethernet switches by requirement:

- **Cisco Catalyst** 9200 / 9200L / 9200CX, 9300 / 9300L / 9300X, 9400, 9500 / 9500X
- **HPE Aruba Networking CX** 6000, 6100, 6200F / 6200M, 6300M / 6300F, 6400
- **Juniper (HPE Networking) EX** 2300 / 2300-C, 3400, 4100 / 4100-F, 4300, 4400, 4650, 9200
- **Fortinet FortiSwitch** Secure Access (100F, 100G, 200), Secure Campus (300, 400, 600, T1024) and Rugged (FSR-108F, 112F-POE, 216F-POE, 424F-POE)

and wireless access points:

- **Cisco** Wireless 9172 / 9176 / 9178 (Wi-Fi 7), Catalyst 9162 / 9164 / 9166 / 9163E (Wi-Fi 6E), Catalyst 9124AX (outdoor Wi-Fi 6)
- **HPE Aruba Networking** 720 / 730 / 740 / 750 (Wi-Fi 7), 610 / 630 / 650 / 670 (Wi-Fi 6E), 500 / 510 / 530 / 550 / 570 (Wi-Fi 6)
- **Juniper (HPE Mist)** AP17 / AP27 / AP36 / AP47 / AP66 (Wi-Fi 7), AP24 / AP45 / AP64 (Wi-Fi 6E), AP32 / AP33 / AP43 (Wi-Fi 6)
- **Fortinet FortiAP** 221K / 231K / 241K / 23JK / 244K / 222KL / 441K (Wi-Fi 7), 234G / 432G (outdoor Wi-Fi 6E)

**Live page:** https://mrevelino.github.io/switch-spec-finder/

![Page views today / all time](https://hits.sh/mrevelino.github.io/switch-spec-finder.svg?view=today-total&label=Page%20views&color=049fd9&labelColor=0d274d)

The page-view badge (also at the foot of the live page) comes from [hits.sh](https://hits.sh/). It counts every page load, including repeat visits, so it is not a count of unique people. Opening this README also counts as a view.

## What you can do

- Filter by access port count and speed (1G, mGig 2.5/5/10G, 25G, 100G), uplink speed, PoE class and budget, switching capacity, DRAM, flash, MAC table size, IPv4 routes and form factor.
- Require features: stacking / Virtual Chassis (or, separately, stacking or a controller-managed fabric such as FortiLink), OSPF, BGP, EVPN-VXLAN, MACsec, MPLS, redundant PSU.
- Filter rugged / industrial DIN-rail switches by form factor.
- Sort the results table, tick up to four models and compare them side by side. The best value in each numeric row is highlighted.
- Show only rows fully verified against the vendor datasheet.
- **Access points:** filter by vendor, Wi-Fi generation, indoor / wall plate / outdoor, data rate, uplink speed, 4x4 radios, 6 GHz, dual uplinks, full function on 802.3at PoE, BLE/IoT and USB; sort and compare up to four.
- **Export:** download everything that matches your filters, plus your comparisons, as an Excel workbook (one sheet per table) or a PDF report. Use the Export buttons in the side panel.

## Data

| File | Contents |
|---|---|
| [`data/switch_specs.json`](data/switch_specs.json) | 103 models, one object per model (`rows`) |
| [`data/switch_specs.csv`](data/switch_specs.csv) | The same rows as CSV |
| [`scripts/make_specs.py`](scripts/make_specs.py) | The script that generates the JSON: `python scripts/make_specs.py data/switch_specs.json` |
| [`data/access_points.json`](data/access_points.json) | 44 access points (`rows`) |
| [`data/access_points.csv`](data/access_points.csv) | The same AP rows as CSV |
| [`scripts/make_aps.py`](scripts/make_aps.py) | Generates the AP JSON: `python scripts/make_aps.py data/access_points.json` |

Key columns: `ports`, `port_speed`, `port_max_gbps`, `uplinks`, `uplink_max_gbps`, `poe`, `poe_w_port`, `poe_budget_w`, `switching_gbps`, `fwd_mpps`, `dram_gb`, `flash_gb`, `mac`, `ipv4_routes`, `stacking`, `stack_max`, the feature flags (`ospf`, `bgp`, `evpn_vxlan`, `macsec`, `mpls`, `redundant_psu`), plus `verified`, `notes` and `datasheet`. An empty value means the datasheet does not state it.

## Sources and verification

Checked on 13 November 2026 against:

- Cisco Catalyst [9200](https://www.cisco.com/c/en/us/products/collateral/switches/catalyst-9200-series-switches/nb-06-cat9200-ser-data-sheet-cte-en.html), [9300](https://www.cisco.com/c/en/us/products/collateral/switches/catalyst-9300-series-switches/nb-06-cat9300-ser-data-sheet-cte-en.html), [9400](https://www.cisco.com/c/en/us/products/collateral/switches/catalyst-9400-series-switches/nb-06-cat9400-ser-data-sheet-cte-en.html) and [9500](https://www.cisco.com/c/en/us/products/collateral/switches/catalyst-9500-series-switches/nb-06-cat9500-ser-data-sheet-cte-en.html) datasheets
- HPE Aruba Networking QuickSpecs: [CX 6000](https://www.hpe.com/us/en/collaterals/collateral.a50002592enw.html), [CX 6100](https://www.hpe.com/us/en/collaterals/collateral.a00021859enw.html), [CX 6200](https://www.hpe.com/us/en/collaterals/collateral.a00059762enw.html), [CX 6300](https://www.hpe.com/us/en/collaterals/collateral.a00073540enw.html), [CX 6400](https://www.hpe.com/us/en/collaterals/collateral.a00073541enw.html)
- HPE-hosted Juniper datasheets: [EX2300](https://www.hpe.com/psnow/doc/a00151236enw), [EX2300-C](https://www.hpe.com/psnow/doc/a50014094enw), [EX3400](https://www.hpe.com/psnow/doc/a50014095enw), [EX4100](https://www.hpe.com/psnow/doc/a00150781enw), [EX4100-F](https://www.hpe.com/psnow/doc/a00150847enw), [EX4400](https://www.hpe.com/psnow/doc/a00150783enw), [EX4650](https://www.hpe.com/psnow/doc/a00150780enw), [EX9200](https://www.hpe.com/psnow/doc/a00150784enw)
- Fortinet FortiSwitch datasheets: [Secure Access](https://www.fortinet.com/content/dam/fortinet/assets/data-sheets/pdf/fortiswitch-secure-access-series.pdf), [Secure Campus](https://www.fortinet.com/content/dam/fortinet/assets/data-sheets/pdf/fortiswitch-campus-series.pdf), [Rugged](https://www.fortinet.com/content/dam/fortinet/assets/data-sheets/FortiSwitchRugged.pdf)

Access points were checked on 14 November 2026 against the Cisco access point datasheets on cisco.com, the HPE Aruba Networking and HPE Mist (Juniper) AP datasheets on hpe.com, and the [FortiAP series datasheet](https://www.fortinet.com/content/dam/fortinet/assets/data-sheets/pdf/fortiap-series.pdf). 43 of 44 AP rows are verified; the Juniper AP45's uplink speed could not be read from its datasheet. Max power is blank where the datasheet gives no figure.

Each switch row's `verified` field says how much was confirmed:

- **Verified (54 rows):** every figure matches the datasheet.
- **Partly verified (47 rows):** Catalyst 9300 switching/forwarding figures and routing-feature flags could not be confirmed in the datasheet text; the Catalyst 9400 datasheet does not list supervisor DRAM, MAC or route scale. All 34 FortiSwitch rows: hardware figures match the datasheets, but Fortinet lists routing and MACsec support for each family rather than each model (it points to the FortiSwitch Feature Matrix).
- **Not verified (2 rows):** Juniper EX4300 is no longer published by Juniper or HPE.

### Read with care

- **PoE budget** is quoted differently by each vendor. Cisco 9300 figures are for one PSU with the largest PSU option; Cisco 9200, Juniper EX3400/EX4100/EX4400 and Aruba 6300M figures assume two PSUs. The `notes` field says which.
- **Switching capacity** uses each vendor's headline figure (Juniper's bidirectional figure is used), so small differences across vendors are not meaningful.
- **Chassis rows** (Catalyst 9400, CX 6400, EX9200) show the chassis maximum with full line cards.
- Aruba has no CX 6001, 6002 or 6003 models; the CX 6000 family is the 6000, 6100, 6200, 6300 and 6400 series.
- **FortiSwitches** are normally managed from a FortiGate over FortiLink (8 to 300 switches per FortiGate) instead of being stacked, so they have no stack size. Small FortiSwitch memory and flash sizes are shown in GB (for example 0.25 GB = 256 MB).

Specifications change between software releases and hardware revisions. Always confirm a figure on the linked datasheet before quoting or buying. Product and company names are trademarks of their respective owners; this project is not affiliated with Cisco, HPE, Juniper or Fortinet.

## Run locally

```bash
python -m http.server 8000
```

Then open http://localhost:8000. Opening `index.html` directly as a file will not load the data.
