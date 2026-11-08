with open('platform_ui/bmap_js_template.js', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('function initPipelinesLayers')
print('=== PIPELINES ===')
print(text[idx:idx+2500])

idx2 = text.find('function initDenseGridLayer')
if idx2 == -1:
    idx2 = text.find('globalDenseGrid')
print('=== DENSE GRID ===')
print(text[idx2:idx2+2500])

