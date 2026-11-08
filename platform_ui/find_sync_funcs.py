with open(r'F:\documents\SOIC\EconAgent_Platform\platform_ui\generate_dashboard.py', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('function syncGlobalCountryChange')
if idx != -1:
    print('syncGlobalCountryChange FUNCTION:')
    print(text[idx:idx+2000])
else:
    print('syncGlobalCountryChange not found')

