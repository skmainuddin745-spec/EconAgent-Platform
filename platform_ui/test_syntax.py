import re
import subprocess
import tempfile

def check_html(filepath, name):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
    scripts = re.findall(r'<script>(.*?)</script>', html, re.DOTALL)
    print(f"[{name}] Checking {len(scripts)} inline script(s)...")
    has_err = False
    for i, s in enumerate(scripts):
        with tempfile.NamedTemporaryFile('w', suffix='.js', delete=False, encoding='utf-8') as tf:
            tf.write(s)
            tname = tf.name
        res = subprocess.run(['node', '--check', tname], capture_output=True, text=True)
        if res.returncode != 0:
            print(f"  Script {i} ERROR:\n{res.stderr}")
            has_err = True
        else:
            print(f"  Script {i} PASSED.")
    return not has_err

ok1 = check_html(r'F:\documents\SOIC\EconAgent_Platform\platform_ui\Bloomberg_BMAP_Terminal.html', 'Standalone BMAP')
ok2 = check_html(r'F:\documents\SOIC\EconAgent_Platform\platform_ui\EconAgent_Dashboard.html', 'Master Dashboard')

if ok1 and ok2:
    print("ALL inline scripts in both HTML files passed syntax check with 0 errors!")
else:
    print("Syntax verification failed.")

