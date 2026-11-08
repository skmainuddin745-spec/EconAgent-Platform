with open(r'F:\documents\SOIC\EconAgent_Platform\platform_ui\generate_dashboard.py', 'r', encoding='utf-8') as f:
    text = f.read()

for var in ['titan_section', 'soic_sector_section', 'topnotch_section', 'technicals_section', 'finflows_section']:
    idx = text.find('{' + var + '}')
    print(f"Placeholder {{{var}}}: {'FOUND at ' + str(idx) if idx != -1 else '*** NOT FOUND ***'}")
    if idx != -1:
        print('  Context:', repr(text[idx-40:idx+60]))

