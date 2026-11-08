import json
import os
import sys

BASE_DIR = r"F:\documents\SOIC\EconAgent_Platform\platform_ui"
sys.path.insert(0, BASE_DIR)

from compact_branches_payload import BANKS_LIST, STATES_LIST, TYPES_LIST, BRANCHES_COMPACT
from submarine_cables_payload import SUBMARINE_CABLES_PAYLOAD
from soic_sector_models_component import build_soic_sector_models_section
from global_banking_network import GLOBAL_BANKING_TITANS
from global_pipelines_network import GLOBAL_GAS_PIPELINES, GLOBAL_CRUDE_PIPELINES

# Read HTML template
with open(os.path.join(BASE_DIR, "bmap_html_template.html"), "r", encoding="utf-8") as f:
    html_raw = f.read().rstrip()
    if html_raw.endswith('"""'):
        html_raw = html_raw[:-3].rstrip()

# Read JS template
with open(os.path.join(BASE_DIR, "bmap_js_template.js"), "r", encoding="utf-8") as f:
    js_raw = f.read()

# Inject SOIC Sector Models HTML
soic_html = build_soic_sector_models_section()
html_raw = html_raw.replace('__SOIC_SECTOR_MODELS_HTML__', soic_html)

# Replace placeholders with compact JSON
js_injected = js_raw.replace('__BANKS_JSON__', json.dumps(BANKS_LIST))
js_injected = js_injected.replace('__STATES_JSON__', json.dumps(STATES_LIST))
js_injected = js_injected.replace('__TYPES_JSON__', json.dumps(TYPES_LIST))
js_injected = js_injected.replace('__BRANCHES_JSON__', json.dumps(BRANCHES_COMPACT))
js_injected = js_injected.replace('__SUBMARINE_CABLES_JSON__', json.dumps(SUBMARINE_CABLES_PAYLOAD))
js_injected = js_injected.replace('__GLOBAL_BANKING_JSON__', json.dumps(GLOBAL_BANKING_TITANS))
js_injected = js_injected.replace('__CRUDE_PIPELINES_JSON__', json.dumps(GLOBAL_CRUDE_PIPELINES))
js_injected = js_injected.replace('__GAS_PIPELINES_JSON__', json.dumps(GLOBAL_GAS_PIPELINES))

print(f"HTML size: {len(html_raw)} bytes")
print(f"JS size: {len(js_injected)} bytes")
print(f"Global Banking Titans injected: {len(GLOBAL_BANKING_TITANS)} institutions")
print(f"Global Gas Pipelines injected: {len(GLOBAL_GAS_PIPELINES)} arteries")
print(f"Global Crude Pipelines injected: {len(GLOBAL_CRUDE_PIPELINES)} corridors")

# Write bmap_tanker_component.py cleanly
comp_path = os.path.join(BASE_DIR, "bmap_tanker_component.py")
with open(comp_path, "w", encoding="utf-8") as f:
    f.write('"""\n')
    f.write("EconAgent Platform - Bloomberg BMAP Component (v6.2.0)\n")
    f.write("Global Banking & Financial Institutions Network (Worldwide G-SIBs & 1,675 US FDIC Branches),\n")
    f.write("Global Energy Pipelines Network (Gas & Crude across India, GCC, Europe, Asia, Americas),\n")
    f.write("Dual 3D Cesium Workstation (Native Engine + Bilawal Sidhu Microservice),\n")
    f.write("Concentric Radar Deposit Legend, Parameter Filter Card, Top Ticker Bar,\n")
    f.write("and Map Content Datasets Drawer.\n")
    f.write('"""\n\n')
    
    # Store as raw string representations
    f.write("HTML_PART = " + repr(html_raw) + "\n\n")
    f.write("JS_PART = " + repr(js_injected) + "\n\n")
    f.write("def build_bmap_tanker_section(by_agent=None) -> str:\n")
    f.write('    return HTML_PART + "\\n" + JS_PART\n')

print(f"Generated {comp_path} successfully ({os.path.getsize(comp_path)} bytes)")
