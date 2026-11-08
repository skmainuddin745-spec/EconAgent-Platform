import os
import re

BASE_DIR = r"F:\documents\SOIC\EconAgent_Platform\platform_ui"

# 1. Patch bmap_js_template.js
js_path = os.path.join(BASE_DIR, "bmap_js_template.js")
with open(js_path, "r", encoding="utf-8") as f:
    js = f.read()

# Replace hardcoded crude and gas pipelines with injection placeholders
js = re.sub(r'var crudePipelines = \[.*?\];', 'var crudePipelines = __CRUDE_PIPELINES_JSON__;', js, count=1)
js = re.sub(r'var gasPipelines = \[.*?\];', 'var gasPipelines = __GAS_PIPELINES_JSON__;', js, count=1)

# Update dataset labels in SUGGESTED_DATASETS and NEW_DATASETS
js = js.replace("{ key: 'crude_pipelines', label: 'Natural Gas Pipelines', count: '15 Trans', color: '#3b82f6', category: 'COMMODITIES' }",
                "{ key: 'crude_pipelines', label: 'Global Crude Oil Pipelines', count: '15 Transcontinental', color: '#3b82f6', category: 'COMMODITIES' }")
js = js.replace("{ key: 'natural_gas', label: 'Natural Gas', count: '24 Arteries', color: '#00e5ff', category: 'COMMODITIES' }",
                "{ key: 'natural_gas', label: 'Global Natural Gas Pipelines', count: '16 Arteries (Worldwide)', color: '#00e5ff', category: 'COMMODITIES' }")

js = js.replace("{ key: 'municipal_bonds', label: 'Municipal Bonds (US)', count: '18 State & Local Issuers', color: '#f59e0b', category: 'FINANCIAL' }",
                "{ key: 'municipal_bonds', label: 'Global Sovereign, Muni & Sukuk Debt', count: 'US, India SDL, GCC Sukuk, Bunds', color: '#f59e0b', category: 'FINANCIAL' }")
js = js.replace("{ key: 'crop_yields', label: 'Crop Yield Forecasts (US)', count: 'Midwest Corn/Soy/Wheat', color: '#84cc16', category: 'COMMODITIES' }",
                "{ key: 'crop_yields', label: 'Global Crop Yield Forecasts', count: 'US, India, Brazil, Black Sea', color: '#84cc16', category: 'COMMODITIES' }")
js = js.replace("{ key: 'natural_gas_flows', label: 'Natural Gas Flows (N.Am.)', count: 'Real-time Telemetry', color: '#00e5ff', category: 'COMMODITIES' }",
                "{ key: 'natural_gas_flows', label: 'Global Natural Gas & Energy Flows', count: 'Real-time Telemetry (Worldwide)', color: '#00e5ff', category: 'COMMODITIES' }")
js = js.replace("{ key: 'power_iso', label: 'Power ISO Regions', count: '7 Grids (PJM, ERCOT)', color: '#eab308', category: 'INFRASTRUCTURE' }",
                "{ key: 'power_iso', label: 'Global Power Grids & Transmission', count: 'US ISOs, ENTSO-E, India NLDC', color: '#eab308', category: 'INFRASTRUCTURE' }")

