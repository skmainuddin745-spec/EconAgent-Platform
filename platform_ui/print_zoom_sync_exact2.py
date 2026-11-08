with open(r'F:\documents\SOIC\EconAgent_Platform\platform_ui\fractal_zoom_engine.py', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('function syncGlobalRibbon()')
print(repr(text[idx:idx+1800]))

