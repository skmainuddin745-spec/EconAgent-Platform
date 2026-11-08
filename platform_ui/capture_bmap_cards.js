const { spawn } = require('child_process');
const fs = require('fs');

const chromePath = 'C:/Program Files/Google/Chrome/Application/chrome.exe';
const targetUrl = 'file:///F:/documents/SOIC/EconAgent_Platform/platform_ui/EconAgent_Dashboard.html';
const port = 9340;

const chrome = spawn(chromePath, [
  '--headless=new',
  `--remote-debugging-port=${port}`,
  '--disable-gpu',
  '--no-sandbox',
  '--window-size=1600,1050',
  'about:blank'
]);

async function sleep(ms) { return new Promise(r => setTimeout(r, ms)); }

async function main() {
  await sleep(1500);
  const res = await fetch(`http://127.0.0.1:${port}/json`);
  const pages = await res.json();
  const ws = new WebSocket(pages[0].webSocketDebuggerUrl);
  await new Promise(r => ws.addEventListener('open', r));

  let msgId = 1;
  function sendCdp(method, params = {}) {
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

  await sendCdp('Page.enable');
  await sendCdp('Runtime.enable');
  await sendCdp('Page.navigate', { url: targetUrl });
  await sleep(2500);

  // Switch to BMAP and scroll map into view
  await sendCdp('Runtime.evaluate', {
    expression: `(function() {
      var tabs = Array.from(document.querySelectorAll('button, div, span'));
      var bTab = tabs.find(el => el.textContent && el.textContent.includes('BMAP Tankers'));
      if (bTab) bTab.click();
      
      var mapWrap = document.getElementById('bmap_map_wrapper') || document.getElementById('bmap_view_container_map');
      if (mapWrap) mapWrap.scrollIntoView({ behavior: 'instant', block: 'center' });

      // Open drawer
      var drawer = document.getElementById('bmap_map_content_drawer');
      if (drawer) {
        drawer.style.display = 'flex';
        drawer.style.transform = 'translateX(0)';
      }

      // Slider at 4700M
      var slider = document.getElementById('slider_bank_dep');
      if (slider) {
        slider.value = 4700;
        if (typeof window.filterBankBranches === 'function') window.filterBankBranches();
      }
    })()`,
    awaitPromise: true
  });
  await sleep(1500);

  const shot = await sendCdp('Page.captureScreenshot', { format: 'png' });
  fs.writeFileSync('C:/Users/SK/.gemini/antigravity/brain/49bcdc7d-9012-4831-93a6-42d8b11a6533/shot_bmap_drawer_cards_perfect.png', Buffer.from(shot.data, 'base64'));
  console.log('Saved shot_bmap_drawer_cards_perfect.png');

  ws.close();
  chrome.kill();
  process.exit(0);
}

main();

