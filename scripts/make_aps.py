"""Generate data/access_points.json: access point specs checked against vendor datasheets (14 Nov 2026)."""
import json, sys

V, P = "Verified", "Partly verified"
CISCO = "https://www.cisco.com/site/us/en/products/collateral/networking/wireless/access-points/"
CISCO6 = "https://www.cisco.com/c/en/us/products/collateral/wireless/"
PS = lambda i: "https://www.hpe.com/psnow/doc/" + i
FAP = "https://www.fortinet.com/content/dam/fortinet/assets/data-sheets/pdf/fortiap-series.pdf"

rows = []
def add(base, **kw):
    r = dict(base); r.update(kw); rows.append(r)

# ---------------- Cisco ----------------
c = dict(vendor="Cisco", management="Catalyst 9800 controller or Meraki cloud", verified=V, ip_rating=None, ble="Yes")
c7 = dict(c, wifi="Wi-Fi 7", bands="2.4 / 5 / 6 GHz", has_6ghz="Yes", environment="Indoor")
add(c7, family="Cisco Wireless 9172", model="CW9172I", radios="Tri-radio: 2.4 GHz 2x2, 5 GHz 2x2 (or 4x4 with 6 GHz off), 6 GHz 2x2 + scan + IoT radio",
    max_ss=4, max_rate_gbps=9.0, uplinks="1x 2.5G mGig", uplink_ports=1, uplink_max_gbps=2.5,
    poe="802.3bt Class 5 (802.3at with reduced radios)", full_on_at="No", max_power_w=32, usb="Yes",
    datasheet=CISCO + "wireless-9172-series-access-points-ds.html",
    notes="Up to 9 Gbps PHY rate with 2x2 320 MHz on 6 GHz. BLE 6 IoT radio. Requires a Cisco Networking Subscription.")
add(c7, family="Cisco Wireless 9172", model="CW9172H", environment="Wall plate", radios="Tri-radio: 2.4 / 5 / 6 GHz, each 2x2 + scan + IoT radio",
    max_ss=2, max_rate_gbps=9.0, uplinks="1x 2.5G mGig uplink + 3x 1G LAN (1 with PoE out)", uplink_ports=1, uplink_max_gbps=2.5,
    poe="802.3bt Class 5 (802.3at without PoE out)", full_on_at="No", max_power_w=41, usb="No",
    datasheet=CISCO + "wireless-9172-series-access-points-ds.html",
    notes="Wall-plate AP with 3 LAN ports and a pass-through port. BLE 6 IoT radio.")
for m, ant in [("CW9176I", "internal omni"), ("CW9176D1", "internal directional")]:
    add(c7, family="Cisco Wireless 9176", model=m, radios="Tri-radio 4x4: 2.4 (or second 5) / 5 / 6 GHz + IoT radio, " + ant + " antennas",
        max_ss=4, max_rate_gbps=18.0, uplinks="1x 10G mGig", uplink_ports=1, uplink_max_gbps=10,
        poe="802.3bt Class 5 (802.3at with 2.4 GHz at 2x2)", full_on_at="No", max_power_w=39, usb="Yes",
        datasheet=CISCO + "wireless-9176-series-access-points-ds.html",
        notes="Up to 18 Gbps (23 Gbps in 5+5+6 GHz mode). GNSS/GPS, UWB and accelerometer built in. BLE 5.3 (BLE 6 by software).")
add(c7, family="Cisco Wireless 9178", model="CW9178I", radios="Tri-radio 4x4 (quad-radio mode adds a second 4x4 5 GHz) + IoT radio",
    max_ss=4, max_rate_gbps=24.0, uplinks="2x 10G mGig (redundant)", uplink_ports=2, uplink_max_gbps=10,
    poe="802.3bt Class 6 (802.3at with reduced radios)", full_on_at="No", max_power_w=47, usb="Yes",
    datasheet=CISCO + "wireless-9178-series-access-points-ds.html",
    notes="Up to 24 Gbps in quad-radio mode (18 Gbps tri-radio). GNSS/GPS, UWB, accelerometer.")
