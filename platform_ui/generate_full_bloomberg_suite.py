"""
generate_full_bloomberg_suite.py
Constructs the complete Bloomberg Terminal multi-window suite replicating all 29 images from Bloomberg_Map:
- Crude Oil Pipelines (Image 27) & Natural Gas Pipelines (Image 12)
- Manhattan Street-Level Satellite Zoom & FDIC Tooltip (Images 7, 9, 10)
- Vessel Berth Visits Table (Image 5)
- Greg Mortimer AIS Voyage Vector & Tooltip (Image 8)
- World Equity Markets Heatmap (Images 3, 4)
- Weather Overlays (Images 2, 3)
- SPLC Supply Chain Analysis for AAPL and LMT (Images 20, 24, 25)
- FXC Currency Cross-Rates Matrix (Image 1)
- VOL 3D Volatility Surface (Images 13, 17)
- GPC Candlestick Chart with Technical Checklist (Images 14, 15, 16)
- READ Most Read Stories News Wire (Images 18, 19)
"""

import json
import os
import sys

BASE_DIR = r"F:\documents\SOIC\EconAgent_Platform\platform_ui"
sys.path.insert(0, BASE_DIR)

from compact_branches_payload import BANKS_LIST, STATES_LIST, TYPES_LIST, BRANCHES_COMPACT

