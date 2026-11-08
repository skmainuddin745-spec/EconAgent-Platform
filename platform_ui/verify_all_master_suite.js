const { spawn } = require('child_process');
const fs = require('fs');

const chrome = spawn('C:/Program Files/Google/Chrome/Application/chrome.exe', [
  '--headless=new', '--remote-debugging-port=9290', '--disable-gpu', '--no-sandbox', '--window-size=1600,1050', 'about:blank'
]);

setTimeout(async () => {
  try {
    let ws = null;
    for (let i = 0; i < 20; i++) {
      try {
        const res = await fetch('http://127.0.0.1:9290/json');
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

    const consoleLogs = [];
    const errors = [];
    ws.addEventListener('message', e => {
      const d = JSON.parse(e.data);
      if (d.method === 'Runtime.consoleAPICalled') {
        const text = d.params.args.map(a => a.value || JSON.stringify(a)).join(' ');
        consoleLogs.push('[' + d.params.type + '] ' + text);
        if (d.params.type === 'error') errors.push(text);
      }
      if (d.method === 'Runtime.exceptionThrown') {
        const ex = JSON.stringify(d.params.exceptionDetails);
        errors.push(ex);
        consoleLogs.push('[EXCEPTION] ' + ex);
      }
    });

    await send('Runtime.enable');
    await send('Page.enable');
    await send('Page.navigate', { url: 'file:///F:/documents/SOIC/EconAgent_Platform/platform_ui/EconAgent_Dashboard.html' });
    await new Promise(r => setTimeout(r, 3500));

    console.log('=== 1. VERIFYING GLOBAL TOP DROPDOWNS INITIAL STATE ===');
    const initDropdowns = await send('Runtime.evaluate', {
      expression: `(() => {
        const cSel = document.getElementById('global_country_select');
        const sSel = document.getElementById('global_sector_select');
        const fSel = document.getElementById('global_firm_select');
        return {
          country: cSel ? cSel.value : null,
          sectorCount: sSel ? sSel.options.length : 0,
          sectorSelected: sSel ? sSel.value : null,
          firmCount: fSel ? fSel.options.length : 0,
          firms: fSel ? Array.from(fSel.options).map(o => o.text) : []
        };
      })()`,
      returnByValue: true
    });
    console.log('INIT_DROPDOWNS:', JSON.stringify(initDropdowns && initDropdowns.result ? initDropdowns.result.value : initDropdowns, null, 2));

    console.log('=== 2. SWITCHING COUNTRY TO US (WALL STREET TITANS) ===');
    const usDropdowns = await send('Runtime.evaluate', {
      expression: `(() => {
        const cSel = document.getElementById('global_country_select');
        if (cSel) {
          cSel.value = 'us';
          syncGlobalCountryChange('us');
        }
        const sSel = document.getElementById('global_sector_select');
        const fSel = document.getElementById('global_firm_select');
        return {
          country: cSel ? cSel.value : null,
          sectorSelected: sSel ? sSel.value : null,
          firmCount: fSel ? fSel.options.length : 0,
          firms: fSel ? Array.from(fSel.options).map(o => o.text) : [],
          activeTechStock: document.getElementById('tech_stock_select') ? document.getElementById('tech_stock_select').value : null
        };
      })()`,
      returnByValue: true
    });
    console.log('US_DROPDOWNS:', JSON.stringify(usDropdowns && usDropdowns.result ? usDropdowns.result.value : usDropdowns, null, 2));

    // Capture screenshot of Wall Street top bar
    const shotTop = await send('Page.captureScreenshot', { format: 'png' });
    fs.writeFileSync('C:/Users/SK/.gemini/antigravity/brain/49bcdc7d-9012-4831-93a6-42d8b11a6533/shot_verified_wallstreet_dropdowns.png', Buffer.from(shotTop.data, 'base64'));

    console.log('=== 3. VERIFYING REAL-TIME TECHNICALS TAB (NVDA) ===');
    const techCheck = await send('Runtime.evaluate', {
      expression: `(() => {
        window.showTab(null, 'technicals');
        const price = document.getElementById('tech_price_display') ? document.getElementById('tech_price_display').innerText : null;
        const stage = document.getElementById('tech_stage_display') ? document.getElementById('tech_stage_display').innerText : null;
        const ma30 = document.getElementById('tech_ma30_display') ? document.getElementById('tech_ma30_display').innerText : null;
        return { price, stage, ma30 };
      })()`,
      returnByValue: true
    });
    console.log('TECH_CHECK:', JSON.stringify(techCheck && techCheck.result ? techCheck.result.value : techCheck, null, 2));

    const shotTech = await send('Page.captureScreenshot', { format: 'png' });
    fs.writeFileSync('C:/Users/SK/.gemini/antigravity/brain/49bcdc7d-9012-4831-93a6-42d8b11a6533/shot_verified_technicals_nvda.png', Buffer.from(shotTech.data, 'base64'));

    console.log('=== 4. VERIFYING 2D BMAP WEST (NORTH AMERICA) NAVIGATION ===');
    await send('Runtime.evaluate', {
      expression: `(() => {
        window.showTab(null, 'bmap');
        window.bmapNavigateWest();
      })()`
    });
    await new Promise(r => setTimeout(r, 2000));

    const westCheck = await send('Runtime.evaluate', {
      expression: `(() => {
        const c = window.leafletMap.getCenter();
        const z = window.leafletMap.getZoom();
        return { lat: c.lat, lng: c.lng, zoom: z };
      })()`,
      returnByValue: true
    });
    console.log('WEST_CHECK:', JSON.stringify(westCheck && westCheck.result ? westCheck.result.value : westCheck));

    console.log('=== 5. VERIFYING NATIVE 3D CESIUM WORKSTATION ===');
    await send('Runtime.evaluate', {
      expression: `window.switchBmapView('gev');`
    });
    await new Promise(r => setTimeout(r, 3000));

    const gevCheck = await send('Runtime.evaluate', {
      expression: `(() => {
        const gevCont = document.getElementById('gev_native_cesium_container');
        const tb2d = document.getElementById('bmap_2d_secondary_toolbar');
        const offlineBox = document.getElementById('gev_offline_box');
        return {
          tb2dDisplay: tb2d ? window.getComputedStyle(tb2d).display : null,
          gevContDisplay: gevCont ? window.getComputedStyle(gevCont).display : null,
          gevHeight: gevCont ? gevCont.clientHeight : 0,
          hasViewer: typeof window.nativeCesiumViewer !== 'undefined' && window.nativeCesiumViewer !== null,
          sceneMode: window.nativeCesiumViewer && window.nativeCesiumViewer.scene ? window.nativeCesiumViewer.scene.mode : null,
          entities: window.nativeCesiumViewer && window.nativeCesiumViewer.entities ? window.nativeCesiumViewer.entities.values.length : 0,
          hasOfflineBox: !!offlineBox
        };
      })()`,
      returnByValue: true
    });
    console.log('GEV_CHECK:', JSON.stringify(gevCheck && gevCheck.result ? gevCheck.result.value : gevCheck, null, 2));

    const shotGev = await send('Page.captureScreenshot', { format: 'png' });
    fs.writeFileSync('C:/Users/SK/.gemini/antigravity/brain/49bcdc7d-9012-4831-93a6-42d8b11a6533/shot_verified_cesium_3d_master.png', Buffer.from(shotGev.data, 'base64'));

    console.log('=== 6. RETURN TO 2D BMAP ===');
    await send('Runtime.evaluate', {
      expression: `window.switchBmapView('map');`
    });
    await new Promise(r => setTimeout(r, 1000));

    const returnCheck = await send('Runtime.evaluate', {
      expression: `(() => {
        const tb2d = document.getElementById('bmap_2d_secondary_toolbar');
        const mapCont = document.getElementById('bmap_view_container_map');
        return {
          tb2dDisplay: tb2d ? window.getComputedStyle(tb2d).display : null,
          mapContDisplay: mapCont ? window.getComputedStyle(mapCont).display : null
        };
      })()`,
      returnByValue: true
    });
    console.log('RETURN_CHECK:', JSON.stringify(returnCheck && returnCheck.result ? returnCheck.result.value : returnCheck, null, 2));

    console.log('TOTAL_CONSOLE_ERRORS:', errors.length);
    if (errors.length > 0) {
      console.log('ERRORS:\n', errors.join('\n'));
    }

    ws.close();
    chrome.kill();
    console.log('ALL_VERIFICATIONS_COMPLETE');
  } catch (err) {
    console.error('VERIFY_ERROR:', err);
    chrome.kill();
  }
}, 500);

