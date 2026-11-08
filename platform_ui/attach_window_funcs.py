with open(r'F:\documents\SOIC\EconAgent_Platform\platform_ui\generate_dashboard.py', 'r', encoding='utf-8') as f:
    code = f.read()

# Make all synchronization functions explicitly attached to window
replacements = [
    ("function populateGlobalDropdowns(countryKey, sectorKey) {{", "window.populateGlobalDropdowns = function(countryKey, sectorKey) {{"),
    ("function populateCompaniesForCountryAndSector(countryKey, selectedSector) {{", "window.populateCompaniesForCountryAndSector = function(countryKey, selectedSector) {{"),
    ("function updateNanoAsset(firmObj) {{", "window.updateNanoAsset = function(firmObj) {{"),
    ("function syncGlobalCountryChange(countryKey) {{", "window.syncGlobalCountryChange = function(countryKey) {{"),
    ("function syncGlobalSectorChange(sectorKey) {{", "window.syncGlobalSectorChange = function(sectorKey) {{"),
    ("function syncGlobalFirmChange(firmKey) {{", "window.syncGlobalFirmChange = function(firmKey) {{"),
    ("function syncGlobalNanoChange(nanoKey) {{", "window.syncGlobalNanoChange = function(nanoKey) {{")
]

for old, new in replacements:
    assert old in code, f"Could not find {old}"
    code = code.replace(old, new)

with open(r'F:\documents\SOIC\EconAgent_Platform\platform_ui\generate_dashboard.py', 'w', encoding='utf-8') as f:
    f.write(code)

print("generate_dashboard.py updated with explicit window.* assignments!")

