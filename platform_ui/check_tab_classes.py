with open(r'F:\documents\SOIC\EconAgent_Platform\platform_ui\generate_dashboard.py', 'r', encoding='utf-8') as f:
    text = f.read()

import re
tab_tags = re.findall(r'<button[^>]*showTab[^>]*>', text)
print(f"Total showTab buttons in generate_dashboard.py: {len(tab_tags)}")
for t in tab_tags[:15]:
    print(' ', t)