c6e = dict(c, wifi="Wi-Fi 6E", bands="2.4 / 5 / 6 GHz", has_6ghz="Yes", environment="Indoor", usb="Yes")
add(c6e, family="Cisco Catalyst 9162", model="CW9162I", radios="Tri-radio: 2.4 / 5 / 6 GHz, each 2x2", max_ss=2, max_rate_gbps=3.9,
    uplinks="1x 2.5G mGig", uplink_ports=1, uplink_max_gbps=2.5, poe="802.3at (full); 802.3af reduced", full_on_at="Yes", max_power_w=25.5,
    datasheet=CISCO6 + "catalyst-9100ax-access-points/cat-9162-series-access-points-ds.html", notes="BLE 5.1. Also runs from 12 V DC.")
add(c6e, family="Cisco Catalyst 9164", model="CW9164I", radios="Tri-radio: 2.4 GHz 2x2, 5 GHz 4x4, 6 GHz 4x4", max_ss=4, max_rate_gbps=7.49,
    uplinks="1x 2.5G mGig", uplink_ports=1, uplink_max_gbps=2.5, poe="802.3bt (802.3at supported)", full_on_at="No", max_power_w=30.0,
    datasheet=CISCO6 + "catalyst-9164-series-access-points/catalyst-9164-series-access-points-ds.html", notes="BLE 5.1. Max draw 30 W on 802.3bt, 25 W on 802.3at.")
for m, ant in [("CW9166I", "internal omni"), ("CW9166D1", "internal directional")]:
    add(c6e, family="Cisco Catalyst 9166", model=m, radios="Tri-radio 4x4: 2.4 / 5 / 6 GHz (plus 5 GHz XOR), " + ant, max_ss=4, max_rate_gbps=7.78,
        uplinks="1x 5G mGig", uplink_ports=1, uplink_max_gbps=5, poe="802.3bt (802.3at supported)", full_on_at="No", max_power_w=30.5,
        datasheet=CISCO6 + "catalyst-9166-series-access-points/catalyst-9166-series-access-points-ds.html",
        notes="BLE 5.1 and environmental sensors. Max draw 30.5 W on 802.3bt, 25.5 W on 802.3at.")
add(c6e, family="Cisco Catalyst 9163E", model="CW9163E", environment="Outdoor", radios="Tri-radio: 2.4 / 5 / 6 GHz, each 2x2 + IoT and scan radios, external antennas",
    max_ss=2, max_rate_gbps=3.9, uplinks="1x 2.5G mGig", uplink_ports=1, uplink_max_gbps=2.5, poe="802.3at (full)", full_on_at="Yes", max_power_w=25.5,
    usb=None, ip_rating="IP67", datasheet=CISCO6 + "catalyst-9163e-access-point/nb-06-cat-9163e-series-access-ds-cte-en.html",
    notes="Weatherized; external antennas sold separately; GNSS antenna connector. BLE 5.1.")
add(dict(c, wifi="Wi-Fi 6", bands="2.4 / 5 GHz", has_6ghz="No"), family="Cisco Catalyst 9124AX", model="C9124AXI", environment="Outdoor",
    radios="Dual-radio: 2.4 GHz 4x4, 5 GHz 4x4", max_ss=4, max_rate_gbps=5.38,
    uplinks="1x 2.5G + 1x 1G SFP (+ 1x 1G PoE-out downlink)", uplink_ports=2, uplink_max_gbps=2.5,
    poe="802.3bt/UPOE; 802.3at and 802.3af with reduced radios", full_on_at="No", max_power_w=None, usb=None, ip_rating="IP67",
    datasheet=CISCO6 + "catalyst-9100ax-access-points/nb-06-cat9124-ser-ap-ds-cte-en.html",
    notes="Outdoor IP66/IP67. Max power not stated in watts. BLE 5. DC 24-56 V input option.")

# ---------------- HPE Aruba ----------------
a = dict(vendor="HPE Aruba", management="HPE Aruba Networking Central or controller", verified=V, ip_rating=None, ble="Yes", environment="Indoor")
a7 = dict(a, wifi="Wi-Fi 7", bands="2.4 / 5 / 6 GHz", has_6ghz="Yes")
add(a7, family="750 Series", model="AP-755 (750 Series)", radios="Tri-radio: 2.4 / 5 / 6 GHz, each 4x4", max_ss=4, max_rate_gbps=18.7,
    uplinks="2x 10G (hitless failover)", uplink_ports=2, uplink_max_gbps=10, poe="802.3bt Class 6 unrestricted (Class 3-5 restricted)", full_on_at="No",
    max_power_w=51, usb="Yes", datasheet=PS("a00140933enw"),
    notes="Max 40 W (51 W with USB devices) on PoE. Two BLE 5.4/Zigbee radios, two USB ports, GNSS receiver.")
