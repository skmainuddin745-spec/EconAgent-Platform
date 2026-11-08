const { spawn } = require('child_process');

const chromePath = 'C:/Program Files/Google/Chrome/Application/chrome.exe';
const targetUrl = 'file:///F:/documents/SOIC/EconAgent_Platform/platform_ui/Bloomberg_BMAP_Terminal.html';
const port = 9249;

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
  return new Promise(resolve => setTimeout(resolve, ms));
}

async function run() {
  await sleep(1500);
  const res = await fetch(`http://127.0.0.1:${port}/json`);
  const pages = await res.json();
  const ws = new WebSocket(pages[0].webSocketDebuggerUrl);
  await new Promise(r => ws.addEventListener('open', r));

  await sendCdp(ws, 'Page.enable');
  await sendCdp(ws, 'Page.navigate', { url: targetUrl });
  await sleep(3500);

  // Check what layers are on the map by default
  const layers = await evaluate(ws, `(() => {
    var onMap = {};
    for (var k in datasetLayerGroups) {
      onMap[k] = leafletMap.hasLayer(datasetLayerGroups[k]);
    }
    return onMap;
  })()`);
  console.log('Active layers on map load:', JSON.stringify(layers, null, 2));

  // Find container point of Petroline midpoint
  const pipePos = await evaluate(ws, `(() => {
    var petro = crudePipelines.find(p => p.id === 'pipe_petroline');
    // Midpoint between [25.4, 46.5] and [24.5, 42.0]
    var mid = [24.95, 44.25];
    var pt = leafletMap.latLngToContainerPoint(mid);
    return { latLng: mid, containerPoint: pt };
  })()`);
  console.log('Petroline midpoint on screen:', pipePos);

  // Simulate mousemove to Petroline midpoint
  console.log('Dispatching mousemove to Petroline midpoint...');
  await sendCdp(ws, 'Input.dispatchMouseEvent', {
    type: 'mouseMoved',
    x: pipePos.containerPoint.x,
    y: pipePos.containerPoint.y
  });
  await sleep(500);

  // Check if tooltip or inspector was triggered
  const hoverResult = await evaluate(ws, `(() => {
    var pop = document.getElementById('bmap_universal_vessel_popup');
    var tooltips = Array.from(document.querySelectorAll('.leaflet-tooltip')).map(t => t.textContent.trim());
    return {
      inspectorDisplay: pop ? pop.style.display : 'none',
      inspectorName: document.getElementById('uni_vessel_name') ? document.getElementById('uni_vessel_name').textContent : null,
      visibleTooltips: tooltips
    };
  })()`);
  console.log('Hover result on Petroline:', JSON.stringify(hoverResult, null, 2));

  ws.close();
  chrome.kill();
}

run().catch(e => {
  console.error(e);
  chrome.kill();
});

