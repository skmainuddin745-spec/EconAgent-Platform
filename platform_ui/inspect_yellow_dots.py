with open('F:/documents/SOIC/EconAgent_Platform/platform_ui/bmap_tanker_component.py', 'r', encoding='utf-8') as f:
    text = f.read()

import re
idx = text.find("fillColor: '#facc15'")
if idx != -1:
    print('Yellow dots code:')
    print(text[idx-50:idx+600])

