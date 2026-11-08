with open('F:/documents/SOIC/EconAgent_Platform/platform_ui/institutional_giants_engine.py', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find('window.switchTitanTab')
print(text[pos-100:pos+800])
