const { spawn } = require('child_process');

const chromePath = 'C:/Program Files/Google/Chrome/Application/chrome.exe';
const targetUrl = 'file:///F:/documents/SOIC/EconAgent_Platform/platform_ui/Bloomberg_BMAP_Terminal.html';
const port = 9258;

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

  const testCanvas = await evaluate(ws, `(() => {
    try {
      var grp = datasetLayerGroups['crude_pipelines'];
      var layers = Object.values(grp._layers || {});
      var petroPoly = layers.find(l => l.options && l.options.color === '#00e5ff' && l._latlngs && l._latlngs.length === 4);

      var rnd = petroPoly._renderer;
      var canvasEl = rnd._container;

      // Check canvas listeners
      var canvasRect = canvasEl.getBoundingClientRect();

      // Let's test calling _onMouseMove on renderer directly with an event at Petroline
      var pt = leafletMap.latLngToLayerPoint([25.4, 46.5]);
      var fakeEvent = {
        clientX: canvasRect.left + pt.x,
        clientY: canvasRect.top + pt.y
      };

      var layerFound = null;
      if (rnd._onClick) {
        // test which layer contains point
        for (var lId in rnd._layers) {
          var l = rnd._layers[lId];
          if (l._containsPoint && l._containsPoint(pt)) {
            layerFound = l.options;
            break;
          }
        }
      }

      return {
        canvasTagName: canvasEl.tagName,
        canvasWidth: canvasEl.width,
        canvasHeight: canvasEl.height,
        canvasRect: canvasRect,
        pt: pt,
        layerFound: layerFound,
        rndLayersCount: Object.keys(rnd._layers || {}).length
      };
    } catch(e) {
      return { error: e.toString() };
    }
  })()`);
  console.log('Canvas internal test:', JSON.stringify(testCanvas, null, 2));

  ws.close();
  chrome.kill();
}

run().catch(e => {
  console.error(e);
  chrome.kill();
});

