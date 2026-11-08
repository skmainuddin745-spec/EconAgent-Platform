with open(r'F:\documents\SOIC\EconAgent_Platform\platform_ui\generate_dashboard.py', 'r', encoding='utf-8') as f:
    text = f.read()

s1 = text.find('// 5. Financial Titans Level 2 DOM Order Book sync')
print(text[s1:s1+1200])

