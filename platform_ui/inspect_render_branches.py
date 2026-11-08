with open(r'F:\documents\SOIC\EconAgent_Platform\platform_ui\bmap_js_template.js', 'r', encoding='utf-8') as f:
    code = f.read()

pos = code.find('function renderBankBranchesOnMap')
print(code[pos:pos+1500])

