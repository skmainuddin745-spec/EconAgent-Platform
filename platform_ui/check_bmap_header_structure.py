with open(r'F:\documents\SOIC\EconAgent_Platform\platform_ui\bmap_html_template.html', 'r', encoding='utf-8') as f:
    html = f.read()

start = html.find('id="bmap_main_container"')
end = html.find('id="bmap_view_container_gev"')

print('SECTION BETWEEN BMAP_MAIN_CONTAINER AND BMAP_VIEW_CONTAINER_GEV:')
print(html[start:end])

