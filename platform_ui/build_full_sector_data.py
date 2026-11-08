# F:\documents\SOIC\EconAgent_Platform\platform_ui\build_full_sector_data.py
# All 30 sectors across 12 countries with authentic financial parameters and matching firm keys

SECTORS = {
    # ── INDIA (7 Sectors) ──
    'cables_in': {
      'name': 'Cables, Wires & EHV Power Infrastructure (India)', 'country': 'india',
      'betaU': 0.95, 'betaL': 0.97, 'opm': 10.9, 'roic': 21.0, 'wacc': 11.2,
      'evEbitda': 26.5, 'assetTurnover': 2.45,
      'moat': 'Continuous cast copper rod vertical integration (Properzi process), scale economies, strict technical certification (CPR, UL, BASEC), and extensive dealer networks (4,000+ distributors).',
      'soicMetrics': [
        { 'label': 'Market Size & Growth', 'value': '₹700B (FY23) ➔ ₹1.25T (FY27) at 13% CAGR' },
        { 'label': 'LME Metal Pass-Through', 'value': '100% Raw Material Formula (30-day lag)' },
        { 'label': 'B2B vs B2C Margin Spread', 'value': 'Institutional: 8.5-10.5% | Retail B2C: 12.0-15.0%' },
        { 'label': 'Working Capital Cycle', 'value': '78-84 Days (Inventory 45d, Receivables 55d)' },
        { 'label': 'EHV 400kV Capability', 'value': 'Brugg Swiss Tie-up / Import Substitution Monopolies' }
      ],
      'representativeFirms': ['Polycab India Ltd', 'KEI Industries Ltd', 'RR Kabel Ltd', 'Finolex Cables Ltd'],
      'firmKeys': ['polycab', 'kei', 'rrkabel', 'finolex']
    },
    'edu_in': {
      'name': 'Education, EdTech & Skill Development (India)', 'country': 'india',
      'betaU': 0.57, 'betaL': 0.61, 'opm': 6.49, 'roic': 24.5, 'wacc': 10.4,
      'evEbitda': 22.0, 'assetTurnover': 1.85,
      'moat': 'Proprietary curriculum intellectual property, multi-year corporate managed training contracts (MTS), hybrid hub-and-spoke study center footprints, and strong test prep pass rate branding.',
      'soicMetrics': [
        { 'label': 'Indian Education TAM', 'value': '$117B ➔ $225B by 2027 (NEP 2020 driver)' },
        { 'label': 'Student Enrollment CAGR', 'value': '18.5% across IT upskilling, BFSI, & Test Prep' },
        { 'label': 'Blended Student ARPU', 'value': '₹42,000 / year (B2B Corporate $3,200/seat)' },
        { 'label': 'Student LTV to CAC Ratio', 'value': '3.8x (Enterprise Training Contracts > 5.5x)' },
        { 'label': 'Content Amortization Cycle', 'value': '3-Year Straight Line (Zero obsolescence risk)' }
      ],
      'representativeFirms': ['MPS Ltd', 'NIIT Learning Systems', 'Veranda Learning', 'Navneet Education'],
      'firmKeys': ['mps', 'niit', 'veranda', 'navneet']
    },
    'chem_in': {
      'name': 'Specialty Chemicals, Adhesives & Fluorochemicals (India)', 'country': 'india',
      'betaU': 0.88, 'betaL': 0.94, 'opm': 18.5, 'roic': 22.5, 'wacc': 10.8,
      'evEbitda': 28.0, 'assetTurnover': 1.45,
      'moat': 'Brand monopoly in consumer adhesives (Fevicol 70%+ share), complex fluorine synthesis chemistry, 2-3 year customer re-validation cycles, and global customer patent linkages.',
      'soicMetrics': [
        { 'label': 'Synthesis Reaction Yields', 'value': '> 88.5% in multi-step fluorination' },
        { 'label': 'Regulatory Switching Cost', 'value': '2-3 Years customer re-validation cycle' },
        { 'label': 'R&D Reinvestment Ratio', 'value': '4.8% of Gross Revenues' },
        { 'label': 'Global China+1 Offtake', 'value': 'Agro & Pharma intermediates long-term supply' },
        { 'label': 'Export Revenue Share', 'value': '45-65% across global innovators' }
      ],
      'representativeFirms': ['Pidilite Industries Ltd', 'SRF Ltd', 'Navin Fluorine Intl', 'Jubilant Ingrevia Ltd'],
      'firmKeys': ['pidilite', 'srf', 'navin', 'jubilant']
    },
    'hosp_in': {
      'name': 'Super-Specialty Healthcare & Hospital Chains (India)', 'country': 'india',
      'betaU': 0.65, 'betaL': 0.72, 'opm': 24.5, 'roic': 20.8, 'wacc': 9.8,
      'evEbitda': 32.5, 'assetTurnover': 1.15,
      'moat': 'High regulatory barriers to metro hospital construction, doctor retention equity models, high cash-and-TPA payor mix (80%+ non-government), and commanding ARPOB.',
      'soicMetrics': [
        { 'label': 'Average Rev / Bed (ARPOB)', 'value': '₹72,500 / day (NCR/Mumbai ₹85k+)' },
        { 'label': 'Bed Occupancy Ratio', 'value': '74.2% operational capacity' },
        { 'label': 'Payor Mix Cash/TPA', 'value': '82% Private Cash/Insurance : 18% Govt' },
        { 'label': 'ALOS (Avg Length of Stay)', 'value': '3.2 Days (High surgical throughput)' },
        { 'label': 'Brownfield Expansion IRR', 'value': '24-28% post-commissioning' }
      ],
      'representativeFirms': ['Max Healthcare Institute', 'Narayana Hrudayalaya', 'Apollo Hospitals Enterprise'],
      'firmKeys': ['max_health', 'narayana', 'apollo_hosp']
    },
    'hotel_in': {
      'name': 'Hospitality, Luxury Chains & Asset-Light Hotels (India)', 'country': 'india',
      'betaU': 0.78, 'betaL': 0.92, 'opm': 32.0, 'roic': 18.2, 'wacc': 10.2,
      'evEbitda': 28.5, 'assetTurnover': 0.65,
      'moat': 'Prime metropolitan real estate locations, brand equity (Taj, Marriott, Westin), asset-light management contracts (35%+ management fees), and corporate convention stickiness.',
      'soicMetrics': [
        { 'label': 'RevPAR Growth', 'value': '+14.2% YoY (ARR ₹11,200/night)' },
        { 'label': 'Asset-Light Pipeline', 'value': '62% of upcoming keys under management contract' },
        { 'label': 'Metro Occupancy', 'value': '74.8% across key business gateways' },
        { 'label': 'MICE / Wedding Revenue', 'value': '38% of total food & beverage intake' },
        { 'label': 'EBITDA Margin on Managed Keys', 'value': '72% flow-through on contract fees' }
      ],
      'representativeFirms': ['The Indian Hotels Co (Taj)', 'SAMHI Hotels Ltd', 'Chalet Hotels Ltd'],
      'firmKeys': ['ihcl', 'samhi', 'chalet']
    },
    'pipe_in': {
      'name': 'Heavy Structural Tubes, Stainless Steel & ERW Pipes (India)', 'country': 'india',
      'betaU': 0.92, 'betaL': 1.05, 'opm': 11.2, 'roic': 23.5, 'wacc': 11.0,
      'evEbitda': 22.0, 'assetTurnover': 2.85,
      'moat': 'Continuous direct-forming square hollow section technology, 50%+ national market share, distribution logistics moat with 1,500+ exclusive retail distributors.',
      'soicMetrics': [
        { 'label': 'EBITDA per Ton', 'value': '₹4,850 / MT blended' },
        { 'label': 'Scrap Recovery Ratio', 'value': '96.5% high-frequency ERW' },
        { 'label': 'Heavy Hollow Section Share', 'value': '65% domestic organized market' },
        { 'label': 'Inventory Turnover', 'value': '28 Days (Ultra-lean operating cycle)' },
        { 'label': 'Capacity Utilization', 'value': '82% on 3.5 Million MT capacity' }
      ],
      'representativeFirms': ['APL Apollo Tubes Ltd', 'Ratnamani Metals & Tubes', 'Welspun Corp Ltd'],
      'firmKeys': ['apl_apollo', 'ratnamani', 'welspun']
    },
    'bank_in': {
      'name': 'Commercial Banking, Retail Lending & Asset Quality (India)', 'country': 'india',
      'betaU': 0.85, 'betaL': 1.15, 'opm': 38.5, 'roic': 17.5, 'wacc': 10.5,
      'evEbitda': 16.5, 'assetTurnover': 0.15,
      'moat': 'Low-cost CASA deposit franchise (40%+ CASA), nationwide branch architecture (8,000+ branches), pristine underwriting with GNPA < 1.5%, and proprietary credit algorithms.',
      'soicMetrics': [
        { 'label': 'Net Interest Margin (NIM)', 'value': '3.85 - 4.35% annualized' },
        { 'label': 'Gross NPA / Net NPA', 'value': 'GNPA 1.2% - 1.8% | NNPA 0.3% - 0.4%' },
        { 'label': 'Capital Adequacy (CRAR)', 'value': '18.4% - 20.8% (Tier-1 > 16.5%)' },
        { 'label': 'Cost-to-Income Ratio', 'value': '38.2% - 42.5% across top private banks' },
        { 'label': 'Return on Assets (ROA)', 'value': '1.95% - 2.40% best-in-class' }
      ],
      'representativeFirms': ['HDFC Bank Ltd', 'ICICI Bank Ltd', 'Kotak Mahindra Bank', 'State Bank of India'],
      'firmKeys': ['hdfc_bank', 'icici_bank', 'kotak_bank', 'sbi']
    },

    # ── US (5 Sectors) ──
    'semi_us': {
      'name': 'AI Accelerators, Hyperscale GPU Compute & Foundry (US)', 'country': 'us',
      'betaU': 1.15, 'betaL': 1.28, 'opm': 54.5, 'roic': 58.0, 'wacc': 8.8,
      'evEbitda': 34.0, 'assetTurnover': 1.15,
      'moat': 'CUDA parallel computing software ecosystem, NVLink interconnect architecture, TSMC CoWoS advanced packaging capacity lock, and hyperscaler developer lock-in.',
      'soicMetrics': [
        { 'label': 'Data Center Rev Mix', 'value': '85.5% of total corporate revenues' },
        { 'label': 'Gross Margin Profile', 'value': '75.2% non-GAAP hardware & software' },
        { 'label': 'GPU ASP Benchmark', 'value': '$32,000 / B200 accelerator platform' },
        { 'label': 'Hyperscaler AI Capex Run-Rate', 'value': '$250+ Billion annualized spend across MSFT, GOOG, AMZN, META' },
        { 'label': 'CoWoS Packaging Supply', 'value': 'Full allocation through 2026' }
      ],
      'representativeFirms': ['NVIDIA Corporation', 'Advanced Micro Devices', 'Broadcom Inc', 'Qualcomm Inc'],
      'firmKeys': ['nvidia', 'amd', 'broadcom', 'qualcomm']
    },
    'tech_us': {
      'name': 'Mega-Cap Software, Cloud Hyperscalers & Hardware Platforms (US)', 'country': 'us',
      'betaU': 0.95, 'betaL': 1.05, 'opm': 34.2, 'roic': 38.5, 'wacc': 8.2,
      'evEbitda': 24.5, 'assetTurnover': 0.88,
      'moat': 'Global consumer ecosystem lock-in (2.2B active Apple devices), enterprise cloud dominance (Azure & AWS), search advertising monopoly (Google 90%+), and massive FCF generation.',
      'soicMetrics': [
        { 'label': 'Services Gross Margin', 'value': '74.2% recurring software revenue' },
        { 'label': 'Combined Annual FCF', 'value': 'Over $350 Billion across top 5 tech giants' },
        { 'label': 'Active Installed Base', 'value': 'Billions of connected consumer & enterprise endpoints' },
        { 'label': 'Enterprise Cloud Growth', 'value': '+28-33% YoY across Azure and AWS' },
        { 'label': 'Share Repurchases YTD', 'value': '$100B+ annual capital return run-rate' }
      ],
      'representativeFirms': ['Apple Inc', 'Microsoft Corp', 'Alphabet Inc (Google)', 'Amazon.com Inc', 'Tesla Inc'],
      'firmKeys': ['apple', 'microsoft', 'alphabet', 'amazon', 'tesla']
    },
    'edu_us': {
      'name': 'Digital Learning Platforms & Enterprise Education (US)', 'country': 'us',
      'betaU': 0.72, 'betaL': 0.85, 'opm': 14.5, 'roic': 18.0, 'wacc': 8.5,
      'evEbitda': 16.5, 'assetTurnover': 0.95,
      'moat': 'Accredited online public school state funding charters, top-tier university degree partnerships, viral gamified language retention algorithms, and corporate L&D contracts.',
      'soicMetrics': [
        { 'label': 'Global Online EdTech TAM', 'value': '$404B by 2028' },
        { 'label': 'Enterprise LTV to CAC', 'value': '4.2x LTV/CAC ratio' },
        { 'label': 'Annual Course Retention', 'value': '86.4% enterprise renewal rates' },
        { 'label': 'K-12 Virtual Enrollment', 'value': '195,000+ full-time public students' },
        { 'label': 'Gamified DAU Engagement', 'value': '34 Million daily active learners on Duolingo' }
      ],
      'representativeFirms': ['Stride Inc (K12)', 'Coursera Inc', 'Duolingo Inc'],
      'firmKeys': ['stride', 'coursera', 'duolingo']
    },
    'cables_us': {
      'name': 'North American Power Grid Modernization & Wire Systems (US)', 'country': 'us',
      'betaU': 0.88, 'betaL': 0.98, 'opm': 16.8, 'roic': 22.5, 'wacc': 7.8,
      'evEbitda': 16.2, 'assetTurnover': 1.35,
      'moat': 'Submarine HVDC power transmission cable monopoly, offshore wind grid interconnection exclusivity, and high-voltage utility distribution equipment approvals.',
      'soicMetrics': [
        { 'label': 'US Grid Capex 2026E', 'value': '$38B annual transmission spend' },
        { 'label': 'HVDC Subsea Lead Times', 'value': '48 Months order backlog' },
        { 'label': 'Utility Modernization Spend', 'value': 'Aging grid replacement cycle across 3,000 utilities' },
        { 'label': 'Data Center Interconnects', 'value': 'Multi-gigawatt substation supply contracts' },
        { 'label': 'Domestic Production Premium', 'value': 'Buy America compliance advantages' }
      ],
      'representativeFirms': ['Prysmian Group (US/Milan)', 'Hubbell Inc'],
      'firmKeys': ['prysmian_us', 'hubbell']
    },
    'energy_us': {
      'name': 'Integrated Supermajor Hydrocarbons & LNG Export (US)', 'country': 'us',
      'betaU': 0.82, 'betaL': 0.95, 'opm': 18.5, 'roic': 19.2, 'wacc': 7.5,
      'evEbitda': 7.2, 'assetTurnover': 0.85,
      'moat': 'Permian Basin low breakeven lifting costs (< $35/bbl), integrated refining-chemical complexes on the Gulf Coast, and 20-year take-or-pay LNG export liquefaction contracts.',
      'soicMetrics': [
        { 'label': 'Gulf Coast 3-2-1 Crack', 'value': '$22.50 / bbl refining spread' },
        { 'label': 'Permian Breakeven', 'value': '< $35 / bbl WTI profitable drilling' },
        { 'label': 'LNG Export Capacity', 'value': 'Over 85 Million MTPA US export capability' },
        { 'label': 'Dividend Aristocrat History', 'value': '40+ consecutive years of dividend growth' },
        { 'label': 'Upstream Free Cash Flow', 'value': '$45+ Billion annual cash generation' }
      ],
      'representativeFirms': ['ExxonMobil Corporation', 'Chevron Corporation', 'Cheniere Energy Inc', 'ConocoPhillips'],
      'firmKeys': ['exxon', 'chevron', 'cheniere', 'conocophillips']
    },

    # ── GERMANY (3 Sectors) ──
    'auto_de': {
      'name': 'Automotive & Heavy Industry (Germany)', 'country': 'germany',
      'betaU': 0.90, 'betaL': 1.25, 'opm': 8.5, 'roic': 12.0, 'wacc': 7.2,
      'evEbitda': 6.8, 'assetTurnover': 0.95,
      'moat': 'Precision mechanical engineering, century-old luxury heritage brand equity (Mercedes-Benz, BMW, Porsche), and massive automated Industry 4.0 assembly complexes.',
      'soicMetrics': [
        { 'label': 'EV Platform Capex', 'value': '€45B through 2028' },
        { 'label': 'Luxury Pricing Power', 'value': 'Average selling price €72,000+ per vehicle' },
        { 'label': 'Industrial Liquidity', 'value': '€31B+ net cash across German OEMs' },
        { 'label': 'Software-Defined Vehicle (SDV)', 'value': 'MB.OS & Neue Klasse autonomous architectures' },
        { 'label': 'Dividend Yield Benchmark', 'value': '6.5% - 8.2% cash distribution yields' }
      ],
      'representativeFirms': ['Mercedes-Benz Group AG', 'Bayerische Motoren Werke (BMW)', 'Volkswagen AG'],
      'firmKeys': ['mercedes', 'bmw', 'volkswagen']
    },
    'automation_de': {
      'name': 'Industrial Automation & Robotics (Germany)', 'country': 'germany',
      'betaU': 0.82, 'betaL': 0.95, 'opm': 14.2, 'roic': 18.5, 'wacc': 6.8,
      'evEbitda': 16.5, 'assetTurnover': 1.15,
      'moat': 'PLC automation industrial standards (Siemens Simatic), Industry 4.0 digital twin dominance (Teamcenter, NX), and warehouse intralogistics robotics (Dematic).',
      'soicMetrics': [
        { 'label': 'Factory Software Backlog', 'value': '€112B multi-year order backlog' },
        { 'label': 'Defect Rate in Manufacturing', 'value': '11 DPM (Near-zero manufacturing defects)' },
        { 'label': 'Industrial Software ARR', 'value': '€4.2B annual recurring software revenue' },
        { 'label': 'Ecosystem Integration', 'value': 'Standardized across 100,000+ global factories' },
        { 'label': 'Operating Margin Run-Rate', 'value': '15.4% core digital industries margin' }
      ],
      'representativeFirms': ['Siemens AG', 'KION Group AG'],
      'firmKeys': ['siemens', 'kion']
    },
    'chem_de': {
      'name': 'Chemical Conglomerates (Germany)', 'country': 'germany',
      'betaU': 0.75, 'betaL': 0.92, 'opm': 9.8, 'roic': 11.5, 'wacc': 7.0,
      'evEbitda': 8.2, 'assetTurnover': 0.88,
      'moat': 'Verbund site integration (10 sq km Ludwigshafen), closed-loop thermal and material recycling, and high-barrier specialty life sciences patent portfolios.',
      'soicMetrics': [
        { 'label': 'Energy Cost Hedge', 'value': 'Long-term renewable power purchase agreements' },
        { 'label': 'Verbund Cost Savings', 'value': '€1.2B annual internal logistical cost avoidance' },
        { 'label': 'Zhanjiang Mega Project', 'value': '€10B smart Verbund site in Guangdong, China' },
        { 'label': 'Agricultural Solution Share', 'value': 'Global top-3 crop protection formulations' },
        { 'label': 'Free Cash Flow Flow-Through', 'value': '€3.5B+ annual operational cash flow' }
      ],
      'representativeFirms': ['BASF SE', 'Bayer AG'],
      'firmKeys': ['basf', 'bayer']
    },

    # ── JAPAN (3 Sectors) ──
    'semi_jp': {
      'name': 'Semiconductor Equipment & Materials (Japan)', 'country': 'japan',
      'betaU': 0.98, 'betaL': 1.05, 'opm': 28.5, 'roic': 26.5, 'wacc': 6.2,
      'evEbitda': 18.5, 'assetTurnover': 0.95,
      'moat': 'Global monopolies in semiconductor manufacturing steps: Coater/Developers (90% TEL), Actinic EUV Photomask Inspection (100% Lasertec), and Memory ATE Testers (55% Advantest).',
      'soicMetrics': [
        { 'label': 'EUV Inspection Monopoly', 'value': '100% market share on actinic blank inspection' },
        { 'label': 'HBM Memory Tester Share', 'value': 'Over 75% share of HBM3E high-speed test systems' },
        { 'label': 'Net Cash Balance Sheets', 'value': 'Zero net debt with massive cash balances' },
        { 'label': 'Operating Profit Margins', 'value': '28% - 38% across top equipment makers' },
        { 'label': 'R&D Reinvestment Rate', 'value': '12.5% of sales reinvested in advanced physics' }
      ],
      'representativeFirms': ['Tokyo Electron Ltd', 'Advantest Corp', 'Lasertec Corp'],
      'firmKeys': ['tel', 'advantest', 'lasertec']
    },
    'precision_jp': {
      'name': 'Factory Precision Automation, Robotics & Sensors (Japan)', 'country': 'japan',
      'betaU': 0.85, 'betaL': 0.92, 'opm': 42.0, 'roic': 28.5, 'wacc': 5.8,
      'evEbitda': 22.5, 'assetTurnover': 0.65,
      'moat': 'Direct-sales model without middlemen, 50%+ operating margins, 99.5% same-day sensor shipment, and yellow autonomous robot assembly forests at Mount Fuji.',
      'soicMetrics': [
        { 'label': 'Keyence Operating Margin', 'value': '52.4% world-record operating margin' },
        { 'label': 'Direct-Sales Field Engineers', 'value': 'Problem solvers visiting factories directly' },
        { 'label': 'Cash Reserves', 'value': '¥2.8 Trillion ($18B) pristine liquid net cash' },
        { 'label': 'CNC Global Share', 'value': '65% of world machine tool CNC controllers' },
        { 'label': 'Lights-Out Factories', 'value': 'Robots manufacturing robots unmanned for 30 days' }
      ],
      'representativeFirms': ['Keyence Corporation', 'Fanuc Corp'],
      'firmKeys': ['keyence', 'fanuc']
    },
    'sogo_jp': {
      'name': 'Sogo Shosha Conglomerate Trading Houses (Japan)', 'country': 'japan',
      'betaU': 0.78, 'betaL': 0.88, 'opm': 8.5, 'roic': 14.8, 'wacc': 5.5,
      'evEbitda': 7.5, 'assetTurnover': 1.05,
      'moat': 'Global trade infrastructure, resource concessions (LNG, coking coal, copper), Berkshire Hathaway 9%+ endorsement, and steady ROE expansion above 14%.',
      'soicMetrics': [
        { 'label': 'Berkshire Hathaway Stake', 'value': 'Warren Buffett 9%+ strategic equity ownership' },
        { 'label': 'Global Operating Affiliates', 'value': 'Over 1,700 subsidiaries across 90 countries' },
        { 'label': 'Metallurgical Coal Concession', 'value': 'World lowest-cost coking coal export mines' },
        { 'label': 'Dividend Payout Target', 'value': 'Progressive dividend policy with active buybacks' },
        { 'label': 'Non-Resource Net Income', 'value': '75%+ diversified consumer and industrial profit' }
      ],
      'representativeFirms': ['Mitsubishi Corporation', 'Mitsui & Co Ltd', 'Itochu Corporation'],
      'firmKeys': ['mitsubishi', 'mitsui', 'itochu']
    },

    # ── CHINA (3 Sectors) ──
    'ev_cn': {
      'name': 'New Energy Vehicles, Lithium Batteries & Power Grid (China)', 'country': 'china',
      'betaU': 1.05, 'betaL': 1.18, 'opm': 10.5, 'roic': 21.0, 'wacc': 6.5,
      'evEbitda': 13.5, 'assetTurnover': 1.25,
      'moat': 'Massive vertical integration, Blade battery safety, lowest cell cost per kWh globally ($55/kWh), and 4.2 million vehicle annual manufacturing capacity.',
      'soicMetrics': [
        { 'label': 'Global EV Battery Share', 'value': 'CATL 37.5% + BYD 16% = 53.5% global dominance' },
        { 'label': 'Annual NEV Production', 'value': '4.2 Million vehicles / year BYD volume run-rate' },
        { 'label': 'LFP Battery Cell Cost', 'value': '< $55 / kWh packs at cell level' },
        { 'label': 'Export Ro-Ro Fleet', 'value': 'Dedicated 7,000-vehicle car carrier ships' },
        { 'label': 'Free Cash Flow Conversion', 'value': 'Massive negative working capital floats' }
      ],
      'representativeFirms': ['BYD Company Ltd', 'CATL (Contemporary Amperex)'],
      'firmKeys': ['byd', 'catl']
    },
    'solar_cn': {
      'name': 'Photovoltaic Solar Modules, Inverters & Cleantech (China)', 'country': 'china',
      'betaU': 1.12, 'betaL': 1.25, 'opm': 14.8, 'roic': 18.5, 'wacc': 6.8,
      'evEbitda': 9.2, 'assetTurnover': 1.10,
      'moat': 'Global scale monopolies in silicon ingot pulling, wafer slicing, HPBC 2.0 back-contact solar cell efficiency (26.6%), and utility-scale grid-forming inverters.',
      'soicMetrics': [
        { 'label': 'Global Solar Wafer Share', 'value': 'Over 85% of global wafers produced in China' },
        { 'label': 'Inverter Global Share', 'value': 'Sungrow #1 inverter & BESS supplier globally' },
        { 'label': 'Module Conversion Efficiency', 'value': '26.6% mass production HPBC cell efficiency' },
        { 'label': 'LCOE of Solar Power', 'value': '< $0.02 / kWh generation cost in sunny geographies' },
        { 'label': 'Energy Storage Deployments', 'value': 'PowerTitan utility battery grid integration' }
      ],
      'representativeFirms': ['LONGi Green Energy Technology', 'Sungrow Power Supply Co'],
      'firmKeys': ['longi', 'sungrow']
    },
    'ship_cn': {
      'name': 'Heavy Commercial Shipbuilding & Dual-Fuel Fleets (China)', 'country': 'china',
      'betaU': 0.88, 'betaL': 1.10, 'opm': 11.5, 'roic': 14.8, 'wacc': 6.2,
      'evEbitda': 12.0, 'assetTurnover': 0.85,
      'moat': 'Dual-fuel VLCC and mega-container ship order backlogs through 2029, colossal drydocks at Changxing Island, and massive advance customer cash payments.',
      'soicMetrics': [
        { 'label': 'Order Book Coverage', 'value': '4.5 Years forward drydock reservation through 2029' },
        { 'label': 'Dual-Fuel Containerships', 'value': 'Building 24,000 TEU mega-vessels for global liners' },
        { 'label': 'Advance Stage Payments', 'value': 'Negative working capital funded by foreign shipowners' },
        { 'label': 'Container Fleet TEU Size', 'value': 'COSCO 3.2 Million TEU operating fleet' },
        { 'label': 'Net Cash Position', 'value': 'Tens of billions in liquid maritime treasury cash' }
      ],
      'representativeFirms': ['China CSSC Holdings Ltd', 'COSCO SHIPPING Holdings'],
      'firmKeys': ['cssc', 'cosco']
    },

    # ── BRAZIL (2 Sectors) ──
    'oil_br': {
      'name': 'Offshore Deepwater Pre-Salt Crude (Brazil)', 'country': 'brazil',
      'betaU': 0.95, 'betaL': 1.35, 'opm': 32.5, 'roic': 22.0, 'wacc': 13.5,
      'evEbitda': 4.5, 'assetTurnover': 0.72,
      'moat': 'Santos Basin ultra-deepwater lifting costs < $28/bbl, world-class reservoir permeability, and massive FPSO extraction capacity.',
      'soicMetrics': [
        { 'label': 'Lifting Cost / Barrel', 'value': '$26.80 / bbl Santos Basin pre-salt breakeven' },
        { 'label': 'FPSO Extraction Fleet', 'value': 'Búzios, Mero & Tupi ultra-deepwater vessels' },
        { 'label': 'Daily Crude Production', 'value': '2.8 Million barrels / day pre-salt extraction' },
        { 'label': 'Dividend Payout Formula', 'value': '45% of free cash flow distributed as dividends' },
        { 'label': 'P/E Valuation Multiple', 'value': '4.2x deeply discounted cash generator' }
      ],
      'representativeFirms': ['Petróleo Brasileiro S.A. (Petrobras)'],
      'firmKeys': ['petrobras']
    },
    'agri_br': {
      'name': 'Iron Ore & Agribusiness (Brazil)', 'country': 'brazil',
      'betaU': 0.92, 'betaL': 1.15, 'opm': 38.5, 'roic': 24.5, 'wacc': 14.0,
      'evEbitda': 5.2, 'assetTurnover': 0.85,
      'moat': 'Carajás high-grade 65% Fe iron ore natural geological endowment, double-cropping agricultural efficiency, and vast arable Cerrado farmland.',
      'soicMetrics': [
        { 'label': 'Cash Cost FOB Iron Ore', 'value': '$22.40 / ton Carajás S11D cash cost' },
        { 'label': 'Iron Ore Fe Purity', 'value': '65.4% natural high-grade direct charge ore' },
        { 'label': 'Arable Farm Land Area', 'value': '700,000+ hectares under precision double-cropping' },
        { 'label': 'Global Grain Export Share', 'value': 'Brazil #1 exporter of soybeans and corn globally' },
        { 'label': 'Truckless Conveyor System', 'value': 'Electrified in-pit transport cutting diesel costs' }
      ],
      'representativeFirms': ['Vale S.A.', 'SLC Agrícola S.A.'],
      'firmKeys': ['vale', 'slc_agri']
    },

    # ── UK & EUROPE (2 Sectors) ──
    'fin_uk': {
      'name': 'Global Banking & Wealth Management (United Kingdom)', 'country': 'uk',
      'betaU': 0.85, 'betaL': 1.25, 'opm': 34.2, 'roic': 14.5, 'wacc': 7.8,
      'evEbitda': 7.8, 'assetTurnover': 0.12,
      'moat': 'London global financial center clearing, foreign exchange trading liquidity, Asian trade corridor dominance (Hong Kong/Singapore), and CET-1 capital buffers.',
      'soicMetrics': [
        { 'label': 'Common Equity Tier 1 (CET1)', 'value': '15.2% regulatory capital buffer' },
        { 'label': 'Trade Finance Leadership', 'value': '#1 global trade bank in Asia and Europe' },
        { 'label': 'Dividend & Buyback Yield', 'value': '8.5% total capital return yield' },
        { 'label': 'Net Interest Margin', 'value': '1.62% - 1.85% wholesale & retail spreads' },
        { 'label': 'Global Wealth Management AUM', 'value': '$1.8 Trillion affluent customer balances' }
      ],
      'representativeFirms': ['HSBC Holdings plc', 'Barclays PLC'],
      'firmKeys': ['hsbc', 'barclays']
    },
    'pharma_uk': {
      'name': 'Innovative Pharmaceuticals, GLP-1 & EUV Lithography (Europe / UK)', 'country': 'uk',
      'betaU': 0.70, 'betaL': 0.78, 'opm': 38.5, 'roic': 34.0, 'wacc': 7.2,
      'evEbitda': 22.5, 'assetTurnover': 0.75,
      'moat': 'Global monopolies and duopolies: ASML 100% EUV lithography monopoly, Novo Nordisk GLP-1 weight-loss duopoly, AstraZeneca targeted oncology blockbusters.',
      'soicMetrics': [
        { 'label': 'EUV Lithography Monopoly', 'value': 'ASML 100% market share on advanced chip manufacturing' },
        { 'label': 'GLP-1 Weight Loss TAM', 'value': '$100B+ global obesity market by 2030' },
        { 'label': 'Oncology Drug Pipeline', 'value': '28 Phase-III molecules in clinical development' },
        { 'label': 'Gross Profit Margins', 'value': '82% - 88% on patent-protected therapeutics' },
        { 'label': 'Return on Capital Employed', 'value': '45%+ ROCE on advanced lithography and biologics' }
      ],
      'representativeFirms': ['AstraZeneca PLC', 'Novo Nordisk A/S', 'ASML Holding NV'],
      'firmKeys': ['astrazeneca', 'novo', 'asml']
    },

    # ── SAUDI ARABIA (1 Sector) ──
    'energy_sa': {
      'name': 'Integrated Hydrocarbons & Petrochemicals (Saudi Arabia)', 'country': 'saudi',
      'betaU': 0.75, 'betaL': 0.85, 'opm': 44.5, 'roic': 28.5, 'wacc': 6.8,
      'evEbitda': 7.2, 'assetTurnover': 0.85,
      'moat': 'Ghawar field onshore crude with lowest lifting cost globally ($3.20/bbl), captive subsidized ethane feedstocks for SABIC, and sovereign balance sheet fortress.',
      'soicMetrics': [
        { 'label': 'Upstream Lifting Cost', 'value': '$3.20 / bbl (Lowest cost crude on earth)' },
        { 'label': 'Maximum Sustainable Capacity', 'value': '12.0 Million barrels / day crude capacity' },
        { 'label': 'Petrochemical Feedstock Margin', 'value': 'Fixed-price ethane feedstocks at massive global discount' },
        { 'label': 'Annual Free Cash Flow', 'value': 'Over $100 Billion generated annually' },
        { 'label': 'Base Dividend Guarantee', 'value': '$31 Billion quarterly base and performance payouts' }
      ],
      'representativeFirms': ['Saudi Arabian Oil Co (Saudi Aramco)', 'SABIC'],
      'firmKeys': ['aramco', 'sabic']
    },

    # ── SINGAPORE (1 Sector) ──
    'trade_sg': {
      'name': 'Global Maritime Hub & Trade Infrastructure (Singapore)', 'country': 'singapore',
      'betaU': 0.72, 'betaL': 0.85, 'opm': 26.5, 'roic': 18.5, 'wacc': 5.8,
      'evEbitda': 14.2, 'assetTurnover': 0.95,
      'moat': 'Tuas mega-port transshipment logistics, subsea cable landing station chokepoint, Temasek sovereign ownership, and Asian agri-processing processing hubs.',
      'soicMetrics': [
        { 'label': 'Container Throughput', 'value': '39.0M TEUs/year through Singapore seaport' },
        { 'label': 'Subsea Cable Connectivity', 'value': 'Over 25 major international subsea cable systems terminating' },
        { 'label': 'Palm Oil Refining Capacity', 'value': 'Largest edible oil processor in Asia-Pacific' },
        { 'label': 'Sovereign Credit Rating', 'value': 'AAA pristine sovereign stability and zero-tax maritime regime' },
        { 'label': 'Regional Data Center Capacity', 'value': 'Over 1 Gigawatt active enterprise data center capacity' }
      ],
      'representativeFirms': ['Singapore Telecommunications (Singtel)', 'Wilmar International Ltd'],
      'firmKeys': ['singtel', 'wilmar']
    },

    # ── AUSTRALIA (1 Sector) ──
    'mining_au': {
      'name': 'Critical Minerals, Iron Ore & Copper Extraction (Australia)', 'country': 'australia',
      'betaU': 0.88, 'betaL': 1.05, 'opm': 42.0, 'roic': 26.0, 'wacc': 8.2,
      'evEbitda': 6.5, 'assetTurnover': 0.88,
      'moat': 'Pilbara low-cost rail-to-port infrastructure (AutoHaul autonomous trains), Olympic Dam multi-metal mega-deposit, and Tier-1 copper reserves.',
      'soicMetrics': [
        { 'label': 'Iron Ore FOB Cost', 'value': '$18.50 / ton Pilbara rail-to-port cost' },
        { 'label': 'Olympic Dam Reserve Size', 'value': 'World largest known single uranium and copper deposit' },
        { 'label': 'Autonomous Heavy Rail', 'value': '1,700km driverless heavy-haul rail network' },
        { 'label': 'Operating Cash Flow', 'value': '$20+ Billion annual operating cash generation' },
        { 'label': 'Copper Production Growth', 'value': 'Over 1.8 Million tons copper per year' }
      ],
      'representativeFirms': ['BHP Group Ltd', 'Rio Tinto Ltd'],
      'firmKeys': ['bhp', 'rio']
    },

    # ── SOUTH KOREA (1 Sector) ──
    'memory_kr': {
      'name': 'Advanced HBM3E Memory, DRAM & Foundry (South Korea)', 'country': 'korea',
      'betaU': 1.10, 'betaL': 1.18, 'opm': 26.5, 'roic': 22.5, 'wacc': 6.8,
      'evEbitda': 11.2, 'assetTurnover': 0.95,
      'moat': 'High-Bandwidth Memory (HBM3E) mass reflow packaging monopoly for NVIDIA, global DRAM duopoly (75%+ combined share), and GigaFab cleanrooms at Pyeongtaek.',
      'soicMetrics': [
        { 'label': 'HBM Global Market Share', 'value': 'SK Hynix 53% + Samsung 42% = 95% global AI memory monopoly' },
        { 'label': 'Cleanroom Footprint', 'value': 'Pyeongtaek Campus equivalent to 400 football fields' },
        { 'label': 'EUV DRAM Manufacturing', 'value': '1b-nanometer DRAM utilizing ASML EUV lithography' },
        { 'label': 'Liquid Net Cash Balance', 'value': '$85+ Billion cash buffer at Samsung Electronics' },
        { 'label': 'Operating Margin Expansion', 'value': 'HBM3E operating margins approaching 45%' }
      ],
      'representativeFirms': ['Samsung Electronics Co Ltd', 'SK Hynix Inc'],
      'firmKeys': ['samsung', 'sk_hynix']
    },

    # ── UAE (1 Sector) ──
    'logistics_ae': {
      'name': 'Global Air Transit & Marine Port Terminals (UAE)', 'country': 'uae',
      'betaU': 0.82, 'betaL': 1.05, 'opm': 21.0, 'roic': 17.5, 'wacc': 6.5,
      'evEbitda': 10.8, 'assetTurnover': 1.12,
      'moat': 'Dubai global transit crossroad connecting East and West, Jebel Ali mega-harbor (19M TEUs) with adjacent JAFZA free zone, and lowest-cost airline seat-km economics.',
      'soicMetrics': [
        { 'label': 'Transit Passenger Volume', 'value': '87.0M passengers/yr through Dubai hub' },
        { 'label': 'Jebel Ali Container Capacity', 'value': '19.3 Million TEUs deepwater automated port capacity' },
        { 'label': 'JAFZA Free Zone Tenants', 'value': '9,500+ multinational companies from 140 countries' },
        { 'label': 'Low-Cost Airline Seat Margin', 'value': 'Air Arabia 26.8% operating margin' },
        { 'label': 'Sovereign Port Concessions', 'value': '82 marine terminals across 40 countries globally' }
      ],
      'representativeFirms': ['DP World Ltd', 'Air Arabia PJSC'],
      'firmKeys': ['dpworld', 'airarabia']
    }
}

print(f"Total defined sectors in SECTORS: {len(SECTORS)}")

