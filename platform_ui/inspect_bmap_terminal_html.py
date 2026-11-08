with open(r'F:\documents\SOIC\EconAgent_Platform\platform_ui\Bloomberg_BMAP_Terminal.html', 'r', encoding='utf-8') as f:
    code = f.read()

print('Length of Bloomberg_BMAP_Terminal.html:', len(code))
print('First 500 chars:')
print(code[:500])

