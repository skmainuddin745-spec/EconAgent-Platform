with open(r'F:\documents\SOIC\EconAgent_Platform\platform_ui\EconAgent_Dashboard.html', 'r', encoding='utf-8') as f:
    text = f.read()

s_tag = "// ── UNIVERSAL GLOBAL DROPDOWN MASTER SYNCHRONIZATION ──"
idx = text.find(s_tag)
print(text[idx:idx+800])

