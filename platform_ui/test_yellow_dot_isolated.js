const { spawn } = require('child_process');

const chrome = spawn('C:/Program Files/Google/Chrome/Application/chrome.exe', [
  '--headless=new', '--remote-debugging-port=9295', '--disable-gpu', '--no-sandbox', '--window-size=1600,1050', 'about:blank'
]);

setTimeout(async () => {
  try {
    let ws = null;
    for (let i = 0; i < 15; i++) {
      try {
        const res = await fetch('http://127.0.0.1:9295/json');
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

    await send('Page.enable');
    await send('Page.navigate', { url: 'file:///F:/documents/SOIC/EconAgent_Platform/platform_ui/Bloomberg_BMAP_Terminal.html' });
    await new Promise(r => setTimeout(r, 3500));

    // Find a power plant in UAE or Qatar (away from Petroline)
    const dotInfo = await send('Runtime.evaluate', {
      expression: `(() => {
        const map = window.leafletMap;
        // Barakah Nuclear / Taweelah Power Plant or a power plant in UAE/Qatar
        const util = window.globalUtilities.find(u => u.country === 'UAE' || u.country === 'Qatar') || window.globalUtilities[0];
        const pt = map.latLngToContainerPoint([util.lat, util.lon]);
        const rect = map.getContainer().getBoundingClientRect();
        return {
          name: util.name,
          country: util.country,
          capacity: util.capacity,
          type: util.type,
          absX: rect.left + pt.x,
          absY: rect.top + pt.y
        };
      })()`,
      returnByValue: true
    });
    console.log('Testing Yellow Dot (Power Utility):', dotInfo.result.value);

    const tx = dotInfo.result.value.absX;
    const ty = dotInfo.result.value.absY;

    await send('Input.dispatchMouseEvent', {
      type: 'mouseMoved',
      x: tx,
      y: ty
    });
    await new Promise(r => setTimeout(r, 600));

    const hoverState = await send('Runtime.evaluate', {
      expression: `(() => {
        const pop = document.getElementById('bmap_universal_vessel_popup');
        return {
          display: pop ? pop.style.display : 'none',
          name: document.getElementById('uni_vessel_name') ? document.getElementById('uni_vessel_name').textContent : '',
          type: document.getElementById('uni_vessel_type') ? document.getElementById('uni_vessel_type').textContent : '',
          dest: document.getElementById('uni_vessel_dest') ? document.getElementById('uni_vessel_dest').textContent : '',
          status: document.getElementById('uni_vessel_status') ? document.getElementById('uni_vessel_status').textContent : '',
          borderCol: pop ? pop.style.borderColor : ''
        };
      })()`,
      returnByValue: true
    });
    console.log('Yellow Dot Hover Result:', JSON.stringify(hoverState.result.value, null, 2));

    ws.close();
    chrome.kill();
    process.exit(0);
  } catch (err) {
    console.error(err);
    chrome.kill();
    process.exit(1);
  }
}, 1200);

