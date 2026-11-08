with open(r'F:\documents\SOIC\EconAgent_Platform\platform_ui\bmap_js_template.js', 'r', encoding='utf-8') as f:
    js = f.read()

pos_start = js.find('function renderBankBranchesOnMap(branches) {')
pos_end = js.find('  // Helper to display details for generic infrastructure', pos_start)

replacement_branches_render = """function renderBankBranchesOnMap(branches) {
    var group = datasetLayerGroups['bank_branches'];
    if (!group) return;
    group.clearLayers();

    var canvasRenderer = L.canvas({ padding: 0.5 });
    branches.forEach(function(b) {
      // Decode compact branch: [id, bank_idx, lat, lon, dep_M, state_idx, type_idx]
      var bId = b[0];
      var bankIdx = b[1];
      var lat = b[2];
      var lon = b[3];
      var depM = b[4];
      var stateIdx = b[5];
      var typeIdx = b[6];

      var radius = Math.min(18, Math.max(4, Math.log10(depM + 1) * 3.6));

      var marker = L.circleMarker([lat, lon], {
        renderer: canvasRenderer,
        radius: radius,
        fillColor: '#a855f7',
        color: '#ffffff',
        weight: 1.2,
        opacity: 0.85,
        fillOpacity: 0.6
      });

      var bName = banksLookup[bankIdx] || 'FDIC Insured Financial Institution';
      var state = statesLookup[stateIdx] || 'US';
      var bType = typesLookup[typeIdx] || 'Commercial Banking Branch';

      var branchObj = {
        id: bId,
        name: bName + ' (Branch #' + bId + ')',
        bank: bName,
        lat: lat,
        lon: lon,
        depM: depM,
        state: state,
        type: bType,
        address: 'Branch Location · ' + state + ', United States'
      };

      function onBranchHover(e) {
        marker.setRadius(radius + 3.5);
        marker.setStyle({ weight: 2.5, color: '#ffffff', fillOpacity: 0.95 });
        showUniversalInspector('bank_branch', branchObj, [lat, lon]);
      }
      function onBranchOut(e) {
        marker.setRadius(radius);
        marker.setStyle({ weight: 1.2, color: '#ffffff', fillOpacity: 0.6 });
      }
      function onBranchClick(e) {
        marker.setRadius(radius + 4.5);
        marker.setStyle({ weight: 3, color: '#00e5ff', fillOpacity: 1 });
        showUniversalInspector('bank_branch', branchObj, [lat, lon]);
        leafletMap.panTo([lat, lon]);
      }

      marker.on('mouseover mousemove', onBranchHover);
      marker.on('mouseout', onBranchOut);
      marker.on('click', onBranchClick);

      var bTooltipHtml = '<div style="font-family:var(--font-mono);font-size:10px;background:rgba(5,8,15,0.96);border:1.5px solid #a855f7;padding:6px 10px;border-radius:4px;box-shadow:0 6px 20px rgba(0,0,0,0.85);color:#fff;min-width:190px;line-height:1.4;">' +
        '<div style="color:#a855f7;font-weight:bold;font-size:11px;">🏛️ ' + bName + '</div>' +
        '<div style="color:#38bdf8;">Branch #' + bId + ' · ' + state + '</div>' +
        '<div><span style="color:#94a3b8;">Type:</span> ' + bType + '</div>' +
        '<div><span style="color:#94a3b8;">Branch Deposits:</span> <strong style="color:#00e676;">$' + depM.toFixed(1) + 'M USD</strong></div>' +
        '<div style="margin-top:3px;padding-top:2px;border-top:1px dashed #1e2e44;color:#ffaa00;font-size:8.5px;">🖱️ Click for Full FDIC Balance Sheet</div>' +
      '</div>';

      marker.bindTooltip(bTooltipHtml, {
        sticky: true,
        opacity: 0.98,
        className: 'bb-custom-tooltip'
      });

      group.addLayer(marker);
    });
  }

"""

js = js[:pos_start] + replacement_branches_render + js[pos_end:]

with open(r'F:\documents\SOIC\EconAgent_Platform\platform_ui\bmap_js_template.js', 'w', encoding='utf-8') as f:
    f.write(js)

print('Successfully replaced renderBankBranchesOnMap in bmap_js_template.js!')

