import re

# 1. Patch bmap_html_template.html
with open('platform_ui/bmap_html_template.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace US-centric dropdown options
html = html.replace('<option value="bank_branches">🏛️ US Bank Branches (1,675 FDIC Clusters)</option>',
                    '<option value="bank_branches">🏛️ Global Wealth Hubs &amp; Bank Branches (1,727 Global Nodes)</option>')
html = html.replace('<option value="natural_gas">⛽ North American Natural Gas Network (Image 12)</option>',
                    '<option value="natural_gas">⛽ Global Natural Gas Pipelines &amp; LNG Terminals (Image 12)</option>')

# Replace bottom-left floating legends
html = html.replace('<div style="color: #94a3b8; font-size: 10px; font-weight: 700; margin-bottom: 2px; letter-spacing: 0.5px;">Bank Branches (US)</div>',
                    '<div style="color: #c084fc; font-size: 10px; font-weight: 700; margin-bottom: 2px; letter-spacing: 0.5px;">Bank Branches &amp; Global Wealth Hubs</div>')
html = html.replace('<div style="color: #fff; font-size: 10px; font-weight: 800; margin-bottom: 4px;">Pipelines (N.Am.)</div>',
                    '<div style="color: #00e5ff; font-size: 10px; font-weight: 800; margin-bottom: 4px;">Global Pipelines Network (Gas &amp; Crude)</div>')

# Upgrade GEV 3D container in HTML to have dual-engine toggle and iframe fallback
gev_old = '''  <!-- Native 3D WebGL Cesium Workstation Container -->
  <div style="position: relative; width: 100%; height: 740px; background: #000;">
    <div id="gev_native_cesium_container" style="width: 100%; height: 100%; background: #000; position: relative;"></div>

    <!-- 3D HUD Telemetry Overlay -->
    <div style="position: absolute; bottom: 12px; left: 16px; background: rgba(5,8,15,0.85); backdrop-filter: blur(8px); border: 1px solid #1e3a5f; border-radius: 4px; padding: 8px 14px; font-family: var(--font-mono); font-size: 10px; color: #94a3b8; pointer-events: none; z-index: 50; display: flex; gap: 14px; align-items: center;">
      <div><span style="color:#00e5ff;font-weight:800;">3D ENGINE:</span> CesiumJS WebGL</div>
      <div><span style="color:#ffaa00;font-weight:800;">AIS VESSELS:</span> 60 Active</div>
      <div><span style="color:#34d399;font-weight:800;">PIPELINES:</span> Petroline &amp; US Transco</div>
      <div><span style="color:#c084fc;font-weight:800;">CABLES:</span> Submarine Grid</div>
      <div id="cesium_hud_coords"><span style="color:#fff;font-weight:700;">HORMUZ RADAR · 26.4°N, 56.2°E</span></div>
    </div>
  </div>'''

gev_new = '''  <!-- Dual 3D WebGL Cesium Workstation Container (Native Engine + Bilawal Sidhu Microservice) -->
  <div style="position: relative; width: 100%; height: 740px; background: #000;">
    <!-- 1. Native Embedded Cesium 3D Globe (Instant / Zero Servers Needed) -->
    <div id="gev_native_cesium_container" style="width: 100%; height: 100%; background: #000; position: relative; display: block;"></div>

    <!-- 2. Bilawal Sidhu Full Vue/Cesium Workstation Stream (Port 4173) -->
    <iframe id="gev_iframe" src="about:blank" style="display: none; width: 100%; height: 100%; border: none; background: #00040a;"></iframe>

    <!-- 3. Server Offline Guidance Overlay (Shown only if user selects Port 4173 mode while server is offline) -->
    <div id="gev_fallback_box" style="display: none; position: absolute; top: 120px; left: 50%; transform: translateX(-50%); background: rgba(5,8,15,0.95); border: 1.5px solid #ef4444; border-radius: 6px; padding: 22px 28px; text-align: center; max-width: 540px; z-index: 60; box-shadow: 0 10px 40px rgba(0,0,0,0.9);">
      <div style="color: #ef4444; font-size: 15px; font-weight: 900; margin-bottom: 8px;">⚡ God's Eye View 3D Server Not Detected on Port 4173</div>
      <p style="color: #cbd5e1; font-size: 11px; line-height: 1.6; margin-bottom: 14px;">
        To stream Bilawal Sidhu's interactive Vue 3D console, run the background launcher:<br>
        <code style="color: #ffaa00; background: #0f172a; padding: 3px 8px; border-radius: 3px; font-size: 10.5px; border: 1px solid #1e293b; display: inline-block; margin-top: 5px;">F:\\documents\\SOIC\\Launch_Gods_Eye_View.bat</code>
      </p>
      <div style="display: flex; gap: 10px; justify-content: center; flex-wrap: wrap;">
        <button onclick="window.set3DMode('native')" style="background: #0284c7; color: #fff; border: none; padding: 6px 14px; font-size: 11px; font-weight: 800; border-radius: 3px; cursor: pointer;">
          🌐 Switch to Instant Native 3D Globe
        </button>
        <button onclick="window.checkGodsEyeServerStatus(true)" style="background: #10b981; color: #fff; border: none; padding: 6px 14px; font-size: 11px; font-weight: 800; border-radius: 3px; cursor: pointer;">
          ↻ Check Port 4173 Again
        </button>
      </div>
    </div>

    <!-- 3D HUD Telemetry Overlay -->
    <div style="position: absolute; bottom: 12px; left: 16px; background: rgba(5,8,15,0.85); backdrop-filter: blur(8px); border: 1px solid #1e3a5f; border-radius: 4px; padding: 8px 14px; font-family: var(--font-mono); font-size: 10px; color: #94a3b8; pointer-events: none; z-index: 50; display: flex; gap: 14px; align-items: center;">
      <div><span style="color:#00e5ff;font-weight:800;">3D ENGINE:</span> <span id="cesium_hud_engine">CesiumJS WebGL (Native)</span></div>
      <div><span style="color:#ffaa00;font-weight:800;">AIS VESSELS:</span> 60 Active</div>
      <div><span style="color:#34d399;font-weight:800;">PIPELINES:</span> GAIL HVJ, Petroline &amp; Transco</div>
      <div><span style="color:#c084fc;font-weight:800;">CABLES:</span> Submarine Global Grid</div>
      <div id="cesium_hud_coords"><span style="color:#fff;font-weight:700;">HORMUZ RADAR · 26.4°N, 56.2°E</span></div>
    </div>
  </div>'''

html = html.replace(gev_old, gev_new)

# Add engine mode switch buttons in GEV header
old_gev_header = '''      <div id="gev_server_status_pill" style="background: rgba(16,185,129,0.15); border: 1px solid #10b981; color: #34d399; font-size: 10px; padding: 3px 10px; border-radius: 3px; font-weight: 800; display: flex; align-items: center; gap: 4px;">
        <span style="color:#00e676;">●</span> NATIVE CESIUM 3D ONLINE (Hardware Accelerated)
      </div>'''

new_gev_header = '''      <div style="display: flex; gap: 4px; align-items: center;">
        <button id="btn_mode_native_3d" onclick="window.set3DMode('native')" style="background: #0284c7; color: #fff; border: 1px solid #38bdf8; padding: 3px 8px; font-size: 9.5px; font-weight: 800; border-radius: 3px; cursor: pointer;">🌐 Native 3D Globe</button>
        <button id="btn_mode_server_3d" onclick="window.set3DMode('server')" style="background: #0f172a; color: #94a3b8; border: 1px solid #1e293b; padding: 3px 8px; font-size: 9.5px; font-weight: 800; border-radius: 3px; cursor: pointer;">⚡ Bilawal Sidhu 3D (Port 4173)</button>
      </div>
      <div id="gev_server_status_pill" style="background: rgba(2,132,199,0.15); border: 1px solid #0284c7; color: #38bdf8; font-size: 10px; padding: 3px 10px; border-radius: 3px; font-weight: 800; display: flex; align-items: center; gap: 4px;">
        <span style="color:#00e5ff;">●</span> NATIVE 3D WEBGL ACTIVE (Instant)
      </div>'''

html = html.replace(old_gev_header, new_gev_header)

with open('platform_ui/bmap_html_template.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("bmap_html_template.html successfully patched!")