# ==============================================================================
# DATASET 1: CRUDE OIL PIPELINES (Worldwide Major Arteries - Image 27)
# ==============================================================================
CRUDE_PIPELINES = [
    {
        "id": "pipe_keystone",
        "name": "Keystone Pipeline System",
        "company": "TC Energy",
        "type": "Interstate / Transnational",
        "fuel": "Heavy Crude Oil (WCS)",
        "capacity": "620,000 bpd",
        "length": "4,324 km (2,687 mi)",
        "diameter": "36 inch",
        "status": "In Service / Commissioned",
        "coords": [[52.67, -111.30], [49.00, -104.00], [40.03, -97.02], [35.98, -96.76], [29.87, -93.93]]
    },
    {
        "id": "pipe_taps",
        "name": "Trans-Alaska Pipeline System (TAPS)",
        "company": "Alyeska Pipeline Service Co",
        "type": "Interstate",
        "fuel": "Alaska North Slope Crude",
        "capacity": "2,000,000 bpd (Nameplate)",
        "length": "1,287 km (800 mi)",
        "diameter": "48 inch",
        "status": "In Service / Commissioned",
        "coords": [[70.25, -148.42], [67.05, -150.35], [64.83, -147.72], [61.13, -146.35]]
    },
    {
        "id": "pipe_enbridge",
        "name": "Enbridge Mainline System",
        "company": "Enbridge Inc",
        "type": "Interstate / Transnational",
        "fuel": "Light & Heavy Crude",
        "capacity": "3,000,000 bpd",
        "length": "5,360 km (3,330 mi)",
        "diameter": "36-42 inch",
        "status": "In Service / Commissioned",
        "coords": [[53.54, -113.49], [49.88, -99.95], [46.72, -92.10], [42.97, -82.40], [43.65, -79.38]]
    },
    {
        "id": "pipe_dapl",
        "name": "Dakota Access Pipeline (DAPL)",
        "company": "Energy Transfer Partners",
        "type": "Interstate",
        "fuel": "Bakken Light Sweet Crude",
        "capacity": "750,000 bpd",
        "length": "1,886 km (1,172 mi)",
        "diameter": "30 inch",
        "status": "In Service / Commissioned",
        "coords": [[48.31, -102.39], [46.80, -100.78], [42.50, -94.00], [38.75, -89.09]]
    },
    {
        "id": "pipe_colonial",
        "name": "Colonial Pipeline Trunkline",
        "company": "Colonial Pipeline Co",
        "type": "Interstate",
        "fuel": "Refined Petroleum Products",
        "capacity": "2,500,000 bpd",
        "length": "8,850 km (5,500 mi network)",
        "diameter": "36-40 inch",
        "status": "In Service / Commissioned",
        "coords": [[29.76, -95.36], [30.45, -91.18], [33.74, -84.38], [36.07, -79.79], [38.90, -77.03], [40.63, -74.24]]
    },
    {
        "id": "pipe_permian",
        "name": "Permian Basin Express / Cactus",
        "company": "Plains All American",
        "type": "Intrastate",
        "fuel": "Permian WTI Crude",
        "capacity": "670,000 bpd",
        "length": "950 km (590 mi)",
        "diameter": "26 inch",
        "status": "In Service / Commissioned",
        "coords": [[31.99, -102.07], [31.10, -100.50], [29.42, -98.49], [27.80, -97.39]]
    },
    {
        "id": "pipe_druzhba",
        "name": "Druzhba Pipeline (Friendship)",
        "company": "Transneft / PERN / MERO",
        "type": "Transnational Trans-European",
        "fuel": "Urals Crude Oil",
        "capacity": "1,400,000 bpd",
        "length": "4,000 km (2,500 mi)",
        "diameter": "40 inch",
        "status": "In Service (Southern Leg)",
        "coords": [[53.20, 50.15], [53.25, 34.36], [52.05, 29.25], [52.54, 19.70], [53.06, 14.28]]
    },
    {
        "id": "pipe_druzhba_south",
        "name": "Druzhba South Spur (Ukraine-Slovakia)",
        "company": "UkrTransNafta",
        "type": "Transnational",
        "fuel": "Urals Crude Oil",
        "capacity": "600,000 bpd",
        "length": "1,200 km",
        "diameter": "28 inch",
        "status": "In Service / Commissioned",
        "coords": [[52.05, 29.25], [50.08, 25.14], [48.62, 22.30], [48.14, 17.10], [47.50, 19.05]]
    },
    {
        "id": "pipe_espo",
        "name": "Eastern Siberia-Pacific Ocean (ESPO)",
        "company": "Transneft / CNPC",
        "type": "Transnational Trans-Asian",
        "fuel": "ESPO Blend Crude",
        "capacity": "1,600,000 bpd",
        "length": "4,857 km (3,018 mi)",
        "diameter": "42-48 inch",
        "status": "In Service / Commissioned",
        "coords": [[55.93, 98.01], [56.28, 101.61], [58.60, 125.40], [53.98, 123.95], [42.73, 133.02]]
    },
    {
        "id": "pipe_btc",
        "name": "Baku-Tbilisi-Ceyhan (BTC) Pipeline",
        "company": "BP / SOCAR Consortium",
        "type": "Transnational Strategic Choke Bypass",
        "fuel": "Azeri Light Crude",
        "capacity": "1,200,000 bpd",
        "length": "1,768 km (1,099 mi)",
        "diameter": "42-46 inch",
        "status": "In Service / Commissioned",
        "coords": [[40.18, 49.46], [41.71, 44.82], [41.00, 42.00], [39.00, 38.00], [36.88, 35.92]]
    },
    {
        "id": "pipe_petroline",
        "name": "East-West Petroline (Saudi Arabia)",
        "company": "Saudi Aramco",
        "type": "Domestic Strategic Hormuz Bypass",
        "fuel": "Arab Light / Arab Heavy",
        "capacity": "5,000,000 bpd (Expanded to 7.0 Mbd)",
        "length": "1,200 km (746 mi)",
        "diameter": "48-56 inch (Twin Line)",
        "status": "In Service / Commissioned",
        "coords": [[25.93, 49.67], [25.00, 46.00], [24.50, 42.00], [24.08, 38.06]]
    },
    {
        "id": "pipe_sumed",
        "name": "Suez-Mediterranean Pipeline (SUMED)",
        "company": "Arab Petroleum Pipelines Co",
        "type": "Transnational Strategic Choke Bypass",
        "fuel": "Middle Eastern Export Crudes",
        "capacity": "2,500,000 bpd",
        "length": "320 km (200 mi)",
        "diameter": "42 inch (Twin Line)",
        "status": "In Service / Commissioned",
        "coords": [[29.58, 32.33], [30.00, 31.20], [31.08, 29.62]]
    },
    {
        "id": "pipe_cpc",
        "name": "Caspian Pipeline Consortium (CPC)",
        "company": "Chevron / Transneft / KazMunayGas",
        "type": "Transnational Export Conduit",
        "fuel": "CPC Blend Light Sweet Crude",
        "capacity": "1,500,000 bpd",
        "length": "1,510 km (938 mi)",
        "diameter": "40-42 inch",
        "status": "In Service / Commissioned",
        "coords": [[46.15, 53.40], [47.11, 51.88], [46.35, 48.05], [45.03, 38.97], [44.72, 37.78]]
    },
    {
        "id": "pipe_myanmar_china",
        "name": "Myanmar-China Crude Pipeline",
        "company": "CNPC / MOGE",
        "type": "Transnational Malacca Bypass",
        "fuel": "Middle East / African Crudes",
        "capacity": "440,000 bpd",
        "length": "771 km (479 mi)",
        "diameter": "32 inch",
        "status": "In Service / Commissioned",
        "coords": [[19.42, 93.55], [21.95, 96.08], [23.99, 97.85], [25.04, 102.71]]
    },
    {
        "id": "pipe_transmed",
        "name": "Trans-Mediterranean Gas/Condensate",
        "company": "Sonatrach / Eni",
        "type": "Trans-Mediterranean Intercontinental",
        "fuel": "Algerian Gas & Condensate",
        "capacity": "1,100,000 boepd equiv",
        "length": "2,475 km",
        "diameter": "48 inch subsea",
        "status": "In Service / Commissioned",
        "coords": [[32.93, 3.27], [35.00, 7.00], [37.08, 11.03], [37.65, 12.58], [40.50, 15.00], [44.62, 11.48]]
    }
]

