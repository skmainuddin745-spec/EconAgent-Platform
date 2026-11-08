
global.window = global;
global.document = {
  getElementById: () => ({ options: [], appendChild: () => {}, querySelector: () => null }),
  querySelectorAll: () => [],
  addEventListener: () => {}
};

// ── Workspace Layout Switcher Engine ──
var currentWorkspaceMode = 'single';

function setWorkspaceMode(mode) {
  currentWorkspaceMode = mode;
  var vp = document.getElementById('workspace_viewport');
  var bSingle = document.getElementById('ws_btn_single');
  var bSplit = document.getElementById('ws_btn_split');
  var bGrid = document.getElementById('ws_btn_grid');
  if (!vp) return;

  [bSingle, bSplit, bGrid].forEach(b => { if (b) b.classList.remove('active'); });

  if (mode === 'single') {
    vp.classList.remove('split-mode', 'grid-mode');
    if (bSingle) bSingle.classList.add('active');
    var activeTab = document.querySelector('.tab.active');
    if (activeTab) {
      var onclickStr = activeTab.getAttribute('onclick') || '';
      var m = onclickStr.match(/'([^']+)'/g);
      if (m && m[1]) {
        var currentActiveTabId = m[1].replace(/'/g, '');
        document.querySelectorAll('.content').forEach(c => c.classList.remove('active'));
        var tc = document.getElementById(currentActiveTabId);
        if (tc) tc.classList.add('active');
      }
    }
  } else if (mode === 'split') {
    vp.classList.remove('grid-mode');
    vp.classList.add('split-mode');
    if (bSplit) bSplit.classList.add('active');
    window.dispatchEvent(new Event('resize'));
    if (typeof drawBmap === 'function') drawBmap();
    if (typeof initTickDesk === 'function') initTickDesk();
  } else if (mode === 'grid') {
    vp.classList.remove('split-mode');
    vp.classList.add('grid-mode');
    if (bGrid) bGrid.classList.add('active');
    window.dispatchEvent(new Event('resize'));
    if (typeof drawBmap === 'function') drawBmap();
    if (typeof initTickDesk === 'function') initTickDesk();
    if (typeof updateScenarioSliders === 'function') updateScenarioSliders();
  }
}


