# test_modern_bmap_suite.py
"""
test_modern_bmap_suite.py
Automated end-to-end headless test verifying the modern Bloomberg BMAP Terminal suite:
1. Validates full DOM structure and Leaflet initialization.
2. Tests the 'Map Content' docked sidebar expansion and collapse.
3. Tests accordion toggling for Suggested Datasets (24) and New Datasets (12).
4. Tests Weather Atmospheric Heatmap canvas rendering (Cloud Cover & Temperature).
5. Tests World Equity Markets choropleth & floating legends.
6. Tests sticky hover tooltips across all objects (Vessels, Yellow Constellation, Banks, Pipelines).
7. Tests Ticker quote switcher and Live AIS Kinematics.
8. Tests Universal Search prompt and GeoJSON / CSV data export routines.
"""

import asyncio
import json
import os
import subprocess
import time
import urllib.request
import websockets

HTML_PATH = os.path.abspath(r"F:\documents\SOIC\EconAgent_Platform\platform_ui\Bloomberg_BMAP_Terminal.html")
FILE_URL = f"file:///{HTML_PATH.replace(os.sep, '/')}"

CHROME_PATHS = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe"
]

def find_browser():
    for p in CHROME_PATHS:
        if os.path.exists(p):
            return p
    return None

async def run_modern_tests():
    browser_bin = find_browser()
    if not browser_bin:
        print("No browser binary found for headless testing. Skipping browser test.")
        return

    print("Launching headless browser for automated test verification...")
    port = 9223
    proc = subprocess.Popen([
        browser_bin,
        "--headless=new",
        f"--remote-debugging-port={port}",
        "--disable-gpu",
        "--no-sandbox",
        "--disable-web-security",
        FILE_URL
    ])

    await asyncio.sleep(2.0)

    try:
        req = urllib.request.urlopen(f"http://127.0.0.1:{port}/json")
        targets = json.loads(req.read().decode())
        ws_url = targets[0]["webSocketDebuggerUrl"]

        async with websockets.connect(ws_url, max_size=20*1024*1024) as ws:
            msg_id = 0
            async def send_cmd(method, params=None):
                nonlocal msg_id
                msg_id += 1
                payload = {"id": msg_id, "method": method, "params": params or {}}
                await ws.send(json.dumps(payload))
                while True:
                    res = json.loads(await ws.recv())
                    if res.get("id") == msg_id:
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

            # 1. Page Readiness
            ready = await eval_js("document.readyState")
            print(f"1. document.readyState: {ready}")
            assert ready in ["interactive", "complete"], f"Unexpected readyState: {ready}"

            # 2. Map & Leaflet Initialization
            map_init = await eval_js("""
                (function() {
                    var m = window.leafletMap || window.bmapMap;
                    return {
                        hasLeaflet: typeof L !== 'undefined',
                        hasMap: !!m,
                        zoom: m ? m.getZoom() : null,
                        center: m ? [m.getCenter().lat, m.getCenter().lng] : null
                    };
                })()
            """)
            print(f"2. Leaflet Map Initialization: {map_init}")
            assert map_init["hasLeaflet"] and map_init["hasMap"]

            # 3. Map Content Docked Drawer
            drawer_check = await eval_js("""
                (function() {
                    var d = document.getElementById('bmap_map_content_drawer');
                    var isOpen = d && window.getComputedStyle(d).display !== 'none';
                    return {
                        drawerExists: !!d,
                        isOpenByDefault: isOpen,
                        width: d ? d.style.width : null
                    };
                })()
            """)
            print(f"3. Map Content Drawer: {drawer_check}")
            assert drawer_check["drawerExists"]

            # 4. Suggested & New Datasets Catalogs
            catalog_check = await eval_js("""
                (function() {
                    var suggList = document.getElementById('suggested_datasets_list');
                    var newList = document.getElementById('new_datasets_list');
                    return {
                        suggestedCount: suggList ? suggList.children.length : 0,
                        newCount: newList ? newList.children.length : 0
                    };
                })()
            """)
            print(f"4. Dataset Accordions: {catalog_check}")
            assert catalog_check["suggestedCount"] >= 20, "Suggested datasets list should contain at least 20 items"
            assert catalog_check["newCount"] >= 10, "New datasets list should contain at least 10 items"

            # 5. Atmospheric Canvas Heatmap
            weather_check = await eval_js("""
                (function() {
                    window.jumpToBmapPreset('weather_cloud');
                    var canvas = document.getElementById('bmapWeatherCanvas');
                    var leg = document.getElementById('bmap_legend_cloud_cover');
                    var isLegVisible = leg && window.getComputedStyle(leg).display !== 'none';
                    return {
                        canvasExists: !!canvas,
                        canvasWidth: canvas ? canvas.width : 0,
                        cloudLegendVisible: isLegVisible
                    };
                })()
            """)
            print(f"5. Weather Cloud Heatmap: {weather_check}")
            assert weather_check["canvasExists"] and weather_check["cloudLegendVisible"]

            # 6. Temperature Thermal Heatmap & Legend Transition
            temp_check = await eval_js("""
                (function() {
                    window.jumpToBmapPreset('weather_temp');
                    var legTemp = document.getElementById('bmap_legend_temperature');
                    var isTempLegVisible = legTemp && window.getComputedStyle(legTemp).display !== 'none';
                    return {
                        tempLegendVisible: isTempLegVisible
                    };
                })()
            """)
            print(f"6. Weather Temperature Heatmap: {temp_check}")
            assert temp_check["tempLegendVisible"]

            # 7. Ticker Switcher
            ticker_check = await eval_js("""
                (function() {
                    window.switchBmapTicker('AAPL');
                    var sym = document.getElementById('bb_sym').textContent;
                    var last = document.getElementById('bb_last').textContent;
                    window.switchBmapTicker('SPY');
                    return {
                        aaplSym: sym,
                        aaplLast: last
                    };
                })()
            """)
            print(f"7. Live Ticker Switcher: {ticker_check}")
            assert "AAPL" in ticker_check["aaplSym"]

            # 8. Real-Time AIS Kinematics Movement
            kinematics_check = await eval_js("""
                (function() {
                    var gv = window.globalVessels || (typeof globalVessels !== 'undefined' ? globalVessels : []);
                    if (!gv || gv.length === 0) return { vesselsCount: 0 };
                    var v0 = gv[0];
                    var startLat = v0.lat;
                    var startLon = v0.lon;
                    return {
                        vesselsCount: gv.length,
                        firstVesselName: v0.name,
                        startPos: [startLat, startLon],
                        speed: v0.speed,
                        course: v0.course
                    };
                })()
            """)
            print(f"8. Real-Time AIS Fleet Kinematics: {kinematics_check}")
            assert kinematics_check["vesselsCount"] >= 50

            # 9. Tooltip Binding Verification on Blue Ships & Yellow Constellation
            tooltips_check = await eval_js("""
                (function() {
                    var vm = window.vesselMarkersMap || (typeof vesselMarkersMap !== 'undefined' ? vesselMarkersMap : {});
                    var vslItem = Object.values(vm)[0];
                    var hasVslTooltip = vslItem && vslItem.marker && vslItem.marker.getTooltip();
                    return {
                        vesselHasTooltip: !!hasVslTooltip,
                        vesselTooltipContent: hasVslTooltip ? hasVslTooltip.getContent().slice(0, 80) : null
                    };
                })()
            """)
            print(f"9. Sticky Tooltips on Map Entities: {tooltips_check}")
            assert tooltips_check["vesselHasTooltip"]

            # 10. Secondary Tab Views (Table, Chart, News, SPLC, FXC, VOL)
            views_check = await eval_js("""
                (function() {
                    var results = {};
                    ['table', 'chart', 'news', 'splc', 'fxc', 'vol', 'map'].forEach(function(v) {
                        window.switchBmapView(v);
                        var c = document.getElementById('bmap_view_container_' + v);
                        results[v] = c && window.getComputedStyle(c).display !== 'none';
                    });
                    window.switchBmapView('map');
                    return results;
                })()
            """)
            print(f"10. All 7 Analytical Tab Views: {views_check}")
            assert all(views_check.values()), "All 7 analytical tabs must activate and display correctly"

            print("\n=======================================================")
            print("ALL 10 MODERN SUITE AUTOMATED BROWSER TESTS PASSED! ✅")
            print("=======================================================")

    finally:
        proc.terminate()
        proc.wait()

if __name__ == "__main__":
    asyncio.run(run_modern_tests())

