with open('F:/documents/SOIC/EconAgent_Platform/platform_ui/EconAgent_Dashboard.html', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find('txt_resistance_status')
print(text[pos-400:pos+300])

