with open('F:/documents/SOIC/EconAgent_Platform/platform_ui/bmap_tanker_component.py', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('Diameter / Length')
if idx != -1:
    print('=== NEXT 800 CHARS ===')
    print(text[idx:idx+800])

