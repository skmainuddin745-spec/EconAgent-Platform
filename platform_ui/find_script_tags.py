with open(r'F:\documents\SOIC\EconAgent_Platform\platform_ui\EconAgent_Dashboard.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i in range(22908, 0, -1):
    if '<script' in lines[i]:
        print(f"Nearest <script> above was on line {i+1}: {lines[i]}")
        break

for i in range(22908, len(lines)):
    if '</script>' in lines[i]:
        print(f"Nearest </script> below is on line {i+1}: {lines[i]}")
        break

