with open(r'F:\documents\SOIC\EconAgent_Platform\platform_ui\generate_dashboard.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

print('Lines 3085 to 3110:')
for i in range(3084, min(len(lines), 3110)):
    print(f"{i+1:4d}: {lines[i]}", end='')

