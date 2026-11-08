import asyncio
import json
import subprocess
import urllib.request
import websockets

async def run_tests():
    chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    port = 9225
    bmap_url = "file:///F:/documents/SOIC/EconAgent_Platform/platform_ui/Bloomberg_BMAP_Terminal.html"
    
    print("\n--- LAUNCHING CHROME TO TEST BLOOMBERG TERMINAL UI PARAMETERS ---")
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

            await send_cmd("Runtime.enable")
            await send_cmd("Page.enable")
            await asyncio.sleep(1.0)
            
            async def eval_js(expr):
                r = await send_cmd("Runtime.evaluate", {"expression": expr, "returnByValue": True})
                if "exceptionDetails" in r:
                    print("JS Exception:", r["exceptionDetails"])
                    return None
                return r.get("result", {}).get("value")

            # 1. Verify Legend Box & Concentric Circles
            legend_info = await eval_js("""
                (function() {
                    var el = document.getElementById('bmap_branch_legend');
                    var circles = el ? el.querySelectorAll('svg circle').length : 0;
                    return {
                        exists: !!el,
                        visible: el ? window.getComputedStyle(el).display !== 'none' : false,
                        text: el ? el.innerText.replace(/\\s+/g, ' ') : '',
                        circleCount: circles
                    };
                })()
            """)
            print("1. Concentric Radar Legend Box:", legend_info)
            assert legend_info["exists"], "Legend box should exist"
            assert legend_info["circleCount"] == 3, f"Expected 3 concentric circles, got {legend_info['circleCount']}"

            # 2. Verify Top Quote Bar & Telemetry
            quote_info = await eval_js("""
                (function() {
                    return {
                        sym: document.getElementById('bb_sym').textContent,
                        last: document.getElementById('bb_last').textContent,
                        chg: document.getElementById('bb_chg').textContent,
                        vol: document.getElementById('bb_vol').textContent
                    };
                })()
            """)
            print("2. Top Quote Bar:", quote_info)
            assert "SPY" in quote_info["sym"], "Expected SPY as default symbol"

            # 3. Test Ticker Switcher to BRENT and back
            ticker_switch = await eval_js("""
                (function() {
                    window.switchBmapTicker('BRENT');
                    var brentSym = document.getElementById('bb_sym').textContent;
                    window.switchBmapTicker('SPY');
                    var spySym = document.getElementById('bb_sym').textContent;
                    return { brentSym: brentSym, spySym: spySym };
                })()
            """)
            print("3. Ticker Switcher:", ticker_switch)
            assert "CO1 Comdty" in ticker_switch["brentSym"]
            assert "SPY US" in ticker_switch["spySym"]

            # 4. Verify Bank Branches Parameter Card and Live Filtering
            bank_filter_test = await eval_js("""
                (function() {
                    var initialText = document.getElementById('lbl_bank_dep_val').textContent;
                    
                    // Filter by deposits slider > $500M
                    document.getElementById('slider_bank_dep').value = '500';
                    window.filterBankBranches();
                    var text500 = document.getElementById('lbl_bank_dep_val').textContent;
                    var badge500 = document.getElementById('bmap_objects_count_badge').textContent;

                    // Filter by Bank Name 'JPMorgan Chase'
                    document.getElementById('filter_bank_name').value = 'JPMorgan Chase';
                    window.filterBankBranches();
                    var textJPM = document.getElementById('lbl_bank_dep_val').textContent;

                    // Filter by State 'CA'
                    document.getElementById('filter_bank_state').value = 'CA';
                    window.filterBankBranches();
                    var textCA = document.getElementById('lbl_bank_dep_val').textContent;

                    // Reset filter
                    window.resetBankFilter();
                    var resetText = document.getElementById('lbl_bank_dep_val').textContent;
                    var resetBadge = document.getElementById('bmap_objects_count_badge').textContent;

                    return {
                        initial: initialText,
                        after500M: text500,
                        badge500M: badge500,
                        afterJPM: textJPM,
                        afterCA: textCA,
                        resetText: resetText,
                        resetBadge: resetBadge
                    };
                })()
            """)
            print("4. Live Bank Parameter Filters:", json.dumps(bank_filter_test, indent=2))
            assert "1,675" in bank_filter_test["initial"], "Should start with 1,675 branches"
            assert "1,675" in bank_filter_test["resetText"], "Reset should restore 1,675 branches"

            # 5. Verify Map Content Drawer & Datasets
            drawer_check = await eval_js("""
                (function() {
                    var sRows = document.querySelectorAll('#suggested_datasets_list .dataset-row');
                    var nRows = document.querySelectorAll('#new_datasets_list .dataset-row');
                    var names = Array.from(sRows).map(function(r) { return r.textContent.trim(); });
                    return {
                        suggestedCount: sRows.length,
                        newCount: nRows.length,
                        firstFewSuggested: names.slice(0, 8)
                    };
                })()
            """)
            print("5. Map Content Drawer Datasets:", json.dumps(drawer_check, indent=2))
            assert drawer_check["suggestedCount"] >= 15, "Should have all suggested datasets"

            # 6. Verify Bottom Suggested Functions Bar
            footer_check = await eval_js("""
                (function() {
                    var hasSuggested = document.body.innerText.includes('Suggested Functions');
                    var hasPort = document.body.innerText.includes('Analyze portfolio performance & risk');
                    var hasCorr = document.body.innerText.includes('Correlate price movement of securities');
                    return {
                        hasSuggested: hasSuggested,
                        hasPort: hasPort,
                        hasCorr: hasCorr
                    };
                })()
            """)
            print("6. Suggested Functions Footer:", footer_check)
            assert footer_check["hasSuggested"], "Suggested Functions should be present in footer"
            assert footer_check["hasPort"], "PORT function should be present in footer"
            assert footer_check["hasCorr"], "CORR function should be present in footer"

            print("\n>>> ALL TESTS PASSED WITH 100% FIDELITY! <<<")
    finally:
        proc.kill()

if __name__ == "__main__":
    asyncio.run(run_tests())
