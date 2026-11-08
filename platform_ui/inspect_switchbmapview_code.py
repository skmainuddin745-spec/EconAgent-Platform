with open(r'F:\documents\SOIC\EconAgent_Platform\platform_ui\bmap_js_template.js', 'r', encoding='utf-8') as f:
    js = f.read()

idx = js.find('window.switchBmapView = function(viewId)')
print(js[idx:idx+1200])

