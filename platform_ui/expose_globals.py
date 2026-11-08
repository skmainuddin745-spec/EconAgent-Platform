with open(r'F:\documents\SOIC\EconAgent_Platform\platform_ui\bmap_js_template.js', 'r', encoding='utf-8') as f:
    js = f.read()

target = """    window.bmapMap = leafletMap;
    window.leafletMap = leafletMap;
    window.globalVessels = globalVessels;
    window.manhattanBranches = manhattanBranches;
    window.vesselMarkersMap = vesselMarkersMap;
    window.datasetLayerGroups = datasetLayerGroups;
    window.activeLayers = activeLayers;"""

replacement = """    window.bmapMap = leafletMap;
    window.leafletMap = leafletMap;
    window.globalVessels = globalVessels;
    window.crudePipelines = crudePipelines;
    window.gasPipelines = gasPipelines;
    window.worldEquityData = worldEquityData;
    window.globalDenseGrid = globalDenseGrid;
    window.globalSubmarineCables = globalSubmarineCables;
    window.manhattanBranches = manhattanBranches;
    window.vesselMarkersMap = vesselMarkersMap;
    window.datasetLayerGroups = datasetLayerGroups;
    window.activeLayers = activeLayers;"""

if target in js:
    js = js.replace(target, replacement)
    with open(r'F:\documents\SOIC\EconAgent_Platform\platform_ui\bmap_js_template.js', 'w', encoding='utf-8') as f:
        f.write(js)
    print('Successfully exposed crudePipelines, worldEquityData, etc. to window!')
else:
    print('Target not found in bmap_js_template.js!')

