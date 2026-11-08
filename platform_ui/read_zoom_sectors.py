with open(r'F:\documents\SOIC\EconAgent_Platform\platform_ui\fractal_zoom_engine.py', 'r', encoding='utf-8') as f:
    text = f.read()

import re
m_sec = re.search(r'var sectorData\s*=\s*\{([\s\S]*?)\n  \};', text)
if m_sec:
    print("SECTOR KEYS:")
    for line in m_sec.group(1).strip().splitlines()[:35]:
        if 'name:' in line or 'firmKeys:' in line:
            print(" ", line.strip())

