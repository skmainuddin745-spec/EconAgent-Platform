const { spawn } = require('child_process');

const chromePath = 'C:/Program Files/Google/Chrome/Application/chrome.exe';
const targetUrl = 'file:///F:/documents/SOIC/EconAgent_Platform/platform_ui/Bloomberg_BMAP_Terminal.html';
const port = 9252;

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

  // Test hover at Abqaiq [25.93, 49.67]
  const abqaiqInfo = await evaluate(ws, `(() => {
    var rect = document.getElementById('bmap_leaflet_map').getBoundingClientRect();
    var pt = leafletMap.latLngToContainerPoint([25.93, 49.67]);
    var clientX = rect.left + pt.x;
    var clientY = rect.top + pt.y;
    var el = document.elementFromPoint(clientX, clientY);
    return {
      pt, clientX, clientY,
      elem: el ? { tag: el.tagName, id: el.id, class: el.className } : null
    };
  })()`);
  console.log('Abqaiq point:', JSON.stringify(abqaiqInfo, null, 2));

  // Dispatch mousemove to Abqaiq
  await sendCdp(ws, 'Input.dispatchMouseEvent', {
    type: 'mouseMoved',
    x: abqaiqInfo.clientX,
    y: abqaiqInfo.clientY
  });
  await sleep(600);

  const hoverAbqaiq = await evaluate(ws, `(() => {
    var pop = document.getElementById('bmap_universal_vessel_popup');
    var tooltips = Array.from(document.querySelectorAll('.leaflet-tooltip')).map(t => t.textContent.trim());
    return {
      inspectorDisplay: pop ? pop.style.display : 'none',
      inspectorName: document.getElementById('uni_vessel_name') ? document.getElementById('uni_vessel_name').textContent : null,
      visibleTooltips: tooltips
    };
  })()`);
  console.log('Hover result at Abqaiq:', JSON.stringify(hoverAbqaiq, null, 2));

  ws.close();
  chrome.kill();
}

run().catch(e => {
  console.error(e);
  chrome.kill();
});

