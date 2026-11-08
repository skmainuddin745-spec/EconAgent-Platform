with open('platform_ui/bmap_js_template.js', 'r', encoding='utf-8') as f:
    text = f.read()

import re
datasets = [
    'globalLng', 'globalStorage', 'globalGasHubs', 'globalRefineries',
    'globalSeaports', 'globalDataCenters', 'globalSemiconductors',
    'globalFertilizers', 'globalMining', 'gasPipelines'
]

for d in datasets:
    m = re.search(r'var ' + d + r'\s*=\s*\[(.*?)(?:\];|\n\s*var )', text, re.S)
    if m:
        snippet = m.group(1).strip()
        first_item = snippet.split('},')[0] + '}'
        print(f"=== {d} ===")
        print(first_item[:300])

