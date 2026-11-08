with open(r'F:\documents\SOIC\EconAgent_Platform\platform_ui\bmap_js_template.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i in range(644, 728):
    if i < len(lines):
        print(f'{i+1}: {lines[i]}', end='')

