with open(r'F:\documents\SOIC\EconAgent_Platform\platform_ui\bmap_js_template.js', 'r', encoding='utf-8') as f:
    js = f.read()

target1 = """    var step = Math.max(12, Math.floor(width / 60));
    for (var x = 0; x < width; x += step) {
      for (var y = 0; y < height; y += step) {
        var pt = leafletMap.containerPointToLatLng([x + step / 2, y + step / 2]);
        var lat = pt.lat;
        var lon = pt.lng;"""

replacement1 = """    var step = Math.max(12, Math.floor(width / 60));
    for (var x = 0; x < width; x += step) {
      for (var y = 0; y < height; y += step) {
        var pt;
        try {
          pt = leafletMap.containerPointToLatLng([x + step / 2, y + step / 2]);
        } catch (e) {
          continue;
        }
        if (!pt || isNaN(pt.lat) || isNaN(pt.lng)) continue;
        var lat = pt.lat;
        var lon = pt.lng;"""

target2 = """    var step = Math.max(14, Math.floor(width / 50));
    for (var x = 0; x < width; x += step) {
      for (var y = 0; y < height; y += step) {
        var pt = leafletMap.containerPointToLatLng([x + step / 2, y + step / 2]);
        var lat = pt.lat;
        var lon = pt.lng;"""

replacement2 = """    var step = Math.max(14, Math.floor(width / 50));
    for (var x = 0; x < width; x += step) {
      for (var y = 0; y < height; y += step) {
        var pt;
        try {
          pt = leafletMap.containerPointToLatLng([x + step / 2, y + step / 2]);
        } catch (e) {
          continue;
        }
        if (!pt || isNaN(pt.lat) || isNaN(pt.lng)) continue;
        var lat = pt.lat;
        var lon = pt.lng;"""

assert target1 in js, "target1 not found in bmap_js_template.js"
assert target2 in js, "target2 not found in bmap_js_template.js"

js = js.replace(target1, replacement1).replace(target2, replacement2)

with open(r'F:\documents\SOIC\EconAgent_Platform\platform_ui\bmap_js_template.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("Weather heatmaps patched with safe containerPointToLatLng!")

