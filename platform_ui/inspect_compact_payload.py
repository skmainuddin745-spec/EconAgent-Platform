with open(r'F:\documents\SOIC\EconAgent_Platform\platform_ui\compact_branches_payload.py', 'r', encoding='utf-8') as f:
    code = f.read()

print('Length of compact_branches_payload.py:', len(code))
print(code[:600])

from compact_branches_payload import BRANCHES_COMPACT
print('Total branches in BRANCHES_COMPACT:', len(BRANCHES_COMPACT))
dep_values = [b[2] for b in BRANCHES_COMPACT]
print(f'Min b[2]: {min(dep_values)}, Max b[2]: {max(dep_values)}')
print(f'Max deposit in M ($): {max(dep_values)/1000} M')

