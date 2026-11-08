with open(r'F:\documents\SOIC\EconAgent_Platform\platform_ui\bmap_tanker_component.py', 'r', encoding='utf-8') as f:
    code = f.read()

pos = code.find('function initWorldEquityLayer()')
if pos != -1:
    print(code[pos:pos+2500])
