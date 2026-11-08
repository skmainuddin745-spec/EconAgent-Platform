with open(r'F:\documents\SOIC\EconAgent_Platform\platform_ui\generate_dashboard.py', 'r', encoding='utf-8') as f:
    code = f.read()

import re
imports = re.findall(r'from \w+ import \w+|import \w+', code)
print('Imports in generate_dashboard.py:')
for imp in imports:
    print(' ', imp)

pos = code.find('bmap')
print('\nbmap occurrence in generate_dashboard.py:', pos)
if pos != -1:
    print(code[pos-100:pos+500])

