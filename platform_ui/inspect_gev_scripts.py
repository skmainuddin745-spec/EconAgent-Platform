import json
with open(r'F:\documents\SOIC\EconAgent_Platform\platform_ui\gods-eye-view-main\gods-eye-view-main\package.json', 'r', encoding='utf-8') as f:
    pkg = json.load(f)

print('Scripts in package.json:')
for k, v in pkg.get('scripts', {}).items():
    print(f'  "{k}": "{v}"')

print('\nDependencies:')
for k, v in pkg.get('dependencies', {}).items():
    print(f'  "{k}": "{v}"')

