# F:\documents\SOIC\EconAgent_Platform\platform_ui\make_compact_branches.py
import json

with open('F:/documents/SOIC/EconAgent_Platform/platform_ui/us_bank_branches_data.json', 'r', encoding='utf-8') as f:
    branches = json.load(f)

banks = sorted(list(set(b['name'] for b in branches)))
states = sorted(list(set(b['state'] for b in branches)))
b_types = sorted(list(set(b['type'] for b in branches)))

compact = []
for b in branches:
    b_idx = banks.index(b['name'])
    s_idx = states.index(b['state'])
    t_idx = b_types.index(b['type'])
    compact.append([
        int(b['id'].replace('bb_', '')),
        b_idx,
        b['lat'],
        b['lon'],
        b['dep'],
        s_idx,
        t_idx
    ])

print(f"Total compact branches: {len(compact)}")
json_str = json.dumps(compact)
print(f"JSON compact string length: {len(json_str)} bytes")

with open('F:/documents/SOIC/EconAgent_Platform/platform_ui/compact_branches_payload.py', 'w', encoding='utf-8') as f:
    f.write(f"BANKS_LIST = {json.dumps(banks)}\n")
    f.write(f"STATES_LIST = {json.dumps(states)}\n")
    f.write(f"TYPES_LIST = {json.dumps(b_types)}\n")
    f.write(f"BRANCHES_COMPACT = {json_str}\n")

print("Saved compact branches payload.")

