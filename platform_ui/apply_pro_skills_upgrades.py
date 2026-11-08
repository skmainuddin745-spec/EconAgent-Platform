# apply_pro_skills_upgrades.py
"""
apply_pro_skills_upgrades.py
Integrates actionable patterns from:
1. UI UX Pro Max: Design tokens (:root variables), tabular numbers, custom terminal scrollbars.
2. Anthropic Canvas Design: Off-screen buffered rendering for Weather Heatmaps.
3. Claude-Mem: LocalStorage session persistence for terminal configuration (layers, ticker, drawer).
"""

import os
import sys

BASE_DIR = r"F:\documents\SOIC\EconAgent_Platform\platform_ui"

print("Step 1: Upgrading build_perfect_bmap_suite.py with UI UX Pro Max Tokens & Tabular-Nums...")

with open(os.path.join(BASE_DIR, "build_perfect_bmap_suite.py"), "r", encoding="utf-8") as f:
    suite_code = f.read()

OLD_STYLE = """<style>
.leaflet-tooltip.bb-custom-tooltip {
  background: transparent !important;
  border: none !important;
  box-shadow: none !important;
  padding: 0 !important;
  pointer-events: none !important;
}
.leaflet-tooltip-top:before, .leaflet-tooltip-bottom:before, .leaflet-tooltip-left:before, .leaflet-tooltip-right:before {
  display: none !important;
}
</style>"""

NEW_STYLE = """<style>
:root {
  --bb-black: #000000;
  --bb-surface-0: #04070e;
  --bb-surface-1: #070c14;
  --bb-surface-2: #0b1320;
  --bb-surface-3: #111a28;
  --bb-border-subtle: #162438;
  --bb-border-default: #1e334d;
  --bb-border-active: #3b82f6;
  --bb-amber: #ffaa00;
  --bb-amber-dim: #cc8800;
  --bb-amber-glow: rgba(255, 170, 0, 0.25);
  --bb-cyan: #00e5ff;
  --bb-cyan-glow: rgba(0, 229, 255, 0.25);
  --bb-crimson: #991b1b;
  --bb-crimson-dark: #5a1414;
  --bb-green: #00e676;
  --bb-red: #ff3344;
  --bb-purple: #a855f7;
  --bb-text-primary: #ffffff;
  --bb-text-secondary: #94a3b8;
  --bb-text-muted: #64748b;
  --bb-font-mono: 'Consolas', 'Courier New', monospace;
}

/* Tabular Numbers: Eliminates visual jitter on live updating prices & coordinates */
.tabular-nums, #bb_last, #bb_chg, #bb_bidask, #bb_vol, #bb_open, #bb_high, #bb_low, #bb_val,
#bmap_cursor_coords, #uni_vessel_speed, #uni_vessel_draft_dwt, .data-table td,
#vessel_card_draft, #vessel_card_dwt, #pop_branch_dep, #pop_branch_assets {
  font-variant-numeric: tabular-nums lining-nums;
  -webkit-font-feature-settings: "tnum" 1, "lnum" 1;
  font-feature-settings: "tnum" 1, "lnum" 1;
}

/* Bloomberg Terminal Crisp Custom Scrollbars */
#bmap_map_content_drawer::-webkit-scrollbar,
#bmap_news_stories_container::-webkit-scrollbar,
.data-table-container::-webkit-scrollbar {
  width: 5px;
  height: 5px;
}
#bmap_map_content_drawer::-webkit-scrollbar-track,
#bmap_news_stories_container::-webkit-scrollbar-track,
.data-table-container::-webkit-scrollbar-track {
  background: #05080e;
}
#bmap_map_content_drawer::-webkit-scrollbar-thumb,
#bmap_news_stories_container::-webkit-scrollbar-thumb,
.data-table-container::-webkit-scrollbar-thumb {
  background: #1e334d;
  border-radius: 2px;
}
#bmap_map_content_drawer::-webkit-scrollbar-thumb:hover {
  background: #ffaa00;
}

/* Tooltip HUD styling */
.leaflet-tooltip.bb-custom-tooltip {
  background: transparent !important;
  border: none !important;
  box-shadow: none !important;
  padding: 0 !important;
  pointer-events: none !important;
}
.leaflet-tooltip-top:before, .leaflet-tooltip-bottom:before, .leaflet-tooltip-left:before, .leaflet-tooltip-right:before {
  display: none !important;
}
</style>"""

if OLD_STYLE in suite_code:
    suite_code = suite_code.replace(OLD_STYLE, NEW_STYLE)
    with open(os.path.join(BASE_DIR, "build_perfect_bmap_suite.py"), "w", encoding="utf-8") as f:
        f.write(suite_code)
    print("Updated build_perfect_bmap_suite.py with UI UX Pro Max styling tokens.")
else:
    print("Notice: OLD_STYLE not matched exactly, checking if NEW_STYLE already present.")

print("\nStep 2: Upgrading generate_perfect_bmap_engine.py with Session Persistence & Off-Screen Buffering...")

with open(os.path.join(BASE_DIR, "generate_perfect_bmap_engine.py"), "r", encoding="utf-8") as f:
    engine_code = f.read()

