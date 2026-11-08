import asyncio
import json
import subprocess
import urllib.request
import websockets

async def debug_titans():
    chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    port = 9240
    url = "file:///F:/documents/SOIC/EconAgent_Platform/platform_ui/EconAgent_Dashboard.html"
    
    proc = subprocess.Popen([
        chrome_path, "--headless=new", f"--remote-debugging-port={port}",
        "--disable-gpu", "--no-sandbox", "--allow-file-access-from-files", url
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
                        print("EXCEPTION:", res["params"]["exceptionDetails"])

            await send_cmd("Runtime.enable")
            await send_cmd("Page.enable")
            await asyncio.sleep(1.0)
            
            async def eval_js(expr):
                r = await send_cmd("Runtime.evaluate", {"expression": expr, "returnByValue": True})
                if "exceptionDetails" in r:
                    print("JS Exception:", r["exceptionDetails"])
                    return None
                return r.get("result", {}).get("value")

            # Check tabs after flows: titans, soic_sectors, topnotch, macro, beta
            tabs_to_test = ['flows', 'titans', 'soic_sectors', 'topnotch', 'macro', 'beta', 'margins', 'multiples']
            
            for t in tabs_to_test:
                info = await eval_js(f"""
                    (function() {{
                        var tabBtn = Array.from(document.querySelectorAll('.tab')).find(function(el) {{
                            return (el.getAttribute('onclick') || '').indexOf("'{t}'") !== -1;
                        }});
                        if (tabBtn) tabBtn.click();
                        
                        var el = document.getElementById('{t}');
                        if (!el) return {{ exists: false }};
                        var style = window.getComputedStyle(el);
                        var rect = el.getBoundingClientRect();
                        return {{
                            exists: true,
                            display: style.display,
                            visibility: style.visibility,
                            opacity: style.opacity,
                            height: rect.height,
                            width: rect.width,
                            top: rect.top,
                            childCount: el.children.length,
                            classList: Array.from(el.classList),
                            hasText: el.innerText.length
                        }};
                    }})()
                """)
                print(f"Tab '{t}':", info)

    finally:
        proc.terminate()

asyncio.run(debug_titans())

