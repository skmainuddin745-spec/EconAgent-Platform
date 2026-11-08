with open('F:/documents/SOIC/EconAgent_Platform/platform_ui/fractal_zoom_engine.py', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = re.findall(r'tech\.([a-zA-Z0-9_]+)', text)
print("Unique keys on tech:", sorted(set(matches)))

