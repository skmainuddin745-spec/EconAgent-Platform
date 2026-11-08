from bs4 import BeautifulSoup

with open(r'F:\documents\SOIC\EconAgent_Platform\platform_ui\EconAgent_Dashboard.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')
scripts = soup.find_all('script')

s19 = scripts[18].string or scripts[18].text
lines = s19.splitlines()
print('First 60 lines of Script 19:')
for i, l in enumerate(lines[:60]):
    print(f"{i+1:3d}: {l}")

