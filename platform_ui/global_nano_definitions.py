# F:\documents\SOIC\EconAgent_Platform\platform_ui\global_nano_definitions.py
# Real Physical Nano Facilities, Manufacturing Complexes, Foundries, Mines & Operations

GLOBAL_NANOS = {
    # ── INDIA NANOS ──
    'halol_mega': {
      'title': '🏭 Polycab Halol Mega Manufacturing Complex (Gujarat)',
      'facilityType': 'Mega Cables & Continuous Cast Copper Rod Complex',
      'parentFirm': 'Polycab India Ltd [POLYCAB:IN]',
      'coords': [22.496, 73.473],
      'specs': [
        { 'label': 'Total Complex Land Area', 'value': '150+ Acres (Halol Industrial Corridor)' },
        { 'label': 'Continuous Cast Copper Rod Mill', 'value': '12,500 MT / month (Properzi Process)' },
        { 'label': 'Extrusion Line Operating Speed', 'value': '850 meters / minute' },
        { 'label': 'Authorized Distribution Hub', 'value': '4,300+ Distributors | 205k Retailers' },
        { 'label': 'Logistics Traffic Gate AIS', 'value': '142 heavy container trailers / day' }
      ],
      'description': "Polycab's flagship manufacturing mother plant. Houses in-house copper cathode smelting furnaces, high-voltage CCV lines, and automated distribution warehouses supplying 79 export destinations globally."
    },
    'kei_plant': {
      'title': '⚡ KEI Silvassa 400kV EHV Extrusion Tower & Sanand Plant',
      'facilityType': 'Extra High Voltage (EHV) Power Cable Facility',
      'parentFirm': 'KEI Industries Ltd [KEI:IN]',
      'coords': [20.272, 73.008],
      'specs': [
        { 'label': 'Vertical CCV Extrusion Tower', 'value': '135 meters height (German Troester Line)' },
        { 'label': 'Voltage Rating Qualification', 'value': 'Up to 400kV EHV Underground Transmission' },
        { 'label': 'Annual Processing Capacity', 'value': '115,000 km Cables | 1,200 MT Wires' },
        { 'label': 'Brugg Cables Swiss IP License', 'value': 'Exclusive Joint Venture & Technology Transfer' }
      ],
      'description': "Specialized heavy infrastructure manufacturing plant producing EHV power cables for metro rail networks, offshore wind farms, and interstate grid corridors under PGCIL."
    },
    'rr_waghodia': {
      'title': '🏭 RR Kabel Waghodia Integrated Cable & Enamelled Wire Complex',
      'facilityType': 'Low-Smoke Zero-Halogen (LSZH) Cable Manufacturing Plant',
      'parentFirm': 'RR Kabel Ltd [RRKABEL:IN]',
      'coords': [22.302, 73.365],
      'specs': [
        { 'label': 'Campus Footprint', 'value': '78 Acres (Waghodia GIDC, Vadodara)' },
        { 'label': 'FireX LSZH Compound Formulation', 'value': 'In-House Proprietary Polymer Compounding' },
        { 'label': 'Global Safety Certifications', 'value': 'UL (USA), BASEC (UK), VDE (Germany)' }
      ],
      'description': "Ultra-modern wire drawing and compounding plant with export certifications to 80+ countries across North America and the European Union."
    },
    'finolex_urse': {
      'title': '🏭 Finolex Cables Urse Optic Fiber & Power Cable Complex',
      'facilityType': 'Optic Fiber Preform Draw & EHV Facility',
      'parentFirm': 'Finolex Cables Ltd [FINCABLES:IN]',
      'coords': [18.728, 73.654],
      'specs': [
        { 'label': 'Optic Fiber Draw Capacity', 'value': '8 Million Fiber Kilometers (FKM) / year' },
        { 'label': 'Copper Communication Cables', 'value': 'Jelly Filled Telecom Cables & LAN Category 6/7' },
        { 'label': 'Energy Source', 'value': 'Onsite 5MW Captive Solar + Wind Hybrid' }
      ],
      'description': "Finolex's Pune manufacturing complex integrating glass preform draw towers, telecommunication fiber cabling, and industrial PVC compound plants."
    },
    'mps_studio': {
      'title': '🏢 MPS Digital Content & Learning Architecture Studio (Bengaluru)',
      'facilityType': 'Scholarly AI Workflow & Digital Learning Hub',
      'parentFirm': 'MPS Ltd [MPSLTD:IN]',
      'coords': [12.971, 77.594],
      'specs': [
        { 'label': 'Scholarly Journal Output', 'value': '2.4 Million Published Academic Pages / year' },
        { 'label': 'AI Workflow Engine', 'value': 'MPS Think360 Platform & Magplus CMS' },
        { 'label': 'Global STM Publisher Client Base', 'value': 'Elsevier, Springer Nature, Wiley, Oxford' }
      ],
      'description': "Core technology and digital publishing operations center delivering high-margin STM editorial architecture, automated XML conversion, and educational platforms."
    },
    'niit_hub': {
      'title': '🏢 NIIT Managed Training Services (MTS) Global Delivery Hub',
      'facilityType': 'Corporate Enterprise L&D Delivery Center (Gurugram)',
      'parentFirm': 'NIIT Learning Systems Ltd [NIITMTS:IN]',
      'coords': [28.459, 77.026],
      'specs': [
        { 'label': 'Fortune 500 Enterprise Contracts', 'value': '84 Multi-Year Master Service Agreements' },
        { 'label': 'Annual Learner Touchpoints', 'value': '1.2 Million Corporate Professionals' },
        { 'label': 'Contract Revenue Visibility', 'value': '$380M Multi-Year Contract Backlog' }
      ],
      'description': "Global operations hub managing end-to-end outsourced corporate learning programs for aerospace, energy, banking, and technology multinationals."
    },
    'veranda_center': {
      'title': '🎓 Veranda Enterprise EdTech & Offline Test Prep Hub (Chennai)',
      'facilityType': 'Omnichannel Test Prep & Software Training Center',
      'parentFirm': 'Veranda Learning Solutions [VERANDA:IN]',
      'coords': [13.082, 80.270],
      'specs': [
        { 'label': 'Physical Centers Across India', 'value': '180+ Hybrid Offline/Online Learning Hubs' },
        { 'label': 'Government Exam Enrollment', 'value': 'Banking, UPSC, TNPSC & SSC Aspirants' }
      ],
      'description': "Regional hub integrating physical test-prep coaching centers with digital content delivery and corporate IT upskilling tracks."
    },
    'navneet_dantej': {
      'title': '📚 Navneet Dantali High-Speed Publication & Educational Complex',
      'facilityType': 'Educational Publishing & Stationery Export Plant',
      'parentFirm': 'Navneet Education Ltd [NAVNETEDUL:IN]',
      'coords': [23.148, 72.583],
      'specs': [
        { 'label': 'High-Speed Web Printing Output', 'value': '1.8 Million Books & Notebooks / day' },
        { 'label': 'State Board Curriculum Coverage', 'value': 'Maharashtra, Gujarat, CBSE & ICSE' }
      ],
      'description': "Automated printing presses and stationery manufacturing facility supplying academic textbooks, supplementary study guides, and export stationery."
    },
    'vapi': {
      'title': '🧪 Pidilite Vapi Synthetic Resin & Adhesives Mega Plant (Gujarat)',
      'facilityType': 'Polymer Compounding, VAM Reaction & Fevicol Plant',
      'parentFirm': 'Pidilite Industries Ltd [PIDILITIND:IN]',
      'coords': [20.371, 72.910],
      'specs': [
        { 'label': 'Continuous Emulsion Polymerization', 'value': '18,500 MT / month Synthetic Adhesives' },
        { 'label': 'Fevicol / Fevikwik Formulations', 'value': 'Proprietary Plasticizer & Monomer Formulations' },
        { 'label': 'Automated Robotic Packaging', 'value': '650 pouches / minute automated filling' }
      ],
      'description': "Pidilite's mother manufacturing complex. Synthesizes polyvinyl acetate emulsions, water-based adhesives, and specialty construction sealants dominating 70%+ market share."
    },
    'srf_dahej': {
      'title': '🧪 SRF Dahej Mega Specialty Chemicals & Fluorochemicals Complex',
      'facilityType': 'Specialty Fluorination & HFC/HFO Reaction Complex',
      'parentFirm': 'SRF Ltd [SRF:IN]',
      'coords': [21.712, 72.585],
      'specs': [
        { 'label': 'Dahej Chemical SEZ Land Area', 'value': '320 Acres Dedicated Complex' },
        { 'label': 'Fluorination Batch Reactors', 'value': '78 High-Pressure Autoclaves' },
        { 'label': 'Agro & Pharma Intermediate Molecules', 'value': '48 Commercial Active Ingredients' }
      ],
      'description': "World-scale specialty fluorochemicals manufacturing hub providing complex multi-step synthetic molecules to global innovator agrochemical and pharmaceutical clients."
    },
    'navin_surat': {
      'title': '🧪 Navin Fluorine Surat Fluorochemicals & CDMO Center (Bhestan)',
      'facilityType': 'Anhydrous Hydrofluoric Acid (HF) & CRAMS Facility',
      'parentFirm': 'Navin Fluorine International [NAVINFLUOR:IN]',
      'coords': [21.125, 72.842],
      'specs': [
        { 'label': 'Anhydrous HF Distillation', 'value': '24,000 MT / year High Purity HF' },
        { 'label': 'cGMP Synthesis Blocks', 'value': 'US-FDA Inspected Active Pharmaceutical Blocks' }
      ],
      'description': "Surat chemical synthesis center specializing in high-hazard hazardous fluorine chemistry, boron trifluoride adducts, and contract development."
    },
    'jubilant_bharuch': {
      'title': '🧪 Jubilant Ingrevia Bharuch Specialty Chemicals & Pyridine Hub',
      'facilityType': 'Pyridine & Picoline Mega Chemical Complex',
      'parentFirm': 'Jubilant Ingrevia Ltd [JUBLINGREA:IN]',
      'coords': [21.705, 72.998],
      'specs': [
        { 'label': 'Global Pyridine Derivative Rank', 'value': 'Global Lowest Cost Manufacturer (Rank #1)' },
        { 'label': 'Bio-Based Acetic Chemistry', 'value': 'Ethanol to Acetaldehyde & Ethyl Acetate' }
      ],
      'description': "Integrated specialty chemical complex utilizing green bio-ethanol to synthesize high-value intermediates for nutraceuticals, crop protection, and pharma."
    },
    'saket_max': {
      'title': '🏥 Max Super Speciality Hospital Saket (New Delhi)',
      'facilityType': 'Quaternary Care Flagship Academic Medical Campus',
      'parentFirm': 'Max Healthcare Institute Ltd [MAXHEALTH:IN]',
      'coords': [28.528, 77.214],
      'specs': [
        { 'label': 'Licensed Bed Capacity', 'value': '850 Operational Beds (Expanding to 1,200)' },
        { 'label': 'Average Revenue Per Bed (ARPOB)', 'value': '₹84,500 / operational bed day' },
        { 'label': 'Robotic Surgery Systems', 'value': 'da Vinci Xi & Mako Orthopedic Robots' },
        { 'label': 'International Medical Tourists', 'value': '18% of Total Patient Inflows' }
      ],
      'description': "Max Healthcare's crown-jewel quaternary oncology, cardiology, and organ transplant campus delivering the highest EBITDA margins and ARPOB in the Indian healthcare sector."
    },
    'narayana_bommasandra': {
      'title': '🏥 Narayana Health City & Mazumdar Shaw Cancer Centre (Bengaluru)',
      'facilityType': 'Mass-Scale Quaternary Cardiac & Cancer Campus',
      'parentFirm': 'Narayana Hrudayalaya Ltd [NH:IN]',
      'coords': [12.812, 77.692],
      'specs': [
        { 'label': 'Total Campus Bed Count', 'value': '1,400 Tertiary & Quaternary Beds' },
        { 'label': 'Open Heart Surgeries Performed', 'value': '32 Cardiac Surgeries / day (Lowest Cost Globally)' },
        { 'label': 'Cayman Islands Hospital Subsidiary', 'value': 'Health City Cayman Islands (USD Cash Margins 42%)' }
      ],
      'description': "The operational epicenter of Dr. Devi Shetty's assembly-line cardiac surgical efficiency, delivering world-class survival rates at a fraction of Western hospital costs."
    },
    'apollo_chennai': {
      'title': '🏥 Apollo Hospitals Greams Road Flagship Campus (Chennai)',
      'facilityType': 'Multi-Specialty Quaternary Healthcare & Proton Therapy Hub',
      'parentFirm': 'Apollo Hospitals Enterprise Ltd [APOLLOHOSP:IN]',
      'coords': [13.061, 80.252],
      'specs': [
        { 'label': 'Proton Beam Therapy Center', 'value': 'South East Asia First Proton Cancer Center' },
        { 'label': 'Apollo 24/7 Digital Platform', 'value': '30 Million Registered Telemedicine Users' },
        { 'label': 'Pharmacy Distribution Network', 'value': '6,000+ Retail Pharmacy Outlets' }
      ],
      'description': "Apollo's mother quaternary institution combining advanced oncology radiation, organ transplants, and omni-channel pharmacy distribution."
    },
    'taj_mahal_palace': {
      'title': '🏨 The Taj Mahal Palace & Tower (Apollo Bunder, Colaba, Mumbai)',
      'facilityType': 'Ultra-Luxury Heritage Grand Flagship Hotel',
      'parentFirm': 'The Indian Hotels Co Ltd (Taj) [INDHOTEL:IN]',
      'coords': [18.921, 72.833],
      'specs': [
        { 'label': 'Total Keys & Suites', 'value': '560 Luxury Rooms & Presidential Suites' },
        { 'label': 'Average Room Rate (ARR)', 'value': '₹28,500 / night (92% Occupancy Peak Season)' },
        { 'label': 'Food & Beverage Revenue', 'value': 'Wasabi, Golden Dragon, Sea Lounge' }
      ],
      'description': "IHCL's legendary heritage flagship property facing the Gateway of India, commanding unprecedented RevPAR and operating margins under the Taj brand."
    },
    'samhi_aerocity': {
      'title': '🏨 SAMHI Aerocity Multi-Branded Hospitality Cluster (New Delhi)',
      'facilityType': 'Institutional Airport Business Hotel Cluster',
      'parentFirm': 'SAMHI Hotels Ltd [SAMHI:IN]',
      'coords': [28.552, 77.121],
      'specs': [
        { 'label': 'Aerocity Keys Under Management', 'value': '962 Operating Keys (Courtyard, Fairfield by Marriott)' },
        { 'label': 'Blended ARR', 'value': '₹8,900 / night (84% Year-Round Occupancy)' }
      ],
      'description': "High-efficiency business travel asset cluster situated next to Indira Gandhi International Airport, delivering steady institutional corporate travel yields."
    },
    'chalet_powai': {
      'title': '🏨 Chalet Renaissance & Westin Powai Lake Luxury Complex (Mumbai)',
      'facilityType': 'Integrated Hotel, Convention Center & Commercial Office',
      'parentFirm': 'Chalet Hotels Ltd [CHALET:IN]',
      'coords': [19.128, 72.905],
      'specs': [
        { 'label': 'Hotel Keys & Convention Space', 'value': '773 Premium Keys | 100,000 sq ft Ballroom' },
        { 'label': 'Grade-A Commercial Office Asset', 'value': '1.2 Million sq ft Leased to MNC Tech Tenants' }
      ],
      'description': "Chalet's high-margin mixed-use asset combining luxury five-star hotel inventory with steady recurring commercial office lease rentals."
    },
    'apollo_raipur': {
      'title': '🏗️ APL Apollo Raipur 500,000 MT Heavy Structural Tube Complex',
      'facilityType': 'Direct 500x500mm Hollow Section Structural Steel Plant',
      'parentFirm': 'APL Apollo Tubes Ltd [APLAPOLLO:IN]',
      'coords': [21.251, 81.629],
      'specs': [
        { 'label': 'Direct 500x500mm ERW Mill', 'value': 'Largest Heavy Structural Tube Mill in India' },
        { 'label': 'Annual Steel Capacity', 'value': '500,000 MT / year dedicated heavy tubing' },
        { 'label': 'Steel Melting & Raw Material Tie-up', 'value': 'Captive HRC supply agreements with Jindal Steel' }
      ],
      'description': "APL Apollo's mega structural steel mill producing large-dimension hollow structural sections that replace conventional steel I-beams in airports, warehouses, and stadiums."
    },
    'ratnamani_kutch': {
      'title': '🏗️ Ratnamani Kutch High-Pressure Stainless Steel Tube Complex',
      'facilityType': 'Seamless Stainless Steel & Titanium Tubing Plant',
      'parentFirm': 'Ratnamani Metals & Tubes Ltd [RATNAMANI:IN]',
      'coords': [23.194, 70.188],
      'specs': [
        { 'label': 'Hot Extrusion Press Capacity', 'value': '4,500 Ton High-Tonnage Extruder' },
        { 'label': 'Nuclear & Defense Critical Quals', 'value': 'NPCIL, BARC, Shell, Saudi Aramco Approved' }
      ],
      'description': "Advanced metallurgical complex manufacturing high-pressure seamless stainless steel and nickel alloy tubes for nuclear power reactors, LNG terminals, and defense missile casing."
    },
    'welspun_anjar': {
      'title': '🏗️ Welspun Anjar Mega Helical & L-SAW Line Pipe Plant (Gujarat)',
      'facilityType': 'Large Diameter Longitudinal & Spiral Submerged Arc Welded Pipe Mill',
      'parentFirm': 'Welspun Corp Ltd [WELCORP:IN]',
      'coords': [23.112, 70.028],
      'specs': [
        { 'label': 'Pipe Diameter Capability', 'value': 'Up to 144 inches (3.65 meters) Outside Diameter' },
        { 'label': 'Annual Global Capacity', 'value': '2.5 Million MT across India, US, and Saudi Arabia' }
      ],
      'description': "Heavy line-pipe fabrication and internal/external anti-corrosion coating facility supplying deepwater oil/gas transport pipelines and national water grids."
    },
    'hdfc_bkc': {
      'title': '🏦 HDFC Bank Treasury & Global Clearing Operations (BKC Mumbai)',
      'facilityType': 'Central Financial Architecture & Algorithmic Clearing Headquarters',
      'parentFirm': 'HDFC Bank Ltd [HDFCBANK:IN]',
      'coords': [19.066, 72.868],
      'specs': [
        { 'label': 'Daily Payment Clearing Volume', 'value': '₹4.8 Trillion ($57 Billion) / day' },
        { 'label': 'Retail Customer Deposit Accounts', 'value': '95 Million Active Accounts' },
        { 'label': 'Branch & ATM Grid', 'value': '8,800+ Branches | 21,000+ ATMs across India' }
      ],
      'description': "The central banking operational nerve center managing India's largest private balance sheet ($400B+ assets), housing treasury FX desks and algorithmic clearing engines."
    },
    'icici_bkc': {
      'title': '🏦 ICICI Bank Towers & Digital Data Center (Bandra-Kurla Complex)',
      'facilityType': 'Corporate Headquarters & iMobile Cloud Engine',
      'parentFirm': 'ICICI Bank Ltd [ICICIBANK:IN]',
      'coords': [19.064, 72.865],
      'specs': [
        { 'label': 'Digital Transaction Share', 'value': '94% of Financial Transactions Non-Branch' },
        { 'label': 'Underwriting Engine', 'value': 'InstaLoan Pre-Approved Algorithmic Credit' }
      ],
      'description': "ICICI Bank's headquarters and digital banking software operations, operating with one of the lowest operating cost-to-income ratios (39.5%) and highest ROAs in India."
    },
    'kotak_bkc': {
      'title': '🏦 Kotak Infinity Financial Operations & Wealth Hub (BKC Mumbai)',
      'facilityType': 'Private Banking, Treasury & Retail HQ',
      'parentFirm': 'Kotak Mahindra Bank Ltd [KOTAKBANK:IN]',
      'coords': [19.068, 72.871],
      'specs': [
        { 'label': 'Private Wealth AUM', 'value': '₹3.2 Trillion UHNI Family Office Assets' },
        { 'label': 'Capital Adequacy Ratio', 'value': '20.8% (Safest Tier-1 Buffer in Asia)' }
      ],
      'description': "Ultra-conservative financial fortress managing prime retail deposits, investment banking deals, and India's premier ultra-high-net-worth wealth franchise."
    },
    'sbi_nariman': {
      'title': '🏦 State Bank of India Central Office (State Bank Bhavan, Nariman Point)',
      'facilityType': 'National Sovereign Commercial Bank Operations Hub',
      'parentFirm': 'State Bank of India [SBIN:IN]',
      'coords': [18.928, 72.823],
      'specs': [
        { 'label': 'Total Customer Base', 'value': '500 Million Indian Citizens (1 in 3 Citizens)' },
        { 'label': 'Total Loan Book', 'value': '₹38.5 Trillion ($460 Billion Assets)' },
        { 'label': 'YONO Digital Platform', 'value': '70 Million Registered Active Mobile Users' }
      ],
      'description': "The sovereign backbone of India's commercial banking system, commanding 24% of national banking deposits and executing direct government welfare and infrastructure clearing."
    },

    # ── US NANOS ──
    'tsmc_fab': {
      'title': '🔬 TSMC Fab 18A GigaFab & N3/N2 Cleanroom (Tainan Science Park)',
      'facilityType': '3nm / 2nm Extreme Ultraviolet (EUV) Semiconductor Foundry',
      'parentFirm': 'NVIDIA Corporation [NVDA:US]',
      'coords': [23.111, 120.276],
      'specs': [
        { 'label': 'Cleanroom Classification', 'value': 'Class 1 Ultra-Pure Vacuum Chamber' },
        { 'label': 'ASML Twinscan High-NA EUV Scanners', 'value': '34 Operational Systems ($380M each)' },
        { 'label': 'Monthly 3nm Silicon Wafer Output', 'value': '65,000 Wafers / month' },
        { 'label': 'CoWoS-L Advanced Packaging Line', 'value': 'Blackwell B200 Multi-Die Dual Reticle Integration' }
      ],
      'description': "The apex manufacturing hub of human technological civilization. Produces 100% of NVIDIA's Blackwell and Hopper AI computing engines with sub-atomic 3nm transistor architectures."
    },
    'amd_austin': {
      'title': '🔬 AMD Lone Star Silicon Design Campus & Microprocessor Lab (Austin, TX)',
      'facilityType': 'Zen 5 & MI350X GPU Architecture Engineering Center',
      'parentFirm': 'Advanced Micro Devices Inc [AMD:US]',
      'coords': [30.245, -97.868],
      'specs': [
        { 'label': 'Chiplet Packaging Lab', 'value': '3D V-Cache & Multi-Die Stacking Testbeds' },
        { 'label': 'ROCm Software Verification', 'value': '10,000 Node GPU Supercomputing Validation Cluster' }
      ],
      'description': "AMD's microprocessor design hub creating Zen CPU chiplets and Instinct MI300/MI350 series accelerators competing with NVIDIA in AI clusters."
    },
    'broadcom_sanjose': {
      'title': '🔬 Broadcom Global Silicon & Networking Innovation Center (San Jose, CA)',
      'facilityType': 'Custom AI ASIC & Tomahawk 5 Switch Foundry Lab',
      'parentFirm': 'Broadcom Inc [AVGO:US]',
      'coords': [37.382, -121.928],
      'specs': [
        { 'label': 'Tomahawk 5 Ethernet ASIC', 'value': '51.2 Tbps High-Radix Switching Engine' },
        { 'label': 'Custom XPU Co-Design', 'value': 'Hyperscaler AI Silicon (Google TPU v5/v6, Meta MTIA)' }
      ],
      'description': "The silicon heart of global data center networking, designing the high-speed Ethernet fabrics and custom ASICs powering hyperscale cloud infrastructure."
    },
    'qualcomm_sandiego': {
      'title': '🔬 Qualcomm Morehouse Campus & Snapdragon Engineering Hub (San Diego)',
      'facilityType': 'Oryon CPU & Snapdragon X Elite Compute Lab',
      'parentFirm': 'Qualcomm Inc [QCOM:US]',
      'coords': [32.895, -117.195],
      'specs': [
        { 'label': 'Snapdragon X Elite Benchmarks', 'value': '45 NPU TOPS for Windows Copilot+ AI Laptops' },
        { 'label': 'Cellular Modem 5G Advanced', 'value': 'Snapdragon X80 5G RF Baseband Processor' }
      ],
      'description': "Qualcomm's global R&D headquarters designing custom ARM-compatible Oryon CPU cores, edge AI NPU engines, and mobile radio-frequency modems."
    },
    'apple_park': {
      'title': '🏢 Apple Park & Silicon Design Center (1 Apple Park Way, Cupertino, CA)',
      'facilityType': 'Global Design HQ & Apple Silicon Hardware Engineering Center',
      'parentFirm': 'Apple Inc [AAPL:US]',
      'coords': [37.334, -122.009],
      'specs': [
        { 'label': 'Ring Building Footprint', 'value': '2.8 Million sq ft on 175 Acres' },
        { 'label': 'Renewable Microgrid', 'value': '17MW Onsite Rooftop Solar + Fuel Cells' },
        { 'label': 'Apple Silicon Team Lab', 'value': 'M4 / A18 Pro SoC Architecture & Neural Engine Design' }
      ],
      'description': "The operational and design epicenter of Apple Inc. Houses the world's most lucrative hardware and operating system ecosystem engineering teams."
    },
    'msft_redmond': {
      'title': '🏢 Microsoft Redmond Campus & Azure Hyperscale Center (Redmond, WA)',
      'facilityType': 'Enterprise Software & OpenAI Infrastructure Hub',
      'parentFirm': 'Microsoft Corp [MSFT:US]',
      'coords': [47.642, -122.130],
      'specs': [
        { 'label': 'Campus Building Count', 'value': '125 Buildings across 500 Acres' },
        { 'label': 'Azure AI Supercomputer Backlog', 'value': 'Tens of thousands of connected GPU clusters' }
      ],
      'description': "Microsoft's global corporate campus coordinating Azure cloud expansion, Windows OS, Office 365, and multi-billion-dollar OpenAI infrastructure deployments."
    },
    'goog_council_bluffs': {
      'title': '🌐 Google Council Bluffs Hyperscale AI Data Center Campus (Iowa)',
      'facilityType': 'Mega Hyperscale Cloud & Gemini Training Facility',
      'parentFirm': 'Alphabet Inc (Google) [GOOGL:US]',
      'coords': [41.221, -95.845],
      'specs': [
        { 'label': 'Cumulative Capital Investment', 'value': '$5.0+ Billion in Iowa Compute Infrastructure' },
        { 'label': 'Power Consumption', 'value': '450+ Megawatts Continuous Clean Power' },
        { 'label': 'TPU Pod Clusters', 'value': 'TPU v5p Tensor Processing Units for Gemini Model Pre-training' }
      ],
      'description': "One of Google's largest operational hyperscale data center complexes, training frontier multimodal neural networks and hosting YouTube, Search, and Google Cloud."
    },
    'amzn_ashburn': {
      'title': '🌐 AWS Northern Virginia Cloud Infrastructure Epicenter (Ashburn, VA)',
      'facilityType': 'Global Data Chokepoint & AWS us-east-1 Region',
      'parentFirm': 'Amazon.com Inc [AMZN:US]',
      'coords': [39.043, -77.487],
      'specs': [
        { 'label': 'Global Internet Traffic Share', 'value': 'Estimated 70% of World Internet Traffic Routes Through Loudoun' },
        { 'label': 'AWS Availability Zones', 'value': '6 Redundant Zones in us-east-1' }
      ],
      'description': "Data Center Alley in Northern Virginia. The central pillar of Amazon Web Services, powering the mission-critical cloud computing workloads of global banks, governments, and streaming platforms."
    },
    'tsla_austin': {
      'title': '🚗 Tesla Giga Texas Megafactory & 4680 Battery Line (Austin, TX)',
      'facilityType': 'Cybercab, Cybertruck & 4680 Cathode Battery Production Base',
      'parentFirm': 'Tesla Inc [TSLA:US]',
      'coords': [30.222, -97.617],
      'specs': [
        { 'label': 'Factory Footprint', 'value': '10 Million sq ft Factory Floor (Over 2,000 Acres)' },
        { 'label': 'Giga Press Die Casting', 'value': '9,000-Ton High-Pressure Aluminum Injection' },
        { 'label': 'Cortex AI Supercomputer', 'value': '100k H100 Cluster for Full Self-Driving End-to-End Neural Nets' }
      ],
      'description': "Tesla's headquarters and largest operational factory building Cybertruck, Model Y, and training FSD v12 vision-only end-to-end models on massive GPU clusters."
    },
    'baytown': {
      'title': '⛽ ExxonMobil Baytown Refining & Petrochemical Complex (Houston, TX)',
      'facilityType': 'Integrated 560,000 bpd Petroleum Refining & Olefins Plant',
      'parentFirm': 'ExxonMobil Corporation [XOM:US]',
      'coords': [29.749, -95.012],
      'specs': [
        { 'label': 'Crude Refining Capacity', 'value': '560,500 Barrels / day crude distillation' },
        { 'label': 'Steam Cracker Ethylene Output', 'value': '3.8 Million MT / year Polyethylene' },
        { 'label': 'Permian Pipeline Link', 'value': 'Direct Wink-to-Webster 1.5M bpd pipeline intake' }
      ],
      'description': "ExxonMobil's premier petrochemical and refining complex on the Houston Ship Channel, converting low-cost Permian tight crude into jet fuel, diesel, and performance polymers."
    },
    'cvx_pascagoula': {
      'title': '⛽ Chevron Pascagoula Refinery & Deepwater Gulf Hub (Mississippi)',
      'facilityType': '330,000 bpd Premium Hydrocracking Refinery',
      'parentFirm': 'Chevron Corporation [CVX:US]',
      'coords': [30.345, -88.508],
      'specs': [
        { 'label': 'Base Oil Manufacturing', 'value': 'World Largest Premium Group II Base Oil Plant' },
        { 'label': 'Deepwater Gulf of Mexico Offtake', 'value': 'Intake from Jack/St. Malo and Big Foot Spars' }
      ],
      'description': "Chevron's largest refinery, capable of processing complex heavy sour crudes into high-margin lubricants, gasoline, and aviation fuels."
    },
    'cheniere_sabine': {
      'title': '🚢 Cheniere Sabine Pass LNG Export Terminal (Cameron Parish, LA)',
      'facilityType': '30 Million MTPA Liquefied Natural Gas (LNG) Liquefaction Facility',
      'parentFirm': 'Cheniere Energy Inc [LNG:US]',
      'coords': [29.756, -93.872],
      'specs': [
        { 'label': 'Liquefaction Trains', 'value': '6 Operational Trains (30+ MTPA LNG)' },
        { 'label': 'LNG Storage Tanks', 'value': '5 Full-Containment Tanks (3.4M Barrels Liquid)' },
        { 'label': 'Deepwater Berths', 'value': '2 Dedicated Docks Handling Q-Flex LNG Carriers' }
      ],
      'description': "The largest natural gas export facility in the Western Hemisphere, supplying liquefied natural gas under 20-year contracts to Europe and Asia to replace Russian pipeline flows."
    },
    'cop_permian': {
      'title': '⛽ ConocoPhillips Permian Basin Unconventional Assets (Midland, TX)',
      'facilityType': 'Tight Oil & Shale Gas Horizontal Drilling Complex',
      'parentFirm': 'ConocoPhillips [COP:US]',
      'coords': [31.997, -102.077],
      'specs': [
        { 'label': 'Net Permian Production', 'value': '750,000 Barrels of Oil Equivalent / day' },
        { 'label': 'Supply Cost / Barrel', 'value': '< $35 / bbl WTI Breakeven Cost' }
      ],
      'description': "ConocoPhillips' core shale engine, utilizing multi-pad drilling and 3-mile horizontal laterals to produce low-cost crude with multi-decade inventory runway."
    },
    'prysmian_highland': {
      'title': '⚡ Prysmian Highland Submarine High-Voltage Cable Plant (Highland, NY)',
      'facilityType': 'Submarine HVDC Power Transmission Cable Facility',
      'parentFirm': 'Prysmian Group [PRY:IM]',
      'coords': [41.725, -73.965],
      'specs': [
        { 'label': 'Submarine Cable Armoring', 'value': '525kV HVDC Extruded Subsea Cable System' },
        { 'label': 'Cable-Laying Vessel Tie-Up', 'value': 'Leonardo da Vinci & Monna Lisa Installation Fleets' }
      ],
      'description': "Advanced subsea cable plant dedicated to offshore wind interconnections and interstate electric grid transmission lines along the US Eastern Seaboard."
    },
    'hubbell_shelton': {
      'title': '⚡ Hubbell Utility Solutions Grid Modernization Center (Shelton, CT)',
      'facilityType': 'High-Voltage Switchgear & Utility Distribution Equipment Plant',
      'parentFirm': 'Hubbell Inc [HUBB:US]',
      'coords': [41.316, -73.093],
      'specs': [
        { 'label': 'Transmission Connectors & Insulators', 'value': 'Ohio Brass High-Voltage Polymeric Insulators' },
        { 'label': 'Smart Metering & Grid Automation', 'value': 'Aclara Automated AMI Communications Networks' }
      ],
      'description': "Manufacturing center for electric utility transmission grid components, surge arresters, and automated distribution sensors deployed by US power utilities."
    },
    'stride_hq': {
      'title': '🎓 Stride K12 Curriculum & Virtual Academy Hub (Reston, VA)',
      'facilityType': 'Accredited Online Public School Curriculum Operations',
      'parentFirm': 'Stride Inc (K12) [LRN:US]',
      'coords': [38.958, -77.357],
      'specs': [
        { 'label': 'Full-Time Virtual Students', 'value': '195,000+ Enrolled K-12 Students' },
        { 'label': 'State Public School Partnerships', 'value': 'Over 30 US States Funding Virtual Charters' }
      ],
      'description': "The operational and curricular nerve center for Stride's virtual public academies, providing state-funded digital schooling and career tech education across the US."
    },
    'coursera_mtv': {
      'title': '🎓 Coursera Mountain View Silicon Valley Software Lab (Mountain View, CA)',
      'facilityType': 'Global Online Degree & Enterprise Skills Platform Lab',
      'parentFirm': 'Coursera Inc [COUR:US]',
      'coords': [37.386, -122.083],
      'specs': [
        { 'label': 'Registered Global Learners', 'value': '155+ Million Learners Worldwide' },
        { 'label': 'University & Industry Partners', 'value': '325+ Top Universities (Stanford, Penn, Google, IBM)' }
      ],
      'description': "Coursera's headquarters where algorithmic recommendation systems, GenAI course translators, and university degree programs are developed."
    },
    'duolingo_pgh': {
      'title': '🎓 Duolingo East Liberty Algorithmic Learning Hub (Pittsburgh, PA)',
      'facilityType': 'Gamified Language & English Test Assessment Lab',
      'parentFirm': 'Duolingo Inc [DUOL:US]',
      'coords': [40.461, -79.924],
      'specs': [
        { 'label': 'Daily Active Users (DAU)', 'value': '34 Million Daily Active Language Learners' },
        { 'label': 'Duolingo English Test (DET)', 'value': 'Accepted by 5,000+ Higher Ed Institutions Globally' }
      ],
      'description': "Headquarters of Duolingo, developing high-retention gamification mechanisms, synthetic AI character voices, and certified computerized language testing."
    },

    # ── GERMANY NANOS ──
    'mercedes_factory56': {
      'title': '🚗 Mercedes-Benz Factory 56 Ultra-Flexible Industry 4.0 Complex (Sindelfingen)',
      'facilityType': 'Zero-Carbon Digital Automotive Assembly Plant',
      'parentFirm': 'Mercedes-Benz Group AG [MBG:GR]',
      'coords': [48.708, 9.004],
      'specs': [
        { 'label': '5G Private Factory Network', 'value': 'Real-Time IoT Tracking of 400+ Automated AGVs' },
        { 'label': 'Assembly Models', 'value': 'S-Class, Maybach & EQS Electric Flagships on One Single Line' }
      ],
      'description': "The world benchmark for flexible automotive manufacturing, utilizing driverless transport systems, overhead paperless digital cockpits, and 100% solar-powered assembly."
    },
    'bmw_munich': {
      'title': '🚗 BMW Group Plant Munich & FIZ Research Center (Munich, Bavaria)',
      'facilityType': 'High-Precision Automotive Engineering & Electric Drivetrain Plant',
      'parentFirm': 'Bayerische Motoren Werke AG (BMW) [BMW:GR]',
      'coords': [48.178, 11.558],
      'specs': [
        { 'label': 'Daily Vehicle Output', 'value': '1,000 Vehicles / day (3 Series & i4 Gran Coupe)' },
        { 'label': 'FIZ R&D Engineering Staff', 'value': '25,000 Specialized Automotive Engineers' }
      ],
      'description': "BMW's historical mother plant transformed into an electrified manufacturing facility producing the i4 electric sedan alongside internal combustion platforms."
    },
    'vw_wolfsburg': {
      'title': '🚗 Volkswagen Wolfsburg Mega Plant (Wolfsburg, Lower Saxony)',
      'facilityType': 'Largest Single Automotive Manufacturing Complex on Earth',
      'parentFirm': 'Volkswagen AG [VOW3:GR]',
      'coords': [52.433, 10.778],
      'specs': [
        { 'label': 'Factory Campus Footprint', 'value': '6.5 Square Kilometers (70 Million sq ft)' },
        { 'label': 'Rail Infrastructure', 'value': '75 Kilometers of In-Plant Freight Rail Tracks' }
      ],
      'description': "The colossal manufacturing heart of Volkswagen Group, producing over 800,000 vehicles annually and housing the group's global software and procurement leadership."
    },
    'siemens_amberg': {
      'title': '🤖 Siemens Electronics Manufacturing Plant Amberg (EWA, Bavaria)',
      'facilityType': 'Benchmark Industry 4.0 Smart Factory (99.999% Quality Yield)',
      'parentFirm': 'Siemens AG [SIE:GR]',
      'coords': [49.444, 11.859],
      'specs': [
        { 'label': 'Simatic PLC Output', 'value': '17 Million Industrial Controllers / year' },
        { 'label': 'Defect Rate', 'value': '11 DPM (Defects Per Million Units Produced)' },
        { 'label': 'Digital Twin Integration', 'value': 'Full Siemens Teamcenter & NX Simulation' }
      ],
      'description': "The world's most famous Industry 4.0 showcase plant. Machines communicate autonomously with components to assemble programmable logic controllers (PLCs) with near-zero defects."
    },
    'kion_frankfurt': {
      'title': '🤖 KION Dematic Automation & Forklift Engineering Hub (Frankfurt)',
      'facilityType': 'Intralogistics Software & Automated Warehouse Systems',
      'parentFirm': 'KION Group AG [KGX:GR]',
      'coords': [50.110, 8.682],
      'specs': [
        { 'label': 'Dematic Warehouse Systems Installed', 'value': 'Over 6,000 Automated Fulfillment Centers Globally' },
        { 'label': 'Linde & STILL Material Handling', 'value': 'Market Leader in European Electric Forklifts' }
      ],
      'description': "KION's technology center developing automated guided vehicles (AGVs), automated storage and retrieval systems (ASRS), and warehouse management software."
    },
    'basf_ludwigshafen': {
      'title': '🧪 BASF Ludwigshafen Verbund Mega Site (Rhineland-Palatinate)',
      'facilityType': 'World Largest Integrated Chemical Verbund Complex',
      'parentFirm': 'BASF SE [BAS:GR]',
      'coords': [49.497, 8.432],
      'specs': [
        { 'label': 'Continuous Site Land Area', 'value': '10.0 Square Kilometers (2,000 Buildings)' },
        { 'label': 'Pipelines Connecting Plants', 'value': '2,850 Kilometers of Integrated Inter-Plant Pipelines' },
        { 'label': 'Rhine River Port Berths', 'value': 'Handling 21 Million MT Raw Materials / year' }
      ],
      'description': "The mother of all integrated chemical manufacturing. By-products and waste heat from one chemical reaction serve as raw materials for downstream plants, generating immense cost efficiency."
    },
    'bayer_leverkusen': {
      'title': '🧪 Bayer Chempark Leverkusen & Life Sciences HQ (North Rhine-Westphalia)',
      'facilityType': 'Pharmaceutical Synthesis & Crop Science Chemistry Complex',
      'parentFirm': 'Bayer AG [BAYN:GR]',
      'coords': [51.018, 6.985],
      'specs': [
        { 'label': 'Chempark Footprint', 'value': '4.8 Square Kilometers' },
        { 'label': 'Pharmaceutical Blockbusters', 'value': 'Xarelto & Eylea Synthesis and Formulation' }
      ],
      'description': "Bayer's historical headquarters campus housing active pharmaceutical ingredient synthesis, oncology laboratories, and crop protection formulating lines."
    },

    # ── JAPAN NANOS ──
    'tel_miyagi': {
      'title': '🔬 TEL Miyagi Plasma Etch Technology Development Center (Miyagi, Japan)',
      'facilityType': 'Advanced Dielectric & Conductor Etch Equipment Manufacturing Plant',
      'parentFirm': 'Tokyo Electron Ltd [8035:JP]',
      'coords': [38.375, 140.892],
      'specs': [
        { 'label': 'Cleanroom Area', 'value': '45,000 sq meters State-of-the-Art Cleanroom' },
        { 'label': 'High Aspect Ratio Cryogenic Etch', 'value': '400+ Layer 3D NAND & GAA Transistor Etching' }
      ],
      'description': "Tokyo Electron's premier plasma etch systems plant, developing the atomic-precision dry etching machines that create memory channels in 3D NAND and gate-all-around logic chips."
    },
    'advantest_gunma': {
      'title': '🔬 Advantest Gunma R&D Center & High-Speed Test Factory (Gunma, Japan)',
      'facilityType': 'Ultra-High-Speed ATE Semiconductor Memory & SoC Test Systems',
      'parentFirm': 'Advantest Corp [6857:JP]',
      'coords': [36.258, 139.388],
      'specs': [
        { 'label': 'T5503HS2 Memory Tester', 'value': 'Testing HBM3E at 9.6 Gbps Parallel Data Rates' },
        { 'label': 'Global Market Share', 'value': 'Over 55% of World Automated Test Equipment (ATE)' }
      ],
      'description': "The critical chokepoint facility testing high-bandwidth memory (HBM) and complex GPUs before they are assembled into AI supercomputers worldwide."
    },
    'lasertec_yokohama': {
      'title': '🔬 Lasertec Yokohama Advanced Optical Inspection Systems HQ (Yokohama)',
      'facilityType': 'Actinic EUV Photomask Blank & Pattern Inspection Foundry',
      'parentFirm': 'Lasertec Corp [6920:JP]',
      'coords': [35.512, 139.615],
      'specs': [
        { 'label': 'Actinic EUV Scanner (ACTIS A1500)', 'value': 'Uses 13.5nm EUV Light for Sub-Surface Mask Defect Detection' },
        { 'label': 'Global Market Share', 'value': '100% Global Monopoly on Actinic Blank Inspection' }
      ],
      'description': "The sole facility in the world capable of building optical inspection tools that illuminate semiconductor photomasks with extreme ultraviolet light to find sub-nanometer crystal flaws."
    },
    'keyence_osaka': {
      'title': '🔬 Keyence Central R&D & High-Speed Vision Sensor Laboratory (Osaka)',
      'facilityType': 'Direct-Sales Machine Vision, Laser Marker & Sensor Development HQ',
      'parentFirm': 'Keyence Corporation [6861:JP]',
      'coords': [34.733, 135.500],
      'specs': [
        { 'label': 'Same-Day Shipping Ratio', 'value': '99.5% of Customer Sensor Orders Shipped Same Day' },
        { 'label': 'Fabless Gross Margin', 'value': '82.5% Gross Margin | 52% Operating Margin' }
      ],
      'description': "Keyence's headquarters and testing laboratory where direct-sales technical consultants solve manufacturing automation challenges without third-party distributors."
    },
    'fanuc_yamanashi': {
      'title': '🤖 Fanuc Mount Fuji Autonomous CNC & Yellow Robot Complex (Oshino-mura)',
      'facilityType': 'Robots Building Robots Fully Automated Manufacturing Forest',
      'parentFirm': 'Fanuc Corp [6954:JP]',
      'coords': [35.452, 138.854],
      'specs': [
        { 'label': 'Campus Footprint in Forest', 'value': '1.8 Square Kilometers near Mount Fuji' },
        { 'label': 'Unmanned Lights-Out Production', 'value': 'Robotic machining cells running 30 days without human presence' }
      ],
      'description': "The famous bright yellow factory complex at the base of Mount Fuji where autonomous robotic work cells assemble computer numerical controls (CNCs) and industrial robots."
    },
    'mitsubishi_marunouchi': {
      'title': '🏢 Mitsubishi Corporation Global Trading Headquarters (Marunouchi, Tokyo)',
      'facilityType': 'Sogo Shosha Energy, Metals & Global Commodity Control Center',
      'parentFirm': 'Mitsubishi Corporation [8058:JP]',
      'coords': [35.681, 139.764],
      'specs': [
        { 'label': 'Global Operating Subsidiaries', 'value': 'Over 1,700 Group Companies in 90 Countries' },
        { 'label': 'Metallurgical Coal Monopoly', 'value': 'BMA Queensland Australia 50/50 JV with BHP' }
      ],
      'description': "The trading nerve center of Japan's largest Sogo Shosha, orchestrating global LNG supply chains, Australian coking coal, automotive dealerships, and food logistics."
    },
    'mitsui_tokyo': {
      'title': '🏢 Mitsui & Co Headquarters & Natural Resources Trading Floor (Otemachi, Tokyo)',
      'facilityType': 'LNG, Iron Ore & Infrastructure Trading Command Center',
      'parentFirm': 'Mitsui & Co Ltd [8031:JP]',
      'coords': [35.688, 139.763],
      'specs': [
        { 'label': 'Global LNG Equity Portfolio', 'value': 'Equity stakes in Sakhalin-2, Cameron LNG, Mozambique' },
        { 'label': 'Iron Ore Joint Ventures', 'value': 'Robe River & Mt Newman JV with Rio Tinto and BHP' }
      ],
      'description': "Mitsui's executive trading floor controlling strategic equity stakes in iron ore mines, copper extraction in Chile, and global grain distribution."
    },
    'itochu_minato': {
      'title': '🏢 Itochu Corporation Aoyama Flagship Headquarters (Minato-ku, Tokyo)',
      'facilityType': 'Consumer Conglomerate, Retail & Textile Trading Hub',
      'parentFirm': 'Itochu Corporation [8001:JP]',
      'coords': [35.671, 139.718],
      'specs': [
        { 'label': 'FamilyMart Retail Chain', 'value': 'Over 24,000 Convenience Stores Across Asia' },
        { 'label': 'Non-Resource Earnings Share', 'value': 'Over 75% of Group Net Profit' }
      ],
      'description': "Itochu's modern corporate tower commanding Japan's highest non-resource trading house profitability, owning FamilyMart convenience stores, pulp, and food networks."
    },

    # ── CHINA NANOS ──
    'byd_zhengzhou': {
      'title': '🚗 BYD Zhengzhou Mega New Energy Vehicle Industrial Base (Henan)',
      'facilityType': 'Gigantic Integrated EV Assembly, Battery & Motor Factory',
      'parentFirm': 'BYD Company Ltd [002594:SZ]',
      'coords': [34.521, 113.882],
      'specs': [
        { 'label': 'Campus Footprint', 'value': '16.0 Square Kilometers (2,400 football fields)' },
        { 'label': 'Annual EV Output Capacity', 'value': '1.0 Million New Energy Vehicles / year' },
        { 'label': 'Blade Battery Packaging Lines', 'value': 'Cell-to-Body (CTB) Integrated Production' }
      ],
      'description': "BYD's largest single manufacturing base on earth, integrating vertical supply chains from molten aluminum casting to finished hybrid and pure EV sedans and SUVs."
    },
    'catl_ningde': {
      'title': '🔋 CATL Contemporary Amperex Mega Battery Base (Ningde, Fujian)',
      'facilityType': 'World Largest Lithium Iron Phosphate (LFP) & Sodium-Ion Battery Base',
      'parentFirm': 'CATL [300750:SZ]',
      'coords': [26.665, 119.542],
      'specs': [
        { 'label': 'Cumulative Battery Capacity', 'value': 'Over 350 GWh Global Annual Cell Production' },
        { 'label': 'Lighthouse Factory Accreditation', 'value': 'World Economic Forum Zero-Carbon Smart Plant' }
      ],
      'description': "The epicenter of the global electric vehicle transition, supplying prismatic LFP and ternary lithium batteries to Tesla, BMW, Mercedes, and Chinese automakers."
    },
    'longi_xian': {
      'title': '☀️ LONGi Xi’an Advanced Monocrystalline Silicon & HPBC Solar Hub (Shaanxi)',
      'facilityType': 'Monocrystalline Silicon Ingot, Wafer & High-Efficiency Solar Cell Plant',
      'parentFirm': 'LONGi Green Energy Technology [601012:SS]',
      'coords': [34.265, 108.954],
      'specs': [
        { 'label': 'Monocrystalline Wafer Output', 'value': '150 GW Global Annual Wafer Capacity' },
        { 'label': 'HPBC 2.0 Cell Efficiency', 'value': '26.6% Mass Production Conversion Efficiency' }
      ],
      'description': "LONGi's research and manufacturing center developing ultra-thin diamond-wire sliced monocrystalline wafers and high-efficiency back-contact solar modules."
    },
    'sungrow_hefei': {
      'title': '☀️ Sungrow Hefei Mega Solar Inverter & BESS Industrial Park (Anhui)',
      'facilityType': 'Central & String Photovoltaic Inverter and Utility Energy Storage Base',
      'parentFirm': 'Sungrow Power Supply Co [300274:SZ]',
      'coords': [31.820, 117.227],
      'specs': [
        { 'label': 'Annual Inverter Output', 'value': '300 GW Inverter & Power Conversion Systems' },
        { 'label': 'Grid-Forming Energy Storage', 'value': 'PowerTitan 2.0 Liquid-Cooled BESS Systems' }
      ],
      'description': "The world's largest inverter manufacturing base, producing power electronics that convert solar DC electricity into high-voltage grid-synchronized AC power."
    },
    'cssc_shanghai': {
      'title': '🚢 CSSC Jiangnan Shipyard Mega Drydocks (Changxing Island, Shanghai)',
      'facilityType': 'World Largest Commercial & Dual-Fuel Container Shipbuilding Yard',
      'parentFirm': 'China CSSC Holdings Ltd [600150:SS]',
      'coords': [31.354, 121.733],
      'specs': [
        { 'label': 'Changxing Base Waterfront', 'value': '8.0 Kilometers of Deepwater River Outfitting Berths' },
        { 'label': 'Drydock Dimensions', 'value': '580m x 105m Mega Drydock for 24,000 TEU Vessels' },
        { 'label': 'Gantry Crane Capacity', 'value': '1,600-Ton Heavy Gantry Cranes' }
      ],
      'description': "China's premier mega-shipyard constructing ultra-large dual-fuel LNG container ships, very large ammonia carriers, and naval defense vessels."
    },
    'cosco_yangshan': {
      'title': '🚢 COSCO Yangshan Deepwater Automated Container Terminal (Shanghai)',
      'facilityType': 'World Largest Automated Deepwater Maritime Container Hub',
      'parentFirm': 'COSCO SHIPPING Holdings [601919:SS]',
      'coords': [30.628, 122.062],
      'specs': [
        { 'label': 'Annual Container Throughput', 'value': '26+ Million TEUs Handled Annually' },
        { 'label': 'Automated Guided Vehicles (AGV)', 'value': '130+ Driverless Electric Container Haulers' }
      ],
      'description': "An island seaport linked to Shanghai by the 32.5km Donghai Bridge, operating the world's highest-volume robotic maritime logistics interchange."
    },

    # ── BRAZIL NANOS ──
    'petrobras_buzios': {
      'title': '⛽ Petrobras Búzios FPSO Almirante Barroso (Santos Basin Pre-Salt, Brazil)',
      'facilityType': 'Ultra-Deepwater Pre-Salt Floating Production Storage & Offloading Unit',
      'parentFirm': 'Petrobras [PBR:US]',
      'coords': [-24.850, -42.750],
      'specs': [
        { 'label': 'Water Depth', 'value': '2,100 Meters Deepwater Column + 5,000m Salt Layer' },
        { 'label': 'Crude Processing Capacity', 'value': '150,000 Barrels of Oil / day' },
        { 'label': 'Natural Gas Compression', 'value': '6.0 Million Cubic Meters / day' }
      ],
      'description': "Petrobras' flagship pre-salt mega-field offshore Rio de Janeiro, tapping carbonate reservoirs trapped beneath thousands of meters of subterranean salt."
    },
    'vale_carajas': {
      'title': '⛏️ Vale Carajás S11D Eliezer Batista Iron Ore Complex (Pará, Brazil)',
      'facilityType': 'World Largest Open-Pit 65% Fe Premium Iron Ore Mining Complex',
      'parentFirm': 'Vale S.A. [VALE:US]',
      'coords': [-6.058, -50.158],
      'specs': [
        { 'label': 'Annual Iron Ore Production', 'value': '90 Million MT / year (S11D Mine Alone)' },
        { 'label': 'Truckless Conveyor System', 'value': '30+ Kilometers of In-Pit High-Capacity Belts' },
        { 'label': 'Iron Content Quality', 'value': '65.4% Natural Fe (Lowest Silica Impurity Globally)' }
      ],
      'description': "Vale's revolutionary truckless open-pit iron ore operation in the Amazon basin, moving premium ore via electric conveyor belts to dedicated export rail networks."
    },
    'slc_matopiba': {
      'title': '🌾 SLC Agrícola Fazenda Parnaíba Mega Farm (Maranhão / MATOPIBA, Brazil)',
      'facilityType': 'Industrial-Scale Precision Soybean, Cotton & Corn Agri-Estate',
      'parentFirm': 'SLC Agrícola S.A. [SLCE3:BZ]',
      'coords': [-8.520, -45.450],
      'specs': [
        { 'label': 'Arable Land Area Under Cultivation', 'value': '700,000+ Hectares Group-Wide' },
        { 'label': 'Double-Cropping Cycle', 'value': 'Soybean Harvest Immediately Followed by Safrinha Corn' },
        { 'label': 'Satellite Telemetry', 'value': 'Real-Time Precision Fertilizer & Soil Sensor Guidance' }
      ],
      'description': "SLC's mega grain estate demonstrating the tremendous competitive advantage of Brazilian agriculture: double-cropping, abundant rainfall, and scale efficiency."
    },

    # ── UK & EUROPE NANOS ──
    'hsbc_canarywharf': {
      'title': '🏦 HSBC 8 Canada Square Global Tower (Canary Wharf, London)',
      'facilityType': 'Global Banking & Cross-Border Asian Trade Clearing Operations',
      'parentFirm': 'HSBC Holdings plc [HSBA:LN]',
      'coords': [51.503, -0.018],
      'specs': [
        { 'label': 'Tower Height & Floors', 'value': '210 Meters Height (45 Floors Canary Wharf)' },
        { 'label': 'Global Trade Finance Market Share', 'value': '#1 Trade Bank in Asia, Middle East & Europe' }
      ],
      'description': "HSBC's headquarters building overseeing global trade clearing, London foreign exchange liquidity, and banking networks bridging the West and Asian emerging markets."
    },
    'barclays_churchill': {
      'title': '🏦 Barclays 1 Churchill Place Operations Tower (Canary Wharf, London)',
      'facilityType': 'Investment Banking, Fixed Income & UK Retail Banking HQ',
      'parentFirm': 'Barclays PLC [BARC:LN]',
      'coords': [51.504, -0.015],
      'specs': [
        { 'label': 'Fixed Income Currencies & Commodities (FICC)', 'value': 'Major Primary Dealer in UK Gilts & US Treasuries' },
        { 'label': 'Barclays Payments Network', 'value': 'Processing 40% of All UK Credit & Debit Transactions' }
      ],
      'description': "Barclays' corporate tower coordinating the group's investment banking syndicate, UK mortgages, and wholesale payment processing."
    },
    'azn_cambridge': {
      'title': '💊 AstraZeneca The Discovery Centre (DISC) & Cambridge Biomedical Campus',
      'facilityType': 'Global R&D Headquarters & Next-Gen Oncology Biologics Center',
      'parentFirm': 'AstraZeneca PLC [AZN:LN]',
      'coords': [52.176, 0.141],
      'specs': [
        { 'label': 'Biomedical Campus Footprint', 'value': '£1.0 Billion Purpose-Built R&D Campus' },
        { 'label': 'Active Pipeline Molecules', 'value': '170+ Projects in Clinical Development' }
      ],
      'description': "AstraZeneca's state-of-the-art discovery laboratory in Cambridge, UK, leading research into targeted antibody drug conjugates (ADCs) and cell therapies."
    },
    'novo_kalundborg': {
      'title': '💊 Novo Nordisk Kalundborg GLP-1 Active Ingredient Mega Complex (Denmark)',
      'facilityType': 'World Largest Insulin & Semaglutide (Ozempic/Wegovy) Fermentation Site',
      'parentFirm': 'Novo Nordisk A/S [NVO:US]',
      'coords': [55.676, 11.085],
      'specs': [
        { 'label': 'Campus Footprint', 'value': '1.6 Million sq meters (160 Hectares Dedicated)' },
        { 'label': 'Capital Expansion Program', 'value': 'Over $8.5 Billion Active Manufacturing Expansion' },
        { 'label': 'Global Semaglutide Supply', 'value': 'Fermentation of active GLP-1 peptides for worldwide distribution' }
      ],
      'description': "The manufacturing center for the most lucrative pharmaceutical franchise in human history, fermenting and purifying recombinant GLP-1 active ingredients."
    },
    'asml_veldhoven': {
      'title': '🔬 ASML Veldhoven High-NA EUV Manufacturing & Cleanroom Campus (Netherlands)',
      'facilityType': 'Extreme Ultraviolet (EUV) & High-NA Photolithography Assembly Epicenter',
      'parentFirm': 'ASML Holding NV [ASML:NA]',
      'coords': [51.403, 5.412],
      'specs': [
        { 'label': 'High-NA EUV Scanner (EXE:5000)', 'value': '0.55 Numerical Aperture ($380M System Weight 150 Tons)' },
        { 'label': 'Carl Zeiss Optics Integration', 'value': 'Smoothest Mirrors in the World (Atomic Precision)' },
        { 'label': 'Global EUV Market Share', 'value': '100% Total Monopoly on Advanced Photolithography' }
      ],
      'description': "The technological pinnacle of human manufacturing. Thousands of specialized suppliers ship sub-systems to Veldhoven, where lasers blast molten tin droplets 50,000 times per second to create extreme ultraviolet light."
    },

    # ── SAUDI ARABIA NANOS ──
    'aramco_ghawar': {
      'title': '⛽ Saudi Aramco Ghawar Field & Abqaiq Stabilization Plant (Eastern Province)',
      'facilityType': 'World Largest Conventional Onshore Oil Field & Crude Processing Hub',
      'parentFirm': 'Saudi Aramco [2222:SR]',
      'coords': [25.932, 49.664],
      'specs': [
        { 'label': 'Ghawar Field Dimensions', 'value': '280 Kilometers Long x 30 Kilometers Wide' },
        { 'label': 'Abqaiq Stabilization Output', 'value': '7.0 Million Barrels / day Light Crude Processing' },
        { 'label': 'Lifting Cost / Barrel', 'value': '$3.20 / bbl (Lowest Upstream Cost on Earth)' }
      ],
      'description': "The supreme crown jewel of global oil production. Ghawar produces high-gravity Arab Light crude with unmatched operational economics and ultra-low reservoir decline."
    },
    'sabic_jubail': {
      'title': '🧪 SABIC Jubail Industrial City Mega Petrochemical Complex (Eastern Province)',
      'facilityType': 'Ethane Cracking, Methanol & Advanced Polymer Complex',
      'parentFirm': 'SABIC [2010:SR]',
      'coords': [27.012, 49.658],
      'specs': [
        { 'label': 'Jubail Industrial Footprint', 'value': 'World Largest Industrial City with Captive Deepwater Port' },
        { 'label': 'Feedstock Advantage', 'value': 'Captive Aramco Ethane Gas Allocation at Fixed Subsidized Rates' }
      ],
      'description': "SABIC's manufacturing city in Jubail, utilizing cost-advantaged associated gas feedstocks to synthesize commodity plastics and engineered polymers."
    },

    # ── SINGAPORE NANOS ──
    'singtel_tuas': {
      'title': '🌐 Singtel Tuas Subsea Cable Landing Station & DC West Mega Hub (Singapore)',
      'facilityType': 'International Subsea Fiber Chokepoint & AI Cloud Data Center',
      'parentFirm': 'Singtel [Z74:SG]',
      'coords': [1.321, 103.651],
      'specs': [
        { 'label': 'Subsea Cable Systems Terminating', 'value': 'SEA-ME-WE 3/4/5, APG, SJC2 Interconnections' },
        { 'label': 'DC West Capacity', 'value': '60+ Megawatts High-Density AI GPU Rack Space' }
      ],
      'description': "Singapore's vital telecom chokepoint connecting trans-Pacific and Asian submarine optic fiber routes with regional hyperscale enterprise cloud infrastructure."
    },
    'wilmar_jurong': {
      'title': '🌴 Wilmar Jurong Island Edible Oils & Oleochemicals Processing Base',
      'facilityType': 'Palm Oil Refining, Biodiesel & Oleochemical Synthesis Plant',
      'parentFirm': 'Wilmar International Ltd [F34:SG]',
      'coords': [1.272, 103.715],
      'specs': [
        { 'label': 'Daily Refining Throughput', 'value': '6,500 MT / day Crude Palm Oil (CPO)' },
        { 'label': 'Port Berths', 'value': 'Deepwater chemical tanker berths with direct pipeline connection' }
      ],
      'description': "Wilmar's high-volume refining asset on Jurong Island, processing Indonesian and Malaysian sustainable palm oil into consumer packaged foods, fats, and oleochemicals."
    },

    # ── AUSTRALIA NANOS ──
    'bhp_olympic': {
      'title': '⛏️ BHP Olympic Dam Underground Mine Complex (Roxby Downs, South Australia)',
      'facilityType': 'World Largest Single Known Copper, Uranium & Gold Deposit',
      'parentFirm': 'BHP Group Ltd [BHP:AU]',
      'coords': [-30.435, 136.883],
      'specs': [
        { 'label': 'Underground Rail Network', 'value': '450 Kilometers of Deep Underground Roadways & Rail' },
        { 'label': 'Ore Mineralization', 'value': 'Multi-Metals Orebody: Copper, Uranium Oxide (U3O8), Gold, Silver' },
        { 'label': 'Smelter Output', 'value': '210,000 MT / year LME Grade A Refined Copper Cathodes' }
      ],
      'description': "BHP's underground deposit containing the world's fourth largest copper resource and the single largest uranium deposit on the planet."
    },
    'rio_pilbara': {
      'title': '⛏️ Rio Tinto AutoHaul Automated Pilbara Iron Ore Network & Port Dampier',
      'facilityType': 'Fully Autonomous Robotic Heavy-Haul Freight Rail & Bulk Export Port',
      'parentFirm': 'Rio Tinto Ltd [RIO:AU]',
      'coords': [-20.658, 116.711],
      'specs': [
        { 'label': 'Autonomous Train Distance', 'value': '1,700 Kilometers of Driverless Rail Network' },
        { 'label': 'Train Configuration', 'value': '2.4 Kilometers Long (240 Cars / 28,000 Tons Iron Ore per train)' },
        { 'label': 'Port Dampier Rotary Car Dumpers', 'value': 'Dumping 4 Railcars Simultaneously in 90 Seconds' }
      ],
      'description': "The world's first fully automated, driverless heavy-haul freight rail system. Controls 50 driverless trains moving 330 million tons of iron ore annually to export vessels."
    },

    # ── SOUTH KOREA NANOS ──
    'samsung_pyeongtaek': {
      'title': '🔬 Samsung Electronics Pyeongtaek Campus Line 3 & 4 (Gyeonggi-do)',
      'facilityType': 'World Largest Single Semiconductor Mega Fabrication Campus',
      'parentFirm': 'Samsung Electronics [005930:KS]',
      'coords': [37.038, 127.054],
      'specs': [
        { 'label': 'Total Campus Land Area', 'value': '2.89 Million sq meters (Equivalent to 400 Soccer Pitches)' },
        { 'label': 'Cleanroom Height', 'value': '6 Floors High-Ceiling Ultra-Clean Chambers' },
        { 'label': 'Silicon Wafer Technology', 'value': '1b-nm DRAM, 9th-Gen V-NAND & 3nm GAA Foundry Lines' }
      ],
      'description': "The most colossal semiconductor cleanroom facility on the planet, producing the majority of the world's DRAM and V-NAND flash storage memory."
    },
    'sk_icheon': {
      'title': '🔬 SK Hynix Icheon M16 EUV Memory Fab (Gyeonggi-do, South Korea)',
      'facilityType': 'Next-Generation HBM3E & 1b-nm DRAM Manufacturing Center',
      'parentFirm': 'SK Hynix Inc [000660:KS]',
      'coords': [37.258, 127.485],
      'specs': [
        { 'label': 'Fab Floor Space', 'value': '57,000 sq meters (Twin-Line Structure)' },
        { 'label': 'High-Bandwidth Memory (HBM3E)', 'value': 'Advanced Mass Reflow Molded Underfill (MR-MUF) Packaging' },
        { 'label': 'Global AI Memory Share', 'value': 'Primary HBM Supplier for NVIDIA Hopper & Blackwell Platforms' }
      ],
      'description': "SK Hynix's flagship M16 fab where extreme ultraviolet lithography is applied to DRAM wafers, coupled with packaging lines that stack 12-layer HBM3E chips with thermal conduction."
    },

    # ── UAE NANOS ──
    'dpworld_jebelali': {
      'title': '🚢 DP World Jebel Ali Port & Terminal 3 Mega Container Facility (Dubai, UAE)',
      'facilityType': 'World Largest Man-Made Harbor & Automated Maritime Transshipment Hub',
      'parentFirm': 'DP World Ltd [DPW:AE]',
      'coords': [24.985, 55.068],
      'specs': [
        { 'label': 'Total Port Container Capacity', 'value': '19.3 Million TEUs Annual Capacity' },
        { 'label': 'Automated Rail-Mounted Gantry (ARMG)', 'value': 'Remotely Controlled Container Cranes' },
        { 'label': 'Jebel Ali Free Zone (JAFZA)', 'value': '9,500+ Companies from 140 Countries in Adjacent Free Zone' }
      ],
      'description': "The undisputed logistics anchor of the Middle East, linking maritime routes between East Asia and Europe while serving the trade flow of 2 billion people."
    },
    'airarabia_sharjah': {
      'title': '✈️ Air Arabia Sharjah International Airport Maintenance & Operations Hub',
      'facilityType': 'Low-Cost Carrier Flight Operations & A320 Fleet Engineering Hangar',
      'parentFirm': 'Air Arabia PJSC [AIRARABIA:AE]',
      'coords': [25.328, 55.517],
      'specs': [
        { 'label': 'Fleet Composition', 'value': '75+ Airbus A320 & A321 Neo LR Aircraft' },
        { 'label': 'Passenger Load Factor', 'value': '82.5% Average Annual Seat Factor' },
        { 'label': 'Ancillary Revenue Model', 'value': 'Pre-Selected Meals, Baggage & Seat Selection Yields' }
      ],
      'description': "The operational home of the Middle East and North Africa's first and largest low-cost airline, maintaining the lowest seat-kilometer operating cost in the region."
    }
}

print(f"Total nanos loaded in GLOBAL_NANOS: {len(GLOBAL_NANOS)}")

