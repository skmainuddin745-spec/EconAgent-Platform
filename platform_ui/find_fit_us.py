import os

for f in os.listdir('platform_ui'):
    if f.endswith(('.js', '.py', '.html')):
        p = os.path.join('platform_ui', f)
        try:
            with open(p, 'r', encoding='utf-8', errors='ignore') as fp:
                c = fp.read()
                if 'Fit US' in c or 'fit us' in c.lower() or 'Bank Branches' in c:
                    print(f"File: {p} has match (Fit US: {'Fit US' in c}, Bank Branches: {'Bank Branches' in c})")
        except:
            pass

