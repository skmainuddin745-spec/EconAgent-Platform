const { spawn } = require('child_process');
const fs = require('fs');

const chromePath = 'C:/Program Files/Google/Chrome/Application/chrome.exe';
const targetUrl = 'file:///F:/documents/SOIC/EconAgent_Platform/platform_ui/Bloomberg_BMAP_Terminal.html';
const port = 9245;

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
  const wsUrl = pages[0].webSocketDebuggerUrl;
  const ws = new WebSocket(wsUrl);

  await new Promise(r => ws.addEventListener('open', r));

  const consoleErrors = [];
  ws.addEventListener('message', (event) => {
    const data = JSON.parse(event.data);
    if (data.method === 'Runtime.consoleAPICalled' && data.params.type === 'error') {
      consoleErrors.push(data.params.args.map(a => a.value || a.description).join(' '));
    }
  });

  await sendCdp(ws, 'Runtime.enable');
  await sendCdp(ws, 'Page.enable');

  console.log(`Navigating to ${targetUrl}...`);
  await sendCdp(ws, 'Page.navigate', { url: targetUrl });
  await sleep(3500);

  // 1. Check Console Errors
  console.log(`Console Errors count: ${consoleErrors.length}`);
  if (consoleErrors.length > 0) {
    console.log('Console Errors:', consoleErrors);
  }

  // 2. Test Bank Branches Slider at $4700M+
  console.log('\n--- TEST 1: Bank Branches Slider at $4700M+ ---');
  const sliderTest = await evaluate(ws, `(() => {
    var slider = document.getElementById('slider_bank_dep');
    if (!slider) return { error: 'slider_bank_dep not found' };
    slider.value = 4700;
    window.filterBankBranches();
    var lbl = document.getElementById('lbl_bank_dep_val');
    var group = datasetLayerGroups['bank_branches'];
    var layerCount = group ? Object.keys(group._layers || {}).length : 0;
    return {
      sliderVal: slider.value,
      labelText: lbl ? lbl.textContent : null,
      renderedMarkers: layerCount
    };
  })()`);
  console.log('Slider test result:', JSON.stringify(sliderTest, null, 2));

  // 3. Test Petroline (Blue line) Universal Inspector
  console.log('\n--- TEST 2: Petroline (Blue Line) Universal Inspector ---');
  const petrolineTest = await evaluate(ws, `(() => {
    var petro = crudePipelines.find(p => p.id === 'pipe_petroline');
    if (!petro) return { error: 'pipe_petroline not found' };
    window.showUniversalInspector('pipeline', petro, [24.0, 45.0]);
    var pop = document.getElementById('bmap_universal_vessel_popup');
    return {
      name: document.getElementById('uni_vessel_name').textContent,
      type: document.getElementById('uni_vessel_type').textContent,
      status: document.getElementById('uni_vessel_status').textContent,
      dest: document.getElementById('uni_vessel_dest').textContent,
      draftDwt: document.getElementById('uni_vessel_draft_dwt').textContent,
      display: pop.style.display,
      borderColor: pop.style.borderColor
    };
  })()`);
  console.log('Petroline Inspector result:', JSON.stringify(petrolineTest, null, 2));

  // Screenshot Petroline Inspector
  const shot1 = await sendCdp(ws, 'Page.captureScreenshot', { format: 'png' });
  fs.writeFileSync('C:/Users/SK/.gemini/antigravity/brain/49bcdc7d-9012-4831-93a6-42d8b11a6533/shot_bmap_petroline_inspector.png', Buffer.from(shot1.data, 'base64'));
  console.log('Saved shot_bmap_petroline_inspector.png');

  // 4. Test Saudi Tadawul TASI (Green bubble) Universal Inspector
  console.log('\n--- TEST 3: Saudi Tadawul TASI (Green Bubble) Universal Inspector ---');
  const tadawulTest = await evaluate(ws, `(() => {
    var tasi = worldEquityData.find(e => e.code === 'SA');
    if (!tasi) return { error: 'TASI equity not found' };
    window.showUniversalInspector('equity', tasi, [24.0, 45.0]);
    var pop = document.getElementById('bmap_universal_vessel_popup');
    return {
      name: document.getElementById('uni_vessel_name').textContent,
      type: document.getElementById('uni_vessel_type').textContent,
      status: document.getElementById('uni_vessel_status').textContent,
      owner: document.getElementById('uni_vessel_owner').textContent,
      dest: document.getElementById('uni_vessel_dest').textContent,
      berth: document.getElementById('uni_vessel_berth').textContent,
      speed: document.getElementById('uni_vessel_speed').textContent,
      display: pop.style.display
    };
  })()`);
  console.log('Tadawul TASI result:', JSON.stringify(tadawulTest, null, 2));

  // Screenshot Tadawul Inspector
  const shot2 = await sendCdp(ws, 'Page.captureScreenshot', { format: 'png' });
  fs.writeFileSync('C:/Users/SK/.gemini/antigravity/brain/49bcdc7d-9012-4831-93a6-42d8b11a6533/shot_bmap_tadawul_inspector.png', Buffer.from(shot2.data, 'base64'));
  console.log('Saved shot_bmap_tadawul_inspector.png');

  // 5. Test Constellation Grid Node (Yellow Dot) Universal Inspector
  console.log('\n--- TEST 4: Constellation Grid (Yellow Dot) Universal Inspector ---');
  const gridTest = await evaluate(ws, `(() => {
    var node = globalDenseGrid[0];
    window.showUniversalInspector('grid', node, [node.lat, node.lon]);
    var pop = document.getElementById('bmap_universal_vessel_popup');
    return {
      name: document.getElementById('uni_vessel_name').textContent,
      type: document.getElementById('uni_vessel_type').textContent,
      status: document.getElementById('uni_vessel_status').textContent,
      dest: document.getElementById('uni_vessel_dest').textContent,
      display: pop.style.display
    };
  })()`);
  console.log('Grid node result:', JSON.stringify(gridTest, null, 2));

  // 6. Test Submarine Undersea Cables Layer
  console.log('\n--- TEST 5: Submarine Undersea Cables Layer ---');
  const cablesTest = await evaluate(ws, `(() => {
    var cablesCount = (typeof globalSubmarineCables !== 'undefined') ? globalSubmarineCables.length : 0;
    var grp = datasetLayerGroups['submarine_cables'];
    var layerCount = grp ? Object.keys(grp._layers || {}).length : 0;
    // Activate submarine cables layer
    window.addBmapDataset('submarine_cables');
    var isLayerActive = leafletMap.hasLayer(grp);
    return {
      cablesInDataset: cablesCount,
      polylinesRendered: layerCount,
      isLayerActiveOnMap: isLayerActive
    };
  })()`);
  console.log('Submarine cables result:', JSON.stringify(cablesTest, null, 2));

  // Screenshot Submarine Cables
  await sleep(1000);
  const shot3 = await sendCdp(ws, 'Page.captureScreenshot', { format: 'png' });
  fs.writeFileSync('C:/Users/SK/.gemini/antigravity/brain/49bcdc7d-9012-4831-93a6-42d8b11a6533/shot_bmap_submarine_cables.png', Buffer.from(shot3.data, 'base64'));
  console.log('Saved shot_bmap_submarine_cables.png');

  // 7. Test Natural Gas Checkboxes
  console.log('\n--- TEST 6: Natural Gas Sub-layer Toggles ---');
  const natgasTest = await evaluate(ws, `(() => {
    window.toggleSubLayer('storage_terminals', true);
    window.toggleSubLayer('underground_storage', true);
    return {
      storage_active: !!activeLayers.storage_terminals,
      underground_active: !!activeLayers.underground_storage
    };
  })()`);
  console.log('Natural gas toggle result:', JSON.stringify(natgasTest, null, 2));

  ws.close();
  chrome.kill();
  console.log('\nAll tests successfully finished!');
}

run().catch(e => {
  console.error('Test error:', e);
  chrome.kill();
});