add(a7, family="740 Series", model="AP-745 (740 Series)", radios="Tri-radio: 2.4 GHz 2x2, 5 GHz 4x4, 6 GHz 4x4", max_ss=4, max_rate_gbps=9.0,
    uplinks="1x 5G", uplink_ports=1, uplink_max_gbps=5, poe="802.3bt Class 6 unrestricted (802.3at reduced)", full_on_at="No",
    max_power_w=36.8, usb="Yes", datasheet=PS("a00147704enw"), notes="Max 25.7 W (36.8 W with USB devices). BLE 5.4 or Zigbee radio.")
add(a7, family="730 Series", model="730 Series (AP-734/735)", radios="Tri-radio: 2.4 / 5 / 6 GHz, each 2x2 (2.4 GHz can switch to second 5 or 6 GHz)",
    max_ss=2, max_rate_gbps=9.3, uplinks="2x 5G (LACP)", uplink_ports=2, uplink_max_gbps=5, poe="802.3at/bt (Class 4 or higher)", full_on_at="Not stated",
    max_power_w=36, usb="Yes", datasheet=PS("a00138541enw"),
    notes="Up to 14.4 Gbps in dual-5 or dual-6 GHz mode. Max 24 W (36 W with USB). Two BLE 5.4/Zigbee radios, two USB ports. MACsec on uplinks.")
add(a7, family="720 Series", model="720 Series (AP-724/725)", radios="Tri-radio: 2.4 / 5 / 6 GHz, each 2x2", max_ss=2, max_rate_gbps=4.7,
    uplinks="1x 2.5G", uplink_ports=1, uplink_max_gbps=2.5, poe="802.3at (802.3af/at, Class 3 or higher)", full_on_at="Yes",
    max_power_w=22.8, usb="Yes", datasheet=PS("a00146618enw"), notes="Max 17.1 W (22.8 W with USB). Bluetooth 5.4 or Zigbee radio.")
a6e = dict(a, wifi="Wi-Fi 6E", bands="2.4 / 5 / 6 GHz", has_6ghz="Yes", usb="Yes")
add(a6e, family="650 Series", model="AP-655 (650 Series)", radios="Tri-radio: 2.4 / 5 / 6 GHz, each 4x4", max_ss=4, max_rate_gbps=7.8,
    uplinks="2x 5G", uplink_ports=2, uplink_max_gbps=5, poe="802.3af/at/bt (Class 3 or higher)", full_on_at="Not stated", max_power_w=46.5,
    datasheet=PS("a00119145enw"), notes="Max 40.3 W on PoE (46.5 W with USB). BLE 5.0.")
add(a6e, family="630 Series", model="AP-635 (630 Series)", radios="Tri-radio: 2.4 / 5 / 6 GHz, each 2x2", max_ss=2, max_rate_gbps=3.9,
    uplinks="2x 2.5G", uplink_ports=2, uplink_max_gbps=2.5, poe="802.3at/bt (Class 4 or higher)", full_on_at="Not stated", max_power_w=29.4,
    datasheet=PS("a00114648enw"), notes="Max 23.8 W on PoE (29.4 W with USB). BLE 5.0.")
add(a6e, family="610 Series", model="AP-615 (610 Series)", radios="Tri-radio: 2.4 / 5 / 6 GHz, each 2x2", max_ss=2, max_rate_gbps=3.6,
    uplinks="1x 2.5G", uplink_ports=1, uplink_max_gbps=2.5, poe="802.3af/at (Class 3 or higher)", full_on_at="Yes", max_power_w=20.9,
    datasheet=PS("a00125607enw"), notes="Compact, low power: max 14.7 W on PoE (20.9 W with USB). BLE 5.0.")
