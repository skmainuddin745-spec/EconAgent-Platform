const { spawn } = require('child_process');

const chrome = spawn('C:/Program Files/Google/Chrome/Application/chrome.exe', [
  '--headless=new', '--remote-debugging-port=9281', '--disable-gpu', '--no-sandbox', '--window-size=1600,1050', 'about:blank'
]);

setTimeout(async () => {
  try {
    let ws = null;
    for (let i = 0; i < 20; i++) {
      try {
        const res = await fetch('http://127.0.0.1:9281/json');
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

    const exceptions = [];
    ws.addEventListener('message', e => {
      const d = JSON.parse(e.data);
      if (d.method === 'Runtime.exceptionThrown') {
        exceptions.push(d.params.exceptionDetails);
      }
    });

    await send('Runtime.enable');
    await send('Page.enable');
    await send('Page.navigate', { url: 'file:///F:/documents/SOIC/EconAgent_Platform/platform_ui/EconAgent_Dashboard.html' });
    await new Promise(r => setTimeout(r, 3500));

    console.log('TOTAL_EXCEPTIONS:', exceptions.length);
    exceptions.forEach((ex, idx) => {
      console.log(`EX ${idx+1}: line ${ex.lineNumber}:${ex.columnNumber} -> ${ex.text}`);
      if (ex.exception && ex.exception.description) {
        console.log(`  DESC: ${ex.exception.description}`);
      }
    });

    ws.close();
    chrome.kill();
  } catch (e) {
    console.error(e);
    chrome.kill();
  }
}, 500);

