import json, sys

CIS = {
 "9200": "https://www.cisco.com/c/en/us/products/collateral/switches/catalyst-9200-series-switches/nb-06-cat9200-ser-data-sheet-cte-en.html",
 "9300": "https://www.cisco.com/c/en/us/products/collateral/switches/catalyst-9300-series-switches/nb-06-cat9300-ser-data-sheet-cte-en.html",
 "9400": "https://www.cisco.com/c/en/us/products/collateral/switches/catalyst-9400-series-switches/nb-06-cat9400-ser-data-sheet-cte-en.html",
 "9500": "https://www.cisco.com/c/en/us/products/collateral/switches/catalyst-9500-series-switches/nb-06-cat9500-ser-data-sheet-cte-en.html",
}
QS = lambda i: "https://www.hpe.com/us/en/collaterals/collateral.%s.html" % i
PS = lambda i: "https://www.hpe.com/psnow/doc/%s" % i

V, P, N = "Verified", "Partly verified", "Not verified"
rows = []
def add(base, **kw):
    r = dict(base); r.update(kw); rows.append(r)

# ---------------- Cisco Catalyst 9200 ----------------
c9200 = dict(vendor="Cisco", series="Catalyst 9200", os="IOS XE", form="Fixed", dram_gb=4, flash_gb=4,
             mac=32000, ipv4_routes=14000, stacking="StackWise-160", stack_max=8, ospf=True, bgp=False,
             evpn_vxlan=False, macsec=True, mpls=False, redundant_psu=True, datasheet=CIS["9200"],
             port_speed="1G", port_max_gbps=1, poe="PoE+", poe_w_port=30, verified=V,
             notes="IPv4 routes = ARP plus learned routes (10,000 direct + 4,000 indirect). MACsec AES-128. PoE budget shown with two PSUs. BGP, EVPN and MPLS are not listed on the datasheet.")
c9200l = dict(c9200, series="Catalyst 9200L", dram_gb=2, mac=16000, ipv4_routes=11000, stacking="StackWise-80", macsec=False,
              notes="IPv4 routes = ARP plus learned routes (8,000 direct + 3,000 indirect). Field-replaceable PSU, fixed fans. MACsec not listed for 9200L. PoE budget shown with two PSUs.")
add(c9200l, model="C9200L-24T-4G", ports=24, uplinks="4x 1G SFP (fixed)", uplink_max_gbps=1,
    poe="None", poe_w_port=0, poe_budget_w=0, switching_gbps=56, fwd_mpps=41.67)
add(c9200l, model="C9200L-24P-4X", ports=24, uplinks="4x 1/10G SFP+ (fixed)", uplink_max_gbps=10,
    poe_budget_w=740, switching_gbps=128, fwd_mpps=95.23)
add(c9200l, model="C9200L-48P-4X", ports=48, uplinks="4x 1/10G SFP+ (fixed)", uplink_max_gbps=10,
    poe_budget_w=1440, switching_gbps=176, fwd_mpps=130.95)
add(c9200, model="C9200-24P", ports=24, uplinks="Modular: NM-4G (4x 1G) or NM-4X (4x 1/10G)", uplink_max_gbps=10,
    poe_budget_w=740, switching_gbps=128, fwd_mpps=95.23)
add(c9200, model="C9200-48P", ports=48, uplinks="Modular: NM-4G (4x 1G) or NM-4X (4x 1/10G)", uplink_max_gbps=10,
    poe_budget_w=1440, switching_gbps=176, fwd_mpps=130.95)
add(c9200, model="C9200-48PXG", ports=48, port_speed="8x mGig up to 10G + 40x 1G", port_max_gbps=10,
    uplinks="Modular: NM-4X (4x 10G), NM-2Y (2x 25G), NM-2Q (2x 40G)", uplink_max_gbps=40,
    poe_budget_w=1440, switching_gbps=400, fwd_mpps=297.61)
add(c9200, series="Catalyst 9200CX", model="C9200CX-12P-2X2G", form="Compact", ports=12,
    uplinks="2x 10G SFP+ + 2x 1G copper (fixed)", uplink_max_gbps=10, poe_budget_w=240,
    switching_gbps=68, fwd_mpps=50.59, flash_gb=8, stacking="None", stack_max=1, bgp=True, redundant_psu=False,
    notes="Fanless, fixed internal PSU. Basic BGP from IOS XE 17.13.1. MACsec AES-256. Stacking not available.")

# ---------------- Cisco Catalyst 9300 ----------------
c9300 = dict(vendor="Cisco", series="Catalyst 9300", os="IOS XE", form="Fixed", dram_gb=8, flash_gb=16,
             mac=32000, ipv4_routes=32000, stacking="StackWise-480", stack_max=8, ospf=True, bgp=True,
             evpn_vxlan=True, macsec=True, mpls=True, redundant_psu=True, datasheet=CIS["9300"],
             uplinks="Modular: 1G, 10G, 25G, 40G or mGig network modules", uplink_max_gbps=40,
             port_speed="1G", port_max_gbps=1, verified=P,
             notes="DRAM, flash, MAC, routes and PoE checked on the datasheet. Switching and forwarding figures, and the OSPF/BGP/EVPN/MPLS flags (Network Advantage license), could not be confirmed in the datasheet text. PoE budget = single PSU, largest PSU option.")
add(c9300, model="C9300-24T", ports=24, poe="None", poe_w_port=0, poe_budget_w=0, switching_gbps=208, fwd_mpps=154.76)
add(c9300, model="C9300-48P", ports=48, poe="PoE+", poe_w_port=30, poe_budget_w=822, switching_gbps=256, fwd_mpps=190.47)
add(c9300, model="C9300-48U", ports=48, poe="UPOE", poe_w_port=60, poe_budget_w=1622, switching_gbps=256, fwd_mpps=190.48)
add(c9300, model="C9300-24UX", ports=24, port_speed="mGig 100M/1/2.5/5/10G", port_max_gbps=10,
    poe="UPOE", poe_w_port=60, poe_budget_w=1360, switching_gbps=640, fwd_mpps=476.19)
