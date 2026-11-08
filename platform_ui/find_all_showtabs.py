import re

with open(r'F:\documents\SOIC\EconAgent_Platform\platform_ui\EconAgent_Dashboard.html', 'r', encoding='utf-8') as f:
    html = f.read()

matches = re.findall(r'showTab\([^)]+\)', html)
print('ALL SHOWTAB CALLS IN HTML:')
for m in sorted(list(set(matches))):
    print(' ', m)

