import re
import os

BASE_DIR = r"F:\documents\SOIC\EconAgent_Platform\platform_ui"

# 1. UPDATE bmap_html_template.html
html_path = os.path.join(BASE_DIR, "bmap_html_template.html")
with open(html_path, "r", encoding="utf-8") as f:
    html = f.read()

# Replace static navigation span with interactive West / East buttons
old_nav_span = '<span style="color: #64748b; cursor: pointer;">&lt; &gt;</span>'
new_nav_buttons = '''<div style="display: flex; align-items: center; gap: 4px;">
        <button id="btn_bmap_nav_west" onclick="bmapNavigateWest()" style="background: #0f1c2e; color: #38bdf8; border: 1px solid #0284c7; border-radius: 3px; padding: 2px 9px; font-size: 11px; font-weight: 800; cursor: pointer; display: flex; align-items: center; gap: 4px; box-shadow: 0 1px 4px rgba(0,0,0,0.5);" title="Navigate West: North America (US Nationwide Banks, FDIC Hubs, Interstate Pipelines)">
          <span>◀ West (North America)</span>
        </button>
        <button id="btn_bmap_nav_east" onclick="bmapNavigateEast()" style="background: #0f1c2e; color: #ffaa00; border: 1px solid #d97706; border-radius: 3px; padding: 2px 9px; font-size: 11px; font-weight: 800; cursor: pointer; display: flex; align-items: center; gap: 4px; box-shadow: 0 1px 4px rgba(0,0,0,0.5);" title="Navigate East: Middle East (Strait of Hormuz, Persian Gulf, Petroline)">
          <span>East (Hormuz) ▶</span>
        </button>
      </div>'''

if old_nav_span in html:
    html = html.replace(old_nav_span, new_nav_buttons, 1)
    print("Updated navigation buttons in bmap_html_template.html")
else:
    print("Warning: old_nav_span not found in bmap_html_template.html")

# In the crimson header, add direct preset jump pills next to Browse Datasets
browse_btn = '<button id="btn_browse_datasets" onclick="toggleMapContentDrawer()"'
jump_pills = '''<button onclick="bmapNavigateWest()" style="background: #082f49; color: #38bdf8; border: 1px solid #0284c7; padding: 3px 8px; font-size: 10px; font-weight: 800; border-radius: 3px; cursor: pointer;" title="Jump immediately to US FDIC Bank Branches and Interstate Pipelines">
      🇺🇸 North America
    </button>
    <button onclick="bmapNavigateEast()" style="background: #2a1f0a; color: #ffaa00; border: 1px solid #d97706; padding: 3px 8px; font-size: 10px; font-weight: 800; border-radius: 3px; cursor: pointer;" title="Jump immediately to Persian Gulf & Strait of Hormuz">
      🌍 Middle East
    </button>
    '''
if browse_btn in html and "🇺🇸 North America" not in html:
    html = html.replace(browse_btn, jump_pills + browse_btn, 1)
    print("Added preset pills in crimson header in bmap_html_template.html")

# In GEV iframe container: replace src="http://localhost:4173" with src="about:blank"
# And enhance the fallback box
old_iframe_src = '<iframe id="gev_iframe" src="http://localhost:4173"'
new_iframe_src = '<iframe id="gev_iframe" src="about:blank"'
if old_iframe_src in html:
    html = html.replace(old_iframe_src, new_iframe_src, 1)
    print("Updated GEV iframe src to about:blank")

# Replace reload button to call checkGodsEyeServerStatus(true)
old_reload_btn = "document.getElementById('gev_iframe').src = 'http://localhost:4173'"
new_reload_btn = "checkGodsEyeServerStatus(true)"
if old_reload_btn in html:
    html = html.replace(old_reload_btn, new_reload_btn)
    print("Updated GEV reload button")

# Update Pop-out link
old_popout = '<a href="http://localhost:4173" target="_blank"'
new_popout = '<a href="http://127.0.0.1:4173" target="_blank"'
if old_popout in html:
    html = html.replace(old_popout, new_popout)
    print("Updated pop-out link")

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html)
print("Saved bmap_html_template.html")
import re
import os

