with open('platform_ui/bmap_js_template.js', 'r', encoding='utf-8') as f:
    text = f.read()

pos = 723908 + 2200
print(text[pos:pos+2500])
