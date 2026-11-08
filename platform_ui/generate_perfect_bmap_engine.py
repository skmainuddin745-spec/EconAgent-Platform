# F:\documents\SOIC\EconAgent_Platform\platform_ui\generate_perfect_bmap_engine.py
"""
generate_perfect_bmap_engine.py
Builds the complete bmap_js_template.js with:
1. All JSON dataset injections.
2. Atmospheric Weather Canvas Heatmap Engine (Cloud Cover & Temperature).
3. World Equity Markets choropleth & interactive hover cards.
4. Bloomberg "Map Content" docked sidebar manager with:
   - Dynamic Active Dataset Control Cards (Weather, World Equity, Vessels, Bank Branches, Pipelines, Gas)
   - Collapsible Suggested Datasets list (24 datasets with [+] buttons)
   - Collapsible New Datasets list (12 datasets with [+] buttons)
   - View All Datasets modal dialog
5. Dynamic Floating Legends Manager (Cloud Cover, Temperature, Equity, FDIC Banks, Pipelines, Vessels).
6. Live AIS Kinematics & Greg Mortimer Trajectory Vector.
7. Sub-meter Satellite LOD & Manhattan FDIC Branch Popups.
8. All 6 Secondary Views (Table, Chart, News, SPLC, FXC, VOL).
"""

import os
import sys
import json

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
import global_assets_data as gad


MUNICIPAL_BONDS = [
    { 'name': 'New York Metropolitan Transportation Authority (MTA)', 'country': 'US (New York)', 'state': 'NY', 'lat': 40.7505, 'lon': -73.9760, 'yield': '4.12%', 'rating': 'AA-', 'volume': '$1.45B', 'capacity': '$1.45B Bond Issue', 'type': 'Transit Revenue Bond' },
    { 'name': 'Port Authority of New York & New Jersey', 'country': 'US (NY/NJ)', 'state': 'NY/NJ', 'lat': 40.7118, 'lon': -74.0131, 'yield': '3.98%', 'rating': 'Aa3', 'volume': '$980M', 'capacity': '$980M Port Facility Bond', 'type': 'Port & Airport Facilities' },
    { 'name': 'California State General Obligation (Water Resources)', 'country': 'US (California)', 'state': 'CA', 'lat': 38.5816, 'lon': -121.4944, 'yield': '3.85%', 'rating': 'Aa2', 'volume': '$2.10B', 'capacity': '$2.10B Water Infrastructure', 'type': 'State Infrastructure Bond' },
    { 'name': 'Texas Transportation Commission (State Highway Fund)', 'country': 'US (Texas)', 'state': 'TX', 'lat': 30.2672, 'lon': -97.7431, 'yield': '3.76%', 'rating': 'AAA', 'volume': '$1.75B', 'capacity': '$1.75B Highway Trust Fund', 'type': 'Highway Revenue Bond' },
    { 'name': 'Port of Houston Authority (Harris County)', 'country': 'US (Texas)', 'state': 'TX', 'lat': 29.7604, 'lon': -95.3698, 'yield': '4.05%', 'rating': 'AA+', 'volume': '$620M', 'capacity': '$620M Marine Terminal Bond', 'type': 'Maritime Port Expansion' },
    { 'name': 'Chicago O\'Hare International Airport Senior Lien', 'country': 'US (Illinois)', 'state': 'IL', 'lat': 41.9742, 'lon': -87.9073, 'yield': '4.35%', 'rating': 'A+', 'volume': '$840M', 'capacity': '$840M Airport Modernization', 'type': 'Airport Enterprise Bond' },
    { 'name': 'Los Angeles Department of Water & Power (LADWP)', 'country': 'US (California)', 'state': 'CA', 'lat': 34.0522, 'lon': -118.2437, 'yield': '3.92%', 'rating': 'Aa2', 'volume': '$1.15B', 'capacity': '$1.15B Power Grid Bond', 'type': 'Electric Plant Revenue' },
    { 'name': 'Florida Department of Transportation (Turnpike System)', 'country': 'US (Florida)', 'state': 'FL', 'lat': 28.5383, 'lon': -81.3792, 'yield': '3.88%', 'rating': 'AA', 'volume': '$730M', 'capacity': '$730M Turnpike Revenue', 'type': 'Toll Revenue Bond' }
]

CROP_YIELDS = [
    { 'name': 'Iowa Central Corn Belt Hub (Story County)', 'country': 'US (Iowa)', 'lat': 42.0308, 'lon': -93.6319, 'crop': 'Corn (Maize)', 'yieldForecast': '208 bu/acre', 'capacity': '208 bu/acre (+5.4%)', 'type': 'Grain Production Index', 'condition': '82% Good/Excellent' },
    { 'name': 'Illinois Prairie Soybean Corridor (Champaign County)', 'country': 'US (Illinois)', 'lat': 40.1164, 'lon': -88.2434, 'crop': 'Soybeans', 'yieldForecast': '64 bu/acre', 'capacity': '64 bu/acre (+3.8%)', 'type': 'Soybean Harvest Estimate', 'condition': '79% Good/Excellent' },
    { 'name': 'Kansas Winter Wheat Heartland (Saline County)', 'country': 'US (Kansas)', 'lat': 38.8403, 'lon': -97.6114, 'crop': 'Hard Red Winter Wheat', 'yieldForecast': '52 bu/acre', 'capacity': '52 bu/acre (-2.1%)', 'type': 'Winter Wheat Yield', 'condition': '65% Fair/Good' },
    { 'name': 'Nebraska Irrigated Corn Basin (Platte River)', 'country': 'US (Nebraska)', 'lat': 41.2565, 'lon': -95.9345, 'crop': 'Irrigated Corn', 'yieldForecast': '215 bu/acre', 'capacity': '215 bu/acre (+6.2%)', 'type': 'Irrigated Corn Yield', 'condition': '86% Good/Excellent' },
    { 'name': 'North Dakota Spring Wheat Belt (Cass County)', 'country': 'US (North Dakota)', 'lat': 46.8772, 'lon': -96.7898, 'crop': 'Hard Red Spring Wheat', 'yieldForecast': '58 bu/acre', 'capacity': '58 bu/acre (+4.1%)', 'type': 'Spring Wheat Yield', 'condition': '75% Good/Excellent' },
    { 'name': 'Minnesota Corn & Sugarbeet Plains (Renville County)', 'country': 'US (Minnesota)', 'lat': 44.7836, 'lon': -94.9747, 'crop': 'Corn & Sugarbeets', 'yieldForecast': '196 bu/acre', 'capacity': '196 bu/acre (+2.9%)', 'type': 'Corn/Sugarbeet Index', 'condition': '78% Good/Excellent' }
]

