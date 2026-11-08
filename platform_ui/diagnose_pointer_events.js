const { spawn } = require('child_process');

const chromePath = 'C:/Program Files/Google/Chrome/Application/chrome.exe';
const targetUrl = 'file:///F:/documents/SOIC/EconAgent_Platform/platform_ui/Bloomberg_BMAP_Terminal.html';
const port = 9250;

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

  // Check elementFromPoint at map center and container bounds
  const diag = await evaluate(ws, `(() => {
    var mapEl = document.getElementById('bmap_leaflet_map');
    var rect = mapEl.getBoundingClientRect();

    var pt = leafletMap.latLngToContainerPoint([24.95, 44.25]);
    var clientX = rect.left + pt.x;
    var clientY = rect.top + pt.y;

    var elem = document.elementFromPoint(clientX, clientY);

    var weatherCanvas = document.getElementById('bmap_weather_canvas');
    var bmapCanvas = document.getElementById('bmap_canvas_overlay');

    return {
      mapRect: { left: rect.left, top: rect.top, width: rect.width, height: rect.height },
      pt: pt,
      clientCoords: { x: clientX, y: clientY },
      elementTag: elem ? elem.tagName : null,
      elementId: elem ? elem.id : null,
      elementClass: elem ? elem.className : null,
      weatherPointerEvents: weatherCanvas ? window.getComputedStyle(weatherCanvas).pointerEvents : null,
      overlayPointerEvents: bmapCanvas ? window.getComputedStyle(bmapCanvas).pointerEvents : null
    };
  })()`);
  console.log('Diagnostic result:', JSON.stringify(diag, null, 2));

  ws.close();
  chrome.kill();
}

run().catch(e => {
  console.error(e);
  chrome.kill();
});

