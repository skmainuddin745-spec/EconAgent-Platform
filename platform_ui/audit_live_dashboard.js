const { spawn } = require('child_process');
const fs = require('fs');

const chrome = spawn('C:/Program Files/Google/Chrome/Application/chrome.exe', [
  '--headless=new', '--remote-debugging-port=9292', '--disable-gpu', '--no-sandbox', '--window-size=1600,1050', 'about:blank'
]);

setTimeout(async () => {
  try {
    let ws = null;
    for (let i = 0; i < 20; i++) {
      try {
        const res = await fetch('http://127.0.0.1:9292/json');
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

    const check1 = await send('Runtime.evaluate', {
      expression: `(() => ({
        title: document.title,
        hasShowTab: typeof window.showTab,
        hasInitNativeCesiumViewer: typeof window.initNativeCesiumViewer,
        hasSwitchBmapView: typeof window.switchBmapView,
        hasCesium: typeof window.Cesium,
        hasGevNative: !!document.getElementById("gev_native_cesium_container"),
        hasOfflineBox: !!document.getElementById("gev_offline_box"),
        tabs: Array.from(document.querySelectorAll(".terminal-tab, .tab-btn")).map(t => t.innerText.trim()).filter(Boolean)
      }))()`,
      returnByValue: true
    });

    console.log('INITIAL_CHECK:', JSON.stringify(check1 && check1.result ? check1.result.value : check1, null, 2));

    // Switch to bmap and then gev
    await send('Runtime.evaluate', {
      expression: `(() => {
        if (typeof window.showTab === "function") window.showTab("bmap");
        if (typeof window.switchBmapView === "function") window.switchBmapView("gev");
      })()`
    });

    await new Promise(r => setTimeout(r, 4000));

    const shot = await send('Page.captureScreenshot', { format: 'png' });
    fs.writeFileSync('C:/Users/SK/.gemini/antigravity/brain/49bcdc7d-9012-4831-93a6-42d8b11a6533/shot_live_gev_audit.png', Buffer.from(shot.data, 'base64'));

    const check2 = await send('Runtime.evaluate', {
      expression: `(() => {
        const gev = document.getElementById("gev_native_cesium_container");
        return {
          gevDisplay: gev ? window.getComputedStyle(gev).display : null,
          gevHeight: gev ? gev.clientHeight : 0,
          gevWidth: gev ? gev.clientWidth : 0,
          hasNativeCesiumViewer: typeof window.nativeCesiumViewer !== "undefined" && window.nativeCesiumViewer !== null,
          entityCount: (window.nativeCesiumViewer && window.nativeCesiumViewer.entities) ? window.nativeCesiumViewer.entities.values.length : 0,
          offlineBoxDisplay: document.getElementById("gev_offline_box") ? window.getComputedStyle(document.getElementById("gev_offline_box")).display : null
        };
      })()`,
      returnByValue: true
    });

    console.log('GEV_CHECK_AFTER_SWITCH:', JSON.stringify(check2 && check2.result ? check2.result.value : check2, null, 2));
    console.log('TOTAL_CONSOLE_LOGS:', consoleLogs.length);
    if (consoleLogs.length > 0) {
      console.log('LOGS:\n', consoleLogs.join('\n'));
    }

    ws.close();
    chrome.kill();
  } catch (err) {
    console.error('ERROR:', err);
    chrome.kill();
    process.exit(1);
  }
}, 500);