# ==============================================================================
# DATASET 2: NORTH AMERICAN NATURAL GAS PIPELINES (Image 12)
# ==============================================================================
GAS_PIPELINES_NAM = [
    {
        "id": "gas_copano",
        "name": "Copano Pipeline Upper Gulf Coast",
        "holding_co": "Copano Energy LLC / Kinder Morgan",
        "type": "Intrastate",
        "capacity": "1.2 Bcf/d",
        "length": "1,120 km (700 mi)",
        "status": "In Service / Flowing",
        "color": "#00e5ff", # Cyan (Intrastate)
        "coords": [[28.50, -98.30], [29.10, -97.20], [29.50, -95.80], [29.74, -95.12]]
    },
    {
        "id": "gas_transco",
        "name": "Transco Pipeline (Transcontinental Gas Pipe Line)",
        "holding_co": "Williams Companies",
        "type": "Interstate",
        "capacity": "18.7 Bcf/d (Largest US Network)",
        "length": "16,000 km system",
        "status": "In Service / Flowing",
        "color": "#f97316", # Orange (Interstate)
        "coords": [[26.00, -97.50], [29.76, -95.36], [30.45, -91.18], [33.74, -84.38], [37.50, -77.50], [40.71, -74.00]]
    },
    {
        "id": "gas_tennessee",
        "name": "Tennessee Gas Pipeline (TGP)",
        "holding_co": "Kinder Morgan",
        "type": "Interstate",
        "capacity": "13.9 Bcf/d",
        "length": "18,900 km system",
        "status": "In Service / Flowing",
        "color": "#f97316",
        "coords": [[27.80, -97.39], [30.00, -94.00], [32.30, -90.20], [36.16, -86.78], [40.44, -80.00], [42.36, -71.05]]
    },
    {
        "id": "gas_marcellus",
        "name": "Rover & Mountain Valley Supply Line",
        "holding_co": "Energy Transfer / Equitrans",
        "type": "Interstate",
        "capacity": "3.25 Bcf/d",
        "length": "1,150 km",
        "status": "In Service / Flowing",
        "color": "#f97316",
        "coords": [[39.50, -80.50], [40.50, -82.00], [41.65, -83.55], [42.33, -83.04]]
    },
    {
        "id": "gas_gulf_storage",
        "name": "Moss Bluff & Egan Underground Gas Storage",
        "holding_co": "Enbridge",
        "type": "Storage",
        "capacity": "85 Bcf Working Capacity",
        "length": "Salt Cavern Interconnect Hub",
        "status": "Active Injection/Withdrawal",
        "color": "#a855f7", # Purple (Storage)
        "coords": [[30.05, -94.75], [30.22, -92.42], [30.15, -93.25]]
    }
]

# ==============================================================================
# DATASET 3: MARITIME VESSEL BERTH VISITS (Exact Image 5 Table)
# ==============================================================================
BERTH_VISITS = [
    { "visit": "Exports", "berth": "Cabinda/Nemba", "country": "Angola", "cls": "Tanker-LR1", "qty": "79,716", "imo": "9570008", "lat": -5.55, "lon": 12.20 },
    { "visit": "Exports", "berth": "Novorossiysk Urals", "country": "Russia", "cls": "Tanker-Aframax", "qty": "96,726", "imo": "9543524", "lat": 44.72, "lon": 37.78 },
    { "visit": "Exports", "berth": "Basra Oil Terminal Jetty 1-4", "country": "Iraq", "cls": "Tanker-Suezmax", "qty": "164,572", "imo": "9290397", "lat": 29.68, "lon": 48.80 },
    { "visit": "Exports", "berth": "Djeno", "country": "Congo, Republic", "cls": "Tanker-Suezmax", "qty": "163,910", "imo": "9868168", "lat": -4.92, "lon": 11.95 },
    { "visit": "Exports", "berth": "Das Island 2", "country": "United Arab Emirates", "cls": "Tanker-VLCC", "qty": "331,884", "imo": "9926740", "lat": 25.15, "lon": 52.87 },
    { "visit": "Exports", "berth": "Punta Adaro 3", "country": "Venezuela", "cls": "Tanker-Aframax", "qty": "109,853", "imo": "9226970", "lat": 11.72, "lon": -70.22 },
    { "visit": "Imports", "berth": "Delaware City", "country": "United States of America", "cls": "Tanker-Aframax", "qty": "120,963", "imo": "9346859", "lat": 39.57, "lon": -75.59 },
    { "visit": "Imports/Exports", "berth": "Corpus Christi 4", "country": "United States of America", "cls": "Tanker-Aframax", "qty": "111,019", "imo": "9624079", "lat": 27.81, "lon": -97.39 },
    { "visit": "Imports", "berth": "Dongjiakou", "country": "China", "cls": "Tanker-Suezmax", "qty": "159,340", "imo": "9249324", "lat": 35.61, "lon": 119.78 },
    { "visit": "Exports", "berth": "Tuapse", "country": "Russia", "cls": "Tanker-Aframax", "qty": "121,170", "imo": "9437684", "lat": 44.10, "lon": 39.08 },
    { "visit": "Imports", "berth": "Punta Lucero Tanker Terminal 1", "country": "Spain", "cls": "Tanker-Suezmax", "qty": "164,052", "imo": "9457907", "lat": 43.36, "lon": -3.09 },
    { "visit": "Imports", "berth": "Chiba 1", "country": "Japan", "cls": "Tanker-VLCC", "qty": "318,216", "imo": "9327114", "lat": 35.53, "lon": 140.05 },
    { "visit": "Exports", "berth": "Gebig", "country": "Brazil", "cls": "Tanker-Suezmax", "qty": "167,576", "imo": "9453860", "lat": -23.03, "lon": -44.23 },
    { "visit": "Exports", "berth": "CPC terminal, Kazakhstan", "country": "Russia", "cls": "Tanker-Aframax", "qty": "121,168", "imo": "9416551", "lat": 44.75, "lon": 37.60 },
    { "visit": "Exports", "berth": "Corpus Christi 7", "country": "United States of America", "cls": "Tanker-Aframax", "qty": "121,657", "imo": "9453987", "lat": 27.82, "lon": -97.37 },
    { "visit": "Imports", "berth": "Huizhou 1", "country": "China", "cls": "Tanker-VLCC", "qty": "322,224", "imo": "9727039", "lat": 22.71, "lon": 114.61 },
    { "visit": "Exports", "berth": "Ust-Luga crude", "country": "Russia", "cls": "Tanker-LR2", "qty": "122,951", "imo": "9694658", "lat": 59.68, "lon": 28.40 },
    { "visit": "Exports", "berth": "Basra Oil Terminal SPM 5", "country": "Iraq", "cls": "Tanker-VLCC", "qty": "323,572", "imo": "9320831", "lat": 29.62, "lon": 48.88 },
    { "visit": "Imports", "berth": "Kagoshima 5", "country": "Japan", "cls": "Tanker-VLCC", "qty": "327,334", "imo": "9913951", "lat": 31.55, "lon": 130.55 },
    { "visit": "Exports", "berth": "Mina Al Ahmadi 5", "country": "Kuwait", "cls": "Tanker-VLCC", "qty": "318,304", "imo": "9604079", "lat": 29.07, "lon": 48.16 },
    { "visit": "Imports", "berth": "Mumbai 4", "country": "India", "cls": "Tanker-Suezmax", "qty": "164,203", "imo": "9411020", "lat": 18.95, "lon": 72.85 }
]

