with open(r'F:\documents\SOIC\EconAgent_Platform\platform_ui\bmap_js_template.js', 'r', encoding='utf-8') as f:
    code = f.read()

pos = code.find('LNG Berths')
print('LNG Berths pos:', pos)
if pos != -1:
    print(code[pos-200:pos+1500])

