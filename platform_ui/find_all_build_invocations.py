with open(r'F:\documents\SOIC\EconAgent_Platform\platform_ui\generate_dashboard.py', 'r', encoding='utf-8') as f:
    text = f.read()

import re
calls = re.findall(r'[a-zA-Z0-9_]+\s*=\s*build_[a-zA-Z0-9_]+\([^)]*\)', text)
for c in calls:
    print(' ', c)