# ==============================================================================
# DATASET 4: MANHATTAN STREET-LEVEL HIGH-RES FDIC BRANCHES (Images 7, 9, 10)
# ==============================================================================
MANHATTAN_STREET_BRANCHES = [
    {
        "id": "man_3rd_41st",
        "name": "Third Avenue & 41st Street Branch",
        "company": "JPMorgan Chase Bank National Association",
        "lat": 40.7505,
        "lon": -73.9745,
        "dep_branch": 1214602,
        "dep_company": 2128462000,
        "assets_company": 3914143296,
        "year": 2022,
        "address": "633 3rd Ave, New York, NY 10017",
        "type": "Commercial Banking Center"
    },
    {
        "id": "man_400_broadway",
        "name": "400 Broadway Branch",
        "company": "Citibank, N.A.",
        "lat": 40.7182,
        "lon": -74.0028,
        "dep_branch": 845210,
        "dep_company": 1420500000,
        "assets_company": 2420000000,
        "year": 2022,
        "address": "400 Broadway, New York, NY 10013",
        "type": "Retail Full-Service"
    },
    {
        "id": "man_6th_ave",
        "name": "Sixth Avenue & 42nd Street Branch",
        "company": "Bank of America, National Association",
        "lat": 40.7548,
        "lon": -73.9840,
        "dep_branch": 1890400,
        "dep_company": 1950000000,
        "assets_company": 3150000000,
        "year": 2022,
        "address": "1111 Avenue of the Americas, New York, NY 10036",
        "type": "Wealth Management / Private Bank"
    },
    {
        "id": "man_wall_st",
        "name": "Wall Street Institutional Flagship",
        "company": "JPMorgan Chase Bank National Association",
        "lat": 40.7069,
        "lon": -74.0090,
        "dep_branch": 12450000,
        "dep_company": 2128462000,
        "assets_company": 3914143296,
        "year": 2022,
        "address": "23 Wall St, New York, NY 10005",
        "type": "Institutional / Treasury Hub"
    },
    {
        "id": "man_rockefeller",
        "name": "Rockefeller Center Wealth Branch",
        "company": "Wells Fargo Bank, National Association",
        "lat": 40.7587,
        "lon": -73.9787,
        "dep_branch": 1450300,
        "dep_company": 1480000000,
        "assets_company": 1940000000,
        "year": 2022,
        "address": "30 Rockefeller Plaza, New York, NY 10112",
        "type": "Wealth Management / Private Bank"
    }
]

# ==============================================================================
# DATASET 5: GREG MORTIMER EXPEDITION VESSEL & VOYAGE VECTOR (Image 8)
# ==============================================================================
GREG_MORTIMER = {
    "name": "GREG MORTIMER",
    "imo": "9834648",
    "nav_status": "Under way using engine",
    "destination": "DEVIL ISLAND",
    "eta": "03/04/2026 13:00:00 (Local Timezone)",
    "vessel_type": "Passenger / Polar Expedition",
    "current_speed": "10.5 kts",
    "current_draft": "5.2 m",
    "max_draft": "5.3 m",
    "callsign": "C6DV7",
    "flag": "Bahamas",
    "lat": -56.50,
    "lon": -65.20,
    "track": [
        [-54.80, -68.30], # Ushuaia departure
        [-55.50, -66.80],
        [-56.50, -65.20], # Current position
        [-58.20, -63.50],
        [-61.00, -60.00],
        [-63.80, -57.28]  # Devil Island, Antarctica destination
    ]
}

