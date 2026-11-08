with open(r'F:\documents\SOIC\EconAgent_Platform\platform_ui\bmap_js_template.js', 'r', encoding='utf-8') as f:
    code = f.read()

import re
matches = [m.start() for m in re.finditer(r'slider_bank_dep', code)]
print('slider_bank_dep matches:', matches)
for m in matches:
    print('---')
    print(code[m-150:m+250])

