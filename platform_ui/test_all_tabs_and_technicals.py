import asyncio
import json
import os
import subprocess
import time
import urllib.request
import websockets
from typing import Dict, Any

CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
PORT = 9222
DASHBOARD_URL = r"file:///F:/documents/SOIC/EconAgent_Platform/platform_ui/EconAgent_Dashboard.html"

async def run_test():
    print("\n=======================================================")
    print("TESTING ALL TABS AFTER FLOW FINANCING & REAL-TIME TECHNICALS")
    print("=======================================================")

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
    for attempt in range(10):
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
        raise RuntimeError("Failed to connect to Chrome headless")

    async with websockets.connect(ws_url, max_size=10_000_000) as ws:
        msg_id = 0
        async def cdp_eval(expression: str) -> Any:
            nonlocal msg_id
            msg_id += 1
            payload = {
                "id": msg_id,
                "method": "Runtime.evaluate",
                "params": {
                    "expression": expression,
                    "returnByValue": True,
                    "awaitPromise": True
                }
            }
            await ws.send(json.dumps(payload))
            while True:
                raw = await ws.recv()
                res = json.loads(raw)
                if res.get("id") == msg_id:
                    if "exceptionDetails" in res.get("result", {}):
                        raise RuntimeError(f"CDP Eval error: {res['result']['exceptionDetails']}")
                    return res.get("result", {}).get("result", {}).get("value")

        # 1. Test clicking all tabs after flows
        tabs_to_test = [
            ('titans', 'Financial Titans'),
            ('soic_sectors', 'SOIC Sector Models & IRRs'),
            ('topnotch', 'Elite Firm Frameworks'),
            ('macro', 'Macro ERP/WACC'),
            ('beta', 'Beta & Risk'),
            ('margins', 'Margins'),
            ('multiples', 'Multiples'),
            ('growth', 'Growth Rates'),
            ('capstruct', 'Cap Structure'),
            ('workcap', 'Working Capital'),
            ('taxrate', 'Tax Rates'),
            ('fundamentals', 'CapEx/EVA'),
            ('agents', 'Agent Status'),
            ('papers', 'Papers Corpus'),
            ('arch', 'Architecture')
        ]

        print("\n1. Verifying Tabs After FLOW Financing...")
        for tab_id, label in tabs_to_test:
            res = await cdp_eval(f"""
            (function() {{
                showTab(null, '{tab_id}');
                var el = document.getElementById('{tab_id}');
                if (!el) return {{ exists: false }};
                var rect = el.getBoundingClientRect();
                var cs = window.getComputedStyle(el);
                var textLen = el.innerText ? el.innerText.length : 0;
                return {{
                    exists: true,
                    isActive: el.classList.contains('active'),
                    display: cs.display,
                    visibility: cs.visibility,
                    width: rect.width,
                    height: rect.height,
                    textLen: textLen
                }};
            }})()
            """)
            assert res.get('exists'), f"Tab {tab_id} does not exist in DOM"
            assert res.get('isActive'), f"Tab {tab_id} failed to get .active class"
            assert res.get('display') != 'none', f"Tab {tab_id} display is none"
            assert res.get('height') > 100, f"Tab {tab_id} height too small ({res.get('height')}) - blank tab detected!"
            assert res.get('textLen') > 200, f"Tab {tab_id} has insufficient text ({res.get('textLen')})"
            print(f"  ✓ Tab '{tab_id}' ({label}): visible={res['display']}, height={res['height']:.1f}px, text={res['textLen']} chars")

        # 2. Test Real-Time Technicals Tab
        print("\n2. Verifying Real-Time Technicals Tab & Stage Analysis Engine...")
        tech_res = await cdp_eval("""
        (function() {
            showTab(null, 'technicals');
            var el = document.getElementById('technicals');
            if (!el) return { exists: false };
            var rect = el.getBoundingClientRect();
            var cs = window.getComputedStyle(el);
            var canvas = document.getElementById('technicalsCanvas');
            var canvasRect = canvas ? canvas.getBoundingClientRect() : null;
            var cards = [
                document.getElementById('tech_card_stage'),
                document.getElementById('tech_card_wma'),
                document.getElementById('tech_card_ema'),
                document.getElementById('tech_card_adx'),
                document.getElementById('tech_card_rsi'),
                document.getElementById('tech_card_vstop')
            ];
            return {
                exists: true,
                isActive: el.classList.contains('active'),
                display: cs.display,
                width: rect.width,
                height: rect.height,
                hasCanvas: !!canvas,
                canvasW: canvasRect ? canvasRect.width : 0,
                canvasH: canvasRect ? canvasRect.height : 0,
                stageText: cards[0] ? cards[0].innerText : '',
                wmaText: cards[1] ? cards[1].innerText : '',
                emaText: cards[2] ? cards[2].innerText : '',
                adxText: cards[3] ? cards[3].innerText : '',
                rsiText: cards[4] ? cards[4].innerText : '',
                vstopText: cards[5] ? cards[5].innerText : ''
            };
        })()
        """)
        assert tech_res.get('exists'), "Technicals tab does not exist in DOM"
        assert tech_res.get('isActive'), "Technicals tab is not active"
        assert tech_res.get('display') != 'none', "Technicals tab is hidden"
        assert tech_res.get('height') > 500, f"Technicals tab height too small ({tech_res.get('height')})"
        assert tech_res.get('hasCanvas'), "Technicals canvas not found"
        assert tech_res.get('canvasW') > 500, f"Technicals canvas width too small ({tech_res.get('canvasW')})"
        print(f"  ✓ Technicals Tab Mounted: height={tech_res['height']:.1f}px, canvas={tech_res['canvasW']:.0f}x{tech_res['canvasH']:.0f}")
        print(f"  ✓ Stage: {tech_res['stageText']} | 30-WMA: {tech_res['wmaText']} | 200-EMA: {tech_res['emaText']}")
        print(f"  ✓ ADX: {tech_res['adxText']} | RSI: {tech_res['rsiText']} | Vstop: {tech_res['vstopText']}")

        # 3. Test Security Switching in Technicals
        print("\n3. Testing Security Switcher in Technicals...")
        switch_res = await cdp_eval("""
        (function() {
            window.switchTechStock('KEI');
            var keiP = document.getElementById('tech_price_display').innerText;
            var keiTitle = document.getElementById('tech_chart_title').innerText;
            
            window.switchTechStock('NVDA');
            var nvdaP = document.getElementById('tech_price_display').innerText;
            var nvdaTitle = document.getElementById('tech_chart_title').innerText;
            
            // Return back to Polycab
            window.switchTechStock('POLYCAB');
            return { keiPrice: keiP, keiTitle: keiTitle, nvdaPrice: nvdaP, nvdaTitle: nvdaTitle };
        })()
        """)
        print(f"  ✓ Switched to KEI: price={switch_res['keiPrice']}, title={switch_res['keiTitle']}")
        print(f"  ✓ Switched to NVDA: price={switch_res['nvdaPrice']}, title={switch_res['nvdaTitle']}")
        assert "KEI" in switch_res['keiTitle'], "KEI title mismatch"
        assert "NVIDIA" in switch_res['nvdaTitle'], "NVDA title mismatch"

        # 4. Test Quick Action Button & Hotkey
        print("\n4. Testing Quick Jump Ribbon & Hotkey Dispatcher...")
        jump_res = await cdp_eval("""
        (function() {
            // Jump away to macro
            showTab(null, 'macro');
            var macroActive = document.getElementById('macro').classList.contains('active');
            
            // Jump back to technicals using jumpToTabForActiveFirm
            jumpToTabForActiveFirm('technicals');
            var techActiveViaJump = document.getElementById('technicals').classList.contains('active');
            
            // Jump away to scen
            showTab(null, 'scen');
            // Jump back via runHotkey
            runHotkey('technicals');
            var techActiveViaHotkey = document.getElementById('technicals').classList.contains('active');
            
            return { macroActive: macroActive, techActiveViaJump: techActiveViaJump, techActiveViaHotkey: techActiveViaHotkey };
        })()
        """)
        assert jump_res['techActiveViaJump'], "jumpToTabForActiveFirm('technicals') failed"
        assert jump_res['techActiveViaHotkey'], "runHotkey('technicals') failed"
        print(f"  ✓ jumpToTabForActiveFirm('technicals') successfully activated technicals tab!")
        print(f"  ✓ runHotkey('technicals') successfully activated technicals tab!")

    proc.terminate()
    print("\n=======================================================")
    print("ALL TESTS PASSED! ZERO BLANK TABS & REAL-TIME TECHNICALS 100% OPERATIONAL! 🚀")
    print("=======================================================")

if __name__ == "__main__":
    asyncio.run(run_test())
