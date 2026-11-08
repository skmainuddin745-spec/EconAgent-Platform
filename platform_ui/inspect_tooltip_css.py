with open('F:/documents/SOIC/EconAgent_Platform/platform_ui/EconAgent_Dashboard.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = [m.start() for m in re.finditer(r'bb-custom-tooltip|\.leaflet-tooltip', text)]
for idx in matches:
    print('--- CSS SNIPPET ---')
    print(text[idx-50:idx+250])

