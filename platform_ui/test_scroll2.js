const { spawn } = require('child_process');
const fs = require('fs');

const chrome = spawn('C:/Program Files/Google/Chrome/Application/chrome.exe', [
  '--headless=new', '--remote-debugging-port=9295', '--disable-gpu', '--no-sandbox', '--window-size=1600,1050', 'about:blank'
]);

setTimeout(async () => {
  try {
    let ws = null;
    for (let i = 0; i < 15; i++) {
      try {
        const res = await fetch('http://127.0.0.1:9295/json');
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

    // Evaluate clicking titans
    const metrics = await send('Runtime.evaluate', {
      expression: `(() => {
        function getR(el) {
          if (!el) return null;
          const r = el.getBoundingClientRect();
          return { top: r.top, bottom: r.bottom, left: r.left, right: r.right, width: r.width, height: r.height };
        }

        const t = Array.from(document.querySelectorAll('.tab')).find(x => (x.getAttribute('onclick')||'').includes('titans'));
        if (t) t.click();

        const tabs = document.querySelector('.tabs');
        const titans = document.getElementById('titans');
        const vp = document.getElementById('workspace_viewport');

        return {
          windowScrollY: window.scrollY,
          tabsRect: getR(tabs),
          vpRect: getR(vp),
          titansRect: getR(titans),
          activeTabClass: t ? t.className : null,
          activeContentCount: document.querySelectorAll('.content.active').length,
          allActiveContents: Array.from(document.querySelectorAll('.content.active')).map(c => ({ id: c.id, rect: getR(c) }))
        };
      })()`,
      returnByValue: true
    });

    console.log('Metrics:', JSON.stringify(metrics.result.value, null, 2));

    chrome.kill();
    process.exit(0);
  } catch (err) {
    console.error(err);
    chrome.kill();
    process.exit(1);
  }
}, 1500);

