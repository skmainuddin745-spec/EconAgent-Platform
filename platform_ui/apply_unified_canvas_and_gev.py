import os, sys

def main():
    print("Applying Unified Master Canvas & God's Eye View integration...")
    
    # --- 1. UPDATE bmap_html_template.html ---
    html_path = 'F:/documents/SOIC/EconAgent_Platform/platform_ui/bmap_html_template.html'
    with open(html_path, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # Fix pointer-events on legends container
    old_legend = 'id="bmap_legends_container" style="position: absolute; bottom: 25px; left: 16px; z-index: 100; display: flex; flex-direction: column; gap: 8px; pointer-events: auto;"'
    new_legend = 'id="bmap_legends_container" style="position: absolute; bottom: 25px; left: 16px; z-index: 100; display: flex; flex-direction: column; gap: 8px; pointer-events: none !important;"'
    if old_legend in html:
        html = html.replace(old_legend, new_legend)
        print("Updated bmap_legends_container pointer-events to none !important")
    
    # Add 3D God's Eye View button to basemap switchers bar
    old_base_bar = '''      <div style="display: flex; gap: 4px; background: rgba(5,8,15,0.94); border: 1px solid #223750; border-radius: 4px; padding: 2px;">
        <button onclick="setBmapTileLayer('dark')" id="bmap_layer_dark" class="action-btn active" style="font-size: 9px; padding: 3px 6px;">🌑 Bloomberg Dark</button>
        <button onclick="setBmapTileLayer('satellite')" id="bmap_layer_sat" class="action-btn" style="font-size: 9px; padding: 3px 6px;">🛰️ Real Satellite</button>
        <button onclick="setBmapTileLayer('nautical')" id="bmap_layer_naut" class="action-btn" style="font-size: 9px; padding: 3px 6px;">🗺️ Nautical Chart</button>
        <button onclick="setBmapTileLayer('auto')" id="bmap_layer_auto" class="action-btn" style="font-size: 9px; padding: 3px 6px;">🌐 Auto-Adaptive</button>
      </div>'''

    new_base_bar = '''      <div style="display: flex; gap: 4px; background: rgba(5,8,15,0.94); border: 1px solid #223750; border-radius: 4px; padding: 2px;">
        <button onclick="setBmapTileLayer('dark')" id="bmap_layer_dark" class="action-btn active" style="font-size: 9px; padding: 3px 6px;">🌑 Bloomberg Dark</button>
        <button onclick="setBmapTileLayer('satellite')" id="bmap_layer_sat" class="action-btn" style="font-size: 9px; padding: 3px 6px;">🛰️ Real Satellite</button>
        <button onclick="setBmapTileLayer('nautical')" id="bmap_layer_naut" class="action-btn" style="font-size: 9px; padding: 3px 6px;">🗺️ Nautical Chart</button>
        <button onclick="setBmapTileLayer('auto')" id="bmap_layer_auto" class="action-btn" style="font-size: 9px; padding: 3px 6px;">🌐 Auto-Adaptive</button>
        <button onclick="toggleGodsEyeView3D()" id="btn_toggle_gods_eye_3d" class="action-btn" style="font-size: 9px; padding: 3px 8px; background: linear-gradient(135deg, #0d3b66 0%, #005f73 100%); color: #38bdf8; border: 1.5px solid #00e5ff; font-weight: 800; display: inline-flex; align-items: center; gap: 4px; box-shadow: 0 0 10px rgba(0,229,255,0.4); cursor: pointer;">
          <span style="font-size: 11px;">🌍</span> 3D GOD'S EYE VIEW
        </button>
      </div>'''

    if old_base_bar in html:
        html = html.replace(old_base_bar, new_base_bar)
        print("Added 3D God's Eye View button to top navigation bar")

    # Add Fullscreen 3D Globe Workstation container before the closing div
    gev_container_html = '''
    <!-- ── FULLSCREEN 3D GOD'S EYE VIEW WORKSTATION (CESIUM / VITE POWERED) ── -->
    <div id="bmap_3d_globe_container" style="display: none; position: absolute; top: 0; left: 0; width: 100%; height: 100%; z-index: 850; background: #00040a;">
      <!-- Top 3D Control Header -->
      <div style="position: absolute; top: 0; left: 0; right: 0; height: 38px; background: rgba(5,8,15,0.96); border-bottom: 1.5px solid #00e5ff; display: flex; justify-content: space-between; align-items: center; padding: 0 12px; z-index: 900; font-family: var(--font-mono); box-shadow: 0 4px 18px rgba(0,0,0,0.9);">
        <div style="display: flex; align-items: center; gap: 10px;">
          <button onclick="toggleGodsEyeView3D(false)" style="background: #1e293b; color: #fff; border: 1px solid #475569; padding: 4px 10px; font-size: 10px; font-weight: 800; border-radius: 3px; cursor: pointer; display: flex; align-items: center; gap: 4px;">
            ← Back to 2D BMAP
          </button>
          <span style="color: #00e5ff; font-weight: 900; font-size: 11px; letter-spacing: 0.5px;">🌍 GOD'S EYE VIEW 3D WORKSTATION</span>
          <span style="color: #64748b; font-size: 10px;">(Photorealistic Cesium Engine · Bilawal Sidhu / EconAgent)</span>
          <div id="gev_server_status_pill" style="background: rgba(16,185,129,0.15); border: 1px solid #10b981; color: #34d399; font-size: 9.5px; padding: 2px 8px; border-radius: 3px; font-weight: 700;">
            ● VITE 3D SERVER ONLINE (Port 4173)
          </div>
        </div>
        <div style="display: flex; align-items: center; gap: 6px;">
          <button onclick="jumpGevCamera('hormuz')" style="background: #0f172a; color: #38bdf8; border: 1px solid #1e3a5f; padding: 3px 8px; font-size: 9px; border-radius: 2px; cursor: pointer;">🔍 Hormuz</button>
          <button onclick="jumpGevCamera('petroline')" style="background: #0f172a; color: #ffaa00; border: 1px solid #451a03; padding: 3px 8px; font-size: 9px; border-radius: 2px; cursor: pointer;">🛢️ Petroline</button>
          <button onclick="jumpGevCamera('cables')" style="background: #0f172a; color: #a855f7; border: 1px solid #3b0764; padding: 3px 8px; font-size: 9px; border-radius: 2px; cursor: pointer;">🌐 712 Cables</button>
          <button onclick="jumpGevCamera('orbit')" style="background: #0f172a; color: #00e676; border: 1px solid #064e3b; padding: 3px 8px; font-size: 9px; border-radius: 2px; cursor: pointer;">🛰️ Orbit</button>
          <a href="http://localhost:4173" target="_blank" style="background: #0284c7; color: #fff; text-decoration: none; border: 1px solid #38bdf8; padding: 3px 10px; font-size: 9.5px; font-weight: 800; border-radius: 3px; display: inline-flex; align-items: center; gap: 3px;">
            ↗ Pop-out Window
          </a>
        </div>
      </div>

      <!-- Live Vite 3D Engine Frame (Runs http://localhost:4173) -->
      <iframe id="gev_iframe" src="http://localhost:4173" style="width: 100%; height: calc(100% - 38px); margin-top: 38px; border: none;" allow="accelerometer; autoplay; camera; encrypted-media; geolocation; gyroscope; microphone; midi; payment; usb; vr; xr-spatial-tracking"></iframe>

      <!-- Fallback / Server Launcher Card (Only shown if Vite server not running) -->
      <div id="gev_fallback_box" style="display: none; position: absolute; top: 70px; left: 50%; transform: translateX(-50%); width: 620px; background: rgba(5,8,15,0.96); border: 1.5px solid #ef4444; border-radius: 6px; padding: 20px; font-family: var(--font-mono); color: #fff; box-shadow: 0 10px 40px rgba(0,0,0,0.9); z-index: 950; text-align: center;">
        <div style="font-size: 16px; font-weight: 900; color: #f87171; margin-bottom: 8px;">⚡ God's Eye View 3D Server Not Detected on Port 4173</div>
        <div style="font-size: 11px; color: #94a3b8; line-height: 1.6; margin-bottom: 14px;">
          The 3D Photorealistic Cesium workstation is ready to launch. You can start it in 1 click using the batch launcher script in your workspace:
        </div>
        <div style="background: #090e17; border: 1px solid #203a5e; border-radius: 4px; padding: 10px; font-size: 11px; color: #ffaa00; margin-bottom: 14px; text-align: left; font-family: monospace;">
          F:\\documents\\SOIC\\Launch_Gods_Eye_View.bat
        </div>
        <div style="display: flex; justify-content: center; gap: 10px;">
          <button onclick="checkGodsEyeServerStatus()" style="background: #0284c7; color: #fff; border: 1px solid #38bdf8; padding: 6px 16px; border-radius: 3px; font-weight: 800; cursor: pointer; font-size: 11px;">
            🔄 Refresh Status
          </button>
          <button onclick="toggleGodsEyeView3D(false)" style="background: #1e293b; color: #94a3b8; border: 1px solid #475569; padding: 6px 14px; border-radius: 3px; font-weight: 800; cursor: pointer; font-size: 11px;">
            Back to 2D BMAP
          </button>
        </div>
      </div>
    </div>
'''

    if 'id="bmap_3d_globe_container"' not in html:
        # insert before the closing modal or drawer
        insert_marker = '  <!-- ── AUTHENTIC MAP CONTENT DATASETS DRAWER'
        if insert_marker in html:
            html = html.replace(insert_marker, gev_container_html + '\n' + insert_marker)
            print("Inserted bmap_3d_globe_container into HTML")

    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print("bmap_html_template.html successfully updated!")

    # --- 2. UPDATE bmap_js_template.js ---
    js_path = 'F:/documents/SOIC/EconAgent_Platform/platform_ui/bmap_js_template.js'
    with open(js_path, 'r', encoding='utf-8') as f:
        js = f.read()

    # Add masterCanvasRenderer in initLeafletBmap
    target_init = '    // Initialize All Layer Groups\n    initBankBranchesLayer();'
    replacement_init = '''    // Master unified canvas renderer with high hit tolerance (14px) for 100% responsive hover
    var masterCanvasRenderer = L.canvas({ padding: 0.5, tolerance: 14 });
    window.masterCanvasRenderer = masterCanvasRenderer;

    // Initialize All Layer Groups
    initBankBranchesLayer();'''

    if target_init in js and 'window.masterCanvasRenderer' not in js:
        js = js.replace(target_init, replacement_init, 1)
        print("Added masterCanvasRenderer to initLeafletBmap")

    # Update initPipelinesLayers
    old_crude_hb = '''    crudePipelines.forEach(function(pipe) {
      // Invisible wide hit buffer (22px) for effortless mouse targeting
      var hitBuffer = L.polyline(pipe.coords, {
        weight: 22,
        opacity: 0,
        interactive: true
      });

      // Visual line
      var poly = L.polyline(pipe.coords, {
        color: pipe.color || '#00e5ff',
        weight: 4.5,
        opacity: 0.92,
        lineCap: 'round',
        lineJoin: 'round'
      });'''

    new_crude_hb = '''    crudePipelines.forEach(function(pipe) {
      var rdr = window.masterCanvasRenderer;
      // Invisible wide hit buffer (24px) on master canvas for effortless mouse targeting
      var hitBuffer = L.polyline(pipe.coords, {
        renderer: rdr,
        weight: 24,
        opacity: 0.001,
        interactive: true
      });

      // Visual line on master canvas
      var poly = L.polyline(pipe.coords, {
        renderer: rdr,
        color: pipe.color || '#00e5ff',
        weight: 4.5,
        opacity: 0.92,
        lineCap: 'round',
        lineJoin: 'round',
        interactive: true
      });'''

    if old_crude_hb in js:
        js = js.replace(old_crude_hb, new_crude_hb, 1)
        print("Updated crudePipelines to use masterCanvasRenderer with 24px hit buffer")

    # Update gasPipelines
    old_gas_hb = '''    gasPipelines.forEach(function(gpipe) {
      var hitBuffer = L.polyline(gpipe.coords, { weight: 20, opacity: 0, interactive: true });
      var poly = L.polyline(gpipe.coords, {
        color: gpipe.color || '#f97316',
        weight: 4,
        opacity: 0.88,
        dashArray: '6, 6'
      });'''

    new_gas_hb = '''    gasPipelines.forEach(function(gpipe) {
      var rdr = window.masterCanvasRenderer;
      var hitBuffer = L.polyline(gpipe.coords, { renderer: rdr, weight: 22, opacity: 0.001, interactive: true });
      var poly = L.polyline(gpipe.coords, {
        renderer: rdr,
        color: gpipe.color || '#f97316',
        weight: 4,
        opacity: 0.88,
        dashArray: '6, 6',
        interactive: true
      });'''

    if old_gas_hb in js:
        js = js.replace(old_gas_hb, new_gas_hb, 1)
        print("Updated gasPipelines to use masterCanvasRenderer")

    # Update initSubmarineCablesLayer
    old_cables = '''      cable.lines.forEach(function(lineCoords) {
        if (!lineCoords || lineCoords.length < 2) return;
        var hitBuffer = L.polyline(lineCoords, { weight: 20, opacity: 0, interactive: true });
        var poly = L.polyline(lineCoords, {
          color: cable.color || '#38bdf8',
          weight: 2.2,
          opacity: 0.85,
          lineCap: 'round',
          lineJoin: 'round'
        });'''

    new_cables = '''      cable.lines.forEach(function(lineCoords) {
        if (!lineCoords || lineCoords.length < 2) return;
        var rdr = window.masterCanvasRenderer;
        var hitBuffer = L.polyline(lineCoords, { renderer: rdr, weight: 20, opacity: 0.001, interactive: true });
        var poly = L.polyline(lineCoords, {
          renderer: rdr,
          color: cable.color || '#38bdf8',
          weight: 2.2,
          opacity: 0.85,
          lineCap: 'round',
          lineJoin: 'round',
          interactive: true
        });'''

    if old_cables in js:
        js = js.replace(old_cables, new_cables, 1)
        print("Updated submarineCables to use masterCanvasRenderer")

    # Replace local canvasRenderer in layer functions with window.masterCanvasRenderer
    js = js.replace(
        '  function initGlobalInfrastructureLayers() {\n    var canvasRenderer = L.canvas({ padding: 0.5 });',
        '  function initGlobalInfrastructureLayers() {\n    var canvasRenderer = window.masterCanvasRenderer || L.canvas({ padding: 0.5, tolerance: 14 });'
    )

    js = js.replace(
        '  function initDenseGridLayer() {\n    var grp = L.layerGroup();\n    var canvasRenderer = L.canvas({ padding: 0.5 });',
        '  function initDenseGridLayer() {\n    var grp = L.layerGroup();\n    var canvasRenderer = window.masterCanvasRenderer || L.canvas({ padding: 0.5, tolerance: 14 });'
    )

    js = js.replace(
        '  function initWorldEquityLayer() {\n    var grp = L.layerGroup();\n    var canvasRenderer = L.canvas({ padding: 0.5 });',
        '  function initWorldEquityLayer() {\n    var grp = L.layerGroup();\n    var canvasRenderer = window.masterCanvasRenderer || L.canvas({ padding: 0.5, tolerance: 14 });'
    )

    js = js.replace(
        '  function initBankBranchesLayer() {\n    bankBranchesLayerGroup = L.layerGroup();\n    var canvasRenderer = L.canvas({ padding: 0.5 });',
        '  function initBankBranchesLayer() {\n    bankBranchesLayerGroup = L.layerGroup();\n    var canvasRenderer = window.masterCanvasRenderer || L.canvas({ padding: 0.5, tolerance: 14 });'
    )

    js = js.replace(
        '    var quakesLayer = L.layerGroup();\n    var canvasRenderer = L.canvas({ padding: 0.5 });',
        '    var quakesLayer = L.layerGroup();\n    var canvasRenderer = window.masterCanvasRenderer || L.canvas({ padding: 0.5, tolerance: 14 });'
    )

    # Add GEV 3D controller functions
    gev_functions = """
  // ── GOD'S EYE VIEW 3D WORKSTATION CONTROLLER ──
  // ═══════════════════════════════════════════════════════════════
  window.toggleGodsEyeView3D = function(forceState) {
    var cont = document.getElementById('bmap_3d_globe_container');
    var btn = document.getElementById('btn_toggle_gods_eye_3d');
    if (!cont) return;
    var isShowing = (cont.style.display === 'block');
    var next = (forceState !== undefined) ? forceState : !isShowing;
    cont.style.display = next ? 'block' : 'none';
    if (btn) {
      btn.style.background = next ? 'linear-gradient(135deg, #059669 0%, #047857 100%)' : 'linear-gradient(135deg, #0d3b66 0%, #005f73 100%)';
      btn.style.borderColor = next ? '#10b981' : '#00e5ff';
      btn.innerHTML = next ? '<span style="font-size:11px;">🗺️</span> 2D BMAP VIEW' : '<span style="font-size:11px;">🌍</span> 3D GOD\\'S EYE VIEW';
    }
    if (next) {
      window.checkGodsEyeServerStatus();
    }
  };

  window.checkGodsEyeServerStatus = function() {
    var iframe = document.getElementById('gev_iframe');
    var statusPill = document.getElementById('gev_server_status_pill');
    var fallbackBox = document.getElementById('gev_fallback_box');
    
    // Check if Vite port 4173 is responding
    fetch('http://localhost:4173', { mode: 'no-cors' })
      .then(function() {
        if (statusPill) {
          statusPill.innerHTML = '<span style="color:#00e676;">●</span> VITE 3D SERVER ONLINE (Port 4173)';
          statusPill.style.background = 'rgba(16,185,129,0.15)';
          statusPill.style.borderColor = '#10b981';
          statusPill.style.color = '#34d399';
        }
        if (iframe) iframe.style.display = 'block';
        if (fallbackBox) fallbackBox.style.display = 'none';
      })
      .catch(function(err) {
        if (statusPill) {
          statusPill.innerHTML = '<span style="color:#ef4444;">●</span> VITE SERVER OFFLINE — Run Launch_Gods_Eye_View.bat';
          statusPill.style.background = 'rgba(239,68,68,0.15)';
          statusPill.style.borderColor = '#ef4444';
          statusPill.style.color = '#f87171';
        }
        if (fallbackBox) fallbackBox.style.display = 'block';
      });
  };

  window.jumpGevCamera = function(preset) {
    var iframe = document.getElementById('gev_iframe');
    if (!iframe) return;
    try {
      iframe.contentWindow.postMessage({ type: 'GEV_CAMERA_JUMP', preset: preset }, '*');
    } catch(e) {}
  };
"""

    target_bottom = '  // ── AUTO-INITIALIZATION ──'
    if 'window.toggleGodsEyeView3D' not in js and target_bottom in js:
        js = js.replace(target_bottom, gev_functions + '\n  // ── AUTO-INITIALIZATION ──', 1)
        print("Added GEV 3D controller functions to bmap_js_template.js")

    with open(js_path, 'w', encoding='utf-8') as f:
        f.write(js)
    print("bmap_js_template.js successfully updated!")

if __name__ == '__main__':
    main()