add(c9300, model="C9300-48UXM", ports=48, port_speed="36x 100M/1/2.5G + 12x mGig up to 10G", port_max_gbps=10,
    poe="UPOE", poe_w_port=60, poe_budget_w=1290, switching_gbps=580, fwd_mpps=431.54)
add(c9300, model="C9300-24S", ports=24, port_speed="1G SFP", poe="None", poe_w_port=0, poe_budget_w=0, switching_gbps=208, fwd_mpps=154.76)
add(c9300, series="Catalyst 9300L", model="C9300L-48P-4X", ports=48, uplinks="4x 1/10G SFP+ (fixed)", uplink_max_gbps=10,
    poe="PoE+", poe_w_port=30, poe_budget_w=505, switching_gbps=176, fwd_mpps=130.95, stacking="StackWise-320")
c9300x = dict(c9300, series="Catalyst 9300X", dram_gb=16, ipv4_routes=39000, stacking="StackWise-1T",
              uplinks="Modular: up to 100G network modules", uplink_max_gbps=100,
              notes="IPv4 routes 39,000 (24,000 direct + 15,000 indirect). Switching and forwarding figures, and OSPF/BGP/EVPN/MPLS flags, could not be confirmed in the datasheet text. PoE budget = single PSU, largest PSU option.")
add(c9300x, model="C9300X-48HX", ports=48, port_speed="mGig 100M/1/2.5/5/10G", port_max_gbps=10,
    poe="UPOE+", poe_w_port=90, poe_budget_w=1390, switching_gbps=1760, fwd_mpps=1309.0)
add(c9300x, model="C9300X-24Y", ports=24, port_speed="1/10/25G SFP28", port_max_gbps=25,
    poe="None", poe_w_port=0, poe_budget_w=0, switching_gbps=2000, fwd_mpps=1488.0)

# ---------------- Cisco Catalyst 9400 ----------------
c9400 = dict(vendor="Cisco", series="Catalyst 9400", os="IOS XE", form="Modular chassis", dram_gb=None, flash_gb=None,
             mac=None, ipv4_routes=None, stacking="StackWise Virtual", stack_max=2, ospf=True, bgp=True,
             evpn_vxlan=True, macsec=True, mpls=True, redundant_psu=True, datasheet=CIS["9400"],
             poe="UPOE+", poe_w_port=90, poe_budget_w=None, fwd_mpps=None, verified=P,
             notes="The datasheet does not list supervisor DRAM, MAC or route scale. Max PoE 4,320 W per line-card slot. Supervisor SSD up to 960 GB.")
s1 = dict(c9400, port_speed="Line cards: 1G, mGig up to 10G, 1/10G SFP", port_max_gbps=10,
          uplinks="Sup-1XL: up to 2x 40G + 8x 10G", uplink_max_gbps=40)
add(s1, model="C9404R + Sup-1XL", ports=96, switching_gbps=None,
    notes=c9400["notes"] + " 240 Gbps per line-card slot (2 slots).")
add(s1, model="C9407R + Sup-1XL", ports=240, switching_gbps=None,
    notes=c9400["notes"] + " 120 Gbps per line-card slot (5 slots).")
add(s1, model="C9410R + Sup-1XL", ports=384, switching_gbps=None,
    notes=c9400["notes"] + " 80 Gbps per line-card slot (8 slots).")
add(c9400, model="C9410R + Sup-2", ports=384, port_speed="Line cards: 1G to 100G (25/40/100G need Sup-2)", port_max_gbps=100,
    uplinks="Sup-2: up to 4x 100/40G + 4x 25/10G", uplink_max_gbps=100, switching_gbps=9000,
    notes=c9400["notes"] + " Up to 9 Tbps system bandwidth; 240 Gbps per slot (Sup-2XL: 480).")

# ---------------- Cisco Catalyst 9500 ----------------
c9500 = dict(vendor="Cisco", series="Catalyst 9500", os="IOS XE", form="Fixed", dram_gb=16, flash_gb=16,
             mac=82000, ipv4_routes=256000, stacking="StackWise Virtual", stack_max=2, ospf=True, bgp=True,
             evpn_vxlan=True, macsec=True, mpls=True, redundant_psu=True, datasheet=CIS["9500"],
             poe="None", poe_w_port=0, poe_budget_w=0, verified=V,
             notes="MAC up to 82,000 (Distribution template). IPv4 up to 256,000 indirect routes. DRAM/flash read from a table without headers. SSD up to 960 GB.")
add(c9500, model="C9500-24Y4C", ports=24, port_speed="1/10/25G SFP28", port_max_gbps=25, uplinks="4x 40/100G QSFP28", uplink_max_gbps=100,
    switching_gbps=2000, fwd_mpps=1000.0)
add(c9500, model="C9500-48Y4C", ports=48, port_speed="1/10/25G SFP28", port_max_gbps=25, uplinks="4x 40/100G QSFP28", uplink_max_gbps=100,
    switching_gbps=3200, fwd_mpps=1000.0)
add(c9500, model="C9500-32C", ports=32, port_speed="40/100G QSFP28", port_max_gbps=100, uplinks="(all ports 40/100G)", uplink_max_gbps=100,
    switching_gbps=6400, fwd_mpps=2000.0)
add(c9500, series="Catalyst 9500X", model="C9500X-28C8D", ports=28, port_speed="40/100G QSFP28", port_max_gbps=100,
    uplinks="8x 40/100/200/400G QSFP-DD", uplink_max_gbps=400, switching_gbps=12000, fwd_mpps=8000.0,
    dram_gb=32, flash_gb=32, mac=256000, ipv4_routes=2000000,
    notes="MAC up to 256,000 (custom template). Up to 2,000,000 LPM routes. VPLS and MPLS over GRE not yet available. StackWise Virtual from IOS XE 17.10.1.")

