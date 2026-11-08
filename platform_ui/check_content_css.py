with open('platform_ui/generate_dashboard.py', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = re.findall(r'\.content[^{]*\{[^}]*\}', text)
for m in matches:
    print('CONTENT CSS:', m)

