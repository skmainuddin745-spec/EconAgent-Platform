import os, json

root = r'F:\documents\SOIC\EconAgent_Platform\platform_ui'

files_to_check = [
    'global_company_directory.json',
    'damodaran_94_sectors.json',
    'global_firm_definitions.py',
    'build_damodaran_94_dataset.py'
]

for f in files_to_check:
    path = os.path.join(root, f)
    if os.path.exists(path):
        size = os.path.getsize(path)
        print(f"File {f}: {size} bytes")
    else:
        print(f"File {f}: NOT FOUND")

