with open(r'F:\documents\SOIC\EconAgent_Platform\platform_ui\fractal_zoom_engine.py', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = [m.start() for m in re.finditer(r'global_sector_select|global_firm_select', text)]
print('Matches in fractal_zoom_engine.py:', len(matches))
for m in matches:
    print(repr(text[max(0, m-40):min(len(text), m+80)]))

