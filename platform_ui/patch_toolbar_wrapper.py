with open(r'F:\documents\SOIC\EconAgent_Platform\platform_ui\bmap_html_template.html', 'r', encoding='utf-8') as f:
    text = f.read()

part1 = '<!-- Navigation & Security Select Sub-bar -->'
part2 = '<!-- ═══════════════════════════════════════════════════════════════ -->\n<!-- ── PRIMARY VIEW 1: INTERACTIVE MAP & DOCKED BLOOMBERG SIDEBAR ── -->'

idx1 = text.find(part1)
idx2 = text.find(part2)

print('idx1:', idx1)
print('idx2:', idx2)

new_text = text[:idx1] + '<div id="bmap_2d_secondary_toolbar">\n' + text[idx1:idx2] + '</div>\n\n' + text[idx2:]

with open(r'F:\documents\SOIC\EconAgent_Platform\platform_ui\bmap_html_template.html', 'w', encoding='utf-8') as f:
    f.write(new_text)

print('Updated bmap_html_template.html successfully!')

