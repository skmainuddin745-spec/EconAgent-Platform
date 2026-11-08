with open(r'F:\documents\SOIC\EconAgent_Platform\platform_ui\generate_dashboard.py', 'r', encoding='utf-8') as f:
    text = f.read()

idx1 = text.find('build_institutional_giants_section')
idx2 = text.find('build_soic_sector_models_section')
idx3 = text.find('build_top_notch_framework_section')

print('CALLS IN generate_dashboard.py:')
print('titans call:', repr(text[idx1-20:idx1+80]))
print('soic_sectors call:', repr(text[idx2-20:idx2+80]))
print('topnotch call:', repr(text[idx3-20:idx3+80]))

