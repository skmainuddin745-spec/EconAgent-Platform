with open('platform_ui/generate_dashboard.py', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('ws-viewport')
print(text[idx-100:idx+2500])

