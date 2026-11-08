with open(r'F:\documents\SOIC\EconAgent_Platform\platform_ui\bmap_tanker_component.py', 'r', encoding='utf-8') as f:
    code = f.read()

pos = code.find('bmap_universal_vessel_popup')
print(code[pos-200:pos+2000])

