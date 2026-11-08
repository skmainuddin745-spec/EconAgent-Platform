with open(r'F:\documents\SOIC\EconAgent_Platform\platform_ui\EconAgent_Dashboard.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = [m.start() for m in re.finditer(r'global_sector_select', text)]
print('Total matches for global_sector_select in EconAgent_Dashboard.html:', len(matches))
for m in matches:
    print(repr(text[max(0, m-50):min(len(text), m+150)]))

