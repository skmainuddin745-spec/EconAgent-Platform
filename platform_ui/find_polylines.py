with open('F:/documents/SOIC/EconAgent_Platform/platform_ui/bmap_tanker_component.py', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = [m.start() for m in re.finditer(r'L\.polyline', text)]
print('L.polyline count:', len(matches))
for idx in matches:
    print('--- Polyline ---')
    print(text[idx-50:idx+350])

