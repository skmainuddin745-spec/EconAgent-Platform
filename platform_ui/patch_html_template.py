with open(r'F:\documents\SOIC\EconAgent_Platform\platform_ui\bmap_html_template.html', 'r', encoding='utf-8') as f:
    html = f.read()

target = '''        <div style="display: flex; justify-content: space-between;"><span style="color: #94a3b8;">Navigation Status:</span><span id="uni_vessel_status" style="color: #00e676;">Under way using engine</span></div>
        <div style="display: flex; justify-content: space-between;"><span style="color: #94a3b8;">IMO / MMSI:</span><span id="uni_vessel_imo" style="color: #fff;">9394562 / 538002941</span></div>
        <div style="display: flex; justify-content: space-between;"><span style="color: #94a3b8;">Owner / Charterer:</span><span id="uni_vessel_owner" style="color: #ffaa00;">International Seaways</span></div>
        <div style="display: flex; justify-content: space-between;"><span style="color: #94a3b8;">Destination:</span><strong id="uni_vessel_dest" style="color: #38bdf8;">China (Ningbo)</strong></div>
        <div style="display: flex; justify-content: space-between;"><span style="color: #94a3b8;">Berth / Zone:</span><span id="uni_vessel_berth" style="color: #cbd5e1;">Strait of Hormuz Inbound</span></div>
        <div style="display: flex; justify-content: space-between;"><span style="color: #94a3b8;">Speed / Course:</span><span id="uni_vessel_speed" style="color: #00e676; font-weight: bold;">11.4 kn @ 68°</span></div>
        <div style="display: flex; justify-content: space-between;"><span style="color: #94a3b8;">Draft / DWT:</span><span id="uni_vessel_draft_dwt" style="color: #ffaa00;">21.2m · 318,000 MT</span></div>
        <div style="display: flex; gap: 6px; margin-top: 6px; border-top: 1px solid #162438; padding-top: 6px;">
          <button onclick="zoomToActiveVessel()" style="flex: 1; background: #0284c7; color: #fff; border: 1px solid #38bdf8; border-radius: 2px; padding: 4px 6px; font-size: 9.5px; font-weight: 800; cursor: pointer;">[Zoom To]</button>
          <button onclick="viewActiveVesselHistory()" style="flex: 1; background: #111a28; color: #ffaa00; border: 1px solid #ffaa00; border-radius: 2px; padding: 4px 6px; font-size: 9.5px; font-weight: 800; cursor: pointer;">[View History]</button>
          <div style="position: relative;">
            <button onclick="toggleUniversalVesselMoreDropdown()" style="background: #111f33; color: #00e5ff; border: 1px solid #1e3a5f; padding: 4px 8px; font-size: 9.5px; border-radius: 2px; cursor: pointer; font-weight: 700;">More ▾</button>'''

replacement = '''        <div style="display: flex; justify-content: space-between;"><span id="uni_lbl_1" style="color: #94a3b8;">Navigation Status:</span><span id="uni_vessel_status" style="color: #00e676;">Under way using engine</span></div>
        <div style="display: flex; justify-content: space-between;"><span id="uni_lbl_2" style="color: #94a3b8;">IMO / MMSI:</span><span id="uni_vessel_imo" style="color: #fff;">9394562 / 538002941</span></div>
        <div style="display: flex; justify-content: space-between;"><span id="uni_lbl_3" style="color: #94a3b8;">Owner / Charterer:</span><span id="uni_vessel_owner" style="color: #ffaa00;">International Seaways</span></div>
        <div style="display: flex; justify-content: space-between;"><span id="uni_lbl_4" style="color: #94a3b8;">Destination:</span><strong id="uni_vessel_dest" style="color: #38bdf8;">China (Ningbo)</strong></div>
        <div style="display: flex; justify-content: space-between;"><span id="uni_lbl_5" style="color: #94a3b8;">Berth / Zone:</span><span id="uni_vessel_berth" style="color: #cbd5e1;">Strait of Hormuz Inbound</span></div>
        <div style="display: flex; justify-content: space-between;"><span id="uni_lbl_6" style="color: #94a3b8;">Speed / Course:</span><span id="uni_vessel_speed" style="color: #00e676; font-weight: bold;">11.4 kn @ 68°</span></div>
        <div style="display: flex; justify-content: space-between;"><span id="uni_lbl_7" style="color: #94a3b8;">Draft / DWT:</span><span id="uni_vessel_draft_dwt" style="color: #ffaa00;">21.2m · 318,000 MT</span></div>
        <div style="display: flex; gap: 6px; margin-top: 6px; border-top: 1px solid #162438; padding-top: 6px;">
          <button id="btn_uni_zoom" onclick="zoomToActiveAsset()" style="flex: 1; background: #0284c7; color: #fff; border: 1px solid #38bdf8; border-radius: 2px; padding: 4px 6px; font-size: 9.5px; font-weight: 800; cursor: pointer;">[Zoom To]</button>
          <button id="btn_uni_history" onclick="viewActiveAssetAnalytics()" style="flex: 1; background: #111a28; color: #ffaa00; border: 1px solid #ffaa00; border-radius: 2px; padding: 4px 6px; font-size: 9.5px; font-weight: 800; cursor: pointer;">[View History]</button>
          <div style="position: relative;">
            <button onclick="toggleUniversalInspectorMoreDropdown()" style="background: #111f33; color: #00e5ff; border: 1px solid #1e3a5f; padding: 4px 8px; font-size: 9.5px; border-radius: 2px; cursor: pointer; font-weight: 700;">More ▾</button>'''

if target in html:
    html = html.replace(target, replacement)
    with open(r'F:\documents\SOIC\EconAgent_Platform\platform_ui\bmap_html_template.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print('bmap_html_template.html successfully updated with universal label IDs and zoom action!')
else:
    print('Target not found in bmap_html_template.html!')

