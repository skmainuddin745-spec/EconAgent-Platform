const { spawn } = require('child_process');

const chrome = spawn('C:/Program Files/Google/Chrome/Application/chrome.exe', [
  '--headless=new', '--remote-debugging-port=9289', '--disable-gpu', '--no-sandbox', '--window-size=1600,1050', 'about:blank'
]);

setTimeout(async () => {
  try {
    let ws = null;
    for (let i = 0; i < 20; i++) {
      try {
        const res = await fetch('http://127.0.0.1:9289/json');
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

    if (!ws) {
      console.log('CHROME_CONN_FAIL');
      chrome.kill();
      process.exit(1);
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
    await new Promise(r => setTimeout(r, 3000));

    // Call populateGlobalDropdowns and inspect result or exception
    const res = await send('Runtime.evaluate', {
      expression: `(() => {
        try {
          const beforeSecCount = document.getElementById('global_sector_select').options.length;
          const hasSectors = typeof window.GLOBAL_DAMODARAN_SECTORS;
          const hasComps = typeof window.GLOBAL_COMPANIES_BY_COUNTRY;
          
          window.populateGlobalDropdowns('us', 'Semiconductor');
          
          const afterSecCount = document.getElementById('global_sector_select').options.length;
          const afterFirmCount = document.getElementById('global_firm_select').options.length;
          const firms = Array.from(document.getElementById('global_firm_select').options).map(o => o.text);
          return {
            hasSectors,
            hasComps,
            beforeSecCount,
            afterSecCount,
            afterFirmCount,
            firms
          };
        } catch (e) {
          return { error: e.toString(), stack: e.stack };
        }
      })()`,
      returnByValue: true
    });

    console.log('POP_RESULT:', JSON.stringify(res && res.result ? res.result.value : res, null, 2));

    ws.close();
    chrome.kill();
  } catch (e) {
    console.error(e);
    chrome.kill();
  }
}, 500);

