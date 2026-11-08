import asyncio
import json
import os
import subprocess
import time
import urllib.request
import websockets

async def test_all_v5():
    chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    port = 9224
    
    # --- TEST 1: STANDALONE BMAP TERMINAL ---
    bmap_url = "file:///F:/documents/SOIC/EconAgent_Platform/platform_ui/Bloomberg_BMAP_Terminal.html"
    print(f"\n==========================================")
    print(f"TESTING STANDALONE: {bmap_url}")
    print(f"==========================================")
    
    proc = subprocess.Popen([
        chrome_path, "--headless=new", f"--remote-debugging-port={port}",
        "--disable-gpu", "--no-sandbox", "--allow-file-access-from-files", bmap_url
    ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    try:
        await asyncio.sleep(2.0)
        with urllib.request.urlopen(f"http://127.0.0.1:{port}/json") as resp:
            ws_url = json.loads(resp.read().decode())[0]["webSocketDebuggerUrl"]
            
        async with websockets.connect(ws_url, max_size=50_000_000) as ws:
            msg_id = 1
            bmap_errors = []
            
            async def send_cmd(method, params=None):
                nonlocal msg_id
                mid = msg_id
                msg_id += 1
                await ws.send(json.dumps({"id": mid, "method": method, "params": params or {}}))
                while True:
                    res = json.loads(await ws.recv())
                    if res.get("id") == mid:
                        return res.get("result", {})
                    if res.get("method") == "Runtime.consoleAPICalled":
                        c_type = res["params"]["type"]
                        args = " ".join([str(a.get("value", a.get("description", ""))) for a in res["params"]["args"]])
                        if c_type in ("error", "warning"):
                            bmap_errors.append(f"[{c_type.upper()}] {args}")
                            print(f"BMAP CONSOLE {c_type.upper()}: {args}")

            await send_cmd("Runtime.enable")
            await send_cmd("Page.enable")
            await asyncio.sleep(1.0)
            
            async def eval_js(expr):
                r = await send_cmd("Runtime.evaluate", {"expression": expr, "returnByValue": True})
                if "exceptionDetails" in r:
                    print(f"BMAP JS EXCEPTION in '{expr[:60]}...':", r["exceptionDetails"])
                    return None
                return r.get("result", {}).get("value")

            ready = await eval_js("document.readyState")
            print("1. document.readyState:", ready)
            
            map_status = await eval_js("""
                ({
                    hasMap: typeof bmapMap !== 'undefined' && !!bmapMap,
                    zoom: typeof bmapMap !== 'undefined' && bmapMap ? bmapMap.getZoom() : -1,
                    minZoom: typeof bmapMap !== 'undefined' && bmapMap ? bmapMap.getMinZoom() : -1,
                    center: typeof bmapMap !== 'undefined' && bmapMap ? [bmapMap.getCenter().lat, bmapMap.getCenter().lng] : null
                })
            """)
            print("2. Map status:", map_status)
            
            drawer_status = await eval_js("""
                ({
                    hasDrawer: !!document.getElementById('bmap_map_content_drawer'),
                    hasVesselsCard: !!document.getElementById('bmap_vessels_filter_card'),
                    suggestedCount: document.getElementById('suggested_datasets_list') ? document.getElementById('suggested_datasets_list').children.length : 0,
                    newCount: document.getElementById('new_datasets_list') ? document.getElementById('new_datasets_list').children.length : 0
                })
            """)
            print("3. Drawer & Datasets status:", drawer_status)

            # Test toggling Refineries and LNG Terminals
            toggle_res = await eval_js("""
                (function() {
                    window.toggleBmapDataset('refineries');
                    window.toggleBmapDataset('lng_terminals');
                    var refActive = window.bmapMap ? window.bmapMap.hasLayer(window.datasetLayerGroups ? window.datasetLayerGroups['refineries'] : null) : false;
                    var lngActive = window.bmapMap ? window.bmapMap.hasLayer(window.datasetLayerGroups ? window.datasetLayerGroups['lng_terminals'] : null) : false;
                    return { refActive: refActive, lngActive: lngActive };
                })()
            """)
            print("4. Dataset toggle result:", toggle_res)

            # Test Search Autocomplete for Hormuz
            search_res = await eval_js("""
                (function() {
                    window.handleBmapUniversalSearch('Hormuz');
                    var box = document.getElementById('bmap_search_results_box');
                    var visible = box && box.style.display !== 'none';
                    var matchCount = box ? box.children.length : 0;
                    return { searchBoxVisible: visible, matches: matchCount };
                })()
            """)
            print("5. Universal Search for 'Hormuz':", search_res)

            # Test View Switching (Table, Chart, News, Map)
            views_res = await eval_js("""
                (function() {
                    window.switchBmapView('table');
                    var tableVisible = document.getElementById('bmap_view_container_table').style.display === 'block';
                    window.switchBmapView('chart');
                    var chartVisible = document.getElementById('bmap_view_container_chart').style.display === 'block';
                    window.switchBmapView('news');
                    var newsVisible = document.getElementById('bmap_view_container_news').style.display === 'block';
                    window.switchBmapView('map');
                    var mapVisible = document.getElementById('bmap_view_container_map').style.display === 'block';
                    return { table: tableVisible, chart: chartVisible, news: newsVisible, map: mapVisible };
                })()
            """)
            print("6. Multi-View Switching:", views_res)

            print(f"BMAP Standalone Console Errors: {len(bmap_errors)}")
    finally:
        proc.kill()

    # --- TEST 2: MASTER DASHBOARD PLATFORM ---
    dash_url = "file:///F:/documents/SOIC/EconAgent_Platform/platform_ui/EconAgent_Dashboard.html"
    print(f"\n==========================================")
    print(f"TESTING MASTER DASHBOARD: {dash_url}")
    print(f"==========================================")
    
    proc2 = subprocess.Popen([
        chrome_path, "--headless=new", f"--remote-debugging-port={port}",
        "--disable-gpu", "--no-sandbox", "--allow-file-access-from-files", dash_url
    ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    try:
        await asyncio.sleep(2.5)
        with urllib.request.urlopen(f"http://127.0.0.1:{port}/json") as resp:
            ws_url2 = json.loads(resp.read().decode())[0]["webSocketDebuggerUrl"]
            
        async with websockets.connect(ws_url2, max_size=50_000_000) as ws2:
            msg_id = 1
            dash_errors = []
            
            async def send_cmd2(method, params=None):
                nonlocal msg_id
                mid = msg_id
                msg_id += 1
                await ws2.send(json.dumps({"id": mid, "method": method, "params": params or {}}))
                while True:
                    res = json.loads(await ws2.recv())
                    if res.get("id") == mid:
                        return res.get("result", {})
                    if res.get("method") == "Runtime.consoleAPICalled":
                        c_type = res["params"]["type"]
                        args = " ".join([str(a.get("value", a.get("description", ""))) for a in res["params"]["args"]])
                        if c_type in ("error", "warning"):
                            dash_errors.append(f"[{c_type.upper()}] {args}")
                            print(f"DASHBOARD CONSOLE {c_type.upper()}: {args}")

            await send_cmd2("Runtime.enable")
            await send_cmd2("Page.enable")
            await asyncio.sleep(1.0)
            
            async def eval_js2(expr):
                r = await send_cmd2("Runtime.evaluate", {"expression": expr, "returnByValue": True})
                if "exceptionDetails" in r:
                    print(f"DASHBOARD JS EXCEPTION in '{expr[:60]}...':", r["exceptionDetails"])
                    return None
                return r.get("result", {}).get("value")

            ready2 = await eval_js2("document.readyState")
            print("1. document.readyState:", ready2)

            bmap_in_dash = await eval_js2("""
                ({
                    hasBmapTab: !!document.getElementById('bmap'),
                    bmapIsActive: document.getElementById('bmap') ? document.getElementById('bmap').classList.contains('active') : false,
                    hasMapContentDrawer: !!document.querySelector('#bmap #bmap_map_content_drawer'),
                    hasVesselsCard: !!document.querySelector('#bmap #bmap_vessels_filter_card'),
                    suggestedDatasetsCount: document.querySelectorAll('#bmap #suggested_datasets_list .dataset-row').length,
                    newDatasetsCount: document.querySelectorAll('#bmap #new_datasets_list .dataset-row').length
                })
            """)
            print("2. BMAP in Master Dashboard:", bmap_in_dash)

            # Test Master Dropdowns Cascading
            ribbon_test = await eval_js2("""
                (function() {
                    window.syncGlobalCountryChange('india');
                    window.syncGlobalSectorChange('edu_in');
                    window.syncGlobalFirmChange('mps');
                    var gf = document.getElementById('global_firm_select');
                    var curFirm = gf ? gf.value : null;
                    return { selectedFirm: curFirm };
                })()
            """)
            print("3. Master Cascading Dropdowns:", ribbon_test)

            print(f"Master Dashboard Console Errors: {len(dash_errors)}")
    finally:
        proc2.kill()

if __name__ == "__main__":
    asyncio.run(test_all_v5())

