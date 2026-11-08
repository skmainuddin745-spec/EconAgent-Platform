const { spawn } = require('child_process');
const fs = require('fs');

const chrome = spawn('C:/Program Files/Google/Chrome/Application/chrome.exe', [
  '--headless=new', '--remote-debugging-port=9298', '--disable-gpu', '--no-sandbox', '--window-size=1600,1050', 'about:blank'
]);

setTimeout(async () => {
  try {
    let ws = null;
    for (let i = 0; i < 20; i++) {
      try {
        const res = await fetch('http://127.0.0.1:9298/json');
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
    await new Promise(r => setTimeout(r, 3500));

    // Show BMAP tab
    await send('Runtime.evaluate', {
      expression: `window.showTab(null, 'bmap');`
    });
    await new Promise(r => setTimeout(r, 1000));

    // Check initial center
    const initCenter = await send('Runtime.evaluate', {
      expression: `(() => {
        if (!window.leafletMap) return null;
        const c = window.leafletMap.getCenter();
        return { lat: c.lat, lng: c.lng, zoom: window.leafletMap.getZoom() };
      })()`,
      returnByValue: true
    });
    console.log('INITIAL_CENTER:', JSON.stringify(initCenter && initCenter.result ? initCenter.result.value : initCenter));

    // Click West button
    const clickRes = await send('Runtime.evaluate', {
      expression: `(() => {
        const btn = document.getElementById('btn_bmap_nav_west');
        if (!btn) return 'NO_BTN';
        btn.click();
        return 'CLICKED';
      })()`,
      returnByValue: true
    });
    console.log('CLICK_RES:', JSON.stringify(clickRes && clickRes.result ? clickRes.result.value : clickRes));

    // Wait 2s for flyTo animation
    await new Promise(r => setTimeout(r, 2000));

    const finalCenter = await send('Runtime.evaluate', {
      expression: `(() => {
        if (!window.leafletMap) return null;
        const c = window.leafletMap.getCenter();
        return { lat: c.lat, lng: c.lng, zoom: window.leafletMap.getZoom() };
      })()`,
      returnByValue: true
    });
    console.log('FINAL_CENTER_AFTER_WEST:', JSON.stringify(finalCenter && finalCenter.result ? finalCenter.result.value : finalCenter));

    const shot = await send('Page.captureScreenshot', { format: 'png' });
    fs.writeFileSync('C:/Users/SK/.gemini/antigravity/brain/49bcdc7d-9012-4831-93a6-42d8b11a6533/shot_nav_west_verified.png', Buffer.from(shot.data, 'base64'));
    console.log('SHOT_SAVED');

    ws.close();
    chrome.kill();
  } catch (err) {
    console.error('ERROR:', err);
    chrome.kill();
  }
}, 500);

