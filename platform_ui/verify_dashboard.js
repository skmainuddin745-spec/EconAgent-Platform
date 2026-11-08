const { spawn } = require('child_process');
const fs = require('fs');

const chromePath = 'C:/Program Files/Google/Chrome/Application/chrome.exe';
const targetUrl = 'file:///F:/documents/SOIC/EconAgent_Platform/platform_ui/EconAgent_Dashboard.html#bmap';
const port = 9298;

const chrome = spawn(chromePath, [
  '--headless=new',
  `--remote-debugging-port=${port}`,
  '--disable-gpu',
  '--no-sandbox',
  '--window-size=1600,1050',
  'about:blank'
]);

let msgId = 1;
function sendCdp(ws, method, params = {}) {
  return new Promise((resolve, reject) => {
    const id = msgId++;
    const handler = (event) => {
      const data = JSON.parse(event.data);
      if (data.id === id) {
        ws.removeEventListener('message', handler);
        if (data.error) reject(data.error);
        else resolve(data.result);
      }
    };
    ws.addEventListener('message', handler);
    ws.send(JSON.stringify({ id, method, params }));
  });
}

function evaluate(ws, expression) {
  return sendCdp(ws, 'Runtime.evaluate', {
    expression,
    returnByValue: true,
    awaitPromise: true
  }).then(r => r.result ? r.result.value : r);
}

function sleep(ms) {
  return new Promise(r => setTimeout(r, ms));
}

async function run() {
  let ws = null;
  for (let i = 0; i < 15; i++) {
    try {
      const res = await fetch(`http://127.0.0.1:${port}/json`);
      if (res.ok) {
        const pages = await res.json();
        ws = new WebSocket(pages[0].webSocketDebuggerUrl);
        await new Promise(r => ws.addEventListener('open', r));
        break;
      }
    } catch (e) {
      await sleep(300);
    }
  }

  if (!ws) throw new Error('Could not connect to Chrome debugging port');

  await sendCdp(ws, 'Page.enable');
  await sendCdp(ws, 'Page.navigate', { url: targetUrl });
  await sleep(4000);

  console.log('=== Verifying EconAgent_Dashboard.html BMAP & GEV Integration ===');
  const dashDiag = await evaluate(ws, `(() => {
    const map = window.leafletMap;
    const renderer = window.masterCanvasRenderer;
    const canvs = document.querySelectorAll('.leaflet-overlay-pane canvas');
    return {
      hasMap: !!map,
      canvases: canvs.length,
      tolerance: renderer ? renderer.options.tolerance : null,
      activeTab: document.querySelector('.tab.active') ? document.querySelector('.tab.active').textContent.trim() : null
    };
  })()`);
  console.log('Dashboard BMAP diagnostic:', JSON.stringify(dashDiag, null, 2));

  // Hover over Petroline in master dashboard
  const pipePos = await evaluate(ws, `(() => {
    const map = window.leafletMap;
    const pt = map.latLngToContainerPoint([25.4, 46.5]);
    const rect = map.getContainer().getBoundingClientRect();
    return { absX: rect.left + pt.x, absY: rect.top + pt.y };
  })()`);

  await sendCdp(ws, 'Input.dispatchMouseEvent', {
    type: 'mouseMoved',
    x: pipePos.absX,
    y: pipePos.absY
  });
  await sleep(600);

  const shotDash = await sendCdp(ws, 'Page.captureScreenshot', { format: 'png' });
  fs.writeFileSync('C:/Users/SK/.gemini/antigravity/brain/49bcdc7d-9012-4831-93a6-42d8b11a6533/shot_master_dashboard_bmap_petroline_verified.png', Buffer.from(shotDash.data, 'base64'));
  console.log('Saved shot_master_dashboard_bmap_petroline_verified.png');

  // Switch to GEV 3D tab
  await evaluate(ws, `window.switchBmapView('gev')`);
  await sleep(3500);

  const shotGev = await sendCdp(ws, 'Page.captureScreenshot', { format: 'png' });
  fs.writeFileSync('C:/Users/SK/.gemini/antigravity/brain/49bcdc7d-9012-4831-93a6-42d8b11a6533/shot_master_dashboard_gev_3d_verified.png', Buffer.from(shotGev.data, 'base64'));
  console.log('Saved shot_master_dashboard_gev_3d_verified.png');

  ws.close();
  chrome.kill();
  console.log('Dashboard verification complete!');
  process.exit(0);
}

run().catch(err => {
  console.error('Failed:', err);
  chrome.kill();
  process.exit(1);
});

