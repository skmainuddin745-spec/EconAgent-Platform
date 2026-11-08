with open(r'F:\documents\SOIC\EconAgent_Platform\platform_ui\EconAgent_Dashboard.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('id="global_country_select"')
print(repr(text[idx:idx+500]))

