import re

# 1. Update bmap_js_template.js
js_path = 'F:/documents/SOIC/EconAgent_Platform/platform_ui/bmap_js_template.js'
with open(js_path, 'r', encoding='utf-8') as f:
    js = f.read()

# Add 'gev' to views in switchBmapView
old_views = "var views = ['map', 'table', 'chart', 'news', 'splc', 'fxc', 'vol', 'soic'];"
new_views = "var views = ['map', 'gev', 'table', 'chart', 'news', 'splc', 'fxc', 'vol', 'soic'];"
if old_views in js:
    js = js.replace(old_views, new_views, 1)

# Check GEV server status when switching to 'gev'
old_switch_hook = "if (viewId === 'map' && leafletMap) {"
new_switch_hook = """if (viewId === 'gev') {
      window.checkGodsEyeServerStatus();
    } else if (viewId === 'map' && leafletMap) {"""
if old_switch_hook in js and "viewId === 'gev'" not in js:
    js = js.replace(old_switch_hook, new_switch_hook, 1)

with open(js_path, 'w', encoding='utf-8') as f:
    f.write(js)
print("Updated bmap_js_template.js switchBmapView with 'gev' view!")

# 2. Update bmap_html_template.html
html_path = 'F:/documents/SOIC/EconAgent_Platform/platform_ui/bmap_html_template.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Add top tab
old_tab_marker = '''      <div style="background: #1e3a5f; color: #00e5ff; border: 1px solid #3b82f6; border-bottom: none; padding: 2px 10px; border-radius: 3px 3px 0 0; font-size: 10px; font-weight: 800; display: flex; align-items: center; gap: 6px;">
        <span>MAP Custom Map</span>
        <span style="font-size: 9px; cursor: pointer;" onclick="alert('Default Map Locked');">✕</span>
      </div>'''

new_tab_marker = '''      <div id="bmap_btn_view_map" style="background: #1e3a5f; color: #00e5ff; border: 1px solid #3b82f6; border-bottom: 2px solid #00e5ff; padding: 2px 10px; border-radius: 3px 3px 0 0; font-size: 10px; font-weight: 800; display: flex; align-items: center; gap: 6px; cursor: pointer;" onclick="switchBmapView('map')">
        <span>🗺️ MAP Custom Map</span>
      </div>
      <div id="bmap_btn_view_gev" style="background: #0d1726; color: #38bdf8; border: 1px solid #0284c7; padding: 2px 10px; border-radius: 3px 3px 0 0; font-size: 10px; font-weight: 800; cursor: pointer; display: flex; align-items: center; gap: 4px; box-shadow: 0 0 8px rgba(0,229,255,0.3);" onclick="switchBmapView('gev')">
        <span>🌍 3D GOD'S EYE VIEW</span>
      </div>'''

if old_tab_marker in html:
    html = html.replace(old_tab_marker, new_tab_marker, 1)
    print("Added 3D GOD'S EYE VIEW tab in top navigation!")

# Update basemap button to call switchBmapView('gev')
old_gev_btn = '''<button onclick="toggleGodsEyeView3D()" id="btn_toggle_gods_eye_3d" class="action-btn" style="font-size: 9px; padding: 3px 8px; background: linear-gradient(135deg, #0d3b66 0%, #005f73 100%); color: #38bdf8; border: 1.5px solid #00e5ff; font-weight: 800; display: inline-flex; align-items: center; gap: 4px; box-shadow: 0 0 10px rgba(0,229,255,0.4); cursor: pointer;">
          <span style="font-size: 11px;">🌍</span> 3D GOD'S EYE VIEW
        </button>'''

new_gev_btn = '''<button onclick="switchBmapView('gev')" id="btn_toggle_gods_eye_3d" class="action-btn" style="font-size: 9px; padding: 3px 8px; background: linear-gradient(135deg, #0d3b66 0%, #005f73 100%); color: #38bdf8; border: 1.5px solid #00e5ff; font-weight: 800; display: inline-flex; align-items: center; gap: 4px; box-shadow: 0 0 10px rgba(0,229,255,0.4); cursor: pointer;">
          <span style="font-size: 11px;">🌍</span> 3D GOD'S EYE VIEW
        </button>'''