# ==============================================================================
# DATASET 6: WORLD EQUITY MARKETS (Images 3, 4)
# ==============================================================================
WORLD_EQUITY_DATA = [
    { "country": "United States", "code": "US", "index": "S&P 500 (SPX)", "last": "404.19", "chg": "+1.62%", "val": 1.62, "lat": 38.0, "lon": -97.0 },
    { "country": "India", "code": "IN", "index": "NIFTY 50 (NIFTY)", "last": "22,480.0", "chg": "+1.84%", "val": 1.84, "lat": 22.0, "lon": 78.0 },
    { "country": "Japan", "code": "JP", "index": "Nikkei 225 (NKY)", "last": "39,120.0", "chg": "+1.25%", "val": 1.25, "lat": 36.0, "lon": 138.0 },
    { "country": "Germany", "code": "DE", "index": "DAX Index (DAX)", "last": "17,735.0", "chg": "+0.78%", "val": 0.78, "lat": 51.0, "lon": 10.0 },
    { "country": "United Kingdom", "code": "GB", "index": "FTSE 100 (UKX)", "last": "7,911.0", "chg": "+0.45%", "val": 0.45, "lat": 54.0, "lon": -2.0 },
    { "country": "China", "code": "CN", "index": "Shanghai Composite (SHCOMP)", "last": "3,040.0", "chg": "-0.85%", "val": -0.85, "lat": 35.0, "lon": 105.0 },
    { "country": "France", "code": "FR", "index": "CAC 40 (CAC)", "last": "7,932.0", "chg": "+0.92%", "val": 0.92, "lat": 46.0, "lon": 2.0 },
    { "country": "Brazil", "code": "BR", "index": "IBOVESPA (IBOV)", "last": "129,180.0", "chg": "+1.10%", "val": 1.10, "lat": -10.0, "lon": -52.0 },
    { "country": "Saudi Arabia", "code": "SA", "index": "Tadawul All Share (TASI)", "last": "12,630.0", "chg": "+0.65%", "val": 0.65, "lat": 24.0, "lon": 45.0 },
    { "country": "South Korea", "code": "KR", "index": "KOSPI Index (KOSPI)", "last": "2,674.0", "chg": "+0.95%", "val": 0.95, "lat": 36.5, "lon": 128.0 },
    { "country": "Taiwan", "code": "TW", "index": "TWSE Index (TWSE)", "last": "19,305.0", "chg": "+1.40%", "val": 1.40, "lat": 23.7, "lon": 121.0 },
    { "country": "Canada", "code": "CA", "index": "S&P/TSX Composite (SPTSX)", "last": "21,550.0", "chg": "+0.60%", "val": 0.60, "lat": 56.0, "lon": -106.0 },
    { "country": "Australia", "code": "AU", "index": "S&P/ASX 200 (AS51)", "last": "7,745.0", "chg": "+0.35%", "val": 0.35, "lat": -25.0, "lon": 133.0 },
    { "country": "Egypt", "code": "EG", "index": "EGX 30 (EGX30)", "last": "29,400.0", "chg": "-1.85%", "val": -1.85, "lat": 26.0, "lon": 30.0 },
    { "country": "Turkey", "code": "TR", "index": "BIST 100 (XU100)", "last": "9,150.0", "chg": "-1.20%", "val": -1.20, "lat": 39.0, "lon": 35.0 }
]

