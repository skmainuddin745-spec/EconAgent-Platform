with open('platform_ui/bmap_js_template.js', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = re.finditer(r'(toggleNaturalGas|naturalGasConfig|initNaturalGas)', text)
for m in matches:
    pos = m.start()
    print('Match at', pos)
    print(text[pos-50:pos+300])

