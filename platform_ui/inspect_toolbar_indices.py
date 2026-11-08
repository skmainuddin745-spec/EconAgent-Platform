with open(r'F:\documents\SOIC\EconAgent_Platform\platform_ui\bmap_html_template.html', 'r', encoding='utf-8') as f:
    text = f.read()

line47_idx = text.find('<!-- Navigation & Security Select Sub-bar -->')
line116_idx = text.find('<!-- ── PRIMARY VIEW 1: INTERACTIVE MAP & DOCKED BLOOMBERG SIDEBAR ── -->')

print('line47_idx:', line47_idx)
print('line116_idx:', line116_idx)
print('Length of toolbar section:', line116_idx - line47_idx)
print('Section start:\n', text[line47_idx:line47_idx+200])
print('Section end:\n', text[line116_idx-200:line116_idx])

