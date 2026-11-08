with open('F:/documents/SOIC/EconAgent_Platform/platform_ui/fractal_zoom_engine.py', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = [m.start() for m in re.finditer(r'firmData|sectorData|countryData', text)]
for pos in matches[:10]:
    print('Match at pos', pos)
    print(text[pos:pos+300])
    print('='*50)

