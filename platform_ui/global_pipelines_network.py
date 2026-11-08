"""
Global Energy Pipelines Network (Gas, Crude & Trans-Continental Arteries)
Comprehensive worldwide dataset covering India (GAIL, IOCL), Middle East & GCC (Aramco, Dolphin, OQGN),
Europe & Mediterranean (TransMed, Baltic Pipe, TAP, MEG), Asia-Pacific (PipeChina, Power of Siberia),
and the Americas (Keystone, TAPS, Transco, Colonial).
"""

GLOBAL_GAS_PIPELINES = [
    # ── INDIA (GAIL, PIL, EASTERN & SOUTHERN GRIDS) ──
    {
        "id": "gas_gail_hvj",
        "name": "GAIL HVJ (Hazira-Vijaipur-Jagdishpur) National Gas Grid",
        "holding_co": "GAIL (India) Limited",
        "type": "National Arterial Gas Backbone",
        "capacity": "33.4 MMSCMD (~1.2 Bcf/d)",
        "length": "3,474 km",
        "status": "In Service / Flowing (India National Grid)",
        "scope": "india",
        "color": "#00e5ff",
        "coords": [
            [21.17, 72.73],  # Hazira LNG Terminal (Gujarat)
            [22.31, 73.18],  # Vadodara
            [23.58, 75.83],  # Ujjain
            [24.42, 77.30],  # Vijaipur Compressor Station (MP)
            [25.18, 75.83],  # Kota
            [26.47, 81.60],  # Jagdishpur (UP)
            [27.18, 78.01],  # Agra
            [28.27, 78.43],  # Babrala
            [28.55, 77.55]   # Dadri National Gas Hub
        ]
    },
    {
        "id": "gas_urja_ganga",
        "name": "Pradhan Mantri Urja Ganga (JHBDPL Pipeline)",
        "holding_co": "GAIL (India) Limited",
        "type": "Eastern India Arterial Gas Grid",
        "capacity": "16.0 MMSCMD",
        "length": "2,655 km",
        "status": "In Service / Full Commercial Flow",
        "scope": "india",
        "color": "#38bdf8",
        "coords": [
            [26.47, 81.60],  # Jagdishpur (UP)
            [25.32, 82.97],  # Varanasi
            [25.59, 85.14],  # Patna (Bihar)
            [24.79, 85.00],  # Gaya
            [23.67, 86.15],  # Bokaro Steel City (Jharkhand)
            [22.06, 88.06],  # Haldia Petrochemicals (WB)
            [20.80, 86.97]   # Dhamra LNG Regas Terminal (Odisha)
        ]
    },
    {
        "id": "gas_pil_east_west",
        "name": "Kakinada-Hyderabad-Uran (PIL East-West Pipeline)",
        "holding_co": "Pipeline Infrastructure Ltd (Brookfield / RIL)",
        "type": "Trans-Peninsular Interstate Trunkline",
        "capacity": "80.0 MMSCMD (2.8 Bcf/d)",
        "length": "1,480 km",
        "status": "In Service / Flowing (KG-D6 Basin Arterial)",
        "scope": "india",
        "color": "#06b6d4",
        "coords": [
            [16.98, 82.24],  # Kakinada KG-D6 Gas Landfall
            [17.00, 81.80],  # Rajahmundry
            [16.51, 80.64],  # Vijayawada
            [17.38, 78.48],  # Hyderabad
            [17.66, 75.90],  # Solapur
            [18.52, 73.85],  # Pune
            [18.88, 72.94]   # Uran Gas Terminal (Mumbai)
        ]
    },
    {
        "id": "gas_dabhol_bangalore",
        "name": "Dabhol-Bangalore Natural Gas Pipeline",
        "holding_co": "GAIL (India) Limited",
        "type": "Southern Industrial Gas Corridor",
        "capacity": "16.0 MMSCMD",
        "length": "1,000 km",
        "status": "In Service / Flowing",
        "scope": "india",
        "color": "#22d3ee",
        "coords": [
            [17.58, 73.16],  # Dabhol LNG Terminal
            [15.85, 74.50],  # Belgaum
            [15.46, 75.01],  # Dharwad / Hubli
            [14.46, 75.92],  # Davanagere
            [13.34, 77.10],  # Tumkur
            [12.97, 77.59]   # Bangalore Industrial Hub
        ]
    },

    # ── MIDDLE EAST & GCC (ARAMCO, DOLPHIN, OQGN) ──
    {
        "id": "gas_dolphin_gcc",
        "name": "Dolphin Gas Pipeline (Qatar-UAE-Oman)",
        "holding_co": "Dolphin Energy (Mubadala 51%, TotalEnergies, Oxy)",
        "type": "Cross-Border Subsea Strategic Trunkline",
        "capacity": "3.2 Bcf/d (90 MMSCMD)",
        "length": "364 km Subsea + 200 km Overland",
        "status": "In Service / Strategic GCC Energy Flow",
        "scope": "gcc",
        "color": "#ffaa00",
        "coords": [
            [25.92, 51.53],  # Ras Laffan Industrial City (Qatar)
            [25.40, 52.80],  # Persian Gulf Subsea Route
            [24.77, 54.72],  # Taweelah Receiving Station (Abu Dhabi)
            [24.21, 55.76],  # Al Ain
            [25.29, 56.36],  # Qidfa / Fujairah Bunkering Hub
            [24.25, 55.80]   # Buraimi Delivery (Oman Border)
        ]
    },
    {
        "id": "gas_aramco_mgs",
        "name": "Saudi Aramco Master Gas System (MGS Arterial)",
        "holding_co": "Saudi Aramco (Aramco Gas Pipelines Co)",
        "type": "Kingdom-Wide Industrial Energy Grid",
        "capacity": "12.5 Bcf/d (Expanding to 15.0 Bcf/d)",
        "length": "4,000+ km",
        "status": "In Service / Flowing (Yanbu & Riyadh Supply)",
        "scope": "gcc",
        "color": "#f59e0b",
        "coords": [
            [25.68, 49.50],  # Shedgum Gas Plant
            [25.13, 49.33],  # Uthmaniyah Gas Plant
            [24.89, 49.25],  # Hawiyah NGL & Gas Center
            [24.55, 46.85],  # Riyadh 2nd Industrial City
            [24.50, 44.40],  # Al Duwadimi Pumping Node
            [23.90, 42.92],  # Afif
            [24.09, 38.06]   # Yanbu King Fahd Industrial Port (Red Sea)
        ]
    },
    {
        "id": "gas_oqgn_oman",
        "name": "Oman National Gas Transmission Grid (OQGN)",
        "holding_co": "OQ Gas Networks SAOG",
        "type": "Sultanate National Gas Grid",
        "capacity": "130 MMSCMD",
        "length": "4,030 km",
        "status": "In Service / Regulated Monopolist",
        "scope": "gcc",
        "color": "#fbbf24",
        "coords": [
            [22.35, 56.49],  # Fahud Central Gas Processing Hub
            [21.32, 56.88],  # Saih Nihayda Gas Plant
            [22.56, 59.52],  # Oman LNG Qalhat Complex (Sur)
            [24.50, 56.63],  # Sohar Industrial Port & Freezone
            [17.02, 54.09]   # Salalah Free Zone Delivery
        ]
    },

    # ── EUROPE & MEDITERRANEAN (TRANSMED, BALTIC PIPE, TAP, MEG) ──
    {
        "id": "gas_transmed",
        "name": "Trans-Mediterranean Gas Pipeline (TransMed / Enrico Mattei)",
        "holding_co": "Eni S.p.A. / Sonatrach",
        "type": "Deepwater Subsea Trans-Continental Trunkline",
        "capacity": "30.2 Bcm/y (3.0 Bcf/d)",
        "length": "2,475 km",
        "status": "In Service / High Utilization Flow",
        "scope": "europe",
        "color": "#a855f7",
        "coords": [
            [32.93, 3.27],   # Hassi R'Mel Gas Field (Algeria)
            [35.25, 8.45],   # Oued Saf-Saf (Algeria/Tunisia Border)
            [37.08, 11.05],  # Cap Bon (Tunisia Coast)
            [37.50, 11.90],  # Strait of Sicily Deepwater Subsea
            [37.65, 12.59],  # Mazara del Vallo (Sicily Landfall)
            [38.19, 15.55],  # Messina Strait Crossing
            [41.90, 12.50],  # Rome Central Grid Hub
            [44.62, 11.48]   # Minerbio Hub (Po Valley / Milan Industrial)
        ]
    },
    {
        "id": "gas_baltic_pipe",
        "name": "Baltic Pipe System (Norway-Denmark-Poland)",
        "holding_co": "Energinet (Denmark) & Gaz-System (Poland)",
        "type": "Strategic North Sea Diversification Arterial",
        "capacity": "10.0 Bcm/y (1.0 Bcf/d)",
        "length": "900 km",
        "status": "In Service / Flowing",
        "scope": "europe",
        "color": "#818cf8",
        "coords": [
            [55.70, 6.50],   # Europipe II Tie-in (North Sea)
            [55.75, 8.18],   # Blabjerg Landfall (Denmark)
            [55.58, 8.55],   # Nybro Gas Treatment Plant
            [55.25, 12.15],  # Faxe South Baltic Sea Entry
            [54.80, 13.90],  # Baltic Sea Deepwater
            [54.08, 15.12],  # Pogorzelica Landfall (Poland)
            [53.56, 14.83]   # Goleniow Gas Compressor Hub
        ]
    },
    {
        "id": "gas_tap_pipeline",
        "name": "Trans Adriatic Pipeline (TAP / Southern Gas Corridor)",
        "holding_co": "TAP AG (bp, SOCAR, Snam, Fluxys, Enagas)",
        "type": "Caspian-to-Europe Strategic Interconnector",
        "capacity": "10.0 Bcm/y (Expandable to 20.0 Bcm/y)",
        "length": "878 km",
        "status": "In Service / Continuous Baseline Flow",
        "scope": "europe",
        "color": "#c084fc",
        "coords": [
            [40.96, 26.31],  # Kipoi (Greece / Turkey Border Tie-in with TANAP)
            [41.12, 25.40],  # Komotini
            [40.64, 22.94],  # Thessaloniki
            [40.52, 21.26],  # Kastoria
            [40.72, 19.55],  # Fier Compressor (Albania)
            [40.50, 18.80],  # Adriatic Sea Subsea Crossing
            [40.29, 18.39]   # San Foca / Melendugno (Italy Landfall)
        ]
    },

    # ── ASIA-PACIFIC (WEST-EAST, POWER OF SIBERIA, CENTRAL ASIA) ──
    {
        "id": "gas_west_east_china",
        "name": "West-East Gas Pipeline I & II (Tarim to Shanghai)",
        "holding_co": "China Oil & Gas Pipeline Network Corp (PipeChina)",
        "type": "Trans-Continental Asian Mega-Artery",
        "capacity": "30.0 Bcm/y (2.9 Bcf/d)",
        "length": "8,707 km",
        "status": "In Service / Full Load Flow",
        "scope": "asia",
        "color": "#ef4444",
        "coords": [
            [41.75, 84.25],   # Lunnan / Tarim Basin (Xinjiang)
            [42.83, 93.52],   # Hami
            [39.80, 98.28],   # Jiayuguan (Hexi Corridor)
            [36.06, 103.83],  # Lanzhou Hub
            [34.34, 108.94],  # Xi'an
            [30.59, 114.30],  # Wuhan
            [32.06, 118.79],  # Nanjing
            [31.23, 121.47]   # Shanghai Industrial Megacity
        ]
    },
    {
        "id": "gas_power_of_siberia",
        "name": "Power of Siberia Gas Pipeline (Gazprom to CNPC)",
        "holding_co": "Gazprom / PipeChina",
        "type": "Trans-Siberian Megaproject Export Arterial",
        "capacity": "38.0 Bcm/y (3.7 Bcf/d)",
        "length": "3,000 km",
        "status": "In Service / Long-Term Contract Delivery",
        "scope": "asia",
        "color": "#f87171",
        "coords": [
            [59.70, 113.00],  # Chayandinskoye Gas Field (Yakutia)
            [60.72, 114.93],  # Lensk
            [58.60, 125.40],  # Aldan
            [53.98, 123.94],  # Skovorodino
            [50.27, 127.53],  # Blagoveshchensk (Amur Cross-Border)
            [50.24, 127.50],  # Heihe Landfall (China)
            [45.80, 126.53],  # Harbin
            [39.90, 116.40]   # Beijing Municipal Grid
        ]
    },
    {
        "id": "gas_central_asia_china",
        "name": "Central Asia-China Gas Pipeline (Lines A/B/C)",
        "holding_co": "CNPC / KazTransGas / Uzbekneftegaz",
        "type": "Strategic Eurasian Energy Corridor",
        "capacity": "55.0 Bcm/y (5.3 Bcf/d)",
        "length": "1,833 km",
        "status": "In Service / Flowing",
        "scope": "asia",
        "color": "#fb7185",
        "coords": [
            [38.80, 63.80],   # Bagtyyarlyk (Turkmenistan)
            [39.77, 64.42],   # Bukhara (Uzbekistan)
            [41.30, 69.25],   # Tashkent
            [42.32, 69.60],   # Shymkent (Kazakhstan)
            [42.90, 71.37],   # Taraz
            [43.25, 76.95],   # Almaty
            [44.21, 80.41]    # Horgos Land Port (China Border)
        ]
    },

    # ── NORTH AMERICA & AMERICAS (TRANSCO, TGP, ALLIANCE, COPANO) ──
    {
        "id": "gas_transco_us",
        "name": "Transco Pipeline (Transcontinental Gas Pipe Line)",
        "holding_co": "Williams Companies",
        "type": "Interstate Arterial Major",
        "capacity": "17.3 Bcf/d",
        "length": "16,000 km network",
        "status": "In Service / Flowing (Gulf Coast to NYC)",
        "scope": "americas",
        "color": "#00e5ff",
        "coords": [
            [26.1, -97.5],   # South Texas (Brownsville)
            [29.7, -95.3],   # Houston Ship Channel
            [30.4, -91.1],   # Baton Rouge (Louisiana)
            [32.3, -90.2],   # Jackson (Mississippi)
            [33.7, -84.4],   # Atlanta (Georgia)
            [35.2, -80.8],   # Charlotte (North Carolina)
            [37.5, -77.4],   # Richmond (Virginia)
            [39.9, -75.1],   # Philadelphia (Pennsylvania)
            [40.7, -74.0]    # New York City Citygate Hub
        ]
    },
    {
        "id": "gas_tgp_us",
        "name": "Tennessee Gas Pipeline (TGP Interstate)",
        "holding_co": "Kinder Morgan",
        "type": "Interstate Arterial",
        "capacity": "13.9 Bcf/d",
        "length": "19,150 km system",
        "status": "In Service / High Flow",
        "scope": "americas",
        "color": "#38bdf8",
        "coords": [
            [27.8, -97.4],   # Corpus Christi (Texas)
            [30.2, -92.0],   # Lafayette (Louisiana)
            [35.1, -90.0],   # Memphis (Tennessee)
            [38.2, -85.7],   # Louisville (Kentucky)
            [39.9, -82.9],   # Columbus (Ohio)
            [42.3, -71.0]    # Boston / New England Citygate
        ]
    },
    {
        "id": "gas_alliance_us_ca",
        "name": "Alliance Pipeline System (WCSB to Chicago)",
        "holding_co": "Enbridge / Pembina Pipeline",
        "type": "Cross-Border High-Pressure Rich Gas",
        "capacity": "1.6 Bcf/d",
        "length": "3,848 km",
        "status": "In Service / Liquids-Rich Transmission",
        "scope": "americas",
        "color": "#06b6d4",
        "coords": [
            [55.17, -118.80], # Grande Prairie (Alberta / BC)
            [51.05, -114.07], # Calgary
            [50.45, -104.62], # Regina (Saskatchewan)
            [46.87, -96.79],  # Fargo (North Dakota)
            [44.97, -93.26],  # Minneapolis (Minnesota)
            [41.87, -87.62]   # Chicago Hub / Aux Sable NGL Fractionation
        ]
    },
    {
        "id": "gas_copano_us",
        "name": "Copano Pipeline Upper Gulf Coast",
        "holding_co": "Copano Energy LLC / Kinder Morgan",
        "type": "Intrastate Gathering & Transmission",
        "capacity": "1.2 Bcf/d",
        "length": "1,120 km (700 mi)",
        "status": "In Service / Flowing",
        "scope": "americas",
        "color": "#22d3ee",
        "coords": [
            [28.5, -98.3],
            [29.1, -97.2],
            [29.5, -95.8],
            [29.74, -95.12]
        ]
    }
]

