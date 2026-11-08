import os

root = r'F:\documents\SOIC\EconAgent_Platform\platform_ui'
target = "bmapNavigateWest"

for fname in os.listdir(root):
    fpath = os.path.join(root, fname)
    if os.path.isfile(fpath) and (fname.endswith('.py') or fname.endswith('.html') or fname.endswith('.js')):
        try:
            with open(fpath, 'r', encoding='utf-8') as f:
                content = f.read()
                if target in content:
                    print(f"FOUND IN: {fname}")
        except Exception:
            pass

