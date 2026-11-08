const { spawn } = require('child_process');

const chromePath = 'C:/Program Files/Google/Chrome/Application/chrome.exe';
const targetUrl = 'file:///F:/documents/SOIC/EconAgent_Platform/platform_ui/EconAgent_Dashboard.html';
const port = 9336;

const chrome = spawn(chromePath, [
  '--headless=new',
  `--remote-debugging-port=${port}`,
  '--disable-gpu',
  '--no-sandbox',
  'about:blank'
]);

async function sleep(ms) { return new Promise(r => setTimeout(r, ms)); }

async function main() {
  let wsUrl = null;
  for (let i = 0; i < 15; i++) {
    try {
      const res = await fetch(`http://127.0.0.1:${port}/json`);
      const pages = await res.json();
      if (pages.length > 0) { wsUrl = pages[0].webSocketDebuggerUrl; break; }
    } catch(e) {}
    await sleep(500);
  }

  if (!wsUrl) { console.error('Could not connect to Chrome'); chrome.kill(); return; }

  const ws = new WebSocket(wsUrl);
  await new Promise(r => ws.addEventListener('open', r));

  let msgId = 1;
  function sendCdp(method, params = {}) {
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

  await sendCdp('Page.enable');
  await sendCdp('Runtime.enable');
  await sendCdp('Page.navigate', { url: targetUrl });
  await sleep(2500);

  const evalRes = await sendCdp('Runtime.evaluate', {
    expression: `(async function() {
      let fetchRes = null;
      try {
        await fetch('http://127.0.0.1:4173/?embed=1', { mode: 'no-cors' });
        fetchRes = { ok: true };
      } catch(e) {
        fetchRes = { ok: false, err: e.message };
      }

      let imgRes = await new Promise(r => {
        var img = new Image();
        img.onload = () => r({ ok: true });
        img.onerror = () => r({ ok: false });
        img.src = 'http://127.0.0.1:4173/logo.svg?t=' + Date.now();
      });

      return { fetchRes, imgRes };
    })()`,
    awaitPromise: true,
    returnByValue: true
  });

  console.log('Result:', JSON.stringify(evalRes.result.value, null, 2));

  ws.close();
  chrome.kill();
}

main();
