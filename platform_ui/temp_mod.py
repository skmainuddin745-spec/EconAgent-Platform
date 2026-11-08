with open('F:/documents/SOIC/EconAgent_Platform/platform_ui/generate_dashboard.py', 'r', encoding='utf-8') as f:
    code = f.read()

code = code.replace('with open(out_path, "w", encoding="utf-8") as f:', 'with open(out_path, "w", encoding="utf-8", errors="surrogateescape") as f:')

with open('F:/documents/SOIC/EconAgent_Platform/platform_ui/generate_dashboard.py', 'w', encoding='utf-8') as f:
    f.write(code)

print("Updated generate_dashboard.py to use surrogateescape")

