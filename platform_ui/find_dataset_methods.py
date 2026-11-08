with open(r'F:\documents\SOIC\EconAgent_Platform\platform_ui\bmap_js_template.js', 'r', encoding='utf-8') as f:
    code = f.read()

import re
matches = [m.start() for m in re.finditer(r'removeBmapDataset', code)]
print('removeBmapDataset Matches:', matches)
for m in matches:
    print('---')
    print(code[m-50:m+250])

matches2 = [m.start() for m in re.finditer(r'addBmapDataset', code)]
print('addBmapDataset Matches:', matches2)
for m in matches2:
    print('---')
    print(code[m-50:m+250])

