with open(r'F:\documents\SOIC\EconAgent_Platform\platform_ui\generate_dashboard.py', 'r', encoding='utf-8') as f:
    text = f.read()

s_tag = "// ── UNIVERSAL GLOBAL DROPDOWN MASTER SYNCHRONIZATION ──"
e_tag = "function jumpToTabForActiveFirm"

idx1 = text.find(s_tag)
idx2 = text.find(e_tag)

print(text[idx1:idx1+1500])

