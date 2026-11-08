with open(r'F:\documents\SOIC\EconAgent_Platform\platform_ui\bmap_html_template.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Find the toolbar sections above container_map
s1 = html.find('Navigation & Security Select Sub-bar')
s2 = html.find('id="bmap_view_container_map"')

print('Toolbar between s1 and s2:\n')
print(html[s1:s1+600])
print('...\n')
print(html[s2-400:s2])

