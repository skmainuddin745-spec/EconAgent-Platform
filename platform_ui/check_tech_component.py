with open(r'F:\documents\SOIC\EconAgent_Platform\platform_ui\realtime_technicals_component.py', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('def build_realtime_technicals_section')
print(text[idx:idx+800])

