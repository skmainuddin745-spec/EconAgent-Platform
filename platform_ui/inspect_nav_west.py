with open(r'F:\documents\SOIC\EconAgent_Platform\platform_ui\bmap_js_template.js', 'r', encoding='utf-8') as f:
    js = f.read()

idx = js.find('function bmapNavigateWest')
if idx != -1:
    print('bmapNavigateWest code:')
    print(js[idx:idx+800])
else:
    print('bmapNavigateWest NOT FOUND')

