with open('platform_ui/bmap_js_template.js', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('window.addBmapDataset = function')
print(text[idx:idx+2500])