# ==============================================================================
# DATASET 7: SPLC SUPPLY CHAIN ANALYSIS (Images 24, 25)
# ==============================================================================
SPLC_NETWORKS = {
    "AAPL": {
        "ticker": "AAPL US Equity",
        "name": "Apple Inc",
        "last_px": "152.352",
        "chg": "-1.478",
        "rev_quant": "29.32%",
        "cogs_quant": "171.02%",
        "capex_quant": "0.10%",
        "sga_quant": "3.78%",
        "rd_quant": "0.00%",
        "suppliers_count": 694,
        "customers_count": 391,
        "competitors_count": 2,
        "suppliers": [
            { "name": "Hon Hai Precision (Foxconn)", "rev": "57.02%", "cogs": "62.22%", "surprise": 4.2 },
            { "name": "Luxshare Precision", "rev": "74.06%", "cogs": "13.21%", "surprise": 5.8 },
            { "name": "Pegatron Corp", "rev": "54.92%", "cogs": "11.63%", "surprise": 2.1 },
            { "name": "Quanta Computer Inc", "rev": "49.60%", "cogs": "9.79%", "surprise": 3.4 },
            { "name": "Samsung Electronics (OLED)", "rev": "6.59%", "cogs": "7.30%", "surprise": -2.8 },
            { "name": "Taiwan Semiconductor (TSMC)", "rev": "26.55%", "cogs": "6.72%", "surprise": 6.1 },
            { "name": "LG Innotek Co Ltd", "rev": "74.49%", "cogs": "5.79%", "surprise": -1.4 },
            { "name": "QUALCOMM Inc", "rev": "22.29%", "cogs": "5.18%", "surprise": 1.9 },
            { "name": "GoerTek Inc", "rev": "41.31%", "cogs": "3.56%", "surprise": 3.0 },
            { "name": "LG Display Co Ltd", "rev": "35.68%", "cogs": "3.38%", "surprise": -3.2 },
            { "name": "Broadcom Inc", "rev": "20.00%", "cogs": "2.97%", "surprise": 4.5 },
            { "name": "Jabil Inc", "rev": "19.00%", "cogs": "2.85%", "surprise": 1.8 }
        ],
        "customers": [
            { "name": "AT&T Inc", "rev": "3.41%", "cogs": "15.43%" },
            { "name": "Deutsche Telekom AG", "rev": "3.41%", "cogs": "10.71%" },
            { "name": "Verizon Communications", "rev": "2.67%", "cogs": "16.49%" },
            { "name": "Telefonica SA", "rev": "1.96%", "cogs": "15.29%" },
            { "name": "Best Buy Co Inc", "rev": "1.64%", "cogs": "23.22%" },
            { "name": "China Mobile Ltd", "rev": "1.53%", "cogs": "5.69%" },
            { "name": "Vodafone Group PLC", "rev": "1.36%", "cogs": "15.16%" },
            { "name": "TD SYNNEX Corp", "rev": "1.33%", "cogs": "8.33%" },
            { "name": "T-Mobile US Inc", "rev": "1.31%", "cogs": "13.54%" },
            { "name": "Costco Wholesale Corp", "rev": "1.14%", "cogs": "1.62%" },
            { "name": "KDDI Corp", "rev": "0.76%", "cogs": "11.95%" }
        ],
        "competitors": [
            { "name": "Samsung Electronics", "segment": "Smartphones / Tablets / Ecosystem" },
            { "name": "HTC Corp", "segment": "XR / Mobile Devices" }
        ]
    },
    "LMT": {
        "ticker": "LMT US Equity",
        "name": "Lockheed Martin Corp",
        "last_px": "442.80",
        "chg": "+3.10",
        "rev_quant": "74.79%",
        "cogs_quant": "20.44%",
        "capex_quant": "7.32%",
        "sga_quant": "22.81%",
        "rd_quant": "5.91%",
        "suppliers_count": 244,
        "customers_count": 83,
        "competitors_count": 5,
        "suppliers": [
            { "name": "JBG SMITH Properties", "rev": "1.80%", "cogs": "18.42%", "surprise": 2.5 },
            { "name": "Keysight Technologies", "rev": "1.45%", "cogs": "5.91%", "surprise": 4.1 },
            { "name": "Terran Orbital Corp", "rev": "26.90%", "cogs": "5.28%", "surprise": 1.2 },
            { "name": "BAE Systems PLC", "rev": "7.41%", "cogs": "3.27%", "surprise": -0.8 },
            { "name": "Raytheon Technologies", "rev": "1.95%", "cogs": "2.44%", "surprise": -1.5 },
            { "name": "Dassault Systemes SE", "rev": "0.44%", "cogs": "1.55%", "surprise": 3.8 },
            { "name": "Aerojet Rocketdyne", "rev": "32.00%", "cogs": "1.24%", "surprise": 1.1 },
            { "name": "Airbus SE", "rev": "0.90%", "cogs": "0.92%", "surprise": -2.0 },
            { "name": "Howmet Aerospace Inc", "rev": "6.57%", "cogs": "0.69%", "surprise": 5.2 }
        ],
        "customers": [
            { "name": "United States of America (DoD)", "rev": "73.53%", "cogs": "Direct" },
            { "name": "United Kingdom Government", "rev": "0.59%", "cogs": "Direct" },
            { "name": "BAE Systems PLC", "rev": "0.39%", "cogs": "1.04%" },
            { "name": "L3Harris Technologies", "rev": "0.14%", "cogs": "0.73%" },
            { "name": "IHI Corp", "rev": "0.10%", "cogs": "1.01%" },
            { "name": "Kawasaki Heavy Industries", "rev": "0.01%", "cogs": "0.11%" }
        ],
        "competitors": [
            { "name": "Boeing Co / The", "segment": "Defense, Space & Security" },
            { "name": "General Dynamics Corp", "segment": "Combat Systems / Marine" },
            { "name": "L3Harris Technologies", "segment": "C5ISR Systems" },
            { "name": "Northrop Grumman Corp", "segment": "Aeronautics / Space Systems" },
            { "name": "Raytheon Technologies", "segment": "Missiles & Defense" }
        ]
    }
}

