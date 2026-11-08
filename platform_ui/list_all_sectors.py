with open(r'F:\documents\SOIC\EconAgent_Platform\platform_ui\fractal_zoom_engine.py', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = re.findall(r'(\w+):\s*\{\s*name:\s*[\'"]([^\'"]+)[\'"],\s*country:\s*[\'"]([^\'"]+)[\'"]', text)
print(f"Total sectors ({len(matches)}):")
for s_key, s_name, c_key in matches:
    print(f" - {s_key:15s} [{c_key:10s}]: {s_name}")

