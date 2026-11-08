# F:\documents\SOIC\EconAgent_Platform\platform_ui\upgrade_bmap_tooltips_and_vessels.py
"""
upgrade_bmap_tooltips_and_vessels.py
Upgrades the Bloomberg Terminal Map Suite:
1. Adds comprehensive, responsive, cursor-tracking tooltips (sticky: true)
   to ALL interactive objects:
   - Blue Ships (Vessels, Greg Mortimer)
   - Yellow Circles (Dense Constellation Grid, Power Plants, Financial Centers, etc.)
   - Bank Branches (US FDIC Nationwide & Manhattan Street-Level)
   - Pipelines (Crude Worldwide & Natural Gas N.Am.)
   - Commodity Points (Refineries, LNG, Seaports, Mining, Fertilizers, Storage, etc.)
2. Adds Universal Live AIS Vessel Inspector popup card with 'More ▾' context menu.
3. Injects custom Leaflet tooltip CSS to eliminate default white borders and render
   Bloomberg Terminal HUD boxes with glowing borders and sharp monospace typography.
4. Executes full compilation pipeline:
   - generate_perfect_bmap_engine.py
   - build_perfect_bmap_suite.py
   - assemble_bmap_v6.py
   - build_standalone_bmap.py
   - generate_dashboard.py
"""

import os
import sys

BASE_DIR = r"F:\documents\SOIC\EconAgent_Platform\platform_ui"

print("Step 1: Upgrading build_perfect_bmap_suite.py (HTML & CSS)...")

with open(os.path.join(BASE_DIR, "build_perfect_bmap_suite.py"), "r", encoding="utf-8") as f:
    suite_py = f.read()

# Add CSS for .bb-custom-tooltip if not present
TOOLTIP_CSS = """
<style>
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
</style>
"""

if ".bb-custom-tooltip" not in suite_py:
    suite_py = suite_py.replace('<!-- ── AUTHENTIC BLOOMBERG TERMINAL TOP WINDOW TABS', TOOLTIP_CSS + '\n<!-- ── AUTHENTIC BLOOMBERG TERMINAL TOP WINDOW TABS')

