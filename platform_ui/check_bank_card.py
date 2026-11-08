with open('platform_ui/bmap_js_template.js', 'r', encoding='utf-8') as f:
    text = f.read()

pos = 683925
print(text[pos:pos+2500])
