import json, os

p = r'F:\documents\SOIC\EconAgent_Platform\platform_ui\gods-eye-view-main\gods-eye-view-main\src\data\local_data\telegeography_submarine_cables\cable-geo.json'
with open(p, 'r', encoding='utf-8') as f:
    cables = json.load(f)

compact_cables = []
for f in cables['features']:
    props = f['properties']
    geom = f['geometry']
    coords = geom['coordinates']
    # coords is list of lines, each line is list of [lon, lat]
    lines = []
    for line in coords:
        # round lat, lon to 3 decimals
        pts = [[round(pt[1], 3), round(pt[0], 3)] for pt in line]
        lines.append(pts)
    compact_cables.append({
        'id': props.get('id', ''),
        'name': props.get('name', ''),
        'color': props.get('color', '#38bdf8'),
        'lines': lines
    })

out_json = json.dumps(compact_cables)
print(f'Compact cables count: {len(compact_cables)}')
print(f'JSON string length: {len(out_json)} bytes')

