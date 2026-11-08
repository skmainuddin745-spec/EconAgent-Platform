with open(r'F:\documents\SOIC\EconAgent_Platform\platform_ui\bmap_js_template.js', 'r', encoding='utf-8') as f:
    js = f.read()

import re
matches = [m.start() for m in re.finditer(r'bmapNavigateWest', js)]
print('Matches for bmapNavigateWest in bmap_js_template.js:', len(matches))
for m in matches:
    print(repr(js[max(0, m-50):min(len(js), m+200)]))

