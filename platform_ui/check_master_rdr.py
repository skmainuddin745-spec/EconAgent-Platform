with open('platform_ui/bmap_js_template.js', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = re.finditer(r'masterCanvasRenderer', text)
for m in matches:
    pos = m.start()
    print('masterCanvasRenderer at', pos)
    print(text[pos-40:pos+250])

