with open(r'F:\documents\SOIC\EconAgent_Platform\platform_ui\fractal_zoom_engine.py', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('onCountryDropdownChange')
if idx != -1:
    print('FOUND onCountryDropdownChange IN fractal_zoom_engine.py:')
    print(text[idx-50:idx+1500])
else:
    print('NOT FOUND in fractal_zoom_engine.py')

