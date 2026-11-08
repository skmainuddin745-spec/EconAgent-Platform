import re
import os

BASE_DIR = r"F:\documents\SOIC\EconAgent_Platform\platform_ui"

# 1. UPDATE bmap_html_template.html
html_path = os.path.join(BASE_DIR, "bmap_html_template.html")
with open(html_path, "r", encoding="utf-8") as f:
    html = f.read()

# Add Cesium CDN link and script if not present
cesium_cdn = """<!-- Cesium 3D Photorealistic Engine (Zero-Server Native Embedded) -->
<link rel="stylesheet" href="https://cesium.com/downloads/cesiumjs/releases/1.114/Build/Cesium/Widgets/widgets.css">
<script src="https://cesium.com/downloads/cesiumjs/releases/1.114/Build/Cesium/Cesium.js"></script>
"""
if "cesiumjs/releases" not in html:
    html = cesium_cdn + html
    print("Added Cesium CDN script and styles to bmap_html_template.html")

# Replace GEV container with Native Embedded 3D Cesium Container
gev_start = html.find('id="bmap_view_container_gev"')
gev_container_start = html.rfind('<div', 0, gev_start)
gev_container_end = html.find('<!-- ── TABLE VIEW: BERTH VISITS', gev_start)
if gev_container_end == -1:
    gev_container_end = html.find('id="bmap_view_container_table"', gev_start)
    gev_container_end = html.rfind('</div>', 0, gev_container_end) + 6

print(f"Replacing GEV container from pos {gev_container_start} to {gev_container_end}...")

new_gev_html = """<div id="bmap_view_container_gev" style="display: none; background: #00040a; border: 1px solid #1e2e44; border-top: none; font-family: var(--font-mono);">
  <!-- Top 3D Control Header with Direct Camera Presets & Status -->
  <div style="height: 44px; background: rgba(5,8,15,0.98); border-bottom: 1.5px solid #00e5ff; display: flex; justify-content: space-between; align-items: center; padding: 0 14px; box-shadow: 0 4px 18px rgba(0,0,0,0.9); flex-wrap: wrap; gap: 8px;">
    <div style="display: flex; align-items: center; gap: 10px;">
      <button onclick="switchBmapView('map')" style="background: #1e293b; color: #fff; border: 1px solid #475569; padding: 4px 12px; font-size: 10.5px; font-weight: 800; border-radius: 3px; cursor: pointer; display: flex; align-items: center; gap: 4px;">
        ← Return to 2D BMAP
      </button>
      <span style="color: #00e5ff; font-weight: 900; font-size: 12px; letter-spacing: 0.5px;">🌍 GOD'S EYE VIEW 3D WORKSTATION</span>
      <div id="gev_server_status_pill" style="background: rgba(16,185,129,0.15); border: 1px solid #10b981; color: #34d399; font-size: 10px; padding: 3px 10px; border-radius: 3px; font-weight: 800; display: flex; align-items: center; gap: 4px;">
        <span style="color:#00e676;">●</span> NATIVE CESIUM 3D ONLINE (Hardware Accelerated)
      </div>
    </div>

    <!-- Quick Camera Presets (All Bilawal Sidhu & EconAgent Scenarios) -->
    <div style="display: flex; align-items: center; gap: 5px;">
      <button onclick="flyCesiumTo('manhattan')" class="action-btn" style="background: #0c4a6e; color: #38bdf8; border: 1px solid #0284c7; padding: 3px 8px; font-size: 9.5px; font-weight: 800; border-radius: 3px; cursor: pointer;">🏢 Manhattan 400 Bway</button>
      <button onclick="flyCesiumTo('greg_mortimer')" class="action-btn" style="background: #4c1d95; color: #e9d5ff; border: 1px solid #a855f7; padding: 3px 8px; font-size: 9.5px; font-weight: 800; border-radius: 3px; cursor: pointer;">🚢 Greg Mortimer</button>
      <button onclick="flyCesiumTo('dense_grid')" class="action-btn" style="background: #2e1065; color: #facc15; border: 1px solid #eab308; padding: 3px 8px; font-size: 9.5px; font-weight: 800; border-radius: 3px; cursor: pointer;">✨ Constellation</button>
      <button onclick="flyCesiumTo('world')" class="action-btn" style="background: #16253b; color: #fff; border: 1px solid #2a4365; padding: 3px 8px; font-size: 9.5px; border-radius: 3px; cursor: pointer;">🌍 Global View</button>
      <button onclick="flyCesiumTo('west')" class="action-btn" style="background: #064e3b; color: #34d399; border: 1px solid #059669; padding: 3px 8px; font-size: 9.5px; font-weight: 800; border-radius: 3px; cursor: pointer;">◀ N. America</button>
      <button onclick="flyCesiumTo('east')" class="action-btn" style="background: #78350f; color: #fcd34d; border: 1px solid #d97706; padding: 3px 8px; font-size: 9.5px; font-weight: 800; border-radius: 3px; cursor: pointer;">East (Hormuz) ▶</button>
    </div>

    <!-- Right Controls -->
    <div style="display: flex; align-items: center; gap: 8px;">
      <button onclick="flyCesiumTo('east')" style="background: #0f172a; color: #38bdf8; border: 1px solid #1e3a5f; padding: 4px 10px; font-size: 9.5px; border-radius: 3px; cursor: pointer;">
        🔄 Reset 3D View
      </button>
      <a href="Launch_Gods_Eye_View.bat" style="background: #0284c7; color: #fff; text-decoration: none; border: 1px solid #38bdf8; padding: 4px 12px; font-size: 9.5px; font-weight: 800; border-radius: 3px; display: inline-flex; align-items: center; gap: 4px;" title="Launch independent standalone microservice on port 4173">
        ↗ Standalone Launcher
      </a>
    </div>
  </div>

  <!-- Native 3D WebGL Cesium Workstation Container -->
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
  </div>
</div>"""

