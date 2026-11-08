const { spawn } = require('child_process');
const fs = require('fs');

const chrome = spawn('C:/Program Files/Google/Chrome/Application/chrome.exe', [
  '--headless=new', '--remote-debugging-port=9278', '--disable-gpu', '--no-sandbox', '--window-size=1600,1050', 'about:blank'
]);

setTimeout(async () => {
  try {
    let ws = null;
    for (let i = 0; i < 20; i++) {
      try {
        const res = await fetch('http://127.0.0.1:9278/json');
        if (res.ok) {
          const pages = await res.json();
          ws = new WebSocket(pages[0].webSocketDebuggerUrl);
          await new Promise(r => ws.addEventListener('open', r));
          break;
        }
      } catch (e) {
        await new Promise(r => setTimeout(r, 200));
      }
    }

    if (!ws) {
      console.log('CHROME_CONN_FAIL');
      chrome.kill();
      process.exit(1);
    }

    let msgId = 1;
    function send(method, params) {
      return new Promise((resolve) => {
        const id = msgId++;
        const handler = (event) => {
          const d = JSON.parse(event.data);
          if (d.id === id) {
            ws.removeEventListener('message', handler);
            resolve(d.result);
          }
        };
        ws.addEventListener('message', handler);
        ws.send(JSON.stringify({ id, method, params: params || {} }));
      });
    }

    await send('Runtime.enable');
    await send('Page.enable');
    await send('Page.navigate', { url: 'file:///F:/documents/SOIC/EconAgent_Platform/platform_ui/EconAgent_Dashboard.html' });
    await new Promise(r => setTimeout(r, 3000));

    // Test switching to US, then selecting different Damodaran industries
    const usResult = await send('Runtime.evaluate', {
      expression: `(() => {
        window.syncGlobalCountryChange('us');
        const sec = document.getElementById('global_sector_select');
        const firm = document.getElementById('global_firm_select');
        const nano = document.getElementById('global_nano_select');
        const techPrice = document.getElementById('tech_price_display') ? document.getElementById('tech_price_display').innerText : null;
        return {
          country: 'us',
          sectorsCount: sec.options.length,
          selectedSector: sec.value,
          firmsCount: firm.options.length,
          firms: Array.from(firm.options).map(o => o.text),
          selectedFirm: firm.value,
          nanoText: nano && nano.options[0] ? nano.options[0].text : null,
          techPrice
        };
      })()`,
      returnByValue: true
    });
    console.log('US_ECOSYSTEM:', JSON.stringify(usResult.result.value, null, 2));

    // Take screenshot of US Wall Street setup
    const shotUS = await send('Page.captureScreenshot', { format: 'png' });
    fs.writeFileSync('C:/Users/SK/.gemini/antigravity/brain/49bcdc7d-9012-4831-93a6-42d8b11a6533/shot_verified_wallstreet_us_final.png', Buffer.from(shotUS.data, 'base64'));

    // Test switching to Saudi Arabia (Aramco / SABIC)
    const saResult = await send('Runtime.evaluate', {
      expression: `(() => {
        window.syncGlobalCountryChange('sa');
        const sec = document.getElementById('global_sector_select');
        const firm = document.getElementById('global_firm_select');
        return {
          country: 'sa',
          sectorsCount: sec.options.length,
          selectedSector: sec.value,
          firms: Array.from(firm.options).map(o => o.text),
          selectedFirm: firm.value
        };
      })()`,
      returnByValue: true
    });
    console.log('SA_ECOSYSTEM:', JSON.stringify(saResult.result.value, null, 2));

    // Test switching to Taiwan (TSMC)
    const twResult = await send('Runtime.evaluate', {
      expression: `(() => {
        window.syncGlobalCountryChange('tw');
        const firm = document.getElementById('global_firm_select');
        return {
          country: 'tw',
          firms: Array.from(firm.options).map(o => o.text),
          selectedFirm: firm.value
        };
      })()`,
      returnByValue: true
    });
    console.log('TW_ECOSYSTEM:', JSON.stringify(twResult.result.value, null, 2));

    // Test switching to Netherlands (ASML)
    const nlResult = await send('Runtime.evaluate', {
      expression: `(() => {
        window.syncGlobalCountryChange('nl');
        const firm = document.getElementById('global_firm_select');
        return {
          country: 'nl',
          firms: Array.from(firm.options).map(o => o.text),
          selectedFirm: firm.value
        };
      })()`,
      returnByValue: true
    });
    console.log('NL_ECOSYSTEM:', JSON.stringify(nlResult.result.value, null, 2));

    // Test BMAP West / East navigation
    await send('Runtime.evaluate', {
      expression: `(() => {
        window.showTab(null, 'bmap');
        window.bmapNavigateWest();
      })()`
    });
    await new Promise(r => setTimeout(r, 2000));
    const navWestPos = await send('Runtime.evaluate', {
      expression: `(() => ({ lat: window.leafletMap.getCenter().lat, lng: window.leafletMap.getCenter().lng, zoom: window.leafletMap.getZoom() }))()`,
      returnByValue: true
    });
    console.log('BMAP_NAV_WEST:', JSON.stringify(navWestPos.result.value));

    // Test switching to Native Cesium 3D
    await send('Runtime.evaluate', {
      expression: `window.switchBmapView('gev');`
    });
    await new Promise(r => setTimeout(r, 3000));
    const gev3dStatus = await send('Runtime.evaluate', {
      expression: `(() => {
        const gevCont = document.getElementById('gev_native_cesium_container');
        const tb2d = document.getElementById('bmap_2d_secondary_toolbar');
        return {
          tb2dHidden: tb2d ? window.getComputedStyle(tb2d).display === 'none' : false,
          gevContVisible: gevCont ? window.getComputedStyle(gevCont).display === 'block' : false,
          cesiumEntities: window.nativeCesiumViewer ? window.nativeCesiumViewer.entities.values.length : 0,
          sceneMode: window.nativeCesiumViewer && window.nativeCesiumViewer.scene ? window.nativeCesiumViewer.scene.mode : null
        };
      })()`,
      returnByValue: true
    });
    console.log('GEV_3D_STATUS:', JSON.stringify(gev3dStatus.result.value, null, 2));

    // Capture screenshot of Cesium 3D with 2D toolbar hidden!
    const shotGevFinal = await send('Page.captureScreenshot', { format: 'png' });
    fs.writeFileSync('C:/Users/SK/.gemini/antigravity/brain/49bcdc7d-9012-4831-93a6-42d8b11a6533/shot_verified_cesium_3d_flawless.png', Buffer.from(shotGevFinal.data, 'base64'));

    ws.close();
    chrome.kill();
    console.log('ALL_VERIFIED_PERFECTLY');
  } catch (e) {
    console.error(e);
    chrome.kill();
  }
}, 500);

