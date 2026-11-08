js_path = 'F:/documents/SOIC/EconAgent_Platform/platform_ui/bmap_js_template.js'
with open(js_path, 'r', encoding='utf-8') as f:
    js = f.read()

old_code = '''    // Manhattan high-res branch markers (Images 7, 9, 10)
    var manLayer = L.layerGroup();
    manhattanBranches.forEach(function(mb) {
      var m = L.circleMarker([mb.lat, mb.lon], {
        renderer: canvasRenderer,'''

new_code = '''    // Manhattan high-res branch markers (Images 7, 9, 10)
    var manLayer = L.layerGroup();
    manhattanBranches.forEach(function(mb) {
      var m = L.circleMarker([mb.lat, mb.lon], {
        renderer: window.masterCanvasRenderer,'''

assert old_code in js, "old_code not found"
js = js.replace(old_code, new_code, 1)

with open(js_path, 'w', encoding='utf-8') as f:
    f.write(js)

print("Fixed canvasRenderer in manhattanBranches in bmap_js_template.js!")

