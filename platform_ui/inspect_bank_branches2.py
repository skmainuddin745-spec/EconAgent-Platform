with open('F:/documents/SOIC/EconAgent_Platform/platform_ui/bmap_tanker_component.py', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('renderBankBranchesOnMap')
if idx != -1:
    print('renderBankBranchesOnMap next part:')
    print(text[idx+800:idx+1600])

