with open('platform_ui/EconAgent_Dashboard.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = re.finditer(r'switchTitanTab', text)
for m in matches:
    pos = m.start()
    print('Match at', pos)
    print(text[pos-40:pos+250])

