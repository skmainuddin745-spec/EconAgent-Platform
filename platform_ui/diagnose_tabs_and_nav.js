const { spawn } = require('child_process');
const fs = require('fs');
const path = require('path');

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

    if (!ws) {
      console.error('Failed to connect to Chrome');
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
    await new Promise(r => setTimeout(r, 4000));

    console.log(`Initial exceptions: ${exceptions.length}`);
    exceptions.forEach(ex => console.log('EX:', ex.exceptionDetails.text, ex.exceptionDetails.exception?.description));

    // Evaluate tabs and click Titans tab
    const evalRes = await send('Runtime.evaluate', {
      expression: `(() => {
        const tabs = Array.from(document.querySelectorAll('.tab')).map(t => ({
          text: t.innerText.trim(),
          onclick: t.getAttribute('onclick'),
          className: t.className
        }));
        
        // Find Titans tab
        const titansTab = Array.from(document.querySelectorAll('.tab')).find(t => (t.getAttribute('onclick')||'').includes('titans'));
        let clicked = false;
        if (titansTab) {
          titansTab.click();
          clicked = true;
        }

        const titansDiv = document.getElementById('titans');
        let divInfo = null;
        if (titansDiv) {
          const style = window.getComputedStyle(titansDiv);
          divInfo = {
            id: titansDiv.id,
            className: titansDiv.className,
            display: style.display,
            visibility: style.visibility,
            opacity: style.opacity,
            height: style.height,
            offsetHeight: titansDiv.offsetHeight,
            childrenCount: titansDiv.children.length,
            firstFewChars: titansDiv.innerText.slice(0, 150)
          };
        }

        return { tabs, clicked, divInfo };
      })()`,
      returnByValue: true
    });

    console.log('Eval result on Titans click:', JSON.stringify(evalRes.result.value, null, 2));

    await new Promise(r => setTimeout(r, 1000));

    // Capture screenshot after clicking titans
    const shot = await send('Page.captureScreenshot', { format: 'png' });
    fs.writeFileSync('platform_ui/after_titans_click_test.png', Buffer.from(shot.data, 'base64'));
    console.log('Saved platform_ui/after_titans_click_test.png');

    console.log(`Exceptions after click: ${exceptions.length}`);
    exceptions.forEach(ex => console.log('AFTER CLICK EX:', ex.exceptionDetails.text, ex.exceptionDetails.exception?.description));

    chrome.kill();
    process.exit(0);
  } catch (err) {
    console.error('Error:', err);
    chrome.kill();
    process.exit(1);
  }
}, 1500);

