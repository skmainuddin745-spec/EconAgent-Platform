const { spawn } = require('child_process');
const fs = require('fs');

const chromePath = 'C:/Program Files/Google/Chrome/Application/chrome.exe';
const targetUrl = 'file:///F:/documents/SOIC/EconAgent_Platform/platform_ui/EconAgent_Dashboard.html';
const port = 9299;

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

  console.log('=== PAGE LOAD ERRORS ===');
  console.log('Errors count:', pageErrors.length);
  if (pageErrors.length) console.log(pageErrors.slice(0, 5));

  // 1. Audit Tab Switching (especially titans, technicals, soic_sectors, topnotch)
  console.log('\n=== TESTING TAB SWITCHING ===');
  const tabsToTest = ['titans', 'technicals', 'soic_sectors', 'topnotch', 'soic', 'bmap'];
  for (const tabId of tabsToTest) {
    const status = await evaluate(ws, `(() => {
      window.showTab(null, '${tabId}');
      const el = document.getElementById('${tabId}');
      if (!el) return { found: false };
      const cs = window.getComputedStyle(el);
      return {
        found: true,
        isActive: el.classList.contains('active'),
        display: cs.display,
        visibility: cs.visibility,
        height: el.clientHeight,
        textLen: el.innerText.trim().length,
        firstLine: el.innerText.trim().substring(0, 80)
      };
    })()`);
    console.log(`Tab [${tabId}]:`, status);
  }

  // 2. Audit Global Wall Street Dropdowns
  console.log('\n=== TESTING GLOBAL WALL STREET DROPDOWNS ===');
  const globalDropStatus = await evaluate(ws, `(() => {
    const cSelect = document.getElementById('global_country_select');
    const sSelect = document.getElementById('global_sector_select');
    const fSelect = document.getElementById('global_firm_select');
    
    if (cSelect) {
      cSelect.value = 'us';
      cSelect.dispatchEvent(new Event('change'));
    }

    return {
      country: cSelect ? cSelect.value : null,
      sectorCount: sSelect ? sSelect.options.length : 0,
      firstSector: sSelect && sSelect.options[0] ? sSelect.options[0].text : null,
      firmCount: fSelect ? fSelect.options.length : 0,
      firms: fSelect ? Array.from(fSelect.options).map(o => o.text).slice(0, 6) : []
    };
  })()`);
  console.log('US Selection Status:', globalDropStatus);

  // 3. Audit BMAP 2D Map & Sublayer Aliases & Bank Filter
  console.log('\n=== TESTING BMAP 2D MAP & SUBLAYERS ===');
  await evaluate(ws, `(() => { window.showTab(null, 'bmap'); })()`);
  await sleep(1000);

  const bmapStatus = await evaluate(ws, `(() => {
    // Test Natural Gas sublayer checkboxes
    window.toggleSubLayer('underground_storage', true);
    window.toggleSubLayer('lng_berths', true);
    window.toggleSubLayer('hubs', true);

    const hasUnderground = !!window.datasetLayerGroups['underground_storage'];
    const hasLngBerths = !!window.datasetLayerGroups['lng_berths'];
    const hasHubs = !!window.datasetLayerGroups['hubs'];

    // Test bank filter with JPMorgan Chase
    const nameSelect = document.getElementById('filter_bank_name');
    if (nameSelect) {
      nameSelect.value = 'JPMorgan Chase';
      window.filterBankBranches();
    }
    const lblJpm = document.getElementById('lbl_bank_dep_val');

    // Reset bank filter
    window.resetBankFilter();
    const lblAll = document.getElementById('lbl_bank_dep_val');

    return {
      hasUnderground,
      hasLngBerths,
      hasHubs,
      jpmResult: lblJpm ? lblJpm.textContent : null,
      allResult: lblAll ? lblAll.textContent : null
    };
  })()`);
  console.log('BMAP Sublayers & Bank Filter:', bmapStatus);

  // 4. Audit Native Cesium 3D Workstation
  console.log('\n=== TESTING NATIVE CESIUM 3D WORKSTATION ===');
  await evaluate(ws, `window.switchBmapView('gev');`);
  await sleep(1800);

  const gevStatus = await evaluate(ws, `(() => {
    const v = window.nativeCesiumViewer;
    const gevCont = document.getElementById('bmap_view_container_gev');
    const tb2d = document.getElementById('bmap_2d_secondary_toolbar');
    return {
      gevDisplay: gevCont ? gevCont.style.display : null,
      toolbar2dHidden: tb2d ? (tb2d.style.display === 'none') : false,
      hasViewer: !!v,
      entitiesCount: v && v.entities ? v.entities.values.length : 0,
      sceneMode: v && v.scene ? v.scene.mode : null,
      canvasWidth: v && v.canvas ? v.canvas.width : 0,
      canvasHeight: v && v.canvas ? v.canvas.height : 0
    };
  })()`);
  console.log('Cesium 3D Status:', gevStatus);

  // Capture Screenshot of Cesium 3D
  const shotData = await sendCdp(ws, 'Page.captureScreenshot', { format: 'png' });
  fs.writeFileSync('C:/Users/SK/.gemini/antigravity/brain/49bcdc7d-9012-4831-93a6-42d8b11a6533/shot_verify_everything_flawless.png', Buffer.from(shotData.data, 'base64'));
  console.log('\nScreenshot saved to shot_verify_everything_flawless.png');

  ws.close();
  chrome.kill();
}

run().catch(e => {
  console.error('Run failed:', e);
  chrome.kill();
});
