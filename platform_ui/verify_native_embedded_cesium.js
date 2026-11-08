const { spawn } = require('child_process');
const fs = require('fs');

const chrome = spawn('C:/Program Files/Google/Chrome/Application/chrome.exe', [
  '--headless=new', '--remote-debugging-port=9287', '--disable-gpu', '--no-sandbox', '--window-size=1600,1050', 'about:blank'
]);

setTimeout(async () => {
  try {
    let ws = null;
    for (let i = 0; i < 15; i++) {
      try {
        const res = await fetch('http://127.0.0.1:9287/json');
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

    if (!ws) {
      console.error('Cannot connect to Chrome');
      chrome.kill();
      process.exit(1);
    }

    const consoleLogs = [];
    const exceptions = [];

    ws.addEventListener('message', e => {
      const data = JSON.parse(e.data);
      if (data.method === 'Runtime.consoleAPICalled') {
        consoleLogs.push(data.params);
      }
      if (data.method === 'Runtime.exceptionThrown') {
        exceptions.push(data.params);
      }
    });

    let id = 1;
    const send = (m, p) => new Promise((resolve) => {
      const cur = id++;
      const h = e => { const d = JSON.parse(e.data); if (d.id === cur) { ws.removeEventListener('message', h); resolve(d.result); } };
      ws.addEventListener('message', h);
      ws.send(JSON.stringify({ id: cur, method: m, params: p }));
    });

    await send('Runtime.enable');
    await send('Page.enable');

    console.log('Navigating to EconAgent_Dashboard.html...');
    await send('Page.navigate', { url: 'file:///F:/documents/SOIC/EconAgent_Platform/platform_ui/EconAgent_Dashboard.html' });
    await new Promise(r => setTimeout(r, 3500));

    console.log('Switching to GEV Native Cesium 3D view...');
    await send('Runtime.evaluate', {
      expression: `(() => {
        showTab(null, 'bmap');
        switchBmapView('gev');
      })()`
    });

    // Wait 2.5 seconds for Cesium to initialize
    await new Promise(r => setTimeout(r, 2500));

    const checkRes = await send('Runtime.evaluate', {
      expression: `(() => {
        const container = document.getElementById('gev_native_cesium_container');
        const statusPill = document.getElementById('gev_server_status_pill');
        const viewer = window.nativeCesiumViewer;

        return {
          containerFound: !!container,
          containerWidth: container ? container.offsetWidth : 0,
          containerHeight: container ? container.offsetHeight : 0,
          statusText: statusPill ? statusPill.innerText : null,
          viewerInitialized: !!viewer,
          sceneMode: viewer ? viewer.scene.mode : null,
          entitiesCount: viewer ? viewer.entities.values.length : 0,
          hasFallbackBox: !!document.getElementById('gev_fallback_box')
        };
      })()`,
      returnByValue: true
    });

    console.log('Native Cesium 3D View State:', JSON.stringify(checkRes.result.value, null, 2));

    // Test Camera jump to East (Hormuz)
    await send('Runtime.evaluate', {
      expression: `flyCesiumTo('east');`
    });
    await new Promise(r => setTimeout(r, 2000));

    const shot = await send('Page.captureScreenshot', { format: 'png' });
    fs.writeFileSync('C:/Users/SK/.gemini/antigravity/brain/49bcdc7d-9012-4831-93a6-42d8b11a6533/shot_verified_native_cesium_3d_final.png', Buffer.from(shot.data, 'base64'));
    console.log('Saved shot_verified_native_cesium_3d_final.png');

    console.log(`Total exceptions: ${exceptions.length}`);
    exceptions.forEach(ex => console.log('EX:', ex.exceptionDetails.text, ex.exceptionDetails.exception?.description));

    chrome.kill();
    process.exit(0);
  } catch (err) {
    console.error(err);
    chrome.kill();
    process.exit(1);
  }
}, 1500);

