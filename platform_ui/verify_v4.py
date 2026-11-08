from pathlib import Path

bmap_path = Path(r"F:\documents\SOIC\EconAgent_Platform\platform_ui\Bloomberg_BMAP_Terminal.html")
dash_path = Path(r"F:\documents\SOIC\EconAgent_Platform\platform_ui\EconAgent_Dashboard.html")

with open(bmap_path, "r", encoding="utf-8") as f:
    bmap_html = f.read()

with open(dash_path, "r", encoding="utf-8") as f:
    dash_html = f.read()

v4_checks = {
    "No CartoDB API Key URL in BMAP": "cartocdn.com" not in bmap_html,
    "No CartoDB in Dashboard": "cartocdn.com" not in dash_html,
    "Esri Dark Gray Base Present": "World_Dark_Gray_Base" in bmap_html,
    "Esri Dark Gray Reference Present": "World_Dark_Gray_Reference" in bmap_html,
    "Esri World Imagery Present": "World_Imagery" in bmap_html,
    "minZoom is set to 1 (allows full world zoom out)": "minZoom: 1" in bmap_html,
    "maxBounds set for global framing": "maxBounds:" in bmap_html,
    "Global viewport fits world at zoom 1": "leafletMap.flyTo([15.00, 0.00], 1" in bmap_html,
    "LOD tug hiding at wide zoom": "z <= 7 && (obj.category === 'tug'" in bmap_html,
    "Label deconfliction active": "showLabel = (z >= 11) || isSelected" in bmap_html,
    "Global shipping density dots present": "globalTankerDots" in bmap_html,
    "Upward market trend chart watermark present": "<svg width=\"42\" height=\"32\"" in bmap_html,
    "Floating amber card present": 'id="bmap_amber_card"' in bmap_html,
    "Target reticle O present": "drawCenterReticle()" in bmap_html,
    "SOIC 5-Bucket Allocation in Dashboard": "tn_pane_soic_alloc" in dash_html
}

all_pass = True
for name, res in v4_checks.items():
    st = "✅ PASS" if res else "❌ FAIL"
    print(f"{st}: {name}")
    if not res:
        all_pass = False

print(f"\nALL V4 ARCHITECTURAL CHECKS PASSED: {all_pass}")

