const { spawn } = require('child_process');

const chrome = spawn('C:/Program Files/Google/Chrome/Application/chrome.exe', [
  '--headless=new', '--remote-debugging-port=9291', '--disable-gpu', '--no-sandbox', '--window-size=1600,1050', 'about:blank'
]);

setTimeout(async () => {
  try {
    let ws = null;
    for (let i = 0; i < 15; i++) {
      try {
        const res = await fetch('http://127.0.0.1:9291/json');
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

    // Switch to GEV view
    await send('Runtime.evaluate', {
      expression: `(() => {
        showTab(null, 'bmap');
        switchBmapView('gev');
      })()`
    });

    await new Promise(r => setTimeout(r, 2000));

    // Check iframe properties
    const res = await send('Runtime.evaluate', {
      expression: `(() => {
        const iframe = document.getElementById('gev_iframe');
        const fallback = document.getElementById('gev_fallback_box');
        const statusPill = document.getElementById('gev_server_status_pill');
        
        let iframeDocTitle = null;
        try {
          iframeDocTitle = iframe.contentDocument ? iframe.contentDocument.title : 'cross-origin';
        } catch(e) {
          iframeDocTitle = 'cross-origin-restricted';
        }

        return {
          iframeDisplay: window.getComputedStyle(iframe).display,
          iframeSrc: iframe.src,
          iframeDocTitle: iframeDocTitle,
          fallbackDisplay: window.getComputedStyle(fallback).display,
          statusPillText: statusPill.innerText,
          rect: {
            width: iframe.offsetWidth,
            height: iframe.offsetHeight
          }
        };
      })()`,
      returnByValue: true
    });

    console.log('Verification Result:', JSON.stringify(res.result.value, null, 2));

    chrome.kill();
    process.exit(0);
  } catch (err) {
    console.error(err);
    chrome.kill();
    process.exit(1);
  }
}, 1500);

