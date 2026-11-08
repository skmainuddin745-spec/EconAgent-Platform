with open('F:/documents/SOIC/EconAgent_Platform/platform_ui/bmap_tanker_component.py', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = [m.start() for m in re.finditer(r'destinationRoute|routeLine|activeRoute', text)]
for idx in matches:
    print('Route snippet:')
    print(text[idx-50:idx+250])