GLOBAL_CRUDE_PIPELINES = [
    # ── MIDDLE EAST & GCC (ARAMCO PETROLINE, SUMED, BTC) ──
    {
        "id": "pipe_petroline_saudi",
        "name": "East-West Petroline (Saudi Arabia Trans-Peninsular)",
        "company": "Saudi Aramco",
        "type": "Strategic Trans-Continental Crude Arterial",
        "fuel": "Arabian Light / Extra Light Crude",
        "capacity": "5,000,000 bpd (Expanding to 7.0M bpd)",
        "diameter": "48 / 56 inch Dual Trunklines",
        "length": "1,200 km (745 mi)",
        "status": "In Service / Strategic Hormuz Bypass",
        "scope": "gcc",
        "color": "#00e5ff",
        "coords": [
            [26.27, 50.21],  # Abqaiq World Largest Stabilization Plant
            [25.68, 49.50],  # Shedgum Pumping Station 1
            [25.13, 49.33],  # Uthmaniyah
            [24.55, 46.85],  # Riyadh Pumping Node PS-3
            [24.50, 44.40],  # Al Duwadimi PS-5
            [23.90, 42.92],  # Afif PS-7
            [24.09, 38.06]   # Yanbu Terminal King Fahd Port (Red Sea)
        ]
    },
    {
        "id": "pipe_sumed_egypt",
        "name": "Suez-Mediterranean Pipeline (SUMED)",
        "company": "Arab Petroleum Pipelines Co (Egypt, Saudi, UAE, Kuwait, Qatar)",
        "type": "Strategic Chokepoint Transit Corridor",
        "fuel": "Middle Eastern Export Crude",
        "capacity": "2,500,000 bpd",
        "diameter": "42 inch Dual Lines",
        "length": "320 km (200 mi)",
        "status": "In Service / Suez Canal Parallel Route",
        "scope": "gcc",
        "color": "#38bdf8",
        "coords": [
            [29.58, 32.35],  # Ain Sukhna Red Sea Terminal
            [30.05, 31.23],  # Cairo South Bypass
            [30.85, 30.50],  # Tanta Pumping Station
            [31.12, 29.85]   # Sidi Kerir Mediterranean Offshore Terminal
        ]
    },
    {
        "id": "pipe_btc_caspian",
        "name": "Baku-Tbilisi-Ceyhan (BTC) Pipeline",
        "company": "bp / SOCAR / TPAO / Eni / TotalEnergies",
        "type": "Landlocked Caspian Strategic Export Artery",
        "fuel": "Azeri Light Crude Oil",
        "capacity": "1,200,000 bpd",
        "diameter": "42 / 46 inch",
        "length": "1,768 km (1,099 mi)",
        "status": "In Service / Flowing (Caspian to Mediterranean)",
        "scope": "europe",
        "color": "#06b6d4",
        "coords": [
            [40.30, 49.80],  # Sangachal Terminal (Baku, Azerbaijan)
            [40.68, 46.36],  # Ganja
            [41.69, 44.80],  # Tbilisi (Georgia)
            [41.40, 43.48],  # Borjomi Valley
            [40.75, 42.80],  # Kars (Turkey)
            [39.92, 41.27],  # Erzurum
            [38.75, 37.05],  # Sivas
            [36.88, 35.88]   # Ceyhan Marine Terminal (Mediterranean Sea)
        ]
    },

    # ── INDIA (IOCL SMPPL, HMEL MUNDRA-PANIPAT) ──
    {
        "id": "pipe_iocl_smppl",
        "name": "Salaya-Mathura-Panipat Pipeline (SMPPL)",
        "company": "Indian Oil Corporation Limited (IOCL)",
        "type": "National Strategic Refining Crude Backbone",
        "fuel": "Imported Arab & High-TAN Crude",
        "capacity": "500,000 bpd (25 MMTPA)",
        "diameter": "28 / 32 inch",
        "length": "1,870 km",
        "status": "In Service / Critical Refinery Feeder",
        "scope": "india",
        "color": "#22c55e",
        "coords": [
            [22.31, 69.60],  # Salaya Crude Oil Offshore SPM (Gulf of Kutch)
            [22.82, 70.83],  # Viramgam Crude Oil Storage & Pump Station
            [24.63, 72.85],  # Abu Road
            [26.91, 75.78],  # Jaipur
            [27.49, 77.67],  # Mathura Refinery (IOCL)
            [29.39, 76.96]   # Panipat Refinery & Petrochemical Complex
        ]
    },
    {
        "id": "pipe_mundra_panipat",
        "name": "Mundra-Bathinda Crude Pipeline (HPCL-Mittal Energy / HMEL)",
        "company": "HPCL-Mittal Energy Limited (HMEL)",
        "type": "Dedicated High-Pressure Refinery Trunkline",
        "fuel": "Heavy & Sour Import Crude",
        "capacity": "225,000 bpd (11.3 MMTPA)",
        "diameter": "28 inch",
        "length": "1,017 km",
        "status": "In Service / Guru Gobind Singh Refinery Feeder",
        "scope": "india",
        "color": "#16a34a",
        "coords": [
            [22.83, 69.70],  # Mundra Port SPM & Crude Tank Farm (Gujarat)
            [24.17, 71.43],  # Radhanpur
            [26.23, 73.02],  # Jodhpur
            [28.02, 73.31],  # Bikaner
            [30.21, 74.94]   # Bathinda Guru Gobind Singh Refinery (Punjab)
        ]
    },

    # ── EUROPE & EURASIA (DRUZHBA, CPC, ESPO) ──
    {
        "id": "pipe_druzhba",
        "name": "Druzhba Pipeline System (Friendship Network)",
        "company": "Transneft / PERN / Transpetrol / MERO / MOL",
        "type": "Trans-Continental Arterial Network",
        "fuel": "Urals Export Blend Crude",
        "capacity": "1,400,000 bpd",
        "diameter": "40 / 48 inch",
        "length": "4,000 km (2,500 mi)",
        "status": "Partial Service / Central European Delivery",
        "scope": "europe",
        "color": "#e11d48",
        "coords": [
            [53.20, 50.15],  # Samara Hub (Russia)
            [52.96, 43.15],  # Penza
            [52.58, 31.85],  # Unecha Junction
            [52.43, 30.98],  # Mozyr (Belarus)
            [52.23, 21.01],  # Plock (Poland)
            [53.05, 14.28],  # Schwedt Refinery (Germany)
            [50.08, 14.43],  # Kralupy / Litvinov (Czechia)
            [48.15, 17.11]   # Bratislava Slovnaft / Szazhalombatta (Hungary)
        ]
    },
    {
        "id": "pipe_cpc_caspian",
        "name": "Caspian Pipeline Consortium (CPC)",
        "company": "CPC (Chevron, KazMunayGas, Transneft, ExxonMobil)",
        "type": "Deep inland Landlocked Super-Giant Basin Export",
        "fuel": "CPC Blend High-API Crude",
        "capacity": "1,400,000 bpd (Expanding to 1.65M bpd)",
        "diameter": "40 / 42 inch",
        "length": "1,510 km (938 mi)",
        "status": "In Service / High Flow Black Sea Export",
        "scope": "europe",
        "color": "#f43f5e",
        "coords": [
            [46.10, 53.40],  # Tengiz Super-Giant Field (Kazakhstan)
            [47.10, 51.90],  # Atyrau Hub
            [46.35, 48.05],  # Astrakhan
            [45.03, 38.97],  # Kropotkin Pumping Station
            [44.72, 37.78]   # Yuzhnaya Ozereevka Marine Terminal (Novorossiysk)
        ]
    },

    # ── ASIA-PACIFIC (ESPO, MYANMAR-CHINA) ──
    {
        "id": "pipe_espo_asia",
        "name": "Eastern Siberia-Pacific Ocean (ESPO Pipeline)",
        "company": "Transneft / CNPC",
        "type": "Trans-Asian Pacific Strategic Crude Trunkline",
        "fuel": "ESPO Blend Low-Sulfur Light Sweet Crude",
        "capacity": "1,600,000 bpd (80 MMTPA)",
        "diameter": "48 inch",
        "length": "4,857 km (3,018 mi)",
        "status": "In Service / Full Capacity Flow to China & Pacific",
        "scope": "asia",
        "color": "#d946ef",
        "coords": [
            [55.93, 98.00],   # Taishet (Irkutsk Oblast)
            [56.30, 101.70],  # Bratsk
            [53.98, 123.94],  # Skovorodino Spur (Branch to China)
            [50.40, 127.50],  # Mohe Landfall (China)
            [46.58, 125.00],  # Daqing Refining Hub (China)
            [48.48, 135.07],  # Khabarovsk
            [42.73, 133.02]   # Kozmino Deepwater Pacific Port (Nakhodka)
        ]
    },
    {
        "id": "pipe_myanmar_china",
        "name": "Myanmar-China Crude Oil Pipeline",
        "company": "CNPC (Southeast Asia Crude Oil Pipeline Co)",
        "type": "Strategic Malacca Bypass Pipeline",
        "fuel": "Middle East / African Import Crude",
        "capacity": "440,000 bpd (22 MMTPA)",
        "diameter": "32 inch",
        "length": "771 km (Myanmar section)",
        "status": "In Service / Continuous Malacca Bypass Flow",
        "scope": "asia",
        "color": "#c026d3",
        "coords": [
            [19.35, 93.50],  # Maday Island Deepwater Crude Port (Bay of Bengal)
            [20.15, 94.95],  # Magway Region
            [21.97, 96.08],  # Mandalay
            [22.98, 97.75],  # Lashio
            [24.00, 97.85],  # Ruili Border Station (China)
            [25.04, 102.71]  # Anning Refinery (Kunming, Yunnan)
        ]
    },

    # ── AMERICAS (KEYSTONE, TAPS, ENBRIDGE, COLONIAL, DAPL) ──
    {
        "id": "pipe_keystone",
        "name": "Keystone Pipeline System & Marketlink",
        "company": "TC Energy",
        "type": "Transnational Interstate Mega-Artery",
        "fuel": "Heavy Crude Oil (Western Canadian Select / WCS)",
        "capacity": "620,000 bpd",
        "diameter": "30 / 36 inch",
        "length": "3,456 km (2,147 mi)",
        "status": "In Service / Continuous Baseline Flow",
        "scope": "americas",
        "color": "#00e5ff",
        "coords": [
            [53.54, -113.49], # Hardisty Hub (Alberta, Canada)
            [48.8, -105.5],   # Morgan Border Crossing (MT)
            [44.4, -98.2],    # Steele City Hub (NE)
            [35.9, -96.7],    # Cushing Global Crude Oil Storage Hub (OK)
            [29.98, -93.94]   # Port Arthur / Houston Refining Complex (TX)
        ]
    },
    {
        "id": "pipe_taps",
        "name": "Trans-Alaska Pipeline System (TAPS)",
        "company": "Alyeska Pipeline Service Co (ConocoPhillips, Hilcorp, ExxonMobil)",
        "type": "Arctic Engineering Landmark / Interprovincial",
        "fuel": "Alaska North Slope (ANS) Crude",
        "capacity": "2,140,000 bpd (Currently ~480k bpd)",
        "diameter": "48 inch",
        "length": "1,287 km (800 mi)",
        "status": "In Service / Flowing",
        "scope": "americas",
        "color": "#38bdf8",
        "coords": [
            [70.25, -148.42], # Pump Station 1 (Prudhoe Bay, Arctic Ocean)
            [68.13, -149.48], # Atigun Pass (Continental Divide, Brooks Range)
            [65.48, -148.88], # Yukon River Crossing
            [64.84, -147.72], # Fairbanks
            [61.13, -146.35]  # Valdez Marine Terminal (Prince William Sound)
        ]
    },
    {
        "id": "pipe_enbridge_mainline",
        "name": "Enbridge Mainline System (Line 3/5/61 Corridors)",
        "company": "Enbridge Inc",
        "type": "Cross-Border Primary Refining Arterial",
        "fuel": "Light, Medium & Heavy Crude / Syncrude",
        "capacity": "3,000,000 bpd",
        "diameter": "34 / 36 / 42 inch",
        "length": "5,360 km (3,330 mi)",
        "status": "In Service / Flowing",
        "scope": "americas",
        "color": "#06b6d4",
        "coords": [
            [53.54, -113.49], # Edmonton / Hardisty (AB)
            [50.45, -104.62], # Regina (SK)
            [48.80, -97.24],  # Gretna / Neche Border (ND)
            [46.78, -92.10],  # Superior Terminal (WI)
            [41.58, -87.49],  # Flanagan / Chicago Terminal (IL)
            [42.97, -82.40]   # Sarnia Refining Hub (ON)
        ]
    },
    {
        "id": "pipe_colonial_crude",
        "name": "Colonial Pipeline Trunkline",
        "company": "Colonial Pipeline Co (Koch, KKR, Shell)",
        "type": "Interstate Liquid Fuels Backbone",
        "fuel": "Refined Products & Light Distillates",
        "capacity": "2,500,000 bpd",
        "diameter": "36 / 40 inch",
        "length": "8,850 km (5,500 mi)",
        "status": "In Service / Critical East Coast Telemetry",
        "scope": "americas",
        "color": "#22d3ee",
        "coords": [
            [29.76, -95.36],  # Houston Refining Hub (TX)
            [30.22, -92.02],  # Baton Rouge (LA)
            [32.30, -90.18],  # Collins Tank Farm (MS)
            [33.52, -86.81],  # Birmingham (AL)
            [33.75, -84.39],  # Atlanta Hub (GA)
            [35.23, -80.84],  # Greensboro / Charlotte (NC)
            [37.54, -77.44],  # Richmond (VA)
            [40.66, -74.20]   # Linden / New York Harbor (NJ)
        ]
    },
    {
        "id": "pipe_dapl",
        "name": "Dakota Access Pipeline (DAPL)",
        "company": "Energy Transfer Partners",
        "type": "Interstate Shale Evacuation Trunkline",
        "fuel": "Bakken Light Sweet Crude",
        "capacity": "750,000 bpd",
        "diameter": "30 inch",
        "length": "1,886 km (1,172 mi)",
        "status": "In Service / High Flow",
        "scope": "americas",
        "color": "#38bdf8",
        "coords": [
            [48.15, -103.62], # Stanley (Bakken, ND)
            [46.81, -100.78], # Bismarck (ND)
            [44.37, -99.90],  # Pierre (SD)
            [41.60, -93.61],  # Des Moines (IA)
            [38.76, -89.07]   # Patoka Crude Oil Hub (IL)
        ]
    }
]

