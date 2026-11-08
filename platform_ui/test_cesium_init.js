const { spawn } = require('child_process');

const chrome = spawn('C:/Program Files/Google/Chrome/Application/chrome.exe', [
  '--headless=new', '--remote-debugging-port=9289', '--disable-gpu', '--no-sandbox', '--window-size=1600,1050', 'about:blank'
]);

setTimeout(async () => {
  try {
    let ws = null;
    for (let i = 0; i < 15; i++) {
      try {
        const res = await fetch('http://127.0.0.1:9289/json');
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

    await send('Page.navigate', { url: 'about:blank' });
    await new Promise(r => setTimeout(r, 1000));

    const testRes = await send('Runtime.evaluate', {
      expression: `(async () => {
        // Load Cesium CSS and JS
        const link = document.createElement('link');
        link.rel = 'stylesheet';
        link.href = 'https://cesium.com/downloads/cesiumjs/releases/1.114/Build/Cesium/Widgets/widgets.css';
        document.head.appendChild(link);

        await new Promise((resolve) => {
          const s = document.createElement('script');
          s.src = 'https://cesium.com/downloads/cesiumjs/releases/1.114/Build/Cesium/Cesium.js';
          s.onload = resolve;
          document.head.appendChild(s);
        });

        // Create container div
        const div = document.createElement('div');
        div.id = 'cesium_test_container';
        div.style.width = '800px';
        div.style.height = '600px';
        document.body.appendChild(div);

        try {
          // Initialize viewer with offline/OSM imagery so it never fails on ion token
          const viewer = new Cesium.Viewer('cesium_test_container', {
            baseLayerPicker: false,
            geocoder: false,
            homeButton: false,
            infoBox: false,
            sceneModePicker: false,
            selectionIndicator: false,
            timeline: false,
            animation: false,
            navigationHelpButton: false,
            baseLayer: new Cesium.ImageryLayer(new Cesium.OpenStreetMapImageryProvider({
              url: 'https://tile.openstreetmap.org/'
            }))
          });

          return {
            viewerCreated: !!viewer,
            sceneMode: viewer.scene.mode,
            canvasWidth: viewer.canvas.width,
            canvasHeight: viewer.canvas.height
          };
        } catch(e) {
          return { error: e.message, stack: e.stack };
        }
      })()`,
      awaitPromise: true,
      returnByValue: true
    });

    console.log('Cesium Viewer Init Result:', JSON.stringify(testRes.result.value, null, 2));

    chrome.kill();
    process.exit(0);
  } catch (err) {
    console.error(err);
    chrome.kill();
    process.exit(1);
  }
}, 1500);

