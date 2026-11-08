from bs4 import BeautifulSoup
import re

with open(r'F:\documents\SOIC\EconAgent_Platform\platform_ui\EconAgent_Dashboard.html', 'r', encoding='utf-8') as f:
    html = f.read()

tabs_to_check = ['titans', 'soic_sectors', 'topnotch', 'technicals', 'flows', 'vol', 'rot']

for t in tabs_to_check:
    pattern = rf'<div id="{t}" class="content">(.*?)</div>\s*(?:<!--|<div id=|<footer)'
    m = re.search(pattern, html, re.DOTALL)
    if m:
        content = m.group(1).strip()
        print(f"Tab '{t}' raw length: {len(content)} chars. Starts with: {content[:100]!r}")
    else:
        # Try finding just start
        idx = html.find(f'id="{t}"')
        print(f"Tab '{t}' not matched cleanly by regex. Found id at {idx}. Sample:")
        print(html[idx:idx+300])

