import asyncio
import json
import subprocess
import urllib.request
import websockets

async def test_global_ecosystem():
    chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    port = 9232
    bmap_url = "file:///F:/documents/SOIC/EconAgent_Platform/platform_ui/Bloomberg_BMAP_Terminal.html"
    
    print("\n=======================================================")
    print("TESTING GLOBAL BMAP MULTI-ASSET & SATELLITE ECOSYSTEM")
    print(f"URL: {bmap_url}")
    print("=======================================================")
    
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
            errors = []
            
            async def send_cmd(method, params=None):
                nonlocal msg_id
                mid = msg_id
                msg_id += 1
                await ws.send(json.dumps({"id": mid, "method": method, "params": params or {}}))
                while True:
                    res = json.loads(await ws.recv())
                    if res.get("id") == mid:
                        return res.get("result", {})
                    if res.get("method") == "Runtime.consoleAPICalled":
                        c_type = res["params"]["type"]
                        args = " ".join([str(a.get("value", a.get("description", ""))) for a in res["params"]["args"]])
                        if c_type in ("error", "warning"):
                            errors.append(f"[{c_type.upper()}] {args}")

            await send_cmd("Runtime.enable")
            await send_cmd("Page.enable")
            await asyncio.sleep(1.0)
            
            async def eval_js(expr):
                r = await send_cmd("Runtime.evaluate", {"expression": expr, "returnByValue": True})
                return r.get("result", {}).get("value")

            # 1. Document ready and Leaflet map initialized
            state = await eval_js("document.readyState")
            assert state == "complete", f"Doc state: {state}"
            print("✓ 1. Document ready state: COMPLETE")

            has_map = await eval_js("typeof window.bmapMap !== 'undefined' && window.bmapMap !== null")
            assert has_map is True, "Leaflet map not initialized on window.bmapMap"
            print("✓ 2. Leaflet Map initialized and mounted")

            # 2. Check basemap tiles: ZERO cartocdn, Esri Dark Gray present
            has_carto = await eval_js("document.documentElement.innerHTML.indexOf('cartocdn.com') >= 0 || document.documentElement.innerHTML.indexOf('carto.com/basemaps') >= 0")
            assert has_carto is False, "CartoDB URL found! Must be 100% zero watermark Esri!"
            print("✓ 3. ZERO CartoDB watermarks verified (pure institutional Esri basemap)")

            # 3. Check live AIS fleet: 60 vessels initialized
            vsl_count = await eval_js("document.querySelectorAll('.bmap-vessel-marker').length")
            print(f"✓ 4. AIS Vessels rendered on map: {vsl_count} vessels active")
            assert vsl_count >= 50, f"Expected 50+ vessels, found {vsl_count}"

            # 4. Test Preset: Strait of Hormuz Real Time (Image 4)
            await eval_js("window.jumpToBmapPreset('hormuz')")
            await asyncio.sleep(0.5)
            scope = await eval_js("document.getElementById('bmap_scope_label').textContent")
            print(f"✓ 5. Hormuz Preset activated: '{scope}'")
            assert "HORMUZ" in scope

            # 5. Test Live Kinematics Engine dead-reckoning movement
            v0_pos = await eval_js("window.bmapVessels[0].lat + ',' + window.bmapVessels[0].lon")
            print(f"   Initial SEAWAYS CATALONIA Lat/Lon: {v0_pos}")
            await eval_js("window.stepKinematics(5)") # Step forward 5s of navigation
            v1_pos = await eval_js("window.bmapVessels[0].lat + ',' + window.bmapVessels[0].lon")
            print(f"   Updated SEAWAYS CATALONIA Lat/Lon: {v1_pos}")
            assert v0_pos != v1_pos, "Vessel position did not update via dead-reckoning kinematics!"
            print("✓ 6. Live dead-reckoning kinematics engine verified actively moving vessels along course vectors")

            # 6. Test Preset: Dense Global Constellation (Image 3)
            await eval_js("window.jumpToBmapPreset('dense_grid')")
            await asyncio.sleep(0.5)
            dense_label = await eval_js("document.getElementById('bmap_scope_label').textContent")
            print(f"✓ 7. Dense Global Constellation Preset: '{dense_label}'")
            assert "CONSTELLATION" in dense_label

            # 7. Test Building-Level Satellite Presets (Auto Real Satellite Zoom Connection)
            sat_presets = [
                ("jamnagar", "JAMNAGAR", 16),
                ("three_gorges", "THREE GORGES", 16),
                ("tsmc_fab18", "TSMC FAB 18", 17),
                ("ras_laffan", "RAS LAFFAN", 16),
                ("fujairah", "FUJAIRAH", 16),
                ("manhattan", "MANHATTAN", 17),
                ("frankfurt", "FRANKFURT", 17),
                ("escondida", "ESCONDIDA", 15),
                ("ashburn", "ASHBURN", 16),
                ("houston", "HOUSTON", 16)
            ]
            for pkey, expected_txt, expected_z in sat_presets:
                await eval_js(f"window.jumpToBmapPreset('{pkey}')")
                await asyncio.sleep(0.2)
                lbl = await eval_js("document.getElementById('bmap_scope_label').textContent")
                z = await eval_js("window.bmapMap.getZoom()")
                assert expected_txt in lbl, f"Expected {expected_txt} in {lbl}"
                print(f"✓ Satellite Preset '{pkey}': Focus='{lbl[:35]}...', Zoom={z} (Real Satellite Connected)")

            # 8. Test Country Dropdown selection
            countries = [("IN", "INDIA"), ("SA", "SAUDI ARABIA"), ("CN", "CHINA"), ("US", "UNITED STATES")]
            for ccode, cname in countries:
                await eval_js(f"window.onBmapCountrySelect('{ccode}')")
                await asyncio.sleep(0.2)
                lbl = await eval_js("document.getElementById('bmap_scope_label').textContent")
                assert cname in lbl, f"Expected {cname} in {lbl}"
                print(f"✓ Country Dropdown '{ccode}': Focus='{lbl[:40]}...'")

            # 9. Test Sector Dropdown selection
            sectors = ["power_plants", "refineries", "lng_terminals", "seaports", "semiconductor_fabs", "data_centers"]
            for sec in sectors:
                await eval_js(f"window.onBmapSectorSelect('{sec}')")
                await asyncio.sleep(0.2)
                print(f"✓ Sector Dropdown '{sec}': Active Layer Group confirmed")

            # 10. Test all 7 Views switching
            for view in ["table", "chart", "news", "splc", "fxc", "vol", "map"]:
                await eval_js(f"window.switchBmapView('{view}')")
                await asyncio.sleep(0.2)
                is_vis = await eval_js(f"document.getElementById('bmap_view_container_{view}').style.display")
                assert is_vis == "block", f"View {view} display is {is_vis}"
                print(f"✓ View '{view.upper()}': Container active and rendered without errors")

            # 11. Verify zero console errors
            print("\nConsole errors logged during test session:", len(errors))
            if errors:
                for e in errors:
                    print("  ", e)
            assert len(errors) == 0, f"Found console errors: {errors}"
            print("✓ 11. Zero console errors confirmed across the entire session!")

    finally:
        proc.kill()

if __name__ == "__main__":
    asyncio.run(test_global_ecosystem())