// ── UNIVERSAL GLOBAL DROPDOWN MASTER SYNCHRONIZATION ──
window.GLOBAL_DAMODARAN_SECTORS = {"Communication Services": [{"name": "Advertising", "beta": 1.27, "wacc": 9.2, "ebitMargin": 8.55, "evEbitda": 11.1}, {"name": "Broadcasting", "beta": 0.83, "wacc": 7.07, "ebitMargin": 9.97, "evEbitda": 8.5}, {"name": "Cable TV", "beta": 1.1, "wacc": 6.91, "ebitMargin": 17.34, "evEbitda": 6.6}, {"name": "Entertainment", "beta": 1.01, "wacc": 9.07, "ebitMargin": 11.64, "evEbitda": 18.7}, {"name": "Information Services", "beta": 1.02, "wacc": 8.41, "ebitMargin": 11.78, "evEbitda": 10.8}, {"name": "Software (Entertainment)", "beta": 1.25, "wacc": 10.77, "ebitMargin": 31.9, "evEbitda": 21.4}, {"name": "Telecom (Wireless)", "beta": 0.78, "wacc": 6.93, "ebitMargin": 15.83, "evEbitda": 8.4}, {"name": "Telecom. Services", "beta": 0.73, "wacc": 6.48, "ebitMargin": 16.09, "evEbitda": 7.1}], "Industrials": [{"name": "Aerospace/Defense", "beta": 1.23, "wacc": 10.14, "ebitMargin": 9.18, "evEbitda": 22.4}, {"name": "Air Transport", "beta": 0.99, "wacc": 7.23, "ebitMargin": 8.21, "evEbitda": 9.1}, {"name": "Building Materials", "beta": 1.0, "wacc": 8.63, "ebitMargin": 10.4, "evEbitda": 12.4}, {"name": "Business & Consumer Services", "beta": 0.99, "wacc": 8.64, "ebitMargin": 10.15, "evEbitda": 14.1}, {"name": "Construction Supplies", "beta": 1.03, "wacc": 8.51, "ebitMargin": 9.71, "evEbitda": 12.3}, {"name": "Diversified", "beta": 0.8, "wacc": 7.09, "ebitMargin": 15.11, "evEbitda": 10.9}, {"name": "Electrical Equipment", "beta": 1.37, "wacc": 10.81, "ebitMargin": 8.35, "evEbitda": 20.9}, {"name": "Engineering/Construction", "beta": 1.0, "wacc": 7.3, "ebitMargin": 5.1, "evEbitda": 11.3}, {"name": "Environmental & Waste Services", "beta": 1.1, "wacc": 8.62, "ebitMargin": 11.27, "evEbitda": 14.7}, {"name": "Machinery", "beta": 1.37, "wacc": 10.78, "ebitMargin": 10.36, "evEbitda": 16.9}, {"name": "Office Equipment & Services", "beta": 0.76, "wacc": 7.35, "ebitMargin": 7.73, "evEbitda": 9.1}, {"name": "Publishing & Newspapers", "beta": 0.82, "wacc": 7.62, "ebitMargin": 7.38, "evEbitda": 10.2}, {"name": "Shipbuilding & Marine", "beta": 0.87, "wacc": 7.53, "ebitMargin": 14.34, "evEbitda": 7.5}, {"name": "Transportation", "beta": 0.96, "wacc": 7.61, "ebitMargin": 7.21, "evEbitda": 11.2}, {"name": "Transportation (Railroads)", "beta": 0.72, "wacc": 6.74, "ebitMargin": 23.45, "evEbitda": 10.9}, {"name": "Trucking", "beta": 0.85, "wacc": 7.48, "ebitMargin": 7.45, "evEbitda": 9.6}], "Consumer Discretionary": [{"name": "Apparel", "beta": 0.76, "wacc": 7.62, "ebitMargin": 12.59, "evEbitda": 14.0}, {"name": "Auto & Truck", "beta": 1.41, "wacc": 9.48, "ebitMargin": 4.31, "evEbitda": 17.3}, {"name": "Auto Parts", "beta": 1.45, "wacc": 10.42, "ebitMargin": 5.45, "evEbitda": 9.2}, {"name": "Education", "beta": 0.81, "wacc": 7.59, "ebitMargin": 15.93, "evEbitda": 9.0}, {"name": "Electronics (Consumer & Office)", "beta": 1.2, "wacc": 9.8, "ebitMargin": 6.02, "evEbitda": 10.7}, {"name": "Furn/Home Furnishings", "beta": 0.97, "wacc": 8.36, "ebitMargin": 7.65, "evEbitda": 10.6}, {"name": "Homebuilding", "beta": 0.96, "wacc": 7.92, "ebitMargin": 10.71, "evEbitda": 9.4}, {"name": "Hotel/Gaming", "beta": 0.8, "wacc": 7.26, "ebitMargin": 16.66, "evEbitda": 13.9}, {"name": "Recreation", "beta": 1.01, "wacc": 8.29, "ebitMargin": 10.52, "evEbitda": 11.4}, {"name": "Restaurant/Dining", "beta": 0.75, "wacc": 7.4, "ebitMargin": 9.51, "evEbitda": 16.6}, {"name": "Retail (Automotive)", "beta": 0.83, "wacc": 7.15, "ebitMargin": 5.15, "evEbitda": 12.3}, {"name": "Retail (Building Supply)", "beta": 0.94, "wacc": 8.25, "ebitMargin": 10.59, "evEbitda": 13.5}, {"name": "Retail (Distributors)", "beta": 0.81, "wacc": 7.16, "ebitMargin": 4.79, "evEbitda": 14.4}, {"name": "Retail (General)", "beta": 0.98, "wacc": 8.89, "ebitMargin": 6.47, "evEbitda": 17.1}, {"name": "Retail (Special Lines)", "beta": 0.96, "wacc": 8.58, "ebitMargin": 7.41, "evEbitda": 13.1}, {"name": "Rubber& Tires", "beta": 0.94, "wacc": 7.74, "ebitMargin": 7.3, "evEbitda": 6.8}, {"name": "Shoe", "beta": 0.92, "wacc": 8.52, "ebitMargin": 8.8, "evEbitda": 14.7}], "Financials": [{"name": "Bank (Money Center)", "beta": 0.7, "wacc": 5.29, "ebitMargin": 0.38, "evEbitda": 12.5}, {"name": "Banks (Regional)", "beta": 0.51, "wacc": 4.99, "ebitMargin": -0.0, "evEbitda": 12.5}, {"name": "Brokerage & Investment Banking", "beta": 0.98, "wacc": 6.17, "ebitMargin": 0.94, "evEbitda": 12.5}, {"name": "Financial Svcs. (Non-bank & Insurance)", "beta": 0.82, "wacc": 5.49, "ebitMargin": 14.13, "evEbitda": 43.4}, {"name": "Insurance (General)", "beta": 0.51, "wacc": 6.24, "ebitMargin": 15.45, "evEbitda": 9.0}, {"name": "Insurance (Life)", "beta": 0.8, "wacc": 6.69, "ebitMargin": 17.29, "evEbitda": 7.3}, {"name": "Insurance (Prop/Cas.)", "beta": 0.43, "wacc": 6.06, "ebitMargin": 15.26, "evEbitda": 7.8}, {"name": "Investments & Asset Management", "beta": 0.75, "wacc": 6.72, "ebitMargin": 25.05, "evEbitda": 19.0}, {"name": "Reinsurance", "beta": 0.99, "wacc": 8.64, "ebitMargin": 13.32, "evEbitda": 7.9}], "Consumer Staples": [{"name": "Beverage (Alcoholic)", "beta": 0.79, "wacc": 7.72, "ebitMargin": 22.47, "evEbitda": 12.2}, {"name": "Beverage (Soft)", "beta": 0.59, "wacc": 6.82, "ebitMargin": 17.62, "evEbitda": 16.0}, {"name": "Farming/Agriculture", "beta": 0.67, "wacc": 6.46, "ebitMargin": 6.39, "evEbitda": 12.9}, {"name": "Food Processing", "beta": 0.67, "wacc": 6.82, "ebitMargin": 8.54, "evEbitda": 11.1}, {"name": "Food Wholesalers", "beta": 0.68, "wacc": 6.52, "ebitMargin": 2.54, "evEbitda": 10.4}, {"name": "Household Products", "beta": 0.83, "wacc": 8.04, "ebitMargin": 16.17, "evEbitda": 14.6}, {"name": "Retail (Grocery and Food)", "beta": 0.87, "wacc": 7.44, "ebitMargin": 3.78, "evEbitda": 10.3}, {"name": "Tobacco", "beta": 0.43, "wacc": 5.97, "ebitMargin": 32.67, "evEbitda": 12.0}], "Materials": [{"name": "Chemical (Basic)", "beta": 1.26, "wacc": 8.77, "ebitMargin": 3.68, "evEbitda": 13.7}, {"name": "Chemical (Diversified)", "beta": 1.17, "wacc": 8.31, "ebitMargin": 6.83, "evEbitda": 8.7}, {"name": "Chemical (Specialty)", "beta": 1.15, "wacc": 9.28, "ebitMargin": 10.97, "evEbitda": 13.1}, {"name": "Metals & Mining", "beta": 1.24, "wacc": 9.81, "ebitMargin": 10.73, "evEbitda": 10.7}, {"name": "Packaging & Container", "beta": 0.76, "wacc": 6.88, "ebitMargin": 7.84, "evEbitda": 9.6}, {"name": "Paper/Forest Products", "beta": 0.89, "wacc": 6.92, "ebitMargin": 4.3, "evEbitda": 10.5}, {"name": "Precious Metals", "beta": 1.4, "wacc": 11.25, "ebitMargin": 24.94, "evEbitda": 12.7}, {"name": "Steel", "beta": 1.13, "wacc": 8.38, "ebitMargin": 4.85, "evEbitda": 9.0}], "Energy": [{"name": "Coal & Related Energy", "beta": 1.14, "wacc": 9.41, "ebitMargin": 16.04, "evEbitda": 8.0}, {"name": "Oil/Gas (Integrated)", "beta": 0.69, "wacc": 7.16, "ebitMargin": 14.27, "evEbitda": 6.2}, {"name": "Oil/Gas (Production and Exploration)", "beta": 0.89, "wacc": 7.76, "ebitMargin": 28.51, "evEbitda": 4.8}, {"name": "Oilfield Svcs/Equip.", "beta": 0.95, "wacc": 7.88, "ebitMargin": 5.01, "evEbitda": 8.8}], "Information Technology": [{"name": "Computer Services", "beta": 1.12, "wacc": 9.46, "ebitMargin": 7.56, "evEbitda": 14.6}, {"name": "Computers/Peripherals", "beta": 1.49, "wacc": 11.85, "ebitMargin": 12.61, "evEbitda": 20.2}, {"name": "Electronics (General)", "beta": 1.6, "wacc": 11.88, "ebitMargin": 6.29, "evEbitda": 18.7}, {"name": "Semiconductor", "beta": 1.88, "wacc": 14.12, "ebitMargin": 26.99, "evEbitda": 27.0}, {"name": "Semiconductor Equip", "beta": 2.13, "wacc": 15.31, "ebitMargin": 20.28, "evEbitda": 25.7}, {"name": "Software (Internet)", "beta": 1.39, "wacc": 11.12, "ebitMargin": 6.17, "evEbitda": 40.6}, {"name": "Software (System & Application)", "beta": 1.35, "wacc": 11.18, "ebitMargin": 27.41, "evEbitda": 24.6}, {"name": "Telecom. Equipment", "beta": 1.33, "wacc": 10.82, "ebitMargin": 11.03, "evEbitda": 25.0}], "Health Care": [{"name": "Drugs (Biotechnology)", "beta": 1.23, "wacc": 10.24, "ebitMargin": 7.48, "evEbitda": 16.7}, {"name": "Drugs (Pharmaceutical)", "beta": 1.06, "wacc": 9.22, "ebitMargin": 23.07, "evEbitda": 13.8}, {"name": "Healthcare Products", "beta": 1.18, "wacc": 9.86, "ebitMargin": 14.27, "evEbitda": 18.5}, {"name": "Healthcare Support Services", "beta": 0.92, "wacc": 7.79, "ebitMargin": 3.1, "evEbitda": 11.3}, {"name": "Heathcare Information and Technology", "beta": 1.29, "wacc": 10.39, "ebitMargin": 14.79, "evEbitda": 21.0}, {"name": "Hospitals/Healthcare Facilities", "beta": 0.76, "wacc": 6.99, "ebitMargin": 12.27, "evEbitda": 11.9}], "Utilities": [{"name": "Green & Renewable Energy", "beta": 0.84, "wacc": 6.85, "ebitMargin": 27.72, "evEbitda": 14.2}, {"name": "Oil/Gas Distribution", "beta": 0.65, "wacc": 6.37, "ebitMargin": 17.24, "evEbitda": 11.8}, {"name": "Power", "beta": 0.71, "wacc": 6.28, "ebitMargin": 15.16, "evEbitda": 10.1}, {"name": "Utility (General)", "beta": 0.5, "wacc": 5.61, "ebitMargin": 15.22, "evEbitda": 10.8}, {"name": "Utility (Water)", "beta": 0.7, "wacc": 6.2, "ebitMargin": 26.6, "evEbitda": 11.9}], "Real Estate": [{"name": "R.E.I.T.", "beta": 0.56, "wacc": 5.77, "ebitMargin": 31.92, "evEbitda": 19.7}, {"name": "Real Estate (Development)", "beta": 0.93, "wacc": 5.98, "ebitMargin": 3.46, "evEbitda": 14.1}, {"name": "Real Estate (General/Diversified)", "beta": 0.93, "wacc": 6.89, "ebitMargin": 14.92, "evEbitda": 15.0}, {"name": "Real Estate (Operations & Services)", "beta": 0.78, "wacc": 6.53, "ebitMargin": 17.4, "evEbitda": 18.5}, {"name": "Retail (REITs)", "beta": 0.61, "wacc": 6.0, "ebitMargin": 50.02, "evEbitda": 16.8}]};
window.GLOBAL_COMPANIES_BY_COUNTRY = {"us": [{"key": "nvda", "name": "Nvidia Corp [NVDA:US]", "ticker": "NVDA", "industry": "Semiconductor", "sector": "Information Technology", "nano": "TSMC N4P Foundry & Blackwell GB200 Cluster"}, {"key": "aapl", "name": "Apple Inc [AAPL:US]", "ticker": "AAPL", "industry": "Computers/Peripherals", "sector": "Information Technology", "nano": "Cupertino Apple Park & A18 Pro Bionic Fab"}, {"key": "msft", "name": "Microsoft Corp [MSFT:US]", "ticker": "MSFT", "industry": "Software (System & Application)", "sector": "Information Technology", "nano": "Azure Hyperscale Data Center & OpenAI Supercluster"}, {"key": "googl", "name": "Alphabet Inc [GOOGL:US]", "ticker": "GOOGL", "industry": "Information Services", "sector": "Communication Services", "nano": "Googleplex & Gemini TPU v5e Supercluster"}, {"key": "amzn", "name": "Amazon.com Inc [AMZN:US]", "ticker": "AMZN", "industry": "Retail (Online)", "sector": "Consumer Discretionary", "nano": "AWS US-East Ashburn Cloud Hub & Logistics Robotics"}, {"key": "jpm", "name": "JPMorgan Chase & Co [JPM:US]", "ticker": "JPM", "industry": "Bank (Money Center)", "sector": "Financials", "nano": "270 Park Ave Global HQ & Fixed Income Algo Desk"}, {"key": "xom", "name": "ExxonMobil Corp [XOM:US]", "ticker": "XOM", "industry": "Oil/Gas (Integrated)", "sector": "Energy", "nano": "Baytown Mega Refinery & Permian Basin Drilling Rig"}, {"key": "blk", "name": "BlackRock Inc [BLK:US]", "ticker": "BLK", "industry": "Investments & Asset Management", "sector": "Financials", "nano": "Aladdin Enterprise SaaS Engine & $11.5T Risk Desk"}, {"key": "tsla", "name": "Tesla Inc [TSLA:US]", "ticker": "TSLA", "industry": "Auto & Truck", "sector": "Consumer Discretionary", "nano": "Austin Giga Texas 4680 Battery & Dojo FSD Compute"}, {"key": "lly", "name": "Eli Lilly & Co [LLY:US]", "ticker": "LLY", "industry": "Drugs (Pharmaceutical)", "sector": "Health Care", "nano": "Research Triangle Biomanufacturing Facility (Mounjaro)"}, {"key": "lmt", "name": "Lockheed Martin Corp [LMT:US]", "ticker": "LMT", "industry": "Aerospace/Defense", "sector": "Industrials", "nano": "Fort Worth Skunk Works & F-35 Lightning Production"}, {"key": "nee", "name": "NextEra Energy [NEE:US]", "ticker": "NEE", "industry": "Green & Renewable Energy", "sector": "Utilities", "nano": "Florida Solar & Storage Energy Center (FPL Grid)"}], "tw": [{"key": "tsm", "name": "Taiwan Semiconductor Mfg [TSM:US / 2330:TW]", "ticker": "TSM", "industry": "Semiconductor", "sector": "Information Technology", "nano": "Hsinchu Science Park Fab 20 (2nm Gate-All-Around GAA)"}], "nl": [{"key": "asml", "name": "ASML Holding NV [ASML:US / ASML:NA]", "ticker": "ASML", "industry": "Semiconductor Equip", "sector": "Information Technology", "nano": "Veldhoven High-NA EUV (0.55 NA) Lithography Cleanroom"}], "sa": [{"key": "aramco", "name": "Saudi Aramco [2222:SR]", "ticker": "ARAMCO", "industry": "Oil/Gas (Integrated)", "sector": "Energy", "nano": "Abqaiq World Largest Crude Processing Facility (7M bpd)"}, {"key": "sabic", "name": "SABIC [2010:SR]", "ticker": "SABIC", "industry": "Chemical (Specialty)", "sector": "Materials", "nano": "Jubail Industrial City Petrochemical Cracker Complex"}], "de": [{"key": "sap", "name": "SAP SE [SAP:GY]", "ticker": "SAP", "industry": "Software (System & Application)", "sector": "Information Technology", "nano": "Walldorf Enterprise Cloud ERP Development Center"}, {"key": "sie", "name": "Siemens AG [SIE:GY]", "ticker": "SIE", "industry": "Electrical Equipment", "sector": "Industrials", "nano": "Amberg Electronic Works Digital Twin Smart Factory"}], "jp": [{"key": "toyota", "name": "Toyota Motor Corp [7203:JP / TM:US]", "ticker": "TM", "industry": "Auto & Truck", "sector": "Consumer Discretionary", "nano": "Motomachi Plant Solid-State Battery & Lean Production"}, {"key": "tel", "name": "Tokyo Electron Ltd [8035:JP]", "ticker": "8035", "industry": "Semiconductor Equip", "sector": "Information Technology", "nano": "Yamanashi Plasma Etch & Atomic Layer Deposition Hub"}], "kr": [{"key": "samsung", "name": "Samsung Electronics [005930:KS]", "ticker": "SAMSUNG", "industry": "Semiconductor", "sector": "Information Technology", "nano": "Pyeongtaek Campus Line 4 V-NAND & HBM3e Memory Fab"}], "cn": [{"key": "tencent", "name": "Tencent Holdings [0700:HK]", "ticker": "0700", "industry": "Software (Internet)", "sector": "Communication Services", "nano": "Shenzhen Tencent Binhai Mansion & Cloud AI Cluster"}, {"key": "baba", "name": "Alibaba Group [BABA:US / 9988:HK]", "ticker": "BABA", "industry": "Retail (Online)", "sector": "Consumer Discretionary", "nano": "Hangzhou Cloud Data Center & Cainiao Smart Logistics"}, {"key": "byd", "name": "BYD Co Ltd [1211:HK / 002594:SZ]", "ticker": "1211", "industry": "Auto & Truck", "sector": "Consumer Discretionary", "nano": "Shenzhen Mega Blade Battery & FinDreams EV Assembly"}], "uk": [{"key": "shel", "name": "Shell plc [SHEL:LN]", "ticker": "SHEL", "industry": "Oil/Gas (Integrated)", "sector": "Energy", "nano": "Pernis Mega Refinery & Prelude Floating LNG Facility"}], "fr": [{"key": "lvmh", "name": "LVMH Moët Hennessy [MC:FP]", "ticker": "MC", "industry": "Apparel", "sector": "Consumer Discretionary", "nano": "Asnières-sur-Seine Louis Vuitton Historic Trunk Workshop"}, {"key": "tte", "name": "TotalEnergies SE [TTE:FP]", "ticker": "TTE", "industry": "Oil/Gas (Integrated)", "sector": "Energy", "nano": "Antwerp Integrated Petrochemical Platform & LNG Export"}], "ch": [{"key": "roche", "name": "Roche Holding AG [ROG:SW]", "ticker": "ROG", "industry": "Drugs (Pharmaceutical)", "sector": "Health Care", "nano": "Basel Global Diagnostics & Biotechnology Research Campus"}], "au": [{"key": "bhp", "name": "BHP Group Ltd [BHP:AU]", "ticker": "BHP", "industry": "Metals & Mining", "sector": "Materials", "nano": "Western Australia Iron Ore (WAIO) Automated Railway & Port Hedland"}], "in": [{"key": "polycab", "name": "Polycab India Ltd [POLYCAB:IN]", "ticker": "POLYCAB", "industry": "Electrical Equipment", "sector": "Industrials", "nano": "Polycab Halol Mega Manufacturing Complex (Gujarat)"}, {"key": "kei", "name": "KEI Industries Ltd [KEI:IN]", "ticker": "KEI", "industry": "Electrical Equipment", "sector": "Industrials", "nano": "Chinchpada Extra High Voltage (EHV) Power Cable Plant"}, {"key": "apl_apollo", "name": "APL Apollo Tubes Ltd [APLAPOLLO:IN]", "ticker": "APLAPOLLO", "industry": "Steel", "sector": "Materials", "nano": "Raipur 400x400 Heavy Structural Steel Tube Mill"}, {"key": "pidilite", "name": "Pidilite Industries [PIDILITIND:IN]", "ticker": "PIDILITE", "industry": "Chemical (Specialty)", "sector": "Materials", "nano": "Vapi Synthetic Resin & Fevicol Adhesive Polymer Plant"}, {"key": "narayana", "name": "Narayana Hrudayalaya [NH:IN]", "ticker": "NARAYANA", "industry": "Hospitals/Healthcare Facilities", "sector": "Health Care", "nano": "Bangalore Health City 1000-Bed Cardiac Unit Economics"}, {"key": "hdfc_bank", "name": "HDFC Bank Ltd [HDFCBANK:IN]", "ticker": "HDFCBANK", "industry": "Bank (Money Center)", "sector": "Financials", "nano": "Mumbai Senapati Bapat Marg Central Processing Center"}, {"key": "reliance", "name": "Reliance Industries Ltd [RELIANCE:IN]", "ticker": "RELIANCE", "industry": "Oil/Gas (Integrated)", "sector": "Energy", "nano": "Jamnagar 1.24M bpd Export Refinery Complex & Jio 5G Hub"}, {"key": "tcs", "name": "Tata Consultancy Services [TCS:IN]", "ticker": "TCS", "industry": "Computer Services", "sector": "Information Technology", "nano": "TCS Banyan Park Global Delivery Center & BaNCS Engine"}], "all": [{"key": "nvda", "name": "Nvidia Corp [NVDA:US]", "ticker": "NVDA", "industry": "Semiconductor", "sector": "Information Technology", "nano": "TSMC N4P Foundry & Blackwell GB200 Cluster"}, {"key": "aapl", "name": "Apple Inc [AAPL:US]", "ticker": "AAPL", "industry": "Computers/Peripherals", "sector": "Information Technology", "nano": "Cupertino Apple Park & A18 Pro Bionic Fab"}, {"key": "msft", "name": "Microsoft Corp [MSFT:US]", "ticker": "MSFT", "industry": "Software (System & Application)", "sector": "Information Technology", "nano": "Azure Hyperscale Data Center & OpenAI Supercluster"}, {"key": "googl", "name": "Alphabet Inc [GOOGL:US]", "ticker": "GOOGL", "industry": "Information Services", "sector": "Communication Services", "nano": "Googleplex & Gemini TPU v5e Supercluster"}, {"key": "amzn", "name": "Amazon.com Inc [AMZN:US]", "ticker": "AMZN", "industry": "Retail (Online)", "sector": "Consumer Discretionary", "nano": "AWS US-East Ashburn Cloud Hub & Logistics Robotics"}, {"key": "jpm", "name": "JPMorgan Chase & Co [JPM:US]", "ticker": "JPM", "industry": "Bank (Money Center)", "sector": "Financials", "nano": "270 Park Ave Global HQ & Fixed Income Algo Desk"}, {"key": "xom", "name": "ExxonMobil Corp [XOM:US]", "ticker": "XOM", "industry": "Oil/Gas (Integrated)", "sector": "Energy", "nano": "Baytown Mega Refinery & Permian Basin Drilling Rig"}, {"key": "blk", "name": "BlackRock Inc [BLK:US]", "ticker": "BLK", "industry": "Investments & Asset Management", "sector": "Financials", "nano": "Aladdin Enterprise SaaS Engine & $11.5T Risk Desk"}, {"key": "tsla", "name": "Tesla Inc [TSLA:US]", "ticker": "TSLA", "industry": "Auto & Truck", "sector": "Consumer Discretionary", "nano": "Austin Giga Texas 4680 Battery & Dojo FSD Compute"}, {"key": "lly", "name": "Eli Lilly & Co [LLY:US]", "ticker": "LLY", "industry": "Drugs (Pharmaceutical)", "sector": "Health Care", "nano": "Research Triangle Biomanufacturing Facility (Mounjaro)"}, {"key": "lmt", "name": "Lockheed Martin Corp [LMT:US]", "ticker": "LMT", "industry": "Aerospace/Defense", "sector": "Industrials", "nano": "Fort Worth Skunk Works & F-35 Lightning Production"}, {"key": "nee", "name": "NextEra Energy [NEE:US]", "ticker": "NEE", "industry": "Green & Renewable Energy", "sector": "Utilities", "nano": "Florida Solar & Storage Energy Center (FPL Grid)"}, {"key": "tsm", "name": "Taiwan Semiconductor Mfg [TSM:US / 2330:TW]", "ticker": "TSM", "industry": "Semiconductor", "sector": "Information Technology", "nano": "Hsinchu Science Park Fab 20 (2nm Gate-All-Around GAA)"}, {"key": "asml", "name": "ASML Holding NV [ASML:US / ASML:NA]", "ticker": "ASML", "industry": "Semiconductor Equip", "sector": "Information Technology", "nano": "Veldhoven High-NA EUV (0.55 NA) Lithography Cleanroom"}, {"key": "aramco", "name": "Saudi Aramco [2222:SR]", "ticker": "ARAMCO", "industry": "Oil/Gas (Integrated)", "sector": "Energy", "nano": "Abqaiq World Largest Crude Processing Facility (7M bpd)"}, {"key": "sabic", "name": "SABIC [2010:SR]", "ticker": "SABIC", "industry": "Chemical (Specialty)", "sector": "Materials", "nano": "Jubail Industrial City Petrochemical Cracker Complex"}, {"key": "sap", "name": "SAP SE [SAP:GY]", "ticker": "SAP", "industry": "Software (System & Application)", "sector": "Information Technology", "nano": "Walldorf Enterprise Cloud ERP Development Center"}, {"key": "sie", "name": "Siemens AG [SIE:GY]", "ticker": "SIE", "industry": "Electrical Equipment", "sector": "Industrials", "nano": "Amberg Electronic Works Digital Twin Smart Factory"}, {"key": "toyota", "name": "Toyota Motor Corp [7203:JP / TM:US]", "ticker": "TM", "industry": "Auto & Truck", "sector": "Consumer Discretionary", "nano": "Motomachi Plant Solid-State Battery & Lean Production"}, {"key": "tel", "name": "Tokyo Electron Ltd [8035:JP]", "ticker": "8035", "industry": "Semiconductor Equip", "sector": "Information Technology", "nano": "Yamanashi Plasma Etch & Atomic Layer Deposition Hub"}, {"key": "samsung", "name": "Samsung Electronics [005930:KS]", "ticker": "SAMSUNG", "industry": "Semiconductor", "sector": "Information Technology", "nano": "Pyeongtaek Campus Line 4 V-NAND & HBM3e Memory Fab"}, {"key": "tencent", "name": "Tencent Holdings [0700:HK]", "ticker": "0700", "industry": "Software (Internet)", "sector": "Communication Services", "nano": "Shenzhen Tencent Binhai Mansion & Cloud AI Cluster"}, {"key": "baba", "name": "Alibaba Group [BABA:US / 9988:HK]", "ticker": "BABA", "industry": "Retail (Online)", "sector": "Consumer Discretionary", "nano": "Hangzhou Cloud Data Center & Cainiao Smart Logistics"}, {"key": "byd", "name": "BYD Co Ltd [1211:HK / 002594:SZ]", "ticker": "1211", "industry": "Auto & Truck", "sector": "Consumer Discretionary", "nano": "Shenzhen Mega Blade Battery & FinDreams EV Assembly"}, {"key": "shel", "name": "Shell plc [SHEL:LN]", "ticker": "SHEL", "industry": "Oil/Gas (Integrated)", "sector": "Energy", "nano": "Pernis Mega Refinery & Prelude Floating LNG Facility"}, {"key": "lvmh", "name": "LVMH Moët Hennessy [MC:FP]", "ticker": "MC", "industry": "Apparel", "sector": "Consumer Discretionary", "nano": "Asnières-sur-Seine Louis Vuitton Historic Trunk Workshop"}, {"key": "tte", "name": "TotalEnergies SE [TTE:FP]", "ticker": "TTE", "industry": "Oil/Gas (Integrated)", "sector": "Energy", "nano": "Antwerp Integrated Petrochemical Platform & LNG Export"}, {"key": "roche", "name": "Roche Holding AG [ROG:SW]", "ticker": "ROG", "industry": "Drugs (Pharmaceutical)", "sector": "Health Care", "nano": "Basel Global Diagnostics & Biotechnology Research Campus"}, {"key": "bhp", "name": "BHP Group Ltd [BHP:AU]", "ticker": "BHP", "industry": "Metals & Mining", "sector": "Materials", "nano": "Western Australia Iron Ore (WAIO) Automated Railway & Port Hedland"}, {"key": "polycab", "name": "Polycab India Ltd [POLYCAB:IN]", "ticker": "POLYCAB", "industry": "Electrical Equipment", "sector": "Industrials", "nano": "Polycab Halol Mega Manufacturing Complex (Gujarat)"}, {"key": "kei", "name": "KEI Industries Ltd [KEI:IN]", "ticker": "KEI", "industry": "Electrical Equipment", "sector": "Industrials", "nano": "Chinchpada Extra High Voltage (EHV) Power Cable Plant"}, {"key": "apl_apollo", "name": "APL Apollo Tubes Ltd [APLAPOLLO:IN]", "ticker": "APLAPOLLO", "industry": "Steel", "sector": "Materials", "nano": "Raipur 400x400 Heavy Structural Steel Tube Mill"}, {"key": "pidilite", "name": "Pidilite Industries [PIDILITIND:IN]", "ticker": "PIDILITE", "industry": "Chemical (Specialty)", "sector": "Materials", "nano": "Vapi Synthetic Resin & Fevicol Adhesive Polymer Plant"}, {"key": "narayana", "name": "Narayana Hrudayalaya [NH:IN]", "ticker": "NARAYANA", "industry": "Hospitals/Healthcare Facilities", "sector": "Health Care", "nano": "Bangalore Health City 1000-Bed Cardiac Unit Economics"}, {"key": "hdfc_bank", "name": "HDFC Bank Ltd [HDFCBANK:IN]", "ticker": "HDFCBANK", "industry": "Bank (Money Center)", "sector": "Financials", "nano": "Mumbai Senapati Bapat Marg Central Processing Center"}, {"key": "reliance", "name": "Reliance Industries Ltd [RELIANCE:IN]", "ticker": "RELIANCE", "industry": "Oil/Gas (Integrated)", "sector": "Energy", "nano": "Jamnagar 1.24M bpd Export Refinery Complex & Jio 5G Hub"}, {"key": "tcs", "name": "Tata Consultancy Services [TCS:IN]", "ticker": "TCS", "industry": "Computer Services", "sector": "Information Technology", "nano": "TCS Banyan Park Global Delivery Center & BaNCS Engine"}]};

