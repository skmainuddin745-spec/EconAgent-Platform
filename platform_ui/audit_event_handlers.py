# audit_event_handlers.py
import re
import os

filepath = r"F:\documents\SOIC\EconAgent_Platform\platform_ui\Bloomberg_BMAP_Terminal.html"
with open(filepath, "r", encoding="utf-8") as f:
    html = f.read()

calls = set(re.findall(r'on(?:click|change|input|keyup)="([^"]+)"', html, re.I))
all_fns = set()
for c in calls:
    for m in re.finditer(r'([a-zA-Z0-9_$]+)\s*\(', c):
        all_fns.add(m.group(1))

ignore = {'alert', 'document', 'prompt', 'confirm', 'getElementById', 'focus'}
missing = []
for fn in sorted(all_fns):
    if fn in ignore:
        continue
    patterns = [
        f'function {fn}',
        f'window.{fn} =',
        f'window.{fn}=',
        f'{fn} = function',
        f'{fn}=function',
        f'var {fn} ='
    ]
    if not any(p in html for p in patterns):
        missing.append(fn)

print(f"Total HTML event functions checked: {len(all_fns)}")
print(f"Missing functions: {missing}")

