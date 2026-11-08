with open('F:/documents/SOIC/EconAgent_Platform/platform_ui/bmap_js_template.js', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = re.findall(r'datasetLayerGroups\[[\'"].*?[\'"]\]', text)
print(sorted(list(set(matches))))