# ---------------- HPE Aruba CX 6000 ----------------
a6000 = dict(vendor="HPE Aruba", series="CX 6000", os="AOS-CX", form="Fixed", dram_gb=2, flash_gb=8,
             mac=8192, ipv4_routes=512, stacking="None", stack_max=1, ospf=False, bgp=False,
             evpn_vxlan=False, macsec=False, mpls=False, redundant_psu=False, datasheet=QS("a50002592enw"),
             port_speed="1G", port_max_gbps=1, uplink_max_gbps=1, verified=V,
             notes="Layer 2 with static routing. Fixed PSU and fans. No stacking.")
add(a6000, model="6000 12G Class4 PoE 2G/2SFP 139W", ports=12, uplinks="2x 1G RJ45 + 2x 1G SFP", poe="PoE+", poe_w_port=30, poe_budget_w=139, switching_gbps=32, fwd_mpps=23.8)
add(a6000, model="6000 24G 4SFP (R8N88B)", ports=24, uplinks="4x 1G SFP", poe="None", poe_w_port=0, poe_budget_w=0, switching_gbps=56, fwd_mpps=41.6)
add(a6000, model="6000 24G Class4 PoE 4SFP 370W (R8N87B)", ports=24, uplinks="4x 1G SFP", poe="PoE+", poe_w_port=30, poe_budget_w=370, switching_gbps=56, fwd_mpps=41.6)
add(a6000, model="6000 48G 4SFP (R8N86B)", ports=48, uplinks="4x 1G SFP", poe="None", poe_w_port=0, poe_budget_w=0, switching_gbps=104, fwd_mpps=77.3)
add(a6000, model="6000 48G Class4 PoE 4SFP 370W (R8N85B)", ports=48, uplinks="4x 1G SFP", poe="PoE+", poe_w_port=30, poe_budget_w=370, switching_gbps=104, fwd_mpps=77.3)
add(a6000, model="6000 48G Class4 PoE 4SFP 740W (R9Y03B)", ports=48, uplinks="4x 1G SFP", poe="PoE+", poe_w_port=30, poe_budget_w=740, switching_gbps=104, fwd_mpps=77.3)

# ---------------- HPE Aruba CX 6100 ----------------
a6100 = dict(a6000, series="CX 6100", dram_gb=4, flash_gb=16, mac=8192, ipv4_routes=512, uplink_max_gbps=10,
             stacking="VSF", stack_max=6, datasheet=QS("a00021859enw"),
             notes="Layer 2 with static routing. VSF stacking up to 6 members (AOS-CX 10.16.1006+); 12-port models stack only with each other.")
add(a6100, model="6100 12G Class4 PoE 2G/2SFP+ 139W (JL679A)", ports=12, uplinks="2x 1G RJ45 + 2x 1/10G SFP+", poe="PoE+", poe_w_port=30, poe_budget_w=139, switching_gbps=68, fwd_mpps=45.1)
add(a6100, model="6100 24G 4SFP+", ports=24, uplinks="4x 1/10G SFP+", poe="None", poe_w_port=0, poe_budget_w=0, switching_gbps=128, fwd_mpps=95.2)
add(a6100, model="6100 24G Class4 PoE 4SFP+ 370W (JL677A)", ports=24, uplinks="4x 1/10G SFP+", poe="PoE+", poe_w_port=30, poe_budget_w=370, switching_gbps=128, fwd_mpps=95.2)
add(a6100, model="6100 48G 4SFP+", ports=48, uplinks="4x 1/10G SFP+", poe="None", poe_w_port=0, poe_budget_w=0, switching_gbps=176, fwd_mpps=98.6)
add(a6100, model="6100 48G Class4 PoE 4SFP+ 370W", ports=48, uplinks="4x 1/10G SFP+", poe="PoE+", poe_w_port=30, poe_budget_w=370, switching_gbps=176, fwd_mpps=98.6)
add(a6100, model="6100 48G Class4 PoE 4SFP+ 740W (R9Y04A)", ports=48, uplinks="4x 1/10G SFP+", poe="PoE+", poe_w_port=30, poe_budget_w=740, switching_gbps=176, fwd_mpps=98.6)

# ---------------- HPE Aruba CX 6200 ----------------
a6200 = dict(a6000, series="CX 6200F", dram_gb=8, flash_gb=16, mac=32768, ipv4_routes=2048, stacking="VSF", stack_max=8,
             ospf=True, uplink_max_gbps=10, datasheet=QS("a00059762enw"),
             notes="Static and Access OSPF routing. VSF stacking up to 8 members. Fixed PSU.")
add(a6200, model="6200F 24G Class4 PoE 4SFP+ 370W (JL725A)", ports=24, uplinks="4x 1/10G SFP+", poe="PoE+", poe_w_port=30, poe_budget_w=370, switching_gbps=128, fwd_mpps=95.2)
add(a6200, model="6200F 48G 4SFP+ (JL726A)", ports=48, uplinks="4x 1/10G SFP+", poe="None", poe_w_port=0, poe_budget_w=0, switching_gbps=176, fwd_mpps=130.9)
add(a6200, model="6200F 48G Class4 PoE 4SFP+ 740W (JL728A)", ports=48, uplinks="4x 1/10G SFP+", poe="PoE+", poe_w_port=30, poe_budget_w=740, switching_gbps=176, fwd_mpps=202.0)
add(a6200, series="CX 6200M", model="6200M 48G Class4 PoE 4SFP+ (R8Q70A)", ports=48, uplinks="4x 1/10G SFP+ (2 with MACsec-256)", poe="PoE+", poe_w_port=30,
    poe_budget_w=1440, switching_gbps=176, fwd_mpps=202.0, ipv4_routes=2000, macsec=True, redundant_psu=True,
    notes="Static and Access OSPF routing. VSF up to 8 members. Two hot-swap PSU slots. MACsec-256 on 2 uplinks only.")

# ---------------- HPE Aruba CX 6300 ----------------
a6300 = dict(vendor="HPE Aruba", series="CX 6300M", os="AOS-CX", form="Fixed", dram_gb=8, flash_gb=None,
             mac=32768, ipv4_routes=61000, stacking="VSF", stack_max=10, ospf=True, bgp=True,
             evpn_vxlan=True, macsec=False, mpls=False, redundant_psu=True, datasheet=QS("a00073540enw"),
             uplinks="4x 1/10/25G SFP56 (50G with DACs)", uplink_max_gbps=25, verified=V,
             notes="Flash not stated for this SKU (newer 6300M SKUs list 32 GB eMMC). Two hot-swap PSU slots. MACsec only on newer R8S/S0E SKUs.")
