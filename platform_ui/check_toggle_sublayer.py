with open('platform_ui/bmap_js_template.js', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('function toggleSubLayer')
if idx == -1:
    idx = text.find('toggleSubLayer')
print('toggleSubLayer at:', idx)
print(text[idx-50:idx+1500])

