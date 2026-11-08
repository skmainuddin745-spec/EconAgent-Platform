with open(r'F:\documents\SOIC\EconAgent_Platform\platform_ui\EconAgent_Dashboard.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i in range(22860, 22915):
    print(f"{i+1:5d}: {lines[i]}", end='')

