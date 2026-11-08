import json, os

src_path = r'F:\documents\SOIC\EconAgent_Platform\platform_ui\gods-eye-view-main\gods-eye-view-main\src\data\local_data\telegeography_submarine_cables\cable-geo.json'
out_path = r'F:\documents\SOIC\EconAgent_Platform\platform_ui\submarine_cables_payload.py'

with open(src_path, 'r', encoding='utf-8') as f:
    cables = json.load(f)

compact_cables = []
for f in cables['features']:
    props = f['properties']
    geom = f['geometry']
    coords = geom['coordinates']
    lines = []
    for line in coords:
        pts = [[round(pt[1], 3), round(pt[0], 3)] for pt in line]
        if len(pts) >= 2:
            lines.append(pts)
    if lines:
        compact_cables.append({
            'id': props.get('id', ''),
            'name': props.get('name', 'Submarine Cable'),
            'color': props.get('color', '#00e5ff'),
            'lines': lines
        })

print(f'Total compact cables processed: {len(compact_cables)}')
with open(out_path, 'w', encoding='utf-8') as f:
    f.write('# TeleGeography Submarine Undersea Fiber-Optic Cables Dataset\n')
    f.write('# Sourced from gods-eye-view (Bilawal Sidhu)\n')
    f.write('SUBMARINE_CABLES_PAYLOAD = ' + json.dumps(compact_cables) + '\n')

print(f'Generated {out_path} ({os.path.getsize(out_path)} bytes)')

