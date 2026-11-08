with open('platform_ui/bmap_js_template.js', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('// Generic facility / seaport / refinery / cavern')
print(text[idx-50:idx+1500])

