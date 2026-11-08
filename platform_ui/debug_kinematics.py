import asyncio
import json
import subprocess
import urllib.request
import websockets

async def check_kinematics():
    chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    port = 9231
    bmap_url = "file:///F:/documents/SOIC/EconAgent_Platform\platform_ui\Bloomberg_BMAP_Terminal.html"
    
    proc = subprocess.Popen([
        chrome_path, "--headless=new", f"--remote-debugging-port={port}",
        "--disable-gpu", "--no-sandbox", "--allow-file-access-from-files", bmap_url
    ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    try:
        await asyncio.sleep(2.0)
        with urllib.request.urlopen(f"http://127.0.0.1:{port}/json") as resp:
            ws_url = json.loads(resp.read().decode())[0]["webSocketDebuggerUrl"]
            
        async with websockets.connect(ws_url) as ws:
            msg_id = 1
            async def eval_js(expr):
                nonlocal msg_id
                mid = msg_id
                msg_id += 1
                await ws.send(json.dumps({"id": mid, "method": "Runtime.evaluate", "params": {"expression": expr, "returnByValue": True}}))
                while True:
                    res = json.loads(await ws.recv())
                    if res.get("id") == mid:
                        return res.get("result", {}).get("value")

            timer_id = await eval_js("typeof liveKinematicsTimer")
            print("liveKinematicsTimer type:", timer_id)

            step_fn = await eval_js("typeof window.stepKinematics")
            print("stepKinematics type:", step_fn)

    finally:
        proc.kill()

if __name__ == "__main__":
    asyncio.run(check_kinematics())

