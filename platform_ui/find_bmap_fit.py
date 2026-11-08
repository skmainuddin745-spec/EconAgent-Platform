import os

for f in os.listdir('platform_ui'):
    if f.endswith(('.js', '.py', '.html')):
        p = os.path.join('platform_ui', f)
        try:
            with open(p, 'r', encoding='utf-8', errors='ignore') as fp:
                c = fp.read()
                if 'bmapFitBounds' in c:
                    print(f"File {p} has bmapFitBounds (count: {c.count('bmapFitBounds')})")
        except:
            pass

