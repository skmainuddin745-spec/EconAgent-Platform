from bs4 import BeautifulSoup
import subprocess

with open(r'F:\documents\SOIC\EconAgent_Platform\platform_ui\EconAgent_Dashboard.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')
scripts = soup.find_all('script')

s19 = scripts[18].string or scripts[18].text

wrapper = """
global.window = global;
global.document = {
  getElementById: () => ({ options: [], appendChild: () => {}, querySelector: () => null }),
  querySelectorAll: () => [],
  addEventListener: () => {}
};
""" + s19

with open('platform_ui/temp_test_s19.js', 'w', encoding='utf-8') as f:
    f.write(wrapper)

res = subprocess.run(['node', 'platform_ui/temp_test_s19.js'], capture_output=True, text=True)
print("STDOUT:\n", res.stdout)
print("STDERR:\n", res.stderr)

