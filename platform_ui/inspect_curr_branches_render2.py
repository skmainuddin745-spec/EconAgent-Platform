with open(r'F:\documents\SOIC\EconAgent_Platform\platform_ui\bmap_js_template.js', 'r', encoding='utf-8') as f:
    js = f.read()

pos = js.find('function renderBankBranchesOnMap(branches)')
pos_end = js.find('function showCompactBranchPopup', pos)
print(js[pos:pos_end])

