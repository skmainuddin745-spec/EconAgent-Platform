with open(r'F:\documents\SOIC\EconAgent_Platform\platform_ui\bmap_html_template.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines):
    if 'bmap_universal_vessel_popup' in l:
        print(f'Found at line {i+1}:')
        for j in range(max(0, i-5), min(len(lines), i+35)):
            print(f'{j+1}: {lines[j]}', end='')
        break

