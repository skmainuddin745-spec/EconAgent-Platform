with open(r'F:\documents\SOIC\EconAgent_Platform\platform_ui\fractal_zoom_engine.py', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = re.findall(r'(\w+):\s*\{[^\}]*?firmKeys:\s*\[([^\]]*)\]', text)
print("Sectors with firmKeys:")
for s_key, f_keys in matches:
    print(f" - {s_key:15s}: [{f_keys.strip()}]")

