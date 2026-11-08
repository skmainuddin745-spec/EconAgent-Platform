import os

BASE_DIR = r'F:\documents\SOIC\EconAgent_Platform\platform_ui'
js_path = os.path.join(BASE_DIR, 'bmap_js_template.js')

with open(js_path, 'r', encoding='utf-8') as f:
    js = f.read()

print('Initial JS length:', len(js))

# Check for our key targets
targets = [
    'function initPipelinesLayers()',
    'function initWorldEquityLayer()',
    'function initDenseGridLayer()',
    'function initBankBranchesLayer()',
    'function renderBankBranchesOnMap(branches)',
    'window.filterBankBranches = function()',
    'function addPointsLayer(key, dataList, color, radius, isDefaultOn)',
    'showUniversalVesselPopup = function(v)',
    'var SUGGESTED_DATASETS = [',
    'var NEW_DATASETS = [',
    '// CARD 5: NATURAL GAS (SCREENSHOT 12)'
]

for t in targets:
    pos = js.find(t)
    print(f'{t[:35]}: pos={pos}')

