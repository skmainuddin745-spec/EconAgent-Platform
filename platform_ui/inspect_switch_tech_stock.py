with open(r'F:\documents\SOIC\EconAgent_Platform\platform_ui\realtime_technicals_component.py', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('switchTechStock')
if idx != -1:
    print('switchTechStock in realtime_technicals_component.py:')
    print(text[idx:idx+1500])
else:
    print('switchTechStock NOT FOUND')

