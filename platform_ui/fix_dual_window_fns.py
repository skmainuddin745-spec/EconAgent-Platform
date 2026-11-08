with open(r'F:\documents\SOIC\EconAgent_Platform\platform_ui\generate_dashboard.py', 'r', encoding='utf-8') as f:
    code = f.read()

# Replace window.foo = function(...) with function foo(...) and window.foo = foo
replacements = [
    ("window.populateGlobalDropdowns = function(countryKey, sectorKey) {{", "function populateGlobalDropdowns(countryKey, sectorKey) {{\n  window.populateGlobalDropdowns = populateGlobalDropdowns;"),
    ("window.populateCompaniesForCountryAndSector = function(countryKey, selectedSector) {{", "function populateCompaniesForCountryAndSector(countryKey, selectedSector) {{\n  window.populateCompaniesForCountryAndSector = populateCompaniesForCountryAndSector;"),
    ("window.updateNanoAsset = function(firmObj) {{", "function updateNanoAsset(firmObj) {{\n  window.updateNanoAsset = updateNanoAsset;"),
    ("window.syncGlobalCountryChange = function(countryKey) {{", "function syncGlobalCountryChange(countryKey) {{\n  window.syncGlobalCountryChange = syncGlobalCountryChange;"),
    ("window.syncGlobalSectorChange = function(sectorKey) {{", "function syncGlobalSectorChange(sectorKey) {{\n  window.syncGlobalSectorChange = syncGlobalSectorChange;"),
    ("window.syncGlobalFirmChange = function(firmKey) {{", "function syncGlobalFirmChange(firmKey) {{\n  window.syncGlobalFirmChange = syncGlobalFirmChange;"),
    ("window.syncGlobalNanoChange = function(nanoKey) {{", "function syncGlobalNanoChange(nanoKey) {{\n  window.syncGlobalNanoChange = syncGlobalNanoChange;")
]

for old, new in replacements:
    assert old in code, f"Could not find {old}"
    code = code.replace(old, new)

# Also explicitly expose on window at the end of the sync block
expose_block = """
window.populateGlobalDropdowns = populateGlobalDropdowns;
window.populateCompaniesForCountryAndSector = populateCompaniesForCountryAndSector;
window.updateNanoAsset = updateNanoAsset;
window.syncGlobalCountryChange = syncGlobalCountryChange;
window.syncGlobalSectorChange = syncGlobalSectorChange;
window.syncGlobalFirmChange = syncGlobalFirmChange;
window.syncGlobalNanoChange = syncGlobalNanoChange;
"""

target_end = "// Initialize dropdowns immediately and on DOMContentLoaded"
assert target_end in code, "target_end not found"
code = code.replace(target_end, expose_block + "\n" + target_end)

with open(r'F:\documents\SOIC\EconAgent_Platform\platform_ui\generate_dashboard.py', 'w', encoding='utf-8') as f:
    f.write(code)

print("generate_dashboard.py updated with dual function/window pattern!")

