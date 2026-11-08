with open(r'F:\documents\SOIC\EconAgent_Platform\platform_ui\bmap_html_template.html', 'r', encoding='utf-8') as f:
    code = f.read()

print('Length of bmap_html_template.html:', len(code))
pos = code.find('bmap_universal_vessel_popup')
print('bmap_universal_vessel_popup pos:', pos)
if pos != -1:
    print(code[pos-100:pos+1500])

pos2 = code.find('Map Content')
print('Map Content pos:', pos2)
if pos2 != -1:
    print(code[pos2-50:pos2+800])