a6 = dict(a, wifi="Wi-Fi 6", bands="2.4 / 5 GHz", has_6ghz="No")
add(a6, family="550 Series", model="AP-555 (550 Series)", radios="Tri-radio capable: 5 GHz up to 8 streams (dual 5 GHz) + 2.4 GHz 4x4", max_ss=8, max_rate_gbps=5.37,
    uplinks="2x 5G", uplink_ports=2, uplink_max_gbps=5, poe="802.3at/bt (Class 4 or higher)", full_on_at="No", max_power_w=38.2, usb="Yes",
    datasheet=PS("a00064820enw"), notes="Max 38.2 W on 802.3bt or dual 802.3at (25.1 W on single 802.3at). BLE 5.0.")
add(a6, family="530 Series", model="AP-535 (530 Series)", radios="Dual-radio: 5 GHz 4x4, 2.4 GHz 4x4", max_ss=4, max_rate_gbps=2.97,
    uplinks="2x 5G", uplink_ports=2, uplink_max_gbps=5, poe="802.3at/bt (Class 4 or higher)", full_on_at="No", max_power_w=26.4, usb="Yes",
    datasheet=PS("a00064816enw"), notes="Max 26.4 W on 802.3bt or dual 802.3at (23.3 W on 802.3at). Bluetooth 5.0.")
add(a6, family="510 Series", model="AP-515 (510 Series)", radios="Dual-radio: 5 GHz 4x4, 2.4 GHz 2x2", max_ss=4, max_rate_gbps=2.69,
    uplinks="1x 2.5G", uplink_ports=1, uplink_max_gbps=2.5, poe="802.3af/at/bt (Class 3 or higher)", full_on_at="Yes", max_power_w=20.8, usb="Yes",
    datasheet=PS("a00058595enw"), notes="Max 20.8 W on 802.3at/bt (13.5 W on 802.3af with power management).")
add(a6, family="500 Series", model="AP-505 (500 Series)", radios="Dual-radio: 5 GHz 2x2, 2.4 GHz 2x2", max_ss=2, max_rate_gbps=1.49,
    uplinks="1x 1G", uplink_ports=1, uplink_max_gbps=1, poe="802.3af/at (Class 3 or 4)", full_on_at="Yes", max_power_w=None, usb="Yes",
    datasheet=PS("a00081687enw"), notes="Cost-effective Wi-Fi 6. BLE 5.0. Max power not captured from the datasheet.")
add(a6e, family="670 Series", model="AP-675 (670 Series)", environment="Outdoor", radios="Tri-radio: 2.4 / 5 / 6 GHz, each 2x2", max_ss=2, max_rate_gbps=3.9,
    uplinks="1x 2.5G", uplink_ports=1, uplink_max_gbps=2.5, poe="802.3at/bt (Class 4 or higher)", full_on_at="Not stated", max_power_w=45.5,
    ip_rating="IP66", datasheet=PS("a00136588enw"), notes="Max 29 W on PoE (45.5 W with up to 16.5 W USB). BLE 5.0.")
add(a6, family="570 Series", model="570 Series (AP-574/575/577)", environment="Outdoor", radios="Dual-radio: 5 GHz 4x4, 2.4 GHz 2x2", max_ss=4, max_rate_gbps=3.0,
    uplinks="2x Ethernet (E0 2.5G SmartRate)", uplink_ports=2, uplink_max_gbps=2.5, poe="802.3at/bt (Class 4 or higher)", full_on_at="Yes",
    max_power_w=32.0, usb=None, ip_rating="IP66", datasheet=PS("a00096370enw"),
    notes="Max 26.1 W single port full function, 32 W with dual PoE ports. Bluetooth for location.")

# ---------------- Juniper (HPE Mist) ----------------
j = dict(vendor="Juniper", management="Juniper Mist cloud (HPE Mist)", verified=V, ip_rating=None, ble="Yes", environment="Indoor")
j7 = dict(j, wifi="Wi-Fi 7", bands="2.4 / 5 / 6 GHz", has_6ghz="Yes")
add(j7, family="Mist AP47", model="AP47", radios="Tri-radio 4x4 (2.4 / 5 / 6 GHz) + tri-band scan radio + dual IoT", max_ss=4, max_rate_gbps=18.67,
    uplinks="2x 10G (dual PoE failover)", uplink_ports=2, uplink_max_gbps=10, poe="802.3bt Class 6 (802.3at reduced)", full_on_at="No",
    max_power_w=None, usb="Yes", datasheet=PS("a00150816enw"),
    notes="11,528 + 5,764 + 1,376 Mbps. UWB, GPS, vBLE location. Full function on 802.3bt Class 6.")
