with open('F:/documents/SOIC/EconAgent_Platform/platform_ui/bmap_html_template.html', 'r', encoding='utf-8') as f:
    html_tpl = f.read()

import re
open_divs = len(re.findall(r'<div\b', html_tpl, re.IGNORECASE))
close_divs = len(re.findall(r'</div>', html_tpl, re.IGNORECASE))
print('bmap_html_template.html:')
print(f'  <div count: {open_divs}')
print(f'  </div> count: {close_divs}')
print(f'  Difference: {open_divs - close_divs} (UNCLOSED DIVS!)')

with open('F:/documents/SOIC/EconAgent_Platform/platform_ui/bmap_tanker_component.py', 'r', encoding='utf-8') as f:
    tanker_comp = f.read()

open_divs_t = len(re.findall(r'<div\b', tanker_comp, re.IGNORECASE))
close_divs_t = len(re.findall(r'</div>', tanker_comp, re.IGNORECASE))
print('\nbmap_tanker_component.py:')
print(f'  <div count: {open_divs_t}')
print(f'  </div> count: {close_divs_t}')
print(f'  Difference: {open_divs_t - close_divs_t} (UNCLOSED DIVS!)')

