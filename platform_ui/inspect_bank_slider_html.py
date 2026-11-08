with open(r'F:\documents\SOIC\EconAgent_Platform\platform_ui\bmap_tanker_component.py', 'r', encoding='utf-8') as f:
    code = f.read()

pos = code.find('Deposits (M)')
if pos != -1:
    print('Found Deposits (M):')
    print(code[pos-200:pos+1500])
else:
    print('Not found Deposits (M)')

