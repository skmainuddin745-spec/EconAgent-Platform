import json

p = r'F:\documents\SOIC\EconAgent_Platform\platform_ui\global_top_companies_curated.json'
with open(p, 'r', encoding='utf-8') as f:
    comps = json.load(f)

by_country = {}
for c in comps:
    co = c[3]
    by_country[co] = by_country.get(co, 0) + 1

# top 25 countries
sorted_countries = sorted(by_country.items(), key=lambda x: x[1], reverse=True)
for co, count in sorted_countries[:25]:
    print(f"  {co}: {count} companies")

