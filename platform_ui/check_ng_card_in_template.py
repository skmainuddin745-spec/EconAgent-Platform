with open('platform_ui/bmap_js_template.js', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('Natural Gas & Global Energy Pipelines')
print('Found in bmap_js_template.js:', idx != -1)
if idx != -1:
    print(text[idx-50:idx+200])

