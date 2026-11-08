with open(r'F:\documents\SOIC\EconAgent_Platform\platform_ui\EconAgent_Dashboard.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if 'populateGlobalDropdowns' in line:
        print(f"Found on line {i+1}:")
        start = max(0, i - 15)
        end = min(len(lines), i + 20)
        for j in range(start, end):
            print(f"{j+1:5d}: {lines[j]}", end='')
        break

