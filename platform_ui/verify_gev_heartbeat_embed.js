const { spawn } = require('child_process');
const fs = require('fs');

const chrome = spawn('C:/Program Files/Google/Chrome/Application/chrome.exe', [
  '--headless=new', '--remote-debugging-port=9292', '--disable-gpu', '--no-sandbox', '--window-size=1600,1050', 'about:blank'
]);

setTimeout(async () => {
  try {
    let ws = null;
    for (let i = 0; i < 15; i++) {
      try {
        const res = await fetch('http://127.0.0.1:9292/json');
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

    if (!ws) {
      console.error('Cannot connect to Chrome');
      chrome.kill();
      process.exit(1);
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

    console.log('Navigating to EconAgent_Dashboard.html...');
    await send('Page.navigate', { url: 'file:///F:/documents/SOIC/EconAgent_Platform/platform_ui/EconAgent_Dashboard.html' });
    await new Promise(r => setTimeout(r, 3500));

    console.log('Switching to GEV view...');
    await send('Runtime.evaluate', {
      expression: `(() => {
        showTab(null, 'bmap');
        switchBmapView('gev');
      })()`
    });

    // Wait 1.5 seconds for heartbeat fetch
    await new Promise(r => setTimeout(r, 1500));

    const checkRes = await send('Runtime.evaluate', {
      expression: `(() => {
        const iframe = document.getElementById('gev_iframe');
        const fallback = document.getElementById('gev_fallback_box');
        const statusPill = document.getElementById('gev_server_status_pill');

        return {
          iframeDisplay: iframe ? window.getComputedStyle(iframe).display : null,
          iframeSrc: iframe ? iframe.src : null,
          fallbackDisplay: fallback ? window.getComputedStyle(fallback).display : null,
          statusText: statusPill ? statusPill.innerText : null
        };
      })()`,
      returnByValue: true
    });

    console.log('GEV Embed Result:', JSON.stringify(checkRes.result.value, null, 2));

    // Wait 3 more seconds for Cesium 3D tiles to settle
    await new Promise(r => setTimeout(r, 3000));

    const shot = await send('Page.captureScreenshot', { format: 'png' });
    fs.writeFileSync('C:/Users/SK/.gemini/antigravity/brain/49bcdc7d-9012-4831-93a6-42d8b11a6533/shot_verified_cesium_3d_final_perfect.png', Buffer.from(shot.data, 'base64'));
    console.log('Saved shot_verified_cesium_3d_final_perfect.png');

    chrome.kill();
    process.exit(0);
  } catch (err) {
    console.error(err);
    chrome.kill();
    process.exit(1);
  }
}, 1500);

