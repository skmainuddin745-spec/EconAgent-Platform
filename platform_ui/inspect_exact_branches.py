with open(r'F:\documents\SOIC\EconAgent_Platform\platform_ui\bmap_js_template.js', 'r', encoding='utf-8') as f:
    js = f.read()

pos_start = js.find('function renderBankBranchesOnMap(branches) {')
pos_end = js.find('  // Helper to display details for generic infrastructure', pos_start)

print('Start pos:', pos_start, 'End pos:', pos_end)
print(js[pos_start:pos_end])

