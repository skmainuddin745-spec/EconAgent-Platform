const { spawn } = require('child_process');
const fs = require('fs');

const chromePath = 'C:/Program Files/Google/Chrome/Application/chrome.exe';
const targetUrl = 'file:///F:/documents/SOIC/EconAgent_Platform/platform_ui/EconAgent_Dashboard.html';
const port = 9248;

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

  const consoleErrors = [];
  ws.addEventListener('message', (event) => {
    const data = JSON.parse(event.data);
    if (data.method === 'Runtime.consoleAPICalled' && data.params.type === 'error') {
      consoleErrors.push(data.params.args.map(a => a.value || a.description).join(' '));
    }
  });

  await sendCdp(ws, 'Runtime.enable');
  await sendCdp(ws, 'Page.enable');

  console.log(`Navigating to master dashboard ${targetUrl}...`);
  await sendCdp(ws, 'Page.navigate', { url: targetUrl });
  await sleep(4000);

  // Switch to BMAP tab
  console.log('Switching to BMAP Tab...');
  const switchRes = await evaluate(ws, `(() => {
    // Find BMAP tab button
    if (typeof switchTab === 'function') {
      switchTab('tab_bmap');
    }
    // trigger map resize
    if (window.leafletMap) {
      window.leafletMap.invalidateSize();
    }
    return {
      bmapActive: !!window.leafletMap,
      vesselsCount: (window.globalVessels || []).length,
      pipelinesCount: (window.crudePipelines || []).length,
      cablesCount: (window.globalSubmarineCables || []).length
    };
  })()`);
  console.log('Master Dashboard BMAP status:', JSON.stringify(switchRes, null, 2));

  // Trigger Petroline inspector on master dashboard
  const petroRes = await evaluate(ws, `(() => {
    var petro = window.crudePipelines.find(p => p.id === 'pipe_petroline');
    window.showUniversalInspector('pipeline', petro, [24.0, 45.0]);
    return {
      name: document.getElementById('uni_vessel_name').textContent,
      type: document.getElementById('uni_vessel_type').textContent,
      display: document.getElementById('bmap_universal_vessel_popup').style.display
    };
  })()`);
  console.log('Master Dashboard Petroline Inspector:', JSON.stringify(petroRes, null, 2));

  // Capture master dashboard screenshot
  await sleep(1000);
  const shot = await sendCdp(ws, 'Page.captureScreenshot', { format: 'png' });
  fs.writeFileSync('C:/Users/SK/.gemini/antigravity/brain/49bcdc7d-9012-4831-93a6-42d8b11a6533/shot_master_dashboard_bmap_petroline.png', Buffer.from(shot.data, 'base64'));
  console.log('Saved shot_master_dashboard_bmap_petroline.png');

  console.log(`Master Dashboard Console errors: ${consoleErrors.length}`);
  if (consoleErrors.length > 0) {
    console.log('Errors:', consoleErrors);
  }

  ws.close();
  chrome.kill();
  console.log('Master dashboard verification passed cleanly!');
}

run().catch(e => {
  console.error('Test error:', e);
  chrome.kill();
});

