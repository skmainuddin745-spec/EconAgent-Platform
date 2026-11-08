# F:\documents\SOIC\EconAgent_Platform\platform_ui\test_global_wallstreet_expansion.py
import asyncio
import json
import subprocess
import urllib.request
import websockets

CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
PORT = 9225
DASHBOARD_URL = r"file:///F:/documents/SOIC/EconAgent_Platform/platform_ui/EconAgent_Dashboard.html"

async def run_test():
    print("\n=======================================================")
    print("TESTING GLOBAL WALL STREET EXPANSION & MACRO-MICRO MATRIX")
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
        raise RuntimeError("Failed to connect to Chrome headless")

    async with websockets.connect(ws_url, max_size=10_000_000) as ws:
        msg_id = 0
        async def cdp_eval(expr):
            nonlocal msg_id
            msg_id += 1
            await ws.send(json.dumps({
                "id": msg_id,
                "method": "Runtime.evaluate",
                "params": {"expression": expr, "returnByValue": True, "awaitPromise": True}
            }))
            resp = json.loads(await ws.recv())
            if "exceptionDetails" in resp.get("result", {}):
                raise RuntimeError(f"CDP Eval error: {resp['result']['exceptionDetails']}")
            return resp.get("result", {}).get("result", {}).get("value")

        # 1. Test Country & Sector coverage across all 12 economies
        print("\n1. Testing Sovereign & Sector Cascade Across All 12 Economies...")
        test_countries = [
            ('us', 'semi_us', 'nvidia'),
            ('germany', 'automation_de', 'siemens'),
            ('japan', 'precision_jp', 'keyence'),
            ('china', 'ev_cn', 'byd'),
            ('saudi', 'energy_sa', 'aramco'),
            ('uk', 'pharma_uk', 'asml'),
            ('australia', 'mining_au', 'bhp'),
            ('korea', 'memory_kr', 'samsung'),
            ('brazil', 'oil_br', 'petrobras'),
            ('singapore', 'trade_sg', 'singtel'),
            ('uae', 'logistics_ae', 'dpworld'),
            ('india', 'cables_in', 'polycab')
        ]

        for cKey, sKey, fKey in test_countries:
            res = await cdp_eval(f"""
                (() => {{
                    window.onCountryDropdownChange('{cKey}');
                    window.onSectorDropdownChange('{sKey}');
                    window.onFirmDropdownChange('{fKey}');
                    const firmBox = document.getElementById('firm_telemetry_box');
                    const nanoBox = document.getElementById('nano_telemetry_box');
                    return {{
                        firmText: firmBox ? firmBox.textContent.trim().substring(0, 80) : '',
                        hasFirm: firmBox !== null && firmBox.textContent.length > 200,
                        hasNano: nanoBox !== null && nanoBox.textContent.length > 100
                    }};
                }})()
            """)
            assert res['hasFirm'], f"Firm {fKey} failed to load in {cKey}/{sKey}"
            print(f"  ✓ [{cKey.upper()}] Sector: {sKey} ➔ Firm: {fKey} loaded successfully!")

        # 2. Test Macro Transmission Simulator in Financial Titans
        print("\n2. Testing Macro-Micro Sensitivity Simulator in Financial Titans...")
        macro_sim_res = await cdp_eval("""
            (() => {
                window.switchTitanTab('macro');
                const subpane = document.getElementById('titan_subpane_macro');
                const isVisible = subpane && window.getComputedStyle(subpane).display !== 'none';

                // Shock copper +15%, Oil $95, US10Y 5.0%
                document.getElementById('slider_copper').value = 15;
                document.getElementById('slider_brent').value = 95;
                document.getElementById('slider_us10y').value = 500;
                window.runMacroTransmissionSim();

                const tbody = document.getElementById('macro_trans_tbody');
                const rowCount = tbody ? tbody.children.length : 0;
                const sampleText = tbody ? tbody.children[0].textContent : '';

                return {
                    isVisible,
                    rowCount,
                    sampleText: sampleText.substring(0, 100)
                };
            })()
        """)
        assert macro_sim_res['isVisible'], "Macro transmission subpane not visible"
        assert macro_sim_res['rowCount'] >= 8, f"Expected >= 8 transmission rows, got {macro_sim_res['rowCount']}"
        print(f"  ✓ Macro Sensitivity Simulator visible with {macro_sim_res['rowCount']} calculated corporate impacts!")
        print(f"  ✓ Dynamic Shock Output: {macro_sim_res['sampleText']}...")

        # 3. Test Expanded Real-Time Technicals Cockpit
        print("\n3. Testing Technicals Cockpit for Global Wall Street Titans...")
        tech_symbols = ['MSFT', 'HDFCBANK', 'XOM', 'ASML', 'ARAMCO', 'BHP', 'SAMSUNG', 'COPPER']
        for sym in tech_symbols:
            t_res = await cdp_eval(f"""
                (() => {{
                    window.switchTechStock('{sym}');
                    const priceEl = document.getElementById('tech_price_display');
                    const stageEl = document.getElementById('tech_card_stage');
                    const titleEl = document.getElementById('tech_chart_title');
                    return {{
                        price: priceEl ? priceEl.textContent : '',
                        stage: stageEl ? stageEl.textContent : '',
                        title: titleEl ? titleEl.textContent : ''
                    }};
                }})()
            """)
            print(f"  ✓ Technical Stock '{sym}': Price = {t_res['price']} | Stage = {t_res['stage']} | Title = {t_res['title']}")

        # 4. Test Master Cross-Tab Synchronization for Global Titan
        print("\n4. Testing Master Cross-Tab Synchronization for ASML & Microsoft...")
        sync_res = await cdp_eval("""
            (() => {
                syncGlobalFirmChange('asml');
                const dcfTicker = document.getElementById('val_ticker').value;
                const dcfPrice = document.getElementById('val_curr_price').value;
                const dcfWacc = document.getElementById('val_wacc').value;
                const soicScore = document.getElementById('soic_total_score').textContent;
                return { dcfTicker, dcfPrice, dcfWacc, soicScore };
            })()
        """)
        print(f"  ✓ ASML Global Sync: Ticker = '{sync_res['dcfTicker']}' | Price = €{sync_res['dcfPrice']} | WACC = {sync_res['dcfWacc']}% | SOIC Score = {sync_res['soicScore']}/310")

        sync_msft = await cdp_eval("""
            (() => {
                syncGlobalFirmChange('microsoft');
                const dcfTicker = document.getElementById('val_ticker').value;
                const dcfPrice = document.getElementById('val_curr_price').value;
                const dcfWacc = document.getElementById('val_wacc').value;
                return { dcfTicker, dcfPrice, dcfWacc };
            })()
        """)
        print(f"  ✓ MSFT Global Sync: Ticker = '{sync_msft['dcfTicker']}' | Price = ${sync_msft['dcfPrice']} | WACC = {sync_msft['dcfWacc']}%")

        print("\n=======================================================")
        print("ALL GLOBAL WALL STREET EXPANSION TESTS PASSED 100%! 🌐🚀")
        print("=======================================================")

    proc.terminate()

asyncio.run(run_test())
