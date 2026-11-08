import os
import json

curr_dir = r"F:\documents\SOIC\EconAgent_Platform\platform_ui"

# Load Damodaran 94 industries
with open(os.path.join(curr_dir, 'damodaran_94_global_industries.json'), 'r', encoding='utf-8') as f:
    damo_data = json.load(f)

# Build a compact sector-to-industries map
sectors_map = {}
for d in damo_data:
    sec = d['sector']
    if sec not in sectors_map:
        sectors_map[sec] = []
    sectors_map[sec].append({
        'name': d['name'],
        'beta': d['beta'],
        'wacc': d['waccPct'],
        'margin': d['ebitMarginPct']
    })

print(f"Total Sectors: {len(sectors_map)}, Total Industries: {len(damo_data)}")

