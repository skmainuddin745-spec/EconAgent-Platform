const { spawn } = require('child_process');

const chrome = spawn('C:/Program Files/Google/Chrome/Application/chrome.exe', [
  '--headless=new', '--remote-debugging-port=9272', '--disable-gpu', '--no-sandbox', '--window-size=1600,1050', 'about:blank'
]);

setTimeout(async () => {
  try {
    const res = await fetch('http://127.0.0.1:9272/json');
    const [target] = await res.json();
    const ws = new WebSocket(target.webSocketDebuggerUrl);
    await new Promise(r => ws.addEventListener('open', r));
    let id = 1;
    const send = (m, p) => new Promise((resolve) => {
      const cur = id++;
      const h = e => { const d = JSON.parse(e.data); if (d.id === cur) { ws.removeEventListener('message', h); resolve(d.result); } };
      ws.addEventListener('message', h);
      ws.send(JSON.stringify({ id: cur, method: m, params: p }));
    });
    await send('Page.navigate', { url: 'file:///F:/documents/SOIC/EconAgent_Platform/platform_ui/Bloomberg_BMAP_Terminal.html' });
    await new Promise(r => setTimeout(r, 3000));
    
    const rectInfo = await send('Runtime.evaluate', {
      expression: `(() => {
        const map = window.leafletMap;
        const rect = map.getContainer().getBoundingClientRect();
        const pt = map.latLngToContainerPoint([25.4, 46.5]);
        const absX = rect.left + pt.x;
        const absY = rect.top + pt.y;
        const topEl = document.elementFromPoint(absX, absY);
        return {
          mapRect: { left: rect.left, top: rect.top, width: rect.width, height: rect.height },
          point: pt,
          absX, absY,
          topElTag: topEl ? topEl.tagName : null,
          topElId: topEl ? topEl.id : null,
          topElClass: topEl ? topEl.className : null
        };
      })()`,
      returnByValue: true
    });
    console.log('Rect & Hit Info:', JSON.stringify(rectInfo.result.value, null, 2));

    const absX = rectInfo.result.value.absX;
    const absY = rectInfo.result.value.absY;

    console.log(`Dispatching mouseMoved to (${absX}, ${absY})...`);
    await send('Input.dispatchMouseEvent', {
      type: 'mouseMoved',
      x: absX,
      y: absY
    });
    await new Promise(r => setTimeout(r, 600));

    const hoverResult = await send('Runtime.evaluate', {
      expression: `(() => {
        const pop = document.getElementById('bmap_universal_vessel_popup');
        return {
          display: pop ? pop.style.display : 'none',
          name: document.getElementById('uni_vessel_name') ? document.getElementById('uni_vessel_name').textContent : '',
          dest: document.getElementById('uni_vessel_dest') ? document.getElementById('uni_vessel_dest').textContent : '',
          status: document.getElementById('uni_vessel_status') ? document.getElementById('uni_vessel_status').textContent : '',
          currentAsset: window.currentActiveAsset ? window.currentActiveAsset.item.name : null
        };
      })()`,
      returnByValue: true
    });
    console.log('Hover result on Petroline:', JSON.stringify(hoverResult.result.value, null, 2));

    ws.close();
    chrome.kill();
    process.exit(0);
  } catch (err) {
    console.error(err);
    chrome.kill();
    process.exit(1);
  }
}, 1200);
