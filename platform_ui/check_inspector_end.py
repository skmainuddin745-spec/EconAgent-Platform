with open('platform_ui/bmap_js_template.js', 'r', encoding='utf-8') as f:
    text = f.read()

pos = 700451 + 15500
print(text[pos:pos+1600])