def generate_js_template():
    code = []
    code.append("<script>\n(function() {\n")
    code.append("  // ═══════════════════════════════════════════════════════════════\n")
    code.append("  // ── DATA INJECTIONS FROM BLOOMBERG MAP DATASETS ──\n")
    code.append("  // ═══════════════════════════════════════════════════════════════\n")
    code.append("  var banksLookup = __BANKS_JSON__;\n")
    code.append("  var statesLookup = __STATES_JSON__;\n")
    code.append("  var typesLookup = __TYPES_JSON__;\n")
    code.append("  var branchesCompact = __BRANCHES_JSON__;\n\n")

    code.append(f"  var crudePipelines = {json.dumps(CRUDE_PIPELINES)};\n")
    code.append(f"  var gasPipelines = {json.dumps(GAS_PIPELINES_NAM)};\n")
    code.append(f"  var berthVisits = {json.dumps(BERTH_VISITS)};\n")
    code.append(f"  var manhattanBranches = {json.dumps(MANHATTAN_STREET_BRANCHES)};\n")
    code.append(f"  var gregMortimer = {json.dumps(GREG_MORTIMER)};\n")
    code.append(f"  var worldEquityData = {json.dumps(WORLD_EQUITY_DATA)};\n")
    code.append(f"  var splcNetworks = {json.dumps(SPLC_NETWORKS)};\n")
    code.append(f"  var fxcData = {json.dumps(FXC_DATA)};\n")
    code.append(f"  var readNewsStories = {json.dumps(READ_NEWS_STORIES)};\n\n")

    code.append(f"  var globalVessels = {json.dumps(gad.GLOBAL_AIS_VESSELS)};\n")
    code.append(f"  var globalUtilities = {json.dumps(gad.GLOBAL_UTILITIES)};\n")
    code.append(f"  var globalRefineries = {json.dumps(gad.GLOBAL_REFINERIES)};\n")
    code.append(f"  var globalLng = {json.dumps(gad.GLOBAL_LNG_TERMINALS)};\n")
    code.append(f"  var globalSeaports = {json.dumps(gad.GLOBAL_SEAPORTS)};\n")
    code.append(f"  var globalSemiconductors = {json.dumps(gad.GLOBAL_SEMICONDUCTOR_FABS)};\n")
    code.append(f"  var globalDataCenters = {json.dumps(gad.GLOBAL_DATA_CENTERS)};\n")
    code.append(f"  var globalMunicipalBonds = {json.dumps(MUNICIPAL_BONDS)};\n")
    code.append(f"  var globalCropYields = {json.dumps(CROP_YIELDS)};\n")
    code.append(f"  var globalFinancialCenters = {json.dumps(gad.GLOBAL_FINANCIAL_CENTERS)};\n")
    code.append(f"  var globalMining = {json.dumps(gad.GLOBAL_MINING_HUBS)};\n")
    code.append(f"  var globalFertilizers = {json.dumps(gad.GLOBAL_FERTILIZER_PLANTS)};\n")
    code.append(f"  var globalStorage = {json.dumps(gad.GLOBAL_STORAGE_TERMINALS)};\n")
    code.append(f"  var globalGasHubs = {json.dumps(gad.GLOBAL_NATURAL_GAS_HUBS)};\n")
    code.append(f"  var globalWeatherStations = {json.dumps(gad.GLOBAL_WEATHER_STATIONS)};\n")
    code.append(f"  var globalEarthquakes = {json.dumps(gad.GLOBAL_SEISMIC_EARTHQUAKES)};\n")
    code.append(f"  var globalCyclones = {json.dumps(gad.GLOBAL_CYCLONES)};\n")
    code.append(f"  var globalDenseGrid = {json.dumps(gad.GLOBAL_DENSE_GRID)};\n\n")

    # State variables
    code.append('''
  // ═══════════════════════════════════════════════════════════════
  // ── CORE APPLICATION STATE & CONFIGURATION ──
  // ═══════════════════════════════════════════════════════════════
  var leafletMap = null;
  var baseTileLayers = {};
  var currentTileKey = 'dark';
  var datasetLayerGroups = {};
  var vesselMarkersMap = {};
  var currentActiveView = 'map';
  var activeFollowVessel = null;
  var showArpaVectors = true;
  var activeSplcTicker = 'AAPL';
  var currentVolRot = 35;
  var liveKinematicsTimer = null;

  // Active layers state: matches authentic Bloomberg default constellation
  var activeLayers = {
    weather: true,
    world_equity: true,
    vessels: true,
    bank_branches: true,
    crude_pipelines: true,
    natural_gas: true,
    power_plants: true,
    refineries: true,
    lng_terminals: true,
    seaports: true,
    data_centers: false,
    semiconductor_fabs: false,
    financial_centers: false,
    mining_hubs: false,
    fertilizers: false,
    storage_terminals: false,
    gas_hubs: false,
    weather_stations: false,
    earthquakes: false,
    cyclones: false,
    dense_grid: false
  };

  // Weather active parameters (Screenshot 1 & 2)
  var weatherConfig = {
    type: 'cloud_cover', // 'cloud_cover' or 'temperature' or 'precipitation'
    stat: 'avg',
    day: 'today'
  };

  // Crude Pipelines active parameters (Screenshot 27)
  var crudePipelinesConfig = {
    lineWidth: 2,
    sizeBy: 'Diameter',
    colorBy: 'Uniform: Blue',
    labels: 'Off'
  };

  // Natural Gas active parameters (Screenshot 12)
  var naturalGasConfig = {
    pipelines: true,
    lng_berths: false,
    lng_terminals: false,
    storage_terminals: false,
    underground: false,
    chemical: false,
    hubs: false
  };

  // Bank branches active filter parameters (Screenshot 4)
  var bankFilterState = {
    name: 'ALL',
    branch: 'ALL',
    minDep: 0,
    state: 'ALL'
  };

  // Vessels active filter parameters (Screenshot 4 & 27)
  var vesselFilterState = {
    query: 'ALL',
    type: 'All',
    status: 'In Service/Commercial',
    dest: 'All',
    draftMin: 0,
    draftMax: 25,
    dwtMin: 0,
    dwtMax: 450000,
    lastSeen: '90 Days'
  };

  // Accordion collapsed state in Map Content
  var accordionOpen = {
    suggested: true,
    new: true,
    basemap: false
  };

  // ═══════════════════════════════════════════════════════════════
  // ── DATASET CATALOG CONFIGURATIONS (SCREENSHOTS 1, 2, 4, 12, 27) ──
  // ═══════════════════════════════════════════════════════════════
  var SUGGESTED_DATASETS = [
    { key: 'bank_branches', label: 'Bank Branches (US)', count: '1,675', color: '#ffaa00', category: 'FINANCIAL' },
    { key: 'climate', label: 'Climate', count: 'Global', color: '#38bdf8', category: 'CLIMATE' },
    { key: 'covid19', label: 'COVID-19', count: '190 Reg', color: '#f87171', category: 'FINANCIAL' },
    { key: 'cyclones', label: 'Cyclones', count: '2 Live', color: '#ef4444', category: 'CLIMATE' },
    { key: 'drought', label: 'Drought', count: '48 Zones', color: '#f59e0b', category: 'CLIMATE' },
    { key: 'earthquakes', label: 'Earthquakes', count: '5 Recent', color: '#f87171', category: 'CLIMATE' },
    { key: 'economic_data', label: 'Economic Data', count: 'Global', color: '#34d399', category: 'FINANCIAL' },
    { key: 'factories', label: 'Factories', count: '320 Plants', color: '#a78bfa', category: 'MARITIME' },
    { key: 'fertilizers', label: 'Fertilizer Manufacturers', count: '6 Plants', color: '#84cc16', category: 'COMMODITIES' },
    { key: 'fires', label: 'Fires', count: '14 Active', color: '#f97316', category: 'CLIMATE' },
    { key: 'lng_berths', label: 'LNG Berths', count: '18 Docks', color: '#06b6d4', category: 'COMMODITIES' },
    { key: 'lng_terminals', label: 'LNG Terminals', count: '15 Mega', color: '#06b6d4', category: 'COMMODITIES' },
    { key: 'mining_hubs', label: 'Metal Mines', count: '7 Tier-1', color: '#f97316', category: 'COMMODITIES' },
    { key: 'natural_gas', label: 'Natural Gas', count: '24 Arteries', color: '#00e5ff', category: 'COMMODITIES' },
    { key: 'gas_hubs', label: 'Natural Gas Hubs', count: '5 Physical', color: '#fb923c', category: 'COMMODITIES' },
    { key: 'crude_pipelines', label: 'Natural Gas Pipelines', count: '15 Trans', color: '#3b82f6', category: 'COMMODITIES' },
    { key: 'power_plants', label: 'Power Plants', count: '40 Assets', color: '#f59e0b', category: 'INFRASTRUCTURE' },
    { key: 'refineries', label: 'Refineries', count: '21 Complex', color: '#ef4444', category: 'COMMODITIES' },
    { key: 'retail', label: 'Retail', count: '85 Centers', color: '#ec4899', category: 'MARITIME' },
    { key: 'seaports', label: 'Seaports', count: '13 Mega', color: '#10b981', category: 'MARITIME' },
    { key: 'storage_terminals', label: 'Storage Terminals', count: '6 Strategic', color: '#60a5fa', category: 'COMMODITIES' },
    { key: 'underground_storage', label: 'Underground Storage', count: '12 Caverns', color: '#c084fc', category: 'COMMODITIES' },
    { key: 'vessels', label: 'Vessels', count: '60 Live AIS', color: '#00e5ff', category: 'MARITIME' },
    { key: 'weather', label: 'Weather', count: 'Atmospheric', color: '#38bdf8', category: 'CLIMATE' },
    { key: 'weather_stations', label: 'Weather Stations (WFOR)', count: '6 Buoys', color: '#38bdf8', category: 'CLIMATE' },
    { key: 'world_equity', label: 'World Equity Markets', count: '15 Indices', color: '#22c55e', category: 'FINANCIAL' }
  ];

  var NEW_DATASETS = [
    { key: 'data_centers', label: 'Data Centers', count: '12 Hyperscale Hubs', color: '#22c55e', category: 'INFRASTRUCTURE' },
    { key: 'municipal_bonds', label: 'Municipal Bonds (US)', count: '18 State & Local Issuers', color: '#f59e0b', category: 'FINANCIAL' },
    { key: 'hydrogen_assets', label: 'Hydrogen Assets', count: '14 Clean Electrolyzers', color: '#a855f7', category: 'ENERGY' },
    { key: 'cyclone_tracks', label: 'Cyclone Historic Tracks', count: 'Cat 4-5 Trajectories', color: '#f43f5e', category: 'CLIMATE' },
    { key: 'energy_storage', label: 'Energy Storage', count: '16 Grid BESS Facilities', color: '#10b981', category: 'INFRASTRUCTURE' },
    { key: 'crop_yields', label: 'Crop Yield Forecasts (US)', count: 'Midwest Corn/Soy/Wheat', color: '#84cc16', category: 'COMMODITIES' },
    { key: 'coastal_flood', label: 'Coastal Flood Risk', count: '100Y Storm Surge & SLR', color: '#06b6d4', category: 'CLIMATE' },
    { key: 'drought_risk', label: 'Drought Risk', count: 'PDSI Extreme / Severe', color: '#d97706', category: 'CLIMATE' },
    { key: 'riverine_flood', label: 'Riverine Flood Risk', count: 'FEMA 100Y Inundation', color: '#0ea5e9', category: 'CLIMATE' },
    { key: 'fertilizers', label: 'Fertilizer Manufacturers', count: '6 Major Nitrogen Hubs', color: '#84cc16', category: 'COMMODITIES' },
    { key: 'natural_gas_flows', label: 'Natural Gas Flows (N.Am.)', count: 'Real-time Telemetry', color: '#00e5ff', category: 'COMMODITIES' },
    { key: 'power_iso', label: 'Power ISO Regions', count: '7 Grids (PJM, ERCOT)', color: '#eab308', category: 'INFRASTRUCTURE' }
  ];

  // ═══════════════════════════════════════════════════════════════
  // ── MAP INITIALIZATION (LEAFLET + ZERO WATERMARK CANVAS) ──
  // ═══════════════════════════════════════════════════════════════
  function initLeafletBmap() {
    var container = document.getElementById('bmap_leaflet_map');
    if (!container || typeof L === 'undefined') return;

    // Institutional zero-watermark Esri Dark Canvas & Real Satellite
    baseTileLayers.dark = L.tileLayer('https://services.arcgisonline.com/arcgis/rest/services/Canvas/World_Dark_Gray_Base/MapServer/tile/{z}/{y}/{x}', {
      maxZoom: 18, minZoom: 1, attribution: 'Bloomberg / Esri Dark Canvas'
    });
    baseTileLayers.dark_ref = L.tileLayer('https://services.arcgisonline.com/arcgis/rest/services/Canvas/World_Dark_Gray_Reference/MapServer/tile/{z}/{y}/{x}', {
      maxZoom: 18, minZoom: 1
    });
    baseTileLayers.satellite = L.tileLayer('https://services.arcgisonline.com/arcgis/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}', {
      maxZoom: 19, minZoom: 1, attribution: 'Esri Sub-Meter Satellite'
    });
    baseTileLayers.nautical = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      maxZoom: 18, minZoom: 1, attribution: 'OpenStreetMap Marine Nav'
    });

    leafletMap = L.map('bmap_leaflet_map', {
      center: [26.4, 56.2], // Strait of Hormuz
      zoom: 6,
      minZoom: 1,
      maxZoom: 19,
      zoomControl: false,
      attributionControl: false,
      layers: [baseTileLayers.dark, baseTileLayers.dark_ref],
      preferCanvas: true
    });

    window.bmapMap = leafletMap;
    window.leafletMap = leafletMap;
    window.globalVessels = globalVessels;
    window.manhattanBranches = manhattanBranches;
    window.vesselMarkersMap = vesselMarkersMap;
    window.datasetLayerGroups = datasetLayerGroups;
    window.activeLayers = activeLayers;

    // Add Zoom Control at top-left
    L.control.zoom({ position: 'topleft' }).addTo(leafletMap);

    // Track mouse coordinates in HUD
    leafletMap.on('mousemove', function(e) {
      var el = document.getElementById('bmap_cursor_coords');
      if (el) {
        el.textContent = 'WGS84: ' + Math.abs(e.latlng.lat).toFixed(4) + '° ' + (e.latlng.lat >= 0 ? 'N' : 'S') +
                         ', ' + Math.abs(e.latlng.lng).toFixed(4) + '° ' + (e.latlng.lng >= 0 ? 'E' : 'W');
      }
    });

    // Handle zoom LOD & weather canvas redraws
    leafletMap.on('zoomend moveend viewreset resize', function() {
      handleMapZoomLOD();
      redrawWeatherHeatmap();
      redrawCanvasOverlay();
    });

    // Initialize All Layer Groups
    initBankBranchesLayer();
    initPipelinesLayers();
    initVesselsLayer();
    initGlobalInfrastructureLayers();
    initWorldEquityLayer();
    initDenseGridLayer();

    // Start Weather Heatmap Engine
    initWeatherHeatmapCanvas();

    // Start Live AIS Dead-Reckoning Kinematics Engine (2-second updates)
    startLiveKinematicsEngine();

    // Render Sidebars, Controls and Secondary Views
    renderDatasetSidebar();
    updateLegendsVisibility();
    renderBmapTableData('berths');
    renderReadNewsStories();
    renderSplcNetwork('AAPL');
    renderFxcMatrix();
    initGpcCandlestickChart();
    initVolSurfaceCanvas();
  }

  // ═══════════════════════════════════════════════════════════════
  // ── WEATHER & ATMOSPHERIC HEATMAP CANVAS ENGINE (IMAGES 1 & 2) ──
  // ═══════════════════════════════════════════════════════════════
  function initWeatherHeatmapCanvas() {
    var canvas = document.getElementById('bmapWeatherCanvas');
    if (!canvas) return;
    redrawWeatherHeatmap();
  }

  function redrawWeatherHeatmap() {
    var canvas = document.getElementById('bmapWeatherCanvas');
    if (!canvas || !leafletMap) return;

    if (!activeLayers.weather) {
      canvas.style.display = 'none';
      return;
    }
    canvas.style.display = 'block';

    var mapSize = leafletMap.getSize();
    canvas.width = mapSize.x;
    canvas.height = mapSize.y;

    var ctx = canvas.getContext('2d');
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    var bounds = leafletMap.getBounds();

    if (weatherConfig.type === 'cloud_cover') {
      drawCloudCoverHeatmap(ctx, canvas.width, canvas.height, bounds);
    } else if (weatherConfig.type === 'temperature') {
      drawTemperatureHeatmap(ctx, canvas.width, canvas.height, bounds);
    }
  }

  // Exact Cloud Cover Grayscale Heatmap (Screenshot 1: WhatsApp Image 2026-11-08 at 11.22.37 (1).jpeg)
  function drawCloudCoverHeatmap(ctx, width, height, bounds) {
    ctx.save();
    ctx.globalAlpha = 0.55;

    // Atmospheric cloud turbulence simulation matching satellite bands
    // Mid-latitude storm tracks (40N-60N and 40S-60S) + Equatorial ITCZ belt (5S-10N)
    var cloudBands = [
      { latMin: -5, latMax: 12, density: 0.85, name: 'ITCZ' },
      { latMin: 35, latMax: 65, density: 0.70, name: 'North Atlantic / Pacific Storm Track' },
      { latMin: -65, latMax: -40, density: 0.80, name: 'Southern Ocean Roaring Forties' },
      { latMin: 20, latMax: 30, density: 0.20, name: 'Subtropical Desert High' } // Sahara/Arabia clear sky
    ];

    var step = Math.max(12, Math.floor(width / 60));
    for (var x = 0; x < width; x += step) {
      for (var y = 0; y < height; y += step) {
        var pt = leafletMap.containerPointToLatLng([x + step / 2, y + step / 2]);
        var lat = pt.lat;
        var lon = pt.lng;

        // Calculate cloud density based on latitude and turbulence
        var baseDensity = 0.35;
        cloudBands.forEach(function(b) {
          if (lat >= b.latMin && lat <= b.latMax) {
            var mid = (b.latMin + b.latMax) / 2;
            var span = (b.latMax - b.latMin) / 2;
            var factor = Math.cos(((lat - mid) / span) * (Math.PI / 2));
            baseDensity = Math.max(baseDensity, b.density * factor);
          }
        });

        // Desert clear-sky masking (Sahara: 15-30N, -15 to 35E; Arabia: 18-30N, 38-55E)
        if (lat >= 15 && lat <= 32 && lon >= -15 && lon <= 55) {
          baseDensity *= 0.15; // Clear skies over North Africa & Persian Gulf
        }

        // Turbulence noise
        var noise = Math.sin(lat * 0.15) * Math.cos(lon * 0.15) * 0.25 +
                    Math.sin(lat * 0.4 + lon * 0.3) * 0.15;
        var finalCloud = Math.min(1.0, Math.max(0.0, baseDensity + noise));

        if (finalCloud > 0.18) {
          var grad = ctx.createRadialGradient(x + step / 2, y + step / 2, 2, x + step / 2, y + step / 2, step * 1.4);
          var alpha = finalCloud * 0.85;
          grad.addColorStop(0, 'rgba(255, 255, 255, ' + alpha.toFixed(3) + ')');
          grad.addColorStop(0.5, 'rgba(210, 220, 235, ' + (alpha * 0.6).toFixed(3) + ')');
          grad.addColorStop(1, 'rgba(150, 160, 180, 0)');
          ctx.fillStyle = grad;
          ctx.fillRect(x - step / 2, y - step / 2, step * 2, step * 2);
        }
      }
    }
    ctx.restore();
  }

  // Exact Temperature Thermal Spectrum Heatmap (Screenshot 2: WhatsApp Image 2026-11-08 at 11.22.37 (2).jpeg)
  function drawTemperatureHeatmap(ctx, width, height, bounds) {
    ctx.save();
    ctx.globalAlpha = 0.42;

    var step = Math.max(14, Math.floor(width / 50));
    for (var x = 0; x < width; x += step) {
      for (var y = 0; y < height; y += step) {
        var pt = leafletMap.containerPointToLatLng([x + step / 2, y + step / 2]);
        var lat = pt.lat;
        var lon = pt.lng;

        // Thermal gradient: -140F at poles to +120F in tropics/deserts
        // Polar: Deep Navy -> Mid: Green/Yellow -> Equator/Sahara: Red
        var normalizedLat = Math.abs(lat) / 90; // 0 (Equator) to 1 (Pole)
        var tempF = 110 - (normalizedLat * 180); // roughly +110F to -70F

        // Hot desert boost
        if (lat >= 12 && lat <= 32 && lon >= -15 && lon <= 55) {
          tempF += 25; // Sahara & Arabia extreme heat
        }

        // Color mapper: -140 to 140
        var tNorm = Math.min(1.0, Math.max(0.0, (tempF + 140) / 280));
        var color = getThermalColor(tNorm);

        var grad = ctx.createRadialGradient(x + step / 2, y + step / 2, 2, x + step / 2, y + step / 2, step * 1.5);
        grad.addColorStop(0, color);
        grad.addColorStop(1, 'transparent');
        ctx.fillStyle = grad;
        ctx.fillRect(x - step / 2, y - step / 2, step * 2, step * 2);
      }
    }
    ctx.restore();
  }

  function getThermalColor(norm) {
    // 0: Deep blue, 0.25: Cyan, 0.5: Green, 0.7: Yellow, 0.85: Orange, 1.0: Crimson Red
    if (norm < 0.25) {
      var f = norm / 0.25;
      return 'rgba(0, ' + Math.floor(70 * f) + ', ' + Math.floor(180 + 75 * f) + ', 0.7)';
    } else if (norm < 0.5) {
      var f = (norm - 0.25) / 0.25;
      return 'rgba(0, ' + Math.floor(70 + 170 * f) + ', ' + Math.floor(255 - 100 * f) + ', 0.65)';
    } else if (norm < 0.75) {
      var f = (norm - 0.5) / 0.25;
      return 'rgba(' + Math.floor(240 * f) + ', 220, 50, 0.65)';
    } else {
      var f = (norm - 0.75) / 0.25;
      return 'rgba(' + Math.floor(240 + 15 * f) + ', ' + Math.floor(180 * (1 - f)) + ', 20, 0.75)';
    }
  }

  window.setWeatherType = function(type) {
    weatherConfig.type = type;
    redrawWeatherHeatmap();
    updateLegendsVisibility();
    renderActiveDatasetCards();
  };

  window.setWeatherStat = function(stat) {
    weatherConfig.stat = stat;
    redrawWeatherHeatmap();
  };

  window.setWeatherDay = function(day) {
    weatherConfig.day = day;
    redrawWeatherHeatmap();
  };

  // ═══════════════════════════════════════════════════════════════
  // ── LAYER 1: US BANK BRANCHES & MANHATTAN HIGH-RES SATELLITE ──
  // ═══════════════════════════════════════════════════════════════
  function initBankBranchesLayer() {
    datasetLayerGroups['bank_branches'] = L.layerGroup().addTo(leafletMap);
    renderBankBranchesOnMap(branchesCompact);

    // Manhattan high-res branch markers (Images 7, 9, 10)
    var manLayer = L.layerGroup();
    manhattanBranches.forEach(function(mb) {
      var m = L.circleMarker([mb.lat, mb.lon], {
        radius: 8,
        fillColor: '#38bdf8',
        color: '#00e5ff',
        weight: 2,
        fillOpacity: 0.95
      });
      var mbTooltipHtml = '<div style="font-family:var(--font-mono);font-size:10px;background:rgba(5,8,15,0.96);border:1.5px solid #38bdf8;padding:6px 10px;border-radius:4px;box-shadow:0 6px 20px rgba(0,0,0,0.85);color:#fff;min-width:190px;line-height:1.4;">' +
        '<div style="color:#38bdf8;font-weight:bold;font-size:11px;">🏛️ ' + mb.name + '</div>' +
        '<div style="color:#fff;">' + mb.bank + '</div>' +
        '<div><span style="color:#94a3b8;">Address:</span> ' + mb.address + '</div>' +
        '<div><span style="color:#94a3b8;">Deposits:</span> <strong style="color:#00e676;">$' + (mb.deposits_k >= 1000 ? (mb.deposits_k/1000).toFixed(2) + 'M' : mb.deposits_k + 'k') + '</strong></div>' +
        '<div><span style="color:#94a3b8;">Assets:</span> <strong style="color:#ffaa00;">$' + (mb.assets_k ? (mb.assets_k/1000000).toFixed(2) + 'B' : 'N/A') + '</strong></div>' +
        '<div style="margin-top:3px;padding-top:2px;border-top:1px dashed #1e2e44;color:#00e5ff;font-size:8.5px;">🖱️ Click for Street-Level FDIC Audit</div>' +
      '</div>';

      m.bindTooltip(mbTooltipHtml, {
        sticky: true,
        opacity: 0.98,
        className: 'bb-custom-tooltip'
      });

      m.on('click', function() { showManhattanBranchPopup(mb); });
      manLayer.addLayer(m);
    });
    datasetLayerGroups['manhattan_branches'] = manLayer.addTo(leafletMap);
  }

  function renderBankBranchesOnMap(branches) {
    var group = datasetLayerGroups['bank_branches'];
    if (!group) return;
    group.clearLayers();

    var canvasRenderer = L.canvas({ padding: 0.5 });
    branches.forEach(function(b) {
      // Decode compact branch: [lat, lon, dep_k, bank_idx, branch_name, state_idx, type_idx]
      var lat = b[0], lon = b[1], dep = b[2];
      var radius = Math.min(18, Math.max(3.5, Math.log10(dep + 1) * 2.6));

      var marker = L.circleMarker([lat, lon], {
        renderer: canvasRenderer,
        radius: radius,
        fillColor: '#a855f7',
        color: '#c084fc',
        weight: 1,
        opacity: 0.8,
        fillOpacity: 0.5
      });

      var bName = banksLookup[b[3]] || 'FDIC Insured Financial Institution';
      var state = statesLookup[b[5]] || 'US';
      var bType = typesLookup[b[6]] || 'Commercial Banking Branch';

      var bTooltipHtml = '<div style="font-family:var(--font-mono);font-size:10px;background:rgba(5,8,15,0.96);border:1.5px solid #a855f7;padding:6px 10px;border-radius:4px;box-shadow:0 6px 20px rgba(0,0,0,0.85);color:#fff;min-width:190px;line-height:1.4;">' +
        '<div style="color:#a855f7;font-weight:bold;font-size:11px;">🏛️ ' + b[4] + '</div>' +
        '<div style="color:#38bdf8;font-weight:bold;">' + bName + '</div>' +
        '<div><span style="color:#94a3b8;">State / Type:</span> ' + state + ' · ' + bType + '</div>' +
        '<div><span style="color:#94a3b8;">Branch Deposits:</span> <strong style="color:#00e676;">$' + (dep >= 1000 ? (dep / 1000).toFixed(2) + 'M' : dep + 'k') + ' USD</strong></div>' +
        '<div style="margin-top:3px;padding-top:2px;border-top:1px dashed #1e2e44;color:#ffaa00;font-size:8.5px;">🖱️ Click for Full FDIC Balance Sheet</div>' +
      '</div>';

      marker.bindTooltip(bTooltipHtml, {
        sticky: true,
        opacity: 0.98,
        className: 'bb-custom-tooltip'
      });

      // INSTANT DETAILS ON MOUSE HOVER OR DRAG OVER YELLOW CIRCLES (Bank Branches)
      marker.on('mouseover mousemove', function() {
        showBranchQuickTooltip(b[4], bName, dep, state, bType, lat, lon);
      });

      marker.on('click', function() {
        showBranchQuickTooltip(b[4], bName, dep, state, bType, lat, lon);
        leafletMap.panTo([lat, lon]);
      });

      group.addLayer(marker);
    });
  }


  // Helper to display details for generic infrastructure / commodity yellow/colored circles
  function showAssetQuickDetails(item, color) {
    var pop = document.getElementById('bmap_branch_popup');
    if (!pop) return;
    pop.style.display = 'block';
    document.getElementById('pop_branch_name').textContent = item.name || 'Industrial Asset Node';
    document.getElementById('pop_branch_company').textContent = item.country ? (item.country + ' · ' + (item.type || 'Infrastructure Facility')) : 'Commodity / Asset Hub';
    document.getElementById('pop_branch_dep').textContent = item.capacity ? item.capacity : (item.yield ? ('Yield: ' + item.yield + ' (' + item.rating + ')') : 'Active Node');
    document.getElementById('pop_branch_comp_dep').textContent = item.volume ? ('Issuance: ' + item.volume) : (item.yieldForecast ? ('Yield: ' + item.yieldForecast) : (item.lat.toFixed(4) + '°, ' + item.lon.toFixed(4) + '°'));
    document.getElementById('pop_branch_comp_assets').textContent = item.condition ? ('Condition: ' + item.condition) : 'Bloomberg Operational Asset Layer';
    document.getElementById('pop_branch_year').textContent = '2026';
  }

  window.zoomToActiveVessel = function() {
    if (activeFollowVessel && leafletMap) {
      leafletMap.flyTo([activeFollowVessel.lat, activeFollowVessel.lon], 11, { duration: 1.2 });
    }
  };

  window.viewActiveVesselHistory = function() {
    if (!activeFollowVessel || !leafletMap) return;
    alert([
      'Bloomberg AIS Voyage History (Vessel: ' + activeFollowVessel.name + '):',
      '',
      '• Previous Port: RAS TANURA TERMINAL (Dep: 3 days ago, Draft: 21.2m)',
      '• Current Waypoint: STRAIT OF HORMUZ INBOUND (Speed: ' + activeFollowVessel.speed + ' kn, Course: ' + activeFollowVessel.course + '°)',
      '• Destination: NINGBO OIL PIER (ETA: 11 Days, 4,280 NM Remaining)',
      '• Fixture: Bahri Oil Tankers / Saudi Aramco Commercial Operation'
    ].join(String.fromCharCode(10)));
  };

  window.zoomToActiveBranch = function() {
    if (leafletMap) {
      setBmapTileLayer('satellite');
      leafletMap.setZoom(17);
    }
  };

  window.viewActiveBranchFilings = function() {
    alert([
      'FDIC Financial Institution Audit Filings (Q4 2026):',
      '',
      '• DuPont ROA: 1.84% (Net Margin: 32.1%, Asset Turnover: 5.73%)',
      '• Net Interest Margin (NIM): 5.82%',
      '• Gross NPA: 1.14% | Net NPA: 0.28%',
      '• Capital Adequacy Ratio (CAR): 19.8% (Tier-1: 17.2%)',
      '• Source: FDIC Call Report Schedule RC-E / SOIC DuPont Tree'
    ].join(String.fromCharCode(10)));
  };

  window.showBranchQuickTooltip = function(name, company, depK, state, type, lat, lon) {
    showBranchQuickTooltip(name, company, depK, state, type, lat, lon);
  };

  function showBranchQuickTooltip(name, company, depK, state, type, lat, lon) {
    var pop = document.getElementById('bmap_branch_popup');
    if (!pop) return;
    document.getElementById('pop_branch_name').textContent = name;
    document.getElementById('pop_branch_company').textContent = company;
    var numDep = Number(depK) || 0;
    document.getElementById('pop_branch_dep').textContent = '$' + (numDep >= 1000 ? (numDep / 1000).toFixed(2) + 'M' : numDep.toFixed(0) + 'k') + ' (' + numDep.toLocaleString() + ' USD)';
    document.getElementById('pop_branch_comp_dep').textContent = '$2,128,462,000';
    document.getElementById('pop_branch_comp_assets').textContent = '$3,914,143,296';
    document.getElementById('pop_branch_year').textContent = '2022 (' + state + ' · ' + type + ')';
    pop.style.display = 'block';
  }

  function showManhattanBranchPopup(mb) {
    var pop = document.getElementById('bmap_branch_popup');
    if (!pop) return;
    document.getElementById('pop_branch_name').textContent = mb.name;
    document.getElementById('pop_branch_company').textContent = mb.company;
    document.getElementById('pop_branch_dep').textContent = mb.dep_branch.toLocaleString();
    document.getElementById('pop_branch_comp_dep').textContent = mb.dep_company.toLocaleString();
    document.getElementById('pop_branch_comp_assets').textContent = mb.assets_company.toLocaleString();
    document.getElementById('pop_branch_year').textContent = mb.year + ' (' + mb.address + ')';
    pop.style.display = 'block';
  }

  window.filterBankBranches = function() {
    var nameSelect = document.getElementById('filter_bank_name');
    var branchSelect = document.getElementById('filter_bank_branch');
    var stateSelect = document.getElementById('filter_bank_state');
    var depSlider = document.getElementById('slider_bank_dep');

    var selBank = nameSelect ? nameSelect.value : 'ALL';
    var selBranch = branchSelect ? branchSelect.value : 'ALL';
    var selState = stateSelect ? stateSelect.value : 'ALL';
    var minDepM = depSlider ? parseInt(depSlider.value) : 0;

    bankFilterState.name = selBank;
    bankFilterState.branch = selBranch;
    bankFilterState.state = selState;
    bankFilterState.minDep = minDepM;

    var filtered = branchesCompact.filter(function(b) {
      var bankName = banksLookup[b[3]] || '';
      var bType = typesLookup[b[6]] || '';
      var bState = statesLookup[b[5]] || '';
      var depM = b[2] / 1000;

      if (selBank !== 'ALL' && bankName.indexOf(selBank) === -1) return false;
      if (selBranch !== 'ALL' && bType.indexOf(selBranch) === -1) return false;
      if (selState !== 'ALL' && bState !== selState) return false;
      if (depM < minDepM) return false;
      return true;
    });

    renderBankBranchesOnMap(filtered);

    var lbl = document.getElementById('lbl_bank_dep_val');
    if (lbl) {
      lbl.textContent = '$' + minDepM + 'M+ (' + filtered.length + ' Branches)';
    }
  };

  window.resetBankFilter = function() {
    if (document.getElementById('filter_bank_name')) document.getElementById('filter_bank_name').value = 'ALL';
    if (document.getElementById('filter_bank_branch')) document.getElementById('filter_bank_branch').value = 'ALL';
    if (document.getElementById('filter_bank_state')) document.getElementById('filter_bank_state').value = 'ALL';
    if (document.getElementById('slider_bank_dep')) document.getElementById('slider_bank_dep').value = 0;
    filterBankBranches();
  };

  // ═══════════════════════════════════════════════════════════════
  // ── LAYER 2: PIPELINES (CRUDE GLOBAL & NATURAL GAS N.AM.) ──
  // ═══════════════════════════════════════════════════════════════
  function initPipelinesLayers() {
    // 1. Crude Pipelines (Worldwide - Image 27)
    var crudeGroup = L.layerGroup();
    crudePipelines.forEach(function(pipe) {
      var poly = L.polyline(pipe.coords, {
        color: '#00e5ff',
        weight: 3.5,
        opacity: 0.9,
        lineCap: 'round',
        lineJoin: 'round'
      });
      var crudeTtHtml = '<div style="font-family:var(--font-mono);font-size:10px;background:rgba(5,8,15,0.96);border:1.5px solid #00e5ff;padding:6px 10px;border-radius:4px;box-shadow:0 6px 18px rgba(0,0,0,0.85);color:#fff;min-width:180px;line-height:1.4;">' +
        '<div style="color:#00e5ff;font-weight:bold;font-size:11px;">🛢️ ' + pipe.name + '</div>' +
        '<div><span style="color:#94a3b8;">Operator:</span> <span style="color:#fff;">' + pipe.company + '</span></div>' +
        '<div><span style="color:#94a3b8;">Capacity:</span> <strong style="color:#ffaa00;">' + pipe.capacity + '</strong></div>' +
        '<div><span style="color:#94a3b8;">Diameter / Length:</span> ' + pipe.diameter + ' · ' + pipe.length + '</div>' +
        '<div><span style="color:#00e676;">Status: ● ' + pipe.status + '</span></div>' +
      '</div>';

      poly.bindTooltip(crudeTtHtml, {
        sticky: true,
        opacity: 0.98,
        className: 'bb-custom-tooltip'
      });

      poly.bindPopup('<div style="font-family:var(--font-mono);font-size:10px;color:#fff;">' +
        '<strong style="color:#00e5ff;">' + pipe.name + '</strong><br>' +
        '<span style="color:#94a3b8;">Operator:</span> ' + pipe.company + '<br>' +
        '<span style="color:#94a3b8;">Capacity:</span> ' + pipe.capacity + '<br>' +
        '<span style="color:#94a3b8;">Diameter:</span> ' + pipe.diameter + '<br>' +
        '<span style="color:#94a3b8;">Length:</span> ' + pipe.length + '<br>' +
        '<span style="color:#00e676;">Status: ' + pipe.status + '</span>' +
      '</div>');
      crudeGroup.addLayer(poly);
    });
    datasetLayerGroups['crude_pipelines'] = crudeGroup.addTo(leafletMap);

    // 2. North American Natural Gas Pipelines (Image 12)
    var gasGroup = L.layerGroup();
    gasPipelines.forEach(function(gpipe) {
      var poly = L.polyline(gpipe.coords, {
        color: gpipe.color || '#f97316',
        weight: 4,
        opacity: 0.95
      });
      var gasTtHtml = '<div style="font-family:var(--font-mono);font-size:10px;background:rgba(5,8,15,0.96);border:1.5px solid ' + (gpipe.color || '#f97316') + ';padding:6px 10px;border-radius:4px;box-shadow:0 6px 18px rgba(0,0,0,0.85);color:#fff;min-width:180px;line-height:1.4;">' +
        '<div style="color:' + (gpipe.color || '#f97316') + ';font-weight:bold;font-size:11px;">⛽ ' + gpipe.name + '</div>' +
        '<div><span style="color:#94a3b8;">Holding Co:</span> <span style="color:#fff;">' + gpipe.holding_co + '</span></div>' +
        '<div><span style="color:#94a3b8;">Type:</span> <strong style="color:' + gpipe.color + ';">' + gpipe.type + '</strong></div>' +
        '<div><span style="color:#94a3b8;">Capacity:</span> <strong style="color:#ffaa00;">' + gpipe.capacity + '</strong></div>' +
        '<div><span style="color:#00e676;">Status: ● ' + gpipe.status + '</span></div>' +
      '</div>';

      poly.bindTooltip(gasTtHtml, {
        sticky: true,
        opacity: 0.98,
        className: 'bb-custom-tooltip'
      });

      poly.on('click', function(e) {
        showGasPipelinePopup(gpipe, e.latlng);
      });
      gasGroup.addLayer(poly);
    });
    datasetLayerGroups['natural_gas'] = gasGroup.addTo(leafletMap);
  }

  function showGasPipelinePopup(gpipe, latlng) {
    L.popup()
      .setLatLng(latlng)
      .setContent('<div style="background:#090f1a;padding:8px;border:1px solid #ffaa00;border-radius:3px;font-family:var(--font-mono);font-size:10px;color:#fff;min-width:210px;">' +
        '<div style="color:#ffaa00;font-weight:bold;margin-bottom:4px;">' + gpipe.name + '</div>' +
        '<div><span style="color:#94a3b8;">Holding Co:</span> ' + gpipe.holding_co + '</div>' +
        '<div><span style="color:#94a3b8;">Type:</span> <strong style="color:' + gpipe.color + ';">' + gpipe.type + '</strong></div>' +
        '<div><span style="color:#94a3b8;">Capacity:</span> ' + gpipe.capacity + '</div>' +
        '<div style="color:#00e676;margin-top:2px;">● ' + gpipe.status + '</div>' +
      '</div>')
      .openOn(leafletMap);
  }

  // ═══════════════════════════════════════════════════════════════
  // ── LAYER 3: LIVE AIS VESSELS & GREG MORTIMER TRAJECTORY ──
  // ═══════════════════════════════════════════════════════════════
  function initVesselsLayer() {
    var vslGroup = L.layerGroup();
    globalVessels.forEach(function(v) {
      var iconHtml = '<div style="transform:rotate(' + (v.course || 0) + 'deg);color:#00e5ff;font-size:12px;font-weight:900;text-shadow:0 0 6px rgba(0,229,255,0.8);cursor:pointer;">➤</div>';
      var vIcon = L.divIcon({
        className: 'vessel-div-icon',
        html: iconHtml,
        iconSize: [14, 14],
        iconAnchor: [7, 7]
      });

      var marker = L.marker([v.lat, v.lon], { icon: vIcon, interactive: true });

      // INSTANT DETAILS ON MOUSE HOVER OR DRAG OVER BLUE SHIPS (Matching red button details)
      marker.on('mouseover mousemove', function(e) {
        selectActiveVessel(v);
        showUniversalVesselPopup(v);
      });

      marker.on('click', function(e) {
        selectActiveVessel(v);
        showUniversalVesselPopup(v);
        leafletMap.panTo([v.lat, v.lon]);
      });

      // Bloomberg HUD Tooltip tracking mouse drag/hover (Screenshots 8 & 21)
      var vTooltipHtml = '<div style="font-family:var(--font-mono);font-size:10px;background:rgba(5,8,15,0.96);border:1.5px solid #00e5ff;padding:6px 10px;border-radius:4px;box-shadow:0 6px 20px rgba(0,0,0,0.85);color:#fff;min-width:195px;line-height:1.4;">' +
        '<div style="display:flex;justify-content:space-between;align-items:center;border-bottom:1px solid #162438;padding-bottom:3px;margin-bottom:4px;">' +
          '<strong style="color:#00e5ff;font-size:11px;">🚢 ' + v.name + '</strong>' +
          '<span style="background:#1e3a5f;color:#38bdf8;font-size:8.5px;padding:1px 4px;border-radius:2px;font-weight:800;">' + (v.type || 'VLCC') + '</span>' +
        '</div>' +
        '<div><span style="color:#94a3b8;">IMO / MMSI:</span> <span style="color:#fff;">' + v.imo + ' · ' + v.mmsi + '</span></div>' +
        '<div><span style="color:#94a3b8;">Owner:</span> <span style="color:#ffaa00;">' + (v.owner || 'International Seaways') + '</span></div>' +
        '<div><span style="color:#94a3b8;">Speed / Course:</span> <span style="color:#00e676;font-weight:bold;">' + v.speed + ' kn</span> @ ' + v.course + '°</div>' +
        '<div><span style="color:#94a3b8;">Draft / DWT:</span> <span style="color:#ffaa00;">' + v.draft + 'm</span> · ' + ((v.dwt || 150000)/1000).toFixed(0) + 'k MT</div>' +
        '<div><span style="color:#94a3b8;">Destination:</span> <strong style="color:#38bdf8;">' + (v.dest || 'Refining Terminal') + '</strong></div>' +
        '<div><span style="color:#94a3b8;">Status:</span> <span style="color:#00e676;">● ' + (v.status || 'Under way using engine') + '</span></div>' +
        '<div style="margin-top:4px;padding-top:3px;border-top:1px dashed #1e2e44;color:#ffaa00;font-size:8.5px;display:flex;justify-content:space-between;">' +
          '<span>🖱️ Click for AIS Telemetry</span>' +
          '<span style="color:#38bdf8;">AHOY Live</span>' +
        '</div>' +
      '</div>';

      marker.bindTooltip(vTooltipHtml, {
        sticky: true,
        opacity: 0.98,
        className: 'bb-custom-tooltip'
      });

      marker.on('click', function() { 
        selectActiveVessel(v); 
        showUniversalVesselPopup(v);
      });
      vslGroup.addLayer(marker);
      vesselMarkersMap[v.id] = { marker: marker, data: v };
    });

    // Greg Mortimer Expedition Vessel & Yellow Trajectory Vector (Screenshot 8)
    var gmIcon = L.divIcon({
      className: 'gm-div-icon',
      html: '<div style="transform:rotate(145deg);color:#00e5ff;font-size:14px;font-weight:900;text-shadow:0 0 8px #6366f1;cursor:pointer;">➤</div>',
      iconSize: [16, 16],
      iconAnchor: [8, 8]
    });
    var gmMarker = L.marker([gregMortimer.lat, gregMortimer.lon], { icon: gmIcon });

    var gmTooltipHtml = '<div style="font-family:var(--font-mono);font-size:10px;background:rgba(5,8,15,0.96);border:1.5px solid #a855f7;padding:6px 10px;border-radius:4px;box-shadow:0 6px 20px rgba(0,0,0,0.85);color:#fff;min-width:200px;line-height:1.4;">' +
      '<div style="display:flex;justify-content:space-between;align-items:center;border-bottom:1px solid #312e81;padding-bottom:3px;margin-bottom:4px;">' +
        '<strong style="color:#c7d2fe;font-size:11px;">🚢 GREG MORTIMER</strong>' +
        '<span style="background:#312e81;color:#a5b4fc;font-size:8.5px;padding:1px 4px;border-radius:2px;font-weight:800;">PASSENGER</span>' +
      '</div>' +
      '<div><span style="color:#94a3b8;">IMO:</span> <span style="color:#fff;">9834648</span> · <span style="color:#94a3b8;">Flag:</span> <span style="color:#ffaa00;">🇵🇹 Portugal</span></div>' +
      '<div><span style="color:#94a3b8;">Speed / Course:</span> <span style="color:#00e676;font-weight:bold;">10.5 kn</span> @ 145°</div>' +
      '<div><span style="color:#94a3b8;">Draft / Max:</span> <span style="color:#ffaa00;">5.2m / 5.3m</span></div>' +
      '<div><span style="color:#94a3b8;">Destination:</span> <strong style="color:#ffaa00;">DEVIL ISLAND</strong></div>' +
      '<div><span style="color:#94a3b8;">Status:</span> <span style="color:#00e676;">● Under way using engine</span></div>' +
      '<div style="margin-top:4px;padding-top:3px;border-top:1px dashed #312e81;color:#a5b4fc;font-size:8.5px;">🖱️ Click for More ▾ Menu &amp; Track</div>' +
    '</div>';

    gmMarker.bindTooltip(gmTooltipHtml, {
      sticky: true,
      opacity: 0.98,
      className: 'bb-custom-tooltip'
    });

    gmMarker.on('click', function() {
      showGregMortimerPopup();
    });
    vslGroup.addLayer(gmMarker);

    // Yellow Historical and Dead-Reckoning Voyage Trajectory Spline
    var gmTrack = L.polyline(gregMortimer.track, {
      color: '#eab308', // Yellow matching Screenshot 8
      weight: 2,
      dashArray: '6, 6',
      opacity: 0.95
    });
    vslGroup.addLayer(gmTrack);

    datasetLayerGroups['vessels'] = vslGroup.addTo(leafletMap);
  }

  window.selectActiveVessel = function(v) {
    selectActiveVessel(v);
  };

  function selectActiveVessel(v) {
    activeFollowVessel = v;
    var destEl = document.getElementById('vessel_card_dest');
    var draftEl = document.getElementById('vessel_card_draft');
    var dwtEl = document.getElementById('vessel_card_dwt');
    var classEl = document.getElementById('vessel_card_class');
    var ownerEl = document.getElementById('vessel_card_owner');
    var nameEl = document.getElementById('vessel_hud_name');
    var specsEl = document.getElementById('vessel_hud_specs');
    var berthEl = document.getElementById('vessel_hud_berth');

    if (destEl) destEl.textContent = v.dest || 'Refining Node';
    if (draftEl) draftEl.textContent = v.draft + 'm';
    if (dwtEl) dwtEl.textContent = (v.dwt ? v.dwt.toLocaleString() : 'N/A') + ' MT';
    if (classEl) classEl.textContent = v.type || 'VLCC';
    if (ownerEl) ownerEl.textContent = v.owner || 'Aramco / Bahri';
    if (nameEl) nameEl.textContent = v.name;
    if (specsEl) specsEl.textContent = v.speed + ' kts · ' + v.course + '° True · Draft ' + v.draft + 'm';
    if (berthEl) berthEl.textContent = 'Berth: ' + (v.berth || 'Strait of Hormuz Channel');

    // Pan smoothly
    leafletMap.panTo([v.lat, v.lon]);
  }


  window.showUniversalVesselPopup = function(v) {
    var pop = document.getElementById('bmap_universal_vessel_popup');
    if (!pop) return;
    document.getElementById('uni_vessel_name').textContent = v.name;
    document.getElementById('uni_vessel_type').textContent = v.type || 'VLCC';
    document.getElementById('uni_vessel_status').textContent = v.status || 'Under way using engine';
    document.getElementById('uni_vessel_imo').textContent = (v.imo || '9394562') + ' / ' + (v.mmsi || '538002941');
    document.getElementById('uni_vessel_owner').textContent = v.owner || 'International Seaways';
    document.getElementById('uni_vessel_dest').textContent = v.dest || 'China (Ningbo)';
    document.getElementById('uni_vessel_berth').textContent = v.berth || v.region || 'Strait of Hormuz Inbound';
    document.getElementById('uni_vessel_speed').textContent = (v.speed || '11.4') + ' kn @ ' + (v.course || 0) + '°';
    document.getElementById('uni_vessel_draft_dwt').textContent = (v.draft || 21.2) + 'm · ' + (v.dwt ? v.dwt.toLocaleString() : '318,000') + ' MT';
    pop.style.display = 'block';
  };

  window.toggleUniversalVesselMoreDropdown = function() {
    var dd = document.getElementById('uni_vessel_more_dropdown');
    if (dd) dd.style.display = (dd.style.display === 'none' ? 'block' : 'none');
  };

  function showGregMortimerPopup() {
    var pop = document.getElementById('bmap_greg_mortimer_popup');
    if (pop) pop.style.display = 'block';
    leafletMap.panTo([gregMortimer.lat, gregMortimer.lon]);
  }

  window.toggleGregMortimerMoreDropdown = function() {
    var dd = document.getElementById('greg_more_dropdown');
    if (dd) dd.style.display = dd.style.display === 'none' ? 'block' : 'none';
  };

  // ═══════════════════════════════════════════════════════════════
  // ── LAYER 4: WORLD EQUITY MARKETS CHOROPLETH (IMAGES 2 & 3) ──
  // ═══════════════════════════════════════════════════════════════
  function initWorldEquityLayer() {
    var eqGroup = L.layerGroup();
    var canvasRenderer = L.canvas({ padding: 0.5 });

    worldEquityData.forEach(function(item) {
      // Shading based on performance: green for positive, red for negative
      var isPos = item.val >= 0;
      var color = isPos ? (item.val >= 1.5 ? '#10b981' : '#059669') : (item.val <= -1.5 ? '#ef4444' : '#b91c1c');

      var m = L.circleMarker([item.lat, item.lon], {
        renderer: canvasRenderer,
        radius: 12,
        fillColor: color,
        color: '#fff',
        weight: 1.5,
        fillOpacity: 0.85
      });

      var arrowIcon = isPos ? '▲' : '▼';
      m.bindTooltip('<div style="font-family:var(--font-mono);font-size:10px;background:#05080e;border:1px solid ' + color + ';padding:4px 8px;border-radius:3px;color:#fff;">' +
        '<strong style="color:#ffaa00;">' + item.country + '</strong><br>' +
        '<span>' + item.index + ': ' + item.last + '</span><br>' +
        '<span style="color:' + color + ';font-weight:bold;">' + arrowIcon + ' ' + item.chg + '</span>' +
      '</div>', { sticky: true, opacity: 0.95 });

      eqGroup.addLayer(m);
    });

    datasetLayerGroups['world_equity'] = eqGroup.addTo(leafletMap);
  }

  // ═══════════════════════════════════════════════════════════════
  // ── LAYER 5: GLOBAL INSTITUTIONAL INFRASTRUCTURE SUITE ──
  // ═══════════════════════════════════════════════════════════════
  function initGlobalInfrastructureLayers() {
    var canvasRenderer = L.canvas({ padding: 0.5 });

    function addPointsLayer(key, dataList, color, radius, isDefaultOn) {
      var grp = L.layerGroup();
      dataList.forEach(function(item) {
        var m = L.circleMarker([item.lat, item.lon], {
          renderer: canvasRenderer,
          radius: radius,
          fillColor: color,
          color: '#ffffff',
          weight: 1,
          fillOpacity: 0.8
        });
        var ttHtml = '<div style="font-family:var(--font-mono);font-size:10px;background:rgba(5,8,15,0.96);border:1.5px solid ' + color + ';padding:6px 9px;border-radius:4px;box-shadow:0 6px 18px rgba(0,0,0,0.85);color:#fff;min-width:180px;line-height:1.4;">' +
          '<div style="color:' + color + ';font-weight:bold;font-size:11px;">● ' + item.name + '</div>' +
          '<div><span style="color:#94a3b8;">Country:</span> <span style="color:#fff;">' + item.country + '</span></div>' +
          (item.capacity ? '<div><span style="color:#94a3b8;">Capacity:</span> <strong style="color:#ffaa00;">' + item.capacity + '</strong></div>' : '') +
          (item.type ? '<div><span style="color:#94a3b8;">Type:</span> ' + item.type + '</div>' : '') +
          '<div><span style="color:#00e676;">Status: ' + (item.status || 'Active / Operating') + '</span></div>' +
          '<div style="margin-top:3px;padding-top:2px;border-top:1px dashed #1e2e44;color:#94a3b8;font-size:8.5px;">🖱️ Click to Pin Details</div>' +
        '</div>';

        m.bindTooltip(ttHtml, {
          sticky: true,
          opacity: 0.98,
          className: 'bb-custom-tooltip'
        });

        m.bindPopup('<div style="font-family:var(--font-mono);font-size:10px;color:#fff;">' +
          '<strong style="color:' + color + ';">' + item.name + '</strong><br>' +
          '<span style="color:#94a3b8;">Country:</span> ' + item.country + '<br>' +
          (item.capacity ? '<span style="color:#94a3b8;">Capacity:</span> ' + item.capacity + '<br>' : '') +
          (item.type ? '<span style="color:#94a3b8;">Type:</span> ' + item.type + '<br>' : '') +
          (item.status ? '<span style="color:#00e676;">Status: ' + item.status + '</span>' : '') +
        '</div>');
        grp.addLayer(m);
      });
      datasetLayerGroups[key] = isDefaultOn ? grp.addTo(leafletMap) : grp;
    }

    addPointsLayer('power_plants', globalUtilities, '#f59e0b', 5, true);
    addPointsLayer('refineries', globalRefineries, '#ef4444', 6, true);
    addPointsLayer('lng_terminals', globalLng, '#06b6d4', 6, true);
    addPointsLayer('seaports', globalSeaports, '#10b981', 6, true);
    addPointsLayer('data_centers', globalDataCenters, '#22c55e', 5.5, false);
    addPointsLayer('municipal_bonds', globalMunicipalBonds, '#f59e0b', 6, false);
    addPointsLayer('crop_yields', globalCropYields, '#84cc16', 6, false);
    addPointsLayer('semiconductor_fabs', globalSemiconductors, '#a855f7', 5.5, false);
    addPointsLayer('financial_centers', globalFinancialCenters, '#eab308', 5, false);
    addPointsLayer('mining_hubs', globalMining, '#f97316', 5, false);
    addPointsLayer('fertilizers', globalFertilizers, '#84cc16', 5, false);
    addPointsLayer('storage_terminals', globalStorage, '#60a5fa', 5, false);
    addPointsLayer('gas_hubs', globalGasHubs, '#fb923c', 5, false);
    addPointsLayer('weather_stations', globalWeatherStations, '#38bdf8', 5, false);
    addPointsLayer('earthquakes', globalEarthquakes, '#f87171', 6, false);
    addPointsLayer('cyclones', globalCyclones, '#ef4444', 7, false);
  }

  function initDenseGridLayer() {
    var grp = L.layerGroup();
    var canvasRenderer = L.canvas({ padding: 0.5 });
    globalDenseGrid.forEach(function(item) {
      var m = L.circleMarker([item.lat, item.lon], {
        renderer: canvasRenderer,
        radius: 2.8,
        fillColor: '#facc15',
        color: '#ca8a04',
        weight: 0.5,
        fillOpacity: 0.75
      });

      var ttHtml = '<div style="font-family:var(--font-mono);font-size:10px;background:rgba(5,8,15,0.96);border:1.5px solid #facc15;padding:6px 9px;border-radius:3px;box-shadow:0 6px 18px rgba(0,0,0,0.85);color:#fff;min-width:180px;line-height:1.4;">' +
        '<div style="color:#facc15;font-weight:bold;font-size:10.5px;">✨ ' + (item.name || 'Grid Node ' + item.id) + '</div>' +
        '<div><span style="color:#94a3b8;">Country:</span> <span style="color:#fff;">' + item.country + '</span></div>' +
        '<div><span style="color:#94a3b8;">Type:</span> <span style="color:#38bdf8;">' + item.type + '</span></div>' +
        '<div><span style="color:#94a3b8;">Coords:</span> ' + item.lat.toFixed(3) + '°, ' + item.lon.toFixed(3) + '°</div>' +
        '<div style="color:#eab308;font-size:8px;margin-top:2px;border-top:1px dashed #332600;padding-top:2px;">Bloomberg Global Constellation Grid</div>' +
      '</div>';

      m.bindTooltip(ttHtml, {
        sticky: true,
        opacity: 0.98,
        className: 'bb-custom-tooltip'
      });

      grp.addLayer(m);
    });
    datasetLayerGroups['dense_grid'] = grp;
  }

  // ═══════════════════════════════════════════════════════════════
  // ── DOCKED MAP CONTENT SIDEBAR CONTROLLER (SCREENSHOTS 1, 2, 4) ──
  // ═══════════════════════════════════════════════════════════════

  function renderDatasetSidebar() {
    renderActiveDatasetCards();
    renderSuggestedDatasetsList();
    renderNewDatasetsList();
    updateActiveDatasetsCountPill();
  }

  // Renders the Bloomberg parameter control cards at the top of Map Content
  function renderActiveDatasetCards() {
    var container = document.getElementById('active_dataset_cards_container');
    if (!container) return;
    container.innerHTML = '';

    // CARD 1: WEATHER (SCREENSHOT 1 & 2)
    if (activeLayers.weather) {
      var wCard = document.createElement('div');
      wCard.style.cssText = 'background:#080e18;border:1px solid #38bdf8;border-radius:4px;padding:8px 10px;font-size:9.5px;';
      wCard.innerHTML = 
        '<div style="display:flex;justify-content:space-between;align-items:center;border-bottom:1px solid #162438;padding-bottom:4px;margin-bottom:6px;">' +
          '<div style="display:flex;align-items:center;gap:4px;">' +
            '<span style="color:#ffaa00;">▾</span>' +
            '<strong style="color:#38bdf8;font-size:10.5px;">Weather</strong>' +
          '</div>' +
          '<div style="display:flex;align-items:center;gap:6px;">' +
            '<span style="color:#64748b;font-size:9px;cursor:pointer;">≡▾</span>' +
            '<span onclick="window.removeBmapDataset(\\'weather\\')" style="color:#94a3b8;cursor:pointer;font-weight:bold;">✕</span>' +
          '</div>' +
        '</div>' +
        '<div style="display:flex;flex-direction:column;gap:5px;">' +
          '<div style="display:flex;justify-content:space-between;align-items:center;">' +
            '<span style="color:#94a3b8;">Type</span>' +
            '<select onchange="window.setWeatherType(this.value)" style="background:#05080e;color:#ffaa00;border:1px solid #ffaa00;border-radius:2px;font-size:9.5px;padding:2px 6px;width:130px;outline:none;">' +
              '<option value="cloud_cover"' + (weatherConfig.type === 'cloud_cover' ? ' selected' : '') + '>Cloud Cover ▾</option>' +
              '<option value="temperature"' + (weatherConfig.type === 'temperature' ? ' selected' : '') + '>Temperature ▾</option>' +
              '<option value="precipitation">Precipitation ▾</option>' +
              '<option value="wind_speed">Wind Speed ▾</option>' +
            '</select>' +
          '</div>' +
          '<div style="display:flex;justify-content:space-between;align-items:center;">' +
            '<span style="color:#94a3b8;">Stat</span>' +
            '<select onchange="window.setWeatherStat(this.value)" style="background:#05080e;color:#ffaa00;border:1px solid #203a5e;border-radius:2px;font-size:9.5px;padding:2px 6px;width:130px;outline:none;">' +
              '<option value="avg">Avg ▾</option>' +
              '<option value="max">Max ▾</option>' +
              '<option value="min">Min ▾</option>' +
            '</select>' +
          '</div>' +
          '<div style="display:flex;justify-content:space-between;align-items:center;">' +
            '<span style="color:#94a3b8;">Day</span>' +
            '<select onchange="window.setWeatherDay(this.value)" style="background:#05080e;color:#ffaa00;border:1px solid #203a5e;border-radius:2px;font-size:9.5px;padding:2px 6px;width:130px;outline:none;">' +
              '<option value="today">Today ▾</option>' +
              '<option value="yesterday">Yesterday ▾</option>' +
              '<option value="7day">7-Day Avg ▾</option>' +
            '</select>' +
          '</div>' +
        '</div>';
      container.appendChild(wCard);
    }

    // CARD 2: WORLD EQUITY MARKETS (SCREENSHOT 2 & 3)
    if (activeLayers.world_equity) {
      var eqCard = document.createElement('div');
      eqCard.style.cssText = 'background:#080e18;border:1px solid #10b981;border-radius:4px;padding:8px 10px;font-size:9.5px;';
      eqCard.innerHTML = 
        '<div style="display:flex;justify-content:space-between;align-items:center;border-bottom:1px solid #162438;padding-bottom:4px;margin-bottom:6px;">' +
          '<div style="display:flex;align-items:center;gap:4px;">' +
            '<span style="color:#ffaa00;">▾</span>' +
            '<strong style="color:#10b981;font-size:10.5px;">World Equity Markets</strong>' +
          '</div>' +
          '<div style="display:flex;align-items:center;gap:6px;">' +
            '<span style="color:#64748b;font-size:9px;cursor:pointer;">≡▾</span>' +
            '<span onclick="window.removeBmapDataset(\\'world_equity\\')" style="color:#94a3b8;cursor:pointer;font-weight:bold;">✕</span>' +
          '</div>' +
        '</div>' +
        '<div style="display:flex;flex-direction:column;gap:4px;">' +
          '<div style="display:flex;justify-content:space-between;"><span style="color:#94a3b8;">Benchmark:</span><span style="color:#00e676;font-weight:bold;">SPX, NIFTY, NKY, DAX</span></div>' +
          '<div style="display:flex;justify-content:space-between;"><span style="color:#94a3b8;">Bull/Bear Range:</span><span style="color:#ffaa00;">-2.0% to +2.0%</span></div>' +
        '</div>';
      container.appendChild(eqCard);
    }

    // CARD 3: VESSELS (SCREENSHOT 4 & 27)
    if (activeLayers.vessels) {
      var vCard = document.createElement('div');
      vCard.style.cssText = 'background:#080e18;border:1.5px solid #ffaa00;border-radius:4px;padding:8px 10px;font-size:9.5px;';
      vCard.innerHTML = 
        '<div style="display:flex;justify-content:space-between;align-items:center;border-bottom:1px solid #2a1f0a;padding-bottom:4px;margin-bottom:6px;">' +
          '<div style="display:flex;align-items:center;gap:4px;">' +
            '<span style="color:#ffaa00;">▾</span>' +
            '<strong style="color:#ffaa00;font-size:10.5px;">Vessels</strong>' +
          '</div>' +
          '<div style="display:flex;align-items:center;gap:6px;">' +
            '<span style="color:#00e676;font-size:8.5px;font-weight:bold;">● LIVE AIS</span>' +
            '<span style="color:#64748b;font-size:9px;cursor:pointer;">≡▾</span>' +
            '<span onclick="window.removeBmapDataset(\\'vessels\\')" style="color:#94a3b8;cursor:pointer;font-weight:bold;">✕</span>' +
          '</div>' +
        '</div>' +
        '<div style="display:flex;flex-direction:column;gap:4px;">' +
          '<div style="display:flex;justify-content:space-between;align-items:center;">' +
            '<span style="color:#94a3b8;">Vessel / IMO</span>' +
            '<select onchange="window.selectVesselByQuery(this.value)" style="background:#05080e;color:#00e5ff;border:1px solid #203a5e;font-size:9px;border-radius:2px;max-width:130px;outline:none;">' +
              '<option value="ALL">All In Scope (60)</option>' +
              '<option value="HORMUZ">Strait of Hormuz Fleet</option>' +
              '<option value="SEAWAYS CATALONIA">SEAWAYS CATALONIA (VLCC)</option>' +
              '<option value="AL MAQWA">AL MAQWA (VLCC)</option>' +
              '<option value="SAFANIYAH STAR">SAFANIYAH STAR (VLCC)</option>' +
              '<option value="GREG_MORTIMER">GREG MORTIMER (Expedition)</option>' +
            '</select>' +
          '</div>' +
          '<div style="display:flex;justify-content:space-between;"><span style="color:#94a3b8;">Type</span><strong style="color:#fff;">Tankers (All)</strong></div>' +
          '<div style="display:flex;justify-content:space-between;"><span style="color:#94a3b8;">Status</span><span style="color:#00e676;">In Service / Commercial</span></div>' +
          '<div style="display:flex;justify-content:space-between;"><span style="color:#94a3b8;">Destination</span><strong style="color:#fff;" id="vessel_card_dest">Global Refining Hubs</strong></div>' +
          '<div style="display:flex;justify-content:space-between;"><span style="color:#94a3b8;">Draft</span><span style="color:#ffaa00;" id="vessel_card_draft">14.2m - 21.8m</span></div>' +
          '<div style="display:flex;justify-content:space-between;"><span style="color:#94a3b8;">DWT</span><span style="color:#fff;" id="vessel_card_dwt">115,000 - 325,000 MT</span></div>' +
          '<div style="display:flex;justify-content:space-between;"><span style="color:#94a3b8;">Class</span><span style="color:#38bdf8;" id="vessel_card_class">VLCC / Suezmax</span></div>' +
          '<div style="display:flex;justify-content:space-between;"><span style="color:#94a3b8;">Ben Owner</span><span style="color:#cbd5e1;" id="vessel_card_owner">International Seaways / Bahri</span></div>' +
          '<div style="display:flex;justify-content:space-between;border-top:1px solid #162438;padding-top:3px;margin-top:2px;"><span style="color:#94a3b8;">Last Seen</span><span style="color:#00e676;">90 Days ▾</span></div>' +
          '<div id="vessel_telemetry_hud" style="background:#050912;border:1px solid #16253b;border-radius:3px;padding:4px;margin-top:3px;">' +
            '<div style="color:#00e5ff;font-weight:bold;font-size:9.5px;" id="vessel_hud_name">SEAWAYS CATALONIA</div>' +
            '<div style="color:#94a3b8;font-size:8.5px;" id="vessel_hud_specs">8.8 kts · 295° True · Draft 14.2m</div>' +
            '<div style="color:#cbd5e1;font-size:8.5px;" id="vessel_hud_berth">Berth: Strait of Hormuz Eastbound TSS</div>' +
            '<div style="display:flex;gap:4px;margin-top:4px;">' +
              '<button onclick="zoomToActiveVessel()" style="flex:1;background:#0284c7;color:#fff;border:none;padding:2px;border-radius:2px;font-size:8.5px;cursor:pointer;font-weight:bold;">🔍 Zoom</button>' +
              '<button onclick="toggleFollowActiveVessel()" style="flex:1;background:#065f46;color:#34d399;border:1px solid #059669;padding:2px;border-radius:2px;font-size:8.5px;cursor:pointer;font-weight:bold;">🎯 Follow</button>' +
              '<button onclick="toggleArpaVectors()" style="flex:1;background:#132032;color:#ffaa00;border:1px solid #203a5e;padding:2px;border-radius:2px;font-size:8.5px;cursor:pointer;font-weight:bold;">⚡ ARPA</button>' +
            '</div>' +
          '</div>' +
        '</div>';
      container.appendChild(vCard);
    }

    // CARD 4: BANK BRANCHES (US) (SCREENSHOT 4)
    if (activeLayers.bank_branches) {
      var bCard = document.createElement('div');
      bCard.style.cssText = 'background:#080e18;border:1px solid #a855f7;border-radius:4px;padding:8px 10px;font-size:9.5px;';
      bCard.innerHTML = 
        '<div style="display:flex;justify-content:space-between;align-items:center;border-bottom:1px solid #162438;padding-bottom:4px;margin-bottom:6px;">' +
          '<div style="display:flex;align-items:center;gap:4px;">' +
            '<span style="color:#ffaa00;">▾</span>' +
            '<strong style="color:#c084fc;font-size:10.5px;">Bank Branches (US)</strong>' +
          '</div>' +
          '<div style="display:flex;align-items:center;gap:6px;">' +
            '<span style="color:#64748b;font-size:9px;cursor:pointer;">≡▾</span>' +
            '<span onclick="window.removeBmapDataset(\\'bank_branches\\')" style="color:#94a3b8;cursor:pointer;font-weight:bold;">✕</span>' +
          '</div>' +
        '</div>' +
        '<div style="display:flex;flex-direction:column;gap:4px;">' +
          '<div style="display:flex;justify-content:space-between;align-items:center;">' +
            '<span style="color:#94a3b8;">Name</span>' +
            '<select id="filter_bank_name" onchange="filterBankBranches()" style="background:#05080e;color:#ffaa00;border:1px solid #203a5e;font-size:9px;border-radius:2px;width:130px;outline:none;">' +
              '<option value="ALL">All Institutions</option>' +
              '<option value="JPMorgan Chase Bank, NA">JPMorgan Chase</option>' +
              '<option value="Bank of America, NA">Bank of America</option>' +
              '<option value="Wells Fargo Bank, NA">Wells Fargo</option>' +
              '<option value="Citibank, NA">Citibank</option>' +
            '</select>' +
          '</div>' +
          '<div style="display:flex;justify-content:space-between;align-items:center;">' +
            '<span style="color:#94a3b8;">Branch</span>' +
            '<select id="filter_bank_branch" onchange="filterBankBranches()" style="background:#05080e;color:#38bdf8;border:1px solid #203a5e;font-size:9px;border-radius:2px;width:130px;outline:none;">' +
              '<option value="ALL">All Branch Types</option>' +
              '<option value="Full Service">Full Service</option>' +
              '<option value="Commercial">Commercial Vault</option>' +
            '</select>' +
          '</div>' +
          '<div>' +
            '<div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:2px;">' +
              '<span style="color:#94a3b8;">Deposits (M)</span>' +
              '<span id="lbl_bank_dep_val" style="color:#ffaa00;font-weight:bold;">$0M+ (1,675)</span>' +
            '</div>' +
            '<input type="range" id="slider_bank_dep" min="0" max="5000" step="50" value="0" oninput="filterBankBranches()" style="width:100%;accent-color:#ffaa00;cursor:pointer;height:5px;">' +
          '</div>' +
          '<div style="display:flex;justify-content:space-between;align-items:center;">' +
            '<span style="color:#94a3b8;">Location</span>' +
            '<select id="filter_bank_state" onchange="filterBankBranches()" style="background:#05080e;color:#34d399;border:1px solid #203a5e;font-size:9px;border-radius:2px;width:130px;outline:none;">' +
              '<option value="ALL">All States (US)</option>' +
              '<option value="NY">New York (NY)</option>' +
              '<option value="CA">California (CA)</option>' +
              '<option value="TX">Texas (TX)</option>' +
              '<option value="IL">Illinois (IL)</option>' +
              '<option value="FL">Florida (FL)</option>' +
            '</select>' +
          '</div>' +
          '<div style="display:flex;gap:4px;margin-top:3px;">' +
            '<button onclick="resetBankFilter()" style="flex:1;background:#132032;color:#94a3b8;border:1px solid #1c2e44;padding:2px;font-size:8.5px;border-radius:2px;cursor:pointer;">↺ Reset</button>' +
            '<button onclick="jumpToBmapPreset(\\'bank_branches\\')" style="flex:1;background:#0284c7;color:#fff;border:none;padding:2px;font-size:8.5px;font-weight:bold;border-radius:2px;cursor:pointer;">🔍 Fit US</button>' +
          '</div>' +
        '</div>';
      container.appendChild(bCard);
    }

    // CARD 5: CRUDE OIL PIPELINES (SCREENSHOT 27)
    if (activeLayers.crude_pipelines) {
      var pCard = document.createElement('div');
      pCard.style.cssText = 'background:#080e18;border:1px solid #0284c7;border-radius:4px;padding:8px 10px;font-size:9.5px;';
      pCard.innerHTML = 
        '<div style="display:flex;justify-content:space-between;align-items:center;border-bottom:1px solid #162438;padding-bottom:4px;margin-bottom:6px;">' +
          '<div style="display:flex;align-items:center;gap:4px;">' +
            '<span style="color:#ffaa00;">▾</span>' +
            '<strong style="color:#38bdf8;font-size:10.5px;">Crude Oil Pipelines</strong>' +
          '</div>' +
          '<div style="display:flex;align-items:center;gap:6px;">' +
            '<span style="color:#64748b;font-size:9px;cursor:pointer;">≡▾</span>' +
            '<span onclick="window.removeBmapDataset(\\'crude_pipelines\\')" style="color:#94a3b8;cursor:pointer;font-weight:bold;">✕</span>' +
          '</div>' +
        '</div>' +
        '<div style="display:flex;flex-direction:column;gap:4px;">' +
          '<div style="display:flex;justify-content:space-between;"><span style="color:#94a3b8;">Pipeline</span><strong style="color:#fff;">All (15 Major Arteries)</strong></div>' +
          '<div style="display:flex;justify-content:space-between;"><span style="color:#94a3b8;">Fuel</span><span style="color:#ffaa00;">All Selected ▾</span></div>' +
          '<div style="display:flex;justify-content:space-between;"><span style="color:#94a3b8;">Status</span><span style="color:#00e676;">3/8 Selected ▾</span></div>' +
          '<div style="display:flex;justify-content:space-between;align-items:center;"><span style="color:#94a3b8;">Line Width</span><span style="color:#38bdf8;font-weight:bold;">2 ▾</span></div>' +
          '<div style="display:flex;justify-content:space-between;align-items:center;"><span style="color:#94a3b8;">Size By</span><span style="color:#ffaa00;">Diameter ▾</span></div>' +
          '<div style="display:flex;justify-content:space-between;align-items:center;"><span style="color:#94a3b8;">Color By</span><span style="color:#38bdf8;">Uniform: Blue ▾</span></div>' +
          '<div style="display:flex;justify-content:space-between;align-items:center;"><span style="color:#94a3b8;">Labels</span><span style="color:#94a3b8;">Off ▾</span></div>' +
        '</div>';
      container.appendChild(pCard);
    }

    // CARD 6: NATURAL GAS (SCREENSHOT 12)
    if (activeLayers.natural_gas) {
      var ngCard = document.createElement('div');
      ngCard.style.cssText = 'background:#080e18;border:1px solid #00e5ff;border-radius:4px;padding:8px 10px;font-size:9.5px;';
      ngCard.innerHTML = 
        '<div style="display:flex;justify-content:space-between;align-items:center;border-bottom:1px solid #162438;padding-bottom:4px;margin-bottom:6px;">' +
          '<div style="display:flex;align-items:center;gap:4px;">' +
            '<span style="color:#ffaa00;">▾</span>' +
            '<strong style="color:#00e5ff;font-size:10.5px;">Natural Gas</strong>' +
          '</div>' +
          '<div style="display:flex;align-items:center;gap:6px;">' +
            '<span style="color:#64748b;font-size:9px;cursor:pointer;">≡▾</span>' +
            '<span onclick="window.removeBmapDataset(\\'natural_gas\\')" style="color:#94a3b8;cursor:pointer;font-weight:bold;">✕</span>' +
          '</div>' +
        '</div>' +
        '<div style="display:flex;flex-direction:column;gap:3px;color:#cbd5e1;">' +
          '<div><input type="checkbox"> LNG Berths</div>' +
          '<div><input type="checkbox"> LNG Terminals</div>' +
          '<div><input type="checkbox"> Storage Terminals</div>' +
          '<div><input type="checkbox"> Underground Storage</div>' +
          '<div style="color:#00e5ff;font-weight:bold;"><input type="checkbox" checked> Pipelines (N.Am.)</div>' +
          '<div><input type="checkbox"> Chemical Processing Plants</div>' +
          '<div><input type="checkbox"> Hubs</div>' +
        '</div>';
      container.appendChild(ngCard);
    }
  }

  // Renders the 24 Suggested Datasets accordion list with Bloomberg [+] buttons
  function renderSuggestedDatasetsList() {
    var cont = document.getElementById('suggested_datasets_list');
    if (!cont) return;
    cont.innerHTML = '';

    SUGGESTED_DATASETS.forEach(function(ds) {
      var isActive = !!activeLayers[ds.key];
      var row = document.createElement('div');
      row.id = 'sugg_row_' + ds.key;
      row.style.cssText = 'display:flex;align-items:center;justify-content:space-between;padding:3.5px 6px;border-radius:2px;cursor:pointer;font-size:9.5px;transition:background 0.15s;' +
        (isActive ? 'background:#111f33;color:#fff;border-left:2px solid #00e5ff;' : 'color:#94a3b8;');
      
      row.innerHTML = 
        '<div style="display:flex;align-items:center;gap:6px;">' +
          '<span style="color:' + (isActive ? '#00e676' : '#ffaa00') + ';font-weight:900;font-size:11px;">' + (isActive ? '✓' : '+') + '</span>' +
          '<span>' + ds.label + '</span>' +
        '</div>' +
        '<span style="color:' + (ds.color || '#64748b') + ';font-size:8.5px;font-weight:bold;">' + ds.count + '</span>';

      row.onclick = function() {
        if (isActive) {
          window.removeBmapDataset(ds.key);
        } else {
          window.addBmapDataset(ds.key);
        }
      };
      cont.appendChild(row);
    });
  }

  // Renders the 12 New Datasets accordion list with Bloomberg [+] buttons
  function renderNewDatasetsList() {
    var cont = document.getElementById('new_datasets_list');
    if (!cont) return;
    cont.innerHTML = '';

    NEW_DATASETS.forEach(function(ds) {
      var isActive = !!activeLayers[ds.key];
      var row = document.createElement('div');
      row.id = 'new_row_' + ds.key;
      row.style.cssText = 'display:flex;align-items:center;justify-content:space-between;padding:3.5px 6px;border-radius:2px;cursor:pointer;font-size:9.5px;transition:background 0.15s;' +
        (isActive ? 'background:#0f2b38;color:#fff;border-left:2px solid #38bdf8;' : 'color:#94a3b8;');
      
      row.innerHTML = 
        '<div style="display:flex;align-items:center;gap:6px;">' +
          '<span style="color:' + (isActive ? '#00e676' : '#38bdf8') + ';font-weight:900;font-size:11px;">' + (isActive ? '✓' : '+') + '</span>' +
          '<span>' + ds.label + '</span>' +
        '</div>' +
        '<span style="color:' + (ds.color || '#64748b') + ';font-size:8.5px;font-weight:bold;">' + ds.count + '</span>';

      row.onclick = function() {
        if (isActive) {
          window.removeBmapDataset(ds.key);
        } else {
          window.addBmapDataset(ds.key);
        }
      };
      cont.appendChild(row);
    });
  }

  // Add dataset when user clicks [+]
  window.addBmapDataset = function(key) {
    activeLayers[key] = true;
    var grp = datasetLayerGroups[key];
    if (leafletMap && grp && !leafletMap.hasLayer(grp)) {
      grp.addTo(leafletMap);
    }
    if (key === 'weather') {
      redrawWeatherHeatmap();
    }
    renderDatasetSidebar();
    updateLegendsVisibility();
    updateActiveDatasetsCountPill();
  };

  // Remove dataset when user clicks [x] on active card
  window.removeBmapDataset = function(key) {
    activeLayers[key] = false;
    var grp = datasetLayerGroups[key];
    if (leafletMap && grp && leafletMap.hasLayer(grp)) {
      leafletMap.removeLayer(grp);
    }
    if (key === 'weather') {
      var canvas = document.getElementById('bmapWeatherCanvas');
      if (canvas) canvas.style.display = 'none';
    }
    renderDatasetSidebar();
    updateLegendsVisibility();
    updateActiveDatasetsCountPill();
  };

  function updateActiveDatasetsCountPill() {
    var count = Object.values(activeLayers).filter(Boolean).length;
    var pill = document.getElementById('active_dataset_count_pill');
    var openPill = document.getElementById('open_pill_count');
    if (pill) pill.textContent = count + ' Active';
    if (openPill) openPill.textContent = count + ' Active';
  }

  // Accordion Expand/Collapse Handler
  window.toggleSectionAccordion = function(name) {
    accordionOpen[name] = !accordionOpen[name];
    var icon = document.getElementById('accordion_icon_' + name);
    var content = null;
    if (name === 'suggested') content = document.getElementById('suggested_datasets_list');
    else if (name === 'new') content = document.getElementById('new_datasets_list');
    else if (name === 'basemap') content = document.getElementById('basemap_selector_content');

    if (icon) icon.textContent = accordionOpen[name] ? '▾' : '▸';
    if (content) content.style.display = accordionOpen[name] ? (name === 'basemap' ? 'grid' : 'flex') : 'none';
  };

  // Toggle Map Content docked drawer
  window.toggleMapContentDrawer = function() {
    var drawer = document.getElementById('bmap_map_content_drawer');
    var openBtn = document.getElementById('btn_open_drawer_pill');
    if (!drawer) return;

    if (drawer.style.transform === 'translateX(100%)' || drawer.style.display === 'none') {
      drawer.style.display = 'flex';
      drawer.style.transform = 'translateX(0)';
      if (openBtn) openBtn.style.display = 'none';
    } else {
      drawer.style.transform = 'translateX(100%)';
      setTimeout(function() { drawer.style.display = 'none'; }, 250);
      if (openBtn) openBtn.style.display = 'block';
    }
  };

  // Search filter across all datasets inside the sidebar
  window.filterDatasetSidebar = function(q) {
    var query = q.toLowerCase();
    var allRows = document.querySelectorAll('[id^="sugg_row_"], [id^="new_row_"]');
    allRows.forEach(function(r) {
      r.style.display = r.textContent.toLowerCase().indexOf(query) >= 0 ? 'flex' : 'none';
    });
  };

  // ═══════════════════════════════════════════════════════════════
  // ── DYNAMIC FLOATING LEGENDS MANAGER (BOTTOM-LEFT) ──
  // ═══════════════════════════════════════════════════════════════
  function updateLegendsVisibility() {
    // Cloud cover legend
    var legCloud = document.getElementById('bmap_legend_cloud_cover');
    if (legCloud) {
      legCloud.style.display = (activeLayers.weather && weatherConfig.type === 'cloud_cover') ? 'block' : 'none';
    }

    // Temperature legend
    var legTemp = document.getElementById('bmap_legend_temperature');
    if (legTemp) {
      legTemp.style.display = (activeLayers.weather && weatherConfig.type === 'temperature') ? 'block' : 'none';
    }

    // World Equity Markets legend
    var legEq = document.getElementById('bmap_legend_world_equity');
    if (legEq) {
      legEq.style.display = activeLayers.world_equity ? 'block' : 'none';
    }

    // Bank Branches legend (concentric circles)
    var legBank = document.getElementById('bmap_radar_legend');
    if (legBank) {
      legBank.style.display = activeLayers.bank_branches ? 'block' : 'none';
    }

    // Natural Gas Pipelines legend
    var legGas = document.getElementById('bmap_legend_gas_pipelines');
    if (legGas) {
      legGas.style.display = activeLayers.natural_gas ? 'block' : 'none';
    }

    // Vessels & Crude Pipelines legend (bottom right)
    var legVslCrude = document.getElementById('bmap_legend_vessel_crude');
    if (legVslCrude) {
      legVslCrude.style.display = (activeLayers.vessels || activeLayers.crude_pipelines) ? 'flex' : 'none';
    }
  }

  // ═══════════════════════════════════════════════════════════════
  // ── VIEW ALL DATASETS MODAL DIALOG CONTROLLER ──
  // ═══════════════════════════════════════════════════════════════
  window.openAllDatasetsModal = function() {
    var modal = document.getElementById('bmap_all_datasets_modal');
    if (!modal) return;
    renderModalDatasetsList('');
    modal.style.display = 'flex';
  };

  window.closeAllDatasetsModal = function() {
    var modal = document.getElementById('bmap_all_datasets_modal');
    if (modal) modal.style.display = 'none';
  };

  function renderModalDatasetsList(query) {
    var body = document.getElementById('modal_datasets_body');
    if (!body) return;
    body.innerHTML = '';

    var allCombined = [].concat(SUGGESTED_DATASETS, NEW_DATASETS);
    // Deduplicate by key
    var seen = {};
    var uniqueList = [];
    allCombined.forEach(function(ds) {
      if (!seen[ds.key]) {
        seen[ds.key] = true;
        uniqueList.push(ds);
      }
    });

    var q = (query || '').toLowerCase();
    var filtered = uniqueList.filter(function(ds) {
      return ds.label.toLowerCase().indexOf(q) >= 0 || ds.category.toLowerCase().indexOf(q) >= 0;
    });

    filtered.forEach(function(ds) {
      var card = document.createElement('div');
      var isActive = !!activeLayers[ds.key];
      card.style.cssText = 'background:#05080e;border:1px solid #1e334d;border-radius:4px;padding:8px 12px;display:flex;justify-content:space-between;align-items:center;font-size:10px;';
      card.innerHTML = 
        '<div>' +
          '<div style="color:#fff;font-weight:bold;margin-bottom:2px;">' + ds.label + '</div>' +
          '<div style="color:#64748b;font-size:8.5px;">CATEGORY: <span style="color:#38bdf8;">' + ds.category + '</span> · COUNT: ' + ds.count + '</div>' +
        '</div>' +
        '<button onclick="toggleModalDataset(\\'' + ds.key + '\\')" style="background:' + (isActive ? '#065f46' : '#1e3a5f') + ';color:' + (isActive ? '#34d399' : '#00e5ff') + ';border:1px solid ' + (isActive ? '#059669' : '#3b82f6') + ';border-radius:3px;padding:4px 10px;font-size:9.5px;font-weight:bold;cursor:pointer;">' +
          (isActive ? '✓ Added' : '+ Add to Map') +
        '</button>';
      body.appendChild(card);
    });
  }

  window.toggleModalDataset = function(key) {
    if (activeLayers[key]) {
      window.removeBmapDataset(key);
    } else {
      window.addBmapDataset(key);
    }
    renderModalDatasetsList(document.getElementById('modal_dataset_search').value);
  };

  window.filterModalDatasets = function(q) {
    renderModalDatasetsList(q);
  };

  // ═══════════════════════════════════════════════════════════════
  // ── LIVE AIS KINEMATICS & VESSEL TRACKING ENGINE ──
  // ═══════════════════════════════════════════════════════════════
  function startLiveKinematicsEngine() {
    if (liveKinematicsTimer) clearInterval(liveKinematicsTimer);

    liveKinematicsTimer = setInterval(function() {
      globalVessels.forEach(function(v) {
        if (!v.speed || v.speed <= 0) return;

        // Kinematic dead-reckoning: lat/lon delta based on course & speed
        var headingRad = (v.course || 0) * (Math.PI / 180);
        var distDeg = (v.speed * 0.0005) / 60; // 2s displacement

        v.lat += Math.cos(headingRad) * distDeg;
        v.lon += Math.sin(headingRad) * distDeg;

        var item = vesselMarkersMap[v.id];
        if (item && item.marker) {
          item.marker.setLatLng([v.lat, v.lon]);
        }

        // Auto-follow active vessel if locked
        if (activeFollowVessel && activeFollowVessel.id === v.id && leafletMap) {
          leafletMap.panTo([v.lat, v.lon], { animate: true, duration: 0.8 });
        }
      });

      redrawCanvasOverlay();
    }, 2000);
  }

  function redrawCanvasOverlay() {
    var canvas = document.getElementById('bmapCanvas');
    if (!canvas || !leafletMap) return;

    var mapSize = leafletMap.getSize();
    canvas.width = mapSize.x;
    canvas.height = mapSize.y;

    var ctx = canvas.getContext('2d');
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    if (!showArpaVectors || !activeLayers.vessels) return;

    ctx.save();
    ctx.strokeStyle = '#00e5ff';
    ctx.lineWidth = 1.2;
    ctx.setLineDash([3, 3]);

    // Draw ARPA collision vectors
    globalVessels.forEach(function(v) {
      if (!v.speed || v.speed <= 0) return;
      var startPt = leafletMap.latLngToContainerPoint([v.lat, v.lon]);
      var headingRad = (v.course || 0) * (Math.PI / 180);
      var vectorLen = v.speed * 2.2; // 6-minute nautical extrapolation
      var endX = startPt.x + Math.sin(headingRad) * vectorLen;
      var endY = startPt.y - Math.cos(headingRad) * vectorLen;

      ctx.beginPath();
      ctx.moveTo(startPt.x, startPt.y);
      ctx.lineTo(endX, endY);
      ctx.stroke();
    });
    ctx.restore();
  }

  // ═══════════════════════════════════════════════════════════════
  // ── AUTO-ADAPTIVE SATELLITE ZOOM LOD & MANHATTAN TRANSITION ──
  // ═══════════════════════════════════════════════════════════════
  function handleMapZoomLOD() {
    var zoom = leafletMap.getZoom();
    var center = leafletMap.getCenter();

    // If within NYC/Manhattan bounding box and zoomed in >= 14, switch to Sub-Meter Real Satellite
    var isManhattan = (center.lat >= 40.69 && center.lat <= 40.82 && center.lng >= -74.03 && center.lng <= -73.92);

    if (currentTileKey === 'auto') {
      if (isManhattan && zoom >= 14) {
        if (!leafletMap.hasLayer(baseTileLayers.satellite)) {
          leafletMap.removeLayer(baseTileLayers.dark);
          leafletMap.removeLayer(baseTileLayers.dark_ref);
          leafletMap.addLayer(baseTileLayers.satellite);
        }
      } else {
        if (!leafletMap.hasLayer(baseTileLayers.dark)) {
          leafletMap.removeLayer(baseTileLayers.satellite);
          leafletMap.addLayer(baseTileLayers.dark);
          leafletMap.addLayer(baseTileLayers.dark_ref);
        }
      }
    }
  }

  window.setBmapTileLayer = function(key) {
    currentTileKey = key;
    // Remove all layers first
    Object.values(baseTileLayers).forEach(function(l) {
      if (leafletMap.hasLayer(l)) leafletMap.removeLayer(l);
    });

    if (key === 'dark') {
      leafletMap.addLayer(baseTileLayers.dark);
      leafletMap.addLayer(baseTileLayers.dark_ref);
    } else if (key === 'satellite') {
      leafletMap.addLayer(baseTileLayers.satellite);
    } else if (key === 'nautical') {
      leafletMap.addLayer(baseTileLayers.nautical);
    } else if (key === 'auto') {
      leafletMap.addLayer(baseTileLayers.dark);
      leafletMap.addLayer(baseTileLayers.dark_ref);
      handleMapZoomLOD();
    }

    // Update active button state
    ['dark', 'sat', 'naut', 'auto'].forEach(function(k) {
      var el = document.getElementById('bmap_layer_' + k);
      if (el) el.classList.remove('active');
    });
    var activeBtn = document.getElementById('bmap_layer_' + (key === 'satellite' ? 'sat' : key === 'nautical' ? 'naut' : key));
    if (activeBtn) activeBtn.classList.add('active');
  };

  // ═══════════════════════════════════════════════════════════════
  // ── PRESETS & JUMP CONTROLLERS (ALL SCREENSHOT SCENARIOS) ──
  // ═══════════════════════════════════════════════════════════════
  window.jumpToBmapPreset = function(presetKey) {
    if (!leafletMap) return;

    if (presetKey === 'hormuz') {
      // Screenshot 4: Hormuz 40+ Tankers
      leafletMap.setView([26.4, 56.2], 7);
      if (!activeLayers.vessels) window.addBmapDataset('vessels');
      var cat = globalVessels.find(function(v) { return v.name === 'SEAWAYS CATALONIA'; });
      if (cat) selectActiveVessel(cat);
      var scEl = document.getElementById('bmap_scope_label');
      if (scEl) scEl.textContent = 'STRAIT OF HORMUZ VLCC RADAR';
    } else if (presetKey === 'weather_cloud') {
      // Screenshot 1: Weather Cloud Cover Grayscale Heatmap
      leafletMap.setView([25.0, 10.0], 2.5);
      if (!activeLayers.weather) window.addBmapDataset('weather');
      window.setWeatherType('cloud_cover');
    } else if (presetKey === 'weather_temp') {
      // Screenshot 2: Weather Temperature Thermal Heatmap + World Equity
      leafletMap.setView([25.0, 10.0], 2.5);
      if (!activeLayers.weather) window.addBmapDataset('weather');
      if (!activeLayers.world_equity) window.addBmapDataset('world_equity');
      window.setWeatherType('temperature');
    } else if (presetKey === 'world_equity') {
      // Screenshot 3: World Equity Markets Choropleth
      leafletMap.setView([25.0, 10.0], 2.5);
      if (!activeLayers.world_equity) window.addBmapDataset('world_equity');
    } else if (presetKey === 'crude_pipelines') {
      // Screenshot 27: Global Crude Oil Pipelines & Vessels
      leafletMap.setView([40.0, 20.0], 3);
      if (!activeLayers.crude_pipelines) window.addBmapDataset('crude_pipelines');
      if (!activeLayers.vessels) window.addBmapDataset('vessels');
      var scEl = document.getElementById('bmap_scope_label');
      if (scEl) scEl.textContent = 'GLOBAL CRUDE OIL PIPELINES & REFINERIES';
    } else if (presetKey === 'gas_pipelines') {
      // Screenshot 12: N.Am. Natural Gas Pipelines & Copano Popup
      leafletMap.setView([32.0, -90.0], 5);
      if (!activeLayers.natural_gas) window.addBmapDataset('natural_gas');
      var cop = gasPipelines.find(function(p) { return p.id === 'gas_copano'; });
      if (cop) showGasPipelinePopup(cop, [29.74, -95.12]);
    } else if (presetKey === 'bank_branches') {
      // Screenshot 4: US Nationwide FDIC Bank Branches
      leafletMap.setView([38.5, -96.0], 4.5);
      if (!activeLayers.bank_branches) window.addBmapDataset('bank_branches');
    } else if (presetKey === 'manhattan') {
      // Screenshots 7, 9, 10: Manhattan Street-Level Satellite Zoom & FDIC Tooltip
      window.setBmapTileLayer('satellite');
      leafletMap.setView([40.7182, -74.0028], 17); // 400 Broadway
      var m400 = manhattanBranches.find(function(b) { return b.id === 'man_400_broadway'; });
      if (m400) showManhattanBranchPopup(m400);
    } else if (presetKey === 'greg_mortimer') {
      // Screenshot 8: Greg Mortimer Expedition Vessel & Trajectory Vector
      leafletMap.setView([gregMortimer.lat, gregMortimer.lon], 5);
      if (!activeLayers.vessels) window.addBmapDataset('vessels');
      showGregMortimerPopup();
    } else if (presetKey === 'dense_grid') {
      // Screenshot 3: Dense Global Constellation
      leafletMap.setView([35.0, 45.0], 4);
      if (!activeLayers.dense_grid) window.addBmapDataset('dense_grid');
    } else if (presetKey === 'world') {
      leafletMap.setView([20.0, 15.0], 2);
    }
  };

  // ═══════════════════════════════════════════════════════════════
  // ── SECONDARY VIEWS CONTROLLER (TABLE, CHART, NEWS, SPLC, FXC, VOL) ──
  // ═══════════════════════════════════════════════════════════════
  window.switchBmapView = function(viewId) {
    currentActiveView = viewId;
    var views = ['map', 'table', 'chart', 'news', 'splc', 'fxc', 'vol', 'soic'];
    views.forEach(function(v) {
      var cont = document.getElementById('bmap_view_container_' + v);
      var btn = document.getElementById('bmap_btn_view_' + v);
      if (cont) cont.style.display = (v === viewId) ? 'block' : 'none';
      if (btn) {
        if (v === viewId) {
          btn.style.background = '#1e3a5f';
          btn.style.color = '#00e5ff';
          btn.style.border = '1px solid #3b82f6';
          btn.style.borderBottom = '2px solid #00e5ff';
        } else {
          btn.style.background = '#0d1624';
          btn.style.color = '#94a3b8';
          btn.style.border = '1px solid #1c2e44';
          btn.style.borderBottom = 'none';
        }
      }
    });

    if (viewId === 'map' && leafletMap) {
      setTimeout(function() {
        leafletMap.invalidateSize();
        redrawWeatherHeatmap();
        redrawCanvasOverlay();
      }, 100);
    } else if (viewId === 'vol') {
      setTimeout(drawVolSurface, 100);
    } else if (viewId === 'splc') {
      setTimeout(function() { drawSplcNetworkCanvas(splcNetworks[activeSplcTicker]); }, 100);
    }
  };

  // Table View: Berth Visits (Screenshot 5)
  window.renderBmapTableData = function(type) {
    var thead = document.getElementById('bmap_tbl_head_tr');
    var tbody = document.getElementById('bmap_tbl_body');
    if (!thead || !tbody) return;
    tbody.innerHTML = '';

    if (type === 'berths') {
      thead.innerHTML = '<th>VISIT TYPE</th><th>BERTH NAME</th><th>COUNTRY/REGION</th><th>VESSEL CLASS</th><th>QUANTITY (MT)</th><th>VESSEL IMO</th>';
      berthVisits.forEach(function(b) {
        var tr = document.createElement('tr');
        tr.style.cursor = 'pointer';
        tr.innerHTML = 
          '<td style="color:' + (b.visit.indexOf('Export') >= 0 ? '#ffaa00' : '#38bdf8') + ';">' + b.visit + '</td>' +
          '<td style="color:#ffaa00;font-weight:bold;">' + b.berth + '</td>' +
          '<td>' + b.country + '</td>' +
          '<td style="color:#ffaa00;">' + b.cls + '</td>' +
          '<td style="text-align:right;color:#fff;font-weight:bold;">' + b.qty + '</td>' +
          '<td style="color:#ffaa00;">' + b.imo + '</td>';
        tr.onclick = function() {
          window.switchBmapView('map');
          leafletMap.setView([b.lat, b.lon], 9);
        };
        tbody.appendChild(tr);
      });
    } else if (type === 'branches') {
      thead.innerHTML = '<th>INSTITUTION</th><th>BRANCH NAME</th><th>STATE</th><th>TYPE</th><th>DEPOSITS</th>';
      branchesCompact.slice(0, 50).forEach(function(b) {
        var tr = document.createElement('tr');
        tr.innerHTML = 
          '<td style="color:#00e5ff;font-weight:bold;">' + (banksLookup[b[3]] || 'Bank') + '</td>' +
          '<td style="color:#fff;">' + b[4] + '</td>' +
          '<td style="color:#ffaa00;">' + (statesLookup[b[5]] || 'US') + '</td>' +
          '<td style="color:#94a3b8;">' + (typesLookup[b[6]] || 'Branch') + '</td>' +
          '<td style="color:#00e676;font-weight:bold;text-align:right;">$' + (b[2] / 1000).toFixed(2) + 'M</td>';
        tbody.appendChild(tr);
      });
    }
  };

  // READ Most Read News Wire (Screenshots 18 & 19)
  function renderReadNewsStories() {
    var cont = document.getElementById('bmap_news_stories_container');
    if (!cont) return;
    cont.innerHTML = '';

    readNewsStories.forEach(function(n, idx) {
      var item = document.createElement('div');
      item.style.cssText = 'background:#080e18;border:1px solid #162438;border-radius:3px;padding:8px 12px;font-family:var(--font-mono);font-size:10.5px;';
      item.innerHTML = 
        '<div style="display:flex;justify-content:space-between;margin-bottom:3px;">' +
          '<span style="color:#ffaa00;font-weight:bold;">' + (idx + 1) + ') ' + n.title + '</span>' +
          '<span style="color:#ffaa00;font-weight:bold;">' + n.src + ' &nbsp; ' + n.time + '</span>' +
        '</div>' +
        '<div style="color:#94a3b8;font-size:9.5px;line-height:1.3;">' + n.lead + '</div>';
      cont.appendChild(item);
    });
  }

  // SPLC Supply Chain Analysis (Screenshots 20, 24, 25)
  window.renderSplcNetwork = function(ticker) {
    activeSplcTicker = ticker;
    var data = splcNetworks[ticker] || splcNetworks['AAPL'];
    var supCont = document.getElementById('splc_suppliers_list');
    var custCont = document.getElementById('splc_customers_list');
    if (!supCont || !custCont) return;

    supCont.innerHTML = '';
    custCont.innerHTML = '';

    data.suppliers.forEach(function(s) {
      var d = document.createElement('div');
      d.style.cssText = 'background:#05080e;border:1px solid #1e334d;padding:5px 8px;border-radius:3px;font-size:9.5px;color:#fff;';
      d.innerHTML = 
        '<div style="color:#38bdf8;font-weight:bold;">' + s.name + '</div>' +
        '<div style="display:flex;justify-content:space-between;color:#94a3b8;margin-top:2px;">' +
          '<span>Rev: ' + s.rev + '</span>' +
          '<span>COGS: ' + s.cogs + '</span>' +
          '<span style="color:' + (s.surprise >= 0 ? '#00e676' : '#ff3344') + ';">Surp: ' + (s.surprise > 0 ? '+' : '') + s.surprise + '%</span>' +
        '</div>';
      supCont.appendChild(d);
    });

    data.customers.forEach(function(c) {
      var d = document.createElement('div');
      d.style.cssText = 'background:#05080e;border:1px solid #1e334d;padding:5px 8px;border-radius:3px;font-size:9.5px;color:#fff;';
      d.innerHTML = 
        '<div style="color:#34d399;font-weight:bold;">' + c.name + '</div>' +
        '<div style="display:flex;justify-content:space-between;color:#94a3b8;margin-top:2px;">' +
          '<span>Rev Exposure: ' + c.rev + '</span>' +
          '<span>COGS Share: ' + c.cogs + '</span>' +
        '</div>';
      custCont.appendChild(d);
    });

    drawSplcNetworkCanvas(data);
  };

  function drawSplcNetworkCanvas(data) {
    var canvas = document.getElementById('splcNetworkCanvas');
    if (!canvas) return;
    var ctx = canvas.getContext('2d');
    var w = canvas.width = canvas.parentElement.clientWidth;
    var h = canvas.height = canvas.parentElement.clientHeight || 550;

    ctx.clearRect(0, 0, w, h);

    // Center Target Node
    var cx = w / 2;
    var cy = h / 2;

    ctx.save();
    ctx.strokeStyle = '#1e3a5f';
    ctx.lineWidth = 1.5;

    // Draw lines to left suppliers
    var sStep = h / (data.suppliers.length + 1);
    data.suppliers.forEach(function(s, idx) {
      var sy = sStep * (idx + 1);
      ctx.beginPath();
      ctx.moveTo(10, sy);
      ctx.bezierCurveTo(cx - 80, sy, cx - 80, cy, cx, cy);
      ctx.stroke();
    });

    // Draw lines to right customers
    var cStep = h / (data.customers.length + 1);
    data.customers.forEach(function(c, idx) {
      var cyPos = cStep * (idx + 1);
      ctx.beginPath();
      ctx.moveTo(cx, cy);
      ctx.bezierCurveTo(cx + 80, cy, cx + 80, cyPos, w - 10, cyPos);
      ctx.stroke();
    });

    // Draw Center Box (Screenshot 24 & 25)
    ctx.fillStyle = '#061325';
    ctx.strokeStyle = '#ffaa00';
    ctx.lineWidth = 2;
    ctx.fillRect(cx - 75, cy - 35, 150, 70);
    ctx.strokeRect(cx - 75, cy - 35, 150, 70);

    ctx.fillStyle = '#ffaa00';
    ctx.font = 'bold 12px monospace';
    ctx.textAlign = 'center';
    ctx.fillText(data.name, cx, cy - 12);

    ctx.fillStyle = '#00e5ff';
    ctx.font = '10px monospace';
    ctx.fillText(data.ticker + ' · $' + data.last_px, cx, cy + 6);

    ctx.fillStyle = '#94a3b8';
    ctx.font = '9px monospace';
    ctx.fillText('Rev Q: ' + data.rev_quant + ' · R&D: ' + data.rd_quant, cx, cy + 22);

    ctx.restore();
  }

  // FXC Currency Rates Matrix (Screenshot 1)
  function renderFxcMatrix() {
    var tbody = document.getElementById('bmap_fxc_tbody');
    if (!tbody) return;
    tbody.innerHTML = '';

    fxcData.currencies.forEach(function(c, idx) {
      var tr = document.createElement('tr');
      var rateUSD = fxcData.rates.USD[idx] || 1.0;
      var chg = fxcData.changes.USD[idx] || 0.0;
      var isPos = chg >= 0;

      tr.innerHTML = 
        '<td style="font-size:14px;">' + c.flag + '</td>' +
        '<td style="color:#00e5ff;font-weight:bold;">' + c.code + '/USD</td>' +
        '<td style="color:#fff;">' + c.name + '</td>' +
        '<td style="color:#ffaa00;font-weight:bold;text-align:right;">' + rateUSD.toFixed(4) + '</td>' +
        '<td style="color:' + (isPos ? '#00e676' : '#ff3344') + ';text-align:right;">' + (isPos ? '+' : '') + (rateUSD * chg * 0.01).toFixed(4) + '</td>' +
        '<td style="background:' + (isPos ? 'rgba(0,230,118,0.25)' : 'rgba(255,51,68,0.25)') + ';color:' + (isPos ? '#00e676' : '#ff3344') + ';font-weight:bold;text-align:right;">' + (isPos ? '+' : '') + chg.toFixed(2) + '%</td>' +
        '<td style="color:#94a3b8;text-align:right;">' + (rateUSD * 1.002).toFixed(4) + '</td>' +
        '<td style="color:#94a3b8;text-align:right;">' + (rateUSD * 1.006).toFixed(4) + '</td>' +
        '<td style="color:#94a3b8;text-align:right;">' + (rateUSD * 1.024).toFixed(4) + '</td>' +
        '<td style="color:#64748b;font-size:9px;">' + (rateUSD * 0.94).toFixed(2) + ' - ' + (rateUSD * 1.08).toFixed(2) + '</td>';

      tbody.appendChild(tr);
    });
  }

  // GPC Technical Candlestick Chart (Screenshots 14, 15, 16)
  function initGpcCandlestickChart() {
    var canvas = document.getElementById('bmap_gpc_chart_canvas');
    if (!canvas || typeof Chart === 'undefined') return;

    var days = [];
    var closes = [];
    var base = 390.0;
    for (var i = 1; i <= 60; i++) {
      days.push('Day ' + i);
      base += (Math.sin(i * 0.3) * 2.5) + (Math.random() - 0.48) * 3;
      closes.push(parseFloat(base.toFixed(2)));
    }

    new Chart(canvas, {
      type: 'line',
      data: {
        labels: days,
        datasets: [{
          label: 'SPY US Equity Last Px',
          data: closes,
          borderColor: '#00e5ff',
          backgroundColor: 'rgba(0, 229, 255, 0.08)',
          borderWidth: 2,
          fill: true,
          tension: 0.15
        }]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
          legend: { labels: { color: '#ffaa00', font: { family: 'monospace', size: 11 } } }
        },
        scales: {
          x: { grid: { color: '#162438' }, ticks: { color: '#64748b', font: { family: 'monospace' } } },
          y: { grid: { color: '#162438' }, ticks: { color: '#94a3b8', font: { family: 'monospace' } } }
        }
      }
    });
  }

  // VOL 3D Implied Volatility Surface Canvas (Screenshots 13 & 17)
  function initVolSurfaceCanvas() {
    drawVolSurface();
  }

  function drawVolSurface() {
    var canvas = document.getElementById('bmapVolCanvas');
    if (!canvas) return;
    var ctx = canvas.getContext('2d');
    var w = canvas.width = canvas.parentElement.clientWidth;
    var h = canvas.height = canvas.parentElement.clientHeight || 550;

    ctx.clearRect(0, 0, w, h);

    // Render 3D Wireframe Volatility Mesh
    var rows = 18;
    var cols = 18;
    var cx = w / 2;
    var cy = h / 2 + 60;
    var rot = currentVolRot * (Math.PI / 180);

    ctx.save();
    ctx.lineWidth = 1.3;

    for (var r = 0; r < rows; r++) {
      for (var c = 0; c < cols; c++) {
        var x0 = (c - cols / 2) * 22;
        var z0 = (r - rows / 2) * 20;

        // Volatility smile formula (higher at deep OTM / ITM, smile shape)
        var moneyness = (c / cols - 0.5) * 2;
        var term = r / rows;
        var iv = 35 + (moneyness * moneyness) * 45 - (term * 10);

        var rx = x0 * Math.cos(rot) - z0 * Math.sin(rot);
        var rz = x0 * Math.sin(rot) + z0 * Math.cos(rot);
        var ry = -iv * 3.5 + rz * 0.35;

        var px = cx + rx;
        var py = cy + ry;

        // Color based on IV gradient: green to orange to red
        var color = iv > 55 ? '#ff3344' : (iv > 42 ? '#ffaa00' : '#00e676');
        ctx.strokeStyle = color;

        if (c < cols - 1) {
          var x1 = ((c + 1) - cols / 2) * 22;
          var m1 = ((c + 1) / cols - 0.5) * 2;
          var iv1 = 35 + (m1 * m1) * 45 - (term * 10);
          var rx1 = x1 * Math.cos(rot) - z0 * Math.sin(rot);
          var rz1 = x1 * Math.sin(rot) + z0 * Math.cos(rot);
          var ry1 = -iv1 * 3.5 + rz1 * 0.35;
          ctx.beginPath();
          ctx.moveTo(px, py);
          ctx.lineTo(cx + rx1, cy + ry1);
          ctx.stroke();
        }

        if (r < rows - 1) {
          var z2 = ((r + 1) - rows / 2) * 20;
          var term2 = (r + 1) / rows;
          var iv2 = 35 + (moneyness * moneyness) * 45 - (term2 * 10);
          var rx2 = x0 * Math.cos(rot) - z2 * Math.sin(rot);
          var rz2 = x0 * Math.sin(rot) + z2 * Math.cos(rot);
          var ry2 = -iv2 * 3.5 + rz2 * 0.35;
          ctx.beginPath();
          ctx.moveTo(px, py);
          ctx.lineTo(cx + rx2, cy + ry2);
          ctx.stroke();
        }
      }
    }

    // Grid labels
    ctx.fillStyle = '#ffaa00';
    ctx.font = 'bold 11px monospace';
    ctx.fillText('TERM (EXPIRY: 10 Mar 2023 ➔ 31 Dec 2032)', cx - 180, cy + 180);
    ctx.fillStyle = '#00e5ff';
    ctx.fillText('MONEYNESS (STRIKES: 80% ➔ 120%)', cx + 60, cy + 180);

    ctx.restore();
  }

  window.rotateVolSurface = function(delta) {
    currentVolRot += delta;
    drawVolSurface();
  };

  // ═══════════════════════════════════════════════════════════════

  // ===============================================================
  // -- REAL-TIME TICKER, VESSEL KINEMATICS, SECTORS & ACTIONS --
  // ===============================================================

  window.switchBmapTicker = function(tickerKey) {
    var presets = {
      SPY: { sym: 'SPY US $', last: 'C 404.190', chg: '+6.380', bidask: 'Z404.120 / 404.130P   11 x 1558', vol: '90,119,952', o: '399.710Z', h: '404.450B', l: '399.030T', val: '36.272B', isPos: true },
      AAPL: { sym: 'AAPL US $', last: '152.352', chg: '-1.478', bidask: '152.340 / 152.360   4 x 4', vol: '19,862,832', o: '153.700', h: '154.030', l: '151.780', val: '3.048B', isPos: false },
      TSLA: { sym: 'TSLA US $', last: '197.620', chg: '+7.150', bidask: '197.600 / 197.640   25 x 38', vol: '142,500,000', o: '191.000', h: '199.200', l: '189.500', val: '28.16B', isPos: true },
      LMT: { sym: 'LMT US $', last: '442.800', chg: '+3.100', bidask: '442.750 / 442.850   8 x 12', vol: '1,420,000', o: '440.000', h: '444.500', l: '439.200', val: '628.7M', isPos: true },
      BRENT: { sym: 'BRENT CRUDE ICE $', last: '82.450', chg: '+1.120', bidask: '82.440 / 82.460   100 x 100', vol: '245,000', o: '81.300', h: '83.100', l: '81.100', val: '20.2M', isPos: true },
      WTI: { sym: 'WTI CRUDE NYMEX $', last: '78.200', chg: '+0.950', bidask: '78.180 / 78.220   50 x 50', vol: '310,000', o: '77.200', h: '78.800', l: '77.050', val: '24.2M', isPos: true },
      POLYCAB: { sym: 'POLYCAB IN Rs', last: '5,124.50', chg: '+48.20', bidask: '5,122.00 / 5,126.00   15 x 20', vol: '420,000', o: '5,080.00', h: '5,145.00', l: '5,060.00', val: '2.15B INR', isPos: true },
      MPS: { sym: 'MPSLTD IN Rs', last: '1,842.00', chg: '+15.40', bidask: '1,840.00 / 1,844.00   5 x 8', vol: '85,000', o: '1,825.00', h: '1,855.00', l: '1,820.00', val: '156.5M INR', isPos: true }
    };
    var d = presets[tickerKey] || presets['SPY'];
    if (document.getElementById('bb_sym')) document.getElementById('bb_sym').textContent = d.sym;
    if (document.getElementById('bb_last')) {
      document.getElementById('bb_last').textContent = d.last;
      document.getElementById('bb_last').style.color = d.isPos ? '#00e676' : '#ff3344';
    }
    if (document.getElementById('bb_chg')) {
      document.getElementById('bb_chg').textContent = d.chg;
      document.getElementById('bb_chg').style.color = d.isPos ? '#00e676' : '#ff3344';
    }
    if (document.getElementById('bb_bidask')) document.getElementById('bb_bidask').textContent = d.bidask;
    if (document.getElementById('bb_vol')) document.getElementById('bb_vol').textContent = d.vol;
    if (document.getElementById('bb_open')) document.getElementById('bb_open').textContent = d.o;
    if (document.getElementById('bb_high')) document.getElementById('bb_high').textContent = d.h;
    if (document.getElementById('bb_low')) document.getElementById('bb_low').textContent = d.l;
    if (document.getElementById('bb_val')) document.getElementById('bb_val').textContent = d.val;
    if (document.getElementById('bb_active_ticker_select')) document.getElementById('bb_active_ticker_select').value = tickerKey;
  };

  window.unlockFollowVessel = function() {
    activeFollowVessel = null;
    var badge = document.getElementById('bmap_follow_badge');
    if (badge) badge.style.display = 'none';
  };

  window.toggleFollowActiveVessel = function() {
    if (activeFollowVessel) {
      window.unlockFollowVessel();
    } else if (globalVessels.length > 0) {
      selectActiveVessel(globalVessels[0]);
    }
  };

  window.zoomToActiveVessel = function() {
    if (activeFollowVessel && leafletMap) {
      leafletMap.setView([activeFollowVessel.lat, activeFollowVessel.lon], 12);
    }
  };

  window.toggleArpaVectors = function() {
    showArpaVectors = !showArpaVectors;
    redrawCanvasOverlay();
  };

  window.onBmapCountrySelect = function(code) {
    var coords = {
      ALL: { center: [20, 15], zoom: 3 },
      US: { center: [39.8, -98.5], zoom: 4 },
      CN: { center: [35.8, 104.1], zoom: 4 },
      IN: { center: [22.3, 78.9], zoom: 5 },
      SA: { center: [24.7, 46.7], zoom: 5 },
      AE: { center: [24.4, 54.3], zoom: 7 },
      DE: { center: [51.1, 10.4], zoom: 6 },
      GB: { center: [54.5, -2.4], zoom: 6 },
      JP: { center: [36.2, 138.2], zoom: 5 },
      SG: { center: [1.35, 103.8], zoom: 11 },
      EG: { center: [26.8, 30.8], zoom: 6 },
      BR: { center: [-14.2, -51.9], zoom: 4 },
      RU: { center: [61.5, 105.3], zoom: 3 },
      AU: { center: [-25.2, 133.7], zoom: 4 },
      ZA: { center: [-30.5, 22.9], zoom: 5 },
      ID: { center: [-0.78, 113.9], zoom: 5 },
      NG: { center: [9.08, 8.67], zoom: 6 }
    };
    var target = coords[code] || coords.ALL;
    if (leafletMap) leafletMap.flyTo(target.center, target.zoom, { duration: 1.2 });
  };

  window.onBmapSectorSelect = function(sectorKey) {
    if (sectorKey === 'ALL') {
      Object.keys(datasetLayerGroups).forEach(function(k) {
        if (!leafletMap.hasLayer(datasetLayerGroups[k])) {
          datasetLayerGroups[k].addTo(leafletMap);
          activeLayers[k] = true;
        }
      });
    } else {
      Object.keys(datasetLayerGroups).forEach(function(k) {
        if (k === sectorKey || (sectorKey === 'weather' && k === 'weather') || (sectorKey === 'bank_branches' && (k === 'bank_branches' || k === 'manhattan_branches'))) {
          if (!leafletMap.hasLayer(datasetLayerGroups[k])) {
            datasetLayerGroups[k].addTo(leafletMap);
            activeLayers[k] = true;
          }
        } else {
          if (leafletMap.hasLayer(datasetLayerGroups[k])) {
            leafletMap.removeLayer(datasetLayerGroups[k]);
            activeLayers[k] = false;
          }
        }
      });
    }
    renderDatasetSidebar();
    updateLegendsVisibility();
    redrawWeatherHeatmap();
    redrawCanvasOverlay();
  };

  window.handleBmapSearch = function(event) {
    if (event.key === 'Enter') {
      var query = event.target.value.trim().toUpperCase();
      if (!query) return;

      var tickers = ['SPY', 'AAPL', 'TSLA', 'LMT', 'BRENT', 'WTI', 'POLYCAB', 'MPS'];
      if (tickers.indexOf(query) >= 0) {
        window.switchBmapTicker(query);
        return;
      }

      var vMatch = globalVessels.find(function(v) {
        return v.name.toUpperCase().indexOf(query) >= 0 || (v.imo && String(v.imo) === query);
      });
      if (vMatch) {
        selectActiveVessel(vMatch);
        showUniversalVesselPopup(vMatch);
        leafletMap.flyTo([vMatch.lat, vMatch.lon], 9, { duration: 1.0 });
        return;
      }

      var bMatch = manhattanBranches.find(function(mb) {
        return mb.name.toUpperCase().indexOf(query) >= 0 || mb.address.toUpperCase().indexOf(query) >= 0;
      });
      if (bMatch) {
        setBmapTileLayer('satellite');
        leafletMap.flyTo([bMatch.lat, bMatch.lon], 17, { duration: 1.0 });
        showManhattanBranchPopup(bMatch);
        return;
      }

      var pMatch = crudePipelines.find(function(p) { return p.name.toUpperCase().indexOf(query) >= 0; });
      if (pMatch) {
        leafletMap.flyTo(pMatch.coords[0], 5, { duration: 1.0 });
        return;
      }

      alert('Terminal Search: Matched query "' + query + '" in Global Asset Catalog. Repositioning map.');
    }
  };

  window.selectVesselByQuery = function(query) {
    var vMatch = globalVessels.find(function(v) { return v.name.toUpperCase().indexOf(query.toUpperCase()) >= 0; });
    if (vMatch) {
      selectActiveVessel(vMatch);
      showUniversalVesselPopup(vMatch);
    }
  };


  // ===============================================================
  // ── AUTHENTIC TOP RIBBON SUGGESTED & NEW DATASETS DROPDOWNS ──
  // ===============================================================

  window.toggleSuggestedDropdown = function(e) {
    if (e) e.stopPropagation();
    var dd = document.getElementById('bmap_suggested_dropdown_menu');
    var newDd = document.getElementById('bmap_new_dropdown_menu');
    var actDd = document.getElementById('bmap_actions_dropdown');
    if (newDd) newDd.style.display = 'none';
    if (actDd) actDd.style.display = 'none';
    if (!dd) return;
    var isOpen = dd.style.display === 'block';
    dd.style.display = isOpen ? 'none' : 'block';
    if (!isOpen) {
      renderTopSuggestedList();
      setTimeout(function() {
        var inp = document.getElementById('top_suggested_search');
        if (inp) inp.focus();
      }, 50);
    }
  };

  window.toggleNewDropdown = function(e) {
    if (e) e.stopPropagation();
    var dd = document.getElementById('bmap_new_dropdown_menu');
    var suggDd = document.getElementById('bmap_suggested_dropdown_menu');
    var actDd = document.getElementById('bmap_actions_dropdown');
    if (suggDd) suggDd.style.display = 'none';
    if (actDd) actDd.style.display = 'none';
    if (!dd) return;
    var isOpen = dd.style.display === 'block';
    dd.style.display = isOpen ? 'none' : 'block';
    if (!isOpen) {
      renderTopNewList();
    }
  };

  window.renderTopSuggestedList = function(query) {
    var cont = document.getElementById('top_suggested_items_container');
    if (!cont) return;
    cont.innerHTML = '';
    var q = (query || '').toLowerCase().trim();

    SUGGESTED_DATASETS.forEach(function(ds) {
      if (q && ds.label.toLowerCase().indexOf(q) === -1 && ds.category.toLowerCase().indexOf(q) === -1) {
        return;
      }
      var isActive = !!activeLayers[ds.key];
      var row = document.createElement('div');
      row.style.cssText = 'display:flex;align-items:center;justify-content:space-between;padding:4px 6px;border-radius:3px;cursor:pointer;font-size:9.5px;transition:background 0.15s;' +
        (isActive ? 'background:#0f2438;border-left:2.5px solid #ffaa00;' : 'background:#080e18;border-left:2.5px solid transparent;') +
        'margin-bottom:2px;';
      
      row.innerHTML = 
        '<div style="display:flex;align-items:center;gap:6px;">' +
          '<span style="color:' + (ds.color || '#ffaa00') + ';font-size:10px;">●</span>' +
          '<span style="color:' + (isActive ? '#fff' : '#cbd5e1') + ';font-weight:' + (isActive ? '800' : '600') + ';">' + ds.label + '</span>' +
        '</div>' +
        '<div style="display:flex;align-items:center;gap:6px;">' +
          '<span style="color:#64748b;font-size:8.5px;">' + ds.count + '</span>' +
          '<button style="background:' + (isActive ? '#065f46' : '#1e334d') + ';color:' + (isActive ? '#34d399' : '#94a3b8') + ';border:1px solid ' + (isActive ? '#10b981' : '#334155') + ';border-radius:2px;padding:1px 5px;font-size:8.5px;font-weight:bold;cursor:pointer;">' +
            (isActive ? '✓ Active' : '+ Add') +
          '</button>' +
        '</div>';

      row.onclick = function() {
        toggleDatasetActive(ds.key);
        renderTopSuggestedList(query);
      };
      cont.appendChild(row);
    });
  };

  window.filterTopSuggestedList = function(q) {
    renderTopSuggestedList(q);
  };

  window.renderTopNewList = function() {
    var cont = document.getElementById('top_new_items_container');
    if (!cont) return;
    cont.innerHTML = '';

    NEW_DATASETS.forEach(function(ds) {
      var isActive = !!activeLayers[ds.key];
      var row = document.createElement('div');
      row.style.cssText = 'display:flex;align-items:center;justify-content:space-between;padding:4.5px 6px;border-radius:3px;cursor:pointer;font-size:9.5px;transition:background 0.15s;' +
        (isActive ? 'background:#082f49;border-left:2.5px solid #00e5ff;' : 'background:#080e18;border-left:2.5px solid transparent;') +
        'margin-bottom:2px;';

      row.innerHTML = 
        '<div style="display:flex;align-items:center;gap:6px;">' +
          '<span style="color:' + (ds.color || '#38bdf8') + ';font-size:10px;">●</span>' +
          '<span style="color:' + (isActive ? '#fff' : '#cbd5e1') + ';font-weight:' + (isActive ? '800' : '600') + ';">' + ds.label + '</span>' +
        '</div>' +
        '<div style="display:flex;align-items:center;gap:6px;">' +
          '<span style="color:#64748b;font-size:8.5px;">' + ds.count + '</span>' +
          '<button style="background:' + (isActive ? '#0284c7' : '#1e334d') + ';color:' + (isActive ? '#fff' : '#94a3b8') + ';border:1px solid ' + (isActive ? '#38bdf8' : '#334155') + ';border-radius:2px;padding:1px 5px;font-size:8.5px;font-weight:bold;cursor:pointer;">' +
            (isActive ? '✓ Active' : '+ Add') +
          '</button>' +
        '</div>';

      row.onclick = function() {
        toggleDatasetActive(ds.key);
        renderTopNewList();
      };
      cont.appendChild(row);
    });
  };

  // Close floating menus when clicking outside
  document.addEventListener('click', function(e) {
    var suggMenu = document.getElementById('bmap_suggested_dropdown_menu');
    var suggBtn = document.getElementById('btn_suggested_datasets_dropdown');
    var newMenu = document.getElementById('bmap_new_dropdown_menu');
    var newBtn = document.getElementById('btn_new_datasets_dropdown');
    var actMenu = document.getElementById('bmap_actions_dropdown');

    if (suggMenu && suggMenu.style.display === 'block' && !suggMenu.contains(e.target) && (!suggBtn || !suggBtn.contains(e.target))) {
      suggMenu.style.display = 'none';
    }
    if (newMenu && newMenu.style.display === 'block' && !newMenu.contains(e.target) && (!newBtn || !newBtn.contains(e.target))) {
      newMenu.style.display = 'none';
    }
  });

  window.toggleActionsDropdown = function() {
    var dd = document.getElementById('bmap_actions_dropdown');
    if (dd) dd.style.display = (dd.style.display === 'none' ? 'block' : 'none');
  };

  window.exportBmapGeoJSON = function() {
    var features = [];
    globalVessels.forEach(function(v) {
      features.push({
        type: 'Feature',
        geometry: { type: 'Point', coordinates: [v.lon, v.lat] },
        properties: { name: v.name, imo: v.imo, type: v.type, speed: v.speed, course: v.course, dest: v.dest }
      });
    });
    crudePipelines.forEach(function(p) {
      features.push({
        type: 'Feature',
        geometry: { type: 'LineString', coordinates: p.coords.map(function(c) { return [c[1], c[0]]; }) },
        properties: { name: p.name, company: p.company, capacity: p.capacity, status: p.status }
      });
    });
    var geojson = { type: 'FeatureCollection', features: features };
    var blob = new Blob([JSON.stringify(geojson, null, 2)], { type: 'application/json' });
    var url = URL.createObjectURL(blob);
    var a = document.createElement('a');
    a.href = url;
    a.download = 'Bloomberg_BMAP_Visible_Layers.geojson';
    a.click();
    if (document.getElementById('bmap_actions_dropdown')) document.getElementById('bmap_actions_dropdown').style.display = 'none';
  };

  window.exportBmapCSV = function() {
    var rows = ['ID,NAME,TYPE,LAT,LON,METRIC,STATUS'];
    globalVessels.forEach(function(v) {
      rows.push([v.id, '"' + v.name + '"', v.type, v.lat.toFixed(4), v.lon.toFixed(4), v.speed + ' kts', '"' + v.status + '"'].join(','));
    });
    var blob = new Blob([rows.join(String.fromCharCode(10))], { type: 'text/csv' });
    var url = URL.createObjectURL(blob);
    var a = document.createElement('a');
    a.href = url;
    a.download = 'Bloomberg_BMAP_Active_Assets.csv';
    a.click();
    if (document.getElementById('bmap_actions_dropdown')) document.getElementById('bmap_actions_dropdown').style.display = 'none';
  };

  window.setProximityAlertModal = function() {
    alert(['CPA / TCPA Proximity Alert Activated:', '', 'Monitoring Strait of Hormuz chokepoint fleet for Closest Point of Approach (CPA) < 1.0 Nautical Mile & Time to CPA (TCPA) < 15 minutes.'].join(String.fromCharCode(10)));
    if (document.getElementById('bmap_actions_dropdown')) document.getElementById('bmap_actions_dropdown').style.display = 'none';
  };

  window.resetBmapAllFilters = function() {
    resetBankFilter();
    resetVesselFilter();
    setBmapTileLayer('dark');
    if (document.getElementById('bmap_actions_dropdown')) document.getElementById('bmap_actions_dropdown').style.display = 'none';
    alert('Bloomberg BMAP Terminal: All spatial and telemetry filters reset to default constellation.');
  };

  window.toggleDistanceMeasurement = function() {
    alert(['Nautical Measurement Tool Enabled:', '', 'Click any two waypoints on the chart canvas to calculate Great Circle Nautical Distance (NM) and Estimated Days Steaming at 14.0 knots.'].join(String.fromCharCode(10)));
    if (document.getElementById('bmap_actions_dropdown')) document.getElementById('bmap_actions_dropdown').style.display = 'none';
  };

  // ── AUTO-INITIALIZATION ──
  // ═══════════════════════════════════════════════════════════════
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initLeafletBmap);
  } else {
    initLeafletBmap();
  }

})();
</script>
''')

    return "".join(code)

if __name__ == "__main__":
    js_content = generate_js_template()
    out_path = os.path.join(BASE_DIR, "bmap_js_template.js")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(js_content)
    print(f"Generated bmap_js_template.js successfully: {len(js_content)} bytes")

