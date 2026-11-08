# F:\documents\SOIC\EconAgent_Platform\platform_ui\generate_rich_js.py
import json
import os
import sys

BASE_DIR = r"F:\documents\SOIC\EconAgent_Platform\platform_ui"
sys.path.insert(0, BASE_DIR)

from generate_full_bloomberg_suite import (
    CRUDE_PIPELINES,
    GAS_PIPELINES_NAM,
    BERTH_VISITS,
    MANHATTAN_STREET_BRANCHES,
    GREG_MORTIMER,
    WORLD_EQUITY_DATA,
    SPLC_NETWORKS,
    FXC_DATA,
    READ_NEWS_STORIES
)

def generate_js():
    # Convert datasets to JSON
    crude_pipes_json = json.dumps(CRUDE_PIPELINES)
    gas_pipes_json = json.dumps(GAS_PIPELINES_NAM)
    berths_json = json.dumps(BERTH_VISITS)
    manhattan_json = json.dumps(MANHATTAN_STREET_BRANCHES)
    greg_json = json.dumps(GREG_MORTIMER)
    equity_json = json.dumps(WORLD_EQUITY_DATA)
    splc_json = json.dumps(SPLC_NETWORKS)
    fxc_json = json.dumps(FXC_DATA)
    read_news_json = json.dumps(READ_NEWS_STORIES)

    js_code = f"""<script>
(function() {{
  // ═══════════════════════════════════════════════════════════════
  // ── DATA INJECTIONS FROM BLOOMBERG MAP DATASETS ──
  // ═══════════════════════════════════════════════════════════════
  var banksLookup = __BANKS_JSON__;
  var statesLookup = __STATES_JSON__;
  var typesLookup = __TYPES_JSON__;
  var branchesCompact = __BRANCHES_JSON__;

  var crudePipelines = {crude_pipes_json};
  var gasPipelines = {gas_pipes_json};
  var berthVisits = {berths_json};
  var manhattanBranches = {manhattan_json};
  var gregMortimer = {greg_json};
  var worldEquityData = {equity_json};
  var splcNetworks = {splc_json};
  var fxcData = {fxc_json};
  var readNewsStories = {read_news_json};

  var usBankBranches = branchesCompact.map(function(arr) {{
    var bName = banksLookup[arr[1]];
    var sCode = statesLookup[arr[5]];
    var tName = typesLookup[arr[6]];
    return {{
      id: 'bb_' + arr[0],
      name: bName,
      branch: bName + ' #' + (arr[0] * 7 % 8999 + 101) + ' (' + sCode + ')',
      lat: arr[2],
      lon: arr[3],
      dep: arr[4],
      state: sCode,
      type: tName
    }};
  }});

  // Global State
  var leafletMap = null;
  var baseTileLayers = {{}};
  var currentTileType = 'dark';
  var datasetLayerGroups = {{}};
  var activeLayers = {{
    bank_branches: true,
    vessels: true,
    crude_pipelines: true,
    gas_pipelines: false,
    world_equity: false,
    weather: false,
    refineries: false,
    lng_terminals: false
  }};

  var activeFollowVessel = null;
  var currentActiveView = 'map';
  var activeSplcTicker = 'AAPL';
  var currentVolRot = 35;

  // ═══════════════════════════════════════════════════════════════
  // ── MAP INITIALIZATION ──
  // ═══════════════════════════════════════════════════════════════
  function initLeafletBmap() {{
    var container = document.getElementById('bmap_leaflet_map');
    if (!container || typeof L === 'undefined') return;

    // Zero API key, institutional Esri dark and imagery tiles
    baseTileLayers.dark = L.tileLayer('https://services.arcgisonline.com/arcgis/rest/services/Canvas/World_Dark_Gray_Base/MapServer/tile/{{z}}/{{y}}/{{x}}', {{
      maxZoom: 18, minZoom: 1, attribution: 'Bloomberg / Esri Dark'
    }});
    baseTileLayers.dark_ref = L.tileLayer('https://services.arcgisonline.com/arcgis/rest/services/Canvas/World_Dark_Gray_Reference/MapServer/tile/{{z}}/{{y}}/{{x}}', {{
      maxZoom: 18, minZoom: 1
    }});
    baseTileLayers.satellite = L.tileLayer('https://services.arcgisonline.com/arcgis/rest/services/World_Imagery/MapServer/tile/{{z}}/{{y}}/{{x}}', {{
      maxZoom: 19, minZoom: 1, attribution: 'Esri World Imagery (High-Res Real Satellite)'
    }});
    baseTileLayers.nautical = L.tileLayer('https://{{s}}.tile.openstreetmap.org/{{z}}/{{x}}/{{y}}.png', {{
      maxZoom: 18, minZoom: 1
    }});

    leafletMap = L.map('bmap_leaflet_map', {{
      center: [38.5, -96.5],
      zoom: 5,
      minZoom: 1,
      maxZoom: 19,
      zoomControl: false,
      attributionControl: false,
      layers: [baseTileLayers.dark, baseTileLayers.dark_ref],
      preferCanvas: true
    }});

    window.bmapMap = leafletMap;

    // Add Zoom Control at top-left
    L.control.zoom({{ position: 'topleft' }}).addTo(leafletMap);

    // Coordinate telemetry & LOD tracking
    leafletMap.on('mousemove', function(e) {{
      var el = document.getElementById('bmap_cursor_coords');
      if (el) {{
        el.textContent = 'WGS84: ' + Math.abs(e.latlng.lat).toFixed(4) + '° ' + (e.latlng.lat >= 0 ? 'N' : 'S') +
                         ', ' + Math.abs(e.latlng.lng).toFixed(4) + '° ' + (e.latlng.lng >= 0 ? 'E' : 'W');
      }}
    }});

    leafletMap.on('zoomend', handleMapZoomLOD);

    // Initialize Layers
    initBankBranchesLayer();
    initPipelinesLayers();
    initVesselsLayer();
    initWorldEquityLayer();
    initWeatherLayer();

    renderDatasetSidebar();
    renderBmapTableData('berths');
    renderReadNewsStories();
    renderSplcNetwork('AAPL');
    renderFxcMatrix();
    initGpcCandlestickChart();
    initVolSurfaceCanvas();
  }}

  // ═══════════════════════════════════════════════════════════════
  // ── LAYER 1: US BANK BRANCHES (1,675) & MANHATTAN STREET SATELLITE ──
  // ═══════════════════════════════════════════════════════════════
  function initBankBranchesLayer() {{
    datasetLayerGroups['bank_branches'] = L.layerGroup().addTo(leafletMap);
    renderBankBranchesOnMap(usBankBranches);

    // Also add Manhattan high-res branch markers
    var manLayer = L.layerGroup();
    manhattanBranches.forEach(function(mb) {{
      var m = L.circleMarker([mb.lat, mb.lon], {{
        radius: 7,
        fillColor: '#38bdf8',
        color: '#00e5ff',
        weight: 2,
        fillOpacity: 0.95
      }});
      m.on('click', function() {{ showManhattanBranchPopup(mb); }});
      manLayer.addLayer(m);
    }});
    datasetLayerGroups['manhattan_branches'] = manLayer.addTo(leafletMap);
  }}

  function renderBankBranchesOnMap(branchesList) {{
    var group = datasetLayerGroups['bank_branches'];
    if (!group) return;
    group.clearLayers();

    var canvasRenderer = L.canvas({{ padding: 0.5 }});
    branchesList.forEach(function(b) {{
      var rad = b.dep > 2000 ? 5 : (b.dep > 500 ? 3.5 : 2.5);
      var m = L.circleMarker([b.lat, b.lon], {{
        renderer: canvasRenderer,
        radius: rad,
        fillColor: '#bde0fe',
        color: '#38bdf8',
        weight: 0.8,
        fillOpacity: 0.85
      }});
      m.on('click', function() {{
        showGenericBranchPopup(b);
      }});
      group.addLayer(m);
    }});
  }}

  window.showManhattanBranchPopup = function(mb) {{
    var pop = document.getElementById('bmap_branch_popup');
    if (!pop) return;
    document.getElementById('pop_branch_name').textContent = mb.name;
    document.getElementById('pop_branch_company').textContent = mb.company;
    document.getElementById('pop_branch_dep').textContent = '$' + (mb.dep_branch / 1000).toFixed(2) + 'M (' + mb.dep_branch.toLocaleString() + 'k)';
    document.getElementById('pop_branch_comp_dep').textContent = '$' + (mb.dep_company / 1000000).toFixed(2) + 'B (' + mb.dep_company.toLocaleString() + 'k)';
    document.getElementById('pop_branch_comp_assets').textContent = '$' + (mb.assets_company / 1000000).toFixed(2) + 'B (' + mb.assets_company.toLocaleString() + 'k)';
    document.getElementById('pop_branch_year').textContent = mb.year + ' (Active FDIC Report FFIEC 031/041)';
    pop.style.display = 'block';
  }};

  function showGenericBranchPopup(b) {{
    var pop = document.getElementById('bmap_branch_popup');
    if (!pop) return;
    document.getElementById('pop_branch_name').textContent = b.branch;
    document.getElementById('pop_branch_company').textContent = b.name;
    document.getElementById('pop_branch_dep').textContent = '$' + b.dep.toLocaleString() + 'M';
    document.getElementById('pop_branch_comp_dep').textContent = '$2,128,462M (National Domestic Total)';
    document.getElementById('pop_branch_comp_assets').textContent = '$3,914,143M (Consolidated Group)';
    document.getElementById('pop_branch_year').textContent = '2022 (FDIC Insured)';
    pop.style.display = 'block';
  }}

  window.filterBankBranches = function() {{
    var selBank = document.getElementById('filter_bank_name') ? document.getElementById('filter_bank_name').value : 'ALL';
    var selType = document.getElementById('filter_bank_branch') ? document.getElementById('filter_bank_branch').value : 'ALL';
    var selState = document.getElementById('filter_bank_state') ? document.getElementById('filter_bank_state').value : 'ALL';
    var minDep = document.getElementById('slider_bank_dep') ? parseFloat(document.getElementById('slider_bank_dep').value) : 0;

    var filtered = usBankBranches.filter(function(b) {{
      if (selBank !== 'ALL' && b.name !== selBank) return false;
      if (selType !== 'ALL' && b.type !== selType) return false;
      if (selState !== 'ALL' && b.state !== selState) return false;
      if (b.dep < minDep) return false;
      return true;
    }});

    renderBankBranchesOnMap(filtered);
    var lbl = document.getElementById('lbl_bank_dep_val');
    if (lbl) lbl.textContent = '$' + minDep.toLocaleString() + 'M+ (' + filtered.length.toLocaleString() + ' Branches)';

    var countBadge = document.getElementById('bmap_objects_count_badge');
    if (countBadge) countBadge.textContent = filtered.length.toLocaleString() + ' FDIC Branches Active';
  }};

  window.resetBankFilter = function() {{
    var selBank = document.getElementById('filter_bank_name'); if (selBank) selBank.value = 'ALL';
    var selType = document.getElementById('filter_bank_branch'); if (selType) selType.value = 'ALL';
    var selState = document.getElementById('filter_bank_state'); if (selState) selState.value = 'ALL';
    var sld = document.getElementById('slider_bank_dep'); if (sld) sld.value = '0';
    filterBankBranches();
  }};

  // ═══════════════════════════════════════════════════════════════
  // ── LAYER 2: CRUDE OIL PIPELINES & GAS PIPELINES (SCREENSHOTS 12, 27) ──
  // ═══════════════════════════════════════════════════════════════
  function initPipelinesLayers() {{
    var crudeGroup = L.layerGroup();
    crudePipelines.forEach(function(pipe) {{
      var poly = L.polyline(pipe.coords, {{
        color: '#2563eb', // Blue uniform line matching Screenshot 27
        weight: 2.5,
        opacity: 0.9,
        lineCap: 'round',
        lineJoin: 'round'
      }});
      poly.bindPopup(
        '<div style=\"font-family:monospace;font-size:10px;color:#fff;background:#060b14;padding:8px;border:1px solid #3b82f6;border-radius:4px;\">' +
          '<div style=\"color:#38bdf8;font-weight:bold;font-size:11px;margin-bottom:4px;\">' + pipe.name + '</div>' +
          '<div>Company: <strong style=\"color:#fff;\">' + pipe.company + '</strong></div>' +
          '<div>Type: <span style=\"color:#ffaa00;\">' + pipe.type + '</span></div>' +
          '<div>Fuel: ' + pipe.fuel + '</div>' +
          '<div>Capacity: <strong style=\"color:#00e676;\">' + pipe.capacity + '</strong></div>' +
          '<div>Length: ' + pipe.length + ' (' + pipe.diameter + ')</div>' +
          '<div style=\"margin-top:4px;color:#34d399;\">● ' + pipe.status + '</div>' +
        '</div>'
      );
      crudeGroup.addLayer(poly);
    }});
    datasetLayerGroups['crude_pipelines'] = crudeGroup.addTo(leafletMap);

    var gasGroup = L.layerGroup();
    gasPipelines.forEach(function(g) {{
      var poly = L.polyline(g.coords, {{
        color: g.color || '#f97316',
        weight: 2.5,
        dashArray: g.type === 'Intrastate' ? '4, 4' : null,
        opacity: 0.85
      }});
      poly.bindPopup(
        '<div style=\"font-family:monospace;font-size:10px;color:#fff;background:#060b14;padding:8px;border:1px solid #f97316;border-radius:4px;\">' +
          '<div style=\"color:#fb923c;font-weight:bold;font-size:11px;margin-bottom:4px;\">' + g.name + '</div>' +
          '<div>Holding Co: <strong style=\"color:#fff;\">' + g.holding_co + '</strong></div>' +
          '<div>Type: <span style=\"color:#00e5ff;\">' + g.type + '</span></div>' +
          '<div>Capacity: <strong style=\"color:#00e676;\">' + g.capacity + '</strong></div>' +
          '<div>Length: ' + g.length + '</div>' +
          '<div style=\"margin-top:4px;color:#34d399;\">● ' + g.status + '</div>' +
        '</div>'
      );
      gasGroup.addLayer(poly);
    }});
    datasetLayerGroups['gas_pipelines'] = gasGroup;
  }}

  window.togglePipelinesHighlight = function() {{
    var group = datasetLayerGroups['crude_pipelines'];
    if (!group) return;
    group.eachLayer(function(layer) {{
      layer.setStyle({{ weight: 4, color: '#38bdf8' }});
    }});
    setTimeout(function() {{
      group.eachLayer(function(layer) {{ layer.setStyle({{ weight: 2.5, color: '#2563eb' }}); }});
    }}, 2000);
  }};

  // ═══════════════════════════════════════════════════════════════
  // ── LAYER 3: MARITIME VESSELS & GREG MORTIMER (SCREENSHOTS 6, 8, 27) ──
  // ═══════════════════════════════════════════════════════════════
  function initVesselsLayer() {{
    var vGroup = L.layerGroup();

    // 1. Greg Mortimer (Image 8)
    var gmIcon = L.divIcon({{
      className: 'gm-icon',
      html: '<div style=\"width:10px;height:10px;background:#00e5ff;border:1.5px solid #fff;border-radius:50%;box-shadow:0 0 8px #00e5ff;\"></div>',
      iconSize: [10, 10]
    }});
    var gmMكر = L.marker([gregMortimer.lat, gregMortimer.lon], {{ icon: gmIcon }});
    gmMكر.on('click', showGregMortimerPopup);
    vGroup.addLayer(gmMكر);

    // Greg Mortimer Voyage Vector line
    var gmTrack = L.polyline(gregMortimer.track, {{
      color: '#eab308', // Yellow track line matching Screenshot 8
      weight: 2,
      dashArray: '5, 5'
    }});
    vGroup.addLayer(gmTrack);

    // 2. Global Fleet (Persian Gulf Hormuz, Malacca, Houston, Suez, etc.)
    var corridors = [
      {{ name: 'VLCC SEAWAYS CATALONIA', lat: 29.74, lon: -95.01, cls: 'VLCC', speed: '8.8 kts', dest: 'Deer Park Shell' }},
      {{ name: 'VLCC FRONT ALTAIR', lat: 25.85, lon: 56.45, cls: 'VLCC', speed: '12.4 kts', dest: 'Chiba Japan' }},
      {{ name: 'SUEZMAX EURONAV CAP', lat: 26.20, lon: 56.10, cls: 'Suezmax', speed: '11.8 kts', dest: 'Ningbo China' }},
      {{ name: 'AFRAMAX PACIFIC VOYAGER', lat: 1.25, lon: 103.80, cls: 'Aframax', speed: '10.2 kts', dest: 'Singapore Jurong' }},
      {{ name: 'LR2 NORDIC HAWK', lat: 27.90, lon: 34.30, cls: 'LR2', speed: '13.5 kts', dest: 'Suez Ain Sukhna' }}
    ];

    corridors.forEach(function(v) {{
      var vm = L.circleMarker([v.lat, v.lon], {{
        radius: 4.5,
        fillColor: '#00e5ff',
        color: '#fff',
        weight: 1,
        fillOpacity: 0.95
      }});
      vm.on('click', function() {{
        showGenericVesselPopup(v);
      }});
      vGroup.addLayer(vm);
    }});

    datasetLayerGroups['vessels'] = vGroup.addTo(leafletMap);
  }}

  window.showGregMortimerPopup = function() {{
    var pop = document.getElementById('bmap_vessel_popup');
    if (!pop) return;
    document.getElementById('pop_vessel_name').textContent = gregMortimer.name;
    document.getElementById('pop_vessel_imo').textContent = gregMortimer.imo;
    document.getElementById('pop_vessel_status').textContent = gregMortimer.nav_status;
    document.getElementById('pop_vessel_dest').textContent = gregMortimer.destination;
    document.getElementById('pop_vessel_eta').textContent = gregMortimer.eta;
    document.getElementById('pop_vessel_type').textContent = gregMortimer.vessel_type;
    document.getElementById('pop_vessel_speed').textContent = gregMortimer.current_speed;
    document.getElementById('pop_vessel_draft').textContent = gregMortimer.current_draft + ' (Max: ' + gregMortimer.max_draft + ')';
    pop.style.display = 'block';
  }};

  function showGenericVesselPopup(v) {{
    var pop = document.getElementById('bmap_vessel_popup');
    if (!pop) return;
    document.getElementById('pop_vessel_name').textContent = v.name;
    document.getElementById('pop_vessel_imo').textContent = '9' + Math.floor(100000 + Math.random() * 899999);
    document.getElementById('pop_vessel_status').textContent = 'Under way using engine';
    document.getElementById('pop_vessel_dest').textContent = v.dest;
    document.getElementById('pop_vessel_eta').textContent = '03/06/2026 18:00';
    document.getElementById('pop_vessel_type').textContent = 'Crude Tanker (' + v.cls + ')';
    document.getElementById('pop_vessel_speed').textContent = v.speed;
    document.getElementById('pop_vessel_draft').textContent = '14.2 m (Max: 16.5 m)';
    pop.style.display = 'block';
  }}

  window.toggleVesselMoreMenu = function() {{
    var m = document.getElementById('vessel_more_menu');
    if (m) m.style.display = (m.style.display === 'block') ? 'none' : 'block';
  }};

  window.closeBmapVesselPopup = function() {{
    var pop = document.getElementById('bmap_vessel_popup');
    if (pop) pop.style.display = 'none';
  }};

  // ═══════════════════════════════════════════════════════════════
  // ── LAYER 4: WORLD EQUITY MARKETS (SCREENSHOTS 3, 4) ──
  // ═══════════════════════════════════════════════════════════════
  function initWorldEquityLayer() {{
    var eqGroup = L.layerGroup();
    worldEquityData.forEach(function(item) {{
      var col = item.val >= 0 ? '#16a34a' : '#dc2626';
      var m = L.circleMarker([item.lat, item.lon], {{
        radius: 8,
        fillColor: col,
        color: '#fff',
        weight: 1.5,
        fillOpacity: 0.85
      }});
      m.bindPopup(
        '<div style=\"font-family:monospace;font-size:10px;color:#fff;background:#05080e;padding:6px;border:1px solid ' + col + ';\">' +
          '<strong style=\"color:#fff;\">' + item.country + '</strong><br>' +
          '<span>' + item.index + ': </span>' +
          '<strong style=\"color:' + (item.val >= 0 ? '#22c55e' : '#ef4444') + ';\">' + item.chg + '</strong><br>' +
          '<span style=\"color:#94a3b8;\">Level: ' + item.last + '</span>' +
        '</div>'
      );
      eqGroup.addLayer(m);
    }});
    datasetLayerGroups['world_equity'] = eqGroup;
  }}

  // ═══════════════════════════════════════════════════════════════
  // ── LAYER 5: WEATHER OVERLAYS (SCREENSHOTS 2, 3) ──
  // ═══════════════════════════════════════════════════════════════
  function initWeatherLayer() {{
    var wGroup = L.layerGroup();
    // Simulate cloud coverage zones
    var zones = [
      {{ lat: 45, lon: -100, rad: 800000, col: 'rgba(255,255,255,0.22)' }},
      {{ lat: 10, lon: 20, rad: 1200000, col: 'rgba(255,255,255,0.18)' }},
      {{ lat: 25, lon: 85, rad: 900000, col: 'rgba(255,255,255,0.25)' }}
    ];
    zones.forEach(function(z) {{
      wGroup.addLayer(L.circle([z.lat, z.lon], {{
        radius: z.rad,
        fillColor: '#fff',
        fillOpacity: 0.18,
        stroke: false
      }}));
    }});
    datasetLayerGroups['weather'] = wGroup;
  }}

  window.switchWeatherType = function(val) {{
    var lbl = document.getElementById('weather_scale_lbl');
    var bar = document.getElementById('weather_gradient_bar');
    if (!lbl || !bar) return;
    if (val === 'temp') {{
      lbl.textContent = 'Temperature: -140°F to +140°F';
      bar.style.background = 'linear-gradient(90deg, #1e3a8a 0%, #06b6d4 30%, #22c55e 60%, #ea580c 85%, #dc2626 100%)';
    }} else if (val === 'cloud') {{
      lbl.textContent = 'Cloud Cover: 0% to 100%';
      bar.style.background = 'linear-gradient(90deg, #05080e 0%, #475569 50%, #f8fafc 100%)';
    }} else {{
      lbl.textContent = 'Wind Speed: 0 to 80 kts';
      bar.style.background = 'linear-gradient(90deg, #0284c7 0%, #a855f7 50%, #e11d48 100%)';
    }}
  }};

  // ═══════════════════════════════════════════════════════════════
  // ── DATASET DRAWER & SIDEBAR TOGGLES ──
  // ═══════════════════════════════════════════════════════════════
  function renderDatasetSidebar() {{
    var sList = document.getElementById('suggested_datasets_list');
    var nList = document.getElementById('new_datasets_list');
    if (!sList || !nList) return;

    var suggestedItems = [
      {{ key: 'bank_branches', name: 'Bank Branches (US)', count: '1,675' }},
      {{ key: 'crude_pipelines', name: 'Crude Oil Pipelines', count: '15' }},
      {{ key: 'vessels', name: 'Vessels', count: '20+' }},
      {{ key: 'world_equity', name: 'World Equity Markets', count: '15' }},
      {{ key: 'weather', name: 'Weather', count: '3' }},
      {{ key: 'gas_pipelines', name: 'Natural Gas Pipelines (N.Am.)', count: '5' }},
      {{ key: 'cyclones', name: 'Cyclones', count: '2' }},
      {{ key: 'earthquakes', name: 'Earthquakes', count: '2' }},
      {{ key: 'factories', name: 'Factories', count: '5' }},
      {{ key: 'fires', name: 'Fires', count: '2' }},
      {{ key: 'lng_berths', name: 'LNG Berths', count: '4' }},
      {{ key: 'lng_terminals', name: 'LNG Terminals', count: '13' }},
      {{ key: 'power_plants', name: 'Power Plants', count: '6' }},
      {{ key: 'refineries', name: 'Refineries', count: '9' }},
      {{ key: 'retail', name: 'Retail', count: '5' }},
      {{ key: 'seaports', name: 'Seaports', count: '7' }}
    ];

    var newItems = [
      {{ key: 'fertilizer', name: 'Fertilizer Manufacturers', count: '4' }},
      {{ key: 'gas_flows', name: 'Natural Gas Flows (N.Am.)', count: '4' }},
      {{ key: 'gas_eur', name: 'Natural Gas Pipelines (Eur.)', count: '5' }},
      {{ key: 'power_iso', name: 'Power ISO Regions', count: '7' }},
      {{ key: 'wfor', name: 'Weather Stations (WFOR)', count: '6' }}
    ];

    sList.innerHTML = '';
    suggestedItems.forEach(function(item) {{
      var isActive = !!activeLayers[item.key];
      var div = document.createElement('div');
      div.className = 'dataset-row';
      div.style.cssText = 'display:flex;justify-content:space-between;align-items:center;padding:4px 6px;cursor:pointer;border-radius:2px;font-size:10px;' +
                          (isActive ? 'background:#132032;color:#00e5ff;font-weight:700;' : 'color:#cbd5e1;');
      div.innerHTML =
        '<span style=\"display:flex;align-items:center;gap:5px;\">' +
          '<span style=\"color:' + (isActive ? '#00e5ff' : '#64748b') + ';\">' + (isActive ? '✓' : '+') + '</span>' +
          '<span>' + item.name + '</span>' +
        '</span>' +
        '<span style=\"color:#64748b;font-size:9px;background:#05080e;padding:1px 4px;border-radius:2px;\">' + item.count + '</span>';
      div.onclick = function() {{ window.toggleBmapDataset(item.key); }};
      sList.appendChild(div);
    }});

    nList.innerHTML = '';
    newItems.forEach(function(item) {{
      var isActive = !!activeLayers[item.key];
      var div = document.createElement('div');
      div.className = 'dataset-row';
      div.style.cssText = 'display:flex;justify-content:space-between;align-items:center;padding:4px 6px;cursor:pointer;border-radius:2px;font-size:10px;' +
                          (isActive ? 'background:#132032;color:#38bdf8;font-weight:700;' : 'color:#94a3b8;');
      div.innerHTML =
        '<span style=\"display:flex;align-items:center;gap:5px;\">' +
          '<span style=\"color:' + (isActive ? '#38bdf8' : '#64748b') + ';\">' + (isActive ? '✓' : '+') + '</span>' +
          '<span>' + item.name + '</span>' +
        '</span>' +
        '<span style=\"color:#64748b;font-size:9px;background:#05080e;padding:1px 4px;border-radius:2px;\">' + item.count + '</span>';
      div.onclick = function() {{ window.toggleBmapDataset(item.key); }};
      nList.appendChild(div);
    }});
  }}

  window.toggleBmapDataset = function(key) {{
    activeLayers[key] = !activeLayers[key];
    var group = datasetLayerGroups[key];
    if (group && leafletMap) {{
      if (activeLayers[key]) {{
        if (!leafletMap.hasLayer(group)) group.addTo(leafletMap);
      }} else {{
        if (leafletMap.hasLayer(group)) leafletMap.removeLayer(group);
      }}
    }}

    // Toggle corresponding Floating Cards
    var cardBank = document.getElementById('bmap_param_card_bank');
    var cardVessel = document.getElementById('bmap_vessels_filter_card');
    var cardPipe = document.getElementById('bmap_pipelines_filter_card');
    var cardWeather = document.getElementById('bmap_weather_filter_card');
    var cardEquity = document.getElementById('bmap_equity_filter_card');

    if (key === 'bank_branches' && cardBank) cardBank.style.display = activeLayers[key] ? 'block' : 'none';
    if (key === 'vessels' && cardVessel) cardVessel.style.display = activeLayers[key] ? 'block' : 'none';
    if (key === 'crude_pipelines' && cardPipe) cardPipe.style.display = activeLayers[key] ? 'block' : 'none';
    if (key === 'weather' && cardWeather) cardWeather.style.display = activeLayers[key] ? 'block' : 'none';
    if (key === 'world_equity' && cardEquity) cardEquity.style.display = activeLayers[key] ? 'block' : 'none';

    renderDatasetSidebar();
    updateActiveDatasetPill();
  }};

  function updateActiveDatasetPill() {{
    var activeCount = Object.values(activeLayers).filter(Boolean).length;
    var el = document.getElementById('active_dataset_count_pill');
    if (el) el.textContent = activeCount + ' Active';
  }}

  window.toggleMapContentDrawer = function() {{
    var drawer = document.getElementById('bmap_map_content_drawer');
    var btnOpen = document.getElementById('btn_open_drawer_pill');
    if (!drawer) return;
    if (drawer.style.transform === 'translateX(100%)') {{
      drawer.style.transform = 'translateX(0)';
      if (btnOpen) btnOpen.style.display = 'none';
    }} else {{
      drawer.style.transform = 'translateX(100%)';
      if (btnOpen) btnOpen.style.display = 'block';
    }}
  }};

  // ═══════════════════════════════════════════════════════════════
  // ── PRESETS & DEEP ZOOM ENGINE (MANHATTAN, CRUDE PIPELINES, HORMUZ) ──
  // ═══════════════════════════════════════════════════════════════
  window.jumpToBmapPreset = function(presetKey) {{
    if (!leafletMap) return;
    switchBmapView('map');

    var labelEl = document.getElementById('bmap_scope_label');
    var countBadge = document.getElementById('bmap_objects_count_badge');

    if (presetKey === 'manhattan') {{
      // Deep Zoom to Manhattan Street Satellite (Screenshot 7, 9, 10)
      leafletMap.flyTo([40.7182, -74.0028], 17, {{ duration: 1.5 }});
      setBmapTileLayer('satellite');
      if (labelEl) labelEl.textContent = 'MANHATTAN 400 BROADWAY / 3RD AVE FDIC CLUSTER';
      if (countBadge) countBadge.textContent = '5 Commercial Vaults In Scope';
      setTimeout(function() {{
        showManhattanBranchPopup(manhattanBranches[0]);
      }}, 1600);

    }} else if (presetKey === 'crude_pipelines') {{
      // Fit World View & Activate Pipelines (Screenshot 27)
      leafletMap.flyTo([30.0, 10.0], 2.5, {{ duration: 1.2 }});
      setBmapTileLayer('dark');
      if (!activeLayers['crude_pipelines']) window.toggleBmapDataset('crude_pipelines');
      if (!activeLayers['vessels']) window.toggleBmapDataset('vessels');
      var cardPipe = document.getElementById('bmap_pipelines_filter_card');
      if (cardPipe) cardPipe.style.display = 'block';
      if (labelEl) labelEl.textContent = 'GLOBAL CRUDE OIL PIPELINES & TRANSIT ARTERIES';
      if (countBadge) countBadge.textContent = '15 Major Continental Trunklines';

    }} else if (presetKey === 'world_equity') {{
      leafletMap.flyTo([25.0, 15.0], 2, {{ duration: 1.2 }});
      if (!activeLayers['world_equity']) window.toggleBmapDataset('world_equity');
      var cardEq = document.getElementById('bmap_equity_filter_card');
      if (cardEq) cardEq.style.display = 'block';
      if (labelEl) labelEl.textContent = 'WORLD EQUITY MARKETS BENCHMARK RETURN HEATMAP';
      if (countBadge) countBadge.textContent = '15 Sovereign Benchmarks';

    }} else if (presetKey === 'weather') {{
      leafletMap.flyTo([25.0, -40.0], 2.5, {{ duration: 1.2 }});
      if (!activeLayers['weather']) window.toggleBmapDataset('weather');
      var cardW = document.getElementById('bmap_weather_filter_card');
      if (cardW) cardW.style.display = 'block';
      if (labelEl) labelEl.textContent = 'GLOBAL SATELLITE CLOUD COVER & THERMAL FIELDS';

    }} else if (presetKey === 'greg_mortimer') {{
      leafletMap.flyTo([gregMortimer.lat, gregMortimer.lon], 6, {{ duration: 1.5 }});
      if (!activeLayers['vessels']) window.toggleBmapDataset('vessels');
      showGregMortimerPopup();
      if (labelEl) labelEl.textContent = 'DRAKE PASSAGE / ANTARCTIC EXPEDITION CORRIDOR';
      if (countBadge) countBadge.textContent = 'Vessel GREG MORTIMER Under Way';

    }} else if (presetKey === 'bank_branches') {{
      leafletMap.flyTo([38.5, -96.5], 5, {{ duration: 1.2 }});
      setBmapTileLayer('dark');
      if (!activeLayers['bank_branches']) window.toggleBmapDataset('bank_branches');
      if (labelEl) labelEl.textContent = 'US BANK BRANCHES (FDIC GEOSPATIAL CLUSTERS)';
      if (countBadge) countBadge.textContent = '1,675 FDIC Branches Active';

    }} else if (presetKey === 'hormuz') {{
      leafletMap.flyTo([25.85, 56.45], 8.5, {{ duration: 1.2 }});
      if (!activeLayers['vessels']) window.toggleBmapDataset('vessels');
      if (labelEl) labelEl.textContent = 'STRAIT OF HORMUZ TSS MARITIME CHOKE POINT';
      if (countBadge) countBadge.textContent = '20+ Commercial Tankers in Scope';

    }} else if (presetKey === 'world') {{
      leafletMap.flyTo([20, 0], 2, {{ duration: 1.0 }});
      if (labelEl) labelEl.textContent = 'GLOBAL MULTI-ASSET ENERGY & FINANCIAL RADAR';
    }}
  }};

  function handleMapZoomLOD() {{
    if (!leafletMap) return;
    var z = leafletMap.getZoom();
    if (z >= 16 && currentTileType === 'auto') {{
      setBmapTileLayer('satellite');
    }} else if (z < 16 && currentTileType === 'auto') {{
      setBmapTileLayer('dark');
    }}
  }}

  window.setBmapTileLayer = function(type) {{
    if (!leafletMap) return;
    currentTileType = type;
    Object.values(baseTileLayers).forEach(function(l) {{
      if (leafletMap.hasLayer(l)) leafletMap.removeLayer(l);
    }});

    ['dark', 'sat', 'naut', 'auto'].forEach(function(k) {{
      var btn = document.getElementById('bmap_layer_' + k);
      if (btn) btn.classList.remove('active');
    }});

    if (type === 'dark') {{
      baseTileLayers.dark.addTo(leafletMap);
      baseTileLayers.dark_ref.addTo(leafletMap);
      var b = document.getElementById('bmap_layer_dark'); if (b) b.classList.add('active');
    }} else if (type === 'satellite') {{
      baseTileLayers.satellite.addTo(leafletMap);
      var b = document.getElementById('bmap_layer_sat'); if (b) b.classList.add('active');
    }} else if (type === 'nautical') {{
      baseTileLayers.nautical.addTo(leafletMap);
      var b = document.getElementById('bmap_layer_naut'); if (b) b.classList.add('active');
    }} else {{
      baseTileLayers.dark.addTo(leafletMap);
      var b = document.getElementById('bmap_layer_auto'); if (b) b.classList.add('active');
    }}
  }};

  window.zoomToManhattanStreetLevel = function() {{
    jumpToBmapPreset('manhattan');
  }};

  // ═══════════════════════════════════════════════════════════════
  // ── MULTI-VIEW SWITCHING (MAP, TABLE, CHART, NEWS, SPLC, FXC, VOL) ──
  // ═══════════════════════════════════════════════════════════════
  window.switchBmapView = function(viewKey) {{
    currentActiveView = viewKey;
    ['map', 'table', 'chart', 'news', 'splc', 'fxc', 'vol'].forEach(function(k) {{
      var btn = document.getElementById('bmap_btn_view_' + k);
      var container = document.getElementById('bmap_view_container_' + k);
      if (btn) {{
        if (k === viewKey) {{
          btn.style.background = '#1e3a5f';
          btn.style.color = '#00e5ff';
          btn.style.borderBottom = '2px solid #00e5ff';
        }} else {{
          btn.style.background = '#0d1624';
          btn.style.color = '#94a3b8';
          btn.style.borderBottom = 'none';
        }}
      }}
      if (container) container.style.display = (k === viewKey) ? 'block' : 'none';
    }});

    if (viewKey === 'map' && leafletMap) {{
      setTimeout(function() {{ leafletMap.invalidateSize(); }}, 60);
    }} else if (viewKey === 'chart') {{
      setTimeout(drawGpcChart, 60);
    }} else if (viewKey === 'vol') {{
      setTimeout(drawVolSurface, 60);
    }}
  }};

  // ═══════════════════════════════════════════════════════════════
  // ── VIEW 2: MARITIME BERTH VISITS TABLE (SCREENSHOT 5) ──
  // ═══════════════════════════════════════════════════════════════
  window.switchTableDataset = function(type) {{
    renderBmapTableData(type);
  }};

  function renderBmapTableData(datasetType) {{
    var thead = document.getElementById('bmap_table_thead');
    var tbody = document.getElementById('bmap_data_grid_tbody');
    var badge = document.getElementById('table_total_count_badge');
    if (!thead || !tbody) return;

    tbody.innerHTML = '';

    if (datasetType === 'berths') {{
      thead.innerHTML =
        '<tr style=\"background:#0e1a2d;position:sticky;top:0;z-index:5;\">' +
          '<th>VISIT TYPE</th>' +
          '<th>BERTH NAME</th>' +
          '<th>COUNTRY / REGION</th>' +
          '<th>VESSEL CLASS</th>' +
          '<th>QUANTITY (BBLS/MT)</th>' +
          '<th>VESSEL IMO</th>' +
          '<th>ACTION</th>' +
        '</tr>';

      if (badge) badge.textContent = berthVisits.length + ' Maritime Berth Visits Active';

      berthVisits.forEach(function(b) {{
        var tr = document.createElement('tr');
        var isExp = b.visit.includes('Exports');
        tr.innerHTML =
          '<td><span class=\"badge\" style=\"background:' + (isExp ? '#064e3b;color:#34d399;' : '#1e3a5f;color:#38bdf8;') + '\">' + b.visit + '</span></td>' +
          '<td><strong style=\"color:#fff;\">' + b.berth + '</strong></td>' +
          '<td style=\"color:#e2e8f0;\">' + b.country + '</td>' +
          '<td style=\"color:#ffaa00;font-weight:700;\">' + b.cls + '</td>' +
          '<td style=\"color:#00e5ff;font-weight:700;\">' + b.qty + '</td>' +
          '<td style=\"color:#94a3b8;\">' + b.imo + '</td>' +
          '<td><button onclick=\"zoomToBerth(' + b.lat + ',' + b.lon + ')\" style=\"background:#1e3a5f;color:#00e5ff;border:1px solid #3b82f6;padding:2px 6px;font-size:9px;border-radius:2px;cursor:pointer;\">🔍 Zoom</button></td>';
        tbody.appendChild(tr);
      }});

    }} else if (datasetType === 'banks') {{
      thead.innerHTML =
        '<tr style=\"background:#0e1a2d;position:sticky;top:0;z-index:5;\">' +
          '<th>INSTITUTION</th>' +
          '<th>BRANCH IDENTIFIER</th>' +
          '<th>LOCATION</th>' +
          '<th>TOTAL DEPOSITS</th>' +
          '<th>BRANCH TYPE</th>' +
          '<th>STATUS</th>' +
          '<th>ACTION</th>' +
        '</tr>';

      if (badge) badge.textContent = usBankBranches.length + ' FDIC Branches Total';

      usBankBranches.slice(0, 50).forEach(function(b) {{
        var tr = document.createElement('tr');
        tr.innerHTML =
          '<td><strong style=\"color:#fff;\">' + b.name + '</strong></td>' +
          '<td style=\"color:#94a3b8;\">' + b.branch + '</td>' +
          '<td style=\"color:#e2e8f0;\">' + b.state + ' (' + b.lat.toFixed(2) + ', ' + b.lon.toFixed(2) + ')</td>' +
          '<td style=\"color:#ffaa00;font-weight:700;\">$' + b.dep.toLocaleString() + 'M</td>' +
          '<td style=\"color:#38bdf8;\">' + b.type + '</td>' +
          '<td><span style=\"color:#00e676;\">FDIC Insured</span></td>' +
          '<td><button onclick=\"zoomToBerth(' + b.lat + ',' + b.lon + ')\" style=\"background:#1e3a5f;color:#00e5ff;border:1px solid #3b82f6;padding:2px 6px;font-size:9px;border-radius:2px;cursor:pointer;\">🔍 Zoom</button></td>';
        tbody.appendChild(tr);
      }});

    }} else if (datasetType === 'pipelines') {{
      thead.innerHTML =
        '<tr style=\"background:#0e1a2d;position:sticky;top:0;z-index:5;\">' +
          '<th>PIPELINE NAME</th>' +
          '<th>OPERATING COMPANY</th>' +
          '<th>SYSTEM TYPE</th>' +
          '<th>THROUGHPUT CAPACITY</th>' +
          '<th>LENGTH / DIAMETER</th>' +
          '<th>OPERATIONAL STATUS</th>' +
        '</tr>';

      if (badge) badge.textContent = crudePipelines.length + ' Crude Arteries Active';

      crudePipelines.forEach(function(p) {{
        var tr = document.createElement('tr');
        tr.innerHTML =
          '<td><strong style=\"color:#38bdf8;\">' + p.name + '</strong></td>' +
          '<td style=\"color:#fff;\">' + p.company + '</td>' +
          '<td style=\"color:#ffaa00;\">' + p.type + '</td>' +
          '<td style=\"color:#00e676;font-weight:700;\">' + p.capacity + '</td>' +
          '<td style=\"color:#94a3b8;\">' + p.length + ' (' + p.diameter + ')</td>' +
          '<td><span style=\"color:#34d399;\">● ' + p.status + '</span></td>';
        tbody.appendChild(tr);
      }});
    }}
  }}

  window.zoomToBerth = function(lat, lon) {{
    switchBmapView('map');
    if (leafletMap) leafletMap.flyTo([lat, lon], 12, {{ duration: 1.2 }});
  }};

  window.filterBmapTableRows = function(q) {{
    q = (q || '').toLowerCase();
    var tbody = document.getElementById('bmap_data_grid_tbody');
    if (!tbody) return;
    Array.from(tbody.children).forEach(function(tr) {{
      tr.style.display = tr.textContent.toLowerCase().includes(q) ? '' : 'none';
    }});
  }};

  // ═══════════════════════════════════════════════════════════════
  // ── VIEW 5: SPLC SUPPLY CHAIN ANALYSIS (SCREENSHOTS 20, 24, 25) ──
  // ═══════════════════════════════════════════════════════════════
  window.switchSplcTargetFirm = function(ticker) {{
    renderSplcNetwork(ticker);
  }};

  function renderSplcNetwork(ticker) {{
    activeSplcTicker = ticker;
    var net = splcNetworks[ticker] || splcNetworks['AAPL'];

    // Header & Telemetry
    document.getElementById('splc_firm_title').textContent = 'SPLC ' + net.ticker;
    document.getElementById('splc_firm_name_label').textContent = net.name;
    document.getElementById('splc_last_price').textContent = net.last_px + ' USD ' + net.chg;
    document.getElementById('splc_rev_quant').textContent = net.rev_quant;
    document.getElementById('splc_cogs_quant').textContent = net.cogs_quant;
    document.getElementById('splc_capex_quant').textContent = net.capex_quant;
    document.getElementById('splc_sga_quant').textContent = net.sga_quant;
    document.getElementById('splc_rd_quant').textContent = net.rd_quant;

    document.getElementById('splc_anchor_name').textContent = net.name;
    document.getElementById('splc_anchor_ticker').textContent = net.ticker;
    document.getElementById('splc_node_sup_count').textContent = net.suppliers_count + ' Nodes';
    document.getElementById('splc_node_cust_count').textContent = net.customers_count + ' Nodes';

    document.getElementById('splc_suppliers_count_title').textContent = net.suppliers_count + ' Suppliers';
    document.getElementById('splc_customers_count_title').textContent = net.customers_count + ' Customers';

    // Suppliers (Left)
    var supList = document.getElementById('splc_suppliers_list');
    supList.innerHTML = '';
    net.suppliers.forEach(function(s) {{
      var row = document.createElement('div');
      var surpCol = s.surprise >= 0 ? '#10b981' : '#ef4444';
      row.style.cssText = 'background:#0f172a;border:1px solid #1e293b;border-left:3px solid ' + surpCol + ';border-radius:3px;padding:5px 8px;font-size:9.5px;';
      row.innerHTML =
        '<div style=\"display:flex;justify-content:space-between;\">' +
          '<strong style=\"color:#fff;\">' + s.name + '</strong>' +
          '<span style=\"color:' + surpCol + ';font-weight:bold;\">' + (s.surprise >= 0 ? '+' : '') + s.surprise + '%</span>' +
        '</div>' +
        '<div style=\"display:flex;justify-content:space-between;color:#64748b;font-size:8.5px;margin-top:2px;\">' +
          '<span>Rev: ' + s.rev + '</span>' +
          '<span>COGS Exposure: <strong style=\"color:#ffaa00;\">' + s.cogs + '</strong></span>' +
        '</div>';
      supList.appendChild(row);
    }});

    // Customers (Right)
    var custList = document.getElementById('splc_customers_list');
    custList.innerHTML = '';
    net.customers.forEach(function(c) {{
      var row = document.createElement('div');
      row.style.cssText = 'background:#0f172a;border:1px solid #1e293b;border-right:3px solid #f59e0b;border-radius:3px;padding:5px 8px;font-size:9.5px;';
      row.innerHTML =
        '<div style=\"display:flex;justify-content:space-between;\">' +
          '<strong style=\"color:#fff;\">' + c.name + '</strong>' +
          '<span style=\"color:#ffaa00;font-weight:bold;\">' + c.rev + ' Rev</span>' +
        '</div>' +
        '<div style=\"color:#64748b;font-size:8.5px;margin-top:2px;\">COGS Exposure: ' + c.cogs + '</div>';
      custList.appendChild(row);
    }});

    // Competitors (Bottom)
    var compList = document.getElementById('splc_competitors_list');
    compList.innerHTML = '';
    net.competitors.forEach(function(cp) {{
      var badge = document.createElement('div');
      badge.style.cssText = 'background:#1a1020;border:1px solid #701a75;padding:4px 8px;border-radius:3px;font-size:9px;';
      badge.innerHTML = '<strong style=\"color:#f472b6;\">' + cp.name + '</strong> <span style=\"color:#64748b;\">(' + cp.segment + ')</span>';
      compList.appendChild(badge);
    }});
  }}

  // ═══════════════════════════════════════════════════════════════
  // ── VIEW 6: FXC CURRENCY RATES MATRIX (SCREENSHOT 1) ──
  // ═══════════════════════════════════════════════════════════════
  function renderFxcMatrix() {{
    var thead = document.getElementById('fxc_table_thead');
    var tbody = document.getElementById('fxc_table_tbody');
    if (!thead || !tbody) return;

    var currs = fxcData.currencies;
    var trHead = '<tr><th style=\"background:#0a121e;color:#ffaa00;padding:6px;border:1px solid #162438;\">BASE / QUOTE</th>';
    currs.forEach(function(c) {{
      trHead += '<th style=\"background:#0a121e;color:#fff;padding:6px;border:1px solid #162438;font-size:10px;\">' + c.flag + '<br>' + c.code + '</th>';
    }});
    trHead += '</tr>';
    thead.innerHTML = trHead;

    tbody.innerHTML = '';
    currs.forEach(function(rowCurr) {{
      var tr = document.createElement('tr');
      var rowRates = fxcData.rates[rowCurr.code] || [];
      var rowChanges = fxcData.changes[rowCurr.code] || [];

      var html = '<td style=\"background:#0d1626;color:#ffaa00;font-weight:700;padding:6px;border:1px solid #162438;\">' + rowCurr.flag + ' ' + rowCurr.code + '</td>';
      currs.forEach(function(colCurr, idx) {{
        if (rowCurr.code === colCurr.code) {{
          html += '<td style=\"background:#060a12;color:#64748b;border:1px solid #162438;\">1.0000</td>';
        }} else {{
          var rate = rowRates[idx] || 1.0;
          var chg = rowChanges[idx] || 0.0;
          var cellBg = '#0a101b';
          if (chg > 0.5) cellBg = 'rgba(22, 163, 74, 0.4)';
          else if (chg > 0.1) cellBg = 'rgba(21, 128, 61, 0.25)';
          else if (chg < -0.5) cellBg = 'rgba(220, 38, 38, 0.4)';
          else if (chg < -0.1) cellBg = 'rgba(185, 28, 28, 0.25)';

          var rateStr = rate > 100 ? rate.toFixed(1) : (rate > 1 ? rate.toFixed(4) : rate.toFixed(5));
          html += '<td style=\"background:' + cellBg + ';color:#e2e8f0;padding:5px 3px;border:1px solid #162438;font-size:9.5px;\">' +
                    '<div>' + rateStr + '</div>' +
                    '<div style=\"font-size:8px;color:' + (chg >= 0 ? '#34d399' : '#f87171') + ';\">' + (chg >= 0 ? '+' : '') + chg.toFixed(2) + '%</div>' +
                  '</td>';
        }}
      }});
      tr.innerHTML = html;
      tbody.appendChild(tr);
    }});
  }}

  window.toggleFxcHeatmap = function(show) {{
    renderFxcMatrix();
  }};

  // ═══════════════════════════════════════════════════════════════
  // ── VIEW 4: READ MOST READ STORIES NEWS WIRE (SCREENSHOTS 18, 19) ──
  // ═══════════════════════════════════════════════════════════════
  function renderReadNewsStories() {{
    var list = document.getElementById('bmap_read_news_list');
    if (!list) return;
    list.innerHTML = '';
    readNewsStories.forEach(function(item) {{
      var row = document.createElement('div');
      row.style.cssText = 'background:#0b1320;border-left:3px solid #ffaa00;border-radius:0 4px 4px 0;padding:8px 12px;margin-bottom:4px;cursor:pointer;transition:background 0.15s ease;';
      row.onmouseover = function() {{ this.style.background = '#111e30'; }};
      row.onmouseout = function() {{ this.style.background = '#0b1320'; }};
      row.onclick = function() {{ alert('READ <GO> Story #' + item.id + ':\\n\\n' + item.title + '\\n\\n' + item.lead); }};

      row.innerHTML =
        '<div style=\"display:flex;justify-content:space-between;font-size:9.5px;color:#64748b;margin-bottom:2px;\">' +
          '<div style=\"display:flex;gap:6px;align-items:center;\">' +
            '<span style=\"background:#1e3a5f;color:#38bdf8;padding:1px 5px;border-radius:2px;font-weight:700;\">' + item.src + '</span>' +
            '<span style=\"color:#fff;font-weight:700;\">' + item.id + ') ' + item.title + '</span>' +
          '</div>' +
          '<span style=\"color:#ffaa00;font-weight:700;\">' + item.time + '</span>' +
        '</div>' +
        '<div style=\"color:#94a3b8;font-size:9.5px;margin-top:4px;\">' + item.lead + '</div>';
      list.appendChild(row);
    }});
  }}

  window.filterNewsByText = function(q) {{
    q = (q || '').toLowerCase();
    var list = document.getElementById('bmap_read_news_list');
    if (!list) return;
    Array.from(list.children).forEach(function(row) {{
      row.style.display = row.textContent.toLowerCase().includes(q) ? '' : 'none';
    }});
  }};

  // ═══════════════════════════════════════════════════════════════
  // ── VIEW 3: GPC CANDLESTICK CHART & TECHNICAL CHECKLIST ──
  // ═══════════════════════════════════════════════════════════════
  var gpcIndicators = {{
    last_px: true, ma5: true, ma10: true, ma15: true,
    rsi: true, macd: true, stoch: false, boll: false,
    ichimoku: true, regress: true, volume: true, vix: false,
    triangle: false
  }};

  window.toggleGpcIndicator = function(k) {{
    var chk = document.getElementById('chk_' + k);
    if (chk) gpcIndicators[k] = chk.checked;
    drawGpcChart();
  }};

  window.drawTriangleBreakoutPattern = function() {{
    gpcIndicators.triangle = !gpcIndicators.triangle;
    drawGpcChart();
  }};

  function initGpcCandlestickChart() {{
    setTimeout(drawGpcChart, 100);
  }}

  function drawGpcChart() {{
    var canvas = document.getElementById('gpc_main_canvas');
    if (!canvas) return;
    var ctx = canvas.getContext('2d');
    var w = canvas.width = canvas.parentElement.clientWidth;
    var h = canvas.height = canvas.parentElement.clientHeight;

    ctx.fillStyle = '#000';
    ctx.fillRect(0, 0, w, h);

    // Draw Grid Lines
    ctx.strokeStyle = '#121a28';
    ctx.lineWidth = 1;
    for (var x = 40; x < w; x += 60) {{
      ctx.beginPath(); ctx.moveTo(x, 0); ctx.lineTo(x, h); ctx.stroke();
    }}
    for (var y = 30; y < h; y += 40) {{
      ctx.beginPath(); ctx.moveTo(0, y); ctx.lineTo(w, y); ctx.stroke();
    }}

    // Synthetic Candlestick Series (35 bars)
    var numBars = 36;
    var barWidth = (w - 80) / numBars;
    var prices = [];
    var basePx = 390;

    for (var i = 0; i < numBars; i++) {{
      var change = Math.sin(i * 0.35) * 4 + (Math.random() - 0.45) * 3;
      var open = basePx + change;
      var close = open + (Math.random() - 0.48) * 5;
      var high = Math.max(open, close) + Math.random() * 2.5;
      var low = Math.min(open, close) - Math.random() * 2.5;
      prices.push({{ o: open, c: close, h: high, l: low }});
      basePx = close;
    }}

    var minP = 385, maxP = 412;
    function py(p) {{ return h - 25 - ((p - minP) / (maxP - minP)) * (h - 50); }}

    // 1. Ichimoku Cloud (Screenshot 15)
    if (gpcIndicators.ichimoku) {{
      ctx.fillStyle = 'rgba(30, 58, 138, 0.45)';
      ctx.beginPath();
      for (var i = 0; i < numBars; i++) {{
        var cx = 40 + i * barWidth;
        var leadA = py(prices[i].o + 3);
        if (i === 0) ctx.moveTo(cx, leadA); else ctx.lineTo(cx, leadA);
      }}
      for (var i = numBars - 1; i >= 0; i--) {{
        var cx = 40 + i * barWidth;
        var leadB = py(prices[i].c - 2.5);
        ctx.lineTo(cx, leadB);
      }}
      ctx.closePath();
      ctx.fill();
    }}

    // 2. Candlesticks
    if (gpcIndicators.last_px) {{
      for (var i = 0; i < numBars; i++) {{
        var p = prices[i];
        var cx = 40 + i * barWidth;
        var isUp = p.c >= p.o;

        ctx.strokeStyle = isUp ? '#00e676' : '#ef4444';
        ctx.fillStyle = isUp ? '#00e676' : '#ef4444';
        ctx.lineWidth = 1;

        // Wick
        ctx.beginPath();
        ctx.moveTo(cx, py(p.h));
        ctx.lineTo(cx, py(p.l));
        ctx.stroke();

        // Body
        var bodyTop = py(Math.max(p.o, p.c));
        var bodyH = Math.max(2, Math.abs(py(p.o) - py(p.c)));
        ctx.fillRect(cx - barWidth * 0.35, bodyTop, barWidth * 0.7, bodyH);
      }}
    }}

    // 3. Moving Averages
    if (gpcIndicators.ma5) drawMaLine(ctx, prices, 5, '#38bdf8', barWidth, py);
    if (gpcIndicators.ma10) drawMaLine(ctx, prices, 10, '#f59e0b', barWidth, py);
    if (gpcIndicators.ma15) drawMaLine(ctx, prices, 15, '#ec4899', barWidth, py);

    // 4. Symmetrical Triangle Breakout Pattern (Image 16)
    if (gpcIndicators.triangle) {{
      ctx.strokeStyle = '#ef4444';
      ctx.lineWidth = 2.5;
      // Upper resistance descending line
      ctx.beginPath();
      ctx.moveTo(40 + 10 * barWidth, py(408));
      ctx.lineTo(40 + 32 * barWidth, py(401));
      ctx.stroke();
      // Lower support ascending line
      ctx.beginPath();
      ctx.moveTo(40 + 5 * barWidth, py(391));
      ctx.lineTo(40 + 32 * barWidth, py(400.5));
      ctx.stroke();
    }}
  }}

  function drawMaLine(ctx, prices, period, color, barWidth, pyFunc) {{
    ctx.strokeStyle = color;
    ctx.lineWidth = 1.5;
    ctx.beginPath();
    for (var i = period; i < prices.length; i++) {{
      var sum = 0;
      for (var j = 0; j < period; j++) sum += prices[i - j].c;
      var avg = sum / period;
      var x = 40 + i * barWidth;
      var y = pyFunc(avg);
      if (i === period) ctx.moveTo(x, y); else ctx.lineTo(x, y);
    }}
    ctx.stroke();
  }}

  // ═══════════════════════════════════════════════════════════════
  // ── VIEW 7: VOL 3D VOLATILITY SURFACE (SCREENSHOTS 13, 17) ──
  // ═══════════════════════════════════════════════════════════════
  function initVolSurfaceCanvas() {{
    setTimeout(drawVolSurface, 100);
  }}

  window.rotateVolSurface = function(deg) {{
    currentVolRot = (currentVolRot + deg) % 360;
    drawVolSurface();
  }};

  window.resetVolSurfaceView = function() {{
    currentVolRot = 35;
    drawVolSurface();
  }};

  function drawVolSurface() {{
    var canvas = document.getElementById('vol_surface_canvas');
    if (!canvas) return;
    var ctx = canvas.getContext('2d');
    var w = canvas.width = canvas.parentElement.clientWidth;
    var h = canvas.height = canvas.parentElement.clientHeight;

    ctx.fillStyle = '#05080e';
    ctx.fillRect(0, 0, w, h);

    // 3D Perspective Isometric Mesh Grid
    var terms = ['10 Mar', '19 May', '18 Aug', '19 Jan', '20 Jun', '31 Dec'];
    var strikes = [80, 85, 90, 95, 100, 105, 110, 115, 120];

    var cx = w * 0.45;
    var cy = h * 0.65;
    var angle = currentVolRot * Math.PI / 180;
    var cosA = Math.cos(angle);
    var sinA = Math.sin(angle);

    function project3D(x, y, z) {{
      var px = (x - y) * cosA * 22;
      var py = (x + y) * sinA * 12 - z * 4.5;
      return {{ x: cx + px, y: cy + py }};
    }}

    // Draw Surface Wireframe Grid
    for (var t = 0; t < terms.length; t++) {{
      for (var s = 0; s < strikes.length - 1; s++) {{
        var m1 = strikes[s];
        var m2 = strikes[s + 1];
        // Implied Vol smile equation: ATM=52%, deep OTM put=72%, deep OTM call=62%
        var vol1 = 52 + Math.pow((m1 - 100) * 0.25, 2) + Math.sin(t * 0.5) * 4;
        var vol2 = 52 + Math.pow((m2 - 100) * 0.25, 2) + Math.sin(t * 0.5) * 4;

        var p1 = project3D(t * 3, s * 2, vol1 - 45);
        var p2 = project3D(t * 3, (s + 1) * 2, vol2 - 45);

        var col = vol1 > 65 ? '#ef4444' : (vol1 > 58 ? '#eab308' : '#22c55e');
        ctx.strokeStyle = col;
        ctx.lineWidth = 1.2;
        ctx.beginPath();
        ctx.moveTo(p1.x, p1.y);
        ctx.lineTo(p2.x, p2.y);
        ctx.stroke();

        if (t < terms.length - 1) {{
          var volNext = 52 + Math.pow((m1 - 100) * 0.25, 2) + Math.sin((t + 1) * 0.5) * 4;
          var pNext = project3D((t + 1) * 3, s * 2, volNext - 45);
          ctx.beginPath();
          ctx.moveTo(p1.x, p1.y);
          ctx.lineTo(pNext.x, pNext.y);
          ctx.stroke();
        }}
      }}
    }}
  }}

  // ═══════════════════════════════════════════════════════════════
  // ── UNIVERSAL SEARCH ENGINE & TICKER SWITCHER ──
  // ═══════════════════════════════════════════════════════════════
  window.handleBmapUniversalSearch = function(q) {{
    var box = document.getElementById('bmap_search_results_box');
    if (!box) return;
    q = (q || '').trim().toLowerCase();
    if (!q || q.length < 2) {{ box.style.display = 'none'; return; }}

    var matches = [];
    if ('bank branches us fdic'.includes(q)) {{
      matches.push({{ type: 'DATASET', name: 'Bank Branches (US)', sub: '1,675 FDIC Insured Branch Locations', fn: function() {{ jumpToBmapPreset('bank_branches'); }} }});
    }}
    if ('crude oil pipelines'.includes(q) || 'pipelines'.includes(q)) {{
      matches.push({{ type: 'DATASET', name: 'Crude Oil Pipelines', sub: '15 Transnational Arteries (Keystone, Druzhba, ESPO)', fn: function() {{ jumpToBmapPreset('crude_pipelines'); }} }});
    }}
    if ('manhattan'.includes(q) || 'broadway'.includes(q) || '400 broadway'.includes(q)) {{
      matches.push({{ type: 'LOCATION', name: 'Manhattan 400 Broadway', sub: 'Street-Level Satellite FDIC Cluster', fn: function() {{ jumpToBmapPreset('manhattan'); }} }});
    }}
    if ('greg mortimer'.includes(q) || 'devil island'.includes(q)) {{
      matches.push({{ type: 'VESSEL', name: 'GREG MORTIMER (IMO 9834648)', sub: 'Antarctic Expedition Destination DEVIL ISLAND', fn: function() {{ jumpToBmapPreset('greg_mortimer'); }} }});
    }}
    if ('hormuz'.includes(q) || 'strait of hormuz'.includes(q)) {{
      matches.push({{ type: 'CHOKE POINT', name: 'Strait of Hormuz', sub: 'Persian Gulf TSS Corridor', fn: function() {{ jumpToBmapPreset('hormuz'); }} }});
    }}
    if ('supply chain'.includes(q) || 'splc'.includes(q) || 'apple'.includes(q) || 'lockheed'.includes(q)) {{
      matches.push({{ type: 'FUNCTION', name: 'SPLC Supply Chain Analysis', sub: 'Multi-Tier Supplier & Customer Graph', fn: function() {{ switchBmapView('splc'); }} }});
    }}
    if ('currency'.includes(q) || 'fxc'.includes(q) || 'fx'.includes(q)) {{
      matches.push({{ type: 'FUNCTION', name: 'FXC Currency Rates Matrix', sub: 'Asian Cross-Rates & Heat Map', fn: function() {{ switchBmapView('fxc'); }} }});
    }}
    if ('volatility'.includes(q) || 'vol'.includes(q) || 'surface'.includes(q)) {{
      matches.push({{ type: 'FUNCTION', name: 'VOL 3D Volatility Surface', sub: 'TSLA 3D Implied Volatility Mesh', fn: function() {{ switchBmapView('vol'); }} }});
    }}

    if (matches.length === 0) {{
      box.innerHTML = '<div style=\"padding:8px 12px;color:#64748b;font-size:10px;\">No matching securities or assets found</div>';
    }} else {{
      box.innerHTML = '';
      matches.forEach(function(m) {{
        var row = document.createElement('div');
        row.style.cssText = 'padding:7px 12px;border-bottom:1px solid #142236;cursor:pointer;display:flex;justify-content:space-between;align-items:center;';
        row.onclick = function() {{
          if (m.fn) m.fn();
          box.style.display = 'none';
        }};
        row.innerHTML =
          '<div><div style=\"color:#00e5ff;font-size:10.5px;font-weight:700;\">' + m.name + '</div>' +
          '<div style=\"color:#64748b;font-size:9px;\">' + m.sub + '</div></div>' +
          '<span class=\"badge\" style=\"background:#1e3a5f;color:#38bdf8;font-size:8.5px;\">' + m.type + '</span>';
        box.appendChild(row);
      }});
    }}
    box.style.display = 'block';
  }};

  window.switchBmapTicker = function(tickerKey) {{
    var presets = {{
      SPY: {{ sym: 'SPY US $', last: 'C 404.190', chg: '+6.380', bidask: 'Z404.120 / 404.130P   11 × 1558', vol: '90,119,952', o: '399.710Z', h: '404.450B', l: '399.030T', val: '36.272B', color: '#00e676' }},
      AAPL: {{ sym: 'AAPL US $', last: '152.352', chg: '-1.478', bidask: '152.340 / 152.360   4 × 4', vol: '19,862,832', o: '153.700', h: '154.030', l: '151.780', val: '3.048B', color: '#ef4444' }},
      TSLA: {{ sym: 'TSLA US $', last: '197.620', chg: '+7.150', bidask: '197.600 / 197.640   25 × 38', vol: '142,500,000', o: '191.000', h: '199.200', l: '189.500', val: '28.16B', color: '#00e676' }},
      LMT: {{ sym: 'LMT US $', last: '442.800', chg: '+3.100', bidask: '442.750 / 442.850   8 × 12', vol: '1,420,000', o: '440.000', h: '444.500', l: '439.200', val: '628.7M', color: '#00e676' }},
      BRENT: {{ sym: 'CO1 Comdty $', last: '75.820', chg: '+0.420', bidask: '75.810 / 75.830   42 × 38', vol: '241,850', o: '75.400', h: '76.150', l: '75.120', val: '18.34B', color: '#00e676' }},
      WTI: {{ sym: 'CL1 Comdty $', last: '71.400', chg: '+0.380', bidask: '71.390 / 71.410   55 × 60', vol: '312,400', o: '71.020', h: '71.800', l: '70.850', val: '22.31B', color: '#00e676' }},
      POLYCAB: {{ sym: 'POLYCAB IN ₹', last: '6,450.00', chg: '+142.50 (+2.26%)', bidask: '6,448.00 / 6,452.00   250 × 420', vol: '842,100', o: '6,320.00', h: '6,480.00', l: '6,310.00', val: '543.1 Cr', color: '#00e676' }},
      MPS: {{ sym: 'MPSLTD IN ₹', last: '2,145.00', chg: '+38.00 (+1.80%)', bidask: '2,142.00 / 2,148.00   85 × 120', vol: '142,500', o: '2,110.00', h: '2,160.00', l: '2,105.00', val: '30.5 Cr', color: '#00e676' }}
    }};

    var p = presets[tickerKey] || presets.SPY;
    document.getElementById('bb_sym').textContent = p.sym;
    document.getElementById('bb_last').textContent = p.last;
    document.getElementById('bb_chg').textContent = p.chg;
    document.getElementById('bb_bidask').textContent = p.bidask;
    document.getElementById('bb_vol').textContent = p.vol;
    document.getElementById('bb_open').textContent = p.o;
    document.getElementById('bb_high').textContent = p.h;
    document.getElementById('bb_low').textContent = p.l;
    document.getElementById('bb_val').textContent = p.val;
  }};

  // Document Click Closes Search
  document.addEventListener('click', function(e) {{
    var box = document.getElementById('bmap_search_results_box');
    var input = document.getElementById('bmap_universal_search');
    if (box && e.target !== input && !box.contains(e.target)) box.style.display = 'none';
  }});

  // DOM Ready
  if (document.readyState === 'loading') {{
    document.addEventListener('DOMContentLoaded', initLeafletBmap);
  }} else {{
    setTimeout(initLeafletBmap, 100);
  }}

}})();
</script>"""

    with open(os.path.join(BASE_DIR, "bmap_js_template.js"), "w", encoding="utf-8") as f:
        f.write(js_code.strip())
    print(f"Generated bmap_js_template.js ({len(js_code)} bytes)")

if __name__ == "__main__":
    generate_js()

