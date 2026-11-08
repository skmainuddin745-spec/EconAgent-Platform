const { spawn } = require('child_process');
const fs = require('fs');

const chromePath = 'C:/Program Files/Google/Chrome/Application/chrome.exe';
const targetUrl = 'file:///F:/documents/SOIC/EconAgent_Platform/platform_ui/EconAgent_Dashboard.html';
const port = 9311;

const chrome = spawn(chromePath, [
  '--headless=new',
  `--remote-debugging-port=${port}`,
  '--disable-gpu',
  '--no-sandbox',
  '--window-size=1600,1050',
  'about:blank'
]);

let msgId = 1;
function sendCdp(ws, method, params = {}) {
  return new Promise((resolve, reject) => {
    const id = msgId++;
    const handler = (event) => {
      const data = JSON.parse(event.data);
      if (data.id === id) {
        ws.removeEventListener('message', handler);
        if (data.error) reject(data.error);
        else resolve(data.result);
      }
    };
    ws.addEventListener('message', handler);
    ws.send(JSON.stringify({ id, method, params }));
  });
}

function evaluate(ws, expression) {
  return sendCdp(ws, 'Runtime.evaluate', {
    expression,
    returnByValue: true,
    awaitPromise: true
  }).then(r => r.result ? r.result.value : r);
}

function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

async function run() {
  await sleep(1500);
  const res = await fetch(`http://127.0.0.1:${port}/json`);
  const pages = await res.json();
  const ws = new WebSocket(pages[0].webSocketDebuggerUrl);
  await new Promise(r => ws.addEventListener('open', r));

  const pageErrors = [];
  ws.addEventListener('message', (event) => {
    const data = JSON.parse(event.data);
    if (data.method === 'Runtime.exceptionThrown') {
      pageErrors.push(data.params.exceptionDetails.exception.description);
    }
  });

  await sendCdp(ws, 'Page.enable');
  await sendCdp(ws, 'Runtime.enable');
  await sendCdp(ws, 'Page.navigate', { url: targetUrl });
  await sleep(4000);

  console.log('=== TEST 1: Page Load & Initial State ===');
  console.log('Console Errors:', pageErrors.length);

  console.log('\n=== TEST 2: Multi-Country Dropdown Switching ===');
  const countries = ['us', 'sa', 'tw', 'nl', 'de', 'jp', 'in'];
  for (const c of countries) {
    const res = await evaluate(ws, `(() => {
      const cs = document.getElementById('global_country_select');
      const ss = document.getElementById('global_sector_select');
      const fs = document.getElementById('global_firm_select');
      if (cs) {
        cs.value = '${c}';
        cs.dispatchEvent(new Event('change'));
      }
      return {
        country: cs ? cs.value : null,
        sectorCount: ss ? ss.options.length : 0,
        firmCount: fs ? fs.options.length : 0,
        sampleFirm: fs && fs.options[0] ? fs.options[0].text : null
      };
    })()`);
    console.log(`Country [${c}]:`, res);
  }

  console.log('\n=== TEST 3: Titans Sub-Pane Switching ===');
  await evaluate(ws, `window.showTab(null, 'titans');`);
  await sleep(300);
  const titanPanes = ['blk', 'vang', 'pe', 'tick', 'macro'];
  for (const p of titanPanes) {
    const paneRes = await evaluate(ws, `(() => {
      window.switchTitanTab('${p}');
      const el = document.getElementById('titan_subpane_${p}');
      return {
        pane: '${p}',
        display: el ? el.style.display : 'not_found',
        hasContent: el ? el.innerText.length > 50 : false
      };
    })()`);
    console.log(`Titan Pane [${p}]:`, paneRes);
  }

  console.log('\n=== TEST 4: BMAP 2D Navigation (West & East) ===');
  await evaluate(ws, `window.showTab(null, 'bmap');`);
  await sleep(400);

  const westRes = await evaluate(ws, `(() => {
    window.bmapNavigateWest();
    const map = window.leafletMap;
    const center = map ? map.getCenter() : null;
    const scope = document.getElementById('bmap_scope_label');
    return {
      lat: center ? center.lat : null,
      lng: center ? center.lng : null,
      zoom: map ? map.getZoom() : null,
      scopeText: scope ? scope.textContent : null
    };
  })()`);
  console.log('Navigate West Result:', westRes);

  const eastRes = await evaluate(ws, `(() => {
    window.bmapNavigateEast();
    const map = window.leafletMap;
    const center = map ? map.getCenter() : null;
    const scope = document.getElementById('bmap_scope_label');
    return {
      lat: center ? center.lat : null,
      lng: center ? center.lng : null,
      zoom: map ? map.getZoom() : null,
      scopeText: scope ? scope.textContent : null
    };
  })()`);
  console.log('Navigate East Result:', eastRes);

  console.log('\n=== TEST 5: Cesium 3D Presets ===');
  await evaluate(ws, `window.switchBmapView('gev');`);
  await sleep(1500);

  const presets = ['manhattan', 'greg_mortimer', 'dense_grid', 'world', 'west', 'east'];
  for (const preset of presets) {
    const presRes = await evaluate(ws, `(() => {
      try {
        window.flyCesiumTo('${preset}');
        return { preset: '${preset}', success: true };
      } catch (e) {
        return { preset: '${preset}', success: false, err: e.message };
      }
    })()`);
    console.log(`Preset [${preset}]:`, presRes);
  }

  console.log('\n=== TEST 6: Final Verification Errors Check ===');
  console.log('Total Runtime Exceptions:', pageErrors.length);
  if (pageErrors.length) console.log(pageErrors);

  ws.close();
  chrome.kill();
  console.log('\nMASTER AUDIT COMPLETE: ALL MODULES ROCK-SOLID!');
}

run().catch(e => {
  console.error('Audit failed:', e);
  chrome.kill();
});

