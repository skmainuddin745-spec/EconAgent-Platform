with open('platform_ui/bmap_js_template.js', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('function renderBankBranchesOnMap')
print(text[idx:idx+2500])

