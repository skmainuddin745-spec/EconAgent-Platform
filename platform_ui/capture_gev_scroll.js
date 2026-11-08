const { spawn } = require('child_process');
const fs = require('fs');

const chrome = spawn('C:/Program Files/Google/Chrome/Application/chrome.exe', [
  '--headless=new', '--remote-debugging-port=9293', '--disable-gpu', '--no-sandbox', '--window-size=1600,1200', 'about:blank'
]);

setTimeout(async () => {
  try {
    let ws = null;
    for (let i = 0; i < 20; i++) {
      try {
        const res = await fetch('http://127.0.0.1:9293/json');
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

    // Show BMAP tab, switch to GEV view, and scroll into view
    await send('Runtime.evaluate', {
      expression: `(() => {
        if (typeof window.showTab === 'function') window.showTab('bmap');
        if (typeof window.switchBmapView === 'function') window.switchBmapView('gev');
        const gev = document.getElementById('bmap_view_container_gev');
        if (gev) gev.scrollIntoView();
      })()`
    });

    await new Promise(r => setTimeout(r, 3500));

    const shot = await send('Page.captureScreenshot', { format: 'png' });
    fs.writeFileSync('C:/Users/SK/.gemini/antigravity/brain/49bcdc7d-9012-4831-93a6-42d8b11a6533/shot_gev_view_scroll.png', Buffer.from(shot.data, 'base64'));

    ws.close();
    chrome.kill();
    console.log('SCREENSHOT_SAVED');
  } catch (e) {
    console.error(e);
    chrome.kill();
  }
}, 500);

