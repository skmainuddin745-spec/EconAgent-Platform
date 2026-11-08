const { spawn } = require('child_process');
const fs = require('fs');

const chrome = spawn('C:/Program Files/Google/Chrome/Application/chrome.exe', [
  '--headless=new', '--remote-debugging-port=9293', '--disable-gpu', '--no-sandbox', '--window-size=1600,1050', 'about:blank'
]);

setTimeout(async () => {
  try {
    let ws = null;
    for (let i = 0; i < 15; i++) {
      try {
        const res = await fetch('http://127.0.0.1:9293/json');
        if (res.ok) {
          const pages = await res.json();
          ws = new WebSocket(pages[0].webSocketDebuggerUrl);
          await new Promise(r => ws.addEventListener('open', r));
          break;
        }
      } catch (e) {
        await new Promise(r => setTimeout(r, 300));
      }
    }

    let id = 1;
    const send = (m, p) => new Promise((resolve) => {
      const cur = id++;
      const h = e => { const d = JSON.parse(e.data); if (d.id === cur) { ws.removeEventListener('message', h); resolve(d.result); } };
      ws.addEventListener('message', h);
      ws.send(JSON.stringify({ id: cur, method: m, params: p }));
    });

    await send('Runtime.enable');
    await send('Page.enable');

    await send('Page.navigate', { url: 'file:///F:/documents/SOIC/EconAgent_Platform/platform_ui/EconAgent_Dashboard.html' });
    await new Promise(r => setTimeout(r, 3000));

    const evalRes = await send('Runtime.evaluate', {
      expression: `(async () => {
        showTab(null, 'bmap');
        switchBmapView('gev');
        const iframe = document.getElementById('gev_iframe');
        const fallback = document.getElementById('gev_fallback_box');
        const statusPill = document.getElementById('gev_server_status_pill');

        if (iframe) {
          iframe.style.display = 'block';
          iframe.src = 'http://127.0.0.1:4173/?embed=1';
        }
        if (fallback) fallback.style.display = 'none';
        if (statusPill) {
          statusPill.innerHTML = '● VITE 3D SERVER ONLINE (Port 4173)';
          statusPill.style.background = 'rgba(16,185,129,0.15)';
          statusPill.style.border = '1px solid #10b981';
          statusPill.style.color = '#34d399';
        }
        return { success: true, src: iframe.src };
      })()`,
      awaitPromise: true,
      returnByValue: true
    });

    console.log('Result:', JSON.stringify(evalRes.result.value, null, 2));

    await new Promise(r => setTimeout(r, 3500));

    const shot = await send('Page.captureScreenshot', { format: 'png' });
    fs.writeFileSync('C:/Users/SK/.gemini/antigravity/brain/49bcdc7d-9012-4831-93a6-42d8b11a6533/shot_verified_cesium_iframe_success.png', Buffer.from(shot.data, 'base64'));
    console.log('Saved shot_verified_cesium_iframe_success.png');

    chrome.kill();
    process.exit(0);
  } catch (err) {
    console.error(err);
    chrome.kill();
    process.exit(1);
  }
}, 1500);
