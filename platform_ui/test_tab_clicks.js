const { spawn } = require('child_process');
const fs = require('fs');

const chrome = spawn('C:/Program Files/Google/Chrome/Application/chrome.exe', [
  '--headless=new', '--remote-debugging-port=9294', '--disable-gpu', '--no-sandbox', '--window-size=1600,1050', 'about:blank'
]);

setTimeout(async () => {
  try {
    let ws = null;
    for (let i = 0; i < 20; i++) {
      try {
        const res = await fetch('http://127.0.0.1:9294/json');
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

    const consoleLogs = [];
    ws.addEventListener('message', e => {
      const d = JSON.parse(e.data);
      if (d.method === 'Runtime.consoleAPICalled') {
        const text = d.params.args.map(a => a.value || JSON.stringify(a)).join(' ');
        consoleLogs.push('[' + d.params.type + '] ' + text);
      }
      if (d.method === 'Runtime.exceptionThrown') {
        consoleLogs.push('[EXCEPTION] ' + JSON.stringify(d.params.exceptionDetails));
      }
    });

    await send('Runtime.enable');
    await send('Page.enable');
    await send('Page.navigate', { url: 'file:///F:/documents/SOIC/EconAgent_Platform/platform_ui/EconAgent_Dashboard.html' });
    await new Promise(r => setTimeout(r, 3500));

    // Test clicking titans tab
    const titansTest = await send('Runtime.evaluate', {
      expression: `(() => {
        // Find the titans tab button
        const allTabs = Array.from(document.querySelectorAll('.tab, .tab-btn'));
        const titanBtn = allTabs.find(t => t.innerText.includes('Titans') || (t.getAttribute('onclick') && t.getAttribute('onclick').includes('titans')));
        
        const beforeClick = {
          hasTitanBtn: !!titanBtn,
          btnText: titanBtn ? titanBtn.innerText : null,
          btnOnclick: titanBtn ? titanBtn.getAttribute('onclick') : null,
          titansContentExists: !!document.getElementById('titans'),
          titansActiveBefore: document.getElementById('titans') ? document.getElementById('titans').classList.contains('active') : false
        };

        if (titanBtn) {
          titanBtn.click();
        }

        const afterClick = {
          titansActiveAfter: document.getElementById('titans') ? document.getElementById('titans').classList.contains('active') : false,
          titansDisplay: document.getElementById('titans') ? window.getComputedStyle(document.getElementById('titans')).display : null,
          titansHeight: document.getElementById('titans') ? document.getElementById('titans').clientHeight : 0,
          titansWidth: document.getElementById('titans') ? document.getElementById('titans').clientWidth : 0,
          titansInnerHTMLSample: document.getElementById('titans') ? document.getElementById('titans').innerHTML.substring(0, 300) : null
        };

        return { beforeClick, afterClick };
      })()`,
      returnByValue: true
    });

    console.log('TITANS_TEST:', JSON.stringify(titansTest ? titansTest.value : titansTest, null, 2));

    // Capture screenshot of titans tab
    const shot = await send('Page.captureScreenshot', { format: 'png' });
    fs.writeFileSync('C:/Users/SK/.gemini/antigravity/brain/49bcdc7d-9012-4831-93a6-42d8b11a6533/shot_titans_tab_click.png', Buffer.from(shot.data, 'base64'));
    console.log('SHOT_SAVED');

    ws.close();
    chrome.kill();
  } catch (err) {
    console.error('ERROR:', err);
    chrome.kill();
    process.exit(1);
  }
}, 500);

