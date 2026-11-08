import json
import os
import re

curr_dir = r"F:\documents\SOIC\EconAgent_Platform\platform_ui"

# Load Damodaran 94 industries
with open(os.path.join(curr_dir, 'damodaran_94_global_industries.json'), 'r', encoding='utf-8') as f:
    damo_data = json.load(f)

# Group industries by GICS Sector
damo_by_sector = {}
for d in damo_data:
    sec = d['sector']
    if sec not in damo_by_sector:
        damo_by_sector[sec] = []
    damo_by_sector[sec].append({
        'name': d['name'],
        'beta': d['beta'],
        'wacc': d['waccPct'],
        'ebitMargin': d['ebitMarginPct'],
        'evEbitda': d['evEbitda']
    })

# Curated global companies by country
COMPANIES_BY_COUNTRY = {
    'us': [
        {'key': 'nvda', 'name': 'Nvidia Corp [NVDA:US]', 'ticker': 'NVDA', 'industry': 'Semiconductor', 'sector': 'Information Technology', 'nano': 'TSMC N4P Foundry & Blackwell GB200 Cluster'},
        {'key': 'aapl', 'name': 'Apple Inc [AAPL:US]', 'ticker': 'AAPL', 'industry': 'Computers/Peripherals', 'sector': 'Information Technology', 'nano': 'Cupertino Apple Park & A18 Pro Bionic Fab'},
        {'key': 'msft', 'name': 'Microsoft Corp [MSFT:US]', 'ticker': 'MSFT', 'industry': 'Software (System & Application)', 'sector': 'Information Technology', 'nano': 'Azure Hyperscale Data Center & OpenAI Supercluster'},
        {'key': 'googl', 'name': 'Alphabet Inc [GOOGL:US]', 'ticker': 'GOOGL', 'industry': 'Information Services', 'sector': 'Communication Services', 'nano': 'Googleplex & Gemini TPU v5e Supercluster'},
        {'key': 'amzn', 'name': 'Amazon.com Inc [AMZN:US]', 'ticker': 'AMZN', 'industry': 'Retail (Online)', 'sector': 'Consumer Discretionary', 'nano': 'AWS US-East Ashburn Cloud Hub & Logistics Robotics'},
        {'key': 'jpm', 'name': 'JPMorgan Chase & Co [JPM:US]', 'ticker': 'JPM', 'industry': 'Bank (Money Center)', 'sector': 'Financials', 'nano': '270 Park Ave Global HQ & Fixed Income Algo Desk'},
        {'key': 'xom', 'name': 'ExxonMobil Corp [XOM:US]', 'ticker': 'XOM', 'industry': 'Oil/Gas (Integrated)', 'sector': 'Energy', 'nano': 'Baytown Mega Refinery & Permian Basin Drilling Rig'},
        {'key': 'blk', 'name': 'BlackRock Inc [BLK:US]', 'ticker': 'BLK', 'industry': 'Investments & Asset Management', 'sector': 'Financials', 'nano': 'Aladdin Enterprise SaaS Engine & $11.5T Risk Desk'},
        {'key': 'tsla', 'name': 'Tesla Inc [TSLA:US]', 'ticker': 'TSLA', 'industry': 'Auto & Truck', 'sector': 'Consumer Discretionary', 'nano': 'Austin Giga Texas 4680 Battery & Dojo FSD Compute'},
        {'key': 'lly', 'name': 'Eli Lilly & Co [LLY:US]', 'ticker': 'LLY', 'industry': 'Drugs (Pharmaceutical)', 'sector': 'Health Care', 'nano': 'Research Triangle Biomanufacturing Facility (Mounjaro)'},
        {'key': 'lmt', 'name': 'Lockheed Martin Corp [LMT:US]', 'ticker': 'LMT', 'industry': 'Aerospace/Defense', 'sector': 'Industrials', 'nano': 'Fort Worth Skunk Works & F-35 Lightning Production'},
        {'key': 'nee', 'name': 'NextEra Energy [NEE:US]', 'ticker': 'NEE', 'industry': 'Green & Renewable Energy', 'sector': 'Utilities', 'nano': 'Florida Solar & Storage Energy Center (FPL Grid)'}
    ],
    'tw': [
        {'key': 'tsm', 'name': 'Taiwan Semiconductor Mfg [TSM:US / 2330:TW]', 'ticker': 'TSM', 'industry': 'Semiconductor', 'sector': 'Information Technology', 'nano': 'Hsinchu Science Park Fab 20 (2nm Gate-All-Around GAA)'}
    ],
    'nl': [
        {'key': 'asml', 'name': 'ASML Holding NV [ASML:US / ASML:NA]', 'ticker': 'ASML', 'industry': 'Semiconductor Equip', 'sector': 'Information Technology', 'nano': 'Veldhoven High-NA EUV (0.55 NA) Lithography Cleanroom'}
    ],
    'sa': [
        {'key': 'aramco', 'name': 'Saudi Aramco [2222:SR]', 'ticker': 'ARAMCO', 'industry': 'Oil/Gas (Integrated)', 'sector': 'Energy', 'nano': 'Abqaiq World Largest Crude Processing Facility (7M bpd)'},
        {'key': 'sabic', 'name': 'SABIC [2010:SR]', 'ticker': 'SABIC', 'industry': 'Chemical (Specialty)', 'sector': 'Materials', 'nano': 'Jubail Industrial City Petrochemical Cracker Complex'}
    ],
    'de': [
        {'key': 'sap', 'name': 'SAP SE [SAP:GY]', 'ticker': 'SAP', 'industry': 'Software (System & Application)', 'sector': 'Information Technology', 'nano': 'Walldorf Enterprise Cloud ERP Development Center'},
        {'key': 'sie', 'name': 'Siemens AG [SIE:GY]', 'ticker': 'SIE', 'industry': 'Electrical Equipment', 'sector': 'Industrials', 'nano': 'Amberg Electronic Works Digital Twin Smart Factory'}
    ],
    'jp': [
        {'key': 'toyota', 'name': 'Toyota Motor Corp [7203:JP / TM:US]', 'ticker': 'TM', 'industry': 'Auto & Truck', 'sector': 'Consumer Discretionary', 'nano': 'Motomachi Plant Solid-State Battery & Lean Production'},
        {'key': 'tel', 'name': 'Tokyo Electron Ltd [8035:JP]', 'ticker': '8035', 'industry': 'Semiconductor Equip', 'sector': 'Information Technology', 'nano': 'Yamanashi Plasma Etch & Atomic Layer Deposition Hub'}
    ],
    'kr': [
        {'key': 'samsung', 'name': 'Samsung Electronics [005930:KS]', 'ticker': 'SAMSUNG', 'industry': 'Semiconductor', 'sector': 'Information Technology', 'nano': 'Pyeongtaek Campus Line 4 V-NAND & HBM3e Memory Fab'}
    ],
    'cn': [
        {'key': 'tencent', 'name': 'Tencent Holdings [0700:HK]', 'ticker': '0700', 'industry': 'Software (Internet)', 'sector': 'Communication Services', 'nano': 'Shenzhen Tencent Binhai Mansion & Cloud AI Cluster'},
        {'key': 'baba', 'name': 'Alibaba Group [BABA:US / 9988:HK]', 'ticker': 'BABA', 'industry': 'Retail (Online)', 'sector': 'Consumer Discretionary', 'nano': 'Hangzhou Cloud Data Center & Cainiao Smart Logistics'},
        {'key': 'byd', 'name': 'BYD Co Ltd [1211:HK / 002594:SZ]', 'ticker': '1211', 'industry': 'Auto & Truck', 'sector': 'Consumer Discretionary', 'nano': 'Shenzhen Mega Blade Battery & FinDreams EV Assembly'}
    ],
    'uk': [
        {'key': 'shel', 'name': 'Shell plc [SHEL:LN]', 'ticker': 'SHEL', 'industry': 'Oil/Gas (Integrated)', 'sector': 'Energy', 'nano': 'Pernis Mega Refinery & Prelude Floating LNG Facility'}
    ],
    'fr': [
        {'key': 'lvmh', 'name': 'LVMH Moët Hennessy [MC:FP]', 'ticker': 'MC', 'industry': 'Apparel', 'sector': 'Consumer Discretionary', 'nano': 'Asnières-sur-Seine Louis Vuitton Historic Trunk Workshop'},
        {'key': 'tte', 'name': 'TotalEnergies SE [TTE:FP]', 'ticker': 'TTE', 'industry': 'Oil/Gas (Integrated)', 'sector': 'Energy', 'nano': 'Antwerp Integrated Petrochemical Platform & LNG Export'}
    ],
    'ch': [
        {'key': 'roche', 'name': 'Roche Holding AG [ROG:SW]', 'ticker': 'ROG', 'industry': 'Drugs (Pharmaceutical)', 'sector': 'Health Care', 'nano': 'Basel Global Diagnostics & Biotechnology Research Campus'}
    ],
    'au': [
        {'key': 'bhp', 'name': 'BHP Group Ltd [BHP:AU]', 'ticker': 'BHP', 'industry': 'Metals & Mining', 'sector': 'Materials', 'nano': 'Western Australia Iron Ore (WAIO) Automated Railway & Port Hedland'}
    ],
    'in': [
        {'key': 'polycab', 'name': 'Polycab India Ltd [POLYCAB:IN]', 'ticker': 'POLYCAB', 'industry': 'Electrical Equipment', 'sector': 'Industrials', 'nano': 'Polycab Halol Mega Manufacturing Complex (Gujarat)'},
        {'key': 'kei', 'name': 'KEI Industries Ltd [KEI:IN]', 'ticker': 'KEI', 'industry': 'Electrical Equipment', 'sector': 'Industrials', 'nano': 'Chinchpada Extra High Voltage (EHV) Power Cable Plant'},
        {'key': 'apl_apollo', 'name': 'APL Apollo Tubes Ltd [APLAPOLLO:IN]', 'ticker': 'APLAPOLLO', 'industry': 'Steel', 'sector': 'Materials', 'nano': 'Raipur 400x400 Heavy Structural Steel Tube Mill'},
        {'key': 'pidilite', 'name': 'Pidilite Industries [PIDILITIND:IN]', 'ticker': 'PIDILITE', 'industry': 'Chemical (Specialty)', 'sector': 'Materials', 'nano': 'Vapi Synthetic Resin & Fevicol Adhesive Polymer Plant'},
        {'key': 'narayana', 'name': 'Narayana Hrudayalaya [NH:IN]', 'ticker': 'NARAYANA', 'industry': 'Hospitals/Healthcare Facilities', 'sector': 'Health Care', 'nano': 'Bangalore Health City 1000-Bed Cardiac Unit Economics'},
        {'key': 'hdfc_bank', 'name': 'HDFC Bank Ltd [HDFCBANK:IN]', 'ticker': 'HDFCBANK', 'industry': 'Bank (Money Center)', 'sector': 'Financials', 'nano': 'Mumbai Senapati Bapat Marg Central Processing Center'},
        {'key': 'reliance', 'name': 'Reliance Industries Ltd [RELIANCE:IN]', 'ticker': 'RELIANCE', 'industry': 'Oil/Gas (Integrated)', 'sector': 'Energy', 'nano': 'Jamnagar 1.24M bpd Export Refinery Complex & Jio 5G Hub'},
        {'key': 'tcs', 'name': 'Tata Consultancy Services [TCS:IN]', 'ticker': 'TCS', 'industry': 'Computer Services', 'sector': 'Information Technology', 'nano': 'TCS Banyan Park Global Delivery Center & BaNCS Engine'}
    ]
}

