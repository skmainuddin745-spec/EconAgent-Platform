with open('F:/documents/SOIC/EconAgent_Platform/platform_ui/bmap_tanker_component.py', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('function renderBankBranchesOnMap')
if idx != -1:
    print('renderBankBranchesOnMap:')
    print(text[idx:idx+1000])

