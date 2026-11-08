with open('F:/documents/SOIC/EconAgent_Platform/platform_ui/EconAgent_Dashboard.html', 'r', encoding='utf-8') as f:
    html = f.read()

from bs4 import BeautifulSoup

soup = BeautifulSoup(html, 'html.parser')

tabs = ['zoom', 'bmap', 'technicals', 'predictor', 'scen', 'soic', 'rot', 'vol', 'flows', 'titans', 'soic_sectors', 'topnotch', 'macro', 'beta', 'margins', 'multiples', 'growth', 'capstruct', 'workcap', 'taxrate', 'fundamentals', 'agents', 'papers', 'arch']

print('--- CHECKING TAB NESTING & PARENTS ---')
for t in tabs:
    el = soup.find(id=t)
    if not el:
        print(f'CRITICAL: Element #{t} NOT FOUND!')
    else:
        parent_tag = el.parent.name if el.parent else 'None'
        parent_id = el.parent.get('id', 'no-id') if el.parent else ''
        parent_class = el.parent.get('class', []) if el.parent else []
        depth = len(list(el.parents))
        children = len(el.find_all(recursive=False))
        print(f'#{t:15} | Parent: <{parent_tag} id="{parent_id}" class="{" ".join(parent_class)}"> | Depth: {depth} | Direct children: {children}')

