with open('platform_ui/institutional_giants_engine.py', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = re.findall(r'<script.*?</script>', text, re.S)
print('Scripts count:', len(matches))
for i, s in enumerate(matches):
    print(f"--- Script {i+1} ({len(s)} chars) ---")
    print(s[:300])
