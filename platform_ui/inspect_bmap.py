import re

with open(r'F:\documents\SOIC\EconAgent_Platform\platform_ui\bmap_tanker_component.py', 'r', encoding='utf-8') as f:
    code = f.read()

print('Length of code:', len(code))
keywords = ['selectVessel', 'crudePipelines', 'gasPipelines', 'globalDenseGrid', 'worldEquityData', 'addPointsLayer', 'bmap_vessel_card', "on('click", 'on("click', 'bindTooltip', 'bindPopup']
for kw in keywords:
    matches = [m.start() for m in re.finditer(re.escape(kw), code)]
    print(f'{kw}: {len(matches)} occurrences')

# Let's inspect where selectVessel is defined and how bmap_vessel_card is used
pos = code.find('selectVessel')
if pos != -1:
    print('\n--- selectVessel definition snippet ---')
    print(code[pos:pos+1500])

# Let's inspect where crudePipelines is handled
pos2 = code.find('crudePipelines')
if pos2 != -1:
    print('\n--- crudePipelines snippet ---')
    print(code[pos2:pos2+1500])

# Let's inspect where globalDenseGrid is handled
pos3 = code.find('globalDenseGrid')
if pos3 != -1:
    print('\n--- globalDenseGrid snippet ---')
    print(code[pos3:pos3+1500])

# Let's inspect where worldEquityData is handled
pos4 = code.find('worldEquityData')
if pos4 != -1:
    print('\n--- worldEquityData snippet ---')
    print(code[pos4:pos4+1500])

