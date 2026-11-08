const { spawn } = require('child_process');

const chrome = spawn('C:/Program Files/Google/Chrome/Application/chrome.exe', [
  '--headless=new', '--remote-debugging-port=9282', '--disable-gpu', '--no-sandbox', '--window-size=1600,1050', 'about:blank'
]);

setTimeout(async () => {
  try {
    let ws = null;
    for (let i = 0; i < 20; i++) {
      try {
        const res = await fetch('http://127.0.0.1:9282/json');
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

    const res = await send('Runtime.evaluate', {
      expression: `(() => {
        const logs = [];
        const secSelect = document.getElementById('global_sector_select');
        logs.push('1. secSelect exists: ' + !!secSelect);
        
        secSelect.innerHTML = '';
        logs.push('2. cleared secSelect, length now: ' + secSelect.options.length);

        const damoSectors = window.GLOBAL_DAMODARAN_SECTORS;
        logs.push('3. damoSectors is object: ' + (typeof damoSectors === 'object'));
        logs.push('4. damoSectors keys count: ' + Object.keys(damoSectors).length);

        Object.keys(damoSectors).forEach(secGroup => {
          const optGroup = document.createElement('optgroup');
          optGroup.label = '── ' + secGroup.toUpperCase() + ' ──';
          const inds = damoSectors[secGroup];
          inds.forEach(ind => {
            const opt = document.createElement('option');
            opt.value = ind.name;
            opt.textContent = ind.name + ' (Beta ' + ind.beta.toFixed(2) + ' · WACC ' + ind.wacc.toFixed(1) + '% · Margin ' + ind.ebitMargin.toFixed(1) + '%)';
            optGroup.appendChild(opt);
          });
          secSelect.appendChild(optGroup);
        });

        logs.push('5. populated secSelect, length now: ' + secSelect.options.length);

        return logs;
      })()`,
      returnByValue: true
    });
    console.log('MANUAL_STEP_LOGS:\n', res.result.value.join('\n'));

    ws.close();
    chrome.kill();
  } catch (e) {
    console.error(e);
    chrome.kill();
  }
}, 500);