add(a6300, model="6300M 48G Class4 PoE 4SFP56 (JL661A)", ports=48, port_speed="1G", port_max_gbps=1, poe="PoE+", poe_w_port=30, poe_budget_w=1600, switching_gbps=496, fwd_mpps=369.0)
add(a6300, model="6300M 48 SmartRate Class6 PoE 4SFP56 (JL659A)", ports=48, port_speed="mGig 100M/1/2.5/5G (SmartRate)", port_max_gbps=5,
    poe="PoE (802.3bt Class 6)", poe_w_port=60, poe_budget_w=2880, switching_gbps=880, fwd_mpps=654.0)
add(a6300, model="6300M 24SFP+ 4SFP56 (JL658A)", ports=24, port_speed="1/10G SFP+", port_max_gbps=10, poe="None", poe_w_port=0, poe_budget_w=0, switching_gbps=880, fwd_mpps=654.0)
add(a6300, model="6300M 48p SR10 Class8 PoE 4p 100G MACsec (S0E91A)", ports=48, port_speed="mGig 100M/1/2.5/5/10G (SmartRate)", port_max_gbps=10,
    uplinks="4x 10/25/40/100G QSFP28 (MACsec)", uplink_max_gbps=100, poe="PoE (802.3bt Class 8)", poe_w_port=90, poe_budget_w=2640,
    switching_gbps=1760, fwd_mpps=1310.0, flash_gb=32, macsec=True,
    notes="8 GB DDR4, 32 GB eMMC. MACsec on all ports. Two hot-swap PSU slots.")
a6300f = dict(a6300, series="CX 6300F", redundant_psu=False,
              notes="Fixed PSU. Memory and flash not stated for these SKUs on the QuickSpecs page.")
add(a6300f, model="6300F 24G 4SFP56 (JL668A)", ports=24, port_speed="1G", port_max_gbps=1, poe="None", poe_w_port=0, poe_budget_w=0, switching_gbps=448, fwd_mpps=334.0, dram_gb=None)
add(a6300f, model="6300F 48G Class4 PoE 4SFP56 (JL665A)", ports=48, port_speed="1G", port_max_gbps=1, poe="PoE+", poe_w_port=30, poe_budget_w=740, switching_gbps=496, fwd_mpps=369.0, dram_gb=None)

# ---------------- HPE Aruba CX 6400 ----------------
a6400 = dict(vendor="HPE Aruba", series="CX 6400", os="AOS-CX", form="Modular chassis", dram_gb=16, flash_gb=32,
             mac=32768, ipv4_routes=61000, stacking="VSX", stack_max=2, ospf=True, bgp=True,
             evpn_vxlan=True, macsec=True, mpls=False, redundant_psu=True, datasheet=QS("a00073541enw"),
             port_speed="Line cards: 1G, SmartRate up to 10G, 10G-100G fiber", port_max_gbps=100,
             uplinks="Any line-card port up to 100G", uplink_max_gbps=100, poe="PoE (802.3bt Class 6)", poe_w_port=60,
             poe_budget_w=None, verified=V,
             notes="Management module: 16 GB DDR4 ECC, 32 GB eMMC. IPv4 routes 61,000 (up to 630,780 with R0X44C/R0X45C line cards).")
add(a6400, model="6405 chassis (5 slots)", ports=240, switching_gbps=14000, fwd_mpps=5700.0)
add(a6400, model="6410 chassis (10 slots)", ports=480, switching_gbps=28000, fwd_mpps=11400.0)

# ---------------- Juniper EX2300 ----------------
ex2300 = dict(vendor="Juniper", series="EX2300", os="Junos", form="Fixed", dram_gb=2, flash_gb=2,
              mac=16000, ipv4_routes=512, stacking="Virtual Chassis", stack_max=4, ospf=True, bgp=False,
              evpn_vxlan=False, macsec=False, mpls=False, redundant_psu=False, datasheet=PS("a00151236enw"),
              port_speed="1G", port_max_gbps=1, uplinks="4x 1/10G SFP+", uplink_max_gbps=10, verified=V,
              notes="IPv4 routes: 512 prefixes (4,096 host routes). RIP and OSPF. Virtual Chassis needs an optional license. Fixed PSU.")
add(ex2300, model="EX2300-24T", ports=24, poe="None", poe_w_port=0, poe_budget_w=0, switching_gbps=128, fwd_mpps=95.0)
add(ex2300, model="EX2300-24P", ports=24, poe="PoE+", poe_w_port=30, poe_budget_w=370, switching_gbps=128, fwd_mpps=95.0)
add(ex2300, model="EX2300-48P", ports=48, poe="PoE+", poe_w_port=30, poe_budget_w=750, switching_gbps=176, fwd_mpps=130.0)
add(ex2300, model="EX2300-48MP", ports=48, port_speed="16x mGig 1/2.5G + 32x 1G", port_max_gbps=2.5, uplinks="6x 1/10G SFP+",
    poe="PoE+", poe_w_port=30, poe_budget_w=750, switching_gbps=264, fwd_mpps=130.0, flash_gb=8, dram_gb=None,
    notes="8 GB flash on multigig models; DRAM not stated for them. IPv4 routes: 512 prefixes. Virtual Chassis needs an optional license.")
add(ex2300, series="EX2300-C", model="EX2300-C-12P", form="Compact", ports=12, uplinks="2x 1/10G SFP/SFP+", poe="PoE+", poe_w_port=30,
    poe_budget_w=124, switching_gbps=64, fwd_mpps=47.0, datasheet=PS("a50014094enw"),
    notes="Fanless compact switch. IPv4 routes: 512 prefixes. Full 30 W PoE+ on up to 4 ports at once.")

