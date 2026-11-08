const { spawn } = require('child_process');
const fs = require('fs');

const chrome = spawn('C:/Program Files/Google/Chrome/Application/chrome.exe', [
  '--headless=new', '--remote-debugging-port=9296', '--disable-gpu', '--no-sandbox', '--window-size=1600,1050', 'about:blank'
]);

setTimeout(async () => {
  try {
    let ws = null;
    for (let i = 0; i < 20; i++) {
      try {
        const res = await fetch('http://127.0.0.1:9296/json');
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

    // Simulate clicking BMAP tab
    await send('Runtime.evaluate', {
      expression: `(() => {
        const bmapTab = Array.from(document.querySelectorAll('.tab')).find(t => t.innerText.includes('BMAP'));
        if (bmapTab) bmapTab.click();
      })()`
    });
    await new Promise(r => setTimeout(r, 1000));

    // Simulate clicking 3D GOD'S EYE VIEW subtab
    await send('Runtime.evaluate', {
      expression: `(() => {
        const gevBtn = document.getElementById('bmap_btn_view_gev') || Array.from(document.querySelectorAll('button')).find(b => b.innerText.includes(\"GOD'S EYE VIEW\"));
        if (gevBtn) gevBtn.click();
      })()`
    });
    await new Promise(r => setTimeout(r, 3500));

    // Capture screenshot
    const shot = await send('Page.captureScreenshot', { format: 'png' });
    fs.writeFileSync('C:/Users/SK/.gemini/antigravity/brain/49bcdc7d-9012-4831-93a6-42d8b11a6533/shot_user_clicked_gev.png', Buffer.from(shot.data, 'base64'));
    console.log('USER_CLICK_GEV_SHOT_SAVED');

    ws.close();
    chrome.kill();
  } catch (err) {
    console.error('ERROR:', err);
    chrome.kill();
  }
}, 500);

