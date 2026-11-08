with open(r'F:\documents\SOIC\EconAgent_Platform\platform_ui\generate_dashboard.py', 'r', encoding='utf-8') as f:
    code = f.read()

target = """  var targetSoic = soicMap[norm] || 'Polycab India Ltd';
  if (typeof window.loadSoicStock === 'function') {{
    window.loadSoicStock(targetSoic);
  }}"""

replacement = """  try {{
    var targetSoic = soicMap[norm] || 'Polycab India Ltd';
    if (typeof window.loadSoicStock === 'function') {{
      window.loadSoicStock(targetSoic);
    }}
  }} catch (e) {{}}"""

assert target in code, "target not found in generate_dashboard.py"
code = code.replace(target, replacement)

with open(r'F:\documents\SOIC\EconAgent_Platform\platform_ui\generate_dashboard.py', 'w', encoding='utf-8') as f:
    f.write(code)

print("generate_dashboard.py patched with safe try-catch for SOIC stock load!")
