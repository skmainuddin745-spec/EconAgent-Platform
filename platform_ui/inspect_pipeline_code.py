with open('F:/documents/SOIC/EconAgent_Platform/platform_ui/bmap_tanker_component.py', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('L.polyline(pipe.coords')
if idx != -1:
    print('=== PIPELINE CODE ===')
    print(text[idx-50:idx+600])

idx2 = text.find('L.polyline(gpipe.coords')
if idx2 != -1:
    print('=== GPIPELINE CODE ===')
    print(text[idx2-50:idx2+600])

