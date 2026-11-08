const { spawn } = require('child_process');

const chromePath = 'C:/Program Files/Google/Chrome/Application/chrome.exe';
const targetUrl = 'file:///F:/documents/SOIC/EconAgent_Platform/platform_ui/Bloomberg_BMAP_Terminal.html';
const port = 9251;

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

  const elemInfo = await evaluate(ws, `(() => {
    var pt = leafletMap.latLngToContainerPoint([24.95, 44.25]);
    var rect = document.getElementById('bmap_leaflet_map').getBoundingClientRect();
    var x = rect.left + pt.x;
    var y = rect.top + pt.y;
    var el = document.elementFromPoint(x, y);

    var parents = [];
    var curr = el;
    while (curr && curr !== document.body) {
      parents.push({
        tag: curr.tagName,
        id: curr.id,
        class: curr.className,
        style: curr.getAttribute('style')
      });
      curr = curr.parentElement;
    }
    return {
      x, y,
      target: el ? { tag: el.tagName, id: el.id, class: el.className, outerHTML: el.outerHTML.substring(0, 300) } : null,
      parents: parents
    };
  })()`);
  console.log('Element hierarchy at Petroline point:', JSON.stringify(elemInfo, null, 2));

  ws.close();
  chrome.kill();
}

run().catch(e => {
  console.error(e);
  chrome.kill();
});

