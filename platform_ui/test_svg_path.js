const { spawn } = require('child_process');

const chromePath = 'C:/Program Files/Google/Chrome/Application/chrome.exe';
const targetUrl = 'file:///F:/documents/SOIC/EconAgent_Platform/platform_ui/Bloomberg_BMAP_Terminal.html';
const port = 9257;

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

  const testDrawn = await evaluate(ws, `(() => {
    try {
      var grp = datasetLayerGroups['crude_pipelines'];
      var layers = grp ? Object.values(grp._layers || {}) : [];
      var petroPoly = layers.find(l => l.options && l.options.color === '#00e5ff' && l._latlngs && l._latlngs.length === 4);

      var rnd = petroPoly._renderer;
      var pathElem = petroPoly._path;

      return {
        rendererConstructor: rnd ? rnd.constructor.name : null,
        hasPathElem: !!pathElem,
        pathTag: pathElem ? pathElem.tagName : null,
        pathStroke: pathElem ? pathElem.getAttribute('stroke') : null,
        pathStrokeWidth: pathElem ? pathElem.getAttribute('stroke-width') : null,
        pathPointerEvents: pathElem ? window.getComputedStyle(pathElem).pointerEvents : null,
        parentTag: pathElem ? pathElem.parentElement.tagName : null
      };
    } catch(e) {
      return { error: e.toString() };
    }
  })()`);
  console.log('SVG Path test:', JSON.stringify(testDrawn, null, 2));

  ws.close();
  chrome.kill();
}

run().catch(e => {
  console.error(e);
  chrome.kill();
});