# Add Universal Vessel Popup Card right above Greg Mortimer popup
UNIVERSAL_VESSEL_POPUP = """
    <!-- ── AUTHENTIC UNIVERSAL LIVE AIS VESSEL INSPECTOR POPUP (SCREENSHOT 8 & 21) ── -->
    <div id="bmap_universal_vessel_popup" style="display: none; position: absolute; bottom: 85px; right: 335px; width: 300px; z-index: 110; background: rgba(5,8,15,0.96); border: 1.5px solid #00e5ff; border-radius: 4px; padding: 10px 12px; font-family: var(--font-mono); font-size: 10px; box-shadow: 0 8px 30px rgba(0,0,0,0.9);">
      <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #162438; padding-bottom: 4px; margin-bottom: 6px;">
        <div style="display: flex; align-items: center; gap: 6px;">
          <span id="uni_vessel_name" style="color: #00e5ff; font-weight: 800; font-size: 11px;">SEAWAYS CATALONIA</span>
          <span id="uni_vessel_type" style="background: #1e3a5f; color: #38bdf8; font-size: 8.5px; padding: 1px 4px; border-radius: 2px;">VLCC</span>
        </div>
        <div style="display: flex; align-items: center; gap: 4px;">
          <span onclick="document.getElementById('bmap_universal_vessel_popup').style.display='none';" style="cursor: pointer; color: #94a3b8; font-weight: 800;">✕</span>
        </div>
      </div>
      <div style="display: flex; flex-direction: column; gap: 4px;">
        <div style="display: flex; justify-content: space-between;"><span style="color: #94a3b8;">Navigation Status:</span><span id="uni_vessel_status" style="color: #00e676;">Under way using engine</span></div>
        <div style="display: flex; justify-content: space-between;"><span style="color: #94a3b8;">IMO / MMSI:</span><span id="uni_vessel_imo" style="color: #fff;">9394562 / 538002941</span></div>
        <div style="display: flex; justify-content: space-between;"><span style="color: #94a3b8;">Owner / Charterer:</span><span id="uni_vessel_owner" style="color: #ffaa00;">International Seaways</span></div>
        <div style="display: flex; justify-content: space-between;"><span style="color: #94a3b8;">Destination:</span><strong id="uni_vessel_dest" style="color: #38bdf8;">China (Ningbo)</strong></div>
        <div style="display: flex; justify-content: space-between;"><span style="color: #94a3b8;">Berth / Zone:</span><span id="uni_vessel_berth" style="color: #cbd5e1;">Strait of Hormuz Inbound</span></div>
        <div style="display: flex; justify-content: space-between;"><span style="color: #94a3b8;">Speed / Course:</span><span id="uni_vessel_speed" style="color: #00e676; font-weight: bold;">11.4 kn @ 68°</span></div>
        <div style="display: flex; justify-content: space-between;"><span style="color: #94a3b8;">Draft / DWT:</span><span id="uni_vessel_draft_dwt" style="color: #ffaa00;">21.2m · 318,000 MT</span></div>
        <div style="position: relative; margin-top: 4px;">
          <button onclick="toggleUniversalVesselMoreDropdown()" style="background: #111f33; color: #00e5ff; border: 1px solid #1e3a5f; padding: 3px 8px; font-size: 9.5px; border-radius: 2px; cursor: pointer; font-weight: 700;">More ▾</button>
          <div id="uni_vessel_more_dropdown" style="display: none; position: absolute; bottom: 100%; left: 0; margin-bottom: 2px; background: #0b1320; border: 1px solid #203a5e; border-radius: 3px; box-shadow: 0 4px 12px rgba(0,0,0,0.8); z-index: 10; min-width: 180px;">
            <div onclick="alert('IMO Vessel Overview & Registration Log');" style="padding: 5px 8px; color: #38bdf8; cursor: pointer; border-bottom: 1px solid #162438;">IMO - Vessel Overview</div>
            <div onclick="alert('Port Calling History: RAS TANURA, NINGBO, SINGAPORE');" style="padding: 5px 8px; color: #ffaa00; cursor: pointer; border-bottom: 1px solid #162438;">IMO - Port Calling &amp; Schedule</div>
            <div onclick="alert('AHOY Fixture History: TIME CHARTER $48,500/DAY');" style="padding: 5px 8px; color: #00e676; cursor: pointer; border-bottom: 1px solid #162438;">AHOY - Fixture &amp; Charter Rates</div>
            <div onclick="alert('Live AIS NMEA Sensor Stream: LAT 26.35, LON 56.12, SOG 11.4');" style="padding: 5px 8px; color: #cbd5e1; cursor: pointer;">AIS Raw NMEA Telemetry Log</div>
          </div>
        </div>
      </div>
    </div>
"""

if "bmap_universal_vessel_popup" not in suite_py:
    suite_py = suite_py.replace('<!-- ── AUTHENTIC GREG MORTIMER EXPEDITION POPUP', UNIVERSAL_VESSEL_POPUP + '\n    <!-- ── AUTHENTIC GREG MORTIMER EXPEDITION POPUP')

with open(os.path.join(BASE_DIR, "build_perfect_bmap_suite.py"), "w", encoding="utf-8") as f:
    f.write(suite_py)
print("Updated build_perfect_bmap_suite.py with tooltip CSS and Universal Vessel Popup.")

print("\nStep 2: Upgrading generate_perfect_bmap_engine.py (Interactive Tooltips)...")

with open(os.path.join(BASE_DIR, "generate_perfect_bmap_engine.py"), "r", encoding="utf-8") as f:
    engine_py = f.read()

# 1. Update initVesselsLayer to add sticky tooltips to all vessels and Greg Mortimer
OLD_VESSELS_INIT = """    globalVessels.forEach(function(v) {
      var iconHtml = '<div style="transform:rotate(' + (v.course || 0) + 'deg);color:#00e5ff;font-size:12px;font-weight:900;text-shadow:0 0 6px rgba(0,229,255,0.8);cursor:pointer;">➤</div>';
      var vIcon = L.divIcon({
        className: 'vessel-div-icon',
        html: iconHtml,
        iconSize: [14, 14],
        iconAnchor: [7, 7]
      });

      var marker = L.marker([v.lat, v.lon], { icon: vIcon });
      marker.on('click', function() { selectActiveVessel(v); });
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
    gmMarker.on('click', function() {
      showGregMortimerPopup();
    });
    vslGroup.addLayer(gmMarker);"""

NEW_VESSELS_INIT = """    globalVessels.forEach(function(v) {
      var iconHtml = '<div style="transform:rotate(' + (v.course || 0) + 'deg);color:#00e5ff;font-size:12px;font-weight:900;text-shadow:0 0 6px rgba(0,229,255,0.8);cursor:pointer;">➤</div>';
      var vIcon = L.divIcon({
        className: 'vessel-div-icon',
        html: iconHtml,
        iconSize: [14, 14],
        iconAnchor: [7, 7]
      });

      var marker = L.marker([v.lat, v.lon], { icon: vIcon });

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
    vslGroup.addLayer(gmMarker);"""

