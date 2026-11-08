const { spawn } = require('child_process');
const fs = require('fs');

const chrome = spawn('C:/Program Files/Google/Chrome/Application/chrome.exe', [
  '--headless=new', '--remote-debugging-port=9295', '--disable-gpu', '--no-sandbox', '--window-size=1600,1050', 'about:blank'
]);

setTimeout(async () => {
  try {
    let ws = null;
    for (let i = 0; i < 20; i++) {
      try {
        const res = await fetch('http://127.0.0.1:9295/json');
        if (res.ok) {
          const pages = await res.json();
          ws = new WebSocket(pages[0].webSocketDebuggerUrl);
          await new Promise(r => ws.addEventListener('open', r));
          break;
        }
      } catch (e) {
        await new Promise(r => setTimeout(r, 200));
      }
    }

    let msgId = 1;
    function send(method, params) {
      return new Promise((resolve) => {
        const id = msgId++;
        const handler = (event) => {
          const d = JSON.parse(event.data);
          if (d.id === id) {
            ws.removeEventListener('message', handler);
            resolve(d.result);
          }
        };
        ws.addEventListener('message', handler);
        ws.send(JSON.stringify({ id, method, params: params || {} }));
      });
    }

    await send('Runtime.enable');
    await send('Page.enable');
    await send('Page.navigate', { url: 'file:///F:/documents/SOIC/EconAgent_Platform/platform_ui/EconAgent_Dashboard.html' });
    await new Promise(r => setTimeout(r, 3500));

    const tabs = [
      'zoom', 'bmap', 'technicals', 'fundamentals', 'scen', 'soic',
      'rot', 'vol', 'flows', 'titans', 'soic_sectors', 'topnotch'
    ];

    const results = {};

    for (const tabId of tabs) {
      const res = await send('Runtime.evaluate', {
        expression: `(() => {
          window.showTab(null, '${tabId}');
          const el = document.getElementById('${tabId}');
          if (!el) return { found: false };
          const cs = window.getComputedStyle(el);
          return {
            found: true,
            isActive: el.classList.contains('active'),
            display: cs.display,
            visibility: cs.visibility,
            height: el.clientHeight,
            scrollHeight: el.scrollHeight,
            textLen: el.innerText.trim().length,
            sampleText: el.innerText.trim().substring(0, 100)
          };
        })()`,
        returnByValue: true
      });
      results[tabId] = res && res.result ? res.result.value : res;
    }

    console.log('ALL_TABS_AUDIT_RESULTS:\n', JSON.stringify(results, null, 2));

    ws.close();
    chrome.kill();
  } catch (err) {
    console.error('ERROR:', err);
    chrome.kill();
  }
}, 500);

