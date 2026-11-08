with open('F:/documents/SOIC/EconAgent_Platform/platform_ui/bmap_tanker_component.py', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('crudePipelines.forEach')
if idx != -1:
    print('Crude Pipelines full block:')
    print(text[idx:idx+1200])

