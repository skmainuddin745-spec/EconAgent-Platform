with open('F:/documents/SOIC/EconAgent_Platform/platform_ui/bmap_tanker_component.py', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find("Grid Node ' + item.id")
if idx != -1:
    print('After ttHtml:')
    print(text[idx-50:idx+500])

