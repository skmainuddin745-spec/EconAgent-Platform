with open(r'F:\documents\SOIC\EconAgent_Platform\platform_ui\bmap_tanker_component.py', 'r', encoding='utf-8') as f:
    code = f.read()

pos = code.find('function showUniversalVesselPopup')
if pos != -1:
    print('Found function showUniversalVesselPopup:')
    print(code[pos:pos+1500])
else:
    print('Searching showUniversalVesselPopup...')
    pos2 = code.find('showUniversalVesselPopup =')
    print('pos2:', pos2)
    if pos2 != -1:
        print(code[pos2:pos2+1000])

