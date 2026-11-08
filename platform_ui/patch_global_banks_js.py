with open('platform_ui/bmap_js_template.js', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Variable declaration
target_decl = "var branchesCompact = __BRANCHES_JSON__;"
replacement_decl = """var branchesCompact = __BRANCHES_JSON__;
  var globalBankingTitans = __GLOBAL_BANKING_JSON__;"""

if target_decl in text:
    text = text.replace(target_decl, replacement_decl, 1)
    print("1. Injected globalBankingTitans declaration!")
else:
    print("WARNING 1: target_decl not found!")

# 2. SUGGESTED_DATASETS label
target_sug = "{ key: 'bank_branches', label: 'Bank Branches (US)', count: '1,675', color: '#ffaa00', category: 'FINANCIAL' },"
replacement_sug = "{ key: 'bank_branches', label: 'Bank Branches & Wealth Hubs (Global G-SIBs & US FDIC)', count: '1,715+', color: '#c084fc', category: 'FINANCIAL' },"

if target_sug in text:
    text = text.replace(target_sug, replacement_sug, 1)
    print("2. Injected SUGGESTED_DATASETS label!")
else:
    print("WARNING 2: target_sug not found!")

# 3. initBankBranchesLayer
target_init_bank = """  function initBankBranchesLayer() {
    datasetLayerGroups['bank_branches'] = L.layerGroup().addTo(leafletMap);
    renderBankBranchesOnMap(branchesCompact);
  }"""

replacement_init_bank = """  function initBankBranchesLayer() {
    datasetLayerGroups['bank_branches'] = L.layerGroup().addTo(leafletMap);
    renderBankBranchesOnMap(branchesCompact, globalBankingTitans);
  }"""

if target_init_bank in text:
    text = text.replace(target_init_bank, replacement_init_bank, 1)
    print("3. Injected initBankBranchesLayer call!")
else:
    print("WARNING 3: target_init_bank not found!")

# 4. Replace renderBankBranchesOnMap
target_render_fn_start = text.find("function renderBankBranchesOnMap(branches) {")
target_render_fn_end = text.find("  // Helper to display details for generic infrastructure", target_render_fn_start)

if target_render_fn_start != -1 and target_render_fn_end != -1:
    old_render_fn = text[target_render_fn_start:target_render_fn_end]
    new_render_fn = """function renderBankBranchesOnMap(branches, globalTitans) {
    var group = datasetLayerGroups['bank_branches'];
    if (!group) return;
    group.clearLayers();

    var canvasRenderer = window.masterCanvasRenderer || L.canvas({ padding: 0.5, tolerance: 14 });

    // 1. RENDER GLOBAL BANKING TITANS & G-SIBS WORLDWIDE (INDIA, GCC, EUROPE, ASIA, US)
    var titansToRender = globalTitans || globalBankingTitans || [];
    titansToRender.forEach(function(g) {
      var radius = Math.min(20, Math.max(8, Math.log10((g.assetsM || g.depM || 1000) + 1) * 3.4));
      var isFlagship = (g.region === 'India' || g.region === 'Middle East / GCC');
      var marker = L.circleMarker([g.lat, g.lon], {
        renderer: canvasRenderer,
        radius: radius,
        fillColor: isFlagship ? '#ffd700' : '#c084fc',
        color: '#ffffff',
        weight: 2,
        opacity: 0.95,
        fillOpacity: 0.88
      });

      function onGlobalBankHover(e) {
        marker.setRadius(radius + 4);
        marker.setStyle({ weight: 3, color: '#00e5ff', fillOpacity: 1 });
        showUniversalInspector('bank_branch', g, [g.lat, g.lon]);
      }
      function onGlobalBankOut(e) {
        marker.setRadius(radius);
        marker.setStyle({ weight: 2, color: '#ffffff', fillOpacity: 0.88 });
      }
      function onGlobalBankClick(e) {
        marker.setRadius(radius + 5);
        marker.setStyle({ weight: 3.5, color: '#ffd700', fillOpacity: 1 });
        showUniversalInspector('bank_branch', g, [g.lat, g.lon]);
        leafletMap.panTo([g.lat, g.lon]);
      }

      marker.on('mouseover mousemove', onGlobalBankHover);
      marker.on('mouseout', onGlobalBankOut);
      marker.on('click', onGlobalBankClick);

      var gTooltipHtml = '<div style="font-family:var(--font-mono);font-size:10px;background:rgba(5,8,15,0.96);border:1.5px solid ' + (isFlagship ? '#ffd700' : '#c084fc') + ';padding:7px 11px;border-radius:4px;box-shadow:0 6px 22px rgba(0,0,0,0.9);color:#fff;min-width:210px;line-height:1.4;">' +
        '<div style="color:' + (isFlagship ? '#ffd700' : '#c084fc') + ';font-weight:bold;font-size:11.5px;">🏛️ ' + g.name + '</div>' +
        '<div style="color:#38bdf8;font-weight:700;">' + g.country + ' · ' + g.regulator + '</div>' +
        '<div><span style="color:#94a3b8;">Classification:</span> ' + g.type + '</div>' +
        '<div><span style="color:#94a3b8;">Total Assets:</span> <strong style="color:#00e676;">$' + (g.assetsM >= 1000 ? (g.assetsM / 1000).toFixed(1) + 'B' : g.assetsM + 'M') + ' USD</strong></div>' +
        '<div><span style="color:#94a3b8;">Deposits / Tier-1:</span> <strong style="color:#ffaa00;">$' + (g.depM >= 1000 ? (g.depM / 1000).toFixed(1) + 'B' : g.depM + 'M') + '</strong> · ' + g.tier1 + '</div>' +
        '<div><span style="color:#94a3b8;">Network:</span> ' + g.branches_total + '</div>' +
        '<div style="margin-top:3px;padding-top:2px;border-top:1px dashed #1e2e44;color:#00e5ff;font-size:8.5px;">🖱️ Click for Global Sovereign & G-SIB Balance Sheet</div>' +
      '</div>';

      marker.bindTooltip(gTooltipHtml, {
        sticky: true,
        opacity: 0.98,
        className: 'bb-custom-tooltip'
      });

      group.addLayer(marker);
    });

    // 2. RENDER US FDIC MICRO-BRANCHES
    var usBranches = branches || [];
    usBranches.forEach(function(b) {
      var bId = b[0];
      var bankIdx = b[1];
      var lat = b[2];
      var lon = b[3];
      var depM = b[4];
      var stateIdx = b[5];
      var typeIdx = b[6];

      var radius = Math.min(18, Math.max(4, Math.log10(depM + 1) * 3.6));

      var marker = L.circleMarker([lat, lon], {
        renderer: canvasRenderer,
        radius: radius,
        fillColor: '#a855f7',
        color: '#ffffff',
        weight: 1.2,
        opacity: 0.85,
        fillOpacity: 0.6
      });

      var bName = banksLookup[bankIdx] || 'FDIC Insured Financial Institution';
      var state = statesLookup[stateIdx] || 'US';
      var bType = typesLookup[typeIdx] || 'Commercial Banking Branch';

      var branchObj = {
        id: bId,
        name: bName + ' (Branch #' + bId + ')',
        bank: bName,
        lat: lat,
        lon: lon,
        depM: depM,
        state: state,
        type: bType,
        country: 'United States',
        address: 'Branch Location · ' + state + ', United States'
      };

      function onBranchHover(e) {
        marker.setRadius(radius + 3.5);
        marker.setStyle({ weight: 2.5, color: '#ffffff', fillOpacity: 0.95 });
        showUniversalInspector('bank_branch', branchObj, [lat, lon]);
      }
      function onBranchOut(e) {
        marker.setRadius(radius);
        marker.setStyle({ weight: 1.2, color: '#ffffff', fillOpacity: 0.6 });
      }
      function onBranchClick(e) {
        marker.setRadius(radius + 4.5);
        marker.setStyle({ weight: 3, color: '#00e5ff', fillOpacity: 1 });
        showUniversalInspector('bank_branch', branchObj, [lat, lon]);
        leafletMap.panTo([lat, lon]);
      }

      marker.on('mouseover mousemove', onBranchHover);
      marker.on('mouseout', onBranchOut);
      marker.on('click', onBranchClick);

      var bTooltipHtml = '<div style="font-family:var(--font-mono);font-size:10px;background:rgba(5,8,15,0.96);border:1.5px solid #a855f7;padding:6px 10px;border-radius:4px;box-shadow:0 6px 20px rgba(0,0,0,0.85);color:#fff;min-width:190px;line-height:1.4;">' +
        '<div style="color:#a855f7;font-weight:bold;font-size:11px;">🏛️ ' + bName + '</div>' +
        '<div style="color:#38bdf8;">Branch #' + bId + ' · ' + state + ' (US)</div>' +
        '<div><span style="color:#94a3b8;">Type:</span> ' + bType + '</div>' +
        '<div><span style="color:#94a3b8;">Branch Deposits:</span> <strong style="color:#00e676;">$' + depM.toFixed(1) + 'M USD</strong></div>' +
        '<div style="margin-top:3px;padding-top:2px;border-top:1px dashed #1e2e44;color:#ffaa00;font-size:8.5px;">🖱️ Click for Full FDIC Balance Sheet</div>' +
      '</div>';

      marker.bindTooltip(bTooltipHtml, {
        sticky: true,
        opacity: 0.98,
        className: 'bb-custom-tooltip'
      });

      group.addLayer(marker);
    });
  }

"""
    text = text[:target_render_fn_start] + new_render_fn + text[target_render_fn_end:]
    print("4. Successfully upgraded renderBankBranchesOnMap!")
else:
    print("WARNING 4: renderBankBranchesOnMap bounds not found!")

# 5. Upgrade filterBankBranches & resetBankFilter
target_filter_start = text.find("window.filterBankBranches = function() {")
target_filter_end = text.find("  // ═══════════════════════════════════════════════════════════════\n  // ── LAYER 2: PIPELINES", target_filter_start)

if target_filter_start != -1 and target_filter_end != -1:
    new_filter_fn = """window.filterBankBranches = function() {
    var regSelect = document.getElementById('filter_bank_region');
    var nameSelect = document.getElementById('filter_bank_name');
    var branchSelect = document.getElementById('filter_bank_branch');
    var stateSelect = document.getElementById('filter_bank_state');
    var depSlider = document.getElementById('slider_bank_dep');

    var selRegion = regSelect ? regSelect.value : 'ALL';
    var selBank = nameSelect ? nameSelect.value : 'ALL';
    var selBranch = branchSelect ? branchSelect.value : 'ALL';
    var selState = stateSelect ? stateSelect.value : 'ALL';
    var minDepM = depSlider ? parseInt(depSlider.value) : 0;

    bankFilterState.region = selRegion;
    bankFilterState.name = selBank;
    bankFilterState.branch = selBranch;
    bankFilterState.state = selState;
    bankFilterState.minDep = minDepM;

    // Filter Global Titans (India, GCC, Europe, Asia, Americas)
    var filteredTitans = [];
    if (selRegion !== 'US') {
      filteredTitans = (globalBankingTitans || []).filter(function(g) {
        if (selRegion === 'INDIA' && g.scope !== 'india') return false;
        if (selRegion === 'GCC' && g.scope !== 'gcc') return false;
        if (selRegion === 'EUROPE' && g.scope !== 'europe') return false;
        if (selRegion === 'ASIA' && g.scope !== 'asia') return false;
        if (selRegion === 'AMERICAS' && g.scope !== 'americas') return false;

        if (selBank !== 'ALL') {
          var nS = selBank.toLowerCase().replace(', na', '').replace(' bank', '').trim();
          var nB = (g.bank || g.name).toLowerCase().replace(', na', '').replace(' bank', '').trim();
          if (!nB.includes(nS) && !nS.includes(nB)) return false;
        }

        if (minDepM > 0 && (g.depM || g.assetsM || 0) < minDepM) return false;
        return true;
      });
    }

    // Filter US FDIC branches
    var filteredUs = [];
    if (selRegion === 'ALL' || selRegion === 'US') {
      filteredUs = branchesCompact.filter(function(b) {
        var bankName = banksLookup[b[1]] || '';
        var depM = b[4];
        var bState = statesLookup[b[5]] || '';
        var bType = typesLookup[b[6]] || '';

        if (selBank !== 'ALL') {
          var normSel = selBank.toLowerCase().replace(', na', '').replace(' bank', '').trim();
          var normName = bankName.toLowerCase().replace(', na', '').replace(' bank', '').trim();
          if (!normName.includes(normSel) && !normSel.includes(normName)) return false;
        }
        if (selBranch !== 'ALL' && bType.indexOf(selBranch) === -1) return false;
        if (selState !== 'ALL' && bState !== selState) return false;
        if (depM < minDepM) return false;
        return true;
      });
    }

    renderBankBranchesOnMap(filteredUs, filteredTitans);

    var totalCount = filteredUs.length + filteredTitans.length;
    var lbl = document.getElementById('lbl_bank_dep_val');
    if (lbl) {
      lbl.textContent = '$' + minDepM + 'M+ (' + totalCount + ' Hubs & Branches)';
    }
  };

  window.resetBankFilter = function() {
    if (document.getElementById('filter_bank_region')) document.getElementById('filter_bank_region').value = 'ALL';
    if (document.getElementById('filter_bank_name')) document.getElementById('filter_bank_name').value = 'ALL';
    if (document.getElementById('filter_bank_branch')) document.getElementById('filter_bank_branch').value = 'ALL';
    if (document.getElementById('filter_bank_state')) document.getElementById('filter_bank_state').value = 'ALL';
    if (document.getElementById('slider_bank_dep')) document.getElementById('slider_bank_dep').value = 0;
    filterBankBranches();
  };

  // Quick Bank Geospatial Fit Presets
  window.fitGlobalBanks = function() {
    if (leafletMap) leafletMap.flyTo([22.0, 30.0], 2.5, { duration: 1.4 });
    var reg = document.getElementById('filter_bank_region');
    if (reg) { reg.value = 'GLOBAL'; filterBankBranches(); }
  };
  window.fitIndiaBanks = function() {
    if (leafletMap) leafletMap.flyTo([19.066, 72.867], 12, { duration: 1.4 }); // Mumbai BKC
    var reg = document.getElementById('filter_bank_region');
    if (reg) { reg.value = 'INDIA'; filterBankBranches(); }
  };
  window.fitGccBanks = function() {
    if (leafletMap) leafletMap.flyTo([24.767, 46.638], 11, { duration: 1.4 }); // Riyadh KAFD
    var reg = document.getElementById('filter_bank_region');
    if (reg) { reg.value = 'GCC'; filterBankBranches(); }
  };
  window.fitEuropeBanks = function() {
    if (leafletMap) leafletMap.flyTo([50.11, 8.68], 5, { duration: 1.4 }); // Frankfurt / Zurich / London
    var reg = document.getElementById('filter_bank_region');
    if (reg) { reg.value = 'EUROPE'; filterBankBranches(); }
  };
  window.fitAsiaBanks = function() {
    if (leafletMap) leafletMap.flyTo([1.28, 103.85], 5, { duration: 1.4 }); // Singapore / Tokyo
    var reg = document.getElementById('filter_bank_region');
    if (reg) { reg.value = 'ASIA'; filterBankBranches(); }
  };

"""
    text = text[:target_filter_start] + new_filter_fn + text[target_filter_end:]
    print("5. Successfully upgraded filterBankBranches & resetBankFilter!")
else:
    print("WARNING 5: filterBankBranches bounds not found!")

# 6. Upgrade showUniversalInspector bank_branch branch
target_inspect_bank = text.find("} else if (type === 'bank_branch' || type === 'manhattan_branch') {")
target_inspect_bank_end = text.find("} else if (type === 'cable' || type === 'submarine_cables') {", target_inspect_bank)

if target_inspect_bank != -1 and target_inspect_bank_end != -1:
    new_inspect_bank = """} else if (type === 'bank_branch' || type === 'manhattan_branch') {
      var isGlobal = !!item.regulator;
      nameEl.textContent = '🏛️ ' + (item.name || item.bank || 'Commercial Banking Branch');
      typeEl.textContent = isGlobal ? (item.type || 'Global Banking Titan') : 'FDIC Insured (US)';
      typeEl.style.background = isGlobal ? '#4a044e' : '#3b0764';
      typeEl.style.color = isGlobal ? '#f472b6' : '#c084fc';

      if (l1) l1.textContent = isGlobal ? 'Regulatory Authority:' : 'FDIC Status:';
      statEl.textContent = isGlobal ? ('● ' + item.regulator) : '● Active / FDIC Insured';
      statEl.style.color = '#00e676';

      if (l2) l2.textContent = isGlobal ? 'Institution / Ticker:' : 'Institution:';
      imoEl.textContent = (item.bank || 'Bank') + (item.symbol ? ' [' + item.symbol + ']' : '') + (item.country ? ' · ' + item.country : '');

      if (l3) l3.textContent = 'Headquarters / Address:';
      ownerEl.textContent = item.address || 'Commercial Banking Center';

      if (l4) l4.textContent = isGlobal ? 'Consolidated Assets:' : 'Branch Deposits:';
      destEl.textContent = isGlobal
        ? ('$' + (item.assetsM >= 1000 ? (item.assetsM / 1000).toFixed(2) + 'B' : item.assetsM + 'M') + ' USD')
        : ('$' + (item.depM ? item.depM.toLocaleString() : (item.dep_branch ? (item.dep_branch/1000).toFixed(1) : '1,214.6')) + 'M');
      destEl.style.color = '#00e676';

      if (l5) l5.textContent = isGlobal ? 'Tier-1 Capital / Deposits:' : 'Company Domestic Assets:';
      berthEl.textContent = isGlobal
        ? ((item.tier1 || '15.2% CET-1') + ' · $' + (item.depM >= 1000 ? (item.depM / 1000).toFixed(2) + 'B' : item.depM + 'M') + ' Dep')
        : (item.assets_company ? '$' + (item.assets_company/1000000000).toFixed(2) + 'B' : '$3,914.1B');

      if (l6) l6.textContent = isGlobal ? 'Branch Network Footprint:' : 'Branch Classification:';
      speedEl.textContent = isGlobal ? (item.branches_total || 'Global Banking Flagship') : (item.type || 'Commercial Banking Center');
      speedEl.style.color = '#38bdf8';

      if (l7) l7.textContent = 'WGS84 Coordinates:';
      draftEl.textContent = item.lat.toFixed(4) + '°, ' + item.lon.toFixed(4) + '°';
    """
    text = text[:target_inspect_bank] + new_inspect_bank + text[target_inspect_bank_end:]
    print("6. Successfully upgraded showUniversalInspector for global bank branches!")
else:
    print("WARNING 6: showUniversalInspector bank_branch not found!")

# 7. Upgrade the Active Card UI in renderActiveDatasetCards
target_card_start = text.find("// CARD 4: BANK BRANCHES (US)")
target_card_end = text.find("// CARD 5: CRUDE OIL PIPELINES", target_card_start)

if target_card_start != -1 and target_card_end != -1:
    new_card_html = """// CARD 4: BANK BRANCHES & GLOBAL WEALTH HUBS
    if (activeLayers.bank_branches) {
      var bCard = document.createElement('div');
      bCard.style.cssText = 'background:#080e18;border:1px solid #a855f7;border-radius:4px;padding:8px 10px;font-size:9.5px;';
      bCard.innerHTML = 
        '<div style="display:flex;justify-content:space-between;align-items:center;border-bottom:1px solid #162438;padding-bottom:4px;margin-bottom:6px;">' +
          '<div style="display:flex;align-items:center;gap:4px;">' +
            '<span style="color:#ffaa00;">▾</span>' +
            '<strong style="color:#c084fc;font-size:10.5px;">Bank Branches &amp; Global Wealth Hubs</strong>' +
          '</div>' +
          '<div style="display:flex;align-items:center;gap:6px;">' +
            '<span style="color:#64748b;font-size:9px;cursor:pointer;">≡▾</span>' +
            '<span onclick="window.removeBmapDataset(\\'bank_branches\\')" style="color:#94a3b8;cursor:pointer;font-weight:bold;">✕</span>' +
          '</div>' +
        '</div>' +
        '<div style="display:flex;flex-direction:column;gap:4px;">' +
          '<div style="display:flex;justify-content:space-between;align-items:center;">' +
            '<span style="color:#94a3b8;">Jurisdiction</span>' +
            '<select id="filter_bank_region" onchange="filterBankBranches()" style="background:#05080e;color:#00e5ff;border:1px solid #0284c7;font-size:9px;border-radius:2px;width:130px;outline:none;font-weight:700;">' +
              '<option value="ALL">Worldwide (Global &amp; US)</option>' +
              '<option value="GLOBAL">Global Systemic G-SIBs</option>' +
              '<option value="INDIA">India (RBI / GIFT City IFSC)</option>' +
              '<option value="GCC">Middle East &amp; GCC (SAMA / CBUAE)</option>' +
              '<option value="EUROPE">Europe &amp; UK (G-SIBs &amp; Swiss)</option>' +
              '<option value="ASIA">Asia-Pacific (Tokyo, SG, HK, CN)</option>' +
              '<option value="US">United States (FDIC 1,675)</option>' +
            '</select>' +
          '</div>' +
          '<div style="display:flex;justify-content:space-between;align-items:center;">' +
            '<span style="color:#94a3b8;">Name</span>' +
            '<select id="filter_bank_name" onchange="filterBankBranches()" style="background:#05080e;color:#ffaa00;border:1px solid #203a5e;font-size:9px;border-radius:2px;width:130px;outline:none;">' +
              '<option value="ALL">All Global Institutions</option>' +
              '<option value="State Bank of India">State Bank of India (SBI)</option>' +
              '<option value="HDFC Bank">HDFC Bank</option>' +
              '<option value="ICICI Bank">ICICI Bank</option>' +
              '<option value="Kotak Mahindra Bank">Kotak Mahindra Bank</option>' +
              '<option value="Saudi National Bank">Saudi National Bank (SNB)</option>' +
              '<option value="Al Rajhi Bank">Al Rajhi Bank</option>' +
              '<option value="First Abu Dhabi Bank">First Abu Dhabi Bank (FAB)</option>' +
              '<option value="Emirates NBD">Emirates NBD</option>' +
              '<option value="HSBC">HSBC Holdings</option>' +
              '<option value="Barclays">Barclays</option>' +
              '<option value="UBS Group">UBS Group</option>' +
              '<option value="BNP Paribas">BNP Paribas</option>' +
              '<option value="Deutsche Bank">Deutsche Bank</option>' +
              '<option value="DBS Bank">DBS Bank (Singapore)</option>' +
              '<option value="MUFG">MUFG Bank (Japan)</option>' +
              '<option value="ICBC">ICBC (China)</option>' +
              '<option value="JPMorgan Chase">JPMorgan Chase (US)</option>' +
              '<option value="Bank of America">Bank of America (US)</option>' +
              '<option value="Wells Fargo">Wells Fargo (US)</option>' +
              '<option value="Citibank">Citigroup (US)</option>' +
            '</select>' +
          '</div>' +
          '<div style="display:flex;justify-content:space-between;align-items:center;">' +
            '<span style="color:#94a3b8;">Branch</span>' +
            '<select id="filter_bank_branch" onchange="filterBankBranches()" style="background:#05080e;color:#38bdf8;border:1px solid #203a5e;font-size:9px;border-radius:2px;width:130px;outline:none;">' +
              '<option value="ALL">All Branch Types</option>' +
              '<option value="Global Headquarters">Global Headquarters</option>' +
              '<option value="Private Wealth">Private Wealth Hub</option>' +
              '<option value="Full Service">Full Service Commercial</option>' +
              '<option value="Commercial">Commercial Vault</option>' +
            '</select>' +
          '</div>' +
          '<div>' +
            '<div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:2px;">' +
              '<span style="color:#94a3b8;">Deposits / Assets (M)</span>' +
              '<span id="lbl_bank_dep_val" style="color:#ffaa00;font-weight:bold;">$0M+ (1,715+)</span>' +
            '</div>' +
            '<input type="range" id="slider_bank_dep" min="0" max="5000" step="50" value="0" oninput="filterBankBranches()" style="width:100%;accent-color:#ffaa00;cursor:pointer;height:5px;">' +
          '</div>' +
          '<div style="display:flex;justify-content:space-between;align-items:center;">' +
            '<span style="color:#94a3b8;">US State</span>' +
            '<select id="filter_bank_state" onchange="filterBankBranches()" style="background:#05080e;color:#34d399;border:1px solid #203a5e;font-size:9px;border-radius:2px;width:130px;outline:none;">' +
              '<option value="ALL">All States (US)</option>' +
              '<option value="NY">New York (NY)</option>' +
              '<option value="CA">California (CA)</option>' +
              '<option value="TX">Texas (TX)</option>' +
              '<option value="IL">Illinois (IL)</option>' +
              '<option value="NC">North Carolina (NC)</option>' +
              '<option value="FL">Florida (FL)</option>' +
            '</select>' +
          '</div>' +
          '<div style="display:flex;gap:4px;margin-top:6px;flex-wrap:wrap;">' +
            '<button onclick="window.fitGlobalBanks()" style="flex:1;min-width:55px;background:#1e3a5f;color:#00e5ff;border:1px solid #0284c7;padding:3px;font-size:8.5px;font-weight:bold;border-radius:2px;cursor:pointer;">🌐 Global</button>' +
            '<button onclick="window.fitIndiaBanks()" style="flex:1;min-width:55px;background:#14532d;color:#86efac;border:1px solid #16a34a;padding:3px;font-size:8.5px;font-weight:bold;border-radius:2px;cursor:pointer;">🇮🇳 India</button>' +
            '<button onclick="window.fitGccBanks()" style="flex:1;min-width:55px;background:#78350f;color:#fcd34d;border:1px solid #d97706;padding:3px;font-size:8.5px;font-weight:bold;border-radius:2px;cursor:pointer;">🇸🇦 GCC</button>' +
            '<button onclick="window.fitEuropeBanks()" style="flex:1;min-width:55px;background:#312e81;color:#a5b4fc;border:1px solid #4f46e5;padding:3px;font-size:8.5px;font-weight:bold;border-radius:2px;cursor:pointer;">🇪🇺 Europe</button>' +
            '<button onclick="window.fitUsBounds()" style="flex:1;min-width:55px;background:#0284c7;color:#fff;border:none;padding:3px;font-size:8.5px;font-weight:bold;border-radius:2px;cursor:pointer;">🇺🇸 US</button>' +
            '<button onclick="window.resetBankFilter()" style="background:#1e293b;color:#94a3b8;border:1px solid #334155;padding:3px 6px;font-size:8.5px;border-radius:2px;cursor:pointer;">Reset</button>' +
          '</div>' +
        '</div>';
      container.appendChild(bCard);
    }

    """
    text = text[:target_card_start] + new_card_html + text[target_card_end:]
    print("7. Successfully upgraded Card UI in renderActiveDatasetCards!")
else:
    print("WARNING 7: Card UI bounds not found!")

with open('platform_ui/bmap_js_template.js', 'w', encoding='utf-8') as f:
    f.write(text)
print("Updated platform_ui/bmap_js_template.js successfully!")

