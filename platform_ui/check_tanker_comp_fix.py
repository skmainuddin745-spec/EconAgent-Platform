with open(r'F:\documents\SOIC\EconAgent_Platform\platform_ui\bmap_tanker_component.py', 'r', encoding='utf-8') as f:
    text = f.read()

print('Has try pt in bmap_tanker_component.py?', 'try {\n          pt = leafletMap.containerPointToLatLng' in text or 'try {\n        pt = leafletMap.containerPointToLatLng' in text or 'try { pt = leafletMap.containerPointToLatLng' in text)

