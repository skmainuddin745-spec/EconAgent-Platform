with open('platform_ui/generate_dashboard.py', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('function setWorkspaceMode')
print(text[idx-50:idx+2500])

