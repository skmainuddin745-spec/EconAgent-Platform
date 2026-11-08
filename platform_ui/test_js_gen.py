import json
from global_firm_definitions import GLOBAL_FIRMS
from global_nano_definitions import GLOBAL_NANOS

def dict_to_js(d, indent=4):
    return json.dumps(d, indent=indent)

# Check that json.dumps produces valid JS
js_firms = "var firmData = " + dict_to_js(GLOBAL_FIRMS) + ";\n"
js_nanos = "var nanoData = " + dict_to_js(GLOBAL_NANOS) + ";\n"

print(f"Generated firmData JS: {len(js_firms)} bytes")
print(f"Generated nanoData JS: {len(js_nanos)} bytes")

