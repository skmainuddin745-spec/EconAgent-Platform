with open('platform_ui/bmap_js_template.js', 'r', encoding='utf-8') as f:
    text = f.read()

pos = 748000
print(text[pos:pos+1500])
