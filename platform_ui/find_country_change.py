with open(r'F:\documents\SOIC\EconAgent_Platform\platform_ui\generate_dashboard.py', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('onCountryDropdownChange')
if idx != -1:
    print('FOUND onCountryDropdownChange IN generate_dashboard.py:')
    print(text[idx-50:idx+1500])
else:
    print('NOT FOUND in generate_dashboard.py')

