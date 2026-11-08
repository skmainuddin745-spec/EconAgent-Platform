with open(r'F:\documents\SOIC\EconAgent_Platform\platform_ui\bmap_js_template.js', 'r', encoding='utf-8') as f:
    code = f.read()

pos = code.find('slider_bank_dep')
print('slider_bank_dep in bmap_js_template.js:', pos)
if pos != -1:
    print(code[pos-200:pos+300])