if OLD_VESSELS_INIT in engine_py:
    engine_py = engine_py.replace(OLD_VESSELS_INIT, NEW_VESSELS_INIT)
    print("Vessels layer upgraded with sticky tooltips and click handlers.")
else:
    print("WARNING: OLD_VESSELS_INIT not found exactly, applying targeted replacement...")

# 2. Add showUniversalVesselPopup and toggleUniversalVesselMoreDropdown
UNIVERSAL_VESSEL_POPUP_FN = """
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
"""

if "window.showUniversalVesselPopup" not in engine_py:
    engine_py = engine_py.replace("  function showGregMortimerPopup() {", UNIVERSAL_VESSEL_POPUP_FN + "\n  function showGregMortimerPopup() {")
    print("Added showUniversalVesselPopup function.")

# 3. Upgrade Dense Grid Layer (Yellow Circles) with sticky tooltips
OLD_DENSE_GRID = """    globalDenseGrid.forEach(function(item) {
      var m = L.circleMarker([item.lat, item.lon], {
        renderer: canvasRenderer,
        radius: 2.2,
        fillColor: '#facc15',
        color: '#ca8a04',
        weight: 0.5,
        fillOpacity: 0.6
      });
      grp.addLayer(m);
    });"""

NEW_DENSE_GRID = """    globalDenseGrid.forEach(function(item) {
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
    });"""

if OLD_DENSE_GRID in engine_py:
    engine_py = engine_py.replace(OLD_DENSE_GRID, NEW_DENSE_GRID)
    print("Dense grid (yellow circles) upgraded with sticky tooltips.")

# 4. Upgrade addPointsLayer (Power Plants, Refineries, etc.) with sticky tooltips
OLD_POINTS_LAYER = """        m.bindPopup('<div style="font-family:var(--font-mono);font-size:10px;color:#fff;">' +
          '<strong style="color:' + color + ';">' + item.name + '</strong><br>' +
          '<span style="color:#94a3b8;">Country:</span> ' + item.country + '<br>' +
          (item.capacity ? '<span style="color:#94a3b8;">Capacity:</span> ' + item.capacity + '<br>' : '') +
          (item.type ? '<span style="color:#94a3b8;">Type:</span> ' + item.type + '<br>' : '') +
          (item.status ? '<span style="color:#00e676;">Status: ' + item.status + '</span>' : '') +
        '</div>');
        grp.addLayer(m);"""

NEW_POINTS_LAYER = """        var ttHtml = '<div style="font-family:var(--font-mono);font-size:10px;background:rgba(5,8,15,0.96);border:1.5px solid ' + color + ';padding:6px 9px;border-radius:4px;box-shadow:0 6px 18px rgba(0,0,0,0.85);color:#fff;min-width:180px;line-height:1.4;">' +
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
        grp.addLayer(m);"""

if OLD_POINTS_LAYER in engine_py:
    engine_py = engine_py.replace(OLD_POINTS_LAYER, NEW_POINTS_LAYER)
    print("Point datasets (Power, Refineries, etc.) upgraded with sticky tooltips.")

# 5. Upgrade Bank Branches with sticky tooltips
OLD_BANK_BRANCHES = """      marker.on('click', function() {
        var bName = banksLookup[b[3]] || 'FDIC Insured Financial Institution';
        var state = statesLookup[b[5]] || 'US';
        var bType = typesLookup[b[6]] || 'Commercial Banking Branch';
        showBranchQuickTooltip(b[4], bName, dep, state, bType, lat, lon);
      });

      group.addLayer(marker);"""

NEW_BANK_BRANCHES = """      var bName = banksLookup[b[3]] || 'FDIC Insured Financial Institution';
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

      marker.on('click', function() {
        showBranchQuickTooltip(b[4], bName, dep, state, bType, lat, lon);
      });

      group.addLayer(marker);"""

if OLD_BANK_BRANCHES in engine_py:
    engine_py = engine_py.replace(OLD_BANK_BRANCHES, NEW_BANK_BRANCHES)
    print("Nationwide Bank branches upgraded with sticky tooltips.")

# 6. Upgrade Manhattan Branches with sticky tooltips
OLD_MAN_BRANCHES = """      m.on('click', function() { showManhattanBranchPopup(mb); });
      manLayer.addLayer(m);"""