# ---------------- Juniper EX3400 ----------------
ex3400 = dict(vendor="Juniper", series="EX3400", os="Junos", form="Fixed", dram_gb=2, flash_gb=2,
              mac=32000, ipv4_routes=14000, stacking="Virtual Chassis", stack_max=10, ospf=True, bgp=True,
              evpn_vxlan=False, macsec=True, mpls=False, redundant_psu=True, datasheet=PS("a50014095enw"),
              port_speed="1G", port_max_gbps=1, uplinks="4x 1/10G SFP+ + 2x 40G QSFP+", uplink_max_gbps=40, verified=V,
              notes="IPv4 routes: 14,000 prefixes (36,000 host routes). BGP needs an advanced license. Two redundant field-replaceable PSUs; PoE budget shown with two PSUs.")
add(ex3400, model="EX3400-24P", ports=24, poe="PoE+", poe_w_port=30, poe_budget_w=720, switching_gbps=288, fwd_mpps=214.0)
add(ex3400, model="EX3400-48T", ports=48, poe="None", poe_w_port=0, poe_budget_w=0, switching_gbps=336, fwd_mpps=250.0)
add(ex3400, model="EX3400-48P", ports=48, poe="PoE+", poe_w_port=30, poe_budget_w=1440, switching_gbps=336, fwd_mpps=250.0)

# ---------------- Juniper EX4100 ----------------
ex4100 = dict(vendor="Juniper", series="EX4100", os="Junos", form="Fixed", dram_gb=4, flash_gb=8,
              mac=64000, ipv4_routes=32650, stacking="Virtual Chassis", stack_max=10, ospf=True, bgp=True,
              evpn_vxlan=True, macsec=True, mpls=False, redundant_psu=True, datasheet=PS("a00150781enw"),
              uplinks="4x 1/10G SFP+ + 4x 10/25G SFP28 (VC or uplink)", uplink_max_gbps=25, verified=V,
              notes="IPv4 routes: 32,650 prefixes (32,150 host routes). MACsec AES-256. EVPN-VXLAN to the access layer. PoE budget shown with two PSUs. MPLS not listed on the datasheet.")
add(ex4100, model="EX4100-48P", ports=48, port_speed="1G", port_max_gbps=1, poe="PoE+", poe_w_port=30, poe_budget_w=1440, switching_gbps=376, fwd_mpps=279.0)
add(ex4100, model="EX4100-48MP", ports=48, port_speed="16x mGig 100M/1/2.5G + 32x 10M/100M/1G", port_max_gbps=2.5,
    poe="PoE++ (802.3bt)", poe_w_port=90, poe_budget_w=1620, switching_gbps=424, fwd_mpps=315.0)
add(ex4100, series="EX4100-F", model="EX4100-F-48P", ports=48, port_speed="1G", port_max_gbps=1, uplinks="4x 1/10G SFP+ (+ 4x 10G SFP+ for VC)", uplink_max_gbps=10,
    poe="PoE+", poe_w_port=30, poe_budget_w=740, switching_gbps=256, fwd_mpps=190.0, macsec=False, redundant_psu=False,
    datasheet=PS("a00150847enw"),
    notes="IPv4 routes: 32,650 prefixes. EVPN-VXLAN to the access layer. MACsec and redundant PSU not listed on the datasheet.")

# ---------------- Juniper EX4300 (end of sale) ----------------
ex4300 = dict(vendor="Juniper", series="EX4300", os="Junos", form="Fixed", dram_gb=None, flash_gb=None,
              mac=None, ipv4_routes=None, stacking="Virtual Chassis", stack_max=10, ospf=True, bgp=True,
              evpn_vxlan=False, macsec=True, mpls=False, redundant_psu=True, datasheet="https://www.hpe.com/us/en/products/networking/ex-switches.html",
              verified=N,
              notes="EX4300 is no longer listed by Juniper or HPE, so its datasheet could not be checked. Figures are from memory; treat them as approximate.")
add(ex4300, model="EX4300-48P", ports=48, port_speed="1G", port_max_gbps=1, uplinks="4x 40G QSFP+ + optional 4x 10G module", uplink_max_gbps=40,
    poe="PoE+", poe_w_port=30, poe_budget_w=900, switching_gbps=496, fwd_mpps=369.0)
add(ex4300, model="EX4300-48MP", ports=48, port_speed="24x mGig up to 10G + 24x mGig up to 2.5G", port_max_gbps=10, uplinks="Module: 4x 25G / 2x 40G",
    uplink_max_gbps=40, poe="UPOE", poe_w_port=60, poe_budget_w=1440, switching_gbps=720, fwd_mpps=535.7, evpn_vxlan=True)

# ---------------- Juniper EX4400 ----------------
ex4400 = dict(vendor="Juniper", series="EX4400", os="Junos", form="Fixed", dram_gb=4, flash_gb=20,
              mac=112000, ipv4_routes=130048, stacking="Virtual Chassis", stack_max=10, ospf=True, bgp=True,
              evpn_vxlan=True, macsec=True, mpls=False, redundant_psu=True, datasheet=PS("a00150783enw"),
              uplinks="2x 100G QSFP28 (VC or uplink) + optional 4x 1/10/25G module", uplink_max_gbps=100, verified=V,
              notes="IPv4 routes: 130,048 prefixes (81,000 host routes). MACsec AES-256. PoE budget shown with two PSUs. MPLS not listed on the datasheet.")
add(ex4400, model="EX4400-24P", ports=24, port_speed="1G", port_max_gbps=1, poe="PoE++ (802.3bt)", poe_w_port=90, poe_budget_w=1806, switching_gbps=648, fwd_mpps=482.0)
add(ex4400, model="EX4400-48P", ports=48, port_speed="1G", port_max_gbps=1, poe="PoE++ (802.3bt)", poe_w_port=90, poe_budget_w=2200, switching_gbps=696, fwd_mpps=517.0)
add(ex4400, model="EX4400-48MP", ports=48, port_speed="12x mGig 100M-10G + 36x mGig 100M-2.5G", port_max_gbps=10,
    poe="PoE++ (802.3bt)", poe_w_port=90, poe_budget_w=2200, switching_gbps=1020, fwd_mpps=758.0)
