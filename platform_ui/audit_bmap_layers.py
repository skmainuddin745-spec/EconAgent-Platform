with open('F:/documents/SOIC/EconAgent_Platform/platform_ui/bmap_tanker_component.py', 'r', encoding='utf-8') as f:
    text = f.read()

import re

# Find all layers created
layer_adds = re.findall(r'(\w+)\.addTo\((?:bmapMap|map)\)', text)
print('Layers added to map:', set(layer_adds))

# Find all interactive elements
# 1. Pipelines / lines
polylines = re.findall(r'L\.polyline\([^)]+\)', text)
print('\nPolylines count:', len(polylines))
for p in polylines[:5]:
    print('  Polyline:', p[:120])

# 2. CircleMarkers
circles = re.findall(r'L\.circleMarker\([^,]+,\s*\{([^}]+)\}\)', text)
print('\nCircleMarkers count:', len(circles))
for c in circles[:8]:
    print('  CircleMarker config:', c.replace('\n', ' ').strip()[:140])

# 3. Markers
markers = re.findall(r'L\.marker\([^,]+,\s*\{([^}]+)\}\)', text)
print('\nMarkers count:', len(markers))
for m in markers[:8]:
    print('  Marker config:', m.replace('\n', ' ').strip()[:140])

