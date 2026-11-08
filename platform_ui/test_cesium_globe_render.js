const { spawn } = require('child_process');
const fs = require('fs');

const chrome = spawn('C:/Program Files/Google/Chrome/Application/chrome.exe', [
  '--headless=new', '--remote-debugging-port=9297', '--disable-gpu', '--no-sandbox', '--window-size=1600,1050', 'about:blank'
]);

setTimeout(async () => {
  try {
    let ws = null;
    for (let i = 0; i < 20; i++) {
      try {
        const res = await fetch('http://127.0.0.1:9297/json');
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
    await new Promise(r => setTimeout(r, 4000));

    // Show BMAP tab, switch to GEV
    await send('Runtime.evaluate', {
      expression: `(() => {
        window.showTab(null, 'bmap');
        window.switchBmapView('gev');
      })()`
    });

    await new Promise(r => setTimeout(r, 4000));

    // Check Cesium container DOM and Cesium Viewer state
    const res = await send('Runtime.evaluate', {
      expression: `(() => {
        const container = document.getElementById('gev_native_cesium_container');
        const canvas = container ? container.querySelector('canvas') : null;
        return {
          containerExists: !!container,
          containerOffsetWidth: container ? container.offsetWidth : 0,
          containerOffsetHeight: container ? container.offsetHeight : 0,
          canvasExists: !!canvas,
          canvasWidth: canvas ? canvas.width : 0,
          canvasHeight: canvas ? canvas.height : 0,
          hasViewer: typeof window.nativeCesiumViewer !== 'undefined' && window.nativeCesiumViewer !== null,
          viewerSceneMode: window.nativeCesiumViewer && window.nativeCesiumViewer.scene ? window.nativeCesiumViewer.scene.mode : null,
          entityCount: window.nativeCesiumViewer && window.nativeCesiumViewer.entities ? window.nativeCesiumViewer.entities.values.length : 0,
          cameraPos: window.nativeCesiumViewer && window.nativeCesiumViewer.camera ? {
            heading: window.nativeCesiumViewer.camera.heading,
            pitch: window.nativeCesiumViewer.camera.pitch
          } : null
        };
      })()`,
      returnByValue: true
    });

    console.log('CESIUM_STATUS:', JSON.stringify(res && res.result ? res.result.value : res, null, 2));

    // Scroll container into view and take screenshot of the 3D globe!
    await send('Runtime.evaluate', {
      expression: `document.getElementById('gev_native_cesium_container').scrollIntoView();`
    });
    await new Promise(r => setTimeout(r, 1000));

    const shot = await send('Page.captureScreenshot', { format: 'png' });
    fs.writeFileSync('C:/Users/SK/.gemini/antigravity/brain/49bcdc7d-9012-4831-93a6-42d8b11a6533/shot_cesium_globe_verified.png', Buffer.from(shot.data, 'base64'));
    console.log('SHOT_CESIUM_GLOBE_VERIFIED_SAVED');

    ws.close();
    chrome.kill();
  } catch (err) {
    console.error('ERROR:', err);
    chrome.kill();
  }
}, 500);

