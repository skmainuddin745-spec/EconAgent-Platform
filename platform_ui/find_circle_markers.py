with open('F:/documents/SOIC/EconAgent_Platform/platform_ui/bmap_tanker_component.py', 'r', encoding='utf-8') as f:
    text = f.read()

import re

# Find arrays or definitions for ports, storage, terminals, etc.
arrays = re.findall(r'var\s+([a-zA-Z0-9_]+)\s*=\s*\[\s*\{', text)
print('Data arrays in bmap_tanker_component.py:', arrays)

# Find circleMarker creation in the layers
circle_defs = [m.start() for m in re.finditer(r'circleMarker', text)]
print(f'Total circleMarker usages: {len(circle_defs)}')
for idx in circle_defs:
    print('--- circleMarker usage ---')
    print(text[idx-40:idx+350])

