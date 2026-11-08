import asyncio
import json
import subprocess
import urllib.request
import websockets

async def test_dashboard():
    chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    port = 9233
    dash_url = "file:///F:/documents/SOIC/EconAgent_Platform/platform_ui/EconAgent_Dashboard.html"
    
    print("\n=======================================================")
    print("TESTING ECONAGENT MASTER DASHBOARD INTEGRATION")
    print(f"URL: {dash_url}")
    print("=======================================================")
    
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
                return r.get("result", {}).get("value")

            # 1. Ready state
            state = await eval_js("document.readyState")
            assert state == "complete", f"Doc state: {state}"
            print("✓ 1. Master Dashboard ready state: COMPLETE")

            # 2. Check BMAP Leaflet map inside dashboard
            has_bmap = await eval_js("typeof window.bmapMap !== 'undefined' && window.bmapMap !== null")
            assert has_bmap is True, "Leaflet bmapMap not found in dashboard"
            print("✓ 2. BMAP Leaflet Map mounted in Master Dashboard")

            # 3. Check that Hormuz preset can be triggered from dashboard
            await eval_js("window.jumpToBmapPreset('hormuz')")
            await asyncio.sleep(0.5)
            scope = await eval_js("document.getElementById('bmap_scope_label').textContent")
            print(f"✓ 3. Dashboard Hormuz Preset: '{scope}'")
            assert "HORMUZ" in scope

            # 4. Check zero CartoDB watermarks
            has_carto = await eval_js("document.documentElement.innerHTML.indexOf('cartocdn.com') >= 0 || document.documentElement.innerHTML.indexOf('carto.com/basemaps') >= 0")
            assert has_carto is False, "CartoDB URL found in dashboard!"
            print("✓ 4. ZERO CartoDB watermarks in Master Dashboard")

            # 5. Check console errors
            print("Console errors logged in Master Dashboard:", len(errors))
            if errors:
                for e in errors:
                    print("  ", e)
            assert len(errors) == 0, f"Found console errors: {errors}"
            print("✓ 5. Zero console errors confirmed in Master Dashboard!")

    finally:
        proc.kill()

if __name__ == "__main__":
    asyncio.run(test_dashboard())

