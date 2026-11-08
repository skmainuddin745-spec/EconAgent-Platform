const { spawn } = require('child_process');

const chrome = spawn('C:/Program Files/Google/Chrome/Application/chrome.exe', [
  '--headless=new', '--remote-debugging-port=9271', '--disable-gpu', '--no-sandbox', '--window-size=1600,1050', 'about:blank'
]);

setTimeout(async () => {
  try {
    const res = await fetch('http://127.0.0.1:9271/json');
    const [target] = await res.json();
    const ws = new WebSocket(target.webSocketDebuggerUrl);
    await new Promise(r => ws.addEventListener('open', r));
    let id = 1;
    const send = (m, p) => new Promise((resolve, reject) => {
      const cur = id++;
      const h = e => { const d = JSON.parse(e.data); if (d.id === cur) { ws.removeEventListener('message', h); resolve(d.result); } };
      ws.addEventListener('message', h);
      ws.send(JSON.stringify({ id: cur, method: m, params: p }));
    });
    await send('Page.navigate', { url: 'file:///F:/documents/SOIC/EconAgent_Platform/platform_ui/Bloomberg_BMAP_Terminal.html' });
    await new Promise(r => setTimeout(r, 3000));
    const info = await send('Runtime.evaluate', {
      expression: `Array.from(document.querySelectorAll('.leaflet-overlay-pane canvas')).map((c, i) => ({
        index: i,
        width: c.width,
        height: c.height,
        className: c.className,
        style: c.getAttribute('style'),
        owner: c._leaflet_id || 'no-id'
      }))`,
      returnByValue: true
    });
    console.log('Canvases in overlay-pane:', info.result.value);

    // Also check what elements exist under point [25.4, 46.5]
    const checkPoint = await send('Runtime.evaluate', {
      expression: `(() => {
        const map = window.leafletMap;
        const pt = map.latLngToContainerPoint([25.4, 46.5]);
        const el = document.elementFromPoint(pt.x, pt.y);
        return {
          pt: pt,
          elemTag: el ? el.tagName : null,
          elemId: el ? el.id : null,
          elemClass: el ? el.className : null
        };
      })()`,
      returnByValue: true
    });
    console.log('Element at Petroline [25.4, 46.5]:', checkPoint.result.value);

    ws.close();
    chrome.kill();
    process.exit(0);
  } catch (err) {
    console.error(err);
    chrome.kill();
    process.exit(1);
  }
}, 1200);

