with open('platform_ui/EconAgent_Dashboard.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('id="titans"')
print('id="titans" found at:', idx)
if idx != -1:
    print(text[idx-50:idx+800])
else:
    print('NOT FOUND!')