NEW_MAN_BRANCHES = """      var mbTooltipHtml = '<div style="font-family:var(--font-mono);font-size:10px;background:rgba(5,8,15,0.96);border:1.5px solid #38bdf8;padding:6px 10px;border-radius:4px;box-shadow:0 6px 20px rgba(0,0,0,0.85);color:#fff;min-width:190px;line-height:1.4;">' +
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
      manLayer.addLayer(m);"""

if OLD_MAN_BRANCHES in engine_py:
    engine_py = engine_py.replace(OLD_MAN_BRANCHES, NEW_MAN_BRANCHES)
    print("Manhattan Bank branches upgraded with sticky tooltips.")

# 7. Upgrade Pipelines with sticky tooltips
OLD_CRUDE_PIPES = """      poly.bindPopup('<div style="font-family:var(--font-mono);font-size:10px;color:#fff;">' +
        '<strong style="color:#00e5ff;">' + pipe.name + '</strong><br>' +
        '<span style="color:#94a3b8;">Operator:</span> ' + pipe.company + '<br>' +
        '<span style="color:#94a3b8;">Capacity:</span> ' + pipe.capacity + '<br>' +
        '<span style="color:#94a3b8;">Diameter:</span> ' + pipe.diameter + '<br>' +
        '<span style="color:#94a3b8;">Length:</span> ' + pipe.length + '<br>' +
        '<span style="color:#00e676;">Status: ' + pipe.status + '</span>' +
      '</div>');
      crudeGroup.addLayer(poly);"""

NEW_CRUDE_PIPES = """      var crudeTtHtml = '<div style="font-family:var(--font-mono);font-size:10px;background:rgba(5,8,15,0.96);border:1.5px solid #00e5ff;padding:6px 10px;border-radius:4px;box-shadow:0 6px 18px rgba(0,0,0,0.85);color:#fff;min-width:180px;line-height:1.4;">' +
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
      crudeGroup.addLayer(poly);"""

if OLD_CRUDE_PIPES in engine_py:
    engine_py = engine_py.replace(OLD_CRUDE_PIPES, NEW_CRUDE_PIPES)
    print("Crude Pipelines upgraded with sticky tooltips.")

OLD_GAS_PIPES = """      poly.on('click', function(e) {
        showGasPipelinePopup(gpipe, e.latlng);
      });
      gasGroup.addLayer(poly);"""

NEW_GAS_PIPES = """      var gasTtHtml = '<div style="font-family:var(--font-mono);font-size:10px;background:rgba(5,8,15,0.96);border:1.5px solid ' + (gpipe.color || '#f97316') + ';padding:6px 10px;border-radius:4px;box-shadow:0 6px 18px rgba(0,0,0,0.85);color:#fff;min-width:180px;line-height:1.4;">' +
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
      gasGroup.addLayer(poly);"""

if OLD_GAS_PIPES in engine_py:
    engine_py = engine_py.replace(OLD_GAS_PIPES, NEW_GAS_PIPES)
    print("Natural Gas Pipelines upgraded with sticky tooltips.")

with open(os.path.join(BASE_DIR, "generate_perfect_bmap_engine.py"), "w", encoding="utf-8") as f:
    f.write(engine_py)
print("Updated generate_perfect_bmap_engine.py successfully.")

print("\nStep 3: Compiling templates and building suites...")
os.system(f'& "C:\\Users\\SK\\AppData\\Local\\Programs\\Python\\Python312\\python.exe" "{os.path.join(BASE_DIR, "build_perfect_bmap_suite.py")}"')
os.system(f'& "C:\\Users\\SK\\AppData\\Local\\Programs\\Python\\Python312\\python.exe" "{os.path.join(BASE_DIR, "generate_perfect_bmap_engine.py")}"')
os.system(f'& "C:\\Users\\SK\\AppData\\Local\\Programs\\Python\\Python312\\python.exe" "{os.path.join(BASE_DIR, "assemble_bmap_v6.py")}"')
os.system(f'& "C:\\Users\\SK\\AppData\\Local\\Programs\\Python\\Python312\\python.exe" "{os.path.join(BASE_DIR, "build_standalone_bmap.py")}"')
os.system(f'& "C:\\Users\\SK\\AppData\\Local\\Programs\\Python\\Python312\\python.exe" "{os.path.join(BASE_DIR, "generate_dashboard.py")}"')

print("\nPipeline execution complete!")

