with open(r'F:\documents\SOIC\EconAgent_Platform\platform_ui\EconAgent_Dashboard.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = [m.start() for m in re.finditer(r'global_sector_select', text)]

print('--- MATCH 2 CONTEXT ---')
print(text[matches[1]-200:matches[1]+800])

print('--- MATCH 3 CONTEXT ---')
print(text[matches[2]-200:matches[2]+800])

