with open(r'F:\documents\SOIC\EconAgent_Platform\platform_ui\bmap_html_template.html', 'r', encoding='utf-8') as f:
    code = f.read()

pos = code.find('slider_bank_dep')
print('slider_bank_dep in bmap_html_template.html:', pos)
if pos != -1:
    print(code[pos-100:pos+200])