if old_gev_btn in html:
    html = html.replace(old_gev_btn, new_gev_btn, 1)

# Add bmap_view_container_gev at the bottom of views
gev_view_html = '''
<!-- ── SECONDARY VIEW 9: GOD'S EYE VIEW 3D WORKSTATION (CESIUM / VITE POWERED) ── -->
<div id="bmap_view_container_gev" style="display: none; background: #00040a; border: 1px solid #1e2e44; border-top: none; font-family: var(--font-mono);">
  <!-- Top 3D Control Header -->
  <div style="height: 42px; background: rgba(5,8,15,0.96); border-bottom: 1.5px solid #00e5ff; display: flex; justify-content: space-between; align-items: center; padding: 0 14px; box-shadow: 0 4px 18px rgba(0,0,0,0.9);">
    <div style="display: flex; align-items: center; gap: 12px;">
      <button onclick="switchBmapView('map')" style="background: #1e293b; color: #fff; border: 1px solid #475569; padding: 5px 12px; font-size: 10px; font-weight: 800; border-radius: 3px; cursor: pointer;">
        ← Return to 2D BMAP
      </button>
      <span style="color: #00e5ff; font-weight: 900; font-size: 12px; letter-spacing: 0.5px;">🌍 GOD'S EYE VIEW 3D WORKSTATION</span>
      <span style="color: #64748b; font-size: 10.5px;">(Photorealistic Cesium 3D Engine · Bilawal Sidhu / EconAgent)</span>
      <div id="gev_server_status_pill" style="background: rgba(16,185,129,0.15); border: 1px solid #10b981; color: #34d399; font-size: 10px; padding: 3px 10px; border-radius: 3px; font-weight: 700;">
        ● VITE 3D SERVER ONLINE (Port 4173)
      </div>
    </div>
    <div style="display: flex; align-items: center; gap: 8px;">
      <button onclick="document.getElementById('gev_iframe').src = 'http://localhost:4173'" style="background: #0f172a; color: #38bdf8; border: 1px solid #1e3a5f; padding: 4px 10px; font-size: 9.5px; border-radius: 3px; cursor: pointer;">
        🔄 Reload 3D Frame
      </button>
      <a href="http://localhost:4173" target="_blank" style="background: #0284c7; color: #fff; text-decoration: none; border: 1px solid #38bdf8; padding: 5px 14px; font-size: 10px; font-weight: 800; border-radius: 3px; display: inline-flex; align-items: center; gap: 4px;">
        ↗ Pop-out Fullscreen
      </a>
    </div>
  </div>

  <!-- Live Vite 3D Engine Frame (Runs http://localhost:4173) -->
  <div style="position: relative; width: 100%; height: 740px;">
    <iframe id="gev_iframe" src="http://localhost:4173" style="width: 100%; height: 100%; border: none;" allow="accelerometer; autoplay; camera; encrypted-media; geolocation; gyroscope; microphone; midi; payment; usb; vr; xr-spatial-tracking"></iframe>

    <!-- Fallback Box if server not running -->
    <div id="gev_fallback_box" style="display: none; position: absolute; top: 80px; left: 50%; transform: translateX(-50%); width: 620px; background: rgba(5,8,15,0.96); border: 1.5px solid #ef4444; border-radius: 6px; padding: 22px; color: #fff; box-shadow: 0 10px 40px rgba(0,0,0,0.9); z-index: 950; text-align: center;">
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
        <button onclick="switchBmapView('map')" style="background: #1e293b; color: #94a3b8; border: 1px solid #475569; padding: 6px 14px; border-radius: 3px; font-weight: 800; cursor: pointer; font-size: 11px;">
          Back to 2D BMAP
        </button>
      </div>
    </div>
  </div>
</div>
'''

if 'id="bmap_view_container_gev"' not in html:
    html += '\n' + gev_view_html
    print("Added bmap_view_container_gev to bmap_html_template.html!")

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated bmap_html_template.html successfully!")