# ==============================================================================
# DATASET 8: FXC CURRENCY RATES MATRIX (Image 1)
# ==============================================================================
FXC_DATA = {
    "currencies": [
        { "code": "USD", "name": "US Dollar", "flag": "🇺🇸" },
        { "code": "CNY", "name": "Chinese Yuan", "flag": "🇨🇳" },
        { "code": "HKD", "name": "Hong Kong Dollar", "flag": "🇭🇰" },
        { "code": "INR", "name": "Indian Rupee", "flag": "🇮🇳" },
        { "code": "IDR", "name": "Indonesian Rupiah", "flag": "🇮🇩" },
        { "code": "MYR", "name": "Malaysian Ringgit", "flag": "🇲🇾" },
        { "code": "PHP", "name": "Philippine Peso", "flag": "🇵🇭" },
        { "code": "SGD", "name": "Singapore Dollar", "flag": "🇸🇬" },
        { "code": "KRW", "name": "South Korean Won", "flag": "🇰🇷" },
        { "code": "TWD", "name": "New Taiwan Dollar", "flag": "🇹🇼" },
        { "code": "THB", "name": "Thai Baht", "flag": "🇹🇭" }
    ],
    # 11x11 cross-rates matrix (Base currency in rows, Quote in columns)
    "rates": {
        "THB": [34.943, 5.0268, 4.4581, 0.42508, 0.00227, 7.8180, 0.63208, 25.862, 0.02660, 1.1392, 1.0000],
        "TWD": [30.673, 4.4124, 3.9132, 0.37313, 0.00199, 6.8625, 0.55483, 22.702, 0.02335, 1.0000, 0.87778],
        "KRW": [1313.6, 188.97, 167.59, 15.979, 0.08538, 293.89, 23.761, 972.21, 1.0000, 42.826, 37.592],
        "SGD": [1.3511, 0.1943, 0.1723, 0.0164, 0.00008, 0.3022, 0.0244, 1.0000, 0.00102, 0.04405, 0.03867],
        "PHP": [55.283, 7.9528, 7.0530, 0.6725, 0.00359, 12.369, 1.0000, 40.916, 0.04208, 1.8024, 1.5821],
        "MYR": [4.4696, 0.6429, 0.5702, 0.0543, 0.00029, 1.0000, 0.0808, 3.3081, 0.00340, 0.1457, 0.1279],
        "IDR": [15384.0, 2213.1, 1962.7, 187.14, 1.0000, 3441.9, 278.28, 11386.0, 11.711, 501.55, 440.25],
        "INR": [82.204, 11.826, 10.488, 1.0000, 0.00534, 18.392, 1.4870, 60.841, 0.06258, 2.6801, 2.3525],
        "HKD": [7.8382, 1.1276, 1.0000, 0.0953, 0.00050, 1.7537, 0.1417, 5.8012, 0.00596, 0.2555, 0.2243],
        "CNY": [6.9514, 1.0000, 0.8868, 0.0845, 0.00045, 1.5553, 0.1257, 5.1449, 0.00529, 0.2266, 0.1989],
        "USD": [1.0000, 0.1438, 0.1275, 0.0121, 0.00006, 0.2237, 0.0180, 0.7401, 0.00076, 0.0326, 0.0286]
    },
    # % Change on day for color mapping
    "changes": {
        "THB": [0.42, 0.15, 0.38, -0.22, 0.18, 0.65, -0.45, 0.82, -0.12, 0.54, 0.0],
        "TWD": [0.35, 0.28, 0.12, 0.44, 0.05, 0.32, -0.18, 0.45, 0.62, 0.0, -0.54],
        "KRW": [-0.65, -0.42, -0.58, -0.35, -0.80, -0.25, -0.72, -0.40, 0.0, -0.62, 0.12],
        "SGD": [0.18, 0.05, 0.15, 0.25, -0.10, 0.35, 0.08, 0.0, 0.40, -0.45, -0.82],
        "PHP": [-0.32, -0.18, -0.25, -0.40, 0.12, -0.15, 0.0, -0.08, 0.72, 0.18, 0.45],
        "MYR": [0.55, 0.40, 0.48, 0.30, 0.62, 0.0, 0.15, -0.35, 0.25, -0.32, -0.65],
        "IDR": [0.12, -0.05, 0.08, 0.15, 0.0, -0.62, -0.12, 0.10, 0.80, -0.05, -0.18],
        "INR": [0.25, 0.18, 0.22, 0.0, -0.15, -0.30, 0.40, -0.25, 0.35, -0.44, 0.22],
        "HKD": [0.02, 0.01, 0.0, -0.22, -0.08, -0.48, 0.25, -0.15, 0.58, -0.12, -0.38],
        "CNY": [-0.15, 0.0, -0.01, -0.18, 0.05, -0.40, 0.18, -0.05, 0.42, -0.28, -0.15],
        "USD": [0.0, 0.15, -0.02, -0.25, -0.12, -0.55, 0.32, -0.18, 0.65, -0.35, -0.42]
    }
}