# Add 'all' constellation
all_companies = []
for c_list in COMPANIES_BY_COUNTRY.values():
    for comp in c_list:
        if comp not in all_companies:
            all_companies.append(comp)
COMPANIES_BY_COUNTRY['all'] = all_companies

print(f"Prepared COMPANIES_BY_COUNTRY for {len(COMPANIES_BY_COUNTRY)} country keys.")
print(f"Total companies in 'all': {len(all_companies)}")

# Now generate the JS script string that will replace the synchronization block in generate_dashboard.py
damo_json_js = json.dumps(damo_by_sector, ensure_ascii=False)
comps_json_js = json.dumps(COMPANIES_BY_COUNTRY, ensure_ascii=False)

js_replacement = f"""// ── UNIVERSAL GLOBAL DROPDOWN MASTER SYNCHRONIZATION ──
window.GLOBAL_DAMODARAN_SECTORS = {damo_json_js};
window.GLOBAL_COMPANIES_BY_COUNTRY = {comps_json_js};

function populateGlobalDropdowns(countryKey, sectorKey) {{
  var cKey = countryKey || 'in';
  var secSelect = document.getElementById('global_sector_select');
  var firmSelect = document.getElementById('global_firm_select');
  var nanoSelect = document.getElementById('global_nano_select');
  
  // 1. Populate Sectors based on selected country
  if (secSelect) {{
    var currSecVal = sectorKey || secSelect.value;
    secSelect.innerHTML = '';
    
    // Group all 94 Damodaran industries
    Object.keys(window.GLOBAL_DAMODARAN_SECTORS).forEach(function(secGroup) {{
      var optGroup = document.createElement('optgroup');
      optGroup.label = '── ' + secGroup.toUpperCase() + ' ──';
      
      var inds = window.GLOBAL_DAMODARAN_SECTORS[secGroup];
      inds.forEach(function(ind) {{
        var opt = document.createElement('option');
        opt.value = ind.name;
        opt.textContent = ind.name + ' (Beta ' + ind.beta.toFixed(2) + ' · WACC ' + ind.wacc.toFixed(1) + '% · Margin ' + ind.ebitMargin.toFixed(1) + '%)';
        optGroup.appendChild(opt);
      }});
      secSelect.appendChild(optGroup);
    }});

    // Default sector selection based on country
    if (currSecVal && Array.from(secSelect.options).some(function(o) {{ return o.value === currSecVal; }})) {{
      secSelect.value = currSecVal;
    }} else if (cKey === 'us') {{
      secSelect.value = 'Semiconductor';
    }} else if (cKey === 'sa') {{
      secSelect.value = 'Oil/Gas (Integrated)';
    }} else if (cKey === 'tw' || cKey === 'kr') {{
      secSelect.value = 'Semiconductor';
    }} else if (cKey === 'nl') {{
      secSelect.value = 'Semiconductor Equip';
    }} else if (cKey === 'in') {{
      secSelect.value = 'Electrical Equipment';
    }} else if (secSelect.options.length > 0) {{
      secSelect.selectedIndex = 0;
    }}
  }}

  // 2. Populate Companies for this country and sector
  populateCompaniesForCountryAndSector(cKey, secSelect ? secSelect.value : null);
}}

function populateCompaniesForCountryAndSector(countryKey, selectedSector) {{
  var firmSelect = document.getElementById('global_firm_select');
  if (!firmSelect) return;
  
  var cKey = countryKey || document.getElementById('global_country_select').value || 'in';
  var compList = window.GLOBAL_COMPANIES_BY_COUNTRY[cKey] || window.GLOBAL_COMPANIES_BY_COUNTRY['all'];
  
  firmSelect.innerHTML = '';
  var activeFirm = null;

  // Filter firms matching selectedSector if any, or list all country firms
  var matchingFirms = compList.filter(function(f) {{
    return !selectedSector || f.industry === selectedSector || f.sector === selectedSector;
  }});

  // Fallback to all country firms if none match sector exactly
  var displayFirms = matchingFirms.length > 0 ? matchingFirms : compList;

  displayFirms.forEach(function(f) {{
    var opt = document.createElement('option');
    opt.value = f.key;
    opt.textContent = f.name + ' · ' + f.industry;
    firmSelect.appendChild(opt);
  }});

  if (displayFirms.length > 0) {{
    firmSelect.selectedIndex = 0;
    activeFirm = displayFirms[0];
    updateNanoAsset(activeFirm);
    syncGlobalFirmChange(activeFirm.key);
  }}
}}

function updateNanoAsset(firmObj) {{
  var nanoSelect = document.getElementById('global_nano_select');
  if (!nanoSelect || !firmObj) return;
  nanoSelect.innerHTML = '';
  
  var opt1 = document.createElement('option');
  opt1.value = 'primary_hub';
  opt1.textContent = '🏭 ' + firmObj.nano;
  nanoSelect.appendChild(opt1);

  var opt2 = document.createElement('option');
  opt2.value = 'dom';
  opt2.textContent = '📊 Level 2 Order Book & Real-Time Flow Telemetry';
  nanoSelect.appendChild(opt2);
}}

function syncGlobalCountryChange(countryKey) {{
  populateGlobalDropdowns(countryKey, null);
  
  // Fly BMAP / Cesium 3D camera to country hub
  var geoCoords = {{
    'us': [38.5, -96.5, 4.5],
    'in': [20.5, 78.9, 5.0],
    'tw': [24.8, 121.0, 7.5],
    'nl': [52.1, 5.4, 7.0],
    'sa': [26.4, 56.2, 5.5],
    'de': [51.1, 10.4, 6.0],
    'jp': [36.2, 138.2, 5.5],
    'kr': [35.9, 127.7, 6.5],
    'cn': [35.8, 104.1, 4.5],
    'uk': [55.3, -3.4, 5.5],
    'fr': [46.2, 2.2, 5.5],
    'ch': [46.8, 8.2, 7.0],
    'au': [-25.2, 133.7, 4.0],
    'all': [20.0, 0.0, 2.0]
  }};

  var coords = geoCoords[countryKey];
  if (coords && window.leafletMap) {{
    window.leafletMap.flyTo([coords[0], coords[1]], coords[2], {{ duration: 1.2 }});
  }}
  if (coords && window.nativeCesiumViewer && typeof window.flyCesiumTo === 'function') {{
    if (countryKey === 'us') window.flyCesiumTo('namerica');
    else if (countryKey === 'sa') window.flyCesiumTo('hormuz');
    else if (countryKey === 'all') window.flyCesiumTo('global');
  }}
}}

function syncGlobalSectorChange(sectorKey) {{
  var cKey = document.getElementById('global_country_select') ? document.getElementById('global_country_select').value : 'in';
  populateCompaniesForCountryAndSector(cKey, sectorKey);
}}

function syncGlobalFirmChange(firmKey) {{
  var norm = (firmKey || 'polycab').toLowerCase();

  // 1. Fractal Zoom Tier sync
  if (typeof window.onFirmDropdownChange === 'function') {{
    window.onFirmDropdownChange(norm);
  }}

  // 2. Real-Time Technicals Cockpit sync
  var techMap = {{
    'polycab': 'POLYCAB',
    'kei': 'KEI',
    'apl_apollo': 'APLAPOLLO',
    'pidilite': 'PIDILITE',
    'narayana': 'NARAYANA',
    'max_health': 'NARAYANA',
    'hdfc_bank': 'HDFCBANK',
    'reliance': 'RELIANCE',
    'tcs': 'TCS',
    'nvda': 'NVDA',
    'nvidia': 'NVDA',
    'aapl': 'AAPL',
    'apple': 'AAPL',
    'msft': 'MSFT',
    'microsoft': 'MSFT',
    'googl': 'GOOGL',
    'alphabet': 'GOOGL',
    'amzn': 'AMZN',
    'amazon': 'AMZN',
    'jpm': 'JPM',
    'xom': 'XOM',
    'exxon': 'XOM',
    'blk': 'BLK',
    'tsla': 'TSLA',
    'tesla': 'TSLA',
    'lly': 'LLY',
    'lmt': 'LMT',
    'nee': 'NEE',
    'tsm': 'TSM',
    'asml': 'ASML',
    'aramco': 'ARAMCO',
    'sabic': 'SABIC',
    'sap': 'SAP',
    'sie': 'SIE',
    'toyota': 'TM',
    'tel': '8035',
    'samsung': 'SAMSUNG',
    'tencent': '0700',
    'baba': 'BABA',
    'byd': '1211',
    'shel': 'SHEL',
    'lvmh': 'MC',
    'tte': 'TTE',
    'roche': 'ROG',
    'bhp': 'BHP'
  }};

  var techSymbol = techMap[norm] || norm.toUpperCase();
  if (typeof window.switchTechStock === 'function') {{
    window.switchTechStock(techSymbol);
  }}

  // 3. Share Price Predictor & DCF sync
  var presetKey = norm;
  if (norm === 'apl_apollo') presetKey = 'apl';
  if (norm === 'narayana' || norm === 'max_health') presetKey = 'narayana';
  if (typeof window.loadStockPreset === 'function') {{
    window.loadStockPreset(presetKey);
  }}

  // 4. SOIC 310-pt Scorecard sync
  var soicMap = {{
    'polycab': 'Polycab India Ltd',
    'kei': 'KEI Industries',
    'apl_apollo': 'APL Apollo Tubes',
    'pidilite': 'Pidilite Industries',
    'narayana': 'NARAYANA HRU',
    'hdfc_bank': 'HDFC Bank Ltd',
    'reliance': 'Reliance Industries',
    'tcs': 'Tata Consultancy Services',
    'nvda': 'Nvidia',
    'aapl': 'Apple Inc.',
    'msft': 'Microsoft Corp',
    'googl': 'Alphabet Inc',
    'amzn': 'Amazon.com Inc',
    'tsla': 'Tesla Inc',
    'xom': 'ExxonMobil Corp',
    'jpm': 'JPMorgan Chase & Co',
    'blk': 'BlackRock Inc',
    'asml': 'ASML Holding NV',
    'aramco': 'Saudi Aramco',
    'bhp': 'BHP Group Ltd',
    'samsung': 'Samsung Electronics'
  }};
  var targetSoic = soicMap[norm] || 'Polycab India Ltd';
  if (typeof window.loadSoicStock === 'function') {{
    window.loadSoicStock(targetSoic);
  }}

  // 5. Financial Titans Level 2 DOM Order Book sync
  if (typeof window.switchTickTicker === 'function') {{
    window.switchTickTicker(techSymbol);
  }}
}}

function syncGlobalNanoChange(nanoKey) {{
  if (typeof window.onNanoDropdownChange === 'function') {{
    window.onNanoDropdownChange(nanoKey);
  }}
}}

// Initialize dropdowns on page load
document.addEventListener('DOMContentLoaded', function() {{
  populateGlobalDropdowns('in', 'Electrical Equipment');
}});"""

# Read generate_dashboard.py
with open(os.path.join(curr_dir, 'generate_dashboard.py'), 'r', encoding='utf-8') as f:
    code = f.read()

# Replace synchronization block
start_tag = "// ── UNIVERSAL GLOBAL DROPDOWN MASTER SYNCHRONIZATION ──"
end_tag = "function jumpToTabForActiveFirm(tabId)"

s_idx = code.find(start_tag)
e_idx = code.find(end_tag)

assert s_idx != -1, "start_tag not found in generate_dashboard.py"
assert e_idx != -1, "end_tag not found in generate_dashboard.py"

new_code = code[:s_idx] + js_replacement + "\n\n" + code[e_idx:]

with open(os.path.join(curr_dir, 'generate_dashboard.py'), 'w', encoding='utf-8') as f:
    f.write(new_code)

print("generate_dashboard.py updated with Global Wall Street & 94-Industry Engine!")

