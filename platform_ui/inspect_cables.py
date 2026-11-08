import json, os

p = r'F:\documents\SOIC\EconAgent_Platform\platform_ui\gods-eye-view-main\gods-eye-view-main\src\data\local_data\telegeography_submarine_cables\cable-geo.json'
with open(p, 'r', encoding='utf-8') as f:
    cables = json.load(f)

print('Features:', len(cables['features']))
sample = cables['features'][:5]
for s in sample:
    print('Props:', s['properties']['name'], s['properties'].get('color'), s['geometry']['type'])

