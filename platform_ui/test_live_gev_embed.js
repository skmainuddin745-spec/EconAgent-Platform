const { spawn } = require('child_process');
const fs = require('fs');

const chrome = spawn('C:/Program Files/Google/Chrome/Application/chrome.exe', [
  '--headless=new', '--remote-debugging-port=9299', '--disable-gpu', '--no-sandbox', '--window-size=1600,1050', 'about:blank'
]);

setTimeout(async () => {
  try {
    let ws = null;
    for (let i = 0; i < 15; i++) {
      try {
        const res = await fetch('http://127.0.0.1:9299/json');
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

    const consoleLogs = [];
    const exceptions = [];

    ws.addEventListener('message', e => {
      const data = JSON.parse(e.data);
      if (data.method === 'Runtime.consoleAPICalled') {
        consoleLogs.push(data.params);
      }
      if (data.method === 'Runtime.exceptionThrown') {
        exceptions.push(data.params);
      }
    });

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

    // Switch to bmap tab then to GEV view
    console.log('Switching to GEV 3D view...');
    const switchRes = await send('Runtime.evaluate', {
      expression: `(() => {
        showTab(null, 'bmap');
        switchBmapView('gev');
        checkGodsEyeServerStatus(true);

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
    console.log('Immediate GEV View State:', JSON.stringify(switchRes.result.value, null, 2));

    // Wait 3 seconds for Cesium 3D canvas and tiles to initialize inside the iframe
    await new Promise(r => setTimeout(r, 3500));

    const checkAfter = await send('Runtime.evaluate', {
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
    console.log('After 3.5s GEV View State:', JSON.stringify(checkAfter.result.value, null, 2));

    const shot = await send('Page.captureScreenshot', { format: 'png' });
    fs.writeFileSync('C:/Users/SK/.gemini/antigravity/brain/49bcdc7d-9012-4831-93a6-42d8b11a6533/shot_verified_live_gev_embed_3d.png', Buffer.from(shot.data, 'base64'));
    console.log('Saved shot_verified_live_gev_embed_3d.png');

    console.log(`Total exceptions: ${exceptions.length}`);
    exceptions.forEach(ex => console.log('EX:', ex.exceptionDetails.text, ex.exceptionDetails.exception?.description));

    chrome.kill();
    process.exit(0);
  } catch (err) {
    console.error(err);
    chrome.kill();
    process.exit(1);
  }
}, 1500);