function populateGlobalDropdowns(countryKey, sectorKey) {
  window.populateGlobalDropdowns = populateGlobalDropdowns;
  var cKey = countryKey || 'in';
  var secSelect = document.getElementById('global_sector_select');
  var firmSelect = document.getElementById('global_firm_select');
  var nanoSelect = document.getElementById('global_nano_select');
  
  // 1. Populate Sectors based on selected country
  if (secSelect) {
    var currSecVal = sectorKey || secSelect.value;
    secSelect.innerHTML = '';
    
    // Group all 94 Damodaran industries
    Object.keys(window.GLOBAL_DAMODARAN_SECTORS).forEach(function(secGroup) {
      var optGroup = document.createElement('optgroup');
      optGroup.label = '── ' + secGroup.toUpperCase() + ' ──';
      
      var inds = window.GLOBAL_DAMODARAN_SECTORS[secGroup];
      inds.forEach(function(ind) {
        var opt = document.createElement('option');
        opt.value = ind.name;
        opt.textContent = ind.name + ' (Beta ' + ind.beta.toFixed(2) + ' · WACC ' + ind.wacc.toFixed(1) + '% · Margin ' + ind.ebitMargin.toFixed(1) + '%)';
        optGroup.appendChild(opt);
      });
      secSelect.appendChild(optGroup);
    });

    // Default sector selection based on country
    if (currSecVal && Array.from(secSelect.options).some(function(o) { return o.value === currSecVal; })) {
      secSelect.value = currSecVal;
    } else if (cKey === 'us') {
      secSelect.value = 'Semiconductor';
    } else if (cKey === 'sa') {
      secSelect.value = 'Oil/Gas (Integrated)';
    } else if (cKey === 'tw' || cKey === 'kr') {
      secSelect.value = 'Semiconductor';
    } else if (cKey === 'nl') {
      secSelect.value = 'Semiconductor Equip';
    } else if (cKey === 'in') {
      secSelect.value = 'Electrical Equipment';
    } else if (secSelect.options.length > 0) {
      secSelect.selectedIndex = 0;
    }
  }

  // 2. Populate Companies for this country and sector
  populateCompaniesForCountryAndSector(cKey, secSelect ? secSelect.value : null);
}

