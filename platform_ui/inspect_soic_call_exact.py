with open(r'F:\documents\SOIC\EconAgent_Platform\platform_ui\generate_dashboard.py', 'r', encoding='utf-8') as f:
    code = f.read()

idx = code.find('loadSoicStock')
print(repr(code[idx-100:idx+250]))

