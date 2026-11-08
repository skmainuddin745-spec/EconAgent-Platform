with open(r'F:\documents\SOIC\EconAgent_Platform\platform_ui\bmap_tanker_component.py', 'r', encoding='utf-8') as f:
    code = f.read()

funcs = [
    'function initPipelinesLayers()',
    'function initVesselsLayer()',
    'function initGlobalInfrastructureLayers()',
    'function initWorldEquityLayer()',
    'function initDenseGridLayer()',
    'function initBankBranchesLayer()'
]

for fn in funcs:
    pos = code.find(fn)
    print(f'=== {fn} === (pos: {pos})')
    if pos != -1:
        print(code[pos:pos+2000])
        print('\n' + '='*40 + '\n')

