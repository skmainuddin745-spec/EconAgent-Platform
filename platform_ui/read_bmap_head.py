with open(r'F:\documents\SOIC\EconAgent_Platform\platform_ui\bmap_html_template.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

print('First 60 lines of bmap_html_template.html:')
for i, line in enumerate(lines[:60]):
    print(f"{i+1:3d}: {line}", end='')

