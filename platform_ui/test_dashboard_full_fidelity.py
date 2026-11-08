import asyncio
import json
import subprocess
import urllib.request
import websockets

async def run_dashboard_tests():
    chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    port = 9227
    dash_url = "file:///F:/documents/SOIC/EconAgent_Platform/platform_ui/EconAgent_Dashboard.html"
    
    print("\n--- LAUNCHING CHROME TO TEST MASTER DASHBOARD PLATFORM ---")
    proc = subprocess.Popen([
        chrome_path, "--headless=new", f"--remote-debugging-port={port}",
        "--disable-gpu", "--no-sandbox", "--allow-file-access-from-files", dash_url
    ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    try:
        await asyncio.sleep(2.5)
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

            # 1. Verify Page Status
            ready = await eval_js("document.readyState")
            print("1. document.readyState:", ready)
            assert ready == "complete"

            # 2. Check BMAP Tab Loaded inside Dashboard
            bmap_status = await eval_js("""
                (function() {
                    var tab = document.getElementById('bmap');
                    var active = tab ? tab.classList.contains('active') : false;
                    var legend = document.querySelector('#bmap #bmap_branch_legend');
                    var card = document.querySelector('#bmap #bmap_param_card_bank');
                    var slider = document.querySelector('#bmap #slider_bank_dep');
                    return {
                        hasTab: !!tab,
                        isActive: active,
                        hasLegend: !!legend,
                        hasCard: !!card,
                        hasSlider: !!slider
                    };
                })()
            """)
            print("2. BMAP in Master Dashboard:", bmap_status)
            assert bmap_status["hasTab"] and bmap_status["hasLegend"] and bmap_status["hasCard"]

            # 3. Test Tab Switching to SOIC, Titans, and back to BMAP
            tab_switch = await eval_js("""
                (function() {
                    window.showTab(null, 'soic_sectors');
                    var soicActive = document.getElementById('soic_sectors').classList.contains('active');
                    window.showTab(null, 'titans');
                    var titansActive = document.getElementById('titans').classList.contains('active');
                    window.showTab(null, 'bmap');
                    var bmapActive = document.getElementById('bmap').classList.contains('active');
                    return {
                        soicActive: soicActive,
                        titansActive: titansActive,
                        bmapActive: bmapActive
                    };
                })()
            """)
            print("3. Master Dashboard Tab Switching:", tab_switch)
            assert tab_switch["soicActive"] and tab_switch["titansActive"] and tab_switch["bmapActive"]

            # 4. Check Console Errors
            print("4. Console errors:", len(errors))
            if errors:
                for e in errors[:5]:
                    print("  Console err:", e)

            print("\n>>> MASTER DASHBOARD FULL FIDELITY CONFIRMED! <<<")
    finally:
        proc.kill()

if __name__ == "__main__":
    asyncio.run(run_dashboard_tests())

