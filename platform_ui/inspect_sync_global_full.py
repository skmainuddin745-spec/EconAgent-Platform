with open(r'F:\documents\SOIC\EconAgent_Platform\platform_ui\generate_dashboard.py', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('function syncGlobalCountryChange')
print('Excerpt from generate_dashboard.py around syncGlobalCountryChange:')
print(text[idx-50:idx+3000])

