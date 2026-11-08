with open(r'F:\documents\SOIC\EconAgent_Platform\platform_ui\fractal_zoom_engine.py', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('function onCountryDropdownChange')
if idx != -1:
    print('JS FUNCTION onCountryDropdownChange:')
    print(text[idx:idx+1500])
else:
    print('function onCountryDropdownChange NOT FOUND')

