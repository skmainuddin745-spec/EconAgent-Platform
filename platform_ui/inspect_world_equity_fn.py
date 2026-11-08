import re
with open('F:/documents/SOIC/EconAgent_Platform/platform_ui/bmap_tanker_component.py', 'r', encoding='utf-8') as f:
    text = f.read()

matches = [m.start() for m in re.finditer(r'worldEquityData\.forEach', text)]
for idx in matches:
    print('Usage snippet:')
    print(text[idx-50:idx+800])
