const { spawn } = require('child_process');
const fs = require('fs');

const chromePath = 'C:/Program Files/Google/Chrome/Application/chrome.exe';
const targetUrl = 'file:///F:/documents/SOIC/EconAgent_Platform/platform_ui/EconAgent_Dashboard.html#bmap';
const port = 9310;

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
  return new Promise(r => setTimeout(r, ms));
}

async function run() {
  let ws = null;
  for (let i = 0; i < 15; i++) {
    try {
      const res = await fetch(`http://127.0.0.1:${port}/json`);
      if (res.ok) {
        const pages = await res.json();
        ws = new WebSocket(pages[0].webSocketDebuggerUrl);
        await new Promise(r => ws.addEventListener('open', r));
        break;
      }
    } catch (e) {
      await sleep(300);
    }
  }

  await sendCdp(ws, 'Page.enable');
  await sendCdp(ws, 'Page.navigate', { url: targetUrl });
  await sleep(4000);

  // Switch to GEV view
  await evaluate(ws, `window.switchBmapView('gev')`);
  await sleep(4000);

  // Check iframe contents
  const iframeState = await evaluate(ws, `(() => {
    const iframe = document.getElementById('gev_iframe');
    const iframeDoc = iframe ? iframe.contentDocument : null;
    return {
      src: iframe ? iframe.src : null,
      hasDoc: !!iframeDoc,
      title: iframeDoc ? iframeDoc.title : null,
      bodyText: iframeDoc && iframeDoc.body ? iframeDoc.body.innerText.slice(0, 200) : null
    };
  })()`);
  console.log('Iframe State:', JSON.stringify(iframeState, null, 2));

  const shot = await sendCdp(ws, 'Page.captureScreenshot', { format: 'png' });
  fs.writeFileSync('C:/Users/SK/.gemini/antigravity/brain/49bcdc7d-9012-4831-93a6-42d8b11a6533/shot_gev_iframe_live_test.png', Buffer.from(shot.data, 'base64'));
  console.log('Saved shot_gev_iframe_live_test.png');

  ws.close();
  chrome.kill();
  process.exit(0);
}

run().catch(e => {
  console.error(e);
  chrome.kill();
  process.exit(1);
});

