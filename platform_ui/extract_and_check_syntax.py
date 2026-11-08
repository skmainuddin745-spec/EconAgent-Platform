from bs4 import BeautifulSoup
import subprocess
import os

with open(r'F:\documents\SOIC\EconAgent_Platform\platform_ui\EconAgent_Dashboard.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')
scripts = soup.find_all('script')

print(f"Total script tags in EconAgent_Dashboard.html: {len(scripts)}")
for i, s in enumerate(scripts):
    src = s.get('src')
    if src:
        print(f"Script {i+1}: External -> {src}")
    else:
        content = s.string or s.text
        tmp_file = f"platform_ui/temp_check_script_{i+1}.js"
        with open(tmp_file, 'w', encoding='utf-8') as tf:
            tf.write(content)
        res = subprocess.run(['node', '-c', tmp_file], capture_output=True, text=True)
        if res.returncode == 0:
            print(f"Script {i+1}: OK ({len(content)} chars)")
        else:
            print(f"Script {i+1}: SYNTAX ERROR!\n{res.stderr}")
        if os.path.exists(tmp_file):
            os.remove(tmp_file)

