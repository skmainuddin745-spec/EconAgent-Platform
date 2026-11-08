import re

with open(r'F:\documents\SOIC\EconAgent_Platform\platform_ui\generate_dashboard.py', 'r', encoding='utf-8') as f:
    text = f.read()

# Find all tab onclicks
tab_calls = re.findall(r'showTab\([^,]+,\s*[\'"]([^\'"]+)[\'"]\)', text)
unique_tabs = []
for t in tab_calls:
    if t not in unique_tabs:
        unique_tabs.append(t)

print(f"Total Unique Tab IDs called in showTab: {len(unique_tabs)}")
for t in unique_tabs:
    has_div = f'id="{t}"' in text or f"id='{t}'" in text
    print(f"Tab '{t}': {'DIV EXISTS' if has_div else '*** MISSING DIV ***'}")