add(j7, family="Mist AP36/AP37", model="AP36", radios="Tri-radio: 5 / 6 GHz 4x4, 2.4 GHz 2x2 + scan radio", max_ss=4, max_rate_gbps=17.98,
    uplinks="1x 10G + 1x 1G (PoE out)", uplink_ports=2, uplink_max_gbps=10, poe="802.3bt", full_on_at="Not stated", max_power_w=None, usb="Yes",
    datasheet=PS("a50014091enw"), notes="11,528 + 5,764 + 688 Mbps. Second port gives 15.4 W PoE out on 802.3bt.")
add(j7, family="Mist AP27", model="AP27", radios="Tri-radio: 2.4 / 5 / 6 GHz, 2x2 + scan radio", max_ss=2, max_rate_gbps=9.39,
    uplinks="1x 10G + 1x 1G", uplink_ports=2, uplink_max_gbps=10, poe="802.3at full function (802.3af cloud only)", full_on_at="Yes", max_power_w=None, usb="Yes",
    datasheet=PS("a00156795enw"), notes="5.8 + 2.9 + 0.688 Gbps. BLE and UWB.")
add(j7, family="Mist AP17", model="AP17", environment="Wall plate", radios="Tri-radio: 2.4 / 5 / 6 GHz, 2x2 + scan radio", max_ss=2, max_rate_gbps=9.39,
    uplinks="1x 10G uplink + 3x 1G LAN (1 PoE out)", uplink_ports=1, uplink_max_gbps=10, poe="802.3at (802.3bt for PoE out)", full_on_at="Not stated",
    max_power_w=None, usb="No", datasheet=PS("a00156302enw"), notes="Wall-plate AP. 5.8 + 2.9 + 0.688 Gbps.")
add(j7, family="Mist AP66", model="AP66", environment="Outdoor", radios="Tri-radio: 2.4 / 5 / 6 GHz, 2x2 + scan radio", max_ss=2, max_rate_gbps=9.39,
    uplinks="1x 10G", uplink_ports=1, uplink_max_gbps=10, poe="802.3at full function (802.3af cloud only)", full_on_at="Yes", max_power_w=None, usb="No",
    ip_rating="IP67", datasheet=PS("a50014092enw"), notes="Ruggedized Wi-Fi 7 outdoor AP. BLE 6.0 and GNSS/GPS.")
j6e = dict(j, wifi="Wi-Fi 6E", bands="2.4 / 5 / 6 GHz", has_6ghz="Yes")
add(j6e, family="Mist AP45", model="AP45", radios="Tri-radio 4x4 (2.4 / 5 / 6 GHz) + scan radio", max_ss=4, max_rate_gbps=8.35,
    uplinks="1x Ethernet (Eth0) + Eth1", uplink_ports=2, uplink_max_gbps=None, poe="802.3bt full (802.3at reduced)", full_on_at="No", max_power_w=None, usb="No",
    datasheet=PS("a50013796enw"), notes="4,800 + 2,400 + 1,148 Mbps. Eth0 speed not captured from the datasheet; check it before relying on it.", verified=P)
add(j6e, family="Mist AP24", model="AP24", radios="Tri-band capable, 2x2 + scan radio", max_ss=2, max_rate_gbps=4.18,
    uplinks="1x 2.5G", uplink_ports=1, uplink_max_gbps=2.5, poe="802.3at", full_on_at="Not stated", max_power_w=None, usb="Yes",
    datasheet=PS("a00150853enw"), notes="2,400 + 1,200 + 575 Mbps.")
add(j6e, family="Mist AP64", model="AP64", environment="Outdoor", radios="Tri-radio 2x2 + scan radio", max_ss=2, max_rate_gbps=4.18,
    uplinks="1x 2.5G", uplink_ports=1, uplink_max_gbps=2.5, poe="802.3at", full_on_at="Not stated", max_power_w=None, usb=None, ip_rating="IP67",
    datasheet=PS("a00150845enw"), notes="2,400 + 1,200 + 575 Mbps. 6 GHz disabled in the US and Canada until AFC approval.")