function populateCompaniesForCountryAndSector(countryKey, selectedSector) {
  window.populateCompaniesForCountryAndSector = populateCompaniesForCountryAndSector;
  var firmSelect = document.getElementById('global_firm_select');
  if (!firmSelect) return;
  
  var cKey = countryKey || document.getElementById('global_country_select').value || 'in';
  var compList = window.GLOBAL_COMPANIES_BY_COUNTRY[cKey] || window.GLOBAL_COMPANIES_BY_COUNTRY['all'];
  
  firmSelect.innerHTML = '';
  var activeFirm = null;

  // Filter firms matching selectedSector if any, or list all country firms
  var matchingFirms = compList.filter(function(f) {
    return !selectedSector || f.industry === selectedSector || f.sector === selectedSector;
  });

  // Fallback to all country firms if none match sector exactly
  var displayFirms = matchingFirms.length > 0 ? matchingFirms : compList;

  displayFirms.forEach(function(f) {
    var opt = document.createElement('option');
    opt.value = f.key;
    opt.textContent = f.name + ' · ' + f.industry;
    firmSelect.appendChild(opt);
  });

  if (displayFirms.length > 0) {
    firmSelect.selectedIndex = 0;
    activeFirm = displayFirms[0];
    updateNanoAsset(activeFirm);
    syncGlobalFirmChange(activeFirm.key);
  }
}

function updateNanoAsset(firmObj) {
  window.updateNanoAsset = updateNanoAsset;
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
}

function syncGlobalCountryChange(countryKey) {
  window.syncGlobalCountryChange = syncGlobalCountryChange;
  populateGlobalDropdowns(countryKey, null);
  
  // Fly BMAP / Cesium 3D camera to country hub
  var geoCoords = {
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
  };

  var coords = geoCoords[countryKey];
  if (coords && window.leafletMap) {
    window.leafletMap.flyTo([coords[0], coords[1]], coords[2], { duration: 1.2 });
  }
  if (coords && window.nativeCesiumViewer && typeof window.flyCesiumTo === 'function') {
    if (countryKey === 'us') window.flyCesiumTo('namerica');
    else if (countryKey === 'sa') window.flyCesiumTo('hormuz');
    else if (countryKey === 'all') window.flyCesiumTo('global');
  }
}

function syncGlobalSectorChange(sectorKey) {
  window.syncGlobalSectorChange = syncGlobalSectorChange;
  var cKey = document.getElementById('global_country_select') ? document.getElementById('global_country_select').value : 'in';
  populateCompaniesForCountryAndSector(cKey, sectorKey);
}

function syncGlobalFirmChange(firmKey) {
  window.syncGlobalFirmChange = syncGlobalFirmChange;
  var norm = (firmKey || 'polycab').toLowerCase();

  // 1. Fractal Zoom Tier sync
  if (typeof window.onFirmDropdownChange === 'function') {
    window.onFirmDropdownChange(norm);
  }

  // 2. Real-Time Technicals Cockpit sync
  var techMap = {
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
  };

  var techSymbol = techMap[norm] || norm.toUpperCase();
  if (typeof window.switchTechStock === 'function') {
    window.switchTechStock(techSymbol);
  }

  // 3. Share Price Predictor & DCF sync
  var presetKey = norm;
  if (norm === 'apl_apollo') presetKey = 'apl';
  if (norm === 'narayana' || norm === 'max_health') presetKey = 'narayana';
  if (typeof window.loadStockPreset === 'function') {
    window.loadStockPreset(presetKey);
  }

  // 4. SOIC 310-pt Scorecard sync
  var soicMap = {
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
  };
  try {
    var targetSoic = soicMap[norm] || 'Polycab India Ltd';
    if (typeof window.loadSoicStock === 'function') {
      window.loadSoicStock(targetSoic);
    }
  } catch (e) {}

  // 5. Financial Titans Level 2 DOM Order Book sync
  if (typeof window.switchTickTicker === 'function') {
    window.switchTickTicker(techSymbol);
  }
}

function syncGlobalNanoChange(nanoKey) {
  window.syncGlobalNanoChange = syncGlobalNanoChange;
  if (typeof window.onNanoDropdownChange === 'function') {
    window.onNanoDropdownChange(nanoKey);
  }
}


window.populateGlobalDropdowns = populateGlobalDropdowns;
window.populateCompaniesForCountryAndSector = populateCompaniesForCountryAndSector;
window.updateNanoAsset = updateNanoAsset;
window.syncGlobalCountryChange = syncGlobalCountryChange;
window.syncGlobalSectorChange = syncGlobalSectorChange;
window.syncGlobalFirmChange = syncGlobalFirmChange;
window.syncGlobalNanoChange = syncGlobalNanoChange;

