with open('platform_ui/bmap_tanker_component.py', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('filterBankBranches = function')
print(text[idx+700:idx+1500])
