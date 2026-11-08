const { spawn } = require('child_process');

const chrome = spawn('C:/Program Files/Google/Chrome/Application/chrome.exe', [
  '--headless=new', '--remote-debugging-port=9290', '--disable-gpu', '--no-sandbox', '--window-size=1600,1050', 'about:blank'
]);

setTimeout(async () => {
  try {
    let ws = null;
    for (let i = 0; i < 15; i++) {
      try {
        const res = await fetch('http://127.0.0.1:9290/json');
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

    // Test loading Cesium from CDN
    await send('Page.navigate', { url: 'about:blank' });
    await new Promise(r => setTimeout(r, 1000));

    const loadRes = await send('Runtime.evaluate', {
      expression: `(async () => {
        return new Promise((resolve) => {
          const s = document.createElement('script');
          s.src = 'https://cesium.com/downloads/cesiumjs/releases/1.114/Build/Cesium/Cesium.js';
          s.onload = () => resolve({ loaded: true, hasCesium: typeof window.Cesium !== 'undefined' });
          s.onerror = (e) => resolve({ loaded: false, error: 'Failed to load script' });
          document.head.appendChild(s);
          setTimeout(() => resolve({ loaded: false, error: 'Timeout' }), 6000);
        });
      })()`,
      awaitPromise: true,
      returnByValue: true
    });

    console.log('Cesium CDN Load Result:', JSON.stringify(loadRes.result.value, null, 2));

    chrome.kill();
    process.exit(0);
  } catch (err) {
    console.error(err);
    chrome.kill();
    process.exit(1);
  }
}, 1500);

