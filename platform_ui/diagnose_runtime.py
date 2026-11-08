import asyncio
import json
import subprocess
import urllib.request
import websockets

CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
PORT = 9223
DASHBOARD_URL = r"file:///F:/documents/SOIC/EconAgent_Platform/platform_ui/EconAgent_Dashboard.html"

async def main():
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
        print("Failed to connect")
        return

    async with websockets.connect(ws_url, max_size=10_000_000) as ws:
        msg_id = 0
        async def cdp_eval(expr):
            nonlocal msg_id
            msg_id += 1
            await ws.send(json.dumps({
                "id": msg_id,
                "method": "Runtime.evaluate",
                "params": {"expression": expr, "returnByValue": True}
            }))
            resp = json.loads(await ws.recv())
            return resp.get("result", {}).get("result", {}).get("value")

        # Check console logs / errors
        # Check active tabs
        res = await cdp_eval("""
            (() => {
                const activeTabs = Array.from(document.querySelectorAll('.tab.active')).map(t => t.textContent.trim());
                const activeContents = Array.from(document.querySelectorAll('.content.active')).map(c => ({
                    id: c.id,
                    offsetHeight: c.offsetHeight,
                    display: window.getComputedStyle(c).display,
                    visibility: window.getComputedStyle(c).visibility
                }));
                const allContents = Array.from(document.querySelectorAll('.content')).map(c => ({
                    id: c.id,
                    display: window.getComputedStyle(c).display,
                    offsetHeight: c.offsetHeight
                }));
                const viewport = document.getElementById('workspace_viewport');
                const vpInfo = viewport ? {
                    display: window.getComputedStyle(viewport).display,
                    offsetHeight: viewport.offsetHeight,
                    childrenCount: viewport.children.length
                } : null;

                return {
                    activeTabs,
                    activeContents,
                    vpInfo,
                    allContents
                };
            })()
        """)
        print("Initial state:", json.dumps(res, indent=2))

        # Now test clicking titans
        titans_click = await cdp_eval("""
            (() => {
                const btn = Array.from(document.querySelectorAll('.tab')).find(t => t.textContent.includes('Titans'));
                if (btn) {
                    btn.click();
                    const titansEl = document.getElementById('titans');
                    return {
                        clicked: true,
                        titansDisplay: window.getComputedStyle(titansEl).display,
                        titansHeight: titansEl.offsetHeight,
                        titansChildCount: titansEl.children.length,
                        activeContents: Array.from(document.querySelectorAll('.content.active')).map(c => c.id)
                    };
                }
                return { clicked: false };
            })()
        """)
        print("After Titans click:", json.dumps(titans_click, indent=2))

        # Check any uncaught errors
        # Now let's see why the user saw a black screen!
        # What if user clicked each tab from flows onwards?
        tab_tests = await cdp_eval("""
            (() => {
                const results = {};
                const tabs = Array.from(document.querySelectorAll('.tab'));
                for (const t of tabs) {
                    const text = t.textContent.trim();
                    t.click();
                    const activeContent = document.querySelector('.content.active');
                    results[text] = activeContent ? {
                        id: activeContent.id,
                        display: window.getComputedStyle(activeContent).display,
                        height: activeContent.offsetHeight
                    } : 'NONE';
                }
                return results;
            })()
        """)
        print("Tab tests:", json.dumps(tab_tests, indent=2))

    proc.terminate()

asyncio.run(main())

