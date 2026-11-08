import asyncio
import json
import subprocess
import urllib.request
import websockets

async def run_feature_verification():
    chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    port = 9238
    bmap_url = "file:///F:/documents/SOIC/EconAgent_Platform/platform_ui/Bloomberg_BMAP_Terminal.html"
    
    print("\n=======================================================")
    print("VERIFYING TOP DROPDOWNS, HOVER/DRAG DETAILS & SOIC VIEW")
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
            async def send_cmd(method, params=None):
                nonlocal msg_id
                mid = msg_id
                msg_id += 1
                await ws.send(json.dumps({"id": mid, "method": method, "params": params or {}}))
                while True:
                    res = json.loads(await ws.recv())
                    if res.get("id") == mid:
                        return res.get("result", {})
                    if res.get("method") == "Runtime.exceptionThrown":
                        print("JS EXCEPTION:", res["params"]["exceptionDetails"])

            await send_cmd("Runtime.enable")
            await send_cmd("Page.enable")
            await asyncio.sleep(1.0)
            
            async def eval_js(expr):
                r = await send_cmd("Runtime.evaluate", {"expression": expr, "returnByValue": True})
                if "exceptionDetails" in r:
                    print("JS Exception:", r["exceptionDetails"])
                    return None
                return r.get("result", {}).get("value")

            # 1. Test Suggested Datasets Dropdown Menu on Crimson Ribbon
            sugg_test = await eval_js("""
                (function() {
                    window.toggleSuggestedDropdown();
                    var menu = document.getElementById('bmap_suggested_dropdown_menu');
                    var items = document.getElementById('top_suggested_items_container');
                    return {
                        isOpen: menu && window.getComputedStyle(menu).display !== 'none',
                        itemsCount: items ? items.children.length : 0
                    };
                })()
            """)
            print("1. Top Ribbon Suggested Datasets Dropdown:", sugg_test)
            assert sugg_test["isOpen"] and sugg_test["itemsCount"] >= 20

            # 2. Test New Datasets Dropdown Menu on Crimson Ribbon
            new_test = await eval_js("""
                (function() {
                    window.toggleNewDropdown();
                    var menu = document.getElementById('bmap_new_dropdown_menu');
                    var items = document.getElementById('top_new_items_container');
                    return {
                        isOpen: menu && window.getComputedStyle(menu).display !== 'none',
                        itemsCount: items ? items.children.length : 0
                    };
                })()
            """)
            print("2. Top Ribbon New Datasets Dropdown:", new_test)
            assert new_test["isOpen"] and new_test["itemsCount"] >= 9

            # 3. Test Blue Ship Hover / Drag Details Inspector
            vsl_test = await eval_js("""
                (function() {
                    var v0 = window.globalVessels[0];
                    window.selectActiveVessel(v0);
                    window.showUniversalVesselPopup(v0);
                    var pop = document.getElementById('bmap_universal_vessel_popup');
                    return {
                        popupVisible: pop && window.getComputedStyle(pop).display !== 'none',
                        vesselName: document.getElementById('uni_vessel_name').textContent,
                        vesselSpeed: document.getElementById('uni_vessel_speed').textContent,
                        vesselDest: document.getElementById('uni_vessel_dest').textContent,
                        hasZoomBtn: !!pop.querySelector('button[onclick*="zoomToActiveVessel"]'),
                        hasHistoryBtn: !!pop.querySelector('button[onclick*="viewActiveVesselHistory"]')
                    };
                })()
            """)
            print("3. Blue Ship Telemetry Inspector Details:", vsl_test)
            assert vsl_test["popupVisible"]
            assert "SEAWAYS CATALONIA" in vsl_test["vesselName"]
            assert vsl_test["hasZoomBtn"] and vsl_test["hasHistoryBtn"]

            # 4. Test Yellow Circle (Bank Branch) Hover / Drag Details Inspector
            branch_test = await eval_js("""
                (function() {
                    var mb = window.manhattanBranches ? window.manhattanBranches[0] : null;
                    if (mb) {
                        window.showBranchQuickTooltip(mb.name, mb.bank, mb.deposits_k, 'NY', 'Commercial Branch', mb.lat, mb.lon);
                    }
                    var pop = document.getElementById('bmap_branch_popup');
                    return {
                        popupVisible: pop && window.getComputedStyle(pop).display !== 'none',
                        branchName: document.getElementById('pop_branch_name').textContent,
                        hasZoomBtn: !!pop.querySelector('button[onclick*="zoomToActiveBranch"]'),
                        hasAuditBtn: !!pop.querySelector('button[onclick*="viewActiveBranchFilings"]')
                    };
                })()
            """)
            print("4. Yellow Circle (Bank Branch) Details Inspector:", branch_test)
            assert branch_test["popupVisible"]
            assert branch_test["hasZoomBtn"] and branch_test["hasAuditBtn"]

            # 5. Test SOIC Valuation (TVGP) View Integration
            soic_test = await eval_js("""
                (function() {
                    window.switchBmapView('soic');
                    var c = document.getElementById('bmap_view_container_soic');
                    return {
                        soicVisible: c && window.getComputedStyle(c).display !== 'none',
                        hasDuPont: c ? c.innerHTML.indexOf('DuPont') !== -1 : false,
                        hasKEI: c ? c.innerHTML.indexOf('KEI Industries') !== -1 : false,
                        hasAPL: c ? c.innerHTML.indexOf('APL Apollo') !== -1 : false
                    };
                })()
            """)
            print("5. SOIC Proprietary Valuation View:", soic_test)
            assert soic_test["soicVisible"] and soic_test["hasDuPont"] and soic_test["hasKEI"]

            print("\n=======================================================")
            print("ALL 5 ADVANCED VERIFICATION TESTS PASSED PERFECTLY! 🚀")
            print("=======================================================")

    finally:
        proc.terminate()

asyncio.run(run_feature_verification())

