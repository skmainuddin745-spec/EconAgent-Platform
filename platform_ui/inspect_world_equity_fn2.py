with open('F:/documents/SOIC/EconAgent_Platform/platform_ui/bmap_tanker_component.py', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('worldEquityData.forEach')
if idx != -1:
    print('After worldEquityData:')
    print(text[idx+400:idx+1200])

