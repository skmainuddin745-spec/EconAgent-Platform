import json, os

p = r'F:\documents\SOIC\EconAgent_Platform\platform_ui\gods-eye-view-main\gods-eye-view-main\src\data\local_data\telegeography_submarine_cables\cable-geo.json'
with open(p, 'r', encoding='utf-8') as f:
    cables = json.load(f)

# Let's count features and total coordinates
features = cables['features']
print('Total features:', len(features))
total_pts = 0
for f in features:
    coords = f['geometry']['coordinates']
    for line in coords:
        total_pts += len(line)
print('Total points across all cables:', total_pts)

# Sample major cables
major_names = ['SEA-ME-WE', 'AAE-1', 'Falcon', 'FLAG', '2Africa', 'Peace', 'Grace Hopper', 'Dunant', 'TAT', 'Faster', 'Unity', 'Jupiter']
found_major = []
for f in features:
    name = f['properties'].get('name', '')
    if any(m.lower() in name.lower() for m in major_names):
        found_major.append(f)
print(f'Major strategic cables matching filter: {len(found_major)}')

