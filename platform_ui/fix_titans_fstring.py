with open('F:/documents/SOIC/EconAgent_Platform/platform_ui/institutional_giants_engine.py', 'r', encoding='utf-8') as f:
    code = f.read()

# Fix all unescaped ${( in institutional_giants_engine.py
import re
# Find all occurrences of ${...} that don't start with ${{
fixed_code = re.sub(r'\$\{([^{}]+)\}', r'${{\1}}', code)

with open('F:/documents/SOIC/EconAgent_Platform/platform_ui/institutional_giants_engine.py', 'w', encoding='utf-8') as f:
    f.write(fixed_code)

print("Fixed unescaped f-string braces in institutional_giants_engine.py")

