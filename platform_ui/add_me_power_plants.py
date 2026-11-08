import json

js_path = 'F:/documents/SOIC/EconAgent_Platform/platform_ui/bmap_js_template.js'
with open(js_path, 'r', encoding='utf-8') as f:
    js = f.read()

me_plants = [
    {
        "id": "util_ghazlan",
        "name": "Ghazlan Thermal Power Plant",
        "country": "Saudi Arabia",
        "lat": 26.85,
        "lon": 49.91,
        "type": "Combined-Cycle Gas & Steam",
        "capacity": "4,528 MW (Major SEC Gulf Grid)",
        "operator": "Saudi Electricity Company (SEC)",
        "source": "ECRA Saudi Arabia",
        "status": "Operational / Base-Load"
    },
    {
        "id": "util_qurayyah",
        "name": "Qurayyah IPP Combined Cycle Station",
        "country": "Saudi Arabia",
        "lat": 25.86,
        "lon": 50.13,
        "type": "Gas CCGT High Efficiency",
        "capacity": "3,927 MW (Eastern Province)",
        "operator": "Hajr Electricity / ACWA Power",
        "source": "SEC Telemetry",
        "status": "Operational"
    },
    {
        "id": "util_barakah",
        "name": "Barakah Nuclear Energy Plant",
        "country": "UAE",
        "lat": 23.996,
        "lon": 52.235,
        "type": "Nuclear (4x APR-1400)",
        "capacity": "5,600 MW (Zero-Carbon Baseload)",
        "operator": "ENEC / Nawah Energy",
        "source": "FANR Regulatory Authority",
        "status": "Operational / 100% Commercial"
    },
    {
        "id": "util_jebel_ali",
        "name": "Jebel Ali Power & Desalination Complex",
        "country": "UAE",
        "lat": 25.04,
        "lon": 55.12,
        "type": "Cogeneration Gas & Thermal Desalination",
        "capacity": "9,547 MW · 470 MIGD Water",
        "operator": "DEWA Dubai",
        "source": "DEWA Telemetry",
        "status": "Operational / World's Largest Power/Water"
    },
    {
        "id": "util_sudair",
        "name": "Sudair Solar PV IPP Complex",
        "country": "Saudi Arabia",
        "lat": 25.65,
        "lon": 45.85,
        "type": "Utility Solar PV",
        "capacity": "1,500 MW (Saudi Vision 2030 Flagship)",
        "operator": "ACWA Power / PIF Badeel",
        "source": "SPPC Saudi Power Procurement",
        "status": "Commercial Operations"
    }
]

plants_json = json.dumps(me_plants)[1:-1] # strip outer brackets
target = 'var globalUtilities = ['
replacement = 'var globalUtilities = [' + plants_json + ', '

assert target in js, "target not found"
js = js.replace(target, replacement, 1)

with open(js_path, 'w', encoding='utf-8') as f:
    f.write(js)

print("Added 5 major Saudi Arabia & UAE power plants to globalUtilities!")