add(ex4400, model="EX4400-48F", ports=48, port_speed="36x 1G SFP + 12x 10G SFP+", port_max_gbps=10, poe="None", poe_w_port=0, poe_budget_w=0,
    switching_gbps=912, fwd_mpps=678.0)

# ---------------- Juniper EX4650 ----------------
add(dict(vendor="Juniper", series="EX4650", os="Junos", form="Fixed", dram_gb=16, flash_gb=64,
         mac=288000, ipv4_routes=208000, stacking="Virtual Chassis", stack_max=4, ospf=True, bgp=True,
         evpn_vxlan=True, macsec=False, mpls=True, redundant_psu=True, datasheet=PS("a00150780enw"),
         poe="None", poe_w_port=0, poe_budget_w=0, verified=V,
         notes="64 GB SSD. IPv4 unicast routes 208,000 (up to 360,000 prefixes in LPM mode). MACsec not listed on the datasheet."),
    model="EX4650-48Y", ports=48, port_speed="10/25G SFP28", port_max_gbps=25, uplinks="8x 40/100G QSFP28", uplink_max_gbps=100,
    switching_gbps=4000, fwd_mpps=2980.0)

# ---------------- Juniper EX9200 ----------------
ex9200 = dict(vendor="Juniper", series="EX9200", os="Junos", form="Modular chassis", dram_gb=64, flash_gb=64,
              mac=1000000, ipv4_routes=512000, stacking="MC-LAG", stack_max=2, ospf=True, bgp=True,
              evpn_vxlan=True, macsec=True, mpls=True, redundant_psu=True, datasheet=PS("a00150784enw"),
              port_speed="Line cards: 1G, 10G, 40G, 100G", port_max_gbps=100, uplinks="Any line-card port up to 100G", uplink_max_gbps=100,
              poe="None", poe_w_port=0, poe_budget_w=0, fwd_mpps=None, verified=V,
              notes="Routing Engine up to 64 GB DRAM and two SSDs up to 64 GB each. 512,000 FIB entries with ML license (256,000 without). Up to 1 million MAC addresses.")
add(ex9200, model="EX9204 chassis", ports=None, switching_gbps=3000,
    notes=ex9200["notes"] + " 2 line-card slots with fabric redundancy (3 without). Port count per chassis not stated.")
add(ex9200, model="EX9208 chassis", ports=None, switching_gbps=7500,
    notes=ex9200["notes"] + " 6 line-card slots. Port count per chassis not stated.")
add(ex9200, model="EX9214 chassis", ports=480, port_speed="Line cards: 1G, 10G, 40G, 100G (480x 10G at wire speed)", switching_gbps=12000,
    notes=ex9200["notes"] + " 11 line-card slots with fabric redundancy (12 without); up to 480 10GbE ports.")

# ---------------- Fortinet FortiSwitch ----------------
FDS = "https://www.fortinet.com/content/dam/fortinet/assets/data-sheets/"
FL = "FortiLink (FortiGate-managed)"
fsa = dict(vendor="Fortinet", series="FortiSwitch Secure Access 100F", os="FortiSwitchOS", form="Fixed",
           stacking=FL, stack_max=None, ospf=True, bgp=False, evpn_vxlan=False, macsec=True, mpls=False,
           redundant_psu=False, ipv4_routes=None, datasheet=FDS + "pdf/fortiswitch-secure-access-series.pdf",
           port_speed="1G", port_max_gbps=1, verified=P,
           notes="Hardware figures from the Secure Access datasheet. Feature flags (OSPF/RIP/VRRP/IS-IS, MACsec) are listed for the whole family; Fortinet says to check the FortiSwitch Feature Matrix per model. Managed from a FortiGate via FortiLink (8 to 300 switches per FortiGate); no stacking.")
add(fsa, model="FS-108F", form="Compact", ports=8, port_speed="1G (1 port is PoE-powered PD)", uplinks="2x 1G SFP", uplink_max_gbps=1,
    poe="None", poe_w_port=0, poe_budget_w=0, switching_gbps=20, fwd_mpps=30.0, dram_gb=0.25, flash_gb=0.03, mac=8000)
add(fsa, model="FS-108F-POE", form="Compact", ports=8, uplinks="2x 1G SFP", uplink_max_gbps=1,
    poe="PoE+", poe_w_port=30, poe_budget_w=65, switching_gbps=20, fwd_mpps=30.0, dram_gb=0.25, flash_gb=0.03, mac=8000)
add(fsa, model="FS-108F-FPOE", form="Compact", ports=8, uplinks="2x 1G SFP", uplink_max_gbps=1,
    poe="PoE+", poe_w_port=30, poe_budget_w=130, switching_gbps=20, fwd_mpps=30.0, dram_gb=0.25, flash_gb=0.03, mac=8000)
for m, poe, w, b in [("FS-124F", "None", 0, 0), ("FS-124F-POE", "PoE+ (12 ports)", 30, 185), ("FS-124F-FPOE", "PoE+", 30, 370)]:
    add(fsa, model=m, ports=24, uplinks="4x 10G SFP+", uplink_max_gbps=10, poe=poe, poe_w_port=w, poe_budget_w=b,
        switching_gbps=128, fwd_mpps=190.0, dram_gb=0.5, flash_gb=0.06, mac=32000)
for m, poe, w, b in [("FS-148F", "None", 0, 0), ("FS-148F-POE", "PoE+ (24 ports)", 30, 370), ("FS-148F-FPOE", "PoE+", 30, 740)]:
    add(fsa, model=m, ports=48, uplinks="4x 10G SFP+", uplink_max_gbps=10, poe=poe, poe_w_port=w, poe_budget_w=b,
        switching_gbps=176, fwd_mpps=260.0, dram_gb=0.5, flash_gb=0.06, mac=32000)
