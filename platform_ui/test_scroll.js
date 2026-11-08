const { spawn } = require('child_process');
const fs = require('fs');

const chrome = spawn('C:/Program Files/Google/Chrome/Application/chrome.exe', [
  '--headless=new', '--remote-debugging-port=9294', '--disable-gpu', '--no-sandbox', '--window-size=1600,1050', 'about:blank'
]);

setTimeout(async () => {
  try {
    let ws = null;
    for (let i = 0; i < 15; i++) {
      try {
        const res = await fetch('http://127.0.0.1:9294/json');
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

    // What happens if we click titans without scrolling?
    await send('Runtime.evaluate', {
      expression: `(() => {
        const t = Array.from(document.querySelectorAll('.tab')).find(x => (x.getAttribute('onclick')||'').includes('titans'));
        if (t) t.click();
      })()`
    });
    await new Promise(r => setTimeout(r, 500));

    // Check window.scrollY, tabs.offsetTop, titans.offsetTop
    const metrics = await send('Runtime.evaluate', {
      expression: `(() => {
        const tabs = document.querySelector('.tabs');
        const titans = document.getElementById('titans');
        return {
          windowScrollY: window.scrollY,
          windowInnerHeight: window.innerHeight,
          tabsOffsetTop: tabs ? tabs.offsetTop : null,
          tabsRect: tabs ? tabs.getBoundingClientRect() : null,
          titansOffsetTop: titans ? titans.offsetTop : null,
          titansRect: titans ? titans.getBoundingClientRect() : null,
          titansParentId: titans ? titans.parentElement.id : null,
          titansParentClass: titans ? titans.parentElement.className : null,
          workspaceViewportRect: document.getElementById('workspace_viewport') ? document.getElementById('workspace_viewport').getBoundingClientRect() : null
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

