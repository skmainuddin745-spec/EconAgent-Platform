const { spawn } = require('child_process');
const fs = require('fs');

const chromePath = 'C:/Program Files/Google/Chrome/Application/chrome.exe';
const targetUrl = 'file:///F:/documents/SOIC/EconAgent_Platform/platform_ui/EconAgent_Dashboard.html';

const chrome = spawn(chromePath, [
  '--headless=new',
  '--remote-debugging-port=9224',
  '--disable-gpu',
  '--no-sandbox',
  '--window-size=1440,900',
  'about:blank'
]);

let msgId = 1;
function sendCdp(ws, method, params = {}) {
  return new Promise((resolve) => {
    const id = msgId++;
    const handler = (event) => {
      const data = JSON.parse(event.data);
      if (data.id === id) {
        ws.removeEventListener('message', handler);
        resolve(data.result);
      }
    };
    ws.addEventListener('message', handler);
    ws.send(JSON.stringify({ id, method, params }));
  });
}

setTimeout(async () => {
  try {
    const listRes = await fetch('http://127.0.0.1:9224/json/new?' + encodeURIComponent(targetUrl), { method: 'PUT' });
    const targetData = await listRes.json();
    const ws = new WebSocket(targetData.webSocketDebuggerUrl);

    ws.onopen = async () => {
      await sendCdp(ws, 'Runtime.enable');
      await sendCdp(ws, 'Page.enable');

      await new Promise(r => setTimeout(r, 2000));

      const tabsToCapture = [
        { id: 'technicals', name: 'f3_technicals' },
        { id: 'titans', name: 'blk_vang_titans' },
        { id: 'soic_sectors', name: 'soic_sectors' },
        { id: 'topnotch', name: 'topnotch_pods' },
        { id: 'macro', name: 'f10_macro' },
        { id: 'soic', name: 'f5_soic_scorecard' },
        { id: 'flows', name: 'f8_flows' }
      ];

      for (const t of tabsToCapture) {
        console.log(`Switching and capturing tab: ${t.id}...`);
        await sendCdp(ws, 'Runtime.evaluate', {
          expression: `
            showTab(null, '${t.id}');
            window.scrollTo(0, 300);
          `
        });
        await new Promise(r => setTimeout(r, 500));

        const shot = await sendCdp(ws, 'Page.captureScreenshot', { format: 'png' });
        fs.writeFileSync(`F:/documents/SOIC/EconAgent_Platform/platform_ui/shot_${t.name}.png`, Buffer.from(shot.data, 'base64'));
        console.log(`Saved shot_${t.name}.png (${shot.data.length} bytes)`);
      }

      ws.close();
      chrome.kill();
      console.log('ALL SCREENSHOTS CAPTURED SUCCESSFULLY!');
      process.exit(0);
    };
  } catch (e) {
    console.error(e);
    chrome.kill();
    process.exit(1);
  }
}, 1500);

