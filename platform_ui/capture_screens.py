import asyncio
import json
import subprocess
import urllib.request
import websockets
import base64

CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
PORT = 9224
DASHBOARD_URL = r"file:///F:/documents/SOIC/EconAgent_Platform/platform_ui/EconAgent_Dashboard.html"

async def capture_tab(tab_name, filename):
    proc = subprocess.Popen([
        CHROME_PATH,
        "--headless=new",
        f"--remote-debugging-port={PORT}",
        "--disable-gpu",
        "--no-sandbox",
        "--window-size=1600,1000",
        DASHBOARD_URL
    ])
    await asyncio.sleep(2.5)

    ws_url = None
    for _ in range(10):
        try:
            with urllib.request.urlopen(f"http://127.0.0.1:{PORT}/json") as resp:
                data = json.loads(resp.read().decode())
                for t in data:
                    if t.get("type") == "page":
                        ws_url = t.get("webSocketDebuggerUrl")
                        break
                if ws_url:
                    break
        except Exception:
            await asyncio.sleep(0.5)

    if not ws_url:
        proc.terminate()
        return

    async with websockets.connect(ws_url, max_size=10_000_000) as ws:
        msg_id = 0
        async def send(method, params=None):
            nonlocal msg_id
            msg_id += 1
            payload = {"id": msg_id, "method": method}
            if params:
                payload["params"] = params
            await ws.send(json.dumps(payload))
            return json.loads(await ws.recv())

        # Switch to tab
        eval_resp = await send("Runtime.evaluate", {
            "expression": f"""
                (() => {{
                    const btn = Array.from(document.querySelectorAll('.tab')).find(t => t.textContent.includes('{tab_name}'));
                    if (btn) btn.click();
                }})()
            """
        })
        await asyncio.sleep(0.5)

        # Capture screenshot
        shot = await send("Page.captureScreenshot", {"format": "png"})
        img_b64 = shot.get("result", {}).get("data")
        if img_b64:
            with open(filename, "wb") as f:
                f.write(base64.b64decode(img_b64))
            print(f"Captured {filename}")

    proc.terminate()

async def main():
    await capture_tab("Titans", "F:/documents/SOIC/EconAgent_Platform/platform_ui/screenshot_titans.png")
    await capture_tab("Technicals", "F:/documents/SOIC/EconAgent_Platform/platform_ui/screenshot_technicals.png")

asyncio.run(main())