fsg = dict(fsa, series="FortiSwitch Secure Access 100G", dram_gb=1, mac=32000)
add(fsg, model="FS-110G-FPOE", form="Compact", ports=10, port_speed="2x mGig up to 5G + 8x mGig up to 2.5G", port_max_gbps=5,
    uplinks="4x 1/10G SFP+", uplink_max_gbps=10, poe="PoE++ (802.3bt on 2 ports, PoE+ on 8)", poe_w_port=90, poe_budget_w=200,
    switching_gbps=140, fwd_mpps=208.0, flash_gb=0.008)
add(fsg, model="FS-124G", ports=24, port_speed="mGig 10M-2.5G", port_max_gbps=2.5, uplinks="6x 1/10G SFP+", uplink_max_gbps=10,
    poe="None", poe_w_port=0, poe_budget_w=0, switching_gbps=240, fwd_mpps=355.0, flash_gb=0.25)
add(fsg, model="FS-124G-FPOE", ports=24, port_speed="mGig 10M-2.5G", port_max_gbps=2.5, uplinks="6x 1/10G SFP+", uplink_max_gbps=10,
    poe="PoE++ (802.3bt on 8 ports, PoE+ on 16)", poe_w_port=90, poe_budget_w=780, switching_gbps=240, fwd_mpps=355.0, flash_gb=0.25)
fs2 = dict(fsa, series="FortiSwitch Secure Access 200", dram_gb=0.5, flash_gb=0.125, mac=16000, ipv4_routes=64,
           uplinks="4x 1G SFP", uplink_max_gbps=1,
           notes="Hardware figures from the Secure Access datasheet; 64 IPv4 route entries, 512 host entries. Feature flags are listed for the whole family (check the FortiSwitch Feature Matrix per model). Optional external FRPS-740 redundant power on PoE models. Managed from a FortiGate via FortiLink; no stacking.")
add(fs2, model="FS-224D-FPOE", ports=24, poe="PoE+", poe_w_port=30, poe_budget_w=370, switching_gbps=56, fwd_mpps=83.0)
add(fs2, model="FS-224E", ports=24, poe="None", poe_w_port=0, poe_budget_w=0, switching_gbps=56, fwd_mpps=83.0)
add(fs2, model="FS-224E-POE", ports=24, poe="PoE+ (12 ports)", poe_w_port=30, poe_budget_w=180, switching_gbps=56, fwd_mpps=83.0)
add(fs2, model="FS-248D", ports=48, poe="None", poe_w_port=0, poe_budget_w=0, switching_gbps=104, fwd_mpps=155.0)
add(fs2, model="FS-248E-POE", ports=48, poe="PoE+ (24 ports)", poe_w_port=30, poe_budget_w=370, switching_gbps=104, fwd_mpps=155.0)
add(fs2, model="FS-248E-FPOE", ports=48, poe="PoE+", poe_w_port=30, poe_budget_w=740, switching_gbps=104, fwd_mpps=155.0)

fsc = dict(vendor="Fortinet", series="FortiSwitch Secure Campus 300", os="FortiSwitchOS", form="Fixed",
           stacking=FL, stack_max=None, ospf=True, bgp=True, evpn_vxlan=False, macsec=True, mpls=False,
           redundant_psu=True, datasheet=FDS + "pdf/fortiswitch-campus-series.pdf", verified=P,
           notes="Hardware figures from the Secure Campus datasheet. Feature flags (OSPF, BGP, IS-IS, MACsec, MCLAG) are listed for the whole family; check the FortiSwitch Feature Matrix per model. Managed from a FortiGate via FortiLink (8 to 300 switches); no stacking.")
c3 = dict(fsc, dram_gb=2, flash_gb=8, mac=32000, ipv4_routes=38000, uplinks="4x 1/10G SFP+", uplink_max_gbps=10)
add(c3, model="FS-324G", ports=24, port_speed="mGig 10M-2.5G", port_max_gbps=2.5, poe="None", poe_w_port=0, poe_budget_w=0, switching_gbps=200, fwd_mpps=297.0)
add(c3, model="FS-324G-FPOE", ports=24, port_speed="mGig 10M-2.5G", port_max_gbps=2.5, poe="PoE++ (802.3bt Type 4)", poe_w_port=90, poe_budget_w=420, switching_gbps=200, fwd_mpps=297.0)
add(c3, model="FS-348G", ports=48, port_speed="24x mGig 10M-2.5G + 24x 1G", port_max_gbps=2.5, poe="None", poe_w_port=0, poe_budget_w=0, switching_gbps=248, fwd_mpps=369.0)
add(c3, model="FS-348G-FPOE", ports=48, port_speed="24x mGig 10M-2.5G + 24x 1G", port_max_gbps=2.5, poe="PoE++ (802.3bt Type 4)", poe_w_port=90, poe_budget_w=1560,
    switching_gbps=248, fwd_mpps=369.0, notes=fsc["notes"] + " PoE budget 1,560 W with dual AC input (780 W single).")
c4 = dict(fsc, series="FortiSwitch Secure Campus 400", dram_gb=1, flash_gb=0.25, uplinks="4x 1/10G SFP+", uplink_max_gbps=10)
add(c4, model="FS-424E-FIBER", ports=24, port_speed="1G SFP", port_max_gbps=1, poe="None", poe_w_port=0, poe_budget_w=0, switching_gbps=128, fwd_mpps=190.0, mac=32000, ipv4_routes=16000)
add(c4, model="FS-M426E-FPOE", ports=26, port_speed="16x 1G + 8x 2.5G + 2x 5G", port_max_gbps=5, poe="PoE+ (8 ports 4-pair 60 W)", poe_w_port=60, poe_budget_w=421,
    switching_gbps=172, fwd_mpps=255.0, mac=16000, ipv4_routes=1000)
add(c4, model="FS-424E-FPOE", ports=24, port_speed="1G", port_max_gbps=1, poe="PoE+", poe_w_port=30, poe_budget_w=421, switching_gbps=128, fwd_mpps=190.0, mac=16000, ipv4_routes=1000)
c6 = dict(fsc, series="FortiSwitch Secure Campus 600", dram_gb=4, flash_gb=32, mac=64000, ipv4_routes=300000,
          notes=fsc["notes"] + " 32 GB SSD. Dual hot-swap PSUs; PoE budget shown with two PSUs.")
