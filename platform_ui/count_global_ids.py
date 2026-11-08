with open(r'F:\documents\SOIC\EconAgent_Platform\platform_ui\EconAgent_Dashboard.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
m1 = re.findall(r'id=["\']global_sector_select["\']', text)
m2 = re.findall(r'id=["\']global_firm_select["\']', text)
m3 = re.findall(r'id=["\']global_country_select["\']', text)

print('Matches for global_sector_select:', len(m1))
print('Matches for global_firm_select:', len(m2))
print('Matches for global_country_select:', len(m3))

