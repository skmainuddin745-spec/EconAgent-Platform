with open(r'F:\documents\SOIC\EconAgent_Platform\platform_ui\generate_dashboard.py', 'r', encoding='utf-8') as f:
    code = f.read()

target = """// Initialize dropdowns on page load
document.addEventListener('DOMContentLoaded', function() {{
  populateGlobalDropdowns('in', 'Electrical Equipment');
}});"""

replacement = """// Initialize dropdowns immediately and on DOMContentLoaded
populateGlobalDropdowns('in', 'Electrical Equipment');
if (document.readyState === 'loading') {{
  document.addEventListener('DOMContentLoaded', function() {{
    populateGlobalDropdowns('in', 'Electrical Equipment');
  }});
}}"""

assert target in code, "target not found in generate_dashboard.py"
code = code.replace(target, replacement)

with open(r'F:\documents\SOIC\EconAgent_Platform\platform_ui\generate_dashboard.py', 'w', encoding='utf-8') as f:
    f.write(code)

print("generate_dashboard.py updated with immediate populateGlobalDropdowns!")

