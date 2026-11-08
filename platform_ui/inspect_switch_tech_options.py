with open(r'F:\documents\SOIC\EconAgent_Platform\platform_ui\realtime_technicals_component.py', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('<option value="XOM">')
print(text[idx:idx+1000])

