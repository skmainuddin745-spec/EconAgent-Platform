with open('platform_ui/bmap_js_template.js', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Add layer aliases in initGlobalInfrastructureLayers
target_aliases = "addPointsLayer('cyclones', globalCyclones, '#ef4444', 7, false);"
replacement_aliases = """addPointsLayer('cyclones', globalCyclones, '#ef4444', 7, false);

    // Aliases for Map Content Sublayer checkboxes (Natural Gas & Commodities drawers)
    datasetLayerGroups['underground_storage'] = datasetLayerGroups['storage_terminals'];
    datasetLayerGroups['lng_berths'] = datasetLayerGroups['lng_terminals'];
    datasetLayerGroups['chemical'] = datasetLayerGroups['refineries'];
    datasetLayerGroups['hubs'] = datasetLayerGroups['gas_hubs'];"""

if target_aliases in text:
    text = text.replace(target_aliases, replacement_aliases, 1)
    print("Successfully injected layer aliases!")
else:
    print("WARNING: target_aliases not found!")

# 2. Add border colors in showUniversalInspector
target_border = "} else if (type === 'cyclone' || type === 'cyclones') {\n      pop.style.borderColor = '#f43f5e';"
replacement_border = """} else if (type === 'cyclone' || type === 'cyclones') {
      pop.style.borderColor = '#f43f5e';
    } else if (type === 'lng_terminals' || type === 'lng_berths') {
      pop.style.borderColor = '#06b6d4';
    } else if (type === 'storage_terminals' || type === 'underground_storage') {
      pop.style.borderColor = '#60a5fa';
    } else if (type === 'gas_hubs' || type === 'hubs') {
      pop.style.borderColor = '#fb923c';
    } else if (type === 'data_centers') {
      pop.style.borderColor = '#22c55e';
    } else if (type === 'semiconductor_fabs' || type === 'semiconductors') {
      pop.style.borderColor = '#c084fc';
    } else if (type === 'fertilizers') {
      pop.style.borderColor = '#86efac';
    } else if (type === 'mining_hubs') {
      pop.style.borderColor = '#fdba74';"""

if target_border in text:
    text = text.replace(target_border, replacement_border, 1)
    print("Successfully injected border colors!")
else:
    print("WARNING: target_border not found!")

# 3. Add rich inspector branches before the generic else
target_else = "    } else {\n      // Generic facility / seaport / refinery / cavern"
rich_branches = """    } else if (type === 'lng_terminals' || type === 'lng_berths') {
      nameEl.textContent = '⛽ ' + item.name;
      typeEl.textContent = 'LNG Liquefaction / Export Terminal';
      typeEl.style.background = '#083344';
      typeEl.style.color = '#06b6d4';
      if (l1) l1.textContent = 'Terminal Status:';
      statEl.textContent = '● ' + (item.status || 'Active Operational');
      statEl.style.color = '#00e676';
      if (l2) l2.textContent = 'Country / Basin:';
      imoEl.textContent = item.country || 'Global LNG Hub';
      if (l3) l3.textContent = 'Operator / Owner:';
      ownerEl.textContent = item.operator || 'QatarEnergy / Cheniere / TotalEnergies';
      if (l4) l4.textContent = 'Nameplate Capacity:';
      destEl.textContent = item.cap || item.capacity || 'Strategic LNG Hub';
      destEl.style.color = '#00e5ff';
      if (l5) l5.textContent = 'Terminal Type:';
      berthEl.textContent = item.type || 'Export / Import Terminal';
      if (l6) l6.textContent = 'Data Source:';
      speedEl.textContent = item.source || 'EIA / GIIGNL Global LNG';
      speedEl.style.color = '#ffaa00';
      if (l7) l7.textContent = 'WGS84 Coordinates:';
      draftEl.textContent = item.lat.toFixed(4) + '°, ' + item.lon.toFixed(4) + '°';
    } else if (type === 'storage_terminals' || type === 'underground_storage') {
      nameEl.textContent = '🛢️ ' + item.name;
      typeEl.textContent = 'Strategic Hydrocarbon Storage';
      typeEl.style.background = '#1e3a8a';
      typeEl.style.color = '#60a5fa';
      if (l1) l1.textContent = 'Storage Status:';
      statEl.textContent = '● ' + (item.status || 'Benchmark Delivery Hub');
      statEl.style.color = '#00e676';
      if (l2) l2.textContent = 'Location / Country:';
      imoEl.textContent = item.country || 'United States';
      if (l3) l3.textContent = 'Operators / Pipeline Links:';
      ownerEl.textContent = item.operator || 'Plains / Enbridge / Enterprise';
      if (l4) l4.textContent = 'Total Working Capacity:';
      destEl.textContent = item.cap || item.capacity || '90M Barrels Crude Storage';
      destEl.style.color = '#60a5fa';
      if (l5) l5.textContent = 'Delivery Grade:';
      berthEl.textContent = 'NYMEX WTI Physical Delivery Hub';
      if (l6) l6.textContent = 'Data Source:';
      speedEl.textContent = item.source || 'EIA / Weekly Petroleum Status Report';
      speedEl.style.color = '#38bdf8';
      if (l7) l7.textContent = 'WGS84 Coordinates:';
      draftEl.textContent = item.lat.toFixed(4) + '°, ' + item.lon.toFixed(4) + '°';
    } else if (type === 'gas_hubs' || type === 'hubs') {
      nameEl.textContent = '🔥 ' + item.name;
      typeEl.textContent = 'Natural Gas Physical Hub';
      typeEl.style.background = '#431407';
      typeEl.style.color = '#fb923c';
      if (l1) l1.textContent = 'Hub Status:';
      statEl.textContent = '● ' + (item.status || 'Benchmark Active Hub');
      statEl.style.color = '#00e676';
      if (l2) l2.textContent = 'Country / Grid:';
      imoEl.textContent = item.country || 'North American Gas Grid';
      if (l3) l3.textContent = 'Hub Operator:';
      ownerEl.textContent = item.operator || 'Sabine Pipe Line / Enbridge';
      if (l4) l4.textContent = 'Pricing Benchmark:';
      destEl.textContent = item.cap || 'NYMEX Front-Month Delivery Point';
      destEl.style.color = '#ffaa00';
      if (l5) l5.textContent = 'Pipeline Interconnects:';
      berthEl.textContent = '16 Major Interstate Interconnects';
      if (l6) l6.textContent = 'Data Source:';
      speedEl.textContent = item.source || 'EIA / NYMEX Henry Hub Benchmark';
      speedEl.style.color = '#00e676';
      if (l7) l7.textContent = 'WGS84 Coordinates:';
      draftEl.textContent = item.lat.toFixed(4) + '°, ' + item.lon.toFixed(4) + '°';
    } else if (type === 'data_centers') {
      nameEl.textContent = '💻 ' + item.name;
      typeEl.textContent = 'Hyperscale Cloud & AI Hub';
      typeEl.style.background = '#052e16';
      typeEl.style.color = '#22c55e';
      if (l1) l1.textContent = 'Facility Status:';
      statEl.textContent = '● ' + (item.status || 'Active Hyperscale');
      statEl.style.color = '#00e676';
      if (l2) l2.textContent = 'Country / Region:';
      imoEl.textContent = item.country || 'Global Cloud Corridor';
      if (l3) l3.textContent = 'Hyperscale Operators:';
      ownerEl.textContent = item.operators || item.operator || 'AWS, Azure, Google Cloud, Equinix';
      if (l4) l4.textContent = 'Power Capacity:';
      destEl.textContent = item.capacity || '3,000+ MW AI/Cloud Cluster';
      destEl.style.color = '#22c55e';
      if (l5) l5.textContent = 'Traffic Share:';
      berthEl.textContent = '70% Global Internet Fiber Traffic';
      if (l6) l6.textContent = 'Telemetry:';
      speedEl.textContent = 'PUE 1.15 · Sub-Millisecond Backbone Latency';
      speedEl.style.color = '#00e5ff';
      if (l7) l7.textContent = 'WGS84 Coordinates:';
      draftEl.textContent = item.lat.toFixed(4) + '°, ' + item.lon.toFixed(4) + '°';
    } else if (type === 'semiconductor_fabs' || type === 'semiconductors') {
      nameEl.textContent = '🔬 ' + item.name;
      typeEl.textContent = 'Semiconductor Fabrication GigaFab';
      typeEl.style.background = '#3b0764';
      typeEl.style.color = '#c084fc';
      if (l1) l1.textContent = 'Fab Status:';
      statEl.textContent = '● ' + (item.status || 'High-Volume Production');
      statEl.style.color = '#00e676';
      if (l2) l2.textContent = 'Country / Foundry:';
      imoEl.textContent = item.country + ' · ' + (item.operator || 'TSMC / Intel / Samsung');
      if (l3) l3.textContent = 'Leading Node:';
      ownerEl.textContent = item.node || 'N3 / N2 Angstrom Class EUV';
      if (l4) l4.textContent = 'Monthly Wafer Runs:';
      destEl.textContent = '100,000+ 300mm Wafers/Month';
      destEl.style.color = '#c084fc';
      if (l5) l5.textContent = 'Lithography:';
      berthEl.textContent = 'ASML High-NA EUV Twinscan EXE';
      if (l6) l6.textContent = 'Data Source:';
      speedEl.textContent = item.source || 'Foundry SEC / IR Disclosures';
      speedEl.style.color = '#ffaa00';
      if (l7) l7.textContent = 'WGS84 Coordinates:';
      draftEl.textContent = item.lat.toFixed(4) + '°, ' + item.lon.toFixed(4) + '°';
    } else if (type === 'fertilizers') {
      nameEl.textContent = '🌾 ' + item.name;
      typeEl.textContent = 'Agri-Nutrient Manufacturing Complex';
      typeEl.style.background = '#14532d';
      typeEl.style.color = '#86efac';
      if (l1) l1.textContent = 'Production Status:';
      statEl.textContent = '● ' + (item.status || 'Active Underground / Chemical');
      statEl.style.color = '#00e676';
      if (l2) l2.textContent = 'Country / Region:';
      imoEl.textContent = item.country || 'Global Agricultural Belt';
      if (l3) l3.textContent = 'Operator / Owner:';
      ownerEl.textContent = item.operator || 'Nutrien / SABIC / CF Industries';
      if (l4) l4.textContent = 'Annual Output:';
      destEl.textContent = item.product || 'Strategic Fertilizer Supply';
      destEl.style.color = '#86efac';
      if (l5) l5.textContent = 'Nutrient Category:';
      berthEl.textContent = 'Potash / Ammonia / Urea / Phosphate';
      if (l6) l6.textContent = 'Data Source:';
      speedEl.textContent = item.source || 'IFA / Department of Energy';
      speedEl.style.color = '#ffaa00';
      if (l7) l7.textContent = 'WGS84 Coordinates:';
      draftEl.textContent = item.lat.toFixed(4) + '°, ' + item.lon.toFixed(4) + '°';
    } else if (type === 'mining_hubs') {
      nameEl.textContent = '⛏️ ' + item.name;
      typeEl.textContent = 'Tier-1 Critical Minerals Mine';
      typeEl.style.background = '#7c2d12';
      typeEl.style.color = '#fdba74';
      if (l1) l1.textContent = 'Mine Status:';
      statEl.textContent = '● ' + (item.status || 'Active Extraction');
      statEl.style.color = '#00e676';
      if (l2) l2.textContent = 'Country / Basin:';
      imoEl.textContent = item.country || 'Global Mineral Basin';
      if (l3) l3.textContent = 'Consortium Operators:';
      ownerEl.textContent = item.operator || 'BHP / Rio Tinto / Freeport';
      if (l4) l4.textContent = 'Annual Production:';
      destEl.textContent = item.product || '1.1M Metric Tons Copper/yr';
      destEl.style.color = '#fdba74';
      if (l5) l5.textContent = 'Mine Classification:';
      berthEl.textContent = 'Tier-1 World-Class Open Pit / Underground';
      if (l6) l6.textContent = 'Strategic Use:';
      speedEl.textContent = 'Energy Transition & Semiconductor Electrification';
      speedEl.style.color = '#00e5ff';
      if (l7) l7.textContent = 'WGS84 Coordinates:';
      draftEl.textContent = item.lat.toFixed(4) + '°, ' + item.lon.toFixed(4) + '°';
    } else {
      // Generic facility / seaport / refinery / cavern"""

if target_else in text:
    text = text.replace(target_else, rich_branches, 1)
    print("Successfully injected rich inspector branches!")
else:
    print("WARNING: target_else not found!")

# 4. Fix bank name selection in filterBankBranches
target_bank_match = "if (selBank !== 'ALL' && bankName.indexOf(selBank) === -1) return false;"
replacement_bank_match = """if (selBank !== 'ALL') {
        var normSel = selBank.toLowerCase().replace(', na', '').replace(' bank', '').trim();
        var normName = bankName.toLowerCase().replace(', na', '').replace(' bank', '').trim();
        if (!normName.includes(normSel) && !normSel.includes(normName)) return false;
      }"""

if target_bank_match in text:
    text = text.replace(target_bank_match, replacement_bank_match, 1)
    print("Successfully upgraded bank filter matching!")
else:
    print("WARNING: target_bank_match not found!")

with open('platform_ui/bmap_js_template.js', 'w', encoding='utf-8') as f:
    f.write(text)
print("Updated bmap_js_template.js successfully!")
