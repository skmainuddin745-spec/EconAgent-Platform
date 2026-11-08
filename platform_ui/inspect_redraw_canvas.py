with open(r'F:\documents\SOIC\EconAgent_Platform\platform_ui\bmap_js_template.js', 'r', encoding='utf-8') as f:
    js = f.read()

idx1 = js.find('function redrawWeatherHeatmap')
idx2 = js.find('function redrawCanvasOverlay')

print('redrawWeatherHeatmap excerpt:')
print(js[idx1:idx1+800])
print('redrawCanvasOverlay excerpt:')
print(js[idx2:idx2+800])

