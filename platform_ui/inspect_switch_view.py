import re

with open(r'F:\documents\SOIC\EconAgent_Platform\platform_ui\bmap_html_template.html', 'r', encoding='utf-8') as f:
    text = f.read()

views = re.findall(r'<div id="bmap_view_[^"]+"[^>]*>', text)
for v in views:
    print('VIEW DIV:', v)

# Check bmap_js_template.js for switchBmapView
with open(r'F:\documents\SOIC\EconAgent_Platform\platform_ui\bmap_js_template.js', 'r', encoding='utf-8') as f:
    js = f.read()

idx = js.find('function switchBmapView')
if idx != -1:
    print('SWITCH_BMAP_VIEW CODE:')
    print(js[idx:idx+2000])
else:
    print('switchBmapView NOT FOUND')

