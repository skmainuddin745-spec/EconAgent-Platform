const { spawn } = require('child_process');

const chromePath = 'C:/Program Files/Google/Chrome/Application/chrome.exe';
const targetUrl = 'file:///F:/documents/SOIC/EconAgent_Platform/platform_ui/Bloomberg_BMAP_Terminal.html';
const port = 9247;

const chrome = spawn(chromePath, [
  '--headless=new',
  `--remote-debugging-port=${port}`,
  '--disable-gpu',
  '--no-sandbox',
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

async function run() {
  await new Promise(r => setTimeout(r, 1500));
  const res = await fetch(`http://127.0.0.1:${port}/json`);
  const pages = await res.json();
  const ws = new WebSocket(pages[0].webSocketDebuggerUrl);
  await new Promise(r => ws.addEventListener('open', r));

  await sendCdp(ws, 'Page.enable');
  await sendCdp(ws, 'Page.navigate', { url: targetUrl });
  await new Promise(r => setTimeout(r, 3000));

  const result = await sendCdp(ws, 'Runtime.evaluate', {
    expression: `typeof window.showUniversalInspector`,
    returnByValue: true
  });

  console.log('typeof window.showUniversalInspector:', JSON.stringify(result));

  const eval2 = await sendCdp(ws, 'Runtime.evaluate', {
    expression: `
      try {
        var petro = crudePipelines.find(p => p.id === 'pipe_petroline');
        window.showUniversalInspector('pipeline', petro, [24.0, 45.0]);
        ({
          name: document.getElementById('uni_vessel_name').textContent,
          type: document.getElementById('uni_vessel_type').textContent,
          status: document.getElementById('uni_vessel_status').textContent
        });
      } catch (e) {
        ({ error: e.toString() });
      }
    `,
    returnByValue: true
  });

  console.log('eval2:', JSON.stringify(eval2));

  ws.close();
  chrome.kill();
}

run().catch(e => {
  console.error(e);
  chrome.kill();
});