# Update Natural Gas Card in Map Content drawer
old_ng_card = '''    // CARD 6: NATURAL GAS (SCREENSHOT 12)
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
          '<div><label style="cursor:pointer;"><input type="checkbox" onchange="toggleSubLayer(\\'lng_terminals\\', this.checked)"' + (activeLayers.lng_terminals ? ' checked' : '') + '> LNG Berths</label></div>' +
          '<div><label style="cursor:pointer;"><input type="checkbox" onchange="toggleSubLayer(\\'lng_terminals\\', this.checked)"' + (activeLayers.lng_terminals ? ' checked' : '') + '> LNG Terminals</label></div>' +
          '<div><label style="cursor:pointer;"><input type="checkbox" onchange="toggleSubLayer(\\'storage_terminals\\', this.checked)"' + (activeLayers.storage_terminals ? ' checked' : '') + '> Storage Terminals</label></div>' +
          '<div><label style="cursor:pointer;"><input type="checkbox" onchange="toggleSubLayer(\\'underground_storage\\', this.checked)"' + (activeLayers.underground_storage ? ' checked' : '') + '> Underground Storage</label></div>' +
          '<div style="color:#00e5ff;font-weight:bold;"><label style="cursor:pointer;"><input type="checkbox" onchange="toggleSubLayer(\\'natural_gas\\', this.checked)"' + (activeLayers.natural_gas ? ' checked' : '') + '> Pipelines (N.Am.)</label></div>' +
          '<div><label style="cursor:pointer;"><input type="checkbox" onchange="toggleSubLayer(\\'refineries\\', this.checked)"' + (activeLayers.refineries ? ' checked' : '') + '> Chemical Processing Plants</label></div>' +
          '<div><label style="cursor:pointer;"><input type="checkbox" onchange="toggleSubLayer(\\'gas_hubs\\', this.checked)"' + (activeLayers.gas_hubs ? ' checked' : '') + '> Hubs</label></div>' +
        '</div>';
      container.appendChild(ngCard);
    }'''

new_ng_card = '''    // CARD 6: NATURAL GAS & GLOBAL PIPELINES
    if (activeLayers.natural_gas) {
      var ngCard = document.createElement('div');
      ngCard.style.cssText = 'background:#080e18;border:1px solid #00e5ff;border-radius:4px;padding:8px 10px;font-size:9.5px;';
      ngCard.innerHTML = 
        '<div style="display:flex;justify-content:space-between;align-items:center;border-bottom:1px solid #162438;padding-bottom:4px;margin-bottom:6px;">' +
          '<div style="display:flex;align-items:center;gap:4px;">' +
            '<span style="color:#ffaa00;">▾</span>' +
            '<strong style="color:#00e5ff;font-size:10.5px;">Natural Gas &amp; Global Energy Pipelines</strong>' +
          '</div>' +
          '<div style="display:flex;align-items:center;gap:6px;">' +
            '<span style="color:#64748b;font-size:9px;cursor:pointer;">≡▾</span>' +
            '<span onclick="window.removeBmapDataset(\\'natural_gas\\')" style="color:#94a3b8;cursor:pointer;font-weight:bold;">✕</span>' +
          '</div>' +
        '</div>' +
        '<div style="display:flex;flex-direction:column;gap:3.5px;color:#cbd5e1;">' +
          '<div><label style="cursor:pointer;"><input type="checkbox" onchange="toggleSubLayer(\\'lng_berths\\', this.checked)"' + (activeLayers.lng_berths ? ' checked' : '') + '> ⚓ LNG Export &amp; Import Berths</label></div>' +
          '<div><label style="cursor:pointer;"><input type="checkbox" onchange="toggleSubLayer(\\'lng_terminals\\', this.checked)"' + (activeLayers.lng_terminals ? ' checked' : '') + '> 🚢 LNG Regasification Terminals (Worldwide)</label></div>' +
          '<div><label style="cursor:pointer;"><input type="checkbox" onchange="toggleSubLayer(\\'storage_terminals\\', this.checked)"' + (activeLayers.storage_terminals ? ' checked' : '') + '> 🛢️ Strategic Crude &amp; Gas Storage</label></div>' +
          '<div><label style="cursor:pointer;"><input type="checkbox" onchange="toggleSubLayer(\\'underground_storage\\', this.checked)"' + (activeLayers.underground_storage ? ' checked' : '') + '> ⛰️ Underground Salt Caverns &amp; Aquifers</label></div>' +
          '<div style="color:#00e5ff;font-weight:bold;"><label style="cursor:pointer;"><input type="checkbox" onchange="toggleSubLayer(\\'natural_gas\\', this.checked)"' + (activeLayers.natural_gas ? ' checked' : '') + '> 🌐 Global Natural Gas Pipelines (GAIL HVJ, TransMed, Dolphin, West-East)</label></div>' +
          '<div><label style="cursor:pointer;"><input type="checkbox" onchange="toggleSubLayer(\\'crude_pipelines\\', this.checked)"' + (activeLayers.crude_pipelines ? ' checked' : '') + '> 🛢️ Global Crude Oil Pipelines (Petroline, Druzhba, BTC, Keystone)</label></div>' +
          '<div><label style="cursor:pointer;"><input type="checkbox" onchange="toggleSubLayer(\\'refineries\\', this.checked)"' + (activeLayers.refineries ? ' checked' : '') + '> 🏭 Petrochemical &amp; Fertilizer Complexes</label></div>' +
          '<div><label style="cursor:pointer;"><input type="checkbox" onchange="toggleSubLayer(\\'gas_hubs\\', this.checked)"' + (activeLayers.gas_hubs ? ' checked' : '') + '> 📍 Major Gas Pricing Hubs (Henry Hub, TTF, JKM, Dahej)</label></div>' +
        '</div>';
      container.appendChild(ngCard);
    }'''