add(c6, model="FS-624F", ports=24, port_speed="mGig 1/2.5/5G", port_max_gbps=5, uplinks="4x 1/10/25G SFP28", uplink_max_gbps=25,
    poe="None", poe_w_port=0, poe_budget_w=0, switching_gbps=440, fwd_mpps=654.0)
add(c6, model="FS-624F-FPOE", ports=24, port_speed="mGig 1/2.5/5G", port_max_gbps=5, uplinks="4x 1/10/25G SFP28", uplink_max_gbps=25,
    poe="PoE++ (802.3bt Type 4)", poe_w_port=90, poe_budget_w=1440, switching_gbps=440, fwd_mpps=654.0)
add(c6, model="FS-648F", ports=48, port_speed="32x mGig 1/2.5G + 16x mGig 1/2.5/5G", port_max_gbps=5, uplinks="8x 1/10/25G SFP28", uplink_max_gbps=25,
    poe="None", poe_w_port=0, poe_budget_w=0, switching_gbps=720, fwd_mpps=1071.0)
add(c6, model="FS-648F-FPOE", ports=48, port_speed="32x mGig 1/2.5G + 16x mGig 1/2.5/5G", port_max_gbps=5, uplinks="8x 1/10/25G SFP28", uplink_max_gbps=25,
    poe="PoE++ (802.3bt Type 4)", poe_w_port=90, poe_budget_w=1800, switching_gbps=720, fwd_mpps=1071.0)
add(fsc, series="FortiSwitch Secure Campus T1024", model="FS-T1024F-FPOE", ports=24, port_speed="mGig 1/2.5/5/10G", port_max_gbps=10,
    uplinks="2x 40/100G QSFP+/QSFP28", uplink_max_gbps=100, poe="PoE++ (802.3bt Type 4)", poe_w_port=90, poe_budget_w=1440,
    switching_gbps=880, fwd_mpps=1309.0, dram_gb=8, flash_gb=8, mac=64000, ipv4_routes=8000,
    notes=fsc["notes"] + " 8 GB SSD. Dual hot-swap PSUs; PoE budget shown with two PSUs.")

fsr = dict(vendor="Fortinet", series="FortiSwitch Rugged", os="FortiSwitchOS", form="Rugged (DIN-rail)",
           stacking=FL, stack_max=None, ospf=True, bgp=True, evpn_vxlan=False, macsec=False, mpls=False,
           redundant_psu=True, datasheet=FDS + "FortiSwitchRugged.pdf", dram_gb=1, flash_gb=1, verified=P,
           notes="Fanless, -40 to 75 °C, redundant DC input terminals. Routing protocols (OSPF, BGP, IS-IS) are listed for the family, but the 108F, 112F-POE and 216F-POE have no hardware routing table. MACsec not listed. Managed from a FortiGate via FortiLink.")
add(fsr, model="FSR-108F", ports=6, port_speed="1G", port_max_gbps=1, uplinks="2x 1G SFP", uplink_max_gbps=1, poe="None", poe_w_port=0, poe_budget_w=0,
    switching_gbps=16, fwd_mpps=23.8, mac=16000, ipv4_routes=None)
add(fsr, model="FSR-112F-POE", ports=8, port_speed="1G", port_max_gbps=1, uplinks="4x 1G SFP", uplink_max_gbps=1, poe="PoE++ (802.3bt)", poe_w_port=90, poe_budget_w=240,
    switching_gbps=24, fwd_mpps=35.7, mac=16000, ipv4_routes=None)
add(fsr, model="FSR-216F-POE", ports=16, port_speed="1G", port_max_gbps=1, uplinks="4x 1/10G SFP+", uplink_max_gbps=10, poe="PoE++ (802.3bt)", poe_w_port=90, poe_budget_w=360,
    switching_gbps=112, fwd_mpps=166.0, mac=16000, ipv4_routes=None)
add(fsr, model="FSR-424F-POE", ports=24, port_speed="12x 1/2.5G RJ45 + 12x 1/2.5G SFP", port_max_gbps=2.5, uplinks="4x 10G SFP+ + 2x 40G QSFP+", uplink_max_gbps=40,
    poe="PoE+ (12 ports 4-pair 60 W)", poe_w_port=60, poe_budget_w=421, switching_gbps=360, fwd_mpps=536.0, mac=32000, ipv4_routes=16000, flash_gb=0.25,
    notes="Fanless, -40 to 70 °C, redundant DC input terminals. Hardware routing: 16,000 IPv4 routes. Routing protocols (OSPF, BGP, IS-IS) listed for the family. MACsec not listed. Managed from a FortiGate via FortiLink.")

cols = ["vendor","series","model","os","form","ports","port_speed","port_max_gbps","uplinks","uplink_max_gbps",
        "poe","poe_w_port","poe_budget_w","switching_gbps","fwd_mpps","dram_gb","flash_gb","mac","ipv4_routes",
        "stacking","stack_max","ospf","bgp","evpn_vxlan","macsec","mpls","redundant_psu","verified","notes","datasheet"]
out = []
for r in rows:
    missing = [c for c in cols if c not in r]
    if missing: sys.exit(f"{r.get('model')}: missing {missing}")
    o = {c: r[c] for c in cols}
    for b in ["ospf","bgp","evpn_vxlan","macsec","mpls","redundant_psu"]:
        o[b] = "Yes" if o[b] else "No"
    out.append(o)
models = [o["model"] for o in out]
assert len(models) == len(set(models)), "duplicate model"
json.dump({"rows": out, "meta": [
    {"label": "How made", "value": "Checked by Claude on 13 Nov 2026 against the Cisco datasheets, HPE Aruba QuickSpecs, HPE-hosted Juniper datasheets and Fortinet FortiSwitch datasheets linked in each row. 'verified' says how much of each row was confirmed; 'notes' gives the datasheet's own wording where it matters."}]},
    open(sys.argv[1], "w"), indent=0)
from collections import Counter
print(len(out), "rows", Counter(o["verified"] for o in out))
