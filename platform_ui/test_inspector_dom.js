const { spawn } = require('child_process');

const chromePath = 'C:/Program Files/Google/Chrome/Application/chrome.exe';
const targetUrl = 'file:///F:/documents/SOIC/EconAgent_Platform/platform_ui/Bloomberg_BMAP_Terminal.html';
const port = 9246;

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
    expression: `
      var petro = crudePipelines.find(p => p.id === 'pipe_petroline');
      window.showUniversalInspector('pipeline', petro, [24.0, 45.0]);
      JSON.stringify({
        name: document.getElementById('uni_vessel_name').textContent,
        type: document.getElementById('uni_vessel_type').textContent,
        status: document.getElementById('uni_vessel_status').textContent,
        owner: document.getElementById('uni_vessel_owner').textContent,
        dest: document.getElementById('uni_vessel_dest').textContent,
        draft: document.getElementById('uni_vessel_draft_dwt').textContent,
        display: document.getElementById('bmap_universal_vessel_popup').style.display
      })
    `,
    returnByValue: true
  });

  console.log('Petroline Inspector DOM values:');
  console.log(result.result.value);

  const tasiResult = await sendCdp(ws, 'Runtime.evaluate', {
    expression: `
      var tasi = worldEquityData.find(e => e.code === 'SA');
      window.showUniversalInspector('equity', tasi, [24.0, 45.0]);
      JSON.stringify({
        name: document.getElementById('uni_vessel_name').textContent,
        type: document.getElementById('uni_vessel_type').textContent,
        status: document.getElementById('uni_vessel_status').textContent,
        last: document.getElementById('uni_vessel_owner').textContent,
        change: document.getElementById('uni_vessel_dest').textContent,
        erp: document.getElementById('uni_vessel_berth').textContent,
        pe: document.getElementById('uni_vessel_speed').textContent
      })
    `,
    returnByValue: true
  });

  console.log('\nTadawul TASI Inspector DOM values:');
  console.log(tasiResult.result.value);

  ws.close();
  chrome.kill();
}

run().catch(e => {
  console.error(e);
  chrome.kill();
});

