import json
import os

curr_dir = r"F:\documents\SOIC\EconAgent_Platform\platform_ui"

# 1. Load Damodaran 94 industries
with open(os.path.join(curr_dir, 'damodaran_94_global_industries.json'), 'r', encoding='utf-8') as f:
    damo_data = json.load(f)

# 2. Load Curated companies
with open(os.path.join(curr_dir, 'global_top_companies_curated.json'), 'r', encoding='utf-8') as f:
    curated_comps = json.load(f)

# Build map of country key to name
COUNTRY_MAP = {
    'us': 'United States',
    'in': 'India',
    'tw': 'Taiwan',
    'nl': 'Netherlands',
    'sa': 'Saudi Arabia',
    'de': 'Germany',
    'jp': 'Japan',
    'kr': 'South Korea',
    'cn': 'China',
    'uk': 'United Kingdom',
    'fr': 'France',
    'ch': 'Switzerland',
    'br': 'Brazil',
    'au': 'Australia',
    'ae': 'United Arab Emirates',
    'ca': 'Canada',
    'all': 'Global Constellation'
}

# Major Wall Street & Global Titans explicitly mapped with tech symbols and nano assets
PREMIER_TITANS = {
    'us': [
        {'key': 'nvda', 'name': 'Nvidia Corp [NVDA:US]', 'ticker': 'NVDA', 'industry': 'Semiconductor', 'sector': 'Information Technology', 'nano': '🏭 TSMC N4P Foundry & Blackwell GB200 Cluster'},
        {'key': 'aapl', 'name': 'Apple Inc [AAPL:US]', 'ticker': 'AAPL', 'industry': 'Computers/Peripherals', 'sector': 'Information Technology', 'nano': '📱 Cupertino Apple Park & A18 Pro Bionic Fab'},
        {'key': 'msft', 'name': 'Microsoft Corp [MSFT:US]', 'ticker': 'MSFT', 'industry': 'Software (System & Application)', 'sector': 'Information Technology', 'nano': '☁️ Azure Hyperscale Data Center & OpenAI Supercluster'},
        {'key': 'googl', 'name': 'Alphabet Inc [GOOGL:US]', 'ticker': 'GOOGL', 'industry': 'Information Services', 'sector': 'Communication Services', 'nano': '🔍 Googleplex & Gemini TPU v5e Supercluster'},
        {'key': 'amzn', 'name': 'Amazon.com Inc [AMZN:US]', 'ticker': 'AMZN', 'industry': 'Retail (Online)', 'sector': 'Consumer Discretionary', 'nano': '📦 AWS US-East Ashburn Cloud Hub & Logistics Robotics'},
        {'key': 'jpm', 'name': 'JPMorgan Chase & Co [JPM:US]', 'ticker': 'JPM', 'industry': 'Bank (Money Center)', 'sector': 'Financials', 'nano': '🏛️ 270 Park Ave Global HQ & Fixed Income Algo Desk'},
        {'key': 'xom', 'name': 'ExxonMobil Corp [XOM:US]', 'ticker': 'XOM', 'industry': 'Oil/Gas (Integrated)', 'sector': 'Energy', 'nano': '🛢️ Baytown Mega Refinery & Permian Basin Drilling Rig'},
        {'key': 'blk', 'name': 'BlackRock Inc [BLK:US]', 'ticker': 'BLK', 'industry': 'Investments & Asset Management', 'sector': 'Financials', 'nano': '💻 Aladdin Enterprise SaaS Engine & $11.5T Risk Desk'},
        {'key': 'tsla', 'name': 'Tesla Inc [TSLA:US]', 'ticker': 'TSLA', 'industry': 'Auto & Truck', 'sector': 'Consumer Discretionary', 'nano': '⚡ Austin Giga Texas 4680 Battery & Dojo FSD Compute'},
        {'key': 'lly', 'name': 'Eli Lilly & Co [LLY:US]', 'ticker': 'LLY', 'industry': 'Drugs (Pharmaceutical)', 'sector': 'Health Care', 'nano': '💊 Research Triangle Biomanufacturing Facility (Mounjaro)'},
        {'key': 'lmt', 'name': 'Lockheed Martin Corp [LMT:US]', 'ticker': 'LMT', 'industry': 'Aerospace/Defense', 'sector': 'Industrials', 'nano': '✈️ Fort Worth Skunk Works & F-35 Lightning Production'},
        {'key': 'nee', 'name': 'NextEra Energy [NEE:US]', 'ticker': 'NEE', 'industry': 'Green & Renewable Energy', 'sector': 'Utilities', 'nano': '☀️ Florida Solar & Storage Energy Center (FPL Grid)'}
    ],
    'tw': [
        {'key': 'tsm', 'name': 'Taiwan Semiconductor Mfg [TSM:US / 2330:TW]', 'ticker': 'TSM', 'industry': 'Semiconductor', 'sector': 'Information Technology', 'nano': '🔬 Hsinchu Science Park Fab 20 (2nm Gate-All-Around GAA)'}
    ],
    'nl': [
        {'key': 'asml', 'name': 'ASML Holding NV [ASML:US / ASML:NA]', 'ticker': 'ASML', 'industry': 'Semiconductor Equip', 'sector': 'Information Technology', 'nano': '💡 Veldhoven High-NA EUV (0.55 NA) Lithography Cleanroom'}
    ],
    'sa': [
        {'key': 'aramco', 'name': 'Saudi Aramco [2222:SR]', 'ticker': 'ARAMCO', 'industry': 'Oil/Gas (Integrated)', 'sector': 'Energy', 'nano': '🛢️ Abqaiq World Largest Crude Processing Facility (7M bpd)'},
        {'key': 'sabic', 'name': 'SABIC [2010:SR]', 'ticker': 'SABIC', 'industry': 'Chemical (Specialty)', 'sector': 'Materials', 'nano': '⚗️ Jubail Industrial City Petrochemical Cracker Complex'}
    ],
    'de': [
        {'key': 'sap', 'name': 'SAP SE [SAP:GY]', 'ticker': 'SAP', 'industry': 'Software (System & Application)', 'sector': 'Information Technology', 'nano': '💻 Walldorf Enterprise Cloud ERP Development Center'},
        {'key': 'sie', 'name': 'Siemens AG [SIE:GY]', 'ticker': 'SIE', 'industry': 'Electrical Equipment', 'sector': 'Industrials', 'nano': '⚙️ Amberg Electronic Works Digital Twin Smart Factory'}
    ],
    'jp': [
        {'key': 'toyota', 'name': 'Toyota Motor Corp [7203:JP / TM:US]', 'ticker': 'TM', 'industry': 'Auto & Truck', 'sector': 'Consumer Discretionary', 'nano': '🚗 Motomachi Plant Solid-State Battery & Lean Production'},
        {'key': 'tel', 'name': 'Tokyo Electron Ltd [8035:JP]', 'ticker': '8035', 'industry': 'Semiconductor Equip', 'sector': 'Information Technology', 'nano': '🔬 Yamanashi Plasma Etch & Atomic Layer Deposition Hub'}
    ],
    'kr': [
        {'key': 'samsung', 'name': 'Samsung Electronics [005930:KS]', 'ticker': 'SAMSUNG', 'industry': 'Semiconductor', 'sector': 'Information Technology', 'nano': '💾 Pyeongtaek Campus Line 4 V-NAND & HBM3e Memory Fab'}
    ],
    'cn': [
        {'key': 'tencent', 'name': 'Tencent Holdings [0700:HK]', 'ticker': '0700', 'industry': 'Software (Internet)', 'sector': 'Communication Services', 'nano': '🌐 Shenzhen Tencent Binhai Mansion & Cloud AI Cluster'},
        {'key': 'baba', 'name': 'Alibaba Group [BABA:US / 9988:HK]', 'ticker': 'BABA', 'industry': 'Retail (Online)', 'sector': 'Consumer Discretionary', 'nano': '☁️ Hangzhou Cloud Data Center & Cainiao Smart Logistics'},
        {'key': 'byd', 'name': 'BYD Co Ltd [1211:HK / 002594:SZ]', 'ticker': '1211', 'industry': 'Auto & Truck', 'sector': 'Consumer Discretionary', 'nano': '🔋 Shenzhen Mega Blade Battery & FinDreams EV Assembly'}
    ],
    'in': [
        {'key': 'polycab', 'name': 'Polycab India Ltd [POLYCAB:IN]', 'ticker': 'POLYCAB', 'industry': 'Electrical Equipment', 'sector': 'Industrials', 'nano': '🏭 Polycab Halol Mega Manufacturing Complex (Gujarat)'},
        {'key': 'kei', 'name': 'KEI Industries Ltd [KEI:IN]', 'ticker': 'KEI', 'industry': 'Electrical Equipment', 'sector': 'Industrials', 'nano': '⚡ Chinchpada Extra High Voltage (EHV) Power Cable Plant'},
        {'key': 'apl_apollo', 'name': 'APL Apollo Tubes Ltd [APLAPOLLO:IN]', 'ticker': 'APLAPOLLO', 'industry': 'Steel', 'sector': 'Materials', 'nano': '🏗️ Raipur 400x400 Heavy Structural Steel Tube Mill'},
        {'key': 'pidilite', 'name': 'Pidilite Industries [PIDILITIND:IN]', 'ticker': 'PIDILITE', 'industry': 'Chemical (Specialty)', 'sector': 'Materials', 'nano': '🧪 Vapi Synthetic Resin & Fevicol Adhesive Polymer Plant'},
        {'key': 'narayana', 'name': 'Narayana Hrudayalaya [NH:IN]', 'ticker': 'NARAYANA', 'industry': 'Hospitals/Healthcare Facilities', 'sector': 'Health Care', 'nano': '🏥 Bangalore Health City 1000-Bed Cardiac Unit Economics'},
        {'key': 'hdfc_bank', 'name': 'HDFC Bank Ltd [HDFCBANK:IN]', 'ticker': 'HDFCBANK', 'industry': 'Bank (Money Center)', 'sector': 'Financials', 'nano': '🏦 Mumbai Senapati Bapat Marg Central Processing Center'},
        {'key': 'reliance', 'name': 'Reliance Industries Ltd [RELIANCE:IN]', 'ticker': 'RELIANCE', 'industry': 'Oil/Gas (Integrated)', 'sector': 'Energy', 'nano': '🛢️ Jamnagar 1.24M bpd Export Refinery Complex & Jio 5G Hub'},
        {'key': 'tcs', 'name': 'Tata Consultancy Services [TCS:IN]', 'ticker': 'TCS', 'industry': 'Computer Services', 'sector': 'Information Technology', 'nano': '💻 TCS Banyan Park Global Delivery Center & BaNCS Engine'}
    ]
}

print("Built premier titans for", list(PREMIER_TITANS.keys()))

