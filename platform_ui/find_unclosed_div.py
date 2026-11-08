with open('F:/documents/SOIC/EconAgent_Platform/platform_ui/bmap_html_template.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

import re

stack = []
for line_idx, line in enumerate(lines, 1):
    # Find all <div> and </div> in this line
    tokens = re.finditer(r'(<div\b[^>]*>|</div>)', line, re.IGNORECASE)
    for t in tokens:
        tag = t.group(0)
        if tag.startswith('</'):
            if stack:
                stack.pop()
            else:
                print(f"Extra </div> at line {line_idx}: {line.strip()}")
        else:
            # open div
            # Extract id or class or first 40 chars
            snippet = tag[:50]
            stack.append((line_idx, snippet))

print(f"Total unclosed <div>s: {len(stack)}")
for line_idx, snippet in stack:
    print(f"  Line {line_idx}: {snippet}")

