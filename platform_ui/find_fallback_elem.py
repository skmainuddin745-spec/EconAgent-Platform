import glob

for f in glob.glob('platform_ui/*.html') + glob.glob('platform_ui/*.py') + glob.glob('platform_ui/*.js'):
    with open(f, 'r', encoding='utf-8', errors='ignore') as fp:
        for i, line in enumerate(fp):
            if 'gev_fallback_box' in line and ('id=' in line or '<div' in line):
                print(f"{f}:{i} {line.strip()[:100]}")