# ==============================================================================
# DATASET 9: READ MOST READ STORIES NEWS WIRE (Images 18, 19)
# ==============================================================================
READ_NEWS_STORIES = [
    { "id": 1, "time": "11:02:18 UTC", "src": "BN", "title": "In Blacklisting Inspur, US Targets Partner Used by Intel and IBM", "lead": "The US added Chinese server maker Inspur Group to its export control list, striking at a major partner of American tech heavyweights. Commerce Department cites national security and advanced AI chips diversion." },
    { "id": 2, "time": "09:51:00 UTC", "src": "BN", "title": "Ukraine Latest: Saudi Generators Sent; Bakhmut Battles Continue", "lead": "Saudi Arabia delivered $100 million in humanitarian assistance including 135 backup power generators as heavy artillery exchanges continue along eastern logistics corridors." },
    { "id": 3, "time": "10:25:00 UTC", "src": "BN", "title": "Italy's CDP, Macquarie Said Set For Telecom Italia Grid Offer", "lead": "Italian state lender CDP and Australian asset manager Macquarie are finalizing a multi-billion-euro non-binding bid to rival KKR for Telecom Italia's nationwide landline broadband infrastructure." },
    { "id": 4, "time": "03/03", "src": "BN", "title": "SoftBank's Son to Join Modi at Oyo Founder's Wedding Gala", "lead": "Masayoshi Son makes a high-profile visit to New Delhi as Indian tech investments rebound and Oyo plans a revamped public listing timeline for institutional investors." },
    { "id": 5, "time": "03/02", "src": "BN", "title": "FBI Documents Show DiCaprio, Kardashian Grilled for 1MDB Secrets", "lead": "Newly released federal law enforcement files detail extensive depositions of Hollywood celebrities regarding multi-million-dollar party gifts and film financing tied to Malaysian financier Jho Low." },
    { "id": 6, "time": "03/03", "src": "BN", "title": "Altimeter Partner Chris Conforti to Leave the Investment Firm", "lead": "Key technology venture and hedge fund partner departs Brad Gerstner's Altimeter Capital after spearheading major cloud and enterprise software allocation strategies." },
    { "id": 7, "time": "03/03", "src": "BN", "title": "EU Seeks Trade Deal With US Next Week to Unlock EV Benefits", "lead": "European Commission President Ursula von der Leyen travels to Washington to negotiate battery critical minerals exemptions under the US Inflation Reduction Act tax credits." },
    { "id": 8, "time": "05:54:00 UTC", "src": "BN", "title": "Iran Says Questions About Suspected Enriched Uranium Resolved", "lead": "Atomic energy agency chief Rafael Grossi visits Tehran as IAEA inspectors seek monitoring guarantees on near-weapons-grade 83.7% uranium particles detected at Fordow." },
    { "id": 9, "time": "08:00:00 UTC", "src": "BBO", "title": "This Supreme Court Case Could Redefine Crime: Stephen L. Carter", "lead": "Bloomberg Opinion analysis on federal wire fraud and honest services doctrines being tested in public corruption challenges before the high court justices." },
    { "id": 10, "time": "03/03", "src": "BN", "title": "Warren Urges DOJ Review of Thoma Bravo Rental Software Unit", "lead": "Senator Elizabeth Warren calls on federal antitrust regulators to investigate RealPage algorithmic pricing algorithms used by institutional multifamily landlords." },
    { "id": 11, "time": "08:00:00 UTC", "src": "BBO", "title": "Fox News Is Trapped by Its Own Zealotry: Francis Wilkinson", "lead": "Dominion Voting Systems defamation disclosures reveal internal editorial conflicts between prime-time viewership demands and factual reporting boundaries." },
    { "id": 12, "time": "03/03", "src": "BN", "title": "Stability AI Is Said to Seek Funds at $4 Billion Value", "lead": "The London-based generative AI startup behind Stable Diffusion seeks new capital backing from venture funds as competition with OpenAI and Midjourney escalates." },
    { "id": 13, "time": "03/03", "src": "BN", "title": "Retailers Fear High-Flying US Consumers Are Sinking", "lead": "Target, Walmart, and Nordstrom commentary warns of spending retrenchment away from discretionary apparel toward grocery staples as excess pandemic savings dwindle." },
    { "id": 14, "time": "03/03", "src": "BN", "title": "Summers Urges Powell to Open Door to 50 Basis Points in March", "lead": "Former Treasury Secretary Lawrence Summers argues hot inflation prints and strong payroll additions mean Federal Reserve officials should keep half-point rate hikes on the table." },
    { "id": 15, "time": "03/03", "src": "BN", "title": "China E-Commerce Giant JD Set for $1.4 Billion Discount Spree", "lead": "JD.com launches aggressive consumer subsidy campaign to counter PDD Holdings' Temu and Pinduoduo in lower-tier Chinese urban retail consumption markets." },
    { "id": 16, "time": "03/03", "src": "BBO", "title": "Bridgewater Overhaul Explains Hedge Fund Reality: Aaron Brown", "lead": "Ray Dalio's succession transition and strategy realignment reflect how multi-asset macro risk parity funds navigate higher interest rates and bond-equity correlation shifts." }
]

print("Datasets configured successfully:")
print(f" - Crude Pipelines: {len(CRUDE_PIPELINES)}")
print(f" - Gas Pipelines: {len(GAS_PIPELINES_NAM)}")
print(f" - Berth Visits: {len(BERTH_VISITS)}")
print(f" - Manhattan Branches: {len(MANHATTAN_STREET_BRANCHES)}")
print(f" - World Equity Countries: {len(WORLD_EQUITY_DATA)}")
print(f" - SPLC Networks: {list(SPLC_NETWORKS.keys())}")
print(f" - FXC Currencies: {len(FXC_DATA['currencies'])}")
print(f" - Read News Stories: {len(READ_NEWS_STORIES)}")

