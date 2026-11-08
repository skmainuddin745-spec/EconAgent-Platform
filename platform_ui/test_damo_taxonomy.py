import json

# Check damodaran_94_global_industries.json
with open(r'F:\documents\SOIC\EconAgent_Platform\platform_ui\damodaran_94_global_industries.json', 'r', encoding='utf-8') as f:
    damo = json.load(f)

print(f"Loaded {len(damo)} Damodaran industries.")
sectors = sorted(list(set(d['sector'] for d in damo)))
print("GICS Sectors:", sectors)

# Sample map by sector
by_sector = {}
for d in damo:
    sec = d['sector']
    if sec not in by_sector:
        by_sector[sec] = []
    by_sector[sec].append(d['name'])

for sec, inds in by_sector.items():
    print(f"  {sec} ({len(inds)} industries): {inds[:3]}...")

