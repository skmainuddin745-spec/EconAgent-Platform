import json

p = r'F:\documents\SOIC\EconAgent_Platform\platform_ui\global_top_companies_curated.json'
with open(p, 'r', encoding='utf-8') as f:
    comps = json.load(f)

print(f"Total curated companies: {len(comps)}")
print("Sample company:", json.dumps(comps[0], indent=2))

# Count by country
by_country = {}
for c in comps:
    co = c.get('country', 'Unknown')
    by_country[co] = by_country.get(co, 0) + 1

print("By country:", by_country)

