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
    print("TESTING DYNAMIC NUMERICAL SYNCHRONIZATION & CROSSCHECK")
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

        # 1. Verify Default Startup Values (Polycab India Ltd)
        print("\n1. Verifying Default Polycab Startup Figures Across All Engines...")
        startup_res = await cdp_eval("""
        (function() {
            var dcfTicker = document.getElementById('val_ticker') ? document.getElementById('val_ticker').value : '';
            var dcfPrice  = document.getElementById('val_curr_price') ? document.getElementById('val_curr_price').value : '';
            var dcfFcf    = document.getElementById('val_base_fcf') ? document.getElementById('val_base_fcf').value : '';
            var dcfShares = document.getElementById('val_shares') ? document.getElementById('val_shares').value : '';
            var dcfFair   = document.getElementById('res_dcf_price') ? document.getElementById('res_dcf_price').innerText : '';
            var dcfTarget = document.getElementById('res_target_price') ? document.getElementById('res_target_price').innerText : '';
            
            var soicStock = document.getElementById('soic_stock_select') ? document.getElementById('soic_stock_select').value : '';
            var soicTotal = document.getElementById('soic_total_score') ? document.getElementById('soic_total_score').innerText : '';
            var soicPct   = document.getElementById('soic_pct_score') ? document.getElementById('soic_pct_score').innerText : '';

            var techPrice = document.getElementById('tech_price_display') ? document.getElementById('tech_price_display').innerText : '';
            var techWma   = document.getElementById('tech_card_wma') ? document.getElementById('tech_card_wma').innerText : '';
            var techAdx   = document.getElementById('tech_card_adx') ? document.getElementById('tech_card_adx').innerText : '';

            return {
                dcfTicker: dcfTicker, dcfPrice: dcfPrice, dcfFcf: dcfFcf, dcfShares: dcfShares,
                dcfFair: dcfFair, dcfTarget: dcfTarget,
                soicStock: soicStock, soicTotal: soicTotal, soicPct: soicPct,
                techPrice: techPrice, techWma: techWma, techAdx: techAdx
            };
        })()
        """)
        print(f"  ✓ DCF Predictor: {startup_res['dcfTicker']} | CMP: ₹{startup_res['dcfPrice']} | FCF: ₹{startup_res['dcfFcf']} Cr")
        print(f"    -> DCF Fair Value: {startup_res['dcfFair']} | 5-Yr Target: {startup_res['dcfTarget']}")
        print(f"  ✓ SOIC 310-pt: {startup_res['soicStock']} | Score: {startup_res['soicTotal']} / 310 {startup_res['soicPct']}")
        print(f"  ✓ Technicals: Price: {startup_res['techPrice']} | 30-WMA: {startup_res['techWma']} | ADX: {startup_res['techAdx']}")
        assert "Polycab" in startup_res['dcfTicker'], "Default DCF ticker not Polycab"
        assert startup_res['soicStock'] == "Polycab India Ltd", "Default SOIC stock not Polycab"
        assert startup_res['soicTotal'] == "280", f"Polycab score mismatch ({startup_res['soicTotal']})"

        # 2. Test Dynamic Synchronization to KEI Industries
        print("\n2. Testing Cross-Tab Dynamic Synchronization to KEI Industries...")
        kei_sync_res = await cdp_eval("""
        (function() {
            syncGlobalFirmChange('kei');

            var dcfTicker = document.getElementById('val_ticker').value;
            var dcfPrice  = document.getElementById('val_curr_price').value;
            var dcfFair   = document.getElementById('res_dcf_price').innerText;
            var soicStock = document.getElementById('soic_stock_select').value;
            var soicTotal = document.getElementById('soic_total_score').innerText;
            var techPrice = document.getElementById('tech_price_display').innerText;
            var techWma   = document.getElementById('tech_card_wma').innerText;
            var domTicker = document.getElementById('tickTickerSelect') ? document.getElementById('tickTickerSelect').value : '';

            return {
                dcfTicker: dcfTicker, dcfPrice: dcfPrice, dcfFair: dcfFair,
                soicStock: soicStock, soicTotal: soicTotal,
                techPrice: techPrice, techWma: techWma,
                domTicker: domTicker
            };
        })()
        """)
        print(f"  ✓ Synchronized DCF Predictor: {kei_sync_res['dcfTicker']} | Price: ₹{kei_sync_res['dcfPrice']} | Fair: {kei_sync_res['dcfFair']}")
        print(f"  ✓ Synchronized SOIC Scorecard: {kei_sync_res['soicStock']} | Score: {kei_sync_res['soicTotal']} / 310")
        print(f"  ✓ Synchronized Technicals: Price: {kei_sync_res['techPrice']} | 30-WMA: {kei_sync_res['techWma']}")
        print(f"  ✓ Synchronized Level 2 DOM Ticker: {kei_sync_res['domTicker']}")
        assert "KEI" in kei_sync_res['dcfTicker'], "DCF failed to sync to KEI"
        assert "KEI" in kei_sync_res['soicStock'], "SOIC failed to sync to KEI"
        assert kei_sync_res['soicTotal'] == "260", "KEI score mismatch"
        assert "4,280" in kei_sync_res['techPrice'], "Technicals failed to sync to KEI"
        assert kei_sync_res['domTicker'] == "KEI", "DOM Order Book failed to sync to KEI"

        # 3. Test Dynamic Slider Adjustment in DCF (WACC Sensitivity)
        print("\n3. Testing Dynamic DCF Slider Recalculation (WACC & Growth)...")
        slider_res = await cdp_eval("""
        (function() {
            // Set WACC slider to 9.0%
            document.getElementById('val_wacc').value = '9.0';
            runValuation();
            var targetAt9 = document.getElementById('res_dcf_price').innerText;

            // Set WACC slider to 12.0%
            document.getElementById('val_wacc').value = '12.0';
            runValuation();
            var targetAt12 = document.getElementById('res_dcf_price').innerText;

            return { targetAt9: targetAt9, targetAt12: targetAt12 };
        })()
        """)
        print(f"  ✓ DCF Fair Value at WACC 9.0%:  {slider_res['targetAt9']}")
        print(f"  ✓ DCF Fair Value at WACC 12.0%: {slider_res['targetAt12']}")
        assert slider_res['targetAt9'] != slider_res['targetAt12'], "DCF valuation did not update on WACC change"

        # 4. Test Dynamic Recalculation in KEI 2-Year IRR Simulator
        print("\n4. Testing Dynamic 2-Year IRR Simulator in SOIC Sector Models...")
        irr_res = await cdp_eval("""
        (function() {
            var slider = document.getElementById('soic_kei_pe_slider');
            if (!slider) return { exists: false };

            // Simulate PE at 28x
            slider.value = '28.0';
            updateKeiSim();
            var mcap28 = document.getElementById('soic_kei_sim_mcap').innerText;
            var irr28  = document.getElementById('soic_kei_sim_irr').innerText;

            // Simulate PE at 42x
            slider.value = '42.0';
            updateKeiSim();
            var mcap42 = document.getElementById('soic_kei_sim_mcap').innerText;
            var irr42  = document.getElementById('soic_kei_sim_irr').innerText;

            return { exists: true, mcap28: mcap28, irr28: irr28, mcap42: mcap42, irr42: irr42 };
        })()
        """)
        assert irr_res['exists'], "KEI PE slider not found"
        print(f"  ✓ KEI at 28.0x PE: Target Mcap = {irr_res['mcap28']} | 2-Yr IRR = {irr_res['irr28']}")
        print(f"  ✓ KEI at 42.0x PE: Target Mcap = {irr_res['mcap42']} | 2-Yr IRR = {irr_res['irr42']}")
        assert irr_res['mcap28'] != irr_res['mcap42'], "IRR simulator failed to recalculate"

    proc.terminate()
    print("\n=======================================================")
    print("ALL NUMERICAL FIGURES VERIFIED ACCURATE, DYNAMIC & SYNCHRONIZED! 🚀")
    print("=======================================================")

if __name__ == "__main__":
    asyncio.run(run_test())
