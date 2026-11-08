with open('F:/documents/SOIC/EconAgent_Platform/platform_ui/realtime_technicals_component.py', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = re.findall(r'id=["\']tech_[^"\']+["\']', text)
print("Technical IDs:", sorted(set(matches)))