BASE_DIR = r"F:\documents\SOIC\EconAgent_Platform\platform_ui"
js_path = os.path.join(BASE_DIR, "bmap_js_template.js")
with open(js_path, "r", encoding="utf-8") as f:
    js = f.read()

# 1. Add worldCopyJump: true to L.map
old_map_init = "layers: [baseTileLayers.dark, baseTileLayers.dark_ref],\n      preferCanvas: true"
new_map_init = "layers: [baseTileLayers.dark, baseTileLayers.dark_ref],\n      preferCanvas: true,\n      worldCopyJump: true"
if old_map_init in js:
    js = js.replace(old_map_init, new_map_init, 1)
    print("Added worldCopyJump: true to L.map options")
else:
    print("Warning: old_map_init not found")

# 2. Add checkGodsEyeServerStatus and GEV controller
gev_controller = '''
  // ── GOD'S EYE VIEW 3D SERVER HEARTBEAT & SMART FALLBACK CONTROLLER ──
  var gevHeartbeatTimer = null;
  window.checkGodsEyeServerStatus = function(forceReload) {
    var iframe = document.getElementById('gev_iframe');
    var fallback = document.getElementById('gev_fallback_box');
    var statusPill = document.getElementById('gev_server_status_pill');

    fetch('http://127.0.0.1:4173/?embed=1', { mode: 'no-cors', cache: 'no-store' })
      .then(function() {
        // Vite 3D server is active and reachable!
        if (fallback) fallback.style.display = 'none';
        if (iframe) {
          iframe.style.display = 'block';
          if (!iframe.src || iframe.src === 'about:blank' || forceReload) {
            iframe.src = 'http://127.0.0.1:4173/?embed=1';
          }
        }
        if (statusPill) {
          statusPill.innerHTML = '● VITE 3D SERVER ONLINE (Port 4173)';
          statusPill.style.background = 'rgba(16,185,129,0.15)';
          statusPill.style.border = '1px solid #10b981';
          statusPill.style.color = '#34d399';
        }
      })
      .catch(function(err) {
        // Vite 3D server is offline or not yet started
        if (iframe) {
          iframe.style.display = 'none';
          iframe.src = 'about:blank';
        }
        if (fallback) fallback.style.display = 'block';
        if (statusPill) {
          statusPill.innerHTML = '○ 3D SERVER OFFLINE (Run Launch Batch)';
          statusPill.style.background = 'rgba(239,68,68,0.15)';
          statusPill.style.border = '1px solid #ef4444';
          statusPill.style.color = '#f87171';
        }
      });
  };
'''

