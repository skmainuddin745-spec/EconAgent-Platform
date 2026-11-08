with open(r'F:\documents\SOIC\EconAgent_Platform\platform_ui\bmap_html_template.html', 'r', encoding='utf-8') as f:
    code = f.read()

pos = code.find('Natural Gas')
print('Natural Gas occurrences in bmap_html_template.html:')
import re
for m in re.finditer(r'Natural Gas', code):
    print(m.start())
    print(code[m.start()-50:m.start()+400])
    print('---')

