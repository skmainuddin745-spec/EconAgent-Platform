with open('F:/documents/SOIC/EconAgent_Platform/platform_ui/generate_dashboard.py', 'r', encoding='utf-8') as f:
    code = f.read()

target = """    # Find surrogates before writing
    surrogates = [(i, c, hex(ord(c))) for i, c in enumerate(html) if 0xD800 <= ord(c) <= 0xDFFF]
    print(f"DEBUG: Found {len(surrogates)} lone surrogates in html!")
    for idx, c, h in surrogates[:5]:
        print(f"  idx {idx}, hex {h}, context: {repr(html[max(0, idx-40):idx+40])}")
    # Sanitize lone surrogates
    clean_html = html.encode('utf-8', errors='replace').decode('utf-8')
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(clean_html)"""

replacement = """    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)"""

if target in code:
    code = code.replace(target, replacement)
    with open('F:/documents/SOIC/EconAgent_Platform/platform_ui/generate_dashboard.py', 'w', encoding='utf-8') as f:
        f.write(code)
    print("Restored standard clean open in generate_dashboard.py")
else:
    print("Target not found")