# 3. Add West / East Navigation Controllers & Keyboard listeners
nav_controllers = '''
  // ── INTERACTIVE WEST / EAST GEOSPATIAL NAVIGATION CONTROLLERS ──
  window.bmapNavigateWest = function() {
    if (!leafletMap) return;
    // Fly smoothly across Atlantic to North America (geographic center of US)
    leafletMap.flyTo([38.5, -96.5], 4.5, { duration: 1.2 });

    // Enable North American layers: FDIC Bank Branches & Interstate Natural Gas Pipelines
    if (!activeLayers.bank_branches && typeof window.addBmapDataset === 'function') {
      window.addBmapDataset('bank_branches');
    }
    if (!activeLayers.natural_gas && typeof window.addBmapDataset === 'function') {
      window.addBmapDataset('natural_gas');
    }

    // Reset deposit slider if it was filtered down to 0
    var slider = document.getElementById('slider_bank_dep');
    if (slider && parseInt(slider.value) > 2000) {
      slider.value = 0;
      if (typeof window.filterBankBranches === 'function') window.filterBankBranches();
    }

    // Update Bloomberg Scope HUD
    var scEl = document.getElementById('bmap_scope_label');
    if (scEl) scEl.textContent = 'NORTH AMERICA SCOPE · 1,675 FDIC BANK BRANCHES · INTERSTATE PIPELINES · KEYSTONE & DAPL';

    // Highlight button
    var bWest = document.getElementById('btn_bmap_nav_west');
    var bEast = document.getElementById('btn_bmap_nav_east');
    if (bWest) { bWest.style.background = '#0284c7'; bWest.style.color = '#fff'; }
    if (bEast) { bEast.style.background = '#0f1c2e'; bEast.style.color = '#ffaa00'; }
  };

  window.bmapNavigateEast = function() {
    if (!leafletMap) return;
    // Fly smoothly back to Strait of Hormuz / Persian Gulf
    leafletMap.flyTo([26.4, 56.2], 6.5, { duration: 1.2 });

    if (!activeLayers.vessels && typeof window.addBmapDataset === 'function') {
      window.addBmapDataset('vessels');
    }
    if (!activeLayers.crude_pipelines && typeof window.addBmapDataset === 'function') {
      window.addBmapDataset('crude_pipelines');
    }

    var scEl = document.getElementById('bmap_scope_label');
    if (scEl) scEl.textContent = 'MIDDLE EAST CHOKEPOINT · STRAIT OF HORMUZ VLCC RADAR · EAST-WEST PETROLINE';

    var bWest = document.getElementById('btn_bmap_nav_west');
    var bEast = document.getElementById('btn_bmap_nav_east');
    if (bWest) { bWest.style.background = '#0f1c2e'; bWest.style.color = '#38bdf8'; }
    if (bEast) { bEast.style.background = '#d97706'; bEast.style.color = '#fff'; }
  };

  // Aliases for popup buttons & presets
  window.bmapFitUS = window.bmapNavigateWest;
  window.bmapFitBounds = function(type) {
    if (type === 'bank_branches' || type === 'natural_gas' || type === 'us') {
      window.bmapNavigateWest();
    } else if (type === 'vessels' || type === 'crude_pipelines' || type === 'hormuz') {
      window.bmapNavigateEast();
    } else if (typeof window.jumpToBmapPreset === 'function') {
      window.jumpToBmapPreset(type);
    }
  };
'''

# Insert controllers before window.switchBmapView
target_view = "window.switchBmapView = function(viewId) {"
if target_view in js:
    js = js.replace(target_view, gev_controller + "\n" + nav_controllers + "\n  " + target_view, 1)
    print("Injected GEV controller and nav controllers")
else:
    print("Warning: target_view not found")

# Update switchBmapView for heartbeat polling
old_gev_call = "if (viewId === 'gev') {\n      window.checkGodsEyeServerStatus();\n    }"
new_gev_call = """if (viewId === 'gev') {
      window.checkGodsEyeServerStatus();
      if (!gevHeartbeatTimer) {
        gevHeartbeatTimer = setInterval(function() {
          if (currentActiveView === 'gev') {
            window.checkGodsEyeServerStatus(false);
          }
        }, 3000);
      }
    } else {
      if (gevHeartbeatTimer) {
        clearInterval(gevHeartbeatTimer);
        gevHeartbeatTimer = null;
      }
    }"""
if old_gev_call in js:
    js = js.replace(old_gev_call, new_gev_call, 1)
    print("Updated switchBmapView with heartbeat polling")
else:
    print("Warning: old_gev_call not found")

# Add keyboard event listener in initLeafletBmap
old_dom_init = "if (document.readyState === 'loading') {"
keyboard_listener = """
  // Keyboard Shortcuts: ArrowLeft (West / N.Am.) and ArrowRight (East / Hormuz)
  document.addEventListener('keydown', function(e) {
    if (e.target && (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA' || e.target.tagName === 'SELECT')) return;
    if (e.key === 'ArrowLeft' || e.key === 'a' || e.key === 'A') {
      window.bmapNavigateWest();
    } else if (e.key === 'ArrowRight' || e.key === 'd' || e.key === 'D') {
      window.bmapNavigateEast();
    }
  });

"""
if old_dom_init in js and "ArrowLeft" not in js:
    js = js.replace(old_dom_init, keyboard_listener + old_dom_init, 1)
    print("Added keyboard shortcut listeners")

with open(js_path, "w", encoding="utf-8") as f:
    f.write(js)
print("Saved bmap_js_template.js")
