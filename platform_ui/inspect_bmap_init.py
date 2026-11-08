with open(r'F:\documents\SOIC\EconAgent_Platform\platform_ui\bmap_tanker_component.py', 'r', encoding='utf-8') as f:
    code = f.read()

# Let's find 'initLeafletBmap'
pos = code.find('function initLeafletBmap()')
if pos != -1:
    print('initLeafletBmap found!')
    snippet = code[pos:pos+15000]
    print(snippet[:3000])
else:
    print('initLeafletBmap not found, looking for initMap or Leaflet setup...')
    pos2 = code.find('L.map(')
    if pos2 != -1:
        print(code[pos2-200:pos2+2000])

