with open(r'F:\documents\SOIC\EconAgent_Platform\platform_ui\generate_dashboard.py', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('GLOBAL COUNTRY')
if idx != -1:
    print('GLOBAL SELECT SECTION IN generate_dashboard.py:')
    print(text[idx-100:idx+2500])
else:
    print('GLOBAL COUNTRY not found in generate_dashboard.py')

