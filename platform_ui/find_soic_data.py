with open('F:/documents/SOIC/EconAgent_Platform/platform_ui/generate_dashboard.py', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find('soicStockData = {')
print(text[pos:pos+1000])

