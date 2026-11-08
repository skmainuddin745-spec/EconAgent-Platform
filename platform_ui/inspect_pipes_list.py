with open(r'F:\documents\SOIC\EconAgent_Platform\platform_ui\bmap_js_template.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()

import json
# let's parse line 11
l11 = lines[10].strip()
if l11.startswith('var crudePipelines = '):
    json_str = l11[len('var crudePipelines = '):-1]
    pipes = json.loads(json_str)
    print(f'Crude pipelines count: {len(pipes)}')
    for p in pipes:
        print(f" - {p['id']}: {p['name']} ({p.get('company')}) coords len: {len(p['coords'])}")

