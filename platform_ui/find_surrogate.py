import glob

files = [
    'fractal_zoom_engine.py',
    'realtime_technicals_component.py',
    'institutional_giants_engine.py',
    'generate_dashboard.py',
    'global_firm_definitions.py',
    'global_nano_definitions.py',
    'build_full_sector_data.py'
]

for fname in files:
    path = f'F:/documents/SOIC/EconAgent_Platform/platform_ui/{fname}'
    with open(path, 'r', encoding='utf-8', errors='surrogateescape') as f:
        text = f.read()
    surrogates = [(i, c, hex(ord(c))) for i, c in enumerate(text) if 0xD800 <= ord(c) <= 0xDFFF]
    if surrogates:
        print(f"File {fname} has {len(surrogates)} surrogates:")
        for i, c, h in surrogates[:5]:
            print(f"  pos {i}: {h}")
    else:
        print(f"File {fname}: Clean (0 surrogates)")

