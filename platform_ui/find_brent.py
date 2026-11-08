with open('F:/documents/SOIC/EconAgent_Platform/platform_ui/realtime_technicals_component.py', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find('BRENT:')
print(text[pos:pos+400])

