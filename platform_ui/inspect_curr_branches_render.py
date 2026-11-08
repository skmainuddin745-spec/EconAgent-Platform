with open(r'F:\documents\SOIC\EconAgent_Platform\platform_ui\bmap_js_template.js', 'r', encoding='utf-8') as f:
    js = f.read()

pos = js.find('function renderBankBranchesOnMap(branches)')
print(js[pos:pos+1500])