js = js.replace(old_ng_card, new_ng_card)

# Update 3D Workstation Controller to support dual engine modes and auto-detection
old_3d_controller = '''  // ── GOD'S EYE VIEW 3D SERVER HEARTBEAT & SMART FALLBACK CONTROLLER ──
  var gevHeartbeatTimer = null;
  window.checkGodsEyeServerStatus = function(forceReload) {
    var iframe = document.getElementById('gev_iframe');
    var fallback = document.getElementById('gev_fallback_box');
    var statusPill = document.getElementById('gev_server_status_pill');

    return fetch('http://127.0.0.1:4173/?embed=1', { mode: 'no-cors', cache: 'no-store' })
      .then(function() {
        // Vite 3D server is active and reachable!
        if (fallback) fallback.style.display = 'none';
        if (iframe) {
          iframe.style.display = 'block';
          if (iframe.src !== 'http://127.0.0.1:4173/?embed=1') {
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
  };'''

new_3d_controller = '''  // ── DUAL 3D WORKSTATION CONTROLLER (NATIVE CESIUM + BILAWAL SIDHU MICROSERVICE) ──
  var active3DMode = 'native';
  var gevHeartbeatTimer = null;

  window.set3DMode = function(mode) {
    active3DMode = mode;
    var nativeEl = document.getElementById('gev_native_cesium_container');
    var iframeEl = document.getElementById('gev_iframe');
    var fallbackEl = document.getElementById('gev_fallback_box');
    var btnNative = document.getElementById('btn_mode_native_3d');
    var btnServer = document.getElementById('btn_mode_server_3d');
    var hudEngine = document.getElementById('cesium_hud_engine');
    var statusPill = document.getElementById('gev_server_status_pill');

    if (mode === 'native') {
      if (nativeEl) nativeEl.style.display = 'block';
      if (iframeEl) { iframeEl.style.display = 'none'; iframeEl.src = 'about:blank'; }
      if (fallbackEl) fallbackEl.style.display = 'none';
      if (btnNative) { btnNative.style.background = '#0284c7'; btnNative.style.color = '#fff'; btnNative.style.borderColor = '#38bdf8'; }
      if (btnServer) { btnServer.style.background = '#0f172a'; btnServer.style.color = '#94a3b8'; btnServer.style.borderColor = '#1e293b'; }
      if (hudEngine) hudEngine.textContent = 'CesiumJS WebGL (Native Engine)';
      if (statusPill) {
        statusPill.innerHTML = '<span style="color:#00e5ff;">●</span> NATIVE 3D WEBGL ACTIVE (Instant)';
        statusPill.style.background = 'rgba(2,132,199,0.15)';
        statusPill.style.borderColor = '#0284c7';
        statusPill.style.color = '#38bdf8';
      }
      setTimeout(function() {
        if (typeof window.initNativeCesiumViewer === 'function') {
          window.initNativeCesiumViewer();
          if (window.nativeCesiumViewer && window.nativeCesiumViewer.resize) window.nativeCesiumViewer.resize();
        }
      }, 50);
    } else {
      // Server mode (Port 4173)
      if (btnServer) { btnServer.style.background = '#0284c7'; btnServer.style.color = '#fff'; btnServer.style.borderColor = '#38bdf8'; }
      if (btnNative) { btnNative.style.background = '#0f172a'; btnNative.style.color = '#94a3b8'; btnNative.style.borderColor = '#1e293b'; }
      if (hudEngine) hudEngine.textContent = 'Bilawal Sidhu 3D Workstation (Port 4173)';
      window.checkGodsEyeServerStatus(true);
    }
  };

  window.checkGodsEyeServerStatus = function(forceReload) {
    var iframe = document.getElementById('gev_iframe');
    var statusPill = document.getElementById('gev_server_status_pill');
    var fallbackBox = document.getElementById('gev_fallback_box');
    var nativeEl = document.getElementById('gev_native_cesium_container');

    return fetch('http://127.0.0.1:4173/?embed=1', { mode: 'no-cors', cache: 'no-store' })
      .then(function() {
        if (statusPill) {
          statusPill.innerHTML = '<span style="color:#00e676;">●</span> 3D MICROSERVICE LIVE (Port 4173)';
          statusPill.style.background = 'rgba(16,185,129,0.15)';
          statusPill.style.borderColor = '#10b981';
          statusPill.style.color = '#34d399';
        }
        if (active3DMode === 'server') {
          if (fallbackBox) fallbackBox.style.display = 'none';
          if (nativeEl) nativeEl.style.display = 'none';
          if (iframe) {
            iframe.style.display = 'block';
            if (!iframe.src || iframe.src.indexOf('4173') === -1 || forceReload) {
              iframe.src = 'http://127.0.0.1:4173/?embed=1';
            }
          }
        }
        return true;
      })
      .catch(function(err) {
        if (statusPill && active3DMode === 'server') {
          statusPill.innerHTML = '<span style="color:#ef4444;">●</span> 3D SERVER OFFLINE — Run Launch_Gods_Eye_View.bat';
          statusPill.style.background = 'rgba(239,68,68,0.15)';
          statusPill.style.borderColor = '#ef4444';
          statusPill.style.color = '#f87171';
        }
        if (active3DMode === 'server') {
          if (iframe) { iframe.style.display = 'none'; iframe.src = 'about:blank'; }
          if (fallbackBox) fallbackBox.style.display = 'block';
        }
        return false;
      });
  };'''

