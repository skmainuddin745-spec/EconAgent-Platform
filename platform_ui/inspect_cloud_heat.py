with open(r'F:\documents\SOIC\EconAgent_Platform\platform_ui\bmap_js_template.js', 'r', encoding='utf-8') as f:
    js = f.read()

idx = js.find('function drawCloudCoverHeatmap')
print(js[idx:idx+1200])

