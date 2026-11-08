with open(r'F:\documents\SOIC\EconAgent_Platform\platform_ui\realtime_technicals_component.py', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('TECH_PRESETS')
if idx != -1:
    print('TECH_PRESETS in realtime_technicals_component.py:')
    print(text[idx:idx+1500])
else:
    print('TECH_PRESETS NOT FOUND')

