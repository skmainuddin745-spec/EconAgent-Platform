"""
generate_global_bmap_js.py
Generates bmap_js_template.js containing all Leaflet rendering logic,
real-time vessel kinematics, auto-adaptive satellite connection,
suggested & new datasets drawers, and global multi-asset ecosystem.
"""

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

from global_assets_data import (
    GLOBAL_AIS_VESSELS,
    GLOBAL_UTILITIES,
    GLOBAL_REFINERIES,
    GLOBAL_LNG_TERMINALS,
    GLOBAL_SEAPORTS,
    GLOBAL_SEMICONDUCTOR_FABS,
    GLOBAL_DATA_CENTERS,
    GLOBAL_FINANCIAL_CENTERS,
    GLOBAL_MINING_HUBS,
    GLOBAL_FERTILIZER_PLANTS,
    GLOBAL_STORAGE_TERMINALS,
    GLOBAL_NATURAL_GAS_HUBS,
    GLOBAL_WEATHER_STATIONS,
    GLOBAL_SEISMIC_EARTHQUAKES,
    GLOBAL_CYCLONES,
    GLOBAL_DENSE_GRID
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

    global_vessels_json = json.dumps(GLOBAL_AIS_VESSELS)
    global_utilities_json = json.dumps(GLOBAL_UTILITIES)
    global_refineries_json = json.dumps(GLOBAL_REFINERIES)
    global_lng_json = json.dumps(GLOBAL_LNG_TERMINALS)
    global_seaports_json = json.dumps(GLOBAL_SEAPORTS)
    global_fabs_json = json.dumps(GLOBAL_SEMICONDUCTOR_FABS)
    global_dc_json = json.dumps(GLOBAL_DATA_CENTERS)
    global_fin_json = json.dumps(GLOBAL_FINANCIAL_CENTERS)
    global_mines_json = json.dumps(GLOBAL_MINING_HUBS)
    global_fert_json = json.dumps(GLOBAL_FERTILIZER_PLANTS)
    global_storage_json = json.dumps(GLOBAL_STORAGE_TERMINALS)
    global_gas_hubs_json = json.dumps(GLOBAL_NATURAL_GAS_HUBS)
    global_weather_json = json.dumps(GLOBAL_WEATHER_STATIONS)
    global_earthquakes_json = json.dumps(GLOBAL_SEISMIC_EARTHQUAKES)
    global_cyclones_json = json.dumps(GLOBAL_CYCLONES)
    global_dense_grid_json = json.dumps(GLOBAL_DENSE_GRID)

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

  // Worldwide Institutional Datasets
  var globalVessels = {global_vessels_json};
  var globalUtilities = {global_utilities_json};
  var globalRefineries = {global_refineries_json};
  var globalLngTerminals = {global_lng_json};
  var globalSeaports = {global_seaports_json};
  var globalSemiconductorFabs = {global_fabs_json};
  var globalDataCenters = {global_dc_json};
  var globalFinancialCenters = {global_fin_json};
  var globalMiningHubs = {global_mines_json};
  var globalFertilizerPlants = {global_fert_json};
  var globalStorageTerminals = {global_storage_json};
  var globalGasHubs = {global_gas_hubs_json};
  var globalWeatherStations = {global_weather_json};
  var globalEarthquakes = {global_earthquakes_json};
  var globalCyclones = {global_cyclones_json};
  var globalDenseGrid = {global_dense_grid_json};

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

  // Global Map State
  var leafletMap = null;
  var baseTileLayers = {{}};
  var currentTileType = 'dark';
  var datasetLayerGroups = {{}};
  
  // Active layer state flags
  var activeLayers = {{
    bank_branches: true,
    vessels: true,
    crude_pipelines: true,
    power_plants: true,
    refineries: true,
    lng_terminals: true,
    seaports: true,
    semiconductor_fabs: true,
    data_centers: true,
    financial_centers: true,
    mining_hubs: true,
    fertilizers: false,
    storage_terminals: false,
    gas_hubs: false,
    weather_stations: false,
    earthquakes: false,
    world_equity: false,
    dense_grid: false
  }};

  var activeFollowVessel = null;
  var showArpaVectors = true;
  var currentActiveView = 'map';
  var activeSplcTicker = 'AAPL';
  var currentVolRot = 35;
  var liveKinematicsTimer = null;

  // ═══════════════════════════════════════════════════════════════
  // ── MAP INITIALIZATION (ZERO API KEY & ZERO WATERMARKS) ──
  // ═══════════════════════════════════════════════════════════════
  function initLeafletBmap() {{
    var container = document.getElementById('bmap_leaflet_map');
    if (!container || typeof L === 'undefined') return;

    // Zero API key, institutional Esri dark and real satellite imagery tiles (No CartoDB watermarks)
    baseTileLayers.dark = L.tileLayer('https://services.arcgisonline.com/arcgis/rest/services/Canvas/World_Dark_Gray_Base/MapServer/tile/{{z}}/{{y}}/{{x}}', {{
      maxZoom: 18, minZoom: 1, attribution: 'Bloomberg / Esri Dark Canvas (Zero Watermark)'
    }});
    baseTileLayers.dark_ref = L.tileLayer('https://services.arcgisonline.com/arcgis/rest/services/Canvas/World_Dark_Gray_Reference/MapServer/tile/{{z}}/{{y}}/{{x}}', {{
      maxZoom: 18, minZoom: 1
    }});
    baseTileLayers.satellite = L.tileLayer('https://services.arcgisonline.com/arcgis/rest/services/World_Imagery/MapServer/tile/{{z}}/{{y}}/{{x}}', {{
      maxZoom: 19, minZoom: 1, attribution: 'Esri High-Resolution World Imagery (Sub-Meter Satellite)'
    }});
    baseTileLayers.nautical = L.tileLayer('https://{{s}}.tile.openstreetmap.org/{{z}}/{{x}}/{{y}}.png', {{
      maxZoom: 18, minZoom: 1, attribution: 'OpenStreetMap Nautical Overlay'
    }});

    leafletMap = L.map('bmap_leaflet_map', {{
      center: [26.4, 56.2],
      zoom: 6,
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

    // Initialize All Layer Groups
    initBankBranchesLayer();
    initPipelinesLayers();
    initVesselsLayer();
    initGlobalInfrastructureLayers();
    initWorldEquityLayer();
    initDenseGridLayer();

    // Start Live AIS Dead-Reckoning Kinematics Engine (2-second updates)
    startLiveKinematicsEngine();

    // Render Sidebars and Secondary Views
    renderDatasetSidebar();
    renderBmapTableData('berths');
    renderReadNewsStories();
    renderSplcNetwork('AAPL');
    renderFxcMatrix();
    initGpcCandlestickChart();
    initVolSurfaceCanvas();
  }}

  // ═══════════════════════════════════════════════════════════════
  // ── LAYER 1: US BANK BRANCHES & MANHATTAN STREET SATELLITE ──
  // ═══════════════════════════════════════════════════════════════
  function initBankBranchesLayer() {{
    datasetLayerGroups['bank_branches'] = L.layerGroup().addTo(leafletMap);
    renderBankBranchesOnMap(usBankBranches);

    // Manhattan high-res branch markers
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
      m.on('click', function() {{ showGenericBranchPopup(b); }});
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
  // ── LAYER 2: CRUDE & GAS PIPELINES (SCREENSHOT 12, 27) ──
  // ═══════════════════════════════════════════════════════════════
  function initPipelinesLayers() {{
    var crudeGroup = L.layerGroup();
    crudePipelines.forEach(function(pipe) {{
      var poly = L.polyline(pipe.coords, {{
        color: '#3b82f6',
        weight: 3.5,
        opacity: 0.9,
        lineCap: 'round',
        lineJoin: 'round'
      }});
      poly.bindPopup('<div style="font-family:monospace;font-size:11px;color:#fff;">' +
        '<strong style="color:#38bdf8;">' + pipe.name + '</strong><br>' +
        'Capacity: <span style="color:#00e676;">' + pipe.cap + '</span><br>' +
        'Operator: ' + pipe.operator + '<br>' +
        'Route: ' + pipe.route + '<br>' +
        'Status: <span style="color:#ffaa00;">' + pipe.status + '</span></div>');
      crudeGroup.addLayer(poly);
    }});
    datasetLayerGroups['crude_pipelines'] = crudeGroup.addTo(leafletMap);

    var gasGroup = L.layerGroup();
    gasPipelines.forEach(function(gp) {{
      var poly = L.polyline(gp.coords, {{
        color: '#fbbf24',
        weight: 2.5,
        dashArray: '6, 6',
        opacity: 0.85
      }});
      poly.bindPopup('<div style="font-family:monospace;font-size:11px;color:#fff;">' +
        '<strong style="color:#fbbf24;">' + gp.name + '</strong><br>' +
        'System: ' + gp.system + '<br>' +
        'Type: ' + gp.type + '<br>' +
        'Capacity: ' + gp.cap + '</div>');
      gasGroup.addLayer(poly);
    }});
    datasetLayerGroups['gas_pipelines'] = gasGroup;
  }}

  // ═══════════════════════════════════════════════════════════════
  // ── LAYER 3: LIVE AIS VESSELS & STRAIT OF HORMUZ CONVOYS (IMAGE 1 & 4) ──
  // ═══════════════════════════════════════════════════════════════
  function initVesselsLayer() {{
    var vGroup = L.layerGroup();

    globalVessels.forEach(function(v) {{
      var isHormuz = v.region.indexOf('Hormuz') >= 0;
      var markerColor = isHormuz ? '#00e5ff' : '#38bdf8';
      
      // SVG Nautical Boat Icon with Heading Direction Arrow
      var iconHtml = '<div style="transform: rotate(' + v.course + 'deg); width: 20px; height: 20px; display: flex; align-items: center; justify-content: center;">' +
        '<svg width="18" height="18" viewBox="0 0 24 24" fill="' + markerColor + '" style="filter: drop-shadow(0 0 3px ' + markerColor + ');">' +
        '<polygon points="12,2 22,22 12,18 2,22"/>' +
        '</svg></div>';

      var customIcon = L.divIcon({{
        html: iconHtml,
        className: 'bmap-vessel-marker',
        iconSize: [20, 20],
        iconAnchor: [10, 10]
      }});

      var m = L.marker([v.lat, v.lon], {{ icon: customIcon }});
      
      // Heading Vector Line (ARPA Dead Reckoning Course Vector)
      var headingDist = v.speed * 0.008;
      var rad = v.course * Math.PI / 180;
      var headLat = v.lat + headingDist * Math.cos(rad);
      var headLon = v.lon + (headingDist * Math.sin(rad)) / Math.cos(v.lat * Math.PI / 180);
      
      var headingLine = L.polyline([[v.lat, v.lon], [headLat, headLon]], {{
        color: markerColor,
        weight: 1.5,
        dashArray: '3, 3',
        opacity: 0.8
      }});

      m.vesselData = v;
      v.marker = m;
      v.headingLine = headingLine;

      m.on('click', function() {{
        selectActiveVessel(v);
      }});

      vGroup.addLayer(m);
      if (showArpaVectors) vGroup.addLayer(headingLine);
    }});

    datasetLayerGroups['vessels'] = vGroup.addTo(leafletMap);
  }}

  // ═══════════════════════════════════════════════════════════════
  // ── LIVE DEAD-RECKONING KINEMATICS ENGINE (2-SECOND TICK) ──
  // ═══════════════════════════════════════════════════════════════
  window.bmapVessels = globalVessels;
  window.datasetLayerGroups = datasetLayerGroups;
  window.activeLayers = activeLayers;

  window.stepKinematics = function(dt) {{
    dt = dt || 2;
    globalVessels.forEach(function(v) {{
      if (v.speed > 0) {{
        var speedMs = (v.speed * 1852) / 3600;
        var distMeters = speedMs * dt;
        var rad = (v.course * Math.PI) / 180;
        var dLat = (distMeters * Math.cos(rad)) / 111139;
        var dLon = (distMeters * Math.sin(rad)) / (111139 * Math.cos((v.lat * Math.PI) / 180));
        v.lat += dLat;
        v.lon += dLon;
        if (v.marker) v.marker.setLatLng([v.lat, v.lon]);
        if (v.headingLine && showArpaVectors) {{
          var headingDist = v.speed * 0.008;
          var hLat = v.lat + headingDist * Math.cos(rad);
          var hLon = v.lon + (headingDist * Math.sin(rad)) / Math.cos(v.lat * Math.PI / 180);
          v.headingLine.setLatLngs([[v.lat, v.lon], [hLat, hLon]]);
        }}
      }}
    }});
    if (activeFollowVessel && leafletMap) {{
      leafletMap.panTo([activeFollowVessel.lat, activeFollowVessel.lon], {{ animate: true, duration: 0.4 }});
    }}
  }};

  function startLiveKinematicsEngine() {{
    if (liveKinematicsTimer) clearInterval(liveKinematicsTimer);
    liveKinematicsTimer = setInterval(function() {{ window.stepKinematics(2); }}, 2000);
    window.liveKinematicsTimer = liveKinematicsTimer;


  }}

  function selectActiveVessel(v) {{
    var card = document.getElementById('bmap_vessels_filter_card');
    if (card) card.style.display = 'block';

    var nameEl = document.getElementById('vessel_hud_name');
    if (nameEl) nameEl.textContent = v.name;

    var specsEl = document.getElementById('vessel_hud_specs');
    if (specsEl) specsEl.textContent = v.speed.toFixed(1) + ' kts · ' + v.course + '° True · Draft ' + v.draft + 'm';

    var berthEl = document.getElementById('vessel_hud_berth');
    if (berthEl) berthEl.textContent = 'Berth / Route: ' + v.berth;

    var destEl = document.getElementById('vessel_card_dest');
    if (destEl) destEl.textContent = v.dest;

    var draftEl = document.getElementById('vessel_card_draft');
    if (draftEl) draftEl.textContent = v.draft + 'm';

    var dwtEl = document.getElementById('vessel_card_dwt');
    if (dwtEl) dwtEl.textContent = v.dwt.toLocaleString() + ' MT';

    var classEl = document.getElementById('vessel_card_class');
    if (classEl) classEl.textContent = v.type;

    var ownerEl = document.getElementById('vessel_card_owner');
    if (ownerEl) ownerEl.textContent = v.owner;

    window.selectedVessel = v;
  }}

  window.zoomToActiveVessel = function() {{
    if (!window.selectedVessel && globalVessels.length > 0) window.selectedVessel = globalVessels[0];
    if (window.selectedVessel && leafletMap) {{
      leafletMap.flyTo([window.selectedVessel.lat, window.selectedVessel.lon], 13, {{ duration: 1.2 }});
    }}
  }};

  window.toggleFollowActiveVessel = function() {{
    if (!window.selectedVessel && globalVessels.length > 0) window.selectedVessel = globalVessels[0];
    var v = window.selectedVessel;
    if (!v) return;

    var btn = document.getElementById('btn_follow_vsl');
    var pill = document.getElementById('bmap_autofollow_pill');
    var pillName = document.getElementById('bmap_autofollow_name');

    if (activeFollowVessel === v) {{
      activeFollowVessel = null;
      if (btn) {{ btn.textContent = '🎯 Follow'; btn.style.background = '#065f46'; }}
      if (pill) pill.style.display = 'none';
    }} else {{
      activeFollowVessel = v;
      if (btn) {{ btn.textContent = '🔒 Following'; btn.style.background = '#0284c7'; }}
      if (pill) {{
        pill.style.display = 'inline-flex';
        if (pillName) pillName.textContent = v.name;
      }}
      leafletMap.panTo([v.lat, v.lon], {{ animate: true }});
    }}
  }};

  window.unlockFollowVessel = function() {{
    activeFollowVessel = null;
    var pill = document.getElementById('bmap_autofollow_pill');
    if (pill) pill.style.display = 'none';
    var btn = document.getElementById('btn_follow_vsl');
    if (btn) {{ btn.textContent = '🎯 Follow'; btn.style.background = '#065f46'; }}
  }};

  window.toggleArpaVectors = function() {{
    showArpaVectors = !showArpaVectors;
    var vGroup = datasetLayerGroups['vessels'];
    if (!vGroup) return;

    globalVessels.forEach(function(v) {{
      if (v.headingLine) {{
        if (showArpaVectors) {{
          vGroup.addLayer(v.headingLine);
        }} else {{
          vGroup.removeLayer(v.headingLine);
        }}
      }}
    }});
  }};

  window.filterVesselsByName = function(vKey) {{
    if (vKey === 'ALL') {{
      leafletMap.flyTo([26.4, 56.2], 6, {{ duration: 1.2 }});
    }} else if (vKey === 'HORMUZ_FLEET') {{
      jumpToBmapPreset('hormuz');
    }} else if (vKey === 'GREG_MORTIMER') {{
      jumpToBmapPreset('greg_mortimer');
    }} else {{
      var v = globalVessels.find(function(item) {{ return item.name === vKey; }});
      if (v) {{
        selectActiveVessel(v);
        leafletMap.flyTo([v.lat, v.lon], 12, {{ duration: 1.2 }});
      }}
    }}
  }};

  // ═══════════════════════════════════════════════════════════════
  // ── LAYER 4: WORLDWIDE INSTITUTIONAL INFRASTRUCTURE SUITE ──
  // ═══════════════════════════════════════════════════════════════
  function initGlobalInfrastructureLayers() {{
    var canvasRenderer = L.canvas({{ padding: 0.5 }});

    // Utilities & Power Plants
    var pGroup = L.layerGroup();
    globalUtilities.forEach(function(u) {{
      var m = L.circleMarker([u.lat, u.lon], {{
        renderer: canvasRenderer,
        radius: 6,
        fillColor: '#f59e0b',
        color: '#d97706',
        weight: 1.5,
        fillOpacity: 0.9
      }});
      m.bindPopup('<div style="font-family:monospace;font-size:11px;color:#fff;">' +
        '<strong style="color:#f59e0b;">' + u.name + '</strong> (' + u.country + ')<br>' +
        'Type: <span style="color:#ffaa00;">' + u.type + '</span><br>' +
        'Capacity: <span style="color:#00e676;">' + u.cap + '</span><br>' +
        'Operator: ' + u.operator + '<br>' +
        'Authority: ' + u.source + '<br>' +
        'Status: ' + u.status + '</div>');
      pGroup.addLayer(m);
    }});
    datasetLayerGroups['power_plants'] = pGroup.addTo(leafletMap);

    // Refineries
    var rGroup = L.layerGroup();
    globalRefineries.forEach(function(r) {{
      var m = L.circleMarker([r.lat, r.lon], {{
        renderer: canvasRenderer,
        radius: 6.5,
        fillColor: '#ef4444',
        color: '#b91c1c',
        weight: 1.5,
        fillOpacity: 0.9
      }});
      m.bindPopup('<div style="font-family:monospace;font-size:11px;color:#fff;">' +
        '<strong style="color:#ef4444;">' + r.name + '</strong> (' + r.country + ')<br>' +
        'Throughput: <span style="color:#ffaa00;">' + r.cap + '</span><br>' +
        'Operator: ' + r.operator + '<br>' +
        'Source: ' + r.source + '<br>' +
        'Status: <span style="color:#00e676;">' + r.status + '</span></div>');
      rGroup.addLayer(m);
    }});
    datasetLayerGroups['refineries'] = rGroup.addTo(leafletMap);

    // LNG Terminals
    var lngGroup = L.layerGroup();
    globalLngTerminals.forEach(function(l) {{
      var m = L.circleMarker([l.lat, l.lon], {{
        renderer: canvasRenderer,
        radius: 6,
        fillColor: '#06b6d4',
        color: '#0891b2',
        weight: 1.5,
        fillOpacity: 0.9
      }});
      m.bindPopup('<div style="font-family:monospace;font-size:11px;color:#fff;">' +
        '<strong style="color:#06b6d4;">' + l.name + '</strong> (' + l.country + ')<br>' +
        'Role: ' + l.type + '<br>' +
        'Capacity: <span style="color:#00e676;">' + l.cap + '</span><br>' +
        'Operator: ' + l.operator + '<br>' +
        'Status: ' + l.status + '</div>');
      lngGroup.addLayer(m);
    }});
    datasetLayerGroups['lng_terminals'] = lngGroup.addTo(leafletMap);

    // Seaports
    var portGroup = L.layerGroup();
    globalSeaports.forEach(function(p) {{
      var m = L.circleMarker([p.lat, p.lon], {{
        renderer: canvasRenderer,
        radius: 6,
        fillColor: '#10b981',
        color: '#059669',
        weight: 1.5,
        fillOpacity: 0.9
      }});
      m.bindPopup('<div style="font-family:monospace;font-size:11px;color:#fff;">' +
        '<strong style="color:#10b981;">' + p.name + '</strong> (' + p.country + ')<br>' +
        'Volume: <span style="color:#ffaa00;">' + p.teu + '</span><br>' +
        'Operator: ' + p.operator + '<br>' +
        'Status: ' + p.status + '</div>');
      portGroup.addLayer(m);
    }});
    datasetLayerGroups['seaports'] = portGroup.addTo(leafletMap);

    // Semiconductor Fabs
    var fabGroup = L.layerGroup();
    globalSemiconductorFabs.forEach(function(f) {{
      var m = L.circleMarker([f.lat, f.lon], {{
        renderer: canvasRenderer,
        radius: 6,
        fillColor: '#a855f7',
        color: '#7c3aed',
        weight: 1.5,
        fillOpacity: 0.9
      }});
      m.bindPopup('<div style="font-family:monospace;font-size:11px;color:#fff;">' +
        '<strong style="color:#a855f7;">' + f.name + '</strong> (' + f.country + ')<br>' +
        'Node / Litho: <span style="color:#ffaa00;">' + f.node + '</span><br>' +
        'Operator: ' + f.operator + '<br>' +
        'Status: <span style="color:#00e676;">' + f.status + '</span></div>');
      fabGroup.addLayer(m);
    }});
    datasetLayerGroups['semiconductor_fabs'] = fabGroup.addTo(leafletMap);

    // Data Centers
    var dcGroup = L.layerGroup();
    globalDataCenters.forEach(function(d) {{
      var m = L.circleMarker([d.lat, d.lon], {{
        renderer: canvasRenderer,
        radius: 6,
        fillColor: '#22c55e',
        color: '#16a34a',
        weight: 1.5,
        fillOpacity: 0.9
      }});
      m.bindPopup('<div style="font-family:monospace;font-size:11px;color:#fff;">' +
        '<strong style="color:#22c55e;">' + d.name + '</strong> (' + d.country + ')<br>' +
        'Capacity: <span style="color:#ffaa00;">' + d.capacity + '</span><br>' +
        'Operators: ' + d.operators + '<br>' +
        'Status: ' + d.status + '</div>');
      dcGroup.addLayer(m);
    }});
    datasetLayerGroups['data_centers'] = dcGroup.addTo(leafletMap);

    // Financial Centers & Exchanges
    var finGroup = L.layerGroup();
    globalFinancialCenters.forEach(function(fc) {{
      var m = L.circleMarker([fc.lat, fc.lon], {{
        renderer: canvasRenderer,
        radius: 7,
        fillColor: '#eab308',
        color: '#ca8a04',
        weight: 2,
        fillOpacity: 0.95
      }});
      m.bindPopup('<div style="font-family:monospace;font-size:11px;color:#fff;">' +
        '<strong style="color:#eab308;">' + fc.name + '</strong> (' + fc.country + ')<br>' +
        'Market Scale: <span style="color:#00e676;">' + fc.val + '</span><br>' +
        'Institution: ' + fc.institution + '<br>' +
        'Status: ' + fc.status + '</div>');
      finGroup.addLayer(m);
    }});
    datasetLayerGroups['financial_centers'] = finGroup.addTo(leafletMap);

    // Critical Mining Hubs
    var mineGroup = L.layerGroup();
    globalMiningHubs.forEach(function(mHub) {{
      var m = L.circleMarker([mHub.lat, mHub.lon], {{
        renderer: canvasRenderer,
        radius: 6,
        fillColor: '#f97316',
        color: '#c2410c',
        weight: 1.5,
        fillOpacity: 0.9
      }});
      m.bindPopup('<div style="font-family:monospace;font-size:11px;color:#fff;">' +
        '<strong style="color:#f97316;">' + mHub.name + '</strong> (' + mHub.country + ')<br>' +
        'Commodity: <span style="color:#ffaa00;">' + mHub.product + '</span><br>' +
        'Operator: ' + mHub.operator + '<br>' +
        'Status: ' + mHub.status + '</div>');
      mineGroup.addLayer(m);
    }});
    datasetLayerGroups['mining_hubs'] = mineGroup.addTo(leafletMap);

    // Fertilizer Plants
    var fertGroup = L.layerGroup();
    globalFertilizerPlants.forEach(function(fp) {{
      var m = L.circleMarker([fp.lat, fp.lon], {{
        renderer: canvasRenderer,
        radius: 5.5,
        fillColor: '#84cc16',
        color: '#65a30d',
        weight: 1.5,
        fillOpacity: 0.9
      }});
      m.bindPopup('<div style="font-family:monospace;font-size:11px;color:#fff;">' +
        '<strong style="color:#84cc16;">' + fp.name + '</strong> (' + fp.country + ')<br>' +
        'Production: ' + fp.product + '<br>' +
        'Operator: ' + fp.operator + '</div>');
      fertGroup.addLayer(m);
    }});
    datasetLayerGroups['fertilizers'] = fertGroup;

    // Storage Terminals
    var stgGroup = L.layerGroup();
    globalStorageTerminals.forEach(function(st) {{
      var m = L.circleMarker([st.lat, st.lon], {{
        renderer: canvasRenderer,
        radius: 5.5,
        fillColor: '#60a5fa',
        color: '#2563eb',
        weight: 1.5,
        fillOpacity: 0.9
      }});
      m.bindPopup('<div style="font-family:monospace;font-size:11px;color:#fff;">' +
        '<strong style="color:#60a5fa;">' + st.name + '</strong> (' + st.country + ')<br>' +
        'Capacity: ' + st.cap + '<br>' +
        'Operator: ' + st.operator + '</div>');
      stgGroup.addLayer(m);
    }});
    datasetLayerGroups['storage_terminals'] = stgGroup;

    // Gas Hubs
    var ghGroup = L.layerGroup();
    globalGasHubs.forEach(function(gh) {{
      var m = L.circleMarker([gh.lat, gh.lon], {{
        renderer: canvasRenderer,
        radius: 5.5,
        fillColor: '#fb923c',
        color: '#ea580c',
        weight: 1.5,
        fillOpacity: 0.9
      }});
      m.bindPopup('<div style="font-family:monospace;font-size:11px;color:#fff;">' +
        '<strong style="color:#fb923c;">' + gh.name + '</strong> (' + gh.country + ')<br>' +
        'Benchmark: ' + gh.cap + '<br>' +
        'Operator: ' + gh.operator + '</div>');
      ghGroup.addLayer(m);
    }});
    datasetLayerGroups['gas_hubs'] = ghGroup;

    // Weather Stations
    var wGroup = L.layerGroup();
    globalWeatherStations.forEach(function(ws) {{
      var m = L.circleMarker([ws.lat, ws.lon], {{
        renderer: canvasRenderer,
        radius: 5,
        fillColor: '#38bdf8',
        color: '#0284c7',
        weight: 1.5,
        fillOpacity: 0.9
      }});
      m.bindPopup('<div style="font-family:monospace;font-size:11px;color:#fff;">' +
        '<strong style="color:#38bdf8;">' + ws.name + '</strong><br>' +
        'Temp: ' + ws.temp + ' · Wind: ' + ws.wind + '<br>' +
        'Wave: ' + ws.wave + ' · Press: ' + ws.press + '</div>');
      wGroup.addLayer(m);
    }});
    datasetLayerGroups['weather_stations'] = wGroup;

    // Earthquakes
    var eqGroup = L.layerGroup();
    globalEarthquakes.forEach(function(eq) {{
      var m = L.circleMarker([eq.lat, eq.lon], {{
        radius: 12,
        fillColor: '#ef4444',
        color: '#dc2626',
        weight: 2,
        dashArray: '4, 4',
        fillOpacity: 0.4
      }});
      m.bindPopup('<div style="font-family:monospace;font-size:11px;color:#fff;">' +
        '<strong style="color:#ef4444;">' + eq.name + '</strong><br>' +
        'Mag: <span style="color:#f87171;">' + eq.mag + '</span> · Depth: ' + eq.depth + '<br>' +
        eq.impact + '</div>');
      eqGroup.addLayer(m);
    }});
    datasetLayerGroups['earthquakes'] = eqGroup;
  }}

  // ═══════════════════════════════════════════════════════════════
  // ── LAYER 5: DENSE WORLDWIDE INFRASTRUCTURE CONSTELLATION (IMAGE 3) ──
  // ═══════════════════════════════════════════════════════════════
  function initDenseGridLayer() {{
    var gridGroup = L.layerGroup();
    var canvasRenderer = L.canvas({{ padding: 0.5 }});

    globalDenseGrid.forEach(function(pt) {{
      var m = L.circleMarker([pt.lat, pt.lon], {{
        renderer: canvasRenderer,
        radius: 2.2,
        fillColor: '#fde047',
        color: '#eab308',
        weight: 0.5,
        fillOpacity: 0.75
      }});
      gridGroup.addLayer(m);
    }});

    datasetLayerGroups['dense_grid'] = gridGroup;
  }}

  // ═══════════════════════════════════════════════════════════════
  // ── LAYER 6: WORLD EQUITY MARKETS (SCREENSHOT 4) ──
  // ═══════════════════════════════════════════════════════════════
  function initWorldEquityLayer() {{
    var eqGroup = L.layerGroup();
    worldEquityData.forEach(function(eq) {{
      var col = eq.chg >= 0 ? '#22c55e' : '#ef4444';
      var m = L.circleMarker([eq.lat, eq.lon], {{
        radius: 6.5,
        fillColor: col,
        color: '#fff',
        weight: 1.5,
        fillOpacity: 0.95
      }});
      m.bindPopup('<div style="font-family:monospace;font-size:11px;color:#fff;">' +
        '<strong style="color:' + col + ';">' + eq.name + '</strong><br>' +
        'Index: ' + eq.idx + ' (' + eq.val.toLocaleString() + ')<br>' +
        'Net Change: <span style="color:' + col + ';">' + (eq.chg >= 0 ? '+' : '') + eq.chg.toFixed(2) + '%</span></div>');
      eqGroup.addLayer(m);
    }});
    datasetLayerGroups['world_equity'] = eqGroup;
  }}

  // ═══════════════════════════════════════════════════════════════
  // ── AUTO-ADAPTIVE REAL SATELLITE CONNECTION & ZOOM LOD ──
  // ═══════════════════════════════════════════════════════════════
  function handleMapZoomLOD() {{
    if (!leafletMap) return;
    var z = leafletMap.getZoom();

    if (currentTileType === 'auto') {{
      if (z >= 15) {{
        if (!leafletMap.hasLayer(baseTileLayers.satellite)) {{
          Object.values(baseTileLayers).forEach(function(l) {{ if (leafletMap.hasLayer(l)) leafletMap.removeLayer(l); }});
          baseTileLayers.satellite.addTo(leafletMap);
        }}
      }} else {{
        if (!leafletMap.hasLayer(baseTileLayers.dark)) {{
          Object.values(baseTileLayers).forEach(function(l) {{ if (leafletMap.hasLayer(l)) leafletMap.removeLayer(l); }});
          baseTileLayers.dark.addTo(leafletMap);
          baseTileLayers.dark_ref.addTo(leafletMap);
        }}
      }}
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
      handleMapZoomLOD();
      var b = document.getElementById('bmap_layer_auto'); if (b) b.classList.add('active');
    }}
  }};

  // ═══════════════════════════════════════════════════════════════
  // ── COUNTRY & SECTOR DROPDOWN FILTERS (INSTRUCTION 5) ──
  // ═══════════════════════════════════════════════════════════════
  window.onBmapCountrySelect = function(countryCode) {{
    if (!leafletMap) return;

    var scopeLabel = document.getElementById('bmap_scope_label');
    var countBadge = document.getElementById('bmap_objects_count_badge');

    var countryTargets = {{
      'ALL': {{ center: [25.0, 15.0], zoom: 2.5, name: 'GLOBAL MULTI-ASSET INFRASTRUCTURE ECOSYSTEM' }},
      'US': {{ center: [38.5, -96.5], zoom: 4.5, name: 'UNITED STATES — FDIC, HUBS, REFINERIES & CHIPS' }},
      'CN': {{ center: [32.0, 115.0], zoom: 4.5, name: 'CHINA — THREE GORGES, YANGSHAN, ZPC, SSE' }},
      'IN': {{ center: [21.5, 79.0], zoom: 5, name: 'INDIA — JAMNAGAR, BHADLA, NSE, JNPT & DISCOM GRID' }},
      'JP': {{ center: [36.0, 138.0], zoom: 5.5, name: 'JAPAN — KASHIWAZAKI, TSE, TOKYO BAY LNG, JASM' }},
      'DE': {{ center: [51.0, 10.5], zoom: 6, name: 'GERMANY — FRANKFURT ECB, REHDEN GAS, DE-CIX' }},
      'GB': {{ center: [54.0, -2.5], zoom: 6, name: 'UNITED KINGDOM — LSE, GRAIN LNG, HORNSEA WIND' }},
      'SA': {{ center: [24.5, 45.0], zoom: 5.5, name: 'SAUDI ARABIA — ARAMCO, RAS TANURA, JUBAIL, TADAWUL' }},
      'AE': {{ center: [24.8, 54.8], zoom: 7.5, name: 'UAE — HORMUZ CONVOYS, RUWAIS, JEBEL ALI, FUJAIRAH' }},
      'QA': {{ center: [25.35, 51.18], zoom: 9, name: 'QATAR — RAS LAFFAN LNG MEGA LIQUEFACTION' }},
      'SG': {{ center: [1.35, 103.82], zoom: 11, name: 'SINGAPORE — JURONG ISLAND, TUAS MEGA PORT, SGX' }},
      'KR': {{ center: [36.5, 128.0], zoom: 7, name: 'SOUTH KOREA — PYEONGTAEK, ULSAN, YEOSU, BUSAN' }},
      'AU': {{ center: [-25.0, 134.0], zoom: 4.5, name: 'AUSTRALIA — PILBARA IRON, GREENBUSHES LI, GORGON' }},
      'BR': {{ center: [-14.0, -52.0], zoom: 4.5, name: 'BRAZIL — ITAIPU HYDRO, CARAJÁS, SANTOS PORT' }},
      'CA': {{ center: [53.0, -105.0], zoom: 4, name: 'CANADA — BRUCE NUCLEAR, NUTRIEN POTASH' }},
      'FR': {{ center: [46.6, 1.9], zoom: 6, name: 'FRANCE — GRAVELINES NUCLEAR, DUNKIRK LNG' }},
      'NL': {{ center: [52.1, 5.3], zoom: 7.5, name: 'NETHERLANDS — ROTTERDAM PORT, SHELL PERNIS, ASML' }},
      'CH': {{ center: [46.8, 8.2], zoom: 7.5, name: 'SWITZERLAND — SIX EXCHANGE, ZURICH VAULTS' }},
      'CL': {{ center: [-24.3, -69.1], zoom: 6, name: 'CHILE — ESCONDIDA COPPER & ATACAMA LITHIUM' }},
      'ZA': {{ center: [-30.5, 23.0], zoom: 5.5, name: 'SOUTH AFRICA — KOEBERG NUCLEAR, SALDANHA BAY' }},
      'ID': {{ center: [-0.8, 114.0], zoom: 5, name: 'INDONESIA — GRASBERG MINE & NICKEL SMELTERS' }},
      'NG': {{ center: [6.4, 4.0], zoom: 6.5, name: 'NIGERIA — DANGOTE MEGA REFINERY, BONNY ISLAND' }}
    }};

    var tgt = countryTargets[countryCode] || countryTargets['ALL'];
    leafletMap.flyTo(tgt.center, tgt.zoom, {{ duration: 1.2 }});

    if (scopeLabel) scopeLabel.textContent = tgt.name;
    if (countBadge) countBadge.textContent = 'Country Focus Activated';
  }};

  window.onBmapSectorSelect = function(sectorKey) {{
    if (!leafletMap) return;

    if (sectorKey === 'ALL') {{
      Object.keys(activeLayers).forEach(function(k) {{
        if (!activeLayers[k] && datasetLayerGroups[k] && k !== 'dense_grid' && k !== 'gas_pipelines') {{
          window.toggleBmapDataset(k);
        }}
      }});
      return;
    }}

    // Activate selected sector and ensure its layer is visible
    if (datasetLayerGroups[sectorKey]) {{
      if (!activeLayers[sectorKey]) window.toggleBmapDataset(sectorKey);
      
      // Auto-fit bounds if markers exist
      var grp = datasetLayerGroups[sectorKey];
      if (grp.getLayers && grp.getLayers().length > 0) {{
        try {{
          var b = grp.getBounds();
          if (b && b.isValid()) leafletMap.flyToBounds(b, {{ padding: [50, 50], maxZoom: 10, duration: 1.2 }});
        }} catch(e) {{}}
      }}
    }}
  }};

  // ═══════════════════════════════════════════════════════════════
  // ── PRESETS QUICK-JUMP DISPATCHER (SATELLITE & HOTSPOTS) ──
  // ═══════════════════════════════════════════════════════════════
  window.jumpToBmapPreset = function(presetKey) {{
    if (!leafletMap) return;
    var labelEl = document.getElementById('bmap_scope_label');
    var countBadge = document.getElementById('bmap_objects_count_badge');

    if (presetKey === 'hormuz') {{
      // Image 4: Hormuz in real time
      leafletMap.flyTo([26.4, 56.2], 9, {{ duration: 1.2 }});
      setBmapTileLayer('dark');
      if (!activeLayers['vessels']) window.toggleBmapDataset('vessels');
      var cardVsl = document.getElementById('bmap_vessels_filter_card');
      if (cardVsl) cardVsl.style.display = 'block';
      if (labelEl) labelEl.textContent = 'STRAIT OF HORMUZ & PERSIAN GULF — 35+ LIVE TANKERS IN REAL TIME';
      if (countBadge) countBadge.textContent = '35 Tankers Active (Dead-Reckoning Kinematics)';

    }} else if (presetKey === 'dense_grid') {{
      // Image 3: Dense Global Constellation
      leafletMap.flyTo([25.0, 15.0], 2.5, {{ duration: 1.2 }});
      setBmapTileLayer('dark');
      if (!activeLayers['dense_grid']) window.toggleBmapDataset('dense_grid');
      if (labelEl) labelEl.textContent = 'GLOBAL DENSE ASSET CONSTELLATION (2,325+ WORLDWIDE POINTS)';
      if (countBadge) countBadge.textContent = '2,325 Dense Points Active';

    }} else if (presetKey === 'jamnagar') {{
      leafletMap.flyTo([22.361, 69.832], 16, {{ duration: 1.5 }});
      setBmapTileLayer('satellite');
      if (labelEl) labelEl.textContent = 'JAMNAGAR MEGA REFINERY COMPLEX (RELIANCE INDUSTRIES — 1.24M BPD)';
      if (countBadge) countBadge.textContent = "World's Largest Petroleum Refining Complex";

    }} else if (presetKey === 'three_gorges') {{
      leafletMap.flyTo([30.823, 111.003], 16, {{ duration: 1.5 }});
      setBmapTileLayer('satellite');
      if (labelEl) labelEl.textContent = 'THREE GORGES DAM (YANGTZE RIVER — 22,500 MW)';
      if (countBadge) countBadge.textContent = "World's Largest Power Station";

    }} else if (presetKey === 'tsmc_fab18') {{
      leafletMap.flyTo([23.115, 120.278], 17, {{ duration: 1.5 }});
      setBmapTileLayer('satellite');
      if (labelEl) labelEl.textContent = 'TSMC FAB 18 GIGAFAB (TAINAN SCIENCE PARK — 3NM/2NM HIGH-NA EUV)';
      if (countBadge) countBadge.textContent = "World's Leading Edge Wafer Fab";

    }} else if (presetKey === 'ras_laffan') {{
      leafletMap.flyTo([25.925, 51.535], 16, {{ duration: 1.5 }});
      setBmapTileLayer('satellite');
      if (labelEl) labelEl.textContent = 'RAS LAFFAN LNG MEGA LIQUEFACTION COMPLEX (QATAR — 77 MTPA)';
      if (countBadge) countBadge.textContent = 'Premier Global LNG Liquefaction Hub';

    }} else if (presetKey === 'fujairah') {{
      leafletMap.flyTo([25.178, 56.365], 16, {{ duration: 1.5 }});
      setBmapTileLayer('satellite');
      if (labelEl) labelEl.textContent = 'FUJAIRAH OIL BUNKERING ANCHORAGE & TERMINALS (UAE)';
      if (countBadge) countBadge.textContent = 'Strategic Hormuz Bypass Crude Export Hub';

    }} else if (presetKey === 'manhattan') {{
      leafletMap.flyTo([40.7182, -74.0028], 17, {{ duration: 1.5 }});
      setBmapTileLayer('satellite');
      if (labelEl) labelEl.textContent = 'MANHATTAN 400 BROADWAY / 3RD AVE FDIC CLUSTER';
      if (countBadge) countBadge.textContent = '5 Commercial Vaults In Scope';
      setTimeout(function() {{
        showManhattanBranchPopup(manhattanBranches[0]);
      }}, 1600);

    }} else if (presetKey === 'frankfurt') {{
      leafletMap.flyTo([50.110, 8.672], 17, {{ duration: 1.5 }});
      setBmapTileLayer('satellite');
      if (labelEl) labelEl.textContent = 'FRANKFURT EUROPEAN CENTRAL BANK & DEUTSCHE BÖRSE';
      if (countBadge) countBadge.textContent = 'Eurozone Monetary Anchor';

    }} else if (presetKey === 'escondida') {{
      leafletMap.flyTo([-24.269, -69.071], 15, {{ duration: 1.5 }});
      setBmapTileLayer('satellite');
      if (labelEl) labelEl.textContent = 'MINERA ESCONDIDA MEGA COPPER MINE (CHILE ATACAMA — 1.1M TONS/YR)';
      if (countBadge) countBadge.textContent = "World's Largest Copper Producing Pit";

    }} else if (presetKey === 'ashburn') {{
      leafletMap.flyTo([39.043, -77.487], 16, {{ duration: 1.5 }});
      setBmapTileLayer('satellite');
      if (labelEl) labelEl.textContent = 'ASHBURN DATA CENTER ALLEY (LOUDOUN COUNTY VA — 3,000+ MW)';
      if (countBadge) countBadge.textContent = 'Global Hyperscale Internet Backbone';

    }} else if (presetKey === 'houston') {{
      leafletMap.flyTo([29.740, -95.120], 16, {{ duration: 1.5 }});
      setBmapTileLayer('satellite');
      if (labelEl) labelEl.textContent = 'HOUSTON SHIP CHANNEL & DEER PARK REACH (IMAGE 1)';
      if (countBadge) countBadge.textContent = 'North American Petrochemical Port';

    }} else if (presetKey === 'crude_pipelines') {{
      leafletMap.flyTo([30.0, 10.0], 2.5, {{ duration: 1.2 }});
      setBmapTileLayer('dark');
      if (!activeLayers['crude_pipelines']) window.toggleBmapDataset('crude_pipelines');
      var cardPipe = document.getElementById('bmap_pipelines_filter_card');
      if (cardPipe) cardPipe.style.display = 'block';
      if (labelEl) labelEl.textContent = 'GLOBAL CRUDE OIL PIPELINES & TRANSIT ARTERIES';
      if (countBadge) countBadge.textContent = '15 Major Arteries Active';

    }} else if (presetKey === 'bank_branches') {{
      leafletMap.flyTo([38.5, -96.5], 5, {{ duration: 1.2 }});
      setBmapTileLayer('dark');
      if (!activeLayers['bank_branches']) window.toggleBmapDataset('bank_branches');
      if (labelEl) labelEl.textContent = 'US BANK BRANCHES (FDIC GEOSPATIAL CLUSTERS)';
      if (countBadge) countBadge.textContent = '1,675 FDIC Branches Active';

    }} else if (presetKey === 'greg_mortimer') {{
      leafletMap.flyTo([gregMortimer.lat, gregMortimer.lon], 9, {{ duration: 1.5 }});
      setBmapTileLayer('satellite');
      var pop = document.getElementById('bmap_greg_mortimer_popup');
      if (pop) pop.style.display = 'block';
      if (labelEl) labelEl.textContent = 'VOYAGE VECTOR: GREG MORTIMER (ANTARCTIC PENINSULA)';
      if (countBadge) countBadge.textContent = 'AIS Live Stream Active';

    }} else if (presetKey === 'world') {{
      leafletMap.flyTo([25.0, 10.0], 2.5, {{ duration: 1.2 }});
      setBmapTileLayer('dark');
      if (labelEl) labelEl.textContent = 'GLOBAL MARITIME, PIPELINE & MULTI-ASSET RADAR';
      if (countBadge) countBadge.textContent = '2,500+ Worldwide Assets In Scope';
    }}
  }};

  // ═══════════════════════════════════════════════════════════════
  // ── AUTHENTIC RIGHT-HAND DATASETS DRAWER (IMAGE 2 & 4 REPLICA) ──
  // ═══════════════════════════════════════════════════════════════
  var suggestedDatasetsConfig = [
    {{ key: 'bank_branches', label: 'Bank Branches (US)', count: '1,675', active: true, color: '#38bdf8' }},
    {{ key: 'cyclones', label: 'Cyclones', count: '2', active: false, color: '#ef4444' }},
    {{ key: 'earthquakes', label: 'Earthquakes', count: '3', active: false, color: '#f87171' }},
    {{ key: 'power_plants', label: 'Power Plants', count: '40', active: true, color: '#f59e0b' }},
    {{ key: 'refineries', label: 'Refineries', count: '21', active: true, color: '#ef4444' }},
    {{ key: 'lng_terminals', label: 'LNG Terminals', count: '15', active: true, color: '#06b6d4' }},
    {{ key: 'seaports', label: 'Seaports', count: '13', active: true, color: '#10b981' }},
    {{ key: 'crude_pipelines', label: 'Natural Gas Pipelines (N.Am. & Global)', count: '15', active: true, color: '#3b82f6' }},
    {{ key: 'gas_hubs', label: 'Natural Gas Hubs', count: '5', active: false, color: '#fb923c' }},
    {{ key: 'storage_terminals', label: 'Storage Terminals', count: '6', active: false, color: '#60a5fa' }},
    {{ key: 'fertilizers', label: 'Fertilizer Manufacturers', count: '6', active: false, color: '#84cc16' }},
    {{ key: 'vessels', label: 'Vessels (Live AIS Fleet)', count: '60', active: true, color: '#00e5ff' }},
    {{ key: 'weather_stations', label: 'Weather Stations (WFOR)', count: '6', active: false, color: '#38bdf8' }},
    {{ key: 'world_equity', label: 'World Equity Markets', count: '30', active: false, color: '#22c55e' }}
  ];

  var newDatasetsConfig = [
    {{ key: 'dense_grid', label: 'Dense Global Constellation (Image 3)', count: '2,325', active: false, color: '#facc15' }},
    {{ key: 'semiconductor_fabs', label: 'Semiconductor Fabs & Silicon', count: '11', active: true, color: '#a855f7' }},
    {{ key: 'data_centers', label: 'Data Centers & Hyperscalers', count: '7', active: true, color: '#22c55e' }},
    {{ key: 'financial_centers', label: 'Financial Centers & Exchanges', count: '12', active: true, color: '#eab308' }},
    {{ key: 'mining_hubs', label: 'Critical Mining Hubs', count: '7', active: true, color: '#f97316' }}
  ];

  function renderDatasetSidebar() {{
    var suggCont = document.getElementById('suggested_datasets_list');
    var newCont = document.getElementById('new_datasets_list');

    if (suggCont) {{
      suggCont.innerHTML = '';
      suggestedDatasetsConfig.forEach(function(ds) {{
        suggCont.appendChild(createDatasetRow(ds));
      }});
    }}

    if (newCont) {{
      newCont.innerHTML = '';
      newDatasetsConfig.forEach(function(ds) {{
        newCont.appendChild(createDatasetRow(ds));
      }});
    }}

    updateActiveDatasetsCountPill();
  }}

  function createDatasetRow(ds) {{
    var row = document.createElement('div');
    row.id = 'ds_row_' + ds.key;
    row.style.display = 'flex';
    row.style.alignItems = 'center';
    row.style.justifyContent = 'space-between';
    row.style.padding = '3px 6px';
    row.style.borderRadius = '3px';
    row.style.cursor = 'pointer';
    row.style.fontSize = '9.5px';
    row.style.background = activeLayers[ds.key] ? '#132032' : 'transparent';
    row.style.color = activeLayers[ds.key] ? '#fff' : '#94a3b8';
    row.style.border = activeLayers[ds.key] ? '1px solid #1e3a5f' : '1px solid transparent';

    row.onclick = function() {{
      window.toggleBmapDataset(ds.key);
    }};

    var leftWrap = document.createElement('div');
    leftWrap.style.display = 'flex';
    leftWrap.style.alignItems = 'center';
    leftWrap.style.gap = '6px';

    var chk = document.createElement('span');
    chk.style.color = activeLayers[ds.key] ? '#00e5ff' : '#475569';
    chk.style.fontWeight = '900';
    chk.textContent = activeLayers[ds.key] ? '☑' : '☐';
    leftWrap.appendChild(chk);

    var lbl = document.createElement('span');
    lbl.textContent = ds.label;
    leftWrap.appendChild(lbl);

    var countBadge = document.createElement('span');
    countBadge.style.color = ds.color || '#ffaa00';
    countBadge.style.fontSize = '8.5px';
    countBadge.style.fontWeight = '700';
    countBadge.textContent = ds.count;

    row.appendChild(leftWrap);
    row.appendChild(countBadge);
    return row;
  }}

  window.toggleBmapDataset = function(key) {{
    activeLayers[key] = !activeLayers[key];
    var grp = datasetLayerGroups[key];

    if (leafletMap && grp) {{
      if (activeLayers[key]) {{
        grp.addTo(leafletMap);
      }} else {{
        leafletMap.removeLayer(grp);
      }}
    }}

    // Update styling in sidebar
    var row = document.getElementById('ds_row_' + key);
    if (row) {{
      row.style.background = activeLayers[key] ? '#132032' : 'transparent';
      row.style.color = activeLayers[key] ? '#fff' : '#94a3b8';
      row.style.border = activeLayers[key] ? '1px solid #1e3a5f' : '1px solid transparent';
      var chk = row.querySelector('span');
      if (chk) {{
        chk.style.color = activeLayers[key] ? '#00e5ff' : '#475569';
        chk.textContent = activeLayers[key] ? '☑' : '☐';
      }}
    }}

    updateActiveDatasetsCountPill();
  }};

  function updateActiveDatasetsCountPill() {{
    var activeCount = Object.values(activeLayers).filter(Boolean).length;
    var pill = document.getElementById('active_dataset_count_pill');
    if (pill) pill.textContent = activeCount + ' Active';
  }}

  window.toggleMapContentDrawer = function() {{
    var drawer = document.getElementById('bmap_map_content_drawer');
    var openBtn = document.getElementById('btn_open_drawer_pill');
    if (!drawer) return;

    if (drawer.style.transform === 'translateX(100%)' || drawer.style.display === 'none') {{
      drawer.style.display = 'flex';
      drawer.style.transform = 'translateX(0)';
      if (openBtn) openBtn.style.display = 'none';
    }} else {{
      drawer.style.transform = 'translateX(100%)';
      setTimeout(function() {{ drawer.style.display = 'none'; }}, 250);
      if (openBtn) openBtn.style.display = 'block';
    }}
  }};

  window.filterDatasetSidebar = function(q) {{
    var query = q.toLowerCase();
    var allRows = document.querySelectorAll('[id^="ds_row_"]');
    allRows.forEach(function(r) {{
      r.style.display = r.textContent.toLowerCase().indexOf(query) >= 0 ? 'flex' : 'none';
    }});
  }};

  // ═══════════════════════════════════════════════════════════════
  // ── SECONDARY VIEWS CONTROLLER (TABLE, CHART, NEWS, SPLC, FXC, VOL) ──
  // ═══════════════════════════════════════════════════════════════
  window.switchBmapView = function(viewId) {{
    currentActiveView = viewId;
    ['map', 'table', 'chart', 'news', 'splc', 'fxc', 'vol'].forEach(function(v) {{
      var cont = document.getElementById('bmap_view_container_' + v);
      var btn = document.getElementById('bmap_btn_view_' + v);
      if (cont) cont.style.display = (v === viewId) ? 'block' : 'none';
      if (btn) {{
        btn.style.background = (v === viewId) ? '#1e3a5f' : '#0d1624';
        btn.style.color = (v === viewId) ? '#00e5ff' : '#94a3b8';
        btn.style.borderBottom = (v === viewId) ? '2px solid #00e5ff' : '1px solid #1c2e44';
      }}
    }});

    if (viewId === 'map' && leafletMap) {{
      setTimeout(function() {{ leafletMap.invalidateSize(); }}, 100);
    }} else if (viewId === 'splc') {{
      setTimeout(function() {{ renderSplcNetwork(activeSplcTicker); }}, 100);
    }} else if (viewId === 'vol') {{
      setTimeout(function() {{ drawVolSurface(); }}, 100);
    }}
  }};

  // Table Renderer
  window.renderBmapTableData = function(type) {{
    var headTr = document.getElementById('bmap_tbl_head_tr');
    var tbody = document.getElementById('bmap_tbl_body');
    var bBerths = document.getElementById('btn_tbl_berths');
    var bBranches = document.getElementById('btn_tbl_branches');

    if (!headTr || !tbody) return;
    tbody.innerHTML = '';

    if (type === 'berths') {{
      if (bBerths) bBerths.classList.add('active');
      if (bBranches) bBranches.classList.remove('active');

      headTr.innerHTML = '<th>TERMINAL / BERTH</th><th>COUNTRY</th><th>IMO</th><th>VESSEL</th><th>TYPE</th><th>DWT</th><th>LAST SEEN</th>';
      berthVisits.forEach(function(b) {{
        var tr = document.createElement('tr');
        tr.innerHTML = '<td><strong style="color:#00e5ff;">' + b.berth + '</strong></td>' +
          '<td>' + b.country + '</td>' +
          '<td>' + b.imo + '</td>' +
          '<td style="color:#ffaa00;">' + b.vessel + '</td>' +
          '<td>' + b.type + '</td>' +
          '<td>' + b.dwt.toLocaleString() + ' MT</td>' +
          '<td style="color:#00e676;">' + b.last_seen + '</td>';
        tbody.appendChild(tr);
      }});
    }} else {{
      if (bBerths) bBerths.classList.remove('active');
      if (bBranches) bBranches.classList.add('active');

      headTr.innerHTML = '<th>BRANCH</th><th>COMPANY</th><th>STATE</th><th>TYPE</th><th>DEPOSITS</th>';
      usBankBranches.slice(0, 30).forEach(function(b) {{
        var tr = document.createElement('tr');
        tr.innerHTML = '<td><strong style="color:#38bdf8;">' + b.branch + '</strong></td>' +
          '<td>' + b.name + '</td>' +
          '<td>' + b.state + '</td>' +
          '<td>' + b.type + '</td>' +
          '<td style="color:#00e676;">$' + b.dep.toLocaleString() + 'M</td>';
        tbody.appendChild(tr);
      }});
    }}
  }};

  // READ News Stories Renderer
  function renderReadNewsStories() {{
    var cont = document.getElementById('bmap_news_stories_container');
    if (!cont) return;
    cont.innerHTML = '';

    readNewsStories.forEach(function(item) {{
      var row = document.createElement('div');
      row.style.display = 'flex';
      row.style.justifyContent = 'space-between';
      row.style.alignItems = 'center';
      row.style.padding = '8px 12px';
      row.style.background = '#0a101d';
      row.style.border = '1px solid #142338';
      row.style.borderRadius = '3px';
      row.style.cursor = 'pointer';

      row.innerHTML = '<div style="display:flex;align-items:center;gap:10px;">' +
        '<span style="color:#ffaa00;font-weight:800;font-size:10.5px;">' + item.time + '</span>' +
        '<span style="background:#16253b;color:#38bdf8;padding:1px 5px;border-radius:2px;font-size:9px;">' + item.source + '</span>' +
        '<strong style="color:#e2e8f0;font-size:11px;">' + item.headline + '</strong>' +
        '</div>' +
        '<span style="color:#00e676;font-size:9.5px;font-weight:700;">' + item.read_count + ' READS</span>';
      cont.appendChild(row);
    }});
  }}

  // SPLC Supply Chain Renderer
  window.renderSplcNetwork = function(ticker) {{
    activeSplcTicker = ticker;
    var data = splcNetworks[ticker] || splcNetworks['AAPL'];
    var supList = document.getElementById('splc_suppliers_list');
    var custList = document.getElementById('splc_customers_list');

    if (supList) {{
      supList.innerHTML = '';
      data.suppliers.forEach(function(s) {{
        var d = document.createElement('div');
        d.style.padding = '6px';
        d.style.background = '#0d1626';
        d.style.borderRadius = '3px';
        d.style.border = '1px solid #1c2e44';
        d.innerHTML = '<strong style="color:#38bdf8;font-size:10px;">' + s.name + '</strong><br>' +
          '<span style="color:#94a3b8;font-size:9px;">' + s.role + ' · Cost: </span><span style="color:#00e676;font-size:9px;">' + s.pct + '</span>';
        supList.appendChild(d);
      }});
    }}

    if (custList) {{
      custList.innerHTML = '';
      data.customers.forEach(function(c) {{
        var d = document.createElement('div');
        d.style.padding = '6px';
        d.style.background = '#0d1626';
        d.style.borderRadius = '3px';
        d.style.border = '1px solid #1c2e44';
        d.innerHTML = '<strong style="color:#34d399;font-size:10px;">' + c.name + '</strong><br>' +
          '<span style="color:#94a3b8;font-size:9px;">' + c.role + ' · Rev: </span><span style="color:#ffaa00;font-size:9px;">' + c.pct + '</span>';
        custList.appendChild(d);
      }});
    }}

    drawSplcNetworkCanvas(data);
  }};

  function drawSplcNetworkCanvas(data) {{
    var canvas = document.getElementById('splcNetworkCanvas');
    if (!canvas) return;
    var ctx = canvas.getContext('2d');
    var w = canvas.width = canvas.parentElement.clientWidth;
    var h = canvas.height = canvas.parentElement.clientHeight || 550;

    ctx.clearRect(0, 0, w, h);

    // Center Node
    var cx = w / 2;
    var cy = h / 2;
    ctx.beginPath();
    ctx.arc(cx, cy, 38, 0, Math.PI * 2);
    ctx.fillStyle = '#1e3a5f';
    ctx.fill();
    ctx.lineWidth = 2.5;
    ctx.strokeStyle = '#00e5ff';
    ctx.stroke();

    ctx.fillStyle = '#fff';
    ctx.font = 'bold 12px monospace';
    ctx.textAlign = 'center';
    ctx.fillText(activeSplcTicker, cx, cy - 4);
    ctx.font = '9px monospace';
    ctx.fillStyle = '#94a3b8';
    ctx.fillText('CORE TICKER', cx, cy + 12);

    // Suppliers (Left)
    var numSup = data.suppliers.length;
    data.suppliers.forEach(function(s, idx) {{
      var sy = (h / (numSup + 1)) * (idx + 1);
      var sx = 60;

      // Connecting bezier curve
      ctx.beginPath();
      ctx.moveTo(sx, sy);
      ctx.bezierCurveTo(sx + 100, sy, cx - 100, cy, cx, cy);
      ctx.strokeStyle = 'rgba(56, 189, 248, 0.45)';
      ctx.lineWidth = 1.8;
      ctx.stroke();

      // Node
      ctx.beginPath();
      ctx.arc(sx, sy, 18, 0, Math.PI * 2);
      ctx.fillStyle = '#0a1626';
      ctx.fill();
      ctx.strokeStyle = '#38bdf8';
      ctx.stroke();

      ctx.fillStyle = '#38bdf8';
      ctx.font = 'bold 9px monospace';
      ctx.fillText(s.name.split(' ')[0], sx, sy + 3);
    }});

    // Customers (Right)
    var numCust = data.customers.length;
    data.customers.forEach(function(c, idx) {{
      var cyy = (h / (numCust + 1)) * (idx + 1);
      var cxRight = w - 60;

      ctx.beginPath();
      ctx.moveTo(cx, cy);
      ctx.bezierCurveTo(cx + 100, cy, cxRight - 100, cyy, cxRight, cyy);
      ctx.strokeStyle = 'rgba(52, 211, 153, 0.45)';
      ctx.lineWidth = 1.8;
      ctx.stroke();

      ctx.beginPath();
      ctx.arc(cxRight, cyy, 18, 0, Math.PI * 2);
      ctx.fillStyle = '#091c18';
      ctx.fill();
      ctx.strokeStyle = '#34d399';
      ctx.stroke();

      ctx.fillStyle = '#34d399';
      ctx.font = 'bold 9px monospace';
      ctx.fillText(c.name.split(' ')[0], cxRight, cyy + 3);
    }});
  }}

  // FXC Currency Rates Matrix Renderer
  function renderFxcMatrix() {{
    var tbody = document.getElementById('bmap_fxc_tbody');
    if (!tbody) return;
    tbody.innerHTML = '';

    fxcData.pairs.forEach(function(p) {{
      var tr = document.createElement('tr');
      var chgColor = p.pct_chg >= 0 ? '#00e676' : '#ef4444';
      tr.innerHTML = '<td style="font-size:14px;">' + p.flag + '</td>' +
        '<td><strong style="color:#ffaa00;">' + p.pair + '</strong></td>' +
        '<td>' + p.name + '</td>' +
        '<td style="font-weight:700;color:#fff;">' + p.spot.toFixed(4) + '</td>' +
        '<td style="color:' + chgColor + ';">' + (p.net_chg >= 0 ? '+' : '') + p.net_chg.toFixed(4) + '</td>' +
        '<td style="font-weight:700;color:' + chgColor + ';">' + (p.pct_chg >= 0 ? '+' : '') + p.pct_chg.toFixed(2) + '%</td>' +
        '<td>' + p.fwd_1m.toFixed(4) + '</td>' +
        '<td>' + p.fwd_3m.toFixed(4) + '</td>' +
        '<td>' + p.fwd_12m.toFixed(4) + '</td>' +
        '<td style="color:#94a3b8;font-size:9px;">' + p.range_52w + '</td>';
      tbody.appendChild(tr);
    }});
  }}

  // GPC Candlestick Chart
  function initGpcCandlestickChart() {{
    var canvas = document.getElementById('bmap_gpc_chart_canvas');
    if (!canvas || typeof Chart === 'undefined') return;

    var days = 40;
    var labels = [];
    var closePrices = [];
    var base = 390;

    for (var i = 0; i < days; i++) {{
      labels.push('Day ' + (i + 1));
      base += (Math.random() - 0.48) * 3;
      closePrices.push(parseFloat(base.toFixed(2)));
    }}

    new Chart(canvas, {{
      type: 'line',
      data: {{
        labels: labels,
        datasets: [{{
          label: 'SPY US Equity Daily Close',
          data: closePrices,
          borderColor: '#00e5ff',
          backgroundColor: 'rgba(0, 229, 255, 0.08)',
          borderWidth: 2,
          fill: true,
          tension: 0.1,
          pointRadius: 2,
          pointBackgroundColor: '#ffaa00'
        }}]
      }},
      options: {{
        responsive: true,
        maintainAspectRatio: false,
        plugins: {{
          legend: {{ labels: {{ color: '#cbd5e1', font: {{ family: 'monospace' }} }} }}
        }},
        scales: {{
          x: {{ grid: {{ color: '#162438' }}, ticks: {{ color: '#94a3b8', font: {{ family: 'monospace' }} }} }},
          y: {{ grid: {{ color: '#162438' }}, ticks: {{ color: '#94a3b8', font: {{ family: 'monospace' }} }} }}
        }}
      }}
    }});
  }}

  // VOL 3D Implied Volatility Surface Canvas
  function initVolSurfaceCanvas() {{
    drawVolSurface();
  }}

  window.rotateVolSurface = function(deg) {{
    currentVolRot = (currentVolRot + deg) % 360;
    drawVolSurface();
  }};

  function drawVolSurface() {{
    var canvas = document.getElementById('bmapVolCanvas');
    if (!canvas) return;
    var ctx = canvas.getContext('2d');
    var w = canvas.width = canvas.parentElement.clientWidth;
    var h = canvas.height = canvas.parentElement.clientHeight || 550;

    ctx.clearRect(0, 0, w, h);

    var cx = w / 2;
    var cy = h / 2 + 40;
    var rad = currentVolRot * Math.PI / 180;

    // Isometric Wireframe Mesh
    var rows = 18;
    var cols = 18;
    var scale = Math.min(w, h) / 36;

    for (var i = -rows/2; i < rows/2; i++) {{
      ctx.beginPath();
      for (var j = -cols/2; j < cols/2; j++) {{
        var dist = Math.sqrt(i * i + j * j);
        var z = Math.sin(dist * 0.4) * 8 + Math.exp(-dist * 0.15) * 12;
        
        var rx = i * Math.cos(rad) - j * Math.sin(rad);
        var ry = i * Math.sin(rad) + j * Math.cos(rad);

        var px = cx + rx * scale * 1.5;
        var py = cy + (ry * scale * 0.8) - (z * scale * 0.6);

        if (j === -cols/2) ctx.moveTo(px, py);
        else ctx.lineTo(px, py);
      }}
      ctx.strokeStyle = 'rgba(0, 229, 255, 0.4)';
      ctx.lineWidth = 1;
      ctx.stroke();
    }}

    ctx.fillStyle = '#ffaa00';
    ctx.font = 'bold 12px monospace';
    ctx.textAlign = 'left';
    ctx.fillText('TSLA US 3D IMPLIED VOL SURFACE (MONEYNESS × MATURITY)', 20, 30);
    ctx.fillStyle = '#94a3b8';
    ctx.font = '10px monospace';
    ctx.fillText('Rotation Angle: ' + currentVolRot + '° · Mesh Points: ' + (rows * cols), 20, 48);
  }}

  // Global Exports & Tool Action Handlers
  window.handleBmapSearch = function(e) {{
    if (e.key === 'Enter') {{
      var q = e.target.value.trim().toUpperCase();
      if (!q) return;

      if (q === 'HORMUZ') jumpToBmapPreset('hormuz');
      else if (q === 'DENSE' || q === 'DATA') jumpToBmapPreset('dense_grid');
      else if (q === 'JAMNAGAR') jumpToBmapPreset('jamnagar');
      else if (q === 'TSMC' || q === 'FAB') jumpToBmapPreset('tsmc_fab18');
      else if (q === 'THREE GORGES') jumpToBmapPreset('three_gorges');
      else if (q === 'RAS LAFFAN') jumpToBmapPreset('ras_laffan');
      else if (q === 'MANHATTAN') jumpToBmapPreset('manhattan');
      else if (q === 'FRANKFURT' || q === 'ECB') jumpToBmapPreset('frankfurt');
      else if (q === 'ASHBURN') jumpToBmapPreset('ashburn');
      else if (q === 'ESCONDIDA') jumpToBmapPreset('escondida');
      else if (q === 'HOUSTON') jumpToBmapPreset('houston');
      else {{
        var matchedVsl = globalVessels.find(function(v) {{ return v.name.toUpperCase().indexOf(q) >= 0; }});
        if (matchedVsl) {{
          selectActiveVessel(matchedVsl);
          leafletMap.flyTo([matchedVsl.lat, matchedVsl.lon], 12, {{ duration: 1.2 }});
        }} else {{
          alert('Bloomberg BMAP Security / Asset Searched: ' + q + '\\nZooming to matching coordinates or related dataset.');
        }}
      }}
    }}
  }};

  window.toggleActionsDropdown = function() {{
    var d = document.getElementById('bmap_actions_dropdown');
    if (d) d.style.display = (d.style.display === 'none' || !d.style.display) ? 'block' : 'none';
  }};

  window.exportBmapGeoJSON = function() {{
    alert('Exporting visible layers to WGS84 GeoJSON format...');
  }};

  window.exportBmapCSV = function() {{
    alert('Exporting active institutional assets to CSV report...');
  }};

  window.setProximityAlertModal = function() {{
    alert('CPA Alert set: Warning triggered when AIS vessel approaches within 2.0 NM.');
  }};

  window.resetBmapAllFilters = function() {{
    resetBankFilter();
    jumpToBmapPreset('world');
  }};

  window.toggleDistanceMeasurement = function() {{
    alert('Nautical Measurement Tool activated. Click two points on map to measure nautical miles.');
  }};

  window.switchBmapTicker = function(ticker) {{
    var symEl = document.getElementById('bb_sym');
    var selectEl = document.getElementById('bb_active_ticker_select');
    if (symEl) symEl.textContent = ticker + ' US $';
    if (selectEl) selectEl.value = ticker;
    renderSplcNetwork(ticker);
  }};

  // ═══════════════════════════════════════════════════════════════
  // ── AUTO-INITIALIZATION ──
  // ═══════════════════════════════════════════════════════════════
  if (document.readyState === 'loading') {{
    document.addEventListener('DOMContentLoaded', initLeafletBmap);
  }} else {{
    initLeafletBmap();
  }}

}})();
</script>"""

    with open(os.path.join(BASE_DIR, "bmap_js_template.js"), "w", encoding="utf-8") as f:
        f.write(js_code)
    print(f"Generated bmap_js_template.js ({len(js_code)} bytes)")

if __name__ == "__main__":
    generate_js()
