with open(r'F:\documents\SOIC\EconAgent_Platform\platform_ui\generate_dashboard.py', 'r', encoding='utf-8') as f:
    code = f.read()

import re
matches = [m.start() for m in re.finditer(r'window\.loadSoicStock', code)]
print('Matches for window.loadSoicStock in generate_dashboard.py:', len(matches))
for m in matches:
    print(repr(code[max(0, m-80):min(len(code), m+120)]))

