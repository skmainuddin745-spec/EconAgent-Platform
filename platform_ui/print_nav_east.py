with open(r'F:\documents\SOIC\EconAgent_Platform\platform_ui\bmap_js_template.js', 'r', encoding='utf-8') as f:
    js = f.read()

idx = js.find('window.bmapNavigateEast = function')
print(repr(js[idx:idx+500]))

