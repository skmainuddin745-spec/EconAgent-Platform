with open('platform_ui/bmap_js_template.js', 'r', encoding='utf-8') as f:
    text = f.read()

import re
arrays = re.findall(r'var ([a-zA-Z0-9_]+)\s*=\s*\[\{', text)
print('Data arrays found with object elements:')
for a in set(arrays):
    print(' ', a)