j6 = dict(j, wifi="Wi-Fi 6", bands="2.4 / 5 GHz", has_6ghz="No", usb="Yes")
add(j6, family="Mist AP43", model="AP43", radios="Dual-radio: 5 GHz 4x4, 2.4 GHz 4x4 + scan radio", max_ss=4, max_rate_gbps=3.55,
    uplinks="1x 2.5G + 1x 1G", uplink_ports=2, uplink_max_gbps=2.5, poe="802.3at or 802.3bt, or 12 V DC", full_on_at="Not stated", max_power_w=None,
    datasheet=PS("a00150854enw"), notes="2,400 + 1,148 Mbps.")
add(j6, family="Mist AP33", model="AP33", radios="Dual-radio: 5 GHz 4x4, 2.4 GHz 2x2 + scan radio", max_ss=4, max_rate_gbps=3.0,
    uplinks="1x 2.5G + 1x 1G", uplink_ports=2, uplink_max_gbps=2.5, poe="802.3at or 802.3bt", full_on_at="Not stated", max_power_w=None,
    datasheet=PS("a00150801enw"), notes="Up to 3 Gbps aggregate.")
add(j6, family="Mist AP32", model="AP32", radios="Dual-radio: 5 GHz 4x4, 2.4 GHz 2x2 + scan radio", max_ss=4, max_rate_gbps=3.0,
    uplinks="1x 2.5G + 1x 1G", uplink_ports=2, uplink_max_gbps=2.5, poe="802.3at or 802.3bt", full_on_at="Not stated", max_power_w=None,
    datasheet=PS("a00150849enw"), notes="Up to 3 Gbps aggregate (2,400 Mbps on 5 GHz).")

# ---------------- Fortinet FortiAP ----------------
f = dict(vendor="Fortinet", management="FortiGate, FortiManagement Cloud or SASE", verified=V, ip_rating=None, ble="Yes", datasheet=FAP)
f7 = dict(f, wifi="Wi-Fi 7", bands="2.4 / 5 / 6 GHz", has_6ghz="Yes", environment="Indoor")
add(f7, family="FortiAP 441K/443K", model="FortiAP 441K", radios="4 radios (2.4 / 5 / 6 GHz + scan), 4x4 + BLE", max_ss=4, max_rate_gbps=21.33,
    uplinks="2x 10G mGig", uplink_ports=2, uplink_max_gbps=10, poe="802.3bt or 2x 802.3at (hitless PoE failover)", full_on_at="No",
    max_power_w=41.7, usb="Yes", notes="1.148 + 8.648 + 11.53 Gbps. USB 3.0. 443K is the external-antenna version.")
add(f7, family="FortiAP 241K/243K", model="FortiAP 241K", radios="4 radios (2.4 / 5 / 6 GHz + scan), 2x2 + BLE", max_ss=2, max_rate_gbps=10.75,
    uplinks="1x 10G mGig + 1x 1G", uplink_ports=2, uplink_max_gbps=10, poe="802.3bt (802.3af low mode)", full_on_at="Not stated",
    max_power_w=26.1, usb="Yes", notes="688 Mbps + 4.3 Gbps + 5.76 Gbps. 243K is the external-antenna version.")
add(f7, family="FortiAP 231K", model="FortiAP 231K", radios="3 Wi-Fi radios (2.4 / 5 / 6 GHz), 2x2 + BLE", max_ss=2, max_rate_gbps=9.33,
    uplinks="1x 5G mGig", uplink_ports=1, uplink_max_gbps=5, poe="802.3at (full)", full_on_at="Yes", max_power_w=15.2, usb="No",
    notes="688 Mbps + 2.88 Gbps + 5.76 Gbps. Also 12 V DC.")
add(dict(f, wifi="Wi-Fi 7", bands="2.4 / 5 GHz", has_6ghz="No", environment="Indoor"), family="FortiAP 221K", model="FortiAP 221K",
    radios="2 Wi-Fi radios (2.4 / 5 GHz), 2x2 + BLE", max_ss=2, max_rate_gbps=3.57, uplinks="1x 2.5G mGig", uplink_ports=1, uplink_max_gbps=2.5,
    poe="802.3at (full)", full_on_at="Yes", max_power_w=16.3, usb="No", notes="688 Mbps + 2.88 Gbps. Dual-band Wi-Fi 7.")
