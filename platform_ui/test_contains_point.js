const { spawn } = require('child_process');

const chromePath = 'C:/Program Files/Google/Chrome/Application/chrome.exe';
const targetUrl = 'file:///F:/documents/SOIC/EconAgent_Platform/platform_ui/Bloomberg_BMAP_Terminal.html';
const port = 9253;

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

  const testContains = await evaluate(ws, `(() => {
    var grp = datasetLayerGroups['crude_pipelines'];
    var layers = grp ? Object.values(grp._layers || {}) : [];
    var petroLayers = layers.filter(l => l._latlngs && l._latlngs.length === 4);

    var pt = leafletMap.latLngToLayerPoint([25.93, 49.67]);
    var results = [];
    petroLayers.forEach(l => {
      results.push({
        options: l.options,
        contains: l._containsPoint ? l._containsPoint(pt) : 'no _containsPoint',
        parts: l._parts ? l._parts.length : 0
      });
    });

    return {
      pt: pt,
      petroLayersCount: petroLayers.length,
      results: results
    };
  })()`);
  console.log('Polyline _containsPoint test:', JSON.stringify(testContains, null, 2));

  ws.close();
  chrome.kill();
}

run().catch(e => {
  console.error(e);
  chrome.kill();
});

