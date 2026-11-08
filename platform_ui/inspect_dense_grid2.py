with open('F:/documents/SOIC/EconAgent_Platform/platform_ui/bmap_tanker_component.py', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('globalDenseGrid.forEach')
if idx != -1:
    print('After globalDenseGrid:')
    print(text[idx+400:idx+1000])

