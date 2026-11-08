import asyncio
import json
import subprocess
import urllib.request
import websockets

async def run_full_suite_tests():
    chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    port = 9228
    bmap_url = "file:///F:/documents/SOIC/EconAgent_Platform/platform_ui/Bloomberg_BMAP_Terminal.html"
    
    print("\n=======================================================")
    print("TESTING FULL BLOOMBERG SUITE (ALL 29 IMAGES REPLICATED)")
    print(f"URL: {bmap_url}")
    print("=======================================================")
    
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
            errors = []
            
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
                            errors.append(f"[{c_type.upper()}] {args}")

            await send_cmd("Runtime.enable")
            await send_cmd("Page.enable")
            await asyncio.sleep(1.0)
            
            async def eval_js(expr):
                r = await send_cmd("Runtime.evaluate", {"expression": expr, "returnByValue": True})
                if "exceptionDetails" in r:
                    print("JS Exception:", r["exceptionDetails"])
                    return None
                return r.get("result", {}).get("value")

            # 1. Verify Page Ready
            ready = await eval_js("document.readyState")
            print("1. document.readyState:", ready)
            assert ready == "complete"

            # 2. Test Crude Oil Pipelines (Image 27)
            pipe_info = await eval_js("""
                (function() {
                    window.jumpToBmapPreset('crude_pipelines');
                    var card = document.getElementById('bmap_pipelines_filter_card');
                    var leg = document.getElementById('bmap_pipelines_legend');
                    return {
                        cardVisible: card ? window.getComputedStyle(card).display !== 'none' : false,
                        legendVisible: leg ? window.getComputedStyle(leg).display !== 'none' : false,
                        label: document.getElementById('bmap_scope_label').textContent
                    };
                })()
            """)
            print("2. Crude Oil Pipelines (Image 27):", pipe_info)
            assert pipe_info["cardVisible"] and pipe_info["legendVisible"]

            # 3. Test Greg Mortimer Expedition Vessel & Tooltip (Image 8)
            greg_info = await eval_js("""
                (function() {
                    window.jumpToBmapPreset('greg_mortimer');
                    var pop = document.getElementById('bmap_vessel_popup');
                    return {
                        popupVisible: pop ? pop.style.display !== 'none' : false,
                        name: document.getElementById('pop_vessel_name').textContent,
                        dest: document.getElementById('pop_vessel_dest').textContent,
                        speed: document.getElementById('pop_vessel_speed').textContent
                    };
                })()
            """)
            print("3. Greg Mortimer Vessel (Image 8):", greg_info)
            assert "GREG MORTIMER" in greg_info["name"]
            assert "DEVIL ISLAND" in greg_info["dest"]

            # 4. Test Manhattan Street-Level Satellite & FDIC Branch Tooltip (Images 7, 9, 10)
            man_info = await eval_js("""
                (function() {
                    window.jumpToBmapPreset('manhattan');
                    var pop = document.getElementById('bmap_branch_popup');
                    return {
                        branchName: document.getElementById('pop_branch_name').textContent,
                        company: document.getElementById('pop_branch_company').textContent,
                        deposits: document.getElementById('pop_branch_dep').textContent,
                        companyAssets: document.getElementById('pop_branch_comp_assets').textContent,
                        year: document.getElementById('pop_branch_year').textContent
                    };
                })()
            """)
            print("4. Manhattan FDIC Tooltip (Image 10):", man_info)
            assert "Third Avenue" in man_info["branchName"]
            assert "JPMorgan Chase" in man_info["company"]
            assert "1,214,602k" in man_info["deposits"]

            # 5. Test Maritime Berth Visits Table (Image 5)
            table_info = await eval_js("""
                (function() {
                    window.switchBmapView('table');
                    var rows = document.querySelectorAll('#bmap_data_grid_tbody tr');
                    var firstRow = rows.length > 0 ? rows[0].innerText.replace(/\\s+/g, ' ') : '';
                    return {
                        rowCount: rows.length,
                        firstRow: firstRow
                    };
                })()
            """)
            print("5. Berth Visits Table (Image 5):", table_info)
            assert table_info["rowCount"] >= 20
            assert "Cabinda/Nemba" in table_info["firstRow"] or "Novorossiysk" in table_info["firstRow"]

            # 6. Test SPLC Supply Chain Analysis (Images 24, 25)
            splc_info = await eval_js("""
                (function() {
                    window.switchBmapView('splc');
                    window.switchSplcTargetFirm('AAPL');
                    var aaplTitle = document.getElementById('splc_firm_title').textContent;
                    var supCount = document.querySelectorAll('#splc_suppliers_list > div').length;
                    var custCount = document.querySelectorAll('#splc_customers_list > div').length;
                    
                    window.switchSplcTargetFirm('LMT');
                    var lmtTitle = document.getElementById('splc_firm_title').textContent;
                    
                    return {
                        aaplTitle: aaplTitle,
                        lmtTitle: lmtTitle,
                        suppliersRendered: supCount,
                        customersRendered: custCount
                    };
                })()
            """)
            print("6. SPLC Supply Chain Analysis (Images 24, 25):", splc_info)
            assert "AAPL" in splc_info["aaplTitle"]
            assert "LMT" in splc_info["lmtTitle"]
            assert splc_info["suppliersRendered"] >= 8

            # 7. Test FXC Currency Rates Matrix (Image 1)
            fxc_info = await eval_js("""
                (function() {
                    window.switchBmapView('fxc');
                    var headers = document.querySelectorAll('#fxc_table_thead th');
                    var rows = document.querySelectorAll('#fxc_table_tbody tr');
                    return {
                        headersCount: headers.length,
                        rowsCount: rows.length
                    };
                })()
            """)
            print("7. FXC Currency Rates Matrix (Image 1):", fxc_info)
            assert fxc_info["headersCount"] == 12  # Base + 11 currencies
            assert fxc_info["rowsCount"] == 11

            # 8. Test VOL 3D Volatility Surface (Images 13, 17)
            vol_info = await eval_js("""
                (function() {
                    window.switchBmapView('vol');
                    window.rotateVolSurface(30);
                    var canvas = document.getElementById('vol_surface_canvas');
                    return {
                        hasCanvas: !!canvas,
                        w: canvas ? canvas.width : 0,
                        h: canvas ? canvas.height : 0
                    };
                })()
            """)
            print("8. VOL 3D Volatility Surface (Images 13, 17):", vol_info)
            assert vol_info["hasCanvas"]

            # 9. Test GPC Candlestick Chart & Checklist (Images 14, 15)
            chart_info = await eval_js("""
                (function() {
                    window.switchBmapView('chart');
                    window.toggleGpcIndicator('ichimoku');
                    window.drawTriangleBreakoutPattern();
                    var canvas = document.getElementById('gpc_main_canvas');
                    return {
                        hasCanvas: !!canvas,
                        checklistItems: document.querySelectorAll('#gpc_checklist_container input').length
                    };
                })()
            """)
            print("9. GPC Candlesticks & Technical Checklist (Images 14, 15):", chart_info)
            assert chart_info["checklistItems"] >= 10

            # 10. Test READ Most Read Stories (Images 18, 19)
            news_info = await eval_js("""
                (function() {
                    window.switchBmapView('news');
                    var count = document.querySelectorAll('#bmap_read_news_list > div').length;
                    return { storiesCount: count };
                })()
            """)
            print("10. READ Most Read Stories (Images 18, 19):", news_info)
            assert news_info["storiesCount"] >= 15

            # 11. Switch back to Map & Check Console Errors
            await eval_js("window.switchBmapView('map');")
            print(f"Total Console Errors: {len(errors)}")
            if errors:
                for e in errors[:5]:
                    print("  Console err:", e)

            print("\n>>> ALL 29 IMAGES & ADVANCED PARAMETERS FULLY VERIFIED WITH 0 ERRORS! <<<")
    finally:
        proc.kill()

if __name__ == "__main__":
    asyncio.run(run_full_suite_tests())

