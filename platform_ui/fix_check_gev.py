with open('platform_ui/bmap_js_template.js', 'r', encoding='utf-8') as f:
    text = f.read()

old_check = "if (!iframe.src || iframe.src === 'about:blank' || forceReload) {"
new_check = "if (!iframe.src || iframe.src.indexOf('4173') === -1 || forceReload) {"

if old_check in text:
    text = text.replace(old_check, new_check)
    print("Updated iframe.src check in bmap_js_template.js")
    with open('platform_ui/bmap_js_template.js', 'w', encoding='utf-8') as f:
        f.write(text)
else:
    print("Warning: old_check not found")

