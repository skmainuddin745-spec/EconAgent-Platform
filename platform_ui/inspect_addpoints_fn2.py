with open('F:/documents/SOIC/EconAgent_Platform/platform_ui/bmap_tanker_component.py', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('function addPointsLayer')
if idx != -1:
    print('addPointsLayer next part:')
    print(text[idx+600:idx+1500])

