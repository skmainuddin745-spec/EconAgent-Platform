import re

with open(r'F:\documents\SOIC\EconAgent_Platform\platform_ui\bmap_tanker_component.py', 'r', encoding='utf-8') as f:
    code = f.read()

pos = code.find('filterBranchesByDeposit')
if pos != -1:
    print('filterBranchesByDeposit snippet:')
    print(code[pos-200:pos+1500])
else:
    print('Searching Branches slider...')
    matches = [m.start() for m in re.finditer(r'deposit', code, re.IGNORECASE)]
    print(f'deposit matches: {len(matches)}')
    for idx in matches[:5]:
        print('--- Match ---')
        print(code[idx-100:idx+300])
