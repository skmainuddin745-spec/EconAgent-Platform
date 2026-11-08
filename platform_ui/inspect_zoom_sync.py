with open(r'F:\documents\SOIC\EconAgent_Platform\platform_ui\fractal_zoom_engine.py', 'r', encoding='utf-8') as f:
    text = f.read()

idx1 = text.find('syncGlobalRibbon')
print('syncGlobalRibbon in fractal_zoom_engine.py:')
print(text[idx1-200:idx1+1200])

