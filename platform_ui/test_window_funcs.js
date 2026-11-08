const { spawn } = require('child_process');
const fs = require('fs');

const chrome = spawn('C:/Program Files/Google/Chrome/Application/chrome.exe', [
  '--headless=new', '--remote-debugging-port=9279', '--disable-gpu', '--no-sandbox', '--window-size=1600,1050', 'about:blank'
]);

setTimeout(async () => {
  try {
    let ws = null;
    for (let i = 0; i < 15; i++) {
      try {
        const res = await fetch('http://127.0.0.1:9279/json');
        if (res.ok) {
          const pages = await res.json();
          ws = new WebSocket(pages[0].webSocketDebuggerUrl);
          await new Promise(r => ws.addEventListener('open', r));
          break;
        }
      } catch (e) {
        await new Promise(r => setTimeout(r, 300));
      }
    }

    let id = 1;
    const send = (m, p) => new Promise((resolve) => {
      const cur = id++;
      const h = e => { const d = JSON.parse(e.data); if (d.id === cur) { ws.removeEventListener('message', h); resolve(d.result); } };
      ws.addEventListener('message', h);
      ws.send(JSON.stringify({ id: cur, method: m, params: p }));
    });

    await send('Runtime.enable');
    await send('Page.enable');

    await send('Page.navigate', { url: 'file:///F:/documents/SOIC/EconAgent_Platform/platform_ui/EconAgent_Dashboard.html' });
    await new Promise(r => setTimeout(r, 3000));

    // 1. Show BMAP and switch to GEV
    await send('Runtime.evaluate', {
      expression: `(() => {
        window.showTab(null, 'bmap');
        window.switchBmapView('gev');
      })()`
    });

    // 2. Wait 2 seconds for Cesium viewer to initialize and add entities
    await new Promise(r => setTimeout(r, 2000));

    const res = await send('Runtime.evaluate', {
      expression: `(() => {
        const v = window.nativeCesiumViewer;
        return {
          hasViewer: !!v,
          sceneMode: v ? v.scene.mode : null,
          canvasWidth: v ? v.canvas.width : 0,
          canvasHeight: v ? v.canvas.height : 0,
          entitiesCount: v ? v.entities.values.length : 0,
          statusText: document.getElementById('gev_server_status_pill')?.innerText,
          containerDisplay: window.getComputedStyle(document.getElementById('bmap_view_container_gev')).display
        };
      })()`,
      returnByValue: true
    });

    console.log('Cesium 3D Initialization Result:', JSON.stringify(res.result.value, null, 2));

    // 3. Capture full screenshot of Native Cesium 3D Workstation
    const shot = await send('Page.captureScreenshot', { format: 'png' });
    fs.writeFileSync('C:/Users/SK/.gemini/antigravity/brain/49bcdc7d-9012-4831-93a6-42d8b11a6533/shot_verified_native_cesium_3d_master.png', Buffer.from(shot.data, 'base64'));
    console.log('Saved shot_verified_native_cesium_3d_master.png');

    chrome.kill();
    process.exit(0);
  } catch (err) {
    console.error(err);
    chrome.kill();
    process.exit(1);
  }
}, 1500);
