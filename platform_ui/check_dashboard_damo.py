with open(r'F:\documents\SOIC\EconAgent_Platform\platform_ui\EconAgent_Dashboard.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('GLOBAL_DAMODARAN_SECTORS')
if idx != -1:
    print('FOUND GLOBAL_DAMODARAN_SECTORS in EconAgent_Dashboard.html:')
    print(text[idx-50:idx+600])
else:
    print('NOT FOUND in EconAgent_Dashboard.html')

