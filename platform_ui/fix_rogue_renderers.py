import re

js_path = 'F:/documents/SOIC/EconAgent_Platform/platform_ui/bmap_js_template.js'
with open(js_path, 'r', encoding='utf-8') as f:
    js = f.read()

# 1. Fix manhattanBranches
old_mb = '''    manhattanBranches.forEach(function(mb) {
      var m = L.circleMarker([mb.lat, mb.lon], {
        radius: 8,'''

new_mb = '''    manhattanBranches.forEach(function(mb) {
      var m = L.circleMarker([mb.lat, mb.lon], {
        renderer: canvasRenderer,
        radius: 8,'''

assert old_mb in js, "old_mb not found"
js = js.replace(old_mb, new_mb, 1)

# 2. Fix gasPipelines hitBuffer
old_gas_hb = '''    gasPipelines.forEach(function(gpipe) {
      var hitBuffer = L.polyline(gpipe.coords, {
        weight: 22,
        opacity: 0,
        interactive: true
      });'''

new_gas_hb = '''    gasPipelines.forEach(function(gpipe) {
      var hitBuffer = L.polyline(gpipe.coords, {
        renderer: window.masterCanvasRenderer,
        weight: 22,
        opacity: 0.001,
        interactive: true
      });'''

if old_gas_hb in js:
    js = js.replace(old_gas_hb, new_gas_hb, 1)

# 3. Fix gregMortimer track
old_gm = '''    var gmTrack = L.polyline(gregMortimer.track, {
      color: '#eab308','''

new_gm = '''    var gmTrack = L.polyline(gregMortimer.track, {
      renderer: window.masterCanvasRenderer,
      color: '#eab308','''

assert old_gm in js, "old_gm not found"
js = js.replace(old_gm, new_gm, 1)

with open(js_path, 'w', encoding='utf-8') as f:
    f.write(js)

print("Fixed manhattanBranches, gasPipelines hitBuffer, and gregMortimer track!")

