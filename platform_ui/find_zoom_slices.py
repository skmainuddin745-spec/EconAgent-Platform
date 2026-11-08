with open('F:/documents/SOIC/EconAgent_Platform/platform_ui/fractal_zoom_engine.py', 'r', encoding='utf-8') as f:
    text = f.read()

pos_s = text.find('var sectorData = {')
if pos_s == -1: pos_s = text.find('sectorData = {')
pos_f = text.find('var firmData = {')
if pos_f == -1: pos_f = text.find('firmData = {')
pos_n = text.find('var nanoData = {')
if pos_n == -1: pos_n = text.find('nanoData = {')
pos_end = text.find('window.onCountryDropdownChange = function')

print(f"Positions: sectorData={pos_s}, firmData={pos_f}, nanoData={pos_n}, end={pos_end}")