add(f7, family="FortiAP 23JK", model="FortiAP 23JK", environment="Wall plate", radios="3 Wi-Fi radios (2.4 / 5 / 6 GHz) + scan, 2x2 + BLE", max_ss=2,
    max_rate_gbps=9.33, uplinks="1x 10G mGig uplink + 3x 1G LAN (1 PoE out)", uplink_ports=1, uplink_max_gbps=10, poe="802.3bt", full_on_at="Not stated",
    max_power_w=31, usb="No", notes="Wall-jack AP. 688 Mbps + 2.88 Gbps + 5.76 Gbps. 19 W without PoE out.")
add(f7, family="FortiAP 244K", model="FortiAP 244K", environment="Outdoor", radios="4 radios (2.4 / 5 / 6 GHz + scan), 2x2 + BLE", max_ss=2,
    max_rate_gbps=10.75, uplinks="1x 5G mGig (PoE in) + 1x 10G SFP+", uplink_ports=2, uplink_max_gbps=10, poe="802.3bt", full_on_at="Not stated",
    max_power_w=26, usb="No", ip_rating="IP67", notes="688 Mbps + 4.3 Gbps + 5.76 Gbps. GNSS.")
add(dict(f, wifi="Wi-Fi 7", bands="2.4 / 5 GHz", has_6ghz="No", environment="Outdoor"), family="FortiAP 222KL", model="FortiAP 222KL",
    radios="2 Wi-Fi radios (2.4 / 5 GHz), 2x2 + LoRaWAN + LTE Cat4 + GNSS", max_ss=2, max_rate_gbps=3.57,
    uplinks="1x 2.5G mGig (PoE in) + 1x 1G (PoE out)", uplink_ports=2, uplink_max_gbps=2.5, poe="802.3bt or passive PoE (included)", full_on_at="Not stated",
    max_power_w=26, usb="No", ip_rating="IP67", notes="Outdoor IoT AP with LoRaWAN and LTE backhaul. 688 Mbps + 2.88 Gbps.")
add(dict(f, wifi="Wi-Fi 6E", bands="2.4 / 5 / 6 GHz", has_6ghz="Yes", environment="Outdoor"), family="FortiAP 432G", model="FortiAP 432G",
    radios="3 radios (2.4 / 5 / 6 GHz), 4x4 + BLE, external antennas", max_ss=4, max_rate_gbps=8.35,
    uplinks="1x 10G mGig (PoE in) + 1x 1G (PoE out)", uplink_ports=2, uplink_max_gbps=10, poe="802.3bt", full_on_at="Not stated",
    max_power_w=41.2, usb="No", ip_rating="IP67", notes="1,148 + 2,402 + 4,804 Mbps. 41.2 W includes 12.9 W PoE out. GNSS.")
add(dict(f, wifi="Wi-Fi 6E", bands="2.4 / 5 / 6 GHz", has_6ghz="Yes", environment="Outdoor"), family="FortiAP 234G", model="FortiAP 234G",
    radios="3 radios (2.4 / 5 / 6 GHz), 2x2 + BLE", max_ss=2, max_rate_gbps=4.18,
    uplinks="1x 2.5G + 1x 1G", uplink_ports=2, uplink_max_gbps=2.5, poe="802.3at or passive PoE (included)", full_on_at="Yes",
    max_power_w=28, usb="No", ip_rating="IP67", notes="574 + 1,201 + 2,401 Mbps. 6 GHz subject to regional approval.")

cols = ["vendor","family","model","wifi","environment","bands","has_6ghz","radios","max_ss","max_rate_gbps","uplinks","uplink_ports",
        "uplink_max_gbps","poe","full_on_at","max_power_w","ble","usb","ip_rating","management","verified","notes","datasheet"]
out = []
for r in rows:
    missing = [k for k in cols if k not in r]
    if missing: sys.exit(f"{r.get('model')}: missing {missing}")
    out.append({k: r[k] for k in cols})
assert len({o["model"] for o in out}) == len(out), "duplicate model"
json.dump({"rows": out, "meta": [{"label": "How made", "value": "Checked by Claude on 14 Nov 2026 against the Cisco, HPE Aruba, HPE Mist (Juniper) and Fortinet access point datasheets linked in each row."}]},
          open(sys.argv[1], "w"), indent=0)
from collections import Counter
print(len(out), "APs", Counter(o["vendor"] for o in out))