js = js.replace(old_3d_controller, new_3d_controller)

# Also update the second definition of checkGodsEyeServerStatus around line 3926
second_def = '''  window.checkGodsEyeServerStatus = function(forceReload) {
    var iframe = document.getElementById('gev_iframe');
    var statusPill = document.getElementById('gev_server_status_pill');
    var fallbackBox = document.getElementById('gev_fallback_box');

    return fetch('http://127.0.0.1:4173/?embed=1', { mode: 'no-cors', cache: 'no-store' })
      .then(function() {
        if (statusPill) {
          statusPill.innerHTML = '<span style="color:#00e676;">●</span> VITE 3D SERVER ONLINE (Port 4173)';
          statusPill.style.background = 'rgba(16,185,129,0.15)';
          statusPill.style.borderColor = '#10b981';
          statusPill.style.color = '#34d399';
        }
        if (fallbackBox) fallbackBox.style.display = 'none';
        if (iframe) {
          iframe.style.display = 'block';
          if (!iframe.src || iframe.src.indexOf('4173') === -1 || forceReload) {
            iframe.src = 'http://127.0.0.1:4173/?embed=1';
          }
        }
        return true;
      })
      .catch(function(err) {
        if (statusPill) {
          statusPill.innerHTML = '<span style="color:#ef4444;">●</span> VITE SERVER OFFLINE — Run Launch_Gods_Eye_View.bat';
          statusPill.style.background = 'rgba(239,68,68,0.15)';
          statusPill.style.borderColor = '#ef4444';
          statusPill.style.color = '#f87171';
        }
        if (iframe) {
          iframe.style.display = 'none';
          iframe.src = 'about:blank';
        }
        if (fallbackBox) fallbackBox.style.display = 'block';
        return false;
      });
  };'''

