const { spawn } = require('child_process');

const chrome = spawn('C:/Program Files/Google/Chrome/Application/chrome.exe', [
  '--headless=new', '--remote-debugging-port=9280', '--disable-gpu', '--no-sandbox', '--window-size=1600,1050', 'about:blank'
]);

setTimeout(async () => {
  try {
    let ws = null;
    for (let i = 0; i < 20; i++) {
      try {
        const res = await fetch('http://127.0.0.1:9280/json');
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
    await new Promise(r => setTimeout(r, 3500));

    const check = await send('Runtime.evaluate', {
      expression: `(() => {
        const sec = document.getElementById('global_sector_select');
        const firm = document.getElementById('global_firm_select');
        const country = document.getElementById('global_country_select');
        return {
          countryValue: country ? country.value : null,
          secOptionsCount: sec ? sec.options.length : 0,
          secFirstOpt: sec && sec.options[0] ? sec.options[0].text : null,
          secVal: sec ? sec.value : null,
          firmOptionsCount: firm ? firm.options.length : 0,
          firmFirstOpt: firm && firm.options[0] ? firm.options[0].text : null,
          firmVal: firm ? firm.value : null,
          allFirms: firm ? Array.from(firm.options).map(o => o.text) : []
        };
      })()`,
      returnByValue: true
    });

    console.log('ON_LOAD_STATE:', JSON.stringify(check.result.value, null, 2));

    ws.close();
    chrome.kill();
  } catch (e) {
    console.error(e);
    chrome.kill();
  }
}, 500);

