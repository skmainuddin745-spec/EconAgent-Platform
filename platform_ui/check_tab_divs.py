import re

with open(r'F:\documents\SOIC\EconAgent_Platform\platform_ui\EconAgent_Dashboard.html', 'r', encoding='utf-8') as f:
    html = f.read()

tabs_to_check = [
    'zoom', 'bmap', 'technicals', 'fundamentals', 'scen', 'soic',
    'rot', 'vol', 'flows', 'titans', 'soic_sectors', 'topnotch'
]

print('CHECKING TAB CONTENT DIVS:')
for t in tabs_to_check:
    # Look for id="t" in html
    pattern = rf'<div[^>]+id=["\']{t}["\'][^>]*>'
    m = re.search(pattern, html)
    if m:
        # get length of content inside this div
        start_idx = m.start()
        print(f"Tab '{t}': FOUND tag: {m.group(0)[:80]}")
    else:
        print(f"Tab '{t}': NOT FOUND!")

