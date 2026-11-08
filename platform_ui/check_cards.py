with open('platform_ui/bmap_js_template.js', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('function renderActiveDatasetCards')
cards_code = text[idx:idx+15000]
import re
cards = re.findall(r'// CARD \d+:[^\n]+', cards_code)
for c in cards:
    print(c)

