const { spawn } = require('child_process');

const chromePath = 'C:/Program Files/Google/Chrome/Application/chrome.exe';
const targetUrl = 'file:///F:/documents/SOIC/EconAgent_Platform/platform_ui/EconAgent_Dashboard.html';

const chrome = spawn(chromePath, [
  '--headless=new',
  '--remote-debugging-port=9230',
  '--disable-gpu',
  '--no-sandbox',
  '--window-size=1600,1000',
  'about:blank'
]);

let msgId = 1;
function sendCdp(ws, method, params = {}) {
  return new Promise((resolve) => {
    const id = msgId++;
    const handler = (event) => {
      const data = JSON.parse(event.data);
      if (data.id === id) {
        ws.removeEventListener('message', handler);
        resolve(data.result);
      }
    };
    ws.addEventListener('message', handler);
    ws.send(JSON.stringify({ id, method, params }));
  });
}

setTimeout(async () => {
  try {
    const listRes = await fetch('http://127.0.0.1:9230/json/new?' + encodeURIComponent(targetUrl), { method: 'PUT' });
    const targetData = await listRes.json();
    const ws = new WebSocket(targetData.webSocketDebuggerUrl);

    const exceptions = [];
    const consoleErrors = [];

    ws.onopen = async () => {
      await sendCdp(ws, 'Console.enable');
      await sendCdp(ws, 'Runtime.enable');
      await sendCdp(ws, 'Page.enable');

      ws.addEventListener('message', (event) => {
        const msg = JSON.parse(event.data);
        if (msg.method === 'Console.messageAdded' && msg.params.message.level === 'error') {
          consoleErrors.push(msg.params.message.text);
        }
        if (msg.method === 'Runtime.exceptionThrown') {
          exceptions.push(msg.params.exceptionDetails.text + ': ' + msg.params.exceptionDetails.exception?.description);
        }
      });

      await new Promise(r => setTimeout(r, 2500));

      // Test switching to soic_sectors tab
      const sectorRes = await sendCdp(ws, 'Runtime.evaluate', {
        expression: `
          (() => {
            showTab(null, 'soic_sectors');
            const el = document.getElementById('soic_sectors');
            const rows = document.querySelectorAll('#damodaran_table_body tr');
            const countDisp = document.getElementById('damo_count_display')?.innerText;
            return {
              display: window.getComputedStyle(el).display,
              height: el.offsetHeight,
              rowCount: rows.length,
              countDisplay: countDisp,
              firstRowName: rows[0]?.children[0]?.innerText,
              firstRowWacc: rows[0]?.children[4]?.innerText
            };
          })()
        `,
        returnByValue: true
      });
      console.log('=== DAMODARAN 94 TABLE AUDIT ===');
      console.log(sectorRes.result.value);

      // Test 48k company search for AAPL and NVDA
      const searchRes = await sendCdp(ws, 'Runtime.evaluate', {
        expression: `
          (() => {
            switchSoicSectorTab('lookup');
            const input = document.getElementById('company_lookup_input');
            input.value = 'AAPL';
            searchGlobalCompanies();
            const cards = Array.from(document.querySelectorAll('#company_search_results > div')).map(c => c.innerText.replace(/\\n/g, ' '));
            return {
              searchQuery: 'AAPL',
              resultCount: cards.length,
              firstResult: cards[0]
            };
          })()
        `,
        returnByValue: true
      });
      console.log('=== 48K COMPANY LOOKUP AUDIT ===');
      console.log(searchRes.result.value);

      // Test Semi Subpane & Simulator
      const semiRes = await sendCdp(ws, 'Runtime.evaluate', {
        expression: `
          (() => {
            switchSoicSectorTab('semi');
            const slider = document.getElementById('slider_semi_tam');
            slider.value = 40;
            updateSemiSim();
            return {
              bearIRR: document.getElementById('semi_bear_irr')?.innerText,
              baseIRR: document.getElementById('semi_base_irr')?.innerText,
              bullIRR: document.getElementById('semi_bull_irr')?.innerText
            };
          })()
        `,
        returnByValue: true
      });
      console.log('=== SEMICONDUCTORS SIMULATOR AUDIT ===');
      console.log(semiRes.result.value);

      // Capture screenshot of the Damodaran 94 matrix
      await sendCdp(ws, 'Runtime.evaluate', {
        expression: `
          switchSoicSectorTab('damodaran');
          window.scrollTo(0, 300);
        `
      });
      await new Promise(r => setTimeout(r, 400));
      const shot = await sendCdp(ws, 'Page.captureScreenshot', { format: 'png' });
      const fs = require('fs');
      fs.writeFileSync('F:/documents/SOIC/EconAgent_Platform/platform_ui/shot_global_damodaran_94.png', Buffer.from(shot.data, 'base64'));
      console.log('Saved shot_global_damodaran_94.png (' + shot.data.length + ' bytes)');

      console.log(`\nExceptions logged: ${exceptions.length}`);
      exceptions.forEach(e => console.log('  EXC:', e));
      console.log(`Console errors logged: ${consoleErrors.length}`);
      consoleErrors.forEach(e => console.log('  ERR:', e));

      ws.close();
      chrome.kill();
      process.exit(0);
    };
  } catch (e) {
    console.error(e);
    chrome.kill();
    process.exit(1);
  }
}, 1500);

