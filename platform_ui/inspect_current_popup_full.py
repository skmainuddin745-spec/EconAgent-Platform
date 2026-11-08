with open(r'F:\documents\SOIC\EconAgent_Platform\platform_ui\bmap_html_template.html', 'r', encoding='utf-8') as f:
    code = f.read()

pos = code.find('bmap_universal_vessel_popup')
end_pos = code.find('<!-- ── AUTHENTIC GREG MORTIMER EXPEDITION VESSEL POPUP', pos)
print(code[pos:end_pos])

