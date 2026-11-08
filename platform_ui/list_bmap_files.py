import os

for f in os.listdir(r'F:\documents\SOIC\EconAgent_Platform\platform_ui'):
    if 'bmap' in f.lower() or 'terminal' in f.lower():
        print(f)