html = html[:gev_container_start] + new_gev_html + html[gev_container_end:]
with open(html_path, "w", encoding="utf-8") as f:
    f.write(html)
print("Updated bmap_html_template.html successfully!")

# 2. UPDATE bmap_js_template.js
js_path = os.path.join(BASE_DIR, "bmap_js_template.js")
with open(js_path, "r", encoding="utf-8") as f:
    js = f.read()

native_cesium_code = '''
  // ═══════════════════════════════════════════════════════════════
  // ── NATIVE EMBEDDED CESIUM 3D GLOBE ENGINE (ZERO SERVER NEEDED) ──
  // ═══════════════════════════════════════════════════════════════
  var nativeCesiumViewer = null;
  var cesiumEntitiesInitialized = false;

  window.initNativeCesiumViewer = function() {
    var container = document.getElementById('gev_native_cesium_container');
    if (!container) return;
    if (nativeCesiumViewer) {
      nativeCesiumViewer.resize();
      return;
    }
    if (typeof Cesium === 'undefined') {
      console.warn('Cesium library still loading...');
      setTimeout(window.initNativeCesiumViewer, 300);
      return;
    }

    try {
      nativeCesiumViewer = new Cesium.Viewer('gev_native_cesium_container', {
        baseLayerPicker: false,
        geocoder: false,
        homeButton: false,
        infoBox: false,
        sceneModePicker: false,
        selectionIndicator: false,
        timeline: false,
        animation: false,
        navigationHelpButton: false,
        baseLayer: new Cesium.ImageryLayer(new Cesium.OpenStreetMapImageryProvider({
          url: 'https://tile.openstreetmap.org/'
        }))
      });

      window.nativeCesiumViewer = nativeCesiumViewer;

      // Dark background and atmospheric lighting
      nativeCesiumViewer.scene.globe.baseColor = Cesium.Color.BLACK;
      nativeCesiumViewer.scene.globe.enableLighting = true;
      nativeCesiumViewer.scene.backgroundColor = Cesium.Color.fromCssColorString('#020611');

      // Populate 3D Entities
      populateCesium3DEntities();

      // Setup click handler to trigger Bloomberg Terminal Inspector
      var handler = new Cesium.ScreenSpaceEventHandler(nativeCesiumViewer.scene.canvas);
      handler.setInputAction(function(click) {
        var picked = nativeCesiumViewer.scene.pick(click.position);
        if (Cesium.defined(picked) && picked.id && picked.id._econData) {
          var data = picked.id._econData;
          if (data.kind === 'vessel' && typeof selectActiveVessel === 'function') {
            selectActiveVessel(data);
          } else if (data.kind === 'pipeline' && typeof showPipelineDetails === 'function') {
            showPipelineDetails(data);
          }
        }
      }, Cesium.ScreenSpaceEventType.LEFT_CLICK);

      // Default camera view: Middle East / Strait of Hormuz
      window.flyCesiumTo('east');

    } catch(e) {
      console.error('Error initializing Native Cesium Viewer:', e);
    }
  };

  function populateCesium3DEntities() {
    if (!nativeCesiumViewer || cesiumEntitiesInitialized) return;
    cesiumEntitiesInitialized = true;

    // 1. Add East-West Petroline (Saudi Arabia)
    var petroline = nativeCesiumViewer.entities.add({
      name: 'East-West Petroline (Saudi Arabia)',
      polyline: {
        positions: Cesium.Cartesian3.fromDegreesArray([
          50.15, 26.27, // Abqaiq
          46.72, 24.69, // Riyadh
          42.00, 24.20,
          38.06, 24.09  // Yanbu Port (Red Sea)
        ]),
        width: 5,
        material: new Cesium.PolylineGlowMaterialProperty({
          glowPower: 0.35,
          color: Cesium.Color.fromCssColorString('#00e5ff')
        })
      }
    });
    petroline._econData = {
      kind: 'pipeline',
      name: 'East-West Petroline (Saudi Arabia)',
      capacity: '5,000,000 bpd (Expanded to 7.0 Mbd)',
      type: 'Crude Oil Transmission Pipeline'
    };

    // 2. Add Keystone & DAPL Pipelines (US)
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
    };

    // 3. Add 60 AIS Tankers in 3D
    if (typeof globalVessels !== 'undefined' && globalVessels && globalVessels.length) {
      globalVessels.forEach(function(v) {
        var isCatalonia = (v.name === 'SEAWAYS CATALONIA');
        var isJubail = (v.name === 'JUBAIL TRADER');
        var color = isCatalonia ? '#00e5ff' : isJubail ? '#00e676' : '#ffaa00';
        
        var vesselEntity = nativeCesiumViewer.entities.add({
          name: v.name,
          position: Cesium.Cartesian3.fromDegrees(v.lon, v.lat, 0),
          point: {
            pixelSize: (isCatalonia || isJubail) ? 9 : 6,
            color: Cesium.Color.fromCssColorString(color),
            outlineColor: Cesium.Color.BLACK,
            outlineWidth: 2
          },
          label: {
            text: (isCatalonia || isJubail) ? '🚢 ' + v.name + ' (' + v.speed + ')' : '',
            font: '10px monospace',
            fillColor: Cesium.Color.WHITE,
            outlineColor: Cesium.Color.BLACK,
            outlineWidth: 2,
            style: Cesium.LabelStyle.FILL_AND_OUTLINE,
            verticalOrigin: Cesium.VerticalOrigin.BOTTOM,
            pixelOffset: new Cesium.Cartesian2(0, -8),
            distanceDisplayCondition: new Cesium.DistanceDisplayCondition(0, 4000000)
          }
        });
        vesselEntity._econData = Object.assign({ kind: 'vessel' }, v);
      });
    }

    // 4. Add Top US FDIC Bank Branches (NYC, Chicago, SF, Charlotte, Dallas)
    var topBankHubs = [
      { name: 'JPMorgan Chase Tower (NYC)', lat: 40.7556, lon: -73.9754, dep: '$1.4T' },
      { name: 'Bank of America Corporate Center (Charlotte)', lat: 35.2271, lon: -80.8431, dep: '$920B' },
      { name: 'Wells Fargo Stagecoach (SF)', lat: 37.7937, lon: -122.4014, dep: '$780B' },
      { name: 'Citigroup Center (Chicago)', lat: 41.8826, lon: -87.6403, dep: '$550B' },
      { name: '400 Broadway FDIC Branch (NYC)', lat: 40.7182, lon: -74.0028, dep: '$148M' }
    ];
    topBankHubs.forEach(function(b) {
      nativeCesiumViewer.entities.add({
        name: b.name,
        position: Cesium.Cartesian3.fromDegrees(b.lon, b.lat, 0),
        point: {
          pixelSize: 8,
          color: Cesium.Color.fromCssColorString('#ffd700'),
          outlineColor: Cesium.Color.BLACK,
          outlineWidth: 2
        },
        label: {
          text: '🏛️ ' + b.name,
          font: '10px monospace',
          fillColor: Cesium.Color.fromCssColorString('#fef08a'),
          outlineColor: Cesium.Color.BLACK,
          outlineWidth: 2,
          style: Cesium.LabelStyle.FILL_AND_OUTLINE,
          verticalOrigin: Cesium.VerticalOrigin.BOTTOM,
          pixelOffset: new Cesium.Cartesian2(0, -8),
          distanceDisplayCondition: new Cesium.DistanceDisplayCondition(0, 3000000)
        }
      });
    });
  }

  // ── 3D CAMERA JUMP CONTROLLER ──
  window.flyCesiumTo = function(presetKey) {
    if (!nativeCesiumViewer) {
      window.initNativeCesiumViewer();
    }
    if (!nativeCesiumViewer) return;

    var hudCoords = document.getElementById('cesium_hud_coords');

    if (presetKey === 'manhattan') {
      nativeCesiumViewer.camera.flyTo({
        destination: Cesium.Cartesian3.fromDegrees(-74.0028, 40.7182, 1200),
        orientation: { pitch: Cesium.Math.toRadians(-35) },
        duration: 1.2
      });
      if (hudCoords) hudCoords.innerHTML = '<span style="color:#38bdf8;font-weight:700;">MANHATTAN 400 BWAY · 40.718°N, 74.003°W (1,200m)</span>';
    } else if (presetKey === 'greg_mortimer') {
      nativeCesiumViewer.camera.flyTo({
        destination: Cesium.Cartesian3.fromDegrees(-64.8, -64.5, 45000),
        duration: 1.5
      });
      if (hudCoords) hudCoords.innerHTML = '<span style="color:#e9d5ff;font-weight:700;">GREG MORTIMER EXPEDITION · 64.5°S, 64.8°W</span>';
    } else if (presetKey === 'dense_grid') {
      nativeCesiumViewer.camera.flyTo({
        destination: Cesium.Cartesian3.fromDegrees(50.0, 25.0, 15000000),
        duration: 1.5
      });
      if (hudCoords) hudCoords.innerHTML = '<span style="color:#facc15;font-weight:700;">ORBITAL SATELLITE CONSTELLATION · 15,000km Orbit</span>';
    } else if (presetKey === 'world') {
      nativeCesiumViewer.camera.flyTo({
        destination: Cesium.Cartesian3.fromDegrees(15.0, 20.0, 22000000),
        duration: 1.5
      });
      if (hudCoords) hudCoords.innerHTML = '<span style="color:#fff;font-weight:700;">GLOBAL EARTH OVERVIEW · 22,000km Orbit</span>';
    } else if (presetKey === 'west') {
      nativeCesiumViewer.camera.flyTo({
        destination: Cesium.Cartesian3.fromDegrees(-96.5, 38.5, 4500000),
        duration: 1.2
      });
      if (hudCoords) hudCoords.innerHTML = '<span style="color:#34d399;font-weight:700;">NORTH AMERICA SCOPE · 1,675 FDIC HUBS &amp; GAS PIPELINES</span>';
    } else if (presetKey === 'east') {
      nativeCesiumViewer.camera.flyTo({
        destination: Cesium.Cartesian3.fromDegrees(55.0, 26.0, 650000),
        duration: 1.2
      });
      if (hudCoords) hudCoords.innerHTML = '<span style="color:#ffaa00;font-weight:700;">STRAIT OF HORMUZ VLCC RADAR &amp; PETROLINE · 26.4°N, 56.2°E</span>';
    }
  };
'''

# Replace old checkGodsEyeServerStatus references and hook into switchBmapView
target_view_call = "if (viewId === 'gev') {"
gev_view_hook = """if (viewId === 'gev') {
      setTimeout(function() {
        if (typeof window.initNativeCesiumViewer === 'function') {
          window.initNativeCesiumViewer();
        }
      }, 50);
    } else """

if target_view_call in js:
    # Find the end of if (viewId === 'gev') { ... } else if (viewId === 'map'
    pos = js.find(target_view_call)
    pos_map = js.find("} else if (viewId === 'map'", pos)
    if pos_map != -1:
        js = js[:pos] + gev_view_hook + js[pos_map+7:]
        print("Hooked native Cesium viewer into switchBmapView")

# Inject the native Cesium code
js = native_cesium_code + "\n" + js

with open(js_path, "w", encoding="utf-8") as f:
    f.write(js)
print("Updated bmap_js_template.js successfully!")
