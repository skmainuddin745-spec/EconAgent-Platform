with open(r'F:\documents\SOIC\EconAgent_Platform\platform_ui\generate_dashboard.py', 'r', encoding='utf-8') as f:
    code = f.read()

s_tag = "// ── UNIVERSAL GLOBAL DROPDOWN MASTER SYNCHRONIZATION ──"
e_tag = "function jumpToTabForActiveFirm(tabId)"

s_idx = code.find(s_tag)
e_idx = code.find(e_tag)

assert s_idx != -1 and e_idx != -1

sync_section = code[s_idx:e_idx]

# Replace single braces with double braces in sync_section, taking care of JSON
# To be completely safe and avoid JSON quote/brace f-string conflicts,
# we can double all { and } in sync_section!

doubled_sync = sync_section.replace('{', '{{').replace('}', '}}')

new_code = code[:s_idx] + doubled_sync + code[e_idx:]

with open(r'F:\documents\SOIC\EconAgent_Platform\platform_ui\generate_dashboard.py', 'w', encoding='utf-8') as f:
    f.write(new_code)

print("Braces doubled in sync section successfully!")

