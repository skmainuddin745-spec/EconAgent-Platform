const { spawn } = require('child_process');

const chromePath = 'C:/Program Files/Google/Chrome/Application/chrome.exe';
const targetUrl = 'file:///F:/documents/SOIC/EconAgent_Platform/platform_ui/EconAgent_Dashboard.html';

const chrome = spawn(chromePath, [
  '--headless=new',
  '--remote-debugging-port=9226',
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
    const listRes = await fetch('http://127.0.0.1:9226/json/new?' + encodeURIComponent(targetUrl), { method: 'PUT' });
    const targetData = await listRes.json();
    const ws = new WebSocket(targetData.webSocketDebuggerUrl);

    ws.onopen = async () => {
      await sendCdp(ws, 'Runtime.enable');
      await sendCdp(ws, 'Page.enable');

      await new Promise(r => setTimeout(r, 2000));

      // 1. Technicals Canvas Test
      const techRes = await sendCdp(ws, 'Runtime.evaluate', {
        expression: `
          (() => {
            showTab(null, 'technicals');
            if (typeof drawTechnicalsChart === 'function') drawTechnicalsChart();
            const c = document.getElementById('technicalsCanvas');
            if (!c) return { error: 'technicalsCanvas not found' };
            const ctx = c.getContext('2d');
            const imgData = ctx.getImageData(0, 0, c.width, c.height);
            let nonZero = 0;
            for (let i = 3; i < imgData.data.length; i += 4) {
              if (imgData.data[i] > 0) nonZero++;
            }
            return {
              width: c.width,
              height: c.height,
              nonZeroPixels: nonZero,
              totalPixels: c.width * c.height,
              fillPercent: ((nonZero / (c.width * c.height)) * 100).toFixed(2) + '%',
              stock: document.getElementById('tech_stock_select')?.value,
              price: document.getElementById('tech_price_display')?.innerText,
              wma: document.getElementById('tech_card_wma')?.innerText,
              stage: document.getElementById('tech_card_stage')?.innerText
            };
          })()
        `,
        returnByValue: true
      });
      console.log('=== TECHNICALS CANVAS RESULT ===');
      console.log(techRes.result.value);

      // 2. Titans Macro Transmission Test
      const titanRes = await sendCdp(ws, 'Runtime.evaluate', {
        expression: `
          (() => {
            showTab(null, 'titans');
            if (typeof switchTitanTab === 'function') switchTitanTab('macro');
            const slider = document.getElementById('macro_slider_copper');
            if (slider) {
              slider.value = 15;
              if (typeof runMacroTransmissionSim === 'function') runMacroTransmissionSim();
            }
            return {
              activeSubpaneDisplay: window.getComputedStyle(document.getElementById('titan_subpane_macro')).display,
              copperVal: document.getElementById('macro_val_copper')?.innerText,
              polycabImpact: document.getElementById('sim_polycab_ebitda')?.innerText,
              keiImpact: document.getElementById('sim_kei_ebitda')?.innerText,
              aramcoImpact: document.getElementById('sim_aramco_ebitda')?.innerText,
              nvdaImpact: document.getElementById('sim_nvda_wacc')?.innerText
            };
          })()
        `,
        returnByValue: true
      });
      console.log('=== TITANS MACRO TRANSMISSION RESULT ===');
      console.log(titanRes.result.value);

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

