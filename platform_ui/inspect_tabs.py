with open('platform_ui/EconAgent_Dashboard.html', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

pos = 2836383
print(text[pos-400:pos+300])