# Replace second definition with a call forwarding to window.set3DMode or check
js = js.replace(second_def, '// checkGodsEyeServerStatus managed by dual 3D controller')

# Expand populateCesium3DEntities to add Global Pipelines & Banking Hubs
old_populate = '''    // 2. Add Keystone & DAPL Pipelines (US)
    var keystone = nativeCesiumViewer.entities.add({
      name: 'Keystone Pipeline System',
      polyline: {
        positions: Cesium.Cartesian3.fromDegreesArray([
          -111.9, 52.8,  // Hardisty, Alberta
          -97.5, 48.9,   // North Dakota border
          -96.0, 41.2,   // Steele City
          -96.7, 35.9,   // Cushing Hub (Oklahoma)
          -93.9, 29.8    // Port Arthur (Gulf Coast)
        ]),
        width: 4,
        material: new Cesium.PolylineGlowMaterialProperty({
          glowPower: 0.3,
          color: Cesium.Color.fromCssColorString('#f97316')
        })
      }
    });
    keystone._econData = {
      kind: 'pipeline',
      name: 'Keystone Pipeline System',
      capacity: '620,000 bpd (WCS Crude)',
      type: 'Transnational Crude Pipeline'
    };'''

new_populate = '''    // 2. Add Keystone System (North America)
    var keystone = nativeCesiumViewer.entities.add({
      name: 'Keystone Pipeline System',
      polyline: {
        positions: Cesium.Cartesian3.fromDegreesArray([
          -111.9, 52.8, -97.5, 48.9, -96.0, 41.2, -96.7, 35.9, -93.9, 29.8
        ]),
        width: 4,
        material: new Cesium.PolylineGlowMaterialProperty({ glowPower: 0.3, color: Cesium.Color.fromCssColorString('#f97316') })
      }
    });

    // 3. Add GAIL HVJ National Gas Backbone (India)
    nativeCesiumViewer.entities.add({
      name: 'GAIL HVJ (Hazira-Vijaipur-Jagdishpur) National Grid',
      polyline: {
        positions: Cesium.Cartesian3.fromDegreesArray([
          72.73, 21.17, 73.18, 22.31, 75.83, 23.58, 77.30, 24.42, 75.83, 25.18, 81.60, 26.47, 77.55, 28.55
        ]),
        width: 5,
        material: new Cesium.PolylineGlowMaterialProperty({ glowPower: 0.35, color: Cesium.Color.fromCssColorString('#00e5ff') })
      }
    });

    // 4. Add Dolphin Gas Pipeline (Qatar -> UAE -> Oman)
    nativeCesiumViewer.entities.add({
      name: 'Dolphin Gas Pipeline (Qatar-UAE-Oman)',
      polyline: {
        positions: Cesium.Cartesian3.fromDegreesArray([
          51.53, 25.92, 52.80, 25.40, 54.72, 24.77, 56.36, 25.29, 55.80, 24.25
        ]),
        width: 4.5,
        material: new Cesium.PolylineGlowMaterialProperty({ glowPower: 0.35, color: Cesium.Color.fromCssColorString('#ffaa00') })
      }
    });

    // 5. Add Trans-Mediterranean Gas Pipeline (Algeria -> Sicily -> Italy)
    nativeCesiumViewer.entities.add({
      name: 'TransMed Gas Pipeline (Algeria-Italy)',
      polyline: {
        positions: Cesium.Cartesian3.fromDegreesArray([
          3.27, 32.93, 8.45, 35.25, 11.05, 37.08, 12.59, 37.65, 15.55, 38.19, 12.50, 41.90, 11.48, 44.62
        ]),
        width: 4.5,
        material: new Cesium.PolylineGlowMaterialProperty({ glowPower: 0.35, color: Cesium.Color.fromCssColorString('#a855f7') })
      }
    });

    // 6. Add Baku-Tbilisi-Ceyhan (BTC) Caspian-Mediterranean Pipeline
    nativeCesiumViewer.entities.add({
      name: 'Baku-Tbilisi-Ceyhan (BTC) Crude Pipeline',
      polyline: {
        positions: Cesium.Cartesian3.fromDegreesArray([
          49.80, 40.30, 44.80, 41.69, 41.27, 39.92, 35.88, 36.88
        ]),
        width: 4.5,
        material: new Cesium.PolylineGlowMaterialProperty({ glowPower: 0.35, color: Cesium.Color.fromCssColorString('#06b6d4') })
      }
    });

    // 7. Add Global Wealth Hubs & Banking Beacons in 3D
    var globalHubBeacons = [
      { name: 'State Bank of India Global HQ (Mumbai Nariman Point)', lon: 72.822, lat: 18.928, assets: '$740B USD' },
      { name: 'HDFC Bank & ICICI Bank Towers (Mumbai BKC)', lon: 72.867, lat: 19.066, assets: '$683B Combined' },
      { name: 'Saudi National Bank & Al Rajhi (Riyadh KAFD Tower)', lon: 46.638, lat: 24.767, assets: '$500B Combined' },
      { name: 'First Abu Dhabi Bank & ADCB (Abu Dhabi Al Maryah)', lon: 54.389, lat: 24.498, assets: '$480B Combined' },
      { name: 'Emirates NBD & Dubai Islamic Bank (DIFC Gate)', lon: 55.279, lat: 25.207, assets: '$310B Assets' },
      { name: 'HSBC Holdings & Barclays (London Canary Wharf)', lon: -0.019, lat: 51.505, assets: '$5.02T Combined' },
      { name: 'UBS Group AG (Zurich Bahnhofstrasse & Geneva)', lon: 8.539, lat: 47.370, assets: '$1.71T Assets · $4.2T AUM' },
      { name: 'Deutsche Bank Twin Towers (Frankfurt Taunusanlage)', lon: 8.670, lat: 50.113, assets: '$1.43T Assets' },
      { name: 'BNP Paribas Global HQ (Paris Boulevard des Italiens)', lon: 2.336, lat: 48.871, assets: '$2.86T Assets' },
      { name: 'DBS Bank Marina Bay Financial Centre (Singapore)', lon: 103.854, lat: 1.280, assets: '$560B Assets' },
      { name: 'MUFG Bank Headquarters (Tokyo Marunouchi)', lon: 139.763, lat: 35.684, assets: '$2.98T Assets' },
      { name: 'ICBC & CCB Headquarters (Beijing Financial Street)', lon: 116.363, lat: 39.914, assets: '$11.7T Combined' },
      { name: 'JPMorgan Chase & Goldman Sachs (New York Wall St / Park Ave)', lon: -73.974, lat: 40.755, assets: '$4.10T Assets' }
    ];

    globalHubBeacons.forEach(function(hub) {
      nativeCesiumViewer.entities.add({
        name: hub.name,
        position: Cesium.Cartesian3.fromDegrees(hub.lon, hub.lat, 250),
        point: {
          pixelSize: 8,
          color: Cesium.Color.fromCssColorString('#a855f7'),
          outlineColor: Cesium.Color.WHITE,
          outlineWidth: 2
        },
        label: {
          text: '🏛️ ' + hub.name.split('(')[0].trim(),
          font: '9px monospace',
          fillColor: Cesium.Color.fromCssColorString('#c084fc'),
          outlineColor: Cesium.Color.BLACK,
          outlineWidth: 2,
          style: Cesium.LabelStyle.FILL_AND_OUTLINE,
          pixelOffset: new Cesium.Cartesian2(0, -14),
          distanceDisplayCondition: new Cesium.DistanceDisplayCondition(0, 15000000)
        }
      });
    });'''

js = js.replace(old_populate, new_populate)

with open(js_path, "w", encoding="utf-8") as f:
    f.write(js)

print("bmap_js_template.js successfully patched!")

