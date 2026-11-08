with open('platform_ui/bmap_js_template.js', 'r', encoding='utf-8') as f:
    text = f.read()

print('=== POS 708100-708400 ===')
print(text[708100:708400])

print('=== POS 717500-718600 ===')
print(text[717500:718600])