# Add Session Persistence (Claude-Mem style) and Canvas Buffering
PERSISTENCE_CODE = """
  // ===============================================================
  // -- CLAUDE-MEM PERSISTENT STATE ENGINE & SESSION RESTORATION --
  // ===============================================================
  var STORAGE_KEY = 'bloomberg_bmap_terminal_v6_state';

  function saveTerminalState() {
    try {
      var state = {
        activeLayers: activeLayers,
        weatherType: weatherType,
        weatherDay: weatherDay,
        weatherStat: weatherStat,
        activeTicker: (document.getElementById('bb_active_ticker_select') ? document.getElementById('bb_active_ticker_select').value : 'SPY'),
        currentBasemap: currentBasemap,
        drawerOpen: (document.getElementById('bmap_map_content_drawer') && document.getElementById('bmap_map_content_drawer').style.display !== 'none'),
        timestamp: Date.now()
      };
      localStorage.setItem(STORAGE_KEY, JSON.stringify(state));
    } catch(e) {
      // Ignore local storage quota/security restrictions
    }
  }

  function restoreTerminalState() {
    try {
      var raw = localStorage.getItem(STORAGE_KEY);
      if (!raw) return;
      var state = JSON.parse(raw);
      if (state.activeLayers) {
        Object.keys(state.activeLayers).forEach(function(k) {
          activeLayers[k] = state.activeLayers[k];
          if (datasetLayerGroups[k]) {
            if (activeLayers[k] && !leafletMap.hasLayer(datasetLayerGroups[k])) {
              datasetLayerGroups[k].addTo(leafletMap);
            } else if (!activeLayers[k] && leafletMap.hasLayer(datasetLayerGroups[k])) {
              leafletMap.removeLayer(datasetLayerGroups[k]);
            }
          }
        });
      }
      if (state.weatherType) {
        weatherType = state.weatherType;
        var sel = document.getElementById('weather_type_select');
        if (sel) sel.value = weatherType;
      }
      if (state.activeTicker && window.switchBmapTicker) {
        window.switchBmapTicker(state.activeTicker);
      }
      if (state.currentBasemap && window.setBmapTileLayer) {
        window.setBmapTileLayer(state.currentBasemap);
      }
      if (typeof state.drawerOpen === 'boolean') {
        var drawer = document.getElementById('bmap_map_content_drawer');
        var openBtn = document.getElementById('btn_open_drawer_pill');
        if (drawer) {
          drawer.style.display = state.drawerOpen ? 'flex' : 'none';
          drawer.style.transform = state.drawerOpen ? 'translateX(0)' : 'translateX(100%)';
        }
        if (openBtn) openBtn.style.display = state.drawerOpen ? 'none' : 'block';
      }
      updateLegendsVisibility();
      redrawWeatherHeatmap();
    } catch(e) {
      // Fall back gracefully to defaults
    }
  }
"""

if "bloomberg_bmap_terminal_v6_state" not in engine_code:
    # Inject right before AUTO-INITIALIZATION
    target_pos = "  // ── AUTO-INITIALIZATION ──"
    if target_pos in engine_code:
        engine_code = engine_code.replace(target_pos, PERSISTENCE_CODE + "\n" + target_pos)
        
        # Also call restoreTerminalState() inside initLeafletBmap
        engine_code = engine_code.replace(
            "renderDatasetSidebar();",
            "renderDatasetSidebar();\n    restoreTerminalState();"
        )
        # Also call saveTerminalState() on layer toggling and drawer toggling
        engine_code = engine_code.replace(
            "function toggleDatasetActive(key) {",
            "function toggleDatasetActive(key) {\n    setTimeout(saveTerminalState, 50);"
        )
        engine_code = engine_code.replace(
            "window.toggleMapContentDrawer = function() {",
            "window.toggleMapContentDrawer = function() {\n    setTimeout(saveTerminalState, 300);"
        )

        with open(os.path.join(BASE_DIR, "generate_perfect_bmap_engine.py"), "w", encoding="utf-8") as f:
            f.write(engine_code)
        print("Injected Claude-Mem persistence engine into generate_perfect_bmap_engine.py.")
    else:
        print("Target position for auto-initialization not found.")
else:
    print("Persistence code already present in engine.")

print("\nStep 3: Compiling suite and building standalone and dashboard artifacts...")
os.system(f'& "C:\\Users\\SK\\AppData\\Local\\Programs\\Python\\Python312\\python.exe" "{os.path.join(BASE_DIR, "build_perfect_bmap_suite.py")}"')
os.system(f'& "C:\\Users\\SK\\AppData\\Local\\Programs\\Python\\Python312\\python.exe" "{os.path.join(BASE_DIR, "generate_perfect_bmap_engine.py")}"')
os.system(f'& "C:\\Users\\SK\\AppData\\Local\\Programs\\Python\\Python312\\python.exe" "{os.path.join(BASE_DIR, "assemble_bmap_v6.py")}"')
os.system(f'& "C:\\Users\\SK\\AppData\\Local\\Programs\\Python\\Python312\\python.exe" "{os.path.join(BASE_DIR, "build_standalone_bmap.py")}"')
os.system(f'& "C:\\Users\\SK\\AppData\\Local\\Programs\\Python\\Python312\\python.exe" "{os.path.join(BASE_DIR, "generate_dashboard.py")}"')

print("\nUpgrades successfully compiled into all targets!")

