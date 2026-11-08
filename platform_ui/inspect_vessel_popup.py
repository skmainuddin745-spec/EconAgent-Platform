with open(r'F:\documents\SOIC\EconAgent_Platform\platform_ui\bmap_tanker_component.py', 'r', encoding='utf-8') as f:
    code = f.read()

pos = code.find('showUniversalVesselPopup')
if pos != -1:
    print('showUniversalVesselPopup snippet:')
    print(code[pos-100:pos+2000])
else:
    print('Searching vessel card popup...')
    pos2 = code.find('JUBAIL TRADER')
    print('JUBAIL TRADER snippet:', pos2)
    if pos2 != -1:
        print(code[pos2-100:pos2+1000])

