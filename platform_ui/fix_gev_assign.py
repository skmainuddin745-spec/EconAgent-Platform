with open('platform_ui/bmap_js_template.js', 'r', encoding='utf-8') as f:
    text = f.read()

import re
old_block = """        // Vite 3D server is active and reachable!
        if (fallback) fallback.style.display = 'none';
        if (iframe) {
          iframe.style.display = 'block';
          if (!iframe.src || iframe.src.indexOf('4173') === -1 || forceReload) {
            iframe.src = 'http://127.0.0.1:4173/?embed=1';
          }
        }"""

new_block = """        // Vite 3D server is active and reachable!
        if (fallback) fallback.style.display = 'none';
        if (iframe) {
          iframe.style.display = 'block';
          if (iframe.src !== 'http://127.0.0.1:4173/?embed=1') {
            iframe.src = 'http://127.0.0.1:4173/?embed=1';
          }
        }"""

if old_block in text:
    text = text.replace(old_block, new_block)
    print("Replaced old_block in bmap_js_template.js")
    with open('platform_ui/bmap_js_template.js', 'w', encoding='utf-8') as f:
        f.write(text)
else:
    print("Warning: old_block not found in bmap_js_template.js")

