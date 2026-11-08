# F:\documents\SOIC\EconAgent_Platform\platform_ui\build_rich_bmap_js.py
"""
Generates the comprehensive bmap_js_template.js containing:
- Injections of all datasets
- Canvas Heatmap Engine for Weather Cloud Cover & Temperature
- World Equity Markets choropleth
- Dynamic Map Content Sidebar Manager (Active Cards, Suggested 24, New 12, Basemap)
- Dynamic Floating Legends Manager
- Live AIS Kinematics & Trajectories (Greg Mortimer)
- Manhattan Satellite LOD & FDIC Bank Branches
- All Secondary Views (Berth Visits Table, GPC Chart, READ News, SPLC Network, FXC Matrix, VOL 3D Surface)
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

def build_js():
    js_parts = []

    # 1. Start IIFE and JSON data declarations
    js_parts.append("""<script>
(function() {
  // ═══════════════════════════════════════════════════════════════
  // ── DATA INJECTIONS FROM BLOOMBERG MAP DATASETS ──
  // ═══════════════════════════════════════════════════════════════
  var banksLookup = __BANKS_JSON__;
  var statesLookup = __STATES_JSON__;
  var typesLookup = __TYPES_JSON__;
  var branchesCompact = __BRANCHES_JSON__;

""")

    js_parts.append(f"  var crudePipelines = {json.dumps(CRUDE_PIPELINES)};\n")
    js_parts.append(f"  var gasPipelines = {json.dumps(GAS_PIPELINES_NAM)};\n")
    js_parts.append(f"  var berthVisits = {json.dumps(BERTH_VISITS)};\n")
    js_parts.append(f"  var manhattanBranches = {json.dumps(MANHATTAN_STREET_BRANCHES)};\n")
    js_parts.append(f"  var gregMortimer = {json.dumps(GREG_MORTIMER)};\n")
    js_parts.append(f"  var worldEquityData = {json.dumps(WORLD_EQUITY_DATA)};\n")
    js_parts.append(f"  var splcNetworks = {json.dumps(SPLC_NETWORKS)};\n")
    js_parts.append(f"  var fxcData = {json.dumps(FXC_DATA)};\n")
    js_parts.append(f"  var readNewsStories = {json.dumps(READ_NEWS_STORIES)};\n\n")

    js_parts.append(f"  var globalVessels = {json.dumps(gad.GLOBAL_AIS_VESSELS)};\n")
    js_parts.append(f"  var globalUtilities = {json.dumps(gad.GLOBAL_UTILITIES)};\n")
    js_parts.append(f"  var globalRefineries = {json.dumps(gad.GLOBAL_REFINERIES)};\n")
    js_parts.append(f"  var globalLng = {json.dumps(gad.GLOBAL_LNG_TERMINALS)};\n")
    js_parts.append(f"  var globalSeaports = {json.dumps(gad.GLOBAL_SEAPORTS)};\n")
    js_parts.append(f"  var globalSemiconductors = {json.dumps(gad.GLOBAL_SEMICONDUCTOR_FABS)};\n")
    js_parts.append(f"  var globalDataCenters = {json.dumps(gad.GLOBAL_DATA_CENTERS)};\n")
    js_parts.append(f"  var globalFinancialCenters = {json.dumps(gad.GLOBAL_FINANCIAL_CENTERS)};\n")
    js_parts.append(f"  var globalMining = {json.dumps(gad.GLOBAL_MINING_HUBS)};\n")
    js_parts.append(f"  var globalFertilizers = {json.dumps(gad.GLOBAL_FERTILIZER_PLANTS)};\n")
    js_parts.append(f"  var globalStorage = {json.dumps(gad.GLOBAL_STORAGE_TERMINALS)};\n")
    js_parts.append(f"  var globalGasHubs = {json.dumps(gad.GLOBAL_NATURAL_GAS_HUBS)};\n")
    js_parts.append(f"  var globalWeatherStations = {json.dumps(gad.GLOBAL_WEATHER_STATIONS)};\n")
    js_parts.append(f"  var globalEarthquakes = {json.dumps(gad.GLOBAL_SEISMIC_EARTHQUAKES)};\n")
    js_parts.append(f"  var globalCyclones = {json.dumps(gad.GLOBAL_CYCLONES)};\n")
    js_parts.append(f"  var globalDenseGrid = {json.dumps(gad.GLOBAL_DENSE_GRID)};\n\n")

    # Read the rest of the JS logic from a dedicated builder file
    return "".join(js_parts)

if __name__ == "__main__":
    prefix = build_js()
    print(f"Prefix generated: {len(prefix)} bytes")

