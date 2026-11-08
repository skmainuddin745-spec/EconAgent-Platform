with open('platform_ui/bmap_js_template.js', 'r', encoding='utf-8') as f:
    text = f.read()

old_fn = "window.checkGodsEyeServerStatus = function(forceReload) {\n    var iframe = document.getElementById('gev_iframe');\n    var fallback = document.getElementById('gev_fallback_box');\n    var statusPill = document.getElementById('gev_server_status_pill');\n\n    fetch('http://127.0.0.1:4173/?embed=1'"
new_fn = "window.checkGodsEyeServerStatus = function(forceReload) {\n    var iframe = document.getElementById('gev_iframe');\n    var fallback = document.getElementById('gev_fallback_box');\n    var statusPill = document.getElementById('gev_server_status_pill');\n\n    return fetch('http://127.0.0.1:4173/?embed=1'"

if old_fn in text:
    text = text.replace(old_fn, new_fn)
    print("Added return to checkGodsEyeServerStatus in bmap_js_template.js")
    with open('platform_ui/bmap_js_template.js', 'w', encoding='utf-8') as f:
        f.write(text)
else:
    print("Warning: old_fn not found")

