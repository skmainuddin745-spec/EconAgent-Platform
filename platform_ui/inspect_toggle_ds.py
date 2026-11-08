with open(r'F:\documents\SOIC\EconAgent_Platform\platform_ui\bmap_js_template.js', 'r', encoding='utf-8') as f:
    code = f.read()

pos = code.find('function toggleDatasetActive(')
if pos == -1:
    pos = code.find('toggleDatasetActive')
print('toggleDatasetActive pos:', pos)
print(code[pos-50:pos+1500])

