with open('F:/documents/SOIC/EconAgent_Platform/platform_ui/fractal_zoom_engine.py', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find('technicalSOIC: {')
print(text[pos:pos+1500])

