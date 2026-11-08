import re
with open('platform_ui/bmap_js_template.js', 'r', encoding='utf-8') as f:
    text = f.read()

matches = [m.start() for m in re.finditer(r'type === .bank_branch.', text)]
print('Matches count:', len(matches))
for p in matches:
    print('Pos:', p)
    print(text[p-50:p+200])

