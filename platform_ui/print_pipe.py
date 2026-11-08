with open('F:/documents/SOIC/EconAgent_Platform/platform_ui/bmap_js_template.js', 'r', encoding='utf-8') as f:
    text = f.read()

import re
m = re.search(r'id:\s*[\'"]pipe_petroline[\'"].*?coords:\s*(\[.*?\])\s*,', text, re.DOTALL)
if m:
    print('Found coords:', m.group(1))
else:
    print('Not found')