// Initialize dropdowns immediately and on DOMContentLoaded
populateGlobalDropdowns('in', 'Electrical Equipment');
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', function() {
    populateGlobalDropdowns('in', 'Electrical Equipment');
  });
}

function jumpToTabForActiveFirm(tabId) {
  showTab(null, tabId);
  if (tabId === 'zoom') {
    if (typeof window.setFractalTier === 'function') window.setFractalTier(4);
  } else if (tabId === 'technicals') {
    var fKey = document.getElementById('global_firm_select') ? document.getElementById('global_firm_select').value : 'polycab';
    if (typeof window.switchTechStock === 'function') {
      window.switchTechStock(fKey.toUpperCase());
    }
    if (typeof window.drawTechnicalsChart === 'function') {
      setTimeout(window.drawTechnicalsChart, 40);
    }
  } else if (tabId === 'bmap') {
    var nKey = document.getElementById('global_nano_select') ? document.getElementById('global_nano_select').value : 'halol_mega';
    if (window.nanoData && window.nanoData[nKey] && typeof window.syncMapToNanoCoords === 'function') {
      var c = window.nanoData[nKey].coords;
      window.syncMapToNanoCoords(c[0], c[1]);
    }
  }
}


function showTab(el, tabId) {
  if (!tabId) return;
  if (currentWorkspaceMode !== 'single') {
    setWorkspaceMode('single');
  }
  document.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
  document.querySelectorAll('.content').forEach(c => c.classList.remove('active'));
  if (el) {
    el.classList.add('active');
  } else {
    var targetTab = Array.from(document.querySelectorAll('.tab')).find(t => {
      var oc = t.getAttribute('onclick') || '';
      return oc.includes("'" + tabId + "'") || oc.includes('"' + tabId + '"');
    });
    if (targetTab) targetTab.classList.add('active');
  }
  var targetContent = document.getElementById(tabId);
  if (targetContent) {
    targetContent.classList.add('active');
  }
  if (tabId === 'technicals') {
    if (typeof window.drawTechnicalsChart === 'function') {
      setTimeout(window.drawTechnicalsChart, 40);
    }
  } else if (tabId === 'titans') {
    if (typeof window.switchTitanTab === 'function') {
      setTimeout(function() { window.switchTitanTab('blk'); }, 40);
    }
  } else if (tabId === 'soic_sectors') {
    if (typeof window.switchSectorPane === 'function') {
      setTimeout(function() { window.switchSectorPane('damodaran'); }, 40);
    }
  } else if (tabId === 'topnotch') {
    if (typeof window.switchTopNotchTab === 'function') {
      setTimeout(function() { window.switchTopNotchTab('citadel'); }, 40);
    }
  }

  // Auto-align viewport so active tab content is smoothly and fully visible
  var tabsBar = document.querySelector('.tabs');
  if (tabsBar) {
    var tabsRect = tabsBar.getBoundingClientRect();
    if (tabsRect.top < 0 || tabsRect.bottom > window.innerHeight || window.scrollY > tabsBar.offsetTop + 10) {
      tabsBar.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
  }

  // Refresh layout for Leaflet maps and Chart.js
  window.dispatchEvent(new Event('resize'));
  if (tabId === 'bmap') {
    setTimeout(function() {
      if (typeof bmapMap !== 'undefined' && bmapMap) bmapMap.invalidateSize();
      if (typeof drawBmap === 'function') drawBmap();
    }, 60);
  }
}

function runHotkey(tabId) {
  if (tabId === 'help') {
    openHelpModal();
    return;
  }
  showTab(null, tabId);
}

// ── Picture-in-Picture Floating Dock ──
var isPipOpen = false;
var pipMode = 'radar';
var pipAnimTimer = null;

function togglePipMode() {
  isPipOpen = !isPipOpen;
  var dock = document.getElementById('bb_pip_dock');
  var btn = document.getElementById('ws_btn_pip');
  if (dock) dock.style.display = isPipOpen ? 'flex' : 'none';
  if (btn) {
    if (isPipOpen) btn.classList.add('active');
    else btn.classList.remove('active');
  }
  if (isPipOpen && !pipAnimTimer) {
    startPipLoop();
  }
}

function togglePipView() {
  pipMode = pipMode === 'radar' ? 'tape' : 'radar';
  var title = document.getElementById('pipTitleText');
  if (title) title.textContent = pipMode === 'radar' ? 'BMAP MINI-RADAR (AIS LIVE)' : 'TICK ORDER BOOK MINI-HUD';
}

function startPipLoop() {
  var pCanvas = document.getElementById('pipCanvas');
  if (!pCanvas) return;
  var pctx = pCanvas.getContext('2d');

  function renderPip() {
    if (!isPipOpen) { pipAnimTimer = null; return; }
    var w = pCanvas.width, h = pCanvas.height;
    pctx.clearRect(0, 0, w, h);

    if (pipMode === 'radar') {
      pctx.fillStyle = '#050c18';
      pctx.fillRect(0, 0, w, h);

      pctx.strokeStyle = 'rgba(0, 229, 255, 0.15)';
      pctx.lineWidth = 1;
      pctx.beginPath(); pctx.arc(w/2, h/2, 40, 0, Math.PI*2); pctx.stroke();
      pctx.beginPath(); pctx.arc(w/2, h/2, 80, 0, Math.PI*2); pctx.stroke();
      pctx.beginPath(); pctx.arc(w/2, h/2, 120, 0, Math.PI*2); pctx.stroke();

      pctx.strokeStyle = '#00e5ff';
      pctx.lineWidth = 2;
      pctx.setLineDash([4, 4]);
      pctx.beginPath();
      pctx.moveTo(30, 220); pctx.lineTo(120, 180); pctx.lineTo(210, 130); pctx.lineTo(290, 90); pctx.lineTo(390, 45);
      pctx.stroke();
      pctx.setLineDash([]);

      var t = Date.now() * 0.001;
      var v1x = 180 + Math.sin(t * 0.3) * 60;
      var v1y = 140 - Math.sin(t * 0.3) * 35;
      pctx.fillStyle = '#00e5ff';
      pctx.beginPath(); pctx.arc(v1x, v1y, 5, 0, Math.PI*2); pctx.fill();
      pctx.fillStyle = '#fff';
      pctx.font = '9px monospace';
      pctx.fillText('SEAWAYS CATALONIA (8.8 kts)', v1x + 8, v1y - 4);

      var tugX = v1x + 22, tugY = v1y + 12;
      pctx.strokeStyle = '#ffaa00';
      pctx.lineWidth = 1.5;
      pctx.beginPath(); pctx.moveTo(v1x, v1y); pctx.lineTo(tugX, tugY); pctx.stroke();
      pctx.fillStyle = '#ffaa00';
      pctx.beginPath(); pctx.arc(tugX, tugY, 3, 0, Math.PI*2); pctx.fill();
      pctx.fillText('TUG THOR', tugX + 6, tugY + 4);

      var v2x = 310 + Math.cos(t * 0.25) * 40;
      var v2y = 80 - Math.cos(t * 0.25) * 20;
      pctx.fillStyle = '#00e676';
      pctx.beginPath(); pctx.arc(v2x, v2y, 4, 0, Math.PI*2); pctx.fill();
      pctx.fillText('EAGLE VIRGINIA', v2x + 6, v2y - 2);

      var berylX = 70 + Math.sin(t * 0.1) * 15;
      var berylY = 60 + Math.cos(t * 0.1) * 15;
      pctx.strokeStyle = 'rgba(255, 51, 68, 0.6)';
      pctx.lineWidth = 1.5;
      pctx.beginPath(); pctx.arc(berylX, berylY, 24, 0, Math.PI*2); pctx.stroke();
      pctx.fillStyle = '#ff3344';
      pctx.beginPath(); pctx.arc(berylX, berylY, 3, 0, Math.PI*2); pctx.fill();
      pctx.fillText('HURRICANE BERYL (CAT 3)', berylX + 8, berylY - 6);

    } else {
      pctx.fillStyle = '#05070e';
      pctx.fillRect(0, 0, w, h);
      pctx.fillStyle = '#ffaa00';
      pctx.font = '10px monospace';
      pctx.fillText('PIDILITE LEVEL 2 ORDER FLOW', 14, 20);

      pctx.fillStyle = '#00e676';
      pctx.fillText('BID 1: ₹3,142.50 [1,420 shs]', 14, 45);
      pctx.fillText('BID 2: ₹3,142.00 [3,200 shs]', 14, 65);
      pctx.fillText('BID 3: ₹3,141.50 [5,100 shs]', 14, 85);

      pctx.fillStyle = '#ff3344';
      pctx.fillText('ASK 1: ₹3,143.00 [840 shs]', 220, 45);
      pctx.fillText('ASK 2: ₹3,143.50 [2,100 shs]', 220, 65);
      pctx.fillText('ASK 3: ₹3,144.00 [4,300 shs]', 220, 85);

      pctx.fillStyle = '#00e5ff';
      pctx.fillText('OFI Drift: +1,240 shs | VPIN: 0.28 (LOW)', 14, 120);
      pctx.fillText('Kyle Lambda: 0.14 bps | Micro-Price: ₹3,142.82', 14, 140);
    }

    pipAnimTimer = requestAnimationFrame(renderPip);
  }
  pipAnimTimer = requestAnimationFrame(renderPip);
}

// Make PiP dock draggable
(function makePipDraggable() {
  var header = document.getElementById('pipHeader');
  var dock = document.getElementById('bb_pip_dock');
  if (!header || !dock) return;
  var isDragging = false, startX = 0, startY = 0, origX = 0, origY = 0;
  header.addEventListener('mousedown', function(e) {
    isDragging = true;
    startX = e.clientX; startY = e.clientY;
    var rect = dock.getBoundingClientRect();
    origX = rect.left; origY = rect.top;
    dock.style.right = 'auto';
    dock.style.bottom = 'auto';
    dock.style.left = origX + 'px';
    dock.style.top = origY + 'px';
  });
  window.addEventListener('mousemove', function(e) {
    if (!isDragging) return;
    var dx = e.clientX - startX;
    var dy = e.clientY - startY;
    dock.style.left = (origX + dx) + 'px';
    dock.style.top = (origY + dy) + 'px';
  });
  window.addEventListener('mouseup', function() { isDragging = false; });
})();

// ── Realtime Ticker Engine & Brownian Perturbation ──
var marketQuotes = {
  spx: { name: 'SPX', val: 5864.67, pct: 0.38, fmt: v => v.toFixed(2), vol: 1.2 },
  ndx: { name: 'NDX', val: 20412.30, pct: 0.55, fmt: v => v.toFixed(2), vol: 4.5 },
  nifty: { name: 'NIFTY', val: 24148.20, pct: 0.42, fmt: v => v.toFixed(2), vol: 5.0 },
  brent: { name: 'BRENT', val: 75.82, pct: -0.24, fmt: v => '$' + v.toFixed(2), vol: 0.08 },
  wti: { name: 'WTI', val: 71.45, pct: -0.18, fmt: v => '$' + v.toFixed(2), vol: 0.08 },
  us10y: { name: 'US10Y', val: 4.34, pct: 0.00, fmt: v => v.toFixed(2) + '%', vol: 0.01 },
  in10y: { name: 'IN10Y', val: 6.81, pct: 0.00, fmt: v => v.toFixed(2) + '%', vol: 0.01 },
  gold: { name: 'GOLD', val: 2684.50, pct: 0.31, fmt: v => '$' + v.toFixed(2), vol: 1.2 },
  vix: { name: 'VIX', val: 14.85, pct: -1.12, fmt: v => v.toFixed(2), vol: 0.09 },
  usdinr: { name: 'USD/INR', val: 84.38, pct: 0.04, fmt: v => v.toFixed(2), vol: 0.02 },
  eurusd: { name: 'EUR/USD', val: 1.0824, pct: -0.08, fmt: v => v.toFixed(4), vol: 0.0004 },
  pidi: { name: 'PIDILITE', val: 3142.50, pct: 0.65, fmt: v => '₹' + v.toFixed(2), vol: 1.8 },
  nvda: { name: 'NVDA', val: 142.20, pct: 1.42, fmt: v => '$' + v.toFixed(2), vol: 0.35 }
};

var isStreamingLive = true;
var bbAudioEnabled = false;
var audioCtx = null;

function playTerminalClick(freq, duration) {
  if (!bbAudioEnabled) return;
  try {
    if (!audioCtx) audioCtx = new (window.AudioContext || window.webkitAudioContext)();
    var osc = audioCtx.createOscillator();
    var gain = audioCtx.createGain();
    osc.type = 'sine';
    osc.frequency.value = freq || 950;
    gain.gain.setValueAtTime(0.03, audioCtx.currentTime);
    gain.gain.exponentialRampToValueAtTime(0.0001, audioCtx.currentTime + (duration || 0.03));
    osc.connect(gain);
    gain.connect(audioCtx.destination);
    osc.start();
    osc.stop(audioCtx.currentTime + (duration || 0.03));
  } catch(e) {}
}

function toggleTickStream() {
  isStreamingLive = !isStreamingLive;
  var b = document.getElementById('tickStreamBtn');
  if (b) {
    b.textContent = isStreamingLive ? '🟢 LIVE STREAM' : '⏸ PAUSED';
    b.style.color = isStreamingLive ? '#00e676' : '#ffaa00';
  }
}

function toggleBbAudio() {
  bbAudioEnabled = !bbAudioEnabled;
  var b = document.getElementById('bbAudioBtn');
  if (b) {
    b.textContent = bbAudioEnabled ? '🔊 AUDIO: ON' : '🔇 AUDIO: OFF';
    b.style.color = bbAudioEnabled ? '#00e5ff' : '#ffaa00';
  }
  if (bbAudioEnabled) playTerminalClick(1000, 0.05);
}

function tickRealtimeMarkets() {
  if (!isStreamingLive) return;
  var keys = Object.keys(marketQuotes);
  var k = keys[Math.floor(Math.random() * keys.length)];
  var item = marketQuotes[k];
  var delta = (Math.random() - 0.49) * item.vol;
  item.val = Math.max(0.01, item.val + delta);
  var pctChg = (delta / item.val) * 100;
  item.pct = +(item.pct + pctChg).toFixed(2);

  var el = document.getElementById('tick_' + k);
  if (el) {
    var isUp = delta >= 0;
    var sign = isUp ? '+' : '';
    var arrow = isUp ? '▲ ' : '▼ ';
    var cls = isUp ? 'bb-green' : 'bb-red';
    el.innerHTML = item.name + ': <span class="' + cls + '">' + item.fmt(item.val) + ' (' + arrow + sign + item.pct.toFixed(2) + '%)</span>';

    el.classList.remove('flash-up', 'flash-down');
    void el.offsetWidth;
    el.classList.add(isUp ? 'flash-up' : 'flash-down');
    setTimeout(function() {
      el.classList.remove('flash-up', 'flash-down');
    }, 700);

    if (bbAudioEnabled) playTerminalClick(isUp ? 1040 : 820, 0.025);
  }
}

// ── Interactive Cross-Asset Crude Shock Engine ──
var baselineCrude = { brent: 75.82, wti: 71.45 };
var isCrudeShocked = false;

function triggerCrudeShock(pct) {
  isCrudeShocked = true;
  pct = pct || 15;
  var shockedBrent = baselineCrude.brent * (1 + pct / 100);
  var shockedWti = baselineCrude.wti * (1 + pct / 100);

  marketQuotes.brent.val = shockedBrent;
  marketQuotes.brent.pct = +pct.toFixed(2);
  marketQuotes.wti.val = shockedWti;
  marketQuotes.wti.pct = +pct.toFixed(2);

  var elBrent = document.getElementById('tick_brent');
  if (elBrent) {
    elBrent.innerHTML = 'BRENT: <span class="bb-red">$' + shockedBrent.toFixed(2) + ' (▲ +' + pct.toFixed(1) + '%)</span>';
    elBrent.classList.add('flash-down');
  }
  var elWti = document.getElementById('tick_wti');
  if (elWti) {
    elWti.innerHTML = 'WTI: <span class="bb-red">$' + shockedWti.toFixed(2) + ' (▲ +' + pct.toFixed(1) + '%)</span>';
    elWti.classList.add('flash-down');
  }

  if (typeof updateOilTransmission === 'function') {
    updateOilTransmission(shockedBrent);
  }

  if (typeof window.bmapFleet !== 'undefined') {
    window.bmapFleet.forEach(v => {
      if (v.id.includes('seaways') || v.id.includes('eagle')) {
        v.speed = 2.4;
        v.status = 'CHOKEPOINT DEMURRAGE / ANCHORAGE (+18h)';
      }
    });
    if (typeof drawBmap === 'function') drawBmap();
  }

  var marginInput = document.getElementById('val_margin');
  if (marginInput) {
    marginInput.value = (parseFloat(marginInput.value) - 3.5).toFixed(1);
    if (typeof runValuation === 'function') runValuation();
  }

  if (typeof window.injectInstitutionalBlock === 'function') {
    window.injectInstitutionalBlock('SELL', 15000, 3138.00);
  }

  var toast = document.getElementById('bbShockToast');
  if (toast) toast.style.display = 'block';

  if (bbAudioEnabled) playTerminalClick(440, 0.2);
}

function resetCrudeShock() {
  isCrudeShocked = false;
  marketQuotes.brent.val = baselineCrude.brent;
  marketQuotes.brent.pct = -0.24;
  marketQuotes.wti.val = baselineCrude.wti;
  marketQuotes.wti.pct = -0.18;

  var elBrent = document.getElementById('tick_brent');
  if (elBrent) elBrent.innerHTML = 'BRENT: <span class="bb-cyan">$75.82 (-0.24%)</span>';
  var elWti = document.getElementById('tick_wti');
  if (elWti) elWti.innerHTML = 'WTI: <span class="bb-cyan">$71.45 (-0.18%)</span>';

  if (typeof updateOilTransmission === 'function') {
    updateOilTransmission(75.82);
  }

  if (typeof window.bmapFleet !== 'undefined') {
    window.bmapFleet.forEach(v => {
      if (v.id.includes('seaways')) { v.speed = 8.8; v.status = 'In Service / Commissioned'; }
      if (v.id.includes('eagle')) { v.speed = 10.4; v.status = 'Underway using Engine (0)'; }
    });
    if (typeof drawBmap === 'function') drawBmap();
  }

  var marginInput = document.getElementById('val_margin');
  if (marginInput) {
    marginInput.value = "22.4";
    if (typeof runValuation === 'function') runValuation();
  }

  var toast = document.getElementById('bbShockToast');
  if (toast) toast.style.display = 'none';

  if (bbAudioEnabled) playTerminalClick(880, 0.05);
}

// ── Bloomberg Universal Command Engine ──
function handleBbCmd(e) {
  if (e.key === 'Enter') executeBbCmd();
}

function openHelpModal() {
  var m = document.getElementById('bbHelpModal');
  if (m) m.style.display = 'flex';
}

function closeHelpModal() {
  var m = document.getElementById('bbHelpModal');
  if (m) m.style.display = 'none';
}

function executeBbCmdQuick(cmd) {
  var inp = document.getElementById('bbCmdInput');
  if (inp) inp.value = cmd;
  executeBbCmd();
}

function executeBbCmd() {
  var inp = document.getElementById('bbCmdInput');
  if (!inp) return;
  var raw = inp.value.trim().toUpperCase().replace(/<GO>/g, '').trim();
  inp.value = '';
  if (!raw) return;

  if (bbAudioEnabled) playTerminalClick(1100, 0.03);

  // Layout switcher
  if (raw === 'SINGLE' || raw === '1') { setWorkspaceMode('single'); return; }
  if (raw === 'SPLIT' || raw === 'DUAL' || raw === '2') { setWorkspaceMode('split'); return; }
  if (raw === 'GRID' || raw === 'LP' || raw === 'LAUNCHPAD' || raw === '4') { setWorkspaceMode('grid'); return; }
  if (raw === 'PIP') { togglePipMode(); return; }

  // Shock simulator
  if (raw === 'SHOCK' || raw === 'SHOCK CRUDE' || raw === 'CRUDE SHOCK') { triggerCrudeShock(15); return; }
  if (raw === 'RESET' || raw === 'REVERT') { resetCrudeShock(); return; }

  // Help modal
  if (raw === 'HELP' || raw === '?' || raw === 'DOCS') { openHelpModal(); return; }

  // Vessel lookups in BMAP
  var vesselMap = {
    'CATALONIA': 'v_seaways', 'SEAWAYS': 'v_seaways',
    'VIRGINIA': 'v_eagle', 'EAGLE': 'v_eagle',
    'TIGER': 'v_dht', 'DHT': 'v_dht',
    'SABINE': 'v_sabine',
    'ARIES': 'v_maran', 'MARAN': 'v_maran',
    'THOR': 'tug_thor',
    'TRITON': 'tug_triton',
    'BRAZOS': 'pilot_brazos',
    'GLASGOW': 'lng_glasgow',
    'DAFNA': 'lng_dafna',
    'GALVESTON': 'sts_lighter',
    'BERYL': 'hurricane_beryl'
  };
  if (vesselMap[raw]) {
    showTab(null, 'bmap');
    if (typeof selectVesselById === 'function') selectVesselById(vesselMap[raw]);
    return;
  }

  // Stock presets
  var stockPresets = {
    'PIDI': 'pidilite', 'PIDILITE': 'pidilite',

    'POLYCAB': 'polycab', 'POLY': 'polycab',
    'RRKABEL': 'rrkabel', 'RR': 'rrkabel',
    'FINCABLES': 'finolex', 'FINOLEX': 'finolex',
    'MPS': 'mps', 'MPSLTD': 'mps',
    'NIIT': 'niit', 'NIITMTS': 'niit',
    'VERANDA': 'veranda',
    'NAVNEET': 'navneet',
    'STRIDE': 'stride', 'LRN': 'stride',
    'COURSERA': 'coursera', 'COUR': 'coursera',

    'APAT': 'apl_apollo', 'APLAPOLLO': 'apl_apollo',
    'RACL': 'racl', 'RACLGEAR': 'racl',
    'TIIL': 'technocraft', 'TECHNOCRAFT': 'technocraft',
    'KEII': 'kei', 'KEI': 'kei',
    'NVDA': 'nvidia', 'NVIDIA': 'nvidia',
    'AAPL': 'apple', 'APPLE': 'apple'
  };
  if (stockPresets[raw]) {
    showTab(null, 'predictor');
    if (typeof loadPresetStock === 'function') loadPresetStock(stockPresets[raw]);
    if (typeof switchTickTicker === 'function') switchTickTicker(raw);
    return;
  }

  // Function tabs
  var cmdMap = {
    'ZOOM': 'zoom',

    'CABLE': 'zoom', 'CABLES': 'zoom', 'WIRES': 'zoom',
    'EDU': 'zoom', 'EDUCATION': 'zoom', 'EDTECH': 'zoom',
 'FRACTAL': 'zoom', 'SCALE': 'zoom', 'GLOBAL': 'zoom', 'NANO': 'zoom', 'COUNTRY': 'zoom',
    'DES': 'predictor', 'DCF': 'predictor', 'VAL': 'predictor',
    'SCEN': 'scen', 'SIM': 'scen',
    'SOIC': 'soic', 'RANK': 'soic',
    'TECH': 'technicals', 'TECHNOLOGY': 'technicals', 'CHART': 'technicals', 'WEINSTEIN': 'technicals', 'STAGE': 'technicals', 'ADX': 'technicals', 'RSI': 'technicals', 'VSA': 'technicals', 'VSTOP': 'technicals',
    'ROT': 'rot', 'SECT': 'rot',
    'VOL': 'vol', 'OPT': 'vol',
    'FLOW': 'flows', 'CAP': 'flows',
    'BMAP': 'bmap', 'VESL': 'bmap', 'TANKER': 'bmap', 'OIL': 'bmap', 'AIS': 'bmap', 'MAP': 'bmap',
    'BLK': 'titans', 'BLACKROCK': 'titans', 'ALADDIN': 'titans', 'VANG': 'titans', 'VANGUARD': 'titans', 'TITANS': 'titans', 'PE': 'titans', 'LBO': 'titans', 'PORT': 'titans', 'TICK': 'titans', 'DOM': 'titans',
    'SECTOR': 'soic_sectors', 'SECTORS': 'soic_sectors', 'HOSP': 'soic_sectors', 'HOSPITAL': 'soic_sectors', 'HOTEL': 'soic_sectors', 'HOTELS': 'soic_sectors', 'BANK': 'soic_sectors', 'BANKS': 'soic_sectors', 'CABLES': 'soic_sectors', 'KEI': 'soic_sectors', 'APOLLO': 'soic_sectors', 'APLAPOLLO': 'soic_sectors', 'JUBL': 'soic_sectors', 'CHEM': 'soic_sectors', 'IRR': 'soic_sectors',
    'POD': 'topnotch', 'PODS': 'topnotch', 'CITADEL': 'topnotch', 'MILLENNIUM': 'topnotch', 'BWATER': 'topnotch', 'DALIO': 'topnotch', 'ALLWEATHER': 'topnotch', 'FORENSIC': 'topnotch', 'FRAUD': 'topnotch', 'STAGE': 'topnotch', 'GRAIL': 'topnotch', 'CLONER': 'topnotch', 'MANDATE': 'topnotch', 'RENTECH': 'topnotch',
    'MACRO': 'macro', 'WACC': 'macro', 'ERP': 'macro',
    'BETA': 'beta', 'RISK': 'beta',
    'MARGINS': 'margins', 'FA': 'margins',
    'MULTIPLES': 'multiples', 'RV': 'multiples',
    'GROWTH': 'growth',
    'CAPSTRUCT': 'capstruct',
    'WORKCAP': 'workcap', 'WC': 'workcap',
    'TAXRATE': 'taxrate', 'TAX': 'taxrate',
    'CORP': 'fundamentals', 'EVA': 'fundamentals', 'CAPEX': 'fundamentals',
    'AGENTS': 'agents', 'STATUS': 'agents',
    'PAPERS': 'papers', 'DOC': 'papers',
    'ARCH': 'arch'
  };
  if (cmdMap[raw]) {
    showTab(null, cmdMap[raw]);
    return;
  }

  alert('Unknown Terminal Command: ' + raw + '\n\nTry:\nHELP <GO>, SPLIT <GO>, GRID <GO>, BMAP <GO>, PODS <GO>, FORENSIC <GO>, STAGE <GO>, SECTORS <GO>, HOSP <GO>, HOTEL <GO>, BANK <GO>, KEI <GO>, APOLLO <GO>, TITANS <GO>, DES <GO>, SOIC <GO>\nOr Tickers: PIDILITE, KEI, APLAPOLLO, NVDA, AAPL\nOr Vessels: CATALONIA, VIRGINIA, THOR, TRITON, BERYL');
}

// ── Scenario Simulation Controls ──
var simInterval = null;
var simRegimes = ['base', 'stagflation', 'ai_supercycle', 'trade_war', 'dovish_pivot', 'em_flight'];
var simRegimeIdx = 0;

function applyMacroRegime(name) {
  var rf = 4.34, erp = 4.40, mDelta = 0.0, gDelta = 0.0, tDelta = 0.0, wcDelta = 0.0;
  if (name === 'base') {
    rf = 4.34; erp = 4.40; mDelta = 0.0; gDelta = 0.0; tDelta = 0.0; wcDelta = 0.0;
  } else if (name === 'stagflation') {
    rf = 5.84; erp = 5.60; mDelta = -3.5; gDelta = -4.0; tDelta = 1.5; wcDelta = 3.0;
  } else if (name === 'ai_supercycle') {
    rf = 4.10; erp = 4.00; mDelta = 3.0; gDelta = 6.0; tDelta = -1.0; wcDelta = -2.0;
  } else if (name === 'trade_war') {
    rf = 4.80; erp = 5.10; mDelta = -2.5; gDelta = -2.5; tDelta = 2.0; wcDelta = 4.0;
  } else if (name === 'dovish_pivot') {
    rf = 3.34; erp = 4.10; mDelta = 1.0; gDelta = 2.5; tDelta = 0.0; wcDelta = 0.0;
  } else if (name === 'em_flight') {
    rf = 4.50; erp = 6.20; mDelta = -1.5; gDelta = -1.5; tDelta = 0.0; wcDelta = 2.0;
  }
  document.getElementById('slider_rf').value = rf;
  document.getElementById('slider_erp').value = erp;
  document.getElementById('slider_margin_delta').value = mDelta;
  document.getElementById('slider_growth_delta').value = gDelta;
  document.getElementById('slider_tax_delta').value = tDelta;
  document.getElementById('slider_wc_delta').value = wcDelta;
  updateScenarioSliders();
}

function updateScenarioSliders() {
  var rf = parseFloat(document.getElementById('slider_rf').value);
  var erp = parseFloat(document.getElementById('slider_erp').value);
  var mDelta = parseFloat(document.getElementById('slider_margin_delta').value);
  var gDelta = parseFloat(document.getElementById('slider_growth_delta').value);
  var tDelta = parseFloat(document.getElementById('slider_tax_delta').value);
  var wcDelta = parseFloat(document.getElementById('slider_wc_delta').value);

  document.getElementById('lbl_rf').textContent = rf.toFixed(2) + '%';
  document.getElementById('lbl_erp').textContent = erp.toFixed(2) + '%';
  document.getElementById('lbl_margin_delta').textContent = (mDelta >= 0 ? '+' : '') + mDelta.toFixed(2) + '%';
  document.getElementById('lbl_growth_delta').textContent = (gDelta >= 0 ? '+' : '') + gDelta.toFixed(2) + '%';
  document.getElementById('lbl_tax_delta').textContent = (tDelta >= 0 ? '+' : '') + tDelta.toFixed(2) + '%';
  document.getElementById('lbl_wc_delta').textContent = (wcDelta >= 0 ? '+' : '') + wcDelta.toFixed(2) + '%';

  var dynWacc = rf + 1.0 * erp;
  document.getElementById('sim_res_wacc').textContent = dynWacc.toFixed(2) + '%';

  var waccInput = document.getElementById('val_wacc');
  if (waccInput) {
    waccInput.value = dynWacc.toFixed(2);
    if (typeof runValuation === 'function') runValuation();
    var pPriceEl = document.getElementById('res_dcf_price');
    var pUpsideEl = document.getElementById('res_dcf_upside');
    if (pPriceEl) document.getElementById('sim_res_price').textContent = pPriceEl.textContent;
    if (pUpsideEl) {
      document.getElementById('sim_res_mos').textContent = pUpsideEl.textContent;
      var mosVal = parseFloat(pUpsideEl.textContent);
      var verdEl = document.getElementById('sim_res_verdict');
      if (verdEl) {
        if (mosVal >= 25) { verdEl.textContent = 'STRONG BUY'; verdEl.style.color = '#00e676'; }
        else if (mosVal >= 0) { verdEl.textContent = 'ACCUMULATE'; verdEl.style.color = '#00e5ff'; }
        else if (mosVal >= -20) { verdEl.textContent = 'NEUTRAL / HOLD'; verdEl.style.color = '#ffaa00'; }
        else { verdEl.textContent = 'OVERVALUED / AVOID'; verdEl.style.color = '#ff3344'; }
      }
    }
  }
}

function setTimeHorizon(years) {
  [0, 1, 3, 5, 10].forEach(y => {
    var b = document.getElementById('th_btn_' + y);
    if (b) b.classList.remove('active');
  });
  var activeBtn = document.getElementById('th_btn_' + years);
  if (activeBtn) activeBtn.classList.add('active');

  var label = 'Active T+' + years + (years === 0 ? ' (LTM Baseline)' : ' Years Forward');
  document.getElementById('sim_clock_display').textContent = label;

  if (years === 10) {
    document.getElementById('slider_growth_delta').value = -2.0;
  } else if (years === 1) {
    document.getElementById('slider_growth_delta').value = 1.5;
  }
  updateScenarioSliders();
}

function toggleScenarioSimulation() {
  var btn = document.getElementById('sim_play_btn');
  var pill = document.getElementById('sim_status_pill');
  if (simInterval) {
    clearInterval(simInterval);
    simInterval = null;
    btn.textContent = '▶ Auto-Replay Scenarios';
    btn.style.background = '#00d26a';
    pill.textContent = 'STATUS: MANUAL';
  } else {
    btn.textContent = '⏸ Pause Simulation';
    btn.style.background = '#ffaa00';
    pill.textContent = 'STATUS: LIVE SIMULATION';
    simInterval = setInterval(function() {
      simRegimeIdx = (simRegimeIdx + 1) % simRegimes.length;
      applyMacroRegime(simRegimes[simRegimeIdx]);
    }, 2800);
  }
}

// ── SOIC 310-Point Master Framework Logic ──
var soicStockData = {
  'Polycab India Ltd': [40, 75, 105, 25, 35],
  'KEI Industries': [40, 70, 105, 25, 20],
  'Varun Beverages': [35, 75, 95, 20, 25],
  'SRF': [40, 63, 75, 35, 40],
  'NARAYANA HRU': [40, 68, 85, 25, 30],
  'APL Apollo Tubes': [35, 65, 85, 25, 30],
  'Navin Fluorine': [35, 60, 78, 30, 30],
  'Apcotex Industries': [30, 60, 80, 25, 35],
  'Shivalik Bimetal': [35, 60, 80, 25, 30],
  'Pricol': [30, 55, 80, 25, 35],
  'Pidilite Industries': [45, 78, 95, 20, 40],
  'Apple Inc.': [45, 78, 100, 25, 34],
  'Nvidia': [45, 80, 105, 15, 29],
  'Microsoft Corp': [45, 80, 102, 25, 40],
  'Alphabet Inc': [45, 78, 98, 30, 40],
  'Amazon.com Inc': [45, 76, 105, 28, 38],
  'Tesla Inc': [40, 68, 105, 20, 34],
  'ExxonMobil Corp': [42, 74, 98, 28, 38],
  'HDFC Bank Ltd': [45, 78, 92, 30, 40],
  'ASML Holding NV': [45, 80, 108, 26, 40],
  'Saudi Aramco': [45, 80, 98, 30, 40],
  'BHP Group Ltd': [45, 78, 100, 30, 40],
  'Samsung Electronics': [45, 78, 92, 34, 40],
  'BALAJI AMINES': [20, 35, 25, 10, -40]
};

function loadSoicStock(name) {
  var sel = document.getElementById('soic_stock_select');
  if (sel && sel.value !== name) sel.value = name;
  var scores = soicStockData[name] || [40, 75, 105, 25, 35];
  document.getElementById('soic_p1').value = scores[0];
  document.getElementById('soic_p2').value = scores[1];
  document.getElementById('soic_p3').value = scores[2];
  document.getElementById('soic_p4').value = scores[3];
  document.getElementById('soic_p5').value = scores[4];
  recalcSoicScore();
}

function recalcSoicScore() {
  var p1 = parseInt(document.getElementById('soic_p1').value);
  var p2 = parseInt(document.getElementById('soic_p2').value);
  var p3 = parseInt(document.getElementById('soic_p3').value);
  var p4 = parseInt(document.getElementById('soic_p4').value);
  var p5 = parseInt(document.getElementById('soic_p5').value);

  document.getElementById('soic_lbl_p1').textContent = p1 + ' / 45';
  document.getElementById('soic_lbl_p2').textContent = p2 + ' / 80';
  document.getElementById('soic_lbl_p3').textContent = p3 + ' / 110';
  document.getElementById('soic_lbl_p4').textContent = p4 + ' / 35';
  document.getElementById('soic_lbl_p5').textContent = p5 + ' / 40';

  var total = p1 + p2 + p3 + p4 + p5;
  var pct = (total / 310.0 * 100).toFixed(1);
  document.getElementById('soic_total_score').textContent = total;
  document.getElementById('soic_pct_score').textContent = '(' + pct + '%)';

  var badgeEl = document.getElementById('soic_grade_badge');
  if (total >= 270) {
    badgeEl.innerHTML = "<span class='badge' style='background:#00d26a;color:#000;font-weight:700;font-size:14px;padding:6px 12px;'>AAA - TIER 1 COMPOUNDER (SOIC CONVICTION)</span>";
  } else if (total >= 220) {
    badgeEl.innerHTML = "<span class='badge' style='background:#00bcd4;color:#000;font-weight:700;font-size:14px;padding:6px 12px;'>AA - HIGH QUALITY COMPOUNDER</span>";
  } else if (total >= 170) {
    badgeEl.innerHTML = "<span class='badge' style='background:#ffa502;color:#000;font-weight:700;font-size:14px;padding:6px 12px;'>A - CYCLICAL / CONDITIONAL ACCUMULATE</span>";
  } else if (total >= 120) {
    badgeEl.innerHTML = "<span class='badge' style='background:#ff6b81;color:#fff;font-weight:700;font-size:14px;padding:6px 12px;'>B - SPECULATIVE / MARGINAL</span>";
  } else {
    badgeEl.innerHTML = "<span class='badge' style='background:#f8312f;color:#fff;font-weight:700;font-size:14px;padding:6px 12px;'>C - DEFICIENT / FORENSIC RED FLAG</span>";
  }
}

// ── Live Bloomberg Clocks with Millisecond Precision ──
function updateBbClocks() {
  var now = new Date();
  var ms = String(Math.floor(now.getMilliseconds() / 100));
  var fmt = function(d) {
    var h = String(d.getHours()).padStart(2, '0');
    var m = String(d.getMinutes()).padStart(2, '0');
    var s = String(d.getSeconds()).padStart(2, '0');
    return h + ':' + m + ':' + s + '.' + ms;
  };

  var nyc = new Date(now.toLocaleString("en-US", {timeZone: "America/New_York"}));
  var lon = new Date(now.toLocaleString("en-US", {timeZone: "Europe/London"}));
  var mum = new Date(now.toLocaleString("en-US", {timeZone: "Asia/Kolkata"}));
  var tyo = new Date(now.toLocaleString("en-US", {timeZone: "Asia/Tokyo"}));

  var isNycOpen = (nyc.getHours() >= 9 && (nyc.getHours() < 16 || (nyc.getHours() === 9 && nyc.getMinutes() >= 30)));
  var isLonOpen = (lon.getHours() >= 8 && lon.getHours() < 16);
  var isMumOpen = (mum.getHours() >= 9 && (mum.getHours() < 15 || (mum.getHours() === 15 && mum.getMinutes() <= 30)));
  var isTyoOpen = (tyo.getHours() >= 9 && tyo.getHours() < 15);

  var setClock = function(id, d, isOpen) {
    var el = document.getElementById(id);
    if (el) {
      var statePill = isOpen ? '<span class="bb-green">OPEN</span>' : '<span class="bb-red">CLOSED</span>';
      el.innerHTML = fmt(d) + ' ' + statePill;
    }
  };

  setClock('clock_nyc', nyc, isNycOpen);
  setClock('clock_lon', lon, isLonOpen);
  setClock('clock_mum', mum, isMumOpen);
  setClock('clock_tyo', tyo, isTyoOpen);
}

document.addEventListener('DOMContentLoaded', function() {
  updateBbClocks();
  setInterval(updateBbClocks, 100);

  // Live ticker updates
  setInterval(tickRealtimeMarkets, 1200);

  // Default landing route: Check URL hash, else default to 'bmap'
  var hash = (window.location.hash || '').replace('#', '').toLowerCase();
  if (hash === 'split') {
    setWorkspaceMode('split');
  } else if (hash === 'grid' || hash === 'lp') {
    setWorkspaceMode('grid');
  } else if (hash && hash !== 'bmap') {
    showTab(null, hash);
  } else {
    showTab(null, 'bmap');
  }

  loadStockPreset('polycab');
  loadSoicStock('Polycab India Ltd');
  recalcSoicScore();
  setTimeout(updateScenarioSliders, 300);

  // Global physical function hotkeys (F1-F12, 1, 2, 4, Esc)
  window.addEventListener('keydown', function(e) {
    var tag = (e.target.tagName || '').toLowerCase();
    if (tag === 'input' || tag === 'select' || tag === 'textarea') {
      if (e.key === 'Escape') {
        closeHelpModal();
        e.target.blur();
      }
      return;
    }

    if (e.key === '1') { setWorkspaceMode('single'); return; }
    if (e.key === '2') { setWorkspaceMode('split'); return; }
    if (e.key === '4') { setWorkspaceMode('grid'); return; }
    if (e.key === 'Escape') { closeHelpModal(); return; }

    var fMap = {
      'F1': 'zoom', 'F2': 'predictor', 'F3': 'technicals', 'F4': 'scen',
      'F5': 'soic', 'F6': 'rot', 'F7': 'vol', 'F8': 'flows',
      'F9': 'bmap', 'F10': 'macro', 'F11': 'fundamentals', 'F12': 'arch'
    };
    if (fMap[e.key]) {
      e.preventDefault();
      showTab(null, fMap[e.key]);
    }
  });

  // Search/filter for papers table
  var ptable = document.getElementById('papersTable');
  if (ptable) {
    var inp = document.createElement('input');
    inp.placeholder = '🔍 Filter papers by title, venue, category…';
    inp.style.cssText = 'width:100%;padding:8px 14px;background:#05070a;border:1px solid #212d40;border-radius:4px;color:#e0e0e0;font-size:12px;margin-bottom:12px;outline:none;';
    ptable.parentNode.insertBefore(inp, ptable);
    inp.addEventListener('input', function() {
      var q = inp.value.toLowerCase();
      ptable.querySelectorAll('tbody tr').forEach(function(row) {
        row.style.display = row.textContent.toLowerCase().includes(q) ? '' : 'none';
      });
    });
  }
});
