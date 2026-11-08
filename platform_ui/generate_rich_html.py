# F:\documents\SOIC\EconAgent_Platform\platform_ui\generate_rich_html.py
import os

BASE_DIR = r"F:\documents\SOIC\EconAgent_Platform\platform_ui"

def generate_html():
    html = """
    <!-- ── AUTHENTIC BLOOMBERG TERMINAL TOP WINDOW TABS & NAVIGATION (SCREENSHOTS 4 & 27) ── -->
    <div style="background: #000; border: 1px solid #1a2736; border-radius: 6px 6px 0 0; padding: 4px 10px; font-family: var(--font-mono); font-size: 11px;">
      
      <!-- Window Tabs Bar -->
      <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #162438; padding-bottom: 4px; margin-bottom: 4px;">
        <div style="display: flex; align-items: center; gap: 4px;">
          <div style="background: #0d1726; color: #94a3b8; border: 1px solid #1e334d; padding: 2px 8px; border-radius: 3px 3px 0 0; font-size: 10px; cursor: pointer;" onclick="switchBmapTicker('SPY')">GPC SPDR S&amp;P 500 ETF Equity</div>
          <div style="background: #1e3a5f; color: #00e5ff; border: 1px solid #3b82f6; border-bottom: none; padding: 2px 10px; border-radius: 3px 3px 0 0; font-size: 10px; font-weight: 800; display: flex; align-items: center; gap: 6px;">
            <span>MAP Custom Map</span>
            <span style="font-size: 9px; cursor: pointer;" onclick="alert('Default Map Locked');">✕</span>
          </div>
          <div style="background: #0d1726; color: #94a3b8; border: 1px solid #1e334d; padding: 2px 8px; border-radius: 3px 3px 0 0; font-size: 10px; cursor: pointer;" onclick="switchBmapView('fxc')">FXC Currency Rates Matrix</div>
          <div style="background: #0d1726; color: #94a3b8; border: 1px solid #1e334d; padding: 2px 8px; border-radius: 3px 3px 0 0; font-size: 10px; cursor: pointer;" onclick="switchBmapView('splc')">SPLC Supply Chain Analysis</div>
          <div style="background: #0d1726; color: #94a3b8; border: 1px solid #1e334d; padding: 2px 8px; border-radius: 3px 3px 0 0; font-size: 10px; cursor: pointer;" onclick="switchBmapView('vol')">VOL 3D Volatility Surface</div>
          <div style="background: #0d1726; color: #64748b; border: 1px solid #1e334d; padding: 2px 6px; border-radius: 3px; font-size: 10px; cursor: pointer;" onclick="alert('New Launchpad Window Added');">+</div>
        </div>
        <div style="display: flex; align-items: center; gap: 10px; color: #64748b; font-size: 10.5px;">
          <span style="cursor: pointer;">Options</span>
          <span>_</span>
          <span>□</span>
          <span style="color: #ef4444; cursor: pointer;">✕</span>
        </div>
      </div>

      <!-- Navigation & Security Select Sub-bar -->
      <div style="display: flex; justify-content: space-between; align-items: center; padding: 2px 0 4px 0; border-bottom: 1px solid #162438; font-size: 10.5px;">
        <div style="display: flex; align-items: center; gap: 8px;">
          <span style="color: #64748b; cursor: pointer;">&lt; &gt;</span>
          <span style="color: #334155;">|</span>
          <select id="bb_active_ticker_select" onchange="switchBmapTicker(this.value)" style="background: #080e18; color: #ffaa00; border: 1px solid #203a5e; border-radius: 3px; padding: 2px 6px; font-size: 10.5px; font-weight: 700; font-family: var(--font-mono); outline: none; cursor: pointer;">
            <option value="SPY">SPDR S&amp;P 500 ETF Equity ▾</option>
            <option value="AAPL">APPLE INC Equity ▾</option>
            <option value="TSLA">TESLA INC Equity ▾</option>
            <option value="LMT">LOCKHEED MARTIN CORP Equity ▾</option>
            <option value="BRENT">BRENT CRUDE OIL ICE ▾</option>
            <option value="WTI">WTI CRUDE NYMEX ▾</option>
            <option value="POLYCAB">POLYCAB INDIA LTD Equity ▾</option>
            <option value="MPS">MPS LIMITED Equity ▾</option>
          </select>
          <span style="color: #94a3b8; cursor: pointer;">MAP ▾</span>
          <span style="color: #94a3b8; cursor: pointer;" onclick="alert('Related Functions: DES, HP, FA, CN, SPLC, FXC, VOL, PORT, CORR, BMAP');">Related Functions Menu ▾</span>
        </div>
        <div style="display: flex; align-items: center; gap: 8px; color: #94a3b8;">
          <span style="cursor: pointer;">✉ Message</span>
          <span style="color: #334155;">|</span>
          <span style="color: #ffaa00;">● LIVE</span>
        </div>
      </div>

      <!-- Bloomberg Live Financial Quote Bar (Exact Screenshot 4) -->
      <div style="display: flex; justify-content: space-between; align-items: baseline; padding: 4px 0 2px 0; flex-wrap: wrap; gap: 8px;">
        <div style="display: flex; align-items: baseline; gap: 10px;">
          <strong style="color: #ffaa00; font-size: 13px;" id="bb_sym">SPY US $</strong>
          <span style="color: #00e676; font-size: 14px; font-weight: 900;" id="bb_last">C 404.190</span>
          <span style="color: #00e676; font-size: 12px; font-weight: 700;" id="bb_chg">+6.380</span>
          <span style="color: #fff; font-size: 11px; margin-left: 8px;" id="bb_bidask">Z404.120 / 404.130P &nbsp; 11 × 1558</span>
        </div>
        <div style="display: flex; align-items: center; gap: 10px; font-size: 10.5px; color: #94a3b8;">
          <span style="background: #ffaa00; color: #000; font-weight: 900; padding: 1px 4px; border-radius: 2px; font-size: 9px;">■</span>
          <span>On <strong style="color: #fff;" id="bb_date">03 Mar d</strong></span>
          <span>Vol <strong style="color: #fff;" id="bb_vol">90,119,952</strong></span>
          <span>O <strong style="color: #fff;" id="bb_open">399.710Z</strong></span>
          <span>H <strong style="color: #fff;" id="bb_high">404.450B</strong></span>
          <span>L <strong style="color: #fff;" id="bb_low">399.030T</strong></span>
          <span>Val <strong style="color: #fff;" id="bb_val">36.272B</strong></span>
        </div>
      </div>
    </div>

    <!-- ── AUTHENTIC BLOOMBERG TERMINAL CRIMSON HEADER RIBBON (SCREENSHOTS 4, 12, 27) ── -->
    <div style="background: linear-gradient(180deg, #781c1c 0%, #5a1414 100%); border: 1px solid #991b1b; border-bottom: 2px solid #b91c1c; padding: 5px 12px; display: flex; justify-content: space-between; align-items: center; font-family: var(--font-mono); font-size: 11px;">
      <div style="display: flex; align-items: center; gap: 10px;">
        <span style="background: #111a28; color: #ffaa00; font-weight: 900; padding: 2px 7px; border-radius: 2px; font-size: 10.5px; border: 1px solid #ffaa00; cursor: pointer;" onclick="document.getElementById('bmap_universal_search').focus();">&lt;Search&gt;</span>
        <button id="btn_browse_datasets" onclick="toggleMapContentDrawer()" style="background: #991b1b; color: #fff; border: 1px solid #dc2626; padding: 3px 10px; font-size: 10.5px; font-weight: 800; border-radius: 3px; cursor: pointer; display: flex; align-items: center; gap: 5px;">
          <span>Browse Datasets</span>
        </button>
        <div style="position: relative; display: inline-block;">
          <button onclick="toggleActionsDropdown()" style="background: #450a0a; color: #fca5a5; border: 1px solid #7f1d1d; padding: 3px 10px; font-size: 10.5px; font-weight: 700; border-radius: 3px; cursor: pointer;">
            Actions ▾
          </button>
          <div id="bmap_actions_dropdown" style="display: none; position: absolute; top: 100%; left: 0; margin-top: 4px; background: #0b1320; border: 1px solid #203a5e; border-radius: 4px; box-shadow: 0 8px 24px rgba(0,0,0,0.8); z-index: 2000; min-width: 230px; font-family: var(--font-mono);">
            <div onclick="exportBmapGeoJSON()" style="padding: 7px 12px; color: #00e5ff; cursor: pointer; border-bottom: 1px solid #142338; font-size: 10px;">📥 Export Visible Layers (GeoJSON)</div>
            <div onclick="exportBmapCSV()" style="padding: 7px 12px; color: #ffaa00; cursor: pointer; border-bottom: 1px solid #142338; font-size: 10px;">📊 Export Active Assets (CSV)</div>
            <div onclick="setProximityAlertModal()" style="padding: 7px 12px; color: #ff3344; cursor: pointer; border-bottom: 1px solid #142338; font-size: 10px;">⚠️ Set CPA Proximity Collision Alert</div>
            <div onclick="resetBmapAllFilters()" style="padding: 7px 12px; color: #94a3b8; cursor: pointer; border-bottom: 1px solid #142338; font-size: 10px;">🔄 Reset Map &amp; Clear Filters</div>
            <div onclick="toggleDistanceMeasurement()" style="padding: 7px 12px; color: #34d399; cursor: pointer; font-size: 10px;">📐 Measure Nautical Distance (NM)</div>
          </div>
        </div>
      </div>
      <div style="display: flex; align-items: center; gap: 12px;">
        <span style="color: #fca5a5; font-size: 10.5px; display: flex; align-items: center; gap: 4px;">
          <span>G 325: Pipelines ⤢ ▾</span>
        </span>
        <span style="color: #fff; font-size: 11px; font-weight: 700; display: flex; align-items: center; gap: 4px; cursor: pointer;" onclick="alert('Custom Map Workspace Synced');">
          <span>⤢</span> Custom Map
        </span>
      </div>
    </div>

    <!-- ── SECONDARY SUB-TOOLBAR (VIEWS, SEARCH, TOOLS, REGIONAL PRESETS) ── -->
    <div style="background: #090e18; border: 1px solid #1e2e44; border-top: none; padding: 5px 12px; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 8px; font-family: var(--font-mono);">
      <!-- View Mode Buttons -->
      <div style="display: flex; align-items: center; gap: 2px;">
        <button id="bmap_btn_view_map" onclick="switchBmapView('map')" style="background: #1e3a5f; color: #00e5ff; border: 1px solid #3b82f6; border-bottom: 2px solid #00e5ff; padding: 3px 9px; font-size: 10px; font-weight: 800; border-radius: 2px; cursor: pointer;">Map</button>
        <button id="bmap_btn_view_table" onclick="switchBmapView('table')" style="background: #0d1624; color: #94a3b8; border: 1px solid #1c2e44; padding: 3px 9px; font-size: 10px; font-weight: 700; border-radius: 2px; cursor: pointer;">Table (Berths/FDIC)</button>
        <button id="bmap_btn_view_chart" onclick="switchBmapView('chart')" style="background: #0d1624; color: #94a3b8; border: 1px solid #1c2e44; padding: 3px 9px; font-size: 10px; font-weight: 700; border-radius: 2px; cursor: pointer;">Chart (GPC)</button>
        <button id="bmap_btn_view_news" onclick="switchBmapView('news')" style="background: #0d1624; color: #94a3b8; border: 1px solid #1c2e44; padding: 3px 9px; font-size: 10px; font-weight: 700; border-radius: 2px; cursor: pointer;">News (READ)</button>
        <button id="bmap_btn_view_splc" onclick="switchBmapView('splc')" style="background: #0d1624; color: #94a3b8; border: 1px solid #1c2e44; padding: 3px 9px; font-size: 10px; font-weight: 700; border-radius: 2px; cursor: pointer;">SPLC Supply Chain</button>
        <button id="bmap_btn_view_fxc" onclick="switchBmapView('fxc')" style="background: #0d1624; color: #94a3b8; border: 1px solid #1c2e44; padding: 3px 9px; font-size: 10px; font-weight: 700; border-radius: 2px; cursor: pointer;">FXC Currency Matrix</button>
        <button id="bmap_btn_view_vol" onclick="switchBmapView('vol')" style="background: #0d1624; color: #94a3b8; border: 1px solid #1c2e44; padding: 3px 9px; font-size: 10px; font-weight: 700; border-radius: 2px; cursor: pointer;">VOL 3D Surface</button>
      </div>

      <!-- Universal Search with Live Autocomplete -->
      <div style="position: relative; display: flex; align-items: center;">
        <span style="position: absolute; left: 8px; color: #64748b; font-size: 10px;">🔍</span>
        <input type="text" id="bmap_universal_search" oninput="handleBmapUniversalSearch(this.value)" placeholder="Add Securities, Data, Locations, WKT, etc." style="background: #060b13; color: #fff; border: 1px solid #253e61; border-radius: 4px; padding: 4px 10px 4px 26px; font-size: 10.5px; font-family: var(--font-mono); width: 240px; outline: none;">
        <div id="bmap_search_results_box" style="display: none; position: absolute; top: 100%; left: 0; right: 0; margin-top: 3px; background: #090f1a; border: 1px solid #203a5e; border-radius: 4px; box-shadow: 0 10px 30px rgba(0,0,0,0.9); z-index: 2100; max-height: 280px; overflow-y: auto;"></div>
      </div>

      <!-- Quick Action Tools matching Screenshots -->
      <div style="display: flex; align-items: center; gap: 6px;">
        <button onclick="toggleDistanceMeasurement()" id="btn_draw_measure" style="background: #111e30; color: #cbd5e1; border: 1px solid #1e334d; padding: 3px 8px; font-size: 10px; border-radius: 2px; cursor: pointer;">Δ Draw</button>
        <span style="color: #64748b; cursor: pointer;">&gt;&gt;</span>
        <button onclick="toggleMapContentDrawer()" style="background: #111e30; color: #ffaa00; border: 1px solid #1e334d; padding: 3px 8px; font-size: 10px; font-weight: 700; border-radius: 2px; cursor: pointer;">Map Content</button>
      </div>

      <!-- Strategic Regional Presets -->
      <div style="display: flex; align-items: center; gap: 4px; flex-wrap: wrap;">
        <span style="color: #64748b; font-size: 9px;">PRESETS:</span>
        <button onclick="jumpToBmapPreset('manhattan')" class="action-btn" style="background: #0284c7; color: #fff; border: 1px solid #38bdf8; padding: 2px 6px; font-size: 9px; font-weight: 800; border-radius: 3px; cursor: pointer;">🏢 Manhattan (Street Satellite)</button>
        <button onclick="jumpToBmapPreset('crude_pipelines')" class="action-btn" style="background: #1e3a5f; color: #38bdf8; border: 1px solid #2563eb; padding: 2px 6px; font-size: 9px; font-weight: 800; border-radius: 3px; cursor: pointer;">🛢️ Global Pipelines (Image 27)</button>
        <button onclick="jumpToBmapPreset('world_equity')" class="action-btn" style="background: #064e3b; color: #34d399; border: 1px solid #059669; padding: 2px 6px; font-size: 9px; font-weight: 800; border-radius: 3px; cursor: pointer;">🌍 Equity Heatmap (Image 4)</button>
        <button onclick="jumpToBmapPreset('weather')" class="action-btn" style="background: #374151; color: #cbd5e1; border: 1px solid #4b5563; padding: 2px 6px; font-size: 9px; font-weight: 800; border-radius: 3px; cursor: pointer;">⛅ Weather (Image 2)</button>
        <button onclick="jumpToBmapPreset('bank_branches')" class="action-btn" style="background: #0f2e4a; color: #38bdf8; border: 1px solid #0284c7; padding: 2px 6px; font-size: 9px; font-weight: 800; border-radius: 3px; cursor: pointer;">🏛️ US Banks (FDIC)</button>
        <button onclick="jumpToBmapPreset('hormuz')" class="action-btn" style="background: #451a03; color: #fbbf24; border: 1px solid #b45309; padding: 2px 6px; font-size: 9px; font-weight: 800; border-radius: 3px; cursor: pointer;">🔥 Hormuz (Real Time)</button>
        <button onclick="jumpToBmapPreset('greg_mortimer')" class="action-btn" style="background: #312e81; color: #a5b4fc; border: 1px solid #6366f1; padding: 2px 6px; font-size: 9px; font-weight: 800; border-radius: 3px; cursor: pointer;">🚢 Greg Mortimer (Image 8)</button>
        <button onclick="jumpToBmapPreset('world')" class="action-btn" style="background: #16253b; color: #fff; border: 1px solid #2a4365; padding: 2px 6px; font-size: 9px; border-radius: 3px; cursor: pointer;">🌐 World</button>
      </div>
    </div>

    <!-- ═══════════════════════════════════════════════════════════════ -->
    <!-- ── PRIMARY VIEW 1: INTERACTIVE MAP & FLOATING PARAMETER CARDS ── -->
    <!-- ═══════════════════════════════════════════════════════════════ -->
    <div id="bmap_view_container_map" style="display: block;">
      <div id="bmap_map_wrapper" style="position: relative; width: 100%; height: 720px; background: #000; border: 1px solid #1e2e44; border-top: none; overflow: hidden;">
        
        <!-- Leaflet Map Container -->
        <div id="bmap_leaflet_map" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; z-index: 1; background: #04070e;"></div>

        <!-- HTML5 Canvas Overlay for Splines & Dynamic Telemetry -->
        <canvas id="bmapCanvas" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; z-index: 2; pointer-events: none;"></canvas>

        <!-- Top Left View Bar -->
        <div style="position: absolute; top: 12px; left: 14px; z-index: 50; display: flex; gap: 8px; flex-wrap: wrap; align-items: center; font-family: var(--font-mono);">
          <div style="background: rgba(5,8,15,0.92); border: 1px solid #223750; border-radius: 4px; padding: 4px 10px; font-size: 10px; color: #00e5ff; display: flex; align-items: center; gap: 6px; box-shadow: 0 4px 12px rgba(0,0,0,0.6);">
            <span>VIEW:</span>
            <strong id="bmap_scope_label" style="color: #ffaa00;">GLOBAL MARITIME, PIPELINE &amp; BANKING RADAR</strong>
            <span style="color: #334155;">|</span>
            <span id="bmap_objects_count_badge" style="color: #94a3b8;">1,675 FDIC Branches Active</span>
            <span style="color: #334155;">|</span>
            <span id="bmap_cursor_coords" style="color: #64748b;">WGS84: 38.5000° N, 96.5000° W</span>
          </div>

          <div style="display: flex; gap: 4px; background: rgba(5,8,15,0.92); border: 1px solid #223750; border-radius: 4px; padding: 2px;">
            <button onclick="setBmapTileLayer('dark')" id="bmap_layer_dark" class="action-btn active" style="font-size: 9px; padding: 3px 6px;">🌑 Bloomberg Dark</button>
            <button onclick="setBmapTileLayer('satellite')" id="bmap_layer_sat" class="action-btn" style="font-size: 9px; padding: 3px 6px;">🛰️ Real Satellite</button>
            <button onclick="setBmapTileLayer('nautical')" id="bmap_layer_naut" class="action-btn" style="font-size: 9px; padding: 3px 6px;">🗺️ Nautical Chart</button>
            <button onclick="setBmapTileLayer('auto')" id="bmap_layer_auto" class="action-btn" style="font-size: 9px; padding: 3px 6px;">🌐 Auto-Adaptive</button>
          </div>
        </div>

        <!-- Reopen Map Content Pill (When Drawer is closed) -->
        <button id="btn_open_drawer_pill" onclick="toggleMapContentDrawer()" style="display: none; position: absolute; top: 12px; right: 14px; z-index: 100; background: #991b1b; color: #fff; border: 1px solid #dc2626; border-radius: 4px; padding: 5px 12px; font-size: 11px; font-weight: 800; font-family: var(--font-mono); cursor: pointer; box-shadow: 0 4px 14px rgba(0,0,0,0.8);">
          Map Content (29 Datasets)
        </button>

        <!-- ── AUTHENTIC RIGHT-HAND "MAP CONTENT" DRAWER (MATCHING SCREENSHOTS 4, 27) ── -->
        <div id="bmap_map_content_drawer" style="position: absolute; right: 0; top: 0; bottom: 0; width: 285px; z-index: 120; background: rgba(7, 12, 20, 0.96); backdrop-filter: blur(10px); border-left: 1px solid #1f3554; display: flex; flex-direction: column; font-family: var(--font-mono); box-shadow: -8px 0 24px rgba(0,0,0,0.8); transition: transform 0.25s cubic-bezier(0.4, 0, 0.2, 1);">
          
          <!-- Drawer Header -->
          <div style="background: #0d1726; border-bottom: 1px solid #1e334d; padding: 8px 12px; display: flex; justify-content: space-between; align-items: center;">
            <div style="display: flex; align-items: center; gap: 6px;">
              <span style="color: #ffaa00; font-size: 11px; font-weight: 900;">Map Content</span>
              <span id="active_dataset_count_pill" style="background: #1e3a5f; color: #38bdf8; font-size: 9px; padding: 1px 5px; border-radius: 10px; font-weight: 700;">3 Active</span>
            </div>
            <button onclick="toggleMapContentDrawer()" style="background: transparent; color: #94a3b8; border: none; font-size: 13px; cursor: pointer; font-weight: 700;">✕</button>
          </div>

          <!-- Drawer Search Box -->
          <div style="padding: 6px 10px; border-bottom: 1px solid #162438;">
            <input type="text" id="dataset_filter_input" oninput="filterDatasetSidebar(this.value)" placeholder="Filter datasets..." style="width: 100%; background: #05080e; color: #fff; border: 1px solid #1c2e44; border-radius: 3px; padding: 4px 8px; font-size: 10px; font-family: var(--font-mono); outline: none;">
          </div>

          <!-- Scrollable Datasets Area (Exact Match Screenshot 4 & 27) -->
          <div style="flex: 1; overflow-y: auto; padding: 6px 10px;">
            
            <!-- GROUP 1: SUGGESTED DATASETS (SCREENSHOT 4 & 27 LIST) -->
            <div style="margin-bottom: 12px;">
              <div style="color: #fff; font-size: 10px; font-weight: 800; margin-bottom: 6px; display: flex; align-items: center; gap: 4px;">
                <span>▾</span> Suggested Datasets
              </div>
              <div id="suggested_datasets_list" style="display: flex; flex-direction: column; gap: 2px;"></div>
            </div>

            <!-- GROUP 2: NEW DATASETS (SCREENSHOT 4 & 27 LIST) -->
            <div style="margin-bottom: 12px;">
              <div style="color: #38bdf8; font-size: 10px; font-weight: 800; margin-bottom: 6px; display: flex; align-items: center; gap: 4px;">
                <span>▾</span> New Datasets
              </div>
              <div id="new_datasets_list" style="display: flex; flex-direction: column; gap: 2px;"></div>
            </div>

          </div>

          <!-- Drawer Footer: Basemap Selector -->
          <div style="background: #0a111e; border-top: 1px solid #1e334d; padding: 8px 12px;">
            <div style="color: #94a3b8; font-size: 9.5px; font-weight: 700; margin-bottom: 4px;">BASEMAP</div>
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 4px;">
              <button onclick="setBmapTileLayer('dark')" style="background: #111b2b; color: #ffaa00; border: 1px solid #1e334d; padding: 3px; font-size: 9px; border-radius: 2px; cursor: pointer;">Bloomberg Dark</button>
              <button onclick="setBmapTileLayer('satellite')" style="background: #111b2b; color: #38bdf8; border: 1px solid #1e334d; padding: 3px; font-size: 9px; border-radius: 2px; cursor: pointer;">Real Satellite</button>
              <button onclick="setBmapTileLayer('nautical')" style="background: #111b2b; color: #34d399; border: 1px solid #1e334d; padding: 3px; font-size: 9px; border-radius: 2px; cursor: pointer;">Nautical Chart</button>
              <button onclick="setBmapTileLayer('auto')" style="background: #111b2b; color: #e2e8f0; border: 1px solid #1e334d; padding: 3px; font-size: 9px; border-radius: 2px; cursor: pointer;">Auto-Adaptive</button>
            </div>
          </div>

        </div>

        <!-- ── FLOATING PARAMETER CARD 1: BANK BRANCHES (US) (SCREENSHOT 4) ── -->
        <div id="bmap_param_card_bank" style="position: absolute; top: 12px; right: 295px; width: 250px; z-index: 100; background: rgba(8, 12, 18, 0.94); border: 1px solid #ffaa00; border-radius: 4px; padding: 8px 10px; font-family: var(--font-mono); box-shadow: 0 8px 24px rgba(0,0,0,0.85); font-size: 9.5px; display: block;">
          <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #332200; padding-bottom: 4px; margin-bottom: 6px;">
            <div style="display: flex; align-items: center; gap: 4px;">
              <span style="color: #ffaa00; font-size: 9px;">▾</span>
              <strong style="color: #ffaa00; font-size: 11px;">Bank Branches (US)</strong>
            </div>
            <div style="display: flex; align-items: center; gap: 5px; color: #94a3b8; font-size: 10px;">
              <span style="cursor: pointer;">✏️</span>
              <span style="cursor: pointer;">⚡</span>
              <span style="cursor: pointer;" onclick="document.getElementById('bmap_param_card_bank').style.display='none';">✕</span>
            </div>
          </div>

          <div style="display: flex; flex-direction: column; gap: 5px;">
            <div style="display: flex; justify-content: space-between; align-items: center;">
              <span style="color: #94a3b8;">Name</span>
              <select id="filter_bank_name" onchange="filterBankBranches()" style="background: #05080e; color: #ffaa00; border: 1px solid #203a5e; font-size: 9.5px; border-radius: 2px; width: 140px; outline: none; padding: 1px 4px;">
                <option value="ALL">All Banks</option>
                <option value="JPMorgan Chase">JPMorgan Chase</option>
                <option value="Bank of America">Bank of America</option>
                <option value="Wells Fargo">Wells Fargo</option>
                <option value="Citigroup">Citigroup</option>
                <option value="U.S. Bancorp">U.S. Bancorp</option>
                <option value="PNC Financial">PNC Financial</option>
                <option value="Truist Financial">Truist Financial</option>
                <option value="Capital One">Capital One</option>
                <option value="TD Bank">TD Bank</option>
              </select>
            </div>

            <div style="display: flex; justify-content: space-between; align-items: center;">
              <span style="color: #94a3b8;">Branch</span>
              <select id="filter_bank_branch" onchange="filterBankBranches()" style="background: #05080e; color: #00e5ff; border: 1px solid #203a5e; font-size: 9.5px; border-radius: 2px; width: 140px; outline: none; padding: 1px 4px;">
                <option value="ALL">All Types</option>
                <option value="Retail Full-Service">Retail Full-Service</option>
                <option value="Commercial Banking Center">Commercial Banking</option>
                <option value="Wealth Management / Private Bank">Wealth / Private Bank</option>
                <option value="Institutional / Treasury Hub">Institutional Hub</option>
              </select>
            </div>

            <!-- Deposits (M) Amber Horizontal Range Bar Slider (Exact Screenshot 4) -->
            <div style="margin-top: 2px;">
              <div style="display: flex; justify-content: space-between; align-items: center; font-size: 9px; margin-bottom: 2px;">
                <span style="color: #94a3b8;">Deposits (M)</span>
                <span style="color: #ffaa00; font-weight: 700;" id="lbl_bank_dep_val">$0M+ (1,675 Branches)</span>
              </div>
              <div style="display: flex; align-items: center; gap: 6px;">
                <input type="range" id="slider_bank_dep" min="0" max="5000" step="50" value="0" oninput="filterBankBranches()" style="flex: 1; accent-color: #ffaa00; cursor: pointer; height: 5px;">
              </div>
            </div>

            <div style="display: flex; justify-content: space-between; align-items: center;">
              <span style="color: #94a3b8;">Location</span>
              <select id="filter_bank_state" onchange="filterBankBranches()" style="background: #05080e; color: #34d399; border: 1px solid #203a5e; font-size: 9.5px; border-radius: 2px; width: 140px; outline: none; padding: 1px 4px;">
                <option value="ALL">All States (Continental US)</option>
                <option value="NY">New York (NY)</option>
                <option value="CA">California (CA)</option>
                <option value="TX">Texas (TX)</option>
                <option value="IL">Illinois (IL)</option>
                <option value="FL">Florida (FL)</option>
                <option value="PA">Pennsylvania (PA)</option>
                <option value="MA">Massachusetts (MA)</option>
                <option value="GA">Georgia (GA)</option>
                <option value="NC">North Carolina (NC)</option>
                <option value="OH">Ohio (OH)</option>
                <option value="VA">Virginia (VA)</option>
                <option value="WA">Washington (WA)</option>
                <option value="CO">Colorado (CO)</option>
              </select>
            </div>

            <div style="display: flex; gap: 4px; margin-top: 4px;">
              <button onclick="resetBankFilter()" style="flex: 1; background: #132032; color: #94a3b8; border: 1px solid #1c2e44; padding: 3px; font-size: 9px; border-radius: 2px; cursor: pointer;">↺ Reset Filter</button>
              <button onclick="jumpToBmapPreset('bank_branches')" style="flex: 1; background: #0284c7; color: #fff; border: none; padding: 3px; font-size: 9px; font-weight: 700; border-radius: 2px; cursor: pointer;">🔍 Fit US View</button>
            </div>
          </div>
        </div>

        <!-- ── FLOATING PARAMETER CARD 2: VESSELS (SCREENSHOTS 3, 6, 27) ── -->
        <div id="bmap_vessels_filter_card" style="position: absolute; top: 12px; right: 555px; width: 230px; z-index: 99; background: rgba(8, 12, 18, 0.94); border: 1.5px solid #ffaa00; border-radius: 4px; padding: 8px 10px; font-family: var(--font-mono); box-shadow: 0 8px 24px rgba(0,0,0,0.85); font-size: 9.5px; display: block;">
          <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #332200; padding-bottom: 4px; margin-bottom: 6px;">
            <strong style="color: #ffaa00; font-size: 11px; letter-spacing: 0.5px;">▾ VESSELS</strong>
            <div style="display: flex; align-items: center; gap: 4px;">
              <span style="color: #00e676; font-size: 9px; font-weight: 700;">● LIVE AIS FEED</span>
              <span style="cursor: pointer; color: #94a3b8;" onclick="document.getElementById('bmap_vessels_filter_card').style.display='none';">✕</span>
            </div>
          </div>

          <div style="display: flex; flex-direction: column; gap: 4px;">
            <div style="display: flex; justify-content: space-between; align-items: center;">
              <span style="color: #94a3b8;">Vessel / IMO:</span>
              <select id="vessel_filter_select" onchange="filterVesselsByName(this.value)" style="background: #05080e; color: #00e5ff; border: 1px solid #203a5e; font-size: 9px; border-radius: 2px; max-width: 120px; outline: none;">
                <option value="ALL">All In Scope</option>
                <option value="GREG_MORTIMER">🚢 GREG MORTIMER (Image 8)</option>
                <option value="HORMUZ_FLEET">🔥 Hormuz Fleet (20+ Tankers)</option>
                <option value="HOUSTON_FLEET">🇺🇸 Houston Fleet (Seaways Catalonia)</option>
                <option value="MALACCA_FLEET">⚓ Malacca Fleet</option>
              </select>
            </div>

            <div style="display: flex; justify-content: space-between;">
              <span style="color: #94a3b8;">Type:</span>
              <strong style="color: #fff;">Tankers (Crude / Products)</strong>
            </div>

            <div style="display: flex; justify-content: space-between;">
              <span style="color: #94a3b8;">Status:</span>
              <span style="color: #00e676;">In Service / Commissioned</span>
            </div>

            <div style="display: flex; justify-content: space-between;">
              <span style="color: #94a3b8;">Destination:</span>
              <strong style="color: #fff;" id="vessel_card_dest">Global Market Hubs</strong>
            </div>

            <!-- Mini Graphic Bars for Draft, DWT, Class, Ben.Owner -->
            <div style="margin-top: 3px; border-top: 1px solid #162438; padding-top: 4px;">
              <div style="display: flex; justify-content: space-between; font-size: 8.5px; color: #64748b; margin-bottom: 2px;">
                <span>Draft Spectrum:</span>
                <span style="color: #ffaa00;">10m - 22m (VLCC Loaded)</span>
              </div>
              <div style="background: #111a28; height: 5px; border-radius: 2px; overflow: hidden; display: flex;">
                <div style="background: #38bdf8; width: 45%;"></div>
                <div style="background: #ffaa00; width: 35%;"></div>
                <div style="background: #ef4444; width: 20%;"></div>
              </div>
            </div>

            <div style="margin-top: 2px;">
              <div style="display: flex; justify-content: space-between; font-size: 8.5px; color: #64748b; margin-bottom: 2px;">
                <span>DWT Class Mix:</span>
                <span style="color: #00e5ff;">VLCC (48%) / Suez (32%)</span>
              </div>
              <div style="background: #111a28; height: 5px; border-radius: 2px; overflow: hidden; display: flex;">
                <div style="background: #00e5ff; width: 48%;"></div>
                <div style="background: #a855f7; width: 32%;"></div>
                <div style="background: #34d399; width: 20%;"></div>
              </div>
            </div>

            <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 3px;">
              <span style="color: #94a3b8;">Last Seen:</span>
              <span style="color: #ffaa00; font-weight: 700;">90 Days (Active)</span>
            </div>

            <div style="display: flex; gap: 4px; margin-top: 6px;">
              <button onclick="jumpToActiveVesselFocus()" style="flex: 1; background: #0284c7; color: #fff; border: none; padding: 4px; font-size: 9px; font-weight: 700; border-radius: 2px; cursor: pointer;">🔍 Zoom</button>
              <button onclick="toggleFollowActiveVessel()" id="btn_card_follow" style="flex: 1; background: #059669; color: #fff; border: none; padding: 4px; font-size: 9px; font-weight: 700; border-radius: 2px; cursor: pointer;">🚢 Follow</button>
              <button onclick="triggerArpaScan()" style="flex: 1; background: #7c2d12; color: #fed7aa; border: 1px solid #c2410c; padding: 4px; font-size: 9px; font-weight: 700; border-radius: 2px; cursor: pointer;">⚡ ARPA</button>
            </div>
          </div>
        </div>

        <!-- ── FLOATING PARAMETER CARD 3: CRUDE OIL PIPELINES (SCREENSHOT 27) ── -->
        <div id="bmap_pipelines_filter_card" style="position: absolute; top: 12px; right: 295px; width: 250px; z-index: 100; background: rgba(8, 12, 18, 0.94); border: 1px solid #3b82f6; border-radius: 4px; padding: 8px 10px; font-family: var(--font-mono); box-shadow: 0 8px 24px rgba(0,0,0,0.85); font-size: 9.5px; display: none;">
          <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #1e3a5f; padding-bottom: 4px; margin-bottom: 6px;">
            <div style="display: flex; align-items: center; gap: 4px;">
              <span style="color: #38bdf8; font-size: 9px;">▾</span>
              <strong style="color: #38bdf8; font-size: 11px;">Crude Oil Pipelines</strong>
            </div>
            <div style="display: flex; align-items: center; gap: 5px; color: #94a3b8; font-size: 10px;">
              <span style="cursor: pointer;">✏️</span>
              <span style="cursor: pointer;" onclick="document.getElementById('bmap_pipelines_filter_card').style.display='none';">✕</span>
            </div>
          </div>

          <div style="display: flex; flex-direction: column; gap: 4px;">
            <div style="display: flex; justify-content: space-between; align-items: center;">
              <span style="color: #94a3b8;">Pipeline</span>
              <span style="color: #fff;">All (15 Trunklines)</span>
            </div>
            <div style="display: flex; justify-content: space-between; align-items: center;">
              <span style="color: #94a3b8;">Segment</span>
              <span style="color: #fff;">All Segments</span>
            </div>
            <div style="display: flex; justify-content: space-between; align-items: center;">
              <span style="color: #94a3b8;">Company</span>
              <span style="color: #fff;">All Operators</span>
            </div>
            <div style="display: flex; justify-content: space-between; align-items: center;">
              <span style="color: #94a3b8;">Fuel</span>
              <span style="color: #ffaa00; font-weight: 700;">All Selected (Crude)</span>
            </div>
            <div style="display: flex; justify-content: space-between; align-items: center;">
              <span style="color: #94a3b8;">Status</span>
              <span style="color: #00e676; font-weight: 700;">3/8 Selected (Active)</span>
            </div>
            <div style="display: flex; justify-content: space-between; align-items: center;">
              <span style="color: #94a3b8;">Location</span>
              <span style="color: #fff;">All (Global Corridors)</span>
            </div>

            <!-- Mini bars for Capacity & Pipe Length -->
            <div style="margin-top: 2px;">
              <div style="display: flex; justify-content: space-between; font-size: 8.5px; color: #94a3b8; margin-bottom: 2px;">
                <span>Capacity:</span>
                <span style="color: #ffaa00;">440k - 5,000k bpd</span>
              </div>
              <div style="background: #111a28; height: 5px; border-radius: 2px; overflow: hidden; display: flex;">
                <div style="background: #f59e0b; width: 75%;"></div>
              </div>
            </div>

            <div style="margin-top: 2px;">
              <div style="display: flex; justify-content: space-between; font-size: 8.5px; color: #94a3b8; margin-bottom: 2px;">
                <span>Pipe Length:</span>
                <span style="color: #38bdf8;">320 - 5,360 km</span>
              </div>
              <div style="background: #111a28; height: 5px; border-radius: 2px; overflow: hidden; display: flex;">
                <div style="background: #3b82f6; width: 65%;"></div>
              </div>
            </div>

            <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 2px;">
              <span style="color: #94a3b8;">Line Width</span>
              <span style="color: #ffaa00; font-weight: 700;">2 px</span>
            </div>
            <div style="display: flex; justify-content: space-between; align-items: center;">
              <span style="color: #94a3b8;">Size By</span>
              <span style="color: #fff;">Diameter</span>
            </div>
            <div style="display: flex; justify-content: space-between; align-items: center;">
              <span style="color: #94a3b8;">Color By</span>
              <span style="color: #38bdf8;">Uniform: Blue</span>
            </div>
            <div style="display: flex; justify-content: space-between; align-items: center;">
              <span style="color: #94a3b8;">Labels</span>
              <span style="color: #64748b;">Off</span>
            </div>

            <div style="display: flex; gap: 4px; margin-top: 4px;">
              <button onclick="togglePipelinesHighlight()" style="flex: 1; background: #1e3a5f; color: #38bdf8; border: 1px solid #3b82f6; padding: 3px; font-size: 9px; border-radius: 2px; cursor: pointer;">⚡ Highlight All</button>
              <button onclick="jumpToBmapPreset('crude_pipelines')" style="flex: 1; background: #2563eb; color: #fff; border: none; padding: 3px; font-size: 9px; font-weight: 700; border-radius: 2px; cursor: pointer;">🔍 Fit World View</button>
            </div>
          </div>
        </div>

        <!-- ── FLOATING PARAMETER CARD 4: WEATHER (SCREENSHOTS 2, 3) ── -->
        <div id="bmap_weather_filter_card" style="position: absolute; top: 12px; right: 295px; width: 220px; z-index: 100; background: rgba(8, 12, 18, 0.94); border: 1px solid #64748b; border-radius: 4px; padding: 8px 10px; font-family: var(--font-mono); box-shadow: 0 8px 24px rgba(0,0,0,0.85); font-size: 9.5px; display: none;">
          <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #334155; padding-bottom: 4px; margin-bottom: 6px;">
            <div style="display: flex; align-items: center; gap: 4px;">
              <span style="color: #cbd5e1; font-size: 9px;">▾</span>
              <strong style="color: #fff; font-size: 11px;">Weather</strong>
            </div>
            <span style="cursor: pointer; color: #94a3b8;" onclick="document.getElementById('bmap_weather_filter_card').style.display='none';">✕</span>
          </div>

          <div style="display: flex; flex-direction: column; gap: 5px;">
            <div style="display: flex; justify-content: space-between; align-items: center;">
              <span style="color: #94a3b8;">Type</span>
              <select id="weather_type_select" onchange="switchWeatherType(this.value)" style="background: #05080e; color: #38bdf8; border: 1px solid #203a5e; font-size: 9.5px; border-radius: 2px; width: 120px; outline: none; padding: 1px 4px;">
                <option value="cloud">Cloud Cover</option>
                <option value="temp">Temperature</option>
                <option value="wind">Wind Speed</option>
              </select>
            </div>
            <div style="display: flex; justify-content: space-between; align-items: center;">
              <span style="color: #94a3b8;">Stat</span>
              <span style="color: #ffaa00; font-weight: 700;">Avg</span>
            </div>
            <div style="display: flex; justify-content: space-between; align-items: center;">
              <span style="color: #94a3b8;">Day</span>
              <span style="color: #00e676; font-weight: 700;">Today</span>
            </div>
            <div style="margin-top: 4px; border-top: 1px solid #1e293b; padding-top: 4px;">
              <div style="display: flex; justify-content: space-between; font-size: 8.5px; color: #94a3b8; margin-bottom: 2px;">
                <span id="weather_scale_lbl">Cloud Cover: 0% to 100%</span>
              </div>
              <div id="weather_gradient_bar" style="height: 6px; border-radius: 2px; background: linear-gradient(90deg, #05080e 0%, #475569 50%, #f8fafc 100%);"></div>
            </div>
          </div>
        </div>

        <!-- ── FLOATING PARAMETER CARD 5: WORLD EQUITY MARKETS (SCREENSHOTS 3, 4) ── -->
        <div id="bmap_equity_filter_card" style="position: absolute; top: 12px; right: 295px; width: 230px; z-index: 100; background: rgba(8, 12, 18, 0.94); border: 1px solid #059669; border-radius: 4px; padding: 8px 10px; font-family: var(--font-mono); box-shadow: 0 8px 24px rgba(0,0,0,0.85); font-size: 9.5px; display: none;">
          <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #064e3b; padding-bottom: 4px; margin-bottom: 6px;">
            <div style="display: flex; align-items: center; gap: 4px;">
              <span style="color: #34d399; font-size: 9px;">▾</span>
              <strong style="color: #34d399; font-size: 11px;">World Equity Markets</strong>
            </div>
            <span style="cursor: pointer; color: #94a3b8;" onclick="document.getElementById('bmap_equity_filter_card').style.display='none';">✕</span>
          </div>

          <div style="display: flex; flex-direction: column; gap: 5px;">
            <div style="font-size: 9px; color: #94a3b8;">National Benchmark Return Heatmap:</div>
            <div style="display: flex; align-items: center; justify-content: space-between; font-size: 8.5px;">
              <span style="color: #ef4444; font-weight: 700;">-2.0 (% Chg)</span>
              <div style="flex: 1; height: 6px; margin: 0 8px; border-radius: 2px; background: linear-gradient(90deg, #dc2626 0%, #451a03 50%, #16a34a 100%);"></div>
              <span style="color: #22c55e; font-weight: 700;">+2.0 (% Chg)</span>
            </div>
            <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 4px;">
              <span style="color: #94a3b8;">Coverage:</span>
              <strong style="color: #fff;">15 Sovereign Indexes</strong>
            </div>
            <div style="display: flex; justify-content: space-between; align-items: center;">
              <span style="color: #94a3b8;">Top Gainer:</span>
              <strong style="color: #22c55e;">India Nifty 50 (+1.84%)</strong>
            </div>
            <div style="display: flex; justify-content: space-between; align-items: center;">
              <span style="color: #94a3b8;">Top Laggard:</span>
              <strong style="color: #ef4444;">Egypt EGX 30 (-1.85%)</strong>
            </div>
          </div>
        </div>

        <!-- ── AUTHENTIC FLOATING CONCENTRIC RADAR CIRCLES LEGEND BOX (SCREENSHOT 4) ── -->
        <div id="bmap_branch_legend" style="position: absolute; top: 180px; left: 140px; z-index: 45; background: rgba(5,8,15,0.88); border: 1px solid #1e334d; border-radius: 4px; padding: 8px 12px; font-family: var(--font-mono); font-size: 9px; pointer-events: none;">
          <div style="color: #fff; font-weight: 800; font-size: 10px; margin-bottom: 2px;">Bank Branches (US)</div>
          <div style="color: #64748b; margin-bottom: 4px;">Branch Deposit Amounts:</div>
          <div style="color: #ffaa00; font-weight: 700;">500,000.00k</div>
          
          <!-- Concentric radar circles matching screenshot -->
          <div style="display: flex; align-items: center; justify-content: center; margin: 4px 0;">
            <svg width="44" height="44" viewBox="0 0 44 44">
              <circle cx="22" cy="22" r="20" stroke="rgba(56,189,248,0.3)" stroke-width="1" fill="none" />
              <circle cx="22" cy="22" r="13" stroke="rgba(56,189,248,0.6)" stroke-width="1.2" fill="none" />
              <circle cx="22" cy="22" r="5" stroke="#00e5ff" stroke-width="1.5" fill="#38bdf8" />
            </svg>
          </div>
          
          <div style="display: flex; justify-content: space-between; align-items: center; color: #64748b;">
            <span>0 (USD)</span>
            <span style="color: #38bdf8; display: flex; align-items: center; gap: 4px; font-weight: 700;">
              <span style="display: inline-block; width: 6px; height: 6px; background: #38bdf8; border-radius: 1px;"></span> Branch
            </span>
          </div>
        </div>

        <!-- ── BOTTOM RIGHT LEGEND: CRUDE PIPELINES & VESSELS (SCREENSHOT 27) ── -->
        <div id="bmap_pipelines_legend" style="position: absolute; bottom: 35px; right: 14px; z-index: 50; background: rgba(5,8,15,0.92); border: 1px solid #1e334d; border-radius: 4px; padding: 6px 12px; font-family: var(--font-mono); font-size: 9.5px; display: block;">
          <div style="margin-bottom: 4px;">
            <div style="color: #94a3b8; font-size: 8.5px; font-weight: 700;">Vessels</div>
            <div style="display: flex; align-items: center; gap: 6px; color: #00e5ff; font-weight: 700;">
              <span style="display: inline-block; width: 6px; height: 6px; background: #00e5ff; border-radius: 1px;"></span>
              <span>Oil</span>
            </div>
          </div>
          <div style="border-top: 1px solid #142236; padding-top: 4px;">
            <div style="color: #94a3b8; font-size: 8.5px; font-weight: 700;">Crude Oil Pipelines</div>
            <div style="display: flex; align-items: center; gap: 6px; color: #3b82f6; font-weight: 700;">
              <span style="display: inline-block; width: 14px; height: 2px; background: #3b82f6;"></span>
              <span>Crude Oil Pipeline</span>
            </div>
          </div>
        </div>

        <!-- ── FLOATING DETAILED VESSEL INSPECTOR POPUP (SCREENSHOT 8 - GREG MORTIMER / SEAWAYS CATALONIA) ── -->
        <div id="bmap_vessel_popup" style="display: none; position: absolute; top: 70px; right: 295px; width: 290px; background: rgba(5,8,15,0.96); border: 1px solid #00e5ff; border-radius: 6px; padding: 12px; z-index: 110; font-family: var(--font-mono); box-shadow: 0 10px 30px rgba(0,0,0,0.9);">
          <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #1a293d; padding-bottom: 6px; margin-bottom: 8px;">
            <div>
              <span id="pop_vessel_name" style="color: #00e5ff; font-weight: 800; font-size: 12px;">GREG MORTIMER</span>
              <div style="color: #64748b; font-size: 9px;">IMO: <span id="pop_vessel_imo">9834648</span></div>
            </div>
            <button onclick="closeBmapVesselPopup()" style="background: transparent; color: #94a3b8; border: none; font-size: 12px; cursor: pointer;">✕</button>
          </div>
          <table style="width: 100%; font-size: 9.5px; border-collapse: collapse;">
            <tr><td style="color:#64748b;padding:2px 0;">Navigation Status:</td><td style="color:#fff;" id="pop_vessel_status">Under way using engine</td></tr>
            <tr><td style="color:#64748b;padding:2px 0;">Destination:</td><td style="color:#ffaa00;font-weight:700;" id="pop_vessel_dest">DEVIL ISLAND</td></tr>
            <tr><td style="color:#64748b;padding:2px 0;">ETA (User Local):</td><td style="color:#fff;" id="pop_vessel_eta">03/04/2026 13:00:00</td></tr>
            <tr><td style="color:#64748b;padding:2px 0;">Vessel Type:</td><td style="color:#fff;" id="pop_vessel_type">Passenger / Expedition</td></tr>
            <tr><td style="color:#64748b;padding:2px 0;">Current Speed:</td><td style="color:#00e676;font-weight:700;" id="pop_vessel_speed">10.5 kts</td></tr>
            <tr><td style="color:#64748b;padding:2px 0;">Current Draft:</td><td style="color:#ffaa00;" id="pop_vessel_draft">5.2 m (Max: 5.3 m)</td></tr>
          </table>

          <!-- More Dropdown matching Image 8 -->
          <div style="margin-top: 6px; position: relative;">
            <button onclick="toggleVesselMoreMenu()" style="width: 100%; background: #132032; color: #94a3b8; border: 1px solid #1e334d; padding: 4px; font-size: 9px; border-radius: 2px; cursor: pointer; text-align: left; display: flex; justify-content: space-between;">
              <span>More ▾</span>
              <span>▼</span>
            </button>
            <div id="vessel_more_menu" style="display: none; background: #0c1626; border: 1px solid #203a5e; border-radius: 3px; margin-top: 2px; font-size: 9px;">
              <div onclick="alert('IMO - Vessel Overview: Technical specifications, engine class, and builder history loaded.');" style="padding: 5px 8px; color: #00e5ff; cursor: pointer; border-bottom: 1px solid #142236;">IMO - Vessel Overview</div>
              <div onclick="alert('IMO - Port Calling: Port fixture chronology and past 10 port inspections loaded.');" style="padding: 5px 8px; color: #ffaa00; cursor: pointer; border-bottom: 1px solid #142236;">IMO - Port Calling</div>
              <div onclick="alert('AHOY - Fixture History: Historical spot charter day-rates and charterer ledger loaded.');" style="padding: 5px 8px; color: #34d399; cursor: pointer;">AHOY - Fixture History</div>
            </div>
          </div>

          <div style="display: flex; gap: 4px; margin-top: 8px;">
            <button onclick="zoomToCurrentPopupVessel()" style="flex:1;background:#1e3a5f;color:#00e5ff;border:1px solid #3b82f6;padding:4px;font-size:9px;border-radius:2px;cursor:pointer;">🔍 Zoom In</button>
            <button onclick="followCurrentPopupVessel()" style="flex:1;background:#064e3b;color:#34d399;border:1px solid #059669;padding:4px;font-size:9px;border-radius:2px;cursor:pointer;">🚢 Auto-Follow</button>
          </div>
        </div>

        <!-- ── FLOATING DETAILED FDIC BANK BRANCH POPUP (EXACT SCREENSHOT 10) ── -->
        <div id="bmap_branch_popup" style="display: none; position: absolute; top: 70px; left: 140px; width: 310px; background: rgba(5,8,15,0.96); border: 1px solid #ffaa00; border-radius: 6px; padding: 12px; z-index: 110; font-family: var(--font-mono); box-shadow: 0 10px 30px rgba(0,0,0,0.9);">
          <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #332200; padding-bottom: 6px; margin-bottom: 8px;">
            <span style="color: #ffaa00; font-weight: 800; font-size: 11.5px;">FDIC BANK BRANCH TELEMETRY</span>
            <button onclick="document.getElementById('bmap_branch_popup').style.display='none';" style="background: transparent; color: #94a3b8; border: none; font-size: 12px; cursor: pointer;">✕</button>
          </div>
          <table style="width: 100%; font-size: 9.5px; border-collapse: collapse;">
            <tr><td style="color:#64748b;padding:3px 0;">Branch Name:</td><td style="color:#fff;font-weight:700;" id="pop_branch_name">Third Avenue &amp; 41st Street Branch</td></tr>
            <tr><td style="color:#64748b;padding:3px 0;">Company:</td><td style="color:#38bdf8;" id="pop_branch_company">JPMorgan Chase Bank National Association</td></tr>
            <tr><td style="color:#64748b;padding:3px 0;">Branch Total Deposits (USD):</td><td style="color:#ffaa00;font-weight:800;" id="pop_branch_dep">1,214,602k ($1.21B)</td></tr>
            <tr><td style="color:#64748b;padding:3px 0;">Company Domestic Deposits (USD):</td><td style="color:#e2e8f0;" id="pop_branch_comp_dep">2,128,462,000k ($2.13T)</td></tr>
            <tr><td style="color:#64748b;padding:3px 0;">Company Total Assets (USD):</td><td style="color:#e2e8f0;" id="pop_branch_comp_assets">3,914,143,296k ($3.91T)</td></tr>
            <tr><td style="color:#64748b;padding:3px 0;">Year:</td><td style="color:#00e676;" id="pop_branch_year">2022 (Active FDIC FFIEC 031/041)</td></tr>
          </table>
          <div style="margin-top: 8px;">
            <button onclick="zoomToManhattanStreetLevel()" style="width: 100%; background: #0284c7; color: #fff; border: none; padding: 4px; font-size: 9px; font-weight: 700; border-radius: 2px; cursor: pointer;">🛰️ Zoom to High-Res Street Satellite</button>
          </div>
        </div>

        <!-- Target Inspection Reticle [⌖ O] -->
        <div id="bmap_reticle" style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); pointer-events: none; z-index: 10; width: 44px; height: 44px; border: 1.5px dashed rgba(255,170,0,0.65); border-radius: 50%; display: flex; align-items: center; justify-content: center;">
          <div style="width: 4px; height: 4px; background: #ffaa00; border-radius: 50%;"></div>
        </div>

        <!-- Nautical Scale Bar (Bottom Left) -->
        <div id="bmap_scale_bar" style="position: absolute; bottom: 12px; left: 14px; z-index: 50; background: rgba(5,8,15,0.85); border: 1px solid #1e334d; border-radius: 3px; padding: 3px 8px; font-size: 9px; font-family: var(--font-mono); color: #00e5ff;">
          <span id="scale_km">2000 km</span> | <span id="scale_mi">1000 mi</span>
        </div>

        <!-- Bloomberg Galileo, Global Oil Tracker & FDIC Attribution (Screenshot 27 Bottom Right) -->
        <div style="position: absolute; bottom: 12px; right: 14px; z-index: 50; background: rgba(5,8,15,0.85); border: 1px solid #1e334d; border-radius: 3px; padding: 2px 8px; font-size: 8.5px; font-family: var(--font-mono); color: #64748b;">
          Bloomberg Finance L.P., Mapbox, OpenStreetMap, Global Oil Infrastructure Tracker, Global Energy Monitor, FDIC
        </div>

      </div>
    </div>

    <!-- ── AUTHENTIC BLOOMBERG BOTTOM SUGGESTED FUNCTIONS BAR (EXACT SCREENSHOTS 4, 18, 20) ── -->
    <div style="background: #000; border: 1px solid #1a2736; border-top: none; padding: 6px 14px; display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 8px; font-family: var(--font-mono); font-size: 10px;">
      <div style="display: flex; align-items: center; gap: 12px; flex-wrap: wrap;">
        <span style="color: #ffaa00; font-weight: 800;">Suggested Functions</span>
        <span style="color: #334155;">|</span>
        <span onclick="alert('PORT <GO>: Portfolio Performance & Factor Risk Attributions Loaded.');" style="color: #e2e8f0; cursor: pointer;">
          <strong style="color: #ffaa00;">PORT</strong> Analyze portfolio performance &amp; risk
        </span>
        <span style="color: #334155;">|</span>
        <span onclick="alert('CORR <GO>: Multi-Asset Cross-Correlation Matrix Loaded.');" style="color: #e2e8f0; cursor: pointer;">
          <strong style="color: #ffaa00;">CORR</strong> Correlate price movement of securities
        </span>
        <span style="color: #334155;">|</span>
        <span onclick="switchBmapView('splc')" style="color: #e2e8f0; cursor: pointer;">
          <strong style="color: #ffaa00;">SPLC</strong> Supply Chain Analysis
        </span>
        <span style="color: #334155;">|</span>
        <span onclick="switchBmapView('fxc')" style="color: #e2e8f0; cursor: pointer;">
          <strong style="color: #ffaa00;">FXC</strong> Currency Rates Matrix
        </span>
      </div>
      <div style="display: flex; align-items: center; gap: 8px; color: #64748b;">
        <span>BMAP &lt;GO&gt;</span>
        <span>•</span>
        <span style="color: #00e676;">100% OPERATIONAL</span>
      </div>
    </div>

    <!-- ═══════════════════════════════════════════════════════════════ -->
    <!-- ── PRIMARY VIEW 2: BLOOMBERG ASSET DATA GRID (SCREENSHOT 5 TABLE) ── -->
    <!-- ═══════════════════════════════════════════════════════════════ -->
    <div id="bmap_view_container_table" style="display: none; background: #080d16; border: 1px solid #1e2e44; border-top: none; padding: 14px; font-family: var(--font-mono);">
      <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px; flex-wrap: wrap; gap: 8px;">
        <div style="display: flex; align-items: center; gap: 8px;">
          <span style="color: #00e5ff; font-weight: 800; font-size: 12px;">📋 BLOOMBERG MARITIME BERTH VISITS &amp; ASSET GRID (SCREENSHOT 5)</span>
          <span id="table_total_count_badge" class="badge" style="background: #1e3a5f; color: #38bdf8;">21 Berth Visits Active</span>
        </div>
        <div style="display: flex; gap: 6px; align-items: center;">
          <select id="bmap_table_dataset_selector" onchange="switchTableDataset(this.value)" style="background: #0d1726; color: #ffaa00; border: 1px solid #203a5e; border-radius: 3px; padding: 4px 8px; font-size: 10px; font-family: var(--font-mono); font-weight: 700;">
            <option value="berths">Vessel Berth Visits (Image 5)</option>
            <option value="banks">US Bank Branches (Image 11)</option>
            <option value="pipelines">Crude Oil Pipelines (Image 27)</option>
            <option value="gas">Natural Gas Pipelines (Image 12)</option>
          </select>
          <input type="text" id="bmap_table_search" oninput="filterBmapTableRows(this.value)" placeholder="Search berth, country, class, IMO..." style="background: #0d1726; color: #fff; border: 1px solid #203a5e; border-radius: 3px; padding: 4px 8px; font-size: 10px; font-family: var(--font-mono); width: 220px;">
          <button onclick="exportBmapCSV()" style="background: #064e3b; color: #34d399; border: 1px solid #059669; padding: 4px 10px; font-size: 10px; font-weight: 700; border-radius: 3px; cursor: pointer;">📥 Export CSV</button>
        </div>
      </div>

      <div style="max-height: 600px; overflow-y: auto; border: 1px solid #1a2a40; border-radius: 4px;">
        <table class="data-table" style="width: 100%; font-size: 10px; margin-bottom: 0;" id="bmap_data_grid_table">
          <thead id="bmap_table_thead">
            <!-- Dynamic header based on dataset -->
          </thead>
          <tbody id="bmap_data_grid_tbody"></tbody>
        </table>
      </div>
    </div>

    <!-- ═══════════════════════════════════════════════════════════════ -->
    <!-- ── PRIMARY VIEW 3: GPC CANDLESTICK CHART & TECHNICAL CHECKLIST (SCREENSHOTS 14, 15) ── -->
    <!-- ═══════════════════════════════════════════════════════════════ -->
    <div id="bmap_view_container_chart" style="display: none; background: #080d16; border: 1px solid #1e2e44; border-top: none; padding: 14px; font-family: var(--font-mono);">
      <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
        <div style="display: flex; align-items: center; gap: 8px;">
          <strong style="color: #ffaa00; font-size: 13px;">GPC &lt;GO&gt; — SPY US Equity — Multi-Indicator Technical Analysis</strong>
          <span class="badge" style="background: #111a28; color: #00e676;">Candlestick + Ichimoku Cloud</span>
        </div>
        <div style="display: flex; gap: 4px;">
          <button class="bb-key" onclick="setChartTimeframe('1D')">1D</button>
          <button class="bb-key" onclick="setChartTimeframe('1M')">1M</button>
          <button class="bb-key" onclick="setChartTimeframe('1Y')">1Y</button>
          <button class="bb-key" style="background:#1e3a5f;color:#00e5ff;" onclick="setChartTimeframe('5Y')">5Y Max</button>
        </div>
      </div>

      <div style="display: flex; gap: 12px; height: 600px;">
        <!-- Left: Interactive Canvas Chart with Sub-panels -->
        <div style="flex: 1; display: flex; flex-direction: column; gap: 6px; background: #000; border: 1px solid #1a2736; border-radius: 4px; padding: 8px; position: relative;">
          <!-- Main Candlestick Pane -->
          <div style="flex: 3; position: relative;">
            <canvas id="gpc_main_canvas" style="width: 100%; height: 100%;"></canvas>
            <div id="gpc_price_hud" style="position: absolute; top: 8px; left: 10px; font-size: 9.5px; color: #94a3b8; pointer-events: none;">
              SPY US: <strong style="color:#00e676;">404.190</strong> &nbsp; MA5: <span style="color:#38bdf8;">398.14</span> &nbsp; MA10: <span style="color:#f59e0b;">399.26</span> &nbsp; MA15: <span style="color:#ec4899;">403.22</span>
            </div>
          </div>
          <!-- RSI Sub-pane -->
          <div id="gpc_pane_rsi" style="flex: 1; border-top: 1px solid #142236; position: relative;">
            <canvas id="gpc_rsi_canvas" style="width: 100%; height: 100%;"></canvas>
            <div style="position: absolute; top: 4px; left: 8px; font-size: 9px; color: #94a3b8;">RSI(14): <strong style="color:#a855f7;" id="gpc_rsi_val">52.82</strong></div>
          </div>
          <!-- MACD Sub-pane -->
          <div id="gpc_pane_macd" style="flex: 1; border-top: 1px solid #142236; position: relative;">
            <canvas id="gpc_macd_canvas" style="width: 100%; height: 100%;"></canvas>
            <div style="position: absolute; top: 4px; left: 8px; font-size: 9px; color: #94a3b8;">MACD(12,26,9): <strong style="color:#00e676;">-0.8401</strong> &nbsp; Sig: <span style="color:#ffaa00;">0.3848</span></div>
          </div>
          <!-- Volume Sub-pane -->
          <div id="gpc_pane_vol" style="flex: 0.8; border-top: 1px solid #142236; position: relative;">
            <canvas id="gpc_vol_canvas" style="width: 100%; height: 100%;"></canvas>
            <div style="position: absolute; top: 4px; left: 8px; font-size: 9px; color: #64748b;">Volume: <strong style="color:#38bdf8;">90,119,952</strong></div>
          </div>
        </div>

        <!-- Right: Authentic Bloomberg Technical Indicators Checklist (Screenshot 15) -->
        <div style="width: 250px; background: #0a101b; border: 1px solid #1e334d; border-radius: 4px; padding: 10px; font-family: var(--font-mono); font-size: 10px; display: flex; flex-direction: column;">
          <div style="color: #ffaa00; font-weight: 800; font-size: 11px; margin-bottom: 8px; border-bottom: 1px solid #162438; padding-bottom: 4px;">
            SPY US Equity Indicators
          </div>
          <div style="display: flex; flex-direction: column; gap: 6px; flex: 1; overflow-y: auto;" id="gpc_checklist_container">
            <label style="display:flex;align-items:center;gap:6px;color:#fff;cursor:pointer;"><input type="checkbox" id="chk_last_px" checked onchange="toggleGpcIndicator('last_px')"> Last Px</label>
            <label style="display:flex;align-items:center;gap:6px;color:#38bdf8;cursor:pointer;"><input type="checkbox" id="chk_ma5" checked onchange="toggleGpcIndicator('ma5')"> Simple MA(5,0)</label>
            <label style="display:flex;align-items:center;gap:6px;color:#f59e0b;cursor:pointer;"><input type="checkbox" id="chk_ma10" checked onchange="toggleGpcIndicator('ma10')"> Simple MA(10,0)</label>
            <label style="display:flex;align-items:center;gap:6px;color:#ec4899;cursor:pointer;"><input type="checkbox" id="chk_ma15" checked onchange="toggleGpcIndicator('ma15')"> Simple MA(15,0)</label>
            <label style="display:flex;align-items:center;gap:6px;color:#a855f7;cursor:pointer;"><input type="checkbox" id="chk_rsi" checked onchange="toggleGpcIndicator('rsi')"> RSI(14)</label>
            <label style="display:flex;align-items:center;gap:6px;color:#10b981;cursor:pointer;"><input type="checkbox" id="chk_macd" checked onchange="toggleGpcIndicator('macd')"> MACD(12,26,9)</label>
            <label style="display:flex;align-items:center;gap:6px;color:#94a3b8;cursor:pointer;"><input type="checkbox" id="chk_stoch" onchange="toggleGpcIndicator('stoch')"> Stochastics(20,5,5,3)</label>
            <label style="display:flex;align-items:center;gap:6px;color:#94a3b8;cursor:pointer;"><input type="checkbox" id="chk_boll" onchange="toggleGpcIndicator('boll')"> Bollinger(20,2,2)</label>
            <label style="display:flex;align-items:center;gap:6px;color:#3b82f6;cursor:pointer;"><input type="checkbox" id="chk_ichimoku" checked onchange="toggleGpcIndicator('ichimoku')"> Ichimoku(9,26,26,26)</label>
            <label style="display:flex;align-items:center;gap:6px;color:#cbd5e1;cursor:pointer;"><input type="checkbox" id="chk_regress" checked onchange="toggleGpcIndicator('regress')"> Regression with Std Dev</label>
            <label style="display:flex;align-items:center;gap:6px;color:#38bdf8;cursor:pointer;"><input type="checkbox" id="chk_volume" checked onchange="toggleGpcIndicator('volume')"> Volume</label>
            <label style="display:flex;align-items:center;gap:6px;color:#ef4444;cursor:pointer;"><input type="checkbox" id="chk_vix" onchange="toggleGpcIndicator('vix')"> VIX Index Overlay</label>
          </div>
          <div style="border-top: 1px solid #162438; padding-top: 6px; margin-top: 6px;">
            <button onclick="drawTriangleBreakoutPattern()" style="width:100%;background:#450a0a;color:#fca5a5;border:1px solid #7f1d1d;padding:4px;font-size:9.5px;font-weight:700;border-radius:2px;cursor:pointer;">📐 Draw Symmetrical Triangle (Image 16)</button>
          </div>
        </div>
      </div>
    </div>

    <!-- ═══════════════════════════════════════════════════════════════ -->
    <!-- ── PRIMARY VIEW 4: READ MOST READ STORIES NEWS WIRE (SCREENSHOTS 18, 19) ── -->
    <!-- ═══════════════════════════════════════════════════════════════ -->
    <div id="bmap_view_container_news" style="display: none; background: #080d16; border: 1px solid #1e2e44; border-top: none; padding: 16px; font-family: var(--font-mono);">
      <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px; flex-wrap: wrap; gap: 8px;">
        <div style="display: flex; align-items: center; gap: 8px;">
          <span style="color: #ffaa00; font-weight: 800; font-size: 12px;">📰 READ &lt;GO&gt; — BLOOMBERG MOST READ STORIES (SCREENSHOTS 18, 19)</span>
          <span class="badge" style="background: #064e3b; color: #34d399;">STREAMING REAL-TIME</span>
        </div>
        <div style="display: flex; gap: 6px; align-items: center;">
          <select id="news_hours_filter" onchange="filterNewsHours(this.value)" style="background: #0d1726; color: #ffaa00; border: 1px solid #203a5e; border-radius: 3px; padding: 3px 8px; font-size: 10px; font-family: var(--font-mono);">
            <option value="8">Most Read News for 8 Hours</option>
            <option value="24">Most Read News for 24 Hours</option>
            <option value="all">All Available News</option>
          </select>
          <input type="text" id="news_search_input" oninput="filterNewsByText(this.value)" placeholder="Search news headlines..." style="background: #0d1726; color: #fff; border: 1px solid #203a5e; border-radius: 3px; padding: 3px 8px; font-size: 10px; font-family: var(--font-mono); width: 200px;">
        </div>
      </div>

      <div style="max-height: 600px; overflow-y: auto; display: flex; flex-direction: column; gap: 6px;" id="bmap_read_news_list"></div>
    </div>

    <!-- ═══════════════════════════════════════════════════════════════ -->
    <!-- ── PRIMARY VIEW 5: SPLC SUPPLY CHAIN ANALYSIS (SCREENSHOTS 20, 24, 25) ── -->
    <!-- ═══════════════════════════════════════════════════════════════ -->
    <div id="bmap_view_container_splc" style="display: none; background: #06090f; border: 1px solid #1e2e44; border-top: none; padding: 14px; font-family: var(--font-mono);">
      <!-- SPLC Header Ribbon -->
      <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #162438; padding-bottom: 8px; margin-bottom: 8px; flex-wrap: wrap; gap: 8px;">
        <div style="display: flex; align-items: baseline; gap: 10px;">
          <strong style="color: #ffaa00; font-size: 13px;" id="splc_firm_title">SPLC APPLE INC Equity</strong>
          <span style="color: #64748b;">|</span>
          <span style="color: #fff; font-size: 11px;">Supply Chain Network Analysis</span>
          <span style="color: #64748b;">|</span>
          <span id="splc_last_price" style="color: #ef4444; font-weight: 700;">152.352 USD -1.478</span>
        </div>
        <div style="display: flex; align-items: center; gap: 8px;">
          <span style="color: #94a3b8; font-size: 10px;">TARGET COMPANY:</span>
          <select id="splc_firm_selector" onchange="switchSplcTargetFirm(this.value)" style="background: #0d1726; color: #00e5ff; border: 1px solid #203a5e; border-radius: 3px; padding: 3px 8px; font-size: 10.5px; font-weight: 700; font-family: var(--font-mono);">
            <option value="AAPL">Apple Inc (AAPL US) — 694 Suppliers, 391 Customers</option>
            <option value="LMT">Lockheed Martin Corp (LMT US) — 244 Suppliers, 83 Customers</option>
          </select>
        </div>
      </div>

      <!-- SPLC Financial Exposure Strip (Exact Screenshots 24, 25) -->
      <div style="background: #0b1320; border: 1px solid #1a2736; border-radius: 4px; padding: 6px 12px; margin-bottom: 10px; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 12px; font-size: 10px;">
        <div style="color: #94a3b8;">
          <strong style="color: #fff;" id="splc_firm_name_label">Apple Inc</strong> Exposure to Related Companies:
        </div>
        <div style="display: flex; gap: 14px; font-size: 10px;">
          <span>Rev. Quantified: <strong style="color:#00e5ff;" id="splc_rev_quant">29.32%</strong></span>
          <span>COGS Quantified: <strong style="color:#ffaa00;" id="splc_cogs_quant">171.02%</strong></span>
          <span>CAPEX Quantified: <strong style="color:#e2e8f0;" id="splc_capex_quant">0.10%</strong></span>
          <span>SG&amp;A Quantified: <strong style="color:#e2e8f0;" id="splc_sga_quant">3.78%</strong></span>
          <span>R&amp;D Quantified: <strong style="color:#e2e8f0;" id="splc_rd_quant">0.00%</strong></span>
        </div>
      </div>

      <!-- SPLC Interactive 3-Tier Multi-Node Network Diagram -->
      <div style="display: grid; grid-template-columns: 1fr 1.2fr 1fr; gap: 12px; min-height: 520px;">
        
        <!-- Tier 1: Suppliers (Left) -->
        <div style="background: #090e18; border: 1px solid #1a2a40; border-radius: 4px; padding: 10px; display: flex; flex-direction: column;">
          <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #162438; padding-bottom: 6px; margin-bottom: 8px;">
            <strong style="color: #38bdf8; font-size: 11px;" id="splc_suppliers_count_title">694 Suppliers</strong>
            <span style="font-size: 8.5px; color: #64748b;">Sorted by COGS Exposure</span>
          </div>
          <div style="flex: 1; overflow-y: auto; display: flex; flex-direction: column; gap: 4px;" id="splc_suppliers_list"></div>
        </div>

        <!-- Tier 2: Target Anchor & Direct Competitors (Center) -->
        <div style="background: #090e18; border: 1px solid #1a2a40; border-radius: 4px; padding: 10px; display: flex; flex-direction: column; justify-content: space-between;">
          <!-- Center Target Node Box -->
          <div style="background: #1e1b4b; border: 2px solid #6366f1; border-radius: 6px; padding: 14px; text-align: center; margin-top: 20px;">
            <div style="color: #ffaa00; font-size: 9px; font-weight: 700;">ANCHOR CORPORATION</div>
            <div style="color: #fff; font-size: 15px; font-weight: 900; margin: 4px 0;" id="splc_anchor_name">Apple Inc</div>
            <div style="color: #a5b4fc; font-size: 10.5px; font-weight: 700;" id="splc_anchor_ticker">AAPL US (Consumer Hardware / Ecosystem)</div>
            <div style="margin-top: 10px; display: grid; grid-template-columns: 1fr 1fr; gap: 6px; font-size: 9.5px; text-align: left; background: #0f172a; padding: 8px; border-radius: 4px;">
              <div>Market Cap: <strong style="color:#00e676;">$2.42T</strong></div>
              <div>Gross Margin: <strong style="color:#00e5ff;">44.1%</strong></div>
              <div>Suppliers: <strong style="color:#38bdf8;" id="splc_node_sup_count">694 Nodes</strong></div>
              <div>Customers: <strong style="color:#f59e0b;" id="splc_node_cust_count">391 Nodes</strong></div>
            </div>
          </div>

          <!-- Connecting Visual Lines Placeholder -->
          <div style="text-align: center; color: #334155; font-size: 18px; margin: 10px 0;">
            ◀ ─── SUPPLY FLOW ─── [CORE VALUE CHAIN] ─── REVENUE FLOW ─── ▶
          </div>

          <!-- Bottom: Company Reported Competitors (Exact Screenshots 24, 25) -->
          <div style="background: #0f1623; border: 1px solid #1f2d42; border-radius: 4px; padding: 10px;">
            <div style="color: #ffaa00; font-size: 10px; font-weight: 800; margin-bottom: 6px;" id="splc_competitors_title">
              Company Reported Competitor(s)
            </div>
            <div style="display: flex; gap: 6px; flex-wrap: wrap;" id="splc_competitors_list"></div>
          </div>
        </div>

        <!-- Tier 3: Customers (Right) -->
        <div style="background: #090e18; border: 1px solid #1a2a40; border-radius: 4px; padding: 10px; display: flex; flex-direction: column;">
          <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #162438; padding-bottom: 6px; margin-bottom: 8px;">
            <strong style="color: #f59e0b; font-size: 11px;" id="splc_customers_count_title">391 Customers</strong>
            <span style="font-size: 8.5px; color: #64748b;">Sorted by Revenue Exposure</span>
          </div>
          <div style="flex: 1; overflow-y: auto; display: flex; flex-direction: column; gap: 4px;" id="splc_customers_list"></div>
        </div>

      </div>
    </div>

    <!-- ═══════════════════════════════════════════════════════════════ -->
    <!-- ── PRIMARY VIEW 6: FXC CURRENCY RATES MATRIX (SCREENSHOT 1) ── -->
    <!-- ═══════════════════════════════════════════════════════════════ -->
    <div id="bmap_view_container_fxc" style="display: none; background: #080d16; border: 1px solid #1e2e44; border-top: none; padding: 14px; font-family: var(--font-mono);">
      <!-- FXC Header Strip -->
      <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #162438; padding-bottom: 8px; margin-bottom: 10px; flex-wrap: wrap; gap: 8px;">
        <div style="display: flex; align-items: center; gap: 10px;">
          <strong style="color: #ffaa00; font-size: 13px;">FXC &lt;GO&gt; — CURRENCY RATES MATRIX</strong>
          <span style="color: #64748b;">|</span>
          <span style="color: #fff; font-size: 11px;">Asian Currency Crosses &amp; Heat Map</span>
        </div>
        <div style="display: flex; align-items: center; gap: 12px; font-size: 10.5px;">
          <div style="display: flex; align-items: center; gap: 4px;">
            <span style="color: #94a3b8;">Basket:</span>
            <select id="fxc_basket_select" onchange="switchFxcBasket(this.value)" style="background: #0d1726; color: #ffaa00; border: 1px solid #203a5e; border-radius: 2px; padding: 2px 6px; font-weight: 700;">
              <option value="Asia">Asia (11 Currencies)</option>
              <option value="G10">G10 Majors</option>
              <option value="EM">Emerging Markets</option>
            </select>
          </div>
          <div style="display: flex; align-items: center; gap: 4px;">
            <span style="color: #94a3b8;">Source:</span>
            <span style="color: #ffaa00; font-weight: 700;">BGN</span>
          </div>
          <div style="display: flex; align-items: center; gap: 4px;">
            <label style="color:#00e5ff;cursor:pointer;"><input type="radio" name="fxc_mode" checked> Last Price</label>
            <label style="color:#94a3b8;cursor:pointer;"><input type="radio" name="fxc_mode"> % Change</label>
          </div>
          <div style="display: flex; align-items: center; gap: 4px;">
            <span style="color: #94a3b8;">Rate:</span>
            <select style="background: #0d1726; color: #fff; border: 1px solid #203a5e; border-radius: 2px; padding: 2px 6px;">
              <option>1 Month</option>
              <option>Spot</option>
              <option>Fixing</option>
            </select>
          </div>
          <label style="display:flex;align-items:center;gap:4px;color:#34d399;cursor:pointer;"><input type="checkbox" id="chk_fxc_heatmap" checked onchange="toggleFxcHeatmap(this.checked)"> Heat Map</label>
        </div>
      </div>

      <!-- FXC Matrix Table -->
      <div style="overflow-x: auto; border: 1px solid #1a2a40; border-radius: 4px;">
        <table style="width: 100%; border-collapse: collapse; font-size: 10.5px; text-align: center;" id="fxc_matrix_table">
          <thead id="fxc_table_thead"></thead>
          <tbody id="fxc_table_tbody"></tbody>
        </table>
      </div>

      <!-- FXC % Change Day Range Legend (Exact Screenshot 1) -->
      <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 10px; padding: 6px 12px; background: #0c1422; border: 1px solid #1c2e44; border-radius: 4px; font-size: 9.5px;">
        <span style="color: #94a3b8;">% Change on Day Range:</span>
        <div style="display: flex; gap: 4px;">
          <span style="background: #991b1b; color: #fff; padding: 2px 6px; border-radius: 2px;">Below -2.5%</span>
          <span style="background: #b91c1c; color: #fff; padding: 2px 6px; border-radius: 2px;">-2.5% to -1.5%</span>
          <span style="background: #dc2626; color: #fff; padding: 2px 6px; border-radius: 2px;">-1.5% to -0.5%</span>
          <span style="background: #111a28; color: #94a3b8; padding: 2px 6px; border-radius: 2px;">-0.5% to 0.0%</span>
          <span style="background: #111a28; color: #94a3b8; padding: 2px 6px; border-radius: 2px;">0.0% to +0.5%</span>
          <span style="background: #15803d; color: #fff; padding: 2px 6px; border-radius: 2px;">+0.5% to +1.5%</span>
          <span style="background: #16a34a; color: #fff; padding: 2px 6px; border-radius: 2px;">+1.5% to +2.5%</span>
          <span style="background: #22c55e; color: #000; font-weight: 800; padding: 2px 6px; border-radius: 2px;">Above +2.5%</span>
        </div>
      </div>
    </div>

    <!-- ═══════════════════════════════════════════════════════════════ -->
    <!-- ── PRIMARY VIEW 7: VOL 3D VOLATILITY SURFACE (SCREENSHOTS 13, 17) ── -->
    <!-- ═══════════════════════════════════════════════════════════════ -->
    <div id="bmap_view_container_vol" style="display: none; background: #080d16; border: 1px solid #1e2e44; border-top: none; padding: 14px; font-family: var(--font-mono);">
      <!-- VOL Header Ribbon -->
      <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #162438; padding-bottom: 8px; margin-bottom: 10px; flex-wrap: wrap; gap: 8px;">
        <div style="display: flex; align-items: baseline; gap: 10px;">
          <strong style="color: #ffaa00; font-size: 13px;">VOL &lt;GO&gt; — TSLA US Equity — 3D Volatility Surface</strong>
          <span style="color: #64748b;">|</span>
          <span style="color: #fff; font-size: 11px;">197.62 USD Mid &nbsp; As of 03-Mar-2023 15:45</span>
        </div>
        <div style="display: flex; gap: 4px; font-size: 10px;">
          <button class="bb-key" onclick="alert('Vol Table Loaded');">1) Vol Table</button>
          <button class="bb-key" style="background:#1e3a5f;color:#00e5ff;">2) 3D Surface</button>
          <button class="bb-key" onclick="alert('Term Structure Loaded');">3) Term</button>
          <button class="bb-key" onclick="alert('Skew Matrix Loaded');">4) Skew</button>
          <button class="bb-key" onclick="alert('Dividend Curves Loaded');">5) Dividends</button>
        </div>
      </div>

      <!-- Controls sub-bar (Screenshot 13) -->
      <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px; background: #0a111e; padding: 6px 10px; border-radius: 4px; font-size: 10px;">
        <div style="display: flex; align-items: center; gap: 10px;">
          <span style="color: #ffaa00; font-weight: 700;">Moneyness ▾</span>
          <span style="color: #334155;">|</span>
          <span style="color: #38bdf8;">Listed ▾</span>
          <span style="color: #334155;">|</span>
          <label style="display:flex;align-items:center;gap:4px;color:#cbd5e1;cursor:pointer;"><input type="checkbox"> Local Vol</label>
          <label style="display:flex;align-items:center;gap:4px;color:#cbd5e1;cursor:pointer;"><input type="checkbox"> Strikes</label>
          <label style="display:flex;align-items:center;gap:4px;color:#00e5ff;cursor:pointer;"><input type="checkbox" checked> Match Scales</label>
        </div>
        <div style="display: flex; gap: 6px;">
          <button onclick="rotateVolSurface(15)" class="action-btn" style="font-size: 9px; padding: 2px 6px;">↺ Rotate</button>
          <button onclick="resetVolSurfaceView()" class="action-btn" style="font-size: 9px; padding: 2px 6px;">⌖ Reset View</button>
        </div>
      </div>

      <!-- 3D Perspective Canvas Container -->
      <div style="position: relative; width: 100%; height: 520px; background: #000; border: 1px solid #1a2a40; border-radius: 4px; overflow: hidden;">
        <canvas id="vol_surface_canvas" style="width: 100%; height: 100%;"></canvas>
        <div style="position: absolute; bottom: 12px; left: 16px; font-size: 9px; color: #64748b;">
          Axes: Term (10 Mar 2023 - 31 Dec 2032) × Moneyness (80% - 120%) × Implied Vol (50% - 75%)
        </div>
        <div style="position: absolute; bottom: 12px; right: 16px; font-size: 9px; color: #22c55e;">
          ● Interactive Volatility Surface Mesh Active
        </div>
      </div>
    </div>
    """
    
    with open(os.path.join(BASE_DIR, "bmap_html_template.html"), "w", encoding="utf-8") as f:
        f.write(html.strip())
    print(f"Generated bmap_html_template.html ({len(html)} bytes)")

if __name__ == "__main__":
    generate_html()

