with open('F:/documents/SOIC/EconAgent_Platform/platform_ui/bmap_tanker_component.py', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = [m.start() for m in re.finditer(r'globalSeaports', text)]
for idx in matches:
    print('globalSeaports usage:')
    print(text[idx-40:idx+350])

