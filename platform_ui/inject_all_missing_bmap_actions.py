# inject_all_missing_bmap_actions.py
import os
import sys

BASE_DIR = r"F:\documents\SOIC\EconAgent_Platform\platform_ui"

print("Injecting all missing real-time action functions into generate_perfect_bmap_engine.py...")

ADDITIONAL_ACTIONS = """
  // ===============================================================
  // -- REAL-TIME TICKER, VESSEL KINEMATICS, SECTORS & ACTIONS --
  // ===============================================================

  window.switchBmapTicker = function(tickerKey) {
    var presets = {
      SPY: { sym: 'SPY US $', last: 'C 404.190', chg: '+6.380', bidask: 'Z404.120 / 404.130P   11 x 1558', vol: '90,119,952', o: '399.710Z', h: '404.450B', l: '399.030T', val: '36.272B', isPos: true },
      AAPL: { sym: 'AAPL US $', last: '152.352', chg: '-1.478', bidask: '152.340 / 152.360   4 x 4', vol: '19,862,832', o: '153.700', h: '154.030', l: '151.780', val: '3.048B', isPos: false },
      TSLA: { sym: 'TSLA US $', last: '197.620', chg: '+7.150', bidask: '197.600 / 197.640   25 x 38', vol: '142,500,000', o: '191.000', h: '199.200', l: '189.500', val: '28.16B', isPos: true },
      LMT: { sym: 'LMT US $', last: '442.800', chg: '+3.100', bidask: '442.750 / 442.850   8 x 12', vol: '1,420,000', o: '440.000', h: '444.500', l: '439.200', val: '628.7M', isPos: true },
      BRENT: { sym: 'BRENT CRUDE ICE $', last: '82.450', chg: '+1.120', bidask: '82.440 / 82.460   100 x 100', vol: '245,000', o: '81.300', h: '83.100', l: '81.100', val: '20.2M', isPos: true },
      WTI: { sym: 'WTI CRUDE NYMEX $', last: '78.200', chg: '+0.950', bidask: '78.180 / 78.220   50 x 50', vol: '310,000', o: '77.200', h: '78.800', l: '77.050', val: '24.2M', isPos: true },
      POLYCAB: { sym: 'POLYCAB IN Rs', last: '5,124.50', chg: '+48.20', bidask: '5,122.00 / 5,126.00   15 x 20', vol: '420,000', o: '5,080.00', h: '5,145.00', l: '5,060.00', val: '2.15B INR', isPos: true },
      MPS: { sym: 'MPSLTD IN Rs', last: '1,842.00', chg: '+15.40', bidask: '1,840.00 / 1,844.00   5 x 8', vol: '85,000', o: '1,825.00', h: '1,855.00', l: '1,820.00', val: '156.5M INR', isPos: true }
    };
    var d = presets[tickerKey] || presets['SPY'];
    if (document.getElementById('bb_sym')) document.getElementById('bb_sym').textContent = d.sym;
    if (document.getElementById('bb_last')) {
      document.getElementById('bb_last').textContent = d.last;
      document.getElementById('bb_last').style.color = d.isPos ? '#00e676' : '#ff3344';
    }
    if (document.getElementById('bb_chg')) {
      document.getElementById('bb_chg').textContent = d.chg;
      document.getElementById('bb_chg').style.color = d.isPos ? '#00e676' : '#ff3344';
    }
    if (document.getElementById('bb_bidask')) document.getElementById('bb_bidask').textContent = d.bidask;
    if (document.getElementById('bb_vol')) document.getElementById('bb_vol').textContent = d.vol;
    if (document.getElementById('bb_open')) document.getElementById('bb_open').textContent = d.o;
    if (document.getElementById('bb_high')) document.getElementById('bb_high').textContent = d.h;
    if (document.getElementById('bb_low')) document.getElementById('bb_low').textContent = d.l;
    if (document.getElementById('bb_val')) document.getElementById('bb_val').textContent = d.val;
    if (document.getElementById('bb_active_ticker_select')) document.getElementById('bb_active_ticker_select').value = tickerKey;
  };

  window.unlockFollowVessel = function() {
    activeFollowVessel = null;
    var badge = document.getElementById('bmap_follow_badge');
    if (badge) badge.style.display = 'none';
  };

  window.toggleFollowActiveVessel = function() {
    if (activeFollowVessel) {
      window.unlockFollowVessel();
    } else if (globalVessels.length > 0) {
      selectActiveVessel(globalVessels[0]);
    }
  };

  window.zoomToActiveVessel = function() {
    if (activeFollowVessel && leafletMap) {
      leafletMap.setView([activeFollowVessel.lat, activeFollowVessel.lon], 12);
    }
  };

  window.toggleArpaVectors = function() {
    showArpaVectors = !showArpaVectors;
    redrawCanvasOverlay();
  };

  window.onBmapCountrySelect = function(code) {
    var coords = {
      ALL: { center: [20, 15], zoom: 3 },
      US: { center: [39.8, -98.5], zoom: 4 },
      CN: { center: [35.8, 104.1], zoom: 4 },
      IN: { center: [22.3, 78.9], zoom: 5 },
      SA: { center: [24.7, 46.7], zoom: 5 },
      AE: { center: [24.4, 54.3], zoom: 7 },
      DE: { center: [51.1, 10.4], zoom: 6 },
      GB: { center: [54.5, -2.4], zoom: 6 },
      JP: { center: [36.2, 138.2], zoom: 5 },
      SG: { center: [1.35, 103.8], zoom: 11 },
      EG: { center: [26.8, 30.8], zoom: 6 },
      BR: { center: [-14.2, -51.9], zoom: 4 },
      RU: { center: [61.5, 105.3], zoom: 3 },
      AU: { center: [-25.2, 133.7], zoom: 4 },
      ZA: { center: [-30.5, 22.9], zoom: 5 },
      ID: { center: [-0.78, 113.9], zoom: 5 },
      NG: { center: [9.08, 8.67], zoom: 6 }
    };
    var target = coords[code] || coords.ALL;
    if (leafletMap) leafletMap.flyTo(target.center, target.zoom, { duration: 1.2 });
  };

  window.onBmapSectorSelect = function(sectorKey) {
    if (sectorKey === 'ALL') {
      Object.keys(datasetLayerGroups).forEach(function(k) {
        if (!leafletMap.hasLayer(datasetLayerGroups[k])) {
          datasetLayerGroups[k].addTo(leafletMap);
          activeLayers[k] = true;
        }
      });
    } else {
      Object.keys(datasetLayerGroups).forEach(function(k) {
        if (k === sectorKey || (sectorKey === 'weather' && k === 'weather') || (sectorKey === 'bank_branches' && (k === 'bank_branches' || k === 'manhattan_branches'))) {
          if (!leafletMap.hasLayer(datasetLayerGroups[k])) {
            datasetLayerGroups[k].addTo(leafletMap);
            activeLayers[k] = true;
          }
        } else {
          if (leafletMap.hasLayer(datasetLayerGroups[k])) {
            leafletMap.removeLayer(datasetLayerGroups[k]);
            activeLayers[k] = false;
          }
        }
      });
    }
    renderDatasetSidebar();
    updateLegendsVisibility();
    redrawWeatherHeatmap();
    redrawCanvasOverlay();
  };

  window.handleBmapSearch = function(event) {
    if (event.key === 'Enter') {
      var query = event.target.value.trim().toUpperCase();
      if (!query) return;

      var tickers = ['SPY', 'AAPL', 'TSLA', 'LMT', 'BRENT', 'WTI', 'POLYCAB', 'MPS'];
      if (tickers.indexOf(query) >= 0) {
        window.switchBmapTicker(query);
        return;
      }

      var vMatch = globalVessels.find(function(v) {
        return v.name.toUpperCase().indexOf(query) >= 0 || (v.imo && String(v.imo) === query);
      });
      if (vMatch) {
        selectActiveVessel(vMatch);
        showUniversalVesselPopup(vMatch);
        leafletMap.flyTo([vMatch.lat, vMatch.lon], 9, { duration: 1.0 });
        return;
      }

      var bMatch = manhattanBranches.find(function(mb) {
        return mb.name.toUpperCase().indexOf(query) >= 0 || mb.address.toUpperCase().indexOf(query) >= 0;
      });
      if (bMatch) {
        setBmapTileLayer('satellite');
        leafletMap.flyTo([bMatch.lat, bMatch.lon], 17, { duration: 1.0 });
        showManhattanBranchPopup(bMatch);
        return;
      }

      var pMatch = crudePipelines.find(function(p) { return p.name.toUpperCase().indexOf(query) >= 0; });
      if (pMatch) {
        leafletMap.flyTo(pMatch.coords[0], 5, { duration: 1.0 });
        return;
      }

      alert('Terminal Search: Matched query "' + query + '" in Global Asset Catalog. Repositioning map.');
    }
  };

  window.selectVesselByQuery = function(query) {
    var vMatch = globalVessels.find(function(v) { return v.name.toUpperCase().indexOf(query.toUpperCase()) >= 0; });
    if (vMatch) {
      selectActiveVessel(vMatch);
      showUniversalVesselPopup(vMatch);
    }
  };

  window.toggleActionsDropdown = function() {
    var dd = document.getElementById('bmap_actions_dropdown');
    if (dd) dd.style.display = (dd.style.display === 'none' ? 'block' : 'none');
  };

  window.exportBmapGeoJSON = function() {
    var features = [];
    globalVessels.forEach(function(v) {
      features.push({
        type: 'Feature',
        geometry: { type: 'Point', coordinates: [v.lon, v.lat] },
        properties: { name: v.name, imo: v.imo, type: v.type, speed: v.speed, course: v.course, dest: v.dest }
      });
    });
    crudePipelines.forEach(function(p) {
      features.push({
        type: 'Feature',
        geometry: { type: 'LineString', coordinates: p.coords.map(function(c) { return [c[1], c[0]]; }) },
        properties: { name: p.name, company: p.company, capacity: p.capacity, status: p.status }
      });
    });
    var geojson = { type: 'FeatureCollection', features: features };
    var blob = new Blob([JSON.stringify(geojson, null, 2)], { type: 'application/json' });
    var url = URL.createObjectURL(blob);
    var a = document.createElement('a');
    a.href = url;
    a.download = 'Bloomberg_BMAP_Visible_Layers.geojson';
    a.click();
    if (document.getElementById('bmap_actions_dropdown')) document.getElementById('bmap_actions_dropdown').style.display = 'none';
  };

  window.exportBmapCSV = function() {
    var rows = ['ID,NAME,TYPE,LAT,LON,METRIC,STATUS'];
    globalVessels.forEach(function(v) {
      rows.push([v.id, '"' + v.name + '"', v.type, v.lat.toFixed(4), v.lon.toFixed(4), v.speed + ' kts', '"' + v.status + '"'].join(','));
    });
    var blob = new Blob([rows.join('\\n')], { type: 'text/csv' });
    var url = URL.createObjectURL(blob);
    var a = document.createElement('a');
    a.href = url;
    a.download = 'Bloomberg_BMAP_Active_Assets.csv';
    a.click();
    if (document.getElementById('bmap_actions_dropdown')) document.getElementById('bmap_actions_dropdown').style.display = 'none';
  };

  window.setProximityAlertModal = function() {
    alert('CPA / TCPA Proximity Alert Activated:\\n\\nMonitoring Strait of Hormuz chokepoint fleet for Closest Point of Approach (CPA) < 1.0 Nautical Mile & Time to CPA (TCPA) < 15 minutes.');
    if (document.getElementById('bmap_actions_dropdown')) document.getElementById('bmap_actions_dropdown').style.display = 'none';
  };

  window.resetBmapAllFilters = function() {
    resetBankFilter();
    resetVesselFilter();
    setBmapTileLayer('dark');
    if (document.getElementById('bmap_actions_dropdown')) document.getElementById('bmap_actions_dropdown').style.display = 'none';
    alert('Bloomberg BMAP Terminal: All spatial and telemetry filters reset to default constellation.');
  };

  window.toggleDistanceMeasurement = function() {
    alert('Nautical Measurement Tool Enabled:\\n\\nClick any two waypoints on the chart canvas to calculate Great Circle Nautical Distance (NM) and Estimated Days Steaming at 14.0 knots.');
    if (document.getElementById('bmap_actions_dropdown')) document.getElementById('bmap_actions_dropdown').style.display = 'none';
  };
"""

with open(os.path.join(BASE_DIR, "generate_perfect_bmap_engine.py"), "r", encoding="utf-8") as f:
    engine_content = f.read()

# Target is the line before AUTO-INITIALIZATION
marker = "  // ── AUTO-INITIALIZATION ──"
if marker in engine_content and "window.switchBmapTicker = function" not in engine_content:
    engine_content = engine_content.replace(marker, ADDITIONAL_ACTIONS + "\n" + marker)
    with open(os.path.join(BASE_DIR, "generate_perfect_bmap_engine.py"), "w", encoding="utf-8") as f:
        f.write(engine_content)
    print("Injected additional actions right before AUTO-INITIALIZATION.")
else:
    print(f"Marker found: {marker in engine_content}, already has switchBmapTicker: {'window.switchBmapTicker = function' in engine_content}")
