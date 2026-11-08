with open(r'F:\documents\SOIC\EconAgent_Platform\platform_ui\bmap_js_template.js', 'r', encoding='utf-8') as f:
    code = f.read()

pos = code.find('key === \'natural_gas\'')
if pos == -1:
    pos = code.find('natural_gas')
    print('Searching natural_gas in card renderer...')
    import re
    for m in re.finditer(r'natural_gas', code):
        start = m.start()
        sub = code[start-50:start+300]
        if 'checkbox' in sub or 'input' in sub or 'card' in sub:
            print(f'Match at {start}:')
            print(sub)
            print('='*30)
else:
    print('Found key === natural_gas at', pos)
    print(code[pos-100:pos+1500])

