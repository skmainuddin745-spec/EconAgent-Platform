with open('platform_ui/bmap_js_template.js', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('addPointsLayer(\'cyclones\', globalCyclones, \'#ef4444\', 7, false);')
print(text[idx-100:idx+300])

