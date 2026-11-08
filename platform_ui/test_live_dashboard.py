import asyncio
import json
import os
import subprocess
import time
import urllib.request
import websockets

async def run_cdp_test():
    chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    port = 9222
    html_url = "file:///F:/documents/SOIC/EconAgent_Platform/platform_ui/EconAgent_Dashboard.html"

    proc = subprocess.Popen([
        chrome_path,
        "--headless=new",
        f"--remote-debugging-port={port}",
        "--disable-gpu",
        "--no-sandbox",
        "--allow-file-access-from-files",
        html_url
    ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    try:
        ws_url = None
        for _ in range(25):
            try:
                with urllib.request.urlopen(f"http://127.0.0.1:{port}/json") as resp:
                    tabs = json.loads(resp.read().decode())
                    if tabs:
                        ws_url = tabs[0]["webSocketDebuggerUrl"]
                        break
            except Exception:
                await asyncio.sleep(0.3)

        if not ws_url:
            print("FAILED to connect to Chrome debugging port")
            return False

        print(f"Connected to Chrome CDP: {ws_url}")

        async with websockets.connect(ws_url, max_size=50_000_000) as ws:
            msg_id = 1
            console_errors = []

            async def send_cmd(method, params=None):
                nonlocal msg_id
                mid = msg_id
                msg_id += 1
                payload = {"id": mid, "method": method, "params": params or {}}
                await ws.send(json.dumps(payload))
                while True:
                    res = json.loads(await ws.recv())
                    if res.get("id") == mid:
                        return res.get("result", {})
                    if res.get("method") == "Runtime.consoleAPICalled":
                        c_type = res["params"]["type"]
                        args = " ".join([str(a.get("value", a.get("description", ""))) for a in res["params"]["args"]])
                        if c_type in ("error", "warning"):
                            console_errors.append(f"[{c_type.upper()}] {args}")
                            print(f"CONSOLE {c_type.upper()}: {args}")

            await send_cmd("Runtime.enable")
            await send_cmd("Page.enable")

            await asyncio.sleep(2.0)

            async def eval_js(expr):
                r = await send_cmd("Runtime.evaluate", {"expression": expr, "returnByValue": True})
                if "exceptionDetails" in r:
                    print(f"JS EXCEPTION in '{expr[:60]}...':", r["exceptionDetails"])
                    return None
                return r.get("result", {}).get("value")

            print("\n--- 1. Testing Document Readiness ---")
            ready = await eval_js("document.readyState")
            print("document.readyState:", ready)

            print("\n--- 2. Testing Dropdown Elements ---")
            elements = await eval_js("""
                ({
                    globalCountry: !!document.getElementById('global_country_select'),
                    globalSector: !!document.getElementById('global_sector_select'),
                    globalFirm: !!document.getElementById('global_firm_select'),
                    globalNano: !!document.getElementById('global_nano_select'),
                    zoomCountry: !!document.getElementById('zoom_country_select'),
                    zoomSector: !!document.getElementById('zoom_sector_select'),
                    zoomFirm: !!document.getElementById('zoom_firm_select'),
                    zoomNano: !!document.getElementById('zoom_nano_select')
                })
            """)
            print("Dropdown elements found:", elements)

            print("\n--- 3. Testing Synchronized Dropdown Cascading ---")
            # Switch to India -> edu_in (Education) -> mps (MPS Ltd)
            test_res = await eval_js("""
                (function() {
                    window.onCountryDropdownChange('india');
                    window.onSectorDropdownChange('edu_in');
                    var gf = document.getElementById('global_firm_select');
                    var firms = gf ? Array.from(gf.options).map(o => o.value) : [];
                    window.onFirmDropdownChange('mps');
                    var gn = document.getElementById('global_nano_select');
                    var nanos = gn ? Array.from(gn.options).map(o => o.value) : [];
                    return {
                        country: window.getCurrentZoomState().country,
                        sector: window.getCurrentZoomState().sector,
                        firm: window.getCurrentZoomState().firm,
                        firmsUnderEdu: firms,
                        nanosUnderMPS: nanos
                    };
                })()
            """)
            print("India -> Education -> MPS cascade result:", test_res)

            # Switch to India -> cables_in (Cables & Wires) -> polycab (Polycab India)
            test_cables = await eval_js("""
                (function() {
                    window.onSectorDropdownChange('cables_in');
                    window.onFirmDropdownChange('polycab');
                    var gf = document.getElementById('global_firm_select');
                    var firms = gf ? Array.from(gf.options).map(o => o.value) : [];
                    return {
                        sector: window.getCurrentZoomState().sector,
                        firm: window.getCurrentZoomState().firm,
                        firmsUnderCables: firms
                    };
                })()
            """)
            print("India -> Cables -> Polycab cascade result:", test_cables)

            # Switch to US -> edu_us (US Education) -> stride (Stride Inc)
            test_us_edu = await eval_js("""
                (function() {
                    window.onCountryDropdownChange('us');
                    window.onSectorDropdownChange('edu_us');
                    window.onFirmDropdownChange('stride');
                    var gf = document.getElementById('global_firm_select');
                    var firms = gf ? Array.from(gf.options).map(o => o.value) : [];
                    return {
                        country: window.getCurrentZoomState().country,
                        sector: window.getCurrentZoomState().sector,
                        firm: window.getCurrentZoomState().firm,
                        firmsUnderUsEdu: firms
                    };
                })()
            """)
            print("US -> US Education -> Stride cascade result:", test_us_edu)

            print("\n--- 4. Testing Interactive SOIC Technical Rulebook Sandbox ---")
            tech_res = await eval_js("""
                (function() {
                    window.onCountryDropdownChange('india');
                    window.onSectorDropdownChange('cables_in');
                    window.onFirmDropdownChange('polycab');
                    
                    var initialScore = document.getElementById('dyn_tech_score') ? document.getElementById('dyn_tech_score').textContent : 'none';
                    
                    if (typeof adjustTechParam === 'function') {
                        adjustTechParam('adx', 10, '20-40 (Trend Forming)');
                    }
                    var afterAdx10 = document.getElementById('dyn_tech_score') ? document.getElementById('dyn_tech_score').textContent : 'none';
                    
                    if (typeof adjustTechParam === 'function') {
                        adjustTechParam('rsi', 0, '<50 (Bearish / Weak Momentum)');
                    }
                    var afterRsi0 = document.getElementById('dyn_tech_score') ? document.getElementById('dyn_tech_score').textContent : 'none';
                    
                    if (typeof resetTechScores === 'function') {
                        resetTechScores();
                    }
                    var afterReset = document.getElementById('dyn_tech_score') ? document.getElementById('dyn_tech_score').textContent : 'none';
                    
                    return {
                        initialScore: initialScore,
                        afterAdx10: afterAdx10,
                        afterRsi0: afterRsi0,
                        afterReset: afterReset
                    };
                })()
            """)
            print("Interactive Technical Sandbox result:", tech_res)

            print("\n--- 5. Testing Interactive DCF Sensitivity Calculator ---")
            dcf_res = await eval_js("""
                (function() {
                    var waccSlider = document.getElementById('slider_dcf_wacc');
                    var gSlider = document.getElementById('slider_dcf_g');
                    var marginSlider = document.getElementById('slider_dcf_margin');
                    
                    var targetBefore = document.getElementById('val_dcf_target') ? document.getElementById('val_dcf_target').textContent : 'none';
                    var mosBefore = document.getElementById('val_dcf_mos') ? document.getElementById('val_dcf_mos').textContent : 'none';
                    
                    if (waccSlider && typeof updateInteractiveDCF === 'function') {
                        waccSlider.value = '14.5';
                        updateInteractiveDCF();
                    }
                    var targetAfterHigherWacc = document.getElementById('val_dcf_target') ? document.getElementById('val_dcf_target').textContent : 'none';
                    var mosAfterHigherWacc = document.getElementById('val_dcf_mos') ? document.getElementById('val_dcf_mos').textContent : 'none';
                    
                    if (waccSlider && typeof updateInteractiveDCF === 'function') {
                        waccSlider.value = '8.5';
                        updateInteractiveDCF();
                    }
                    var targetAfterLowerWacc = document.getElementById('val_dcf_target') ? document.getElementById('val_dcf_target').textContent : 'none';
                    var mosAfterLowerWacc = document.getElementById('val_dcf_mos') ? document.getElementById('val_dcf_mos').textContent : 'none';
                    
                    return {
                        targetBefore: targetBefore,
                        mosBefore: mosBefore,
                        targetAfterHigherWacc: targetAfterHigherWacc,
                        mosAfterHigherWacc: mosAfterHigherWacc,
                        targetAfterLowerWacc: targetAfterLowerWacc,
                        mosAfterLowerWacc: mosAfterLowerWacc
                    };
                })()
            """)
            print("Interactive DCF Sliders result:", dcf_res)

            print("\n--- 6. Testing Level 2 DOM Block Trade Execution Simulator ---")
            dom_res = await eval_js("""
                (function() {
                    // Activate DOM Nano Asset
                    window.onNanoDropdownChange('dom');
                    
                    var ofiBefore = document.getElementById('dom_ofi') ? document.getElementById('dom_ofi').textContent : 'none';
                    var kyleBefore = document.getElementById('dom_kyle') ? document.getElementById('dom_kyle').textContent : 'none';
                    
                    if (typeof injectDomBlockOrder === 'function') {
                        injectDomBlockOrder('BUY', 10000);
                    }
                    
                    var ofiAfterBuy = document.getElementById('dom_ofi') ? document.getElementById('dom_ofi').textContent : 'none';
                    var kyleAfterBuy = document.getElementById('dom_kyle') ? document.getElementById('dom_kyle').textContent : 'none';
                    
                    if (typeof injectDomBlockOrder === 'function') {
                        injectDomBlockOrder('SELL', 10000);
                    }
                    
                    var ofiAfterSell = document.getElementById('dom_ofi') ? document.getElementById('dom_ofi').textContent : 'none';
                    var kyleAfterSell = document.getElementById('dom_kyle') ? document.getElementById('dom_kyle').textContent : 'none';
                    
                    return {
                        ofiBefore: ofiBefore,
                        kyleBefore: kyleBefore,
                        ofiAfterBuy: ofiAfterBuy,
                        kyleAfterBuy: kyleAfterBuy,
                        ofiAfterSell: ofiAfterSell,
                        kyleAfterSell: kyleAfterSell
                    };
                })()
            """)
            print("Level 2 DOM Block Trade result:", dom_res)

            print("\n--- 7. Testing All 23 Bloomberg Tabs Navigation & Clickability ---")
            tabs_to_test = [
                'zoom', 'bmap', 'predictor', 'scen', 'soic', 'rot', 'vol', 'flows',
                'titans', 'soic_sectors', 'topnotch', 'macro', 'beta', 'margins', 'multiples',
                'growth', 'capstruct', 'workcap', 'taxrate', 'fundamentals', 'agents', 'papers', 'arch'
            ]
            tab_results = {}
            for t in tabs_to_test:
                res = await eval_js(f"""
                    (function() {{
                        try {{
                            showTab(null, '{t}');
                            var c = document.getElementById('{t}');
                            var isActive = c ? c.classList.contains('active') : false;
                            return {{ success: true, active: isActive }};
                        }} catch (e) {{
                            return {{ success: false, error: e.message }};
                        }}
                    }})()
                """)
                tab_results[t] = res
            print("All 23 Tabs navigation results:")
            all_tabs_ok = True
            for t, res in tab_results.items():
                ok = res.get('success') and res.get('active')
                if not ok: all_tabs_ok = False
                print(f"  Tab {t}: {'OK' if ok else 'FAIL'}")
            print(f"ALL 23 TABS FUNCTIONING: {all_tabs_ok}")

            print("\n--- 8. Testing Quick Jump Buttons ---")
            jump_res = await eval_js("""
                (function() {
                    try {
                        jumpToTabForActiveFirm('soic');
                        var soicActive = document.getElementById('soic').classList.contains('active');
                        jumpToTabForActiveFirm('predictor');
                        var dcfActive = document.getElementById('predictor').classList.contains('active');
                        jumpToTabForActiveFirm('zoom');
                        var zoomActive = document.getElementById('zoom').classList.contains('active');
                        jumpToTabForActiveFirm('bmap');
                        var bmapActive = document.getElementById('bmap').classList.contains('active');
                        return { soicActive: soicActive, dcfActive: dcfActive, zoomActive: zoomActive, bmapActive: bmapActive };
                    } catch (e) {
                        return { error: e.message };
                    }
                })()
            """)
            print("Quick Jump Buttons result:", jump_res)

            print("\n=== SUMMARY OF CONSOLE ERRORS ===")
            print(f"Total console errors/warnings: {len(console_errors)}")
            for ce in console_errors:
                print("  ", ce)

    finally:
        proc.kill()

if __name__ == "__main__":
    asyncio.run(run_cdp_test())
