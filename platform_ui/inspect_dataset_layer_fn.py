with open('F:/documents/SOIC/EconAgent_Platform/platform_ui/bmap_tanker_component.py', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = [m.start() for m in re.finditer(r'function renderDatasetLayer', text)]
for idx in matches:
    print('renderDatasetLayer:')
    print(text[idx:idx+800])

# Also search for where globalSeaports is rendered
matches2 = [m.start() for m in re.finditer(r'globalSeaports\.forEach|seaports', text, re.IGNORECASE)]
for idx in matches2[:5]:
    print('Seaports match:')
    print(text[idx-20:idx+300])

