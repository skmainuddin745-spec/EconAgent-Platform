from bs4 import BeautifulSoup

with open(r'F:\documents\SOIC\EconAgent_Platform\platform_ui\EconAgent_Dashboard.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')
scripts = soup.find_all('script')

for i, s in enumerate(scripts):
    c = s.string or s.text or ''
    if 'populateGlobalDropdowns' in c:
        print(f"Script {i+1} contains populateGlobalDropdowns! Length: {len(c)}")

