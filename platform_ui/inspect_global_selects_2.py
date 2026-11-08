with open(r'F:\documents\SOIC\EconAgent_Platform\platform_ui\generate_dashboard.py', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('id="global_sector_select"')
print(text[idx:idx+2500])

