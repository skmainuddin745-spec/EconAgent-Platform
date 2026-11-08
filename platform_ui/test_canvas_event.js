const { spawn } = require('child_process');

const chrome = spawn('C:/Program Files/Google/Chrome/Application/chrome.exe', [
  '--headless=new', '--remote-debugging-port=9286', '--disable-gpu', '--no-sandbox', '--window-size=1600,1050', 'about:blank'
]);

setTimeout(async () => {
  try {
    let ws = null;
    for (let i = 0; i < 10; i++) {
      try {
        const res = await fetch('http://127.0.0.1:9286/json');
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

    await send('Page.navigate', { url: 'file:///F:/documents/SOIC/EconAgent_Platform/platform_ui/Bloomberg_BMAP_Terminal.html' });
    await new Promise(r => setTimeout(r, 3000));

    const result = await send('Runtime.evaluate', {
      expression: `(() => {
        try {
          return {
            hasBmap: !!window.leafletMap,
            hasDlg: !!window.datasetLayerGroups,
            dlgKeys: Object.keys(window.datasetLayerGroups || {}),
            crudeGrp: !!(window.datasetLayerGroups && window.datasetLayerGroups['crude_pipelines'])
          };
        } catch (e) {
          return { error: e.message };
        }
      })()`,
      returnByValue: true
    });

    console.log('Direct Layer Event Result:', JSON.stringify(result.result.value, null, 2));

    ws.close();
    chrome.kill();
    process.exit(0);
  } catch (err) {
    console.error(err);
    chrome.kill();
    process.exit(1);
  }
}, 1200);
