with open(r'F:\documents\SOIC\EconAgent_Platform\platform_ui\bmap_js_template.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()

print('Total lines in bmap_js_template.js:', len(lines))
# Let's find large lines or data arrays
for i, line in enumerate(lines):
    if len(line) > 1000 or line.strip().startswith('var ') or line.strip().startswith('const ') or line.strip().startswith('function '):
        if len(line) > 1000:
            print(f'Line {i+1} (length {len(line)}): {line[:80]}...')
        elif any(k in line for k in ['Pipelines', 'Vessels', 'Grid', 'Equity', 'Points', 'Branches', 'Init', 'popup', 'card', 'slider']):
            print(f'Line {i+1}: {line.strip()[:100]}')

