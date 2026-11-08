with open(r'F:\documents\SOIC\EconAgent_Platform\platform_ui\generate_dashboard.py', 'r', encoding='utf-8') as f:
    code = f.read()

idx = code.find('function showTab(el, tabId)')
if idx != -1:
    print('SHOWTAB FUNCTION:')
    print(code[idx:idx+800])
else:
    print('showTab not found')

# Also find where tab buttons are defined in generate_dashboard.py
import re
tabs = re.findall(r'<button[^>]*showTab[^>]*>[^<]*</button>', code)
print('FOUND TABS:', len(tabs))
for t in tabs[:10]:
    print(' ', t)

