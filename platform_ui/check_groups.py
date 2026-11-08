with open('platform_ui/bmap_js_template.js', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = re.findall(r"datasetLayerGroups\[['\"][^'\"]+['\"]] = [^;\n]+", text)
print('datasetLayerGroups populated:', len(matches))
for m in matches:
    print(' ', m)

