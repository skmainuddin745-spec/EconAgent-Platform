const { spawn } = require('child_process');
const fs = require('fs');

const chromePath = 'C:/Program Files/Google/Chrome/Application/chrome.exe';
const targetUrl = 'file:///F:/documents/SOIC/EconAgent_Platform/platform_ui/Bloomberg_BMAP_Terminal.html';
const port = 9265;

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
  });
}

async function run() {
  await new Promise(r => setTimeout(r, 1500));
  const res = await fetch(`http://127.0.0.1:${port}/json`);
  const targets = await res.json();
  const pageTarget = targets.find(t => t.type === 'page');

  const ws = new WebSocket(pageTarget.webSocketDebuggerUrl);
  await new Promise(r => ws.addEventListener('open', r));

  await sendCdp(ws, 'Page.enable');
  await sendCdp(ws, 'Runtime.enable');

  await sendCdp(ws, 'Page.navigate', { url: targetUrl });
  await new Promise(r => setTimeout(r, 4000));

  console.log('=== TEST 1: Canvas Unification Check ===');
  const canvasCheck = await evaluate(ws, `
    (() => {
      const canvases = Array.from(document.querySelectorAll('.leaflet-overlay-pane canvas'));
      const renderer = window.masterCanvasRenderer;
      return {
        canvasCount: canvases.length,
        tolerance: renderer ? renderer.options.tolerance : null,
        hasMaster: !!window.masterCanvasRenderer
      };
    })()
  `);
  console.log('Canvas check result:', JSON.stringify(canvasCheck.result.value, null, 2));

  console.log('\n=== TEST 2: Petroline Blue Line Mouse Hover Test ===');
  const pipePos = await evaluate(ws, `
    (() => {
      const pipe = window.crudePipelines.find(p => p.id === 'pipe_petroline');
      const midCoord = pipe.coords[Math.floor(pipe.coords.length / 2)];
      const map = window.leafletMap;
      const pt = map.latLngToContainerPoint(midCoord);
      const containerRect = map.getContainer().getBoundingClientRect();
      return {
        screenX: containerRect.left + pt.x,
        screenY: containerRect.top + pt.y,
        coord: midCoord,
        pipeName: pipe.name
      };
    })()
  `);
  console.log('Petroline target position:', pipePos.result.value);

  // Dispatch real mouse move
  const px = pipePos.result.value.screenX;
  const py = pipePos.result.value.screenY;
  await sendCdp(ws, 'Input.dispatchMouseEvent', {
    type: 'mouseMoved',
    x: px,
    y: py
  });
  await new Promise(r => setTimeout(r, 600));

  const pipeHoverState = await evaluate(ws, `
    (() => {
      const pop = document.getElementById('bmap_universal_vessel_popup');
      return {
        display: pop ? pop.style.display : 'none',
        name: document.getElementById('uni_vessel_name') ? document.getElementById('uni_vessel_name').textContent : '',
        status: document.getElementById('uni_vessel_status') ? document.getElementById('uni_vessel_status').textContent : '',
        dest: document.getElementById('uni_vessel_dest') ? document.getElementById('uni_vessel_dest').textContent : '',
        owner: document.getElementById('uni_vessel_owner') ? document.getElementById('uni_vessel_owner').textContent : ''
      };
    })()
  `);
  console.log('Petroline hover result:', JSON.stringify(pipeHoverState.result.value, null, 2));

  // Take screenshot of Petroline hover
  const shot1 = await sendCdp(ws, 'Page.captureScreenshot', { format: 'png' });
  fs.writeFileSync('C:/Users/SK/.gemini/antigravity/brain/49bcdc7d-9012-4831-93a6-42d8b11a6533/shot_verified_petroline_hover.png', Buffer.from(shot1.data, 'base64'));
  console.log('Saved shot_verified_petroline_hover.png');

  console.log('\n=== TEST 3: Yellow Dot (Power Utility / Grid Node) Mouse Hover Test ===');
  const yellowDotPos = await evaluate(ws, `
    (() => {
      // Find a power plant near Middle East / visible area
      const pwr = window.datasetLayerGroups && window.datasetLayerGroups['power_plants'];
      // Let's use globalUtilities[0]
      const map = window.leafletMap;
      // Or let's hover over Jubail Petrochemical or Riyadh / Dammam Power Station
      // Let's find power plant or grid node in Saudi Arabia
      const grid = window.globalDenseGrid.find(g => g.country && g.country.indexOf('Saudi') >= 0) || window.globalDenseGrid[0];
      // center map slightly so it's in view
      map.setView([grid.lat, grid.lon], 6);
      const pt = map.latLngToContainerPoint([grid.lat, grid.lon]);
      const containerRect = map.getContainer().getBoundingClientRect();
      return {
        gridName: grid.name,
        gridType: grid.type,
        screenX: containerRect.left + pt.x,
        screenY: containerRect.top + pt.y
      };
    })()
  `);
  console.log('Yellow dot target position:', yellowDotPos.result.value);

  const gx = yellowDotPos.result.value.screenX;
  const gy = yellowDotPos.result.value.screenY;
  await new Promise(r => setTimeout(r, 600));
  await sendCdp(ws, 'Input.dispatchMouseEvent', {
    type: 'mouseMoved',
    x: gx,
    y: gy
  });
  await new Promise(r => setTimeout(r, 600));

  const dotHoverState = await evaluate(ws, `
    (() => {
      const pop = document.getElementById('bmap_universal_vessel_popup');
      return {
        display: pop ? pop.style.display : 'none',
        name: document.getElementById('uni_vessel_name') ? document.getElementById('uni_vessel_name').textContent : '',
        type: document.getElementById('uni_vessel_type') ? document.getElementById('uni_vessel_type').textContent : '',
        status: document.getElementById('uni_vessel_status') ? document.getElementById('uni_vessel_status').textContent : ''
      };
    })()
  `);
  console.log('Yellow dot hover result:', JSON.stringify(dotHoverState.result.value, null, 2));

  // Take screenshot of Yellow Dot hover
  const shot2 = await sendCdp(ws, 'Page.captureScreenshot', { format: 'png' });
  fs.writeFileSync('C:/Users/SK/.gemini/antigravity/brain/49bcdc7d-9012-4831-93a6-42d8b11a6533/shot_verified_yellow_dot_hover.png', Buffer.from(shot2.data, 'base64'));
  console.log('Saved shot_verified_yellow_dot_hover.png');

  console.log('\n=== TEST 4: 3D Gods Eye View Workstation Toggle & Live Embed Test ===');
  const gevState = await evaluate(ws, `
    (() => {
      window.toggleGodsEyeView3D(true);
      const cont = document.getElementById('bmap_3d_globe_container');
      const iframe = document.getElementById('gev_iframe');
      const statusPill = document.getElementById('gev_server_status_pill');
      return {
        containerDisplay: cont ? cont.style.display : 'none',
        iframeSrc: iframe ? iframe.src : '',
        statusPillText: statusPill ? statusPill.textContent.trim() : ''
      };
    })()
  `);
  console.log('Gods Eye View toggle result:', JSON.stringify(gevState.result.value, null, 2));

  await new Promise(r => setTimeout(r, 3000));
  const shot3 = await sendCdp(ws, 'Page.captureScreenshot', { format: 'png' });
  fs.writeFileSync('C:/Users/SK/.gemini/antigravity/brain/49bcdc7d-9012-4831-93a6-42d8b11a6533/shot_verified_gods_eye_view_3d.png', Buffer.from(shot3.data, 'base64'));
  console.log('Saved shot_verified_gods_eye_view_3d.png');

  ws.close();
  chrome.kill();
  process.exit(0);
}

run().catch(err => {
  console.error('Error during test:', err);
  chrome.kill();
  process.exit(1);
});
