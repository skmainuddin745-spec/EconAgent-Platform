with open(r'F:\documents\SOIC\EconAgent_Platform\platform_ui\generate_dashboard.py', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = [m.start() for m in re.finditer(r'technicals', text)]
print('Matches for "technicals" in generate_dashboard.py:', len(matches))
for m in matches:
    print('  Context:', repr(text[max(0, m-40):min(len(text), m+80)]))

