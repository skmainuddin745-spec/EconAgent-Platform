with open('platform_ui/institutional_giants_component.py', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('switchTitanTab')
print(text[idx-50:idx+1500])

