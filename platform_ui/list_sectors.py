with open('F:/documents/SOIC/EconAgent_Platform/platform_ui/fractal_zoom_engine.py', 'r', encoding='utf-8') as f:
    text = f.read()

pos1 = text.find('sectorData = {')
pos2 = text.find('firmData = {')
block = text[pos1:pos2]

import re
lines = block.split('\n')
for line in lines:
    if ':' in line and '{' in line and not line.strip().startswith('//'):
        print(line[:80])
    if 'firmKeys' in line:
        print('   ', line.strip())

