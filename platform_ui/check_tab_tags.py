with open(r'F:\documents\SOIC\EconAgent_Platform\platform_ui\generate_dashboard.py', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = re.findall(r'<[^>]+onclick=["\']showTab\([^>]+>', text)
print(f"Total onclick showTab elements in generate_dashboard.py: {len(matches)}")
for m in matches[:15]:
    print(' ', m)

