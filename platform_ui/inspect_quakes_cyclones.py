with open(r'F:\documents\SOIC\EconAgent_Platform\platform_ui\bmap_js_template.js', 'r', encoding='utf-8') as f:
    code = f.read()

pos1 = code.find('globalEarthquakes')
pos2 = code.find('globalCyclones')
print('globalEarthquakes pos:', pos1)
if pos1 != -1:
    print(code[pos1-50:pos1+500])

print('\nglobalCyclones pos:', pos2)
if pos2 != -1:
    print(code[pos2-50:pos2+500])

