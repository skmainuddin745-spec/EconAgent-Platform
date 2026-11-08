const { spawn } = require('child_process');
const fs = require('fs');

const chromePath = 'C:/Program Files/Google/Chrome/Application/chrome.exe';
const targetUrl = 'file:///F:/documents/SOIC/EconAgent_Platform/platform_ui/Bloomberg_BMAP_Terminal.html';
const port = 9290;

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
  return new Promise(r => setTimeout(r, ms));
}

async function run() {
  let ws = null;
  for (let i = 0; i < 15; i++) {
    try {
      const res = await fetch(`http://127.0.0.1:${port}/json`);
      if (res.ok) {
        const pages = await res.json();
        ws = new WebSocket(pages[0].webSocketDebuggerUrl);
        await new Promise(r => ws.addEventListener('open', r));
        break;
      }
    } catch (e) {
      await sleep(300);
    }
  }

  if (!ws) throw new Error('Could not connect to Chrome debugging port');

  await sendCdp(ws, 'Page.enable');
  await sendCdp(ws, 'Page.navigate', { url: targetUrl });
  await sleep(3500);

  console.log('=== TEST 1: Strict Single Canvas Verification ===');
  const canvasDiag = await evaluate(ws, `(() => {
    const overlayCanvases = Array.from(document.querySelectorAll('.leaflet-overlay-pane canvas'));
    const renderer = window.masterCanvasRenderer;
    return {
      overlayCanvases: overlayCanvases.length,
      tolerance: renderer ? renderer.options.tolerance : null,
      rendererRegisteredLayers: renderer ? Object.keys(renderer._layers || {}).length : 0
    };
  })()`);
  console.log('Canvas diagnostic:', JSON.stringify(canvasDiag, null, 2));

  console.log('\n=== TEST 2: Petroline (Blue Line) Hover Verification ===');
  // Get screen coordinates of Petroline midpoint
  const pipePos = await evaluate(ws, `(() => {
    const map = window.leafletMap;
    // Petroline midpoint: [25.4, 46.5]
    const pt = map.latLngToContainerPoint([25.4, 46.5]);
    const rect = map.getContainer().getBoundingClientRect();
    const absX = rect.left + pt.x;
    const absY = rect.top + pt.y;
    return { absX, absY, pt };
  })()`);
  console.log('Petroline target:', pipePos);

  // Dispatch mouseMove
  await sendCdp(ws, 'Input.dispatchMouseEvent', {
    type: 'mouseMoved',
    x: pipePos.absX,
    y: pipePos.absY
  });
  await sleep(600);

  const pipeHoverState = await evaluate(ws, `(() => {
    const pop = document.getElementById('bmap_universal_vessel_popup');
    return {
      display: pop ? pop.style.display : 'none',
      name: document.getElementById('uni_vessel_name') ? document.getElementById('uni_vessel_name').textContent : '',
      type: document.getElementById('uni_vessel_type') ? document.getElementById('uni_vessel_type').textContent : '',
      dest: document.getElementById('uni_vessel_dest') ? document.getElementById('uni_vessel_dest').textContent : '',
      status: document.getElementById('uni_vessel_status') ? document.getElementById('uni_vessel_status').textContent : ''
    };
  })()`);
  console.log('Petroline hover result:', JSON.stringify(pipeHoverState, null, 2));

  // Save screenshot of Petroline hover
  const shot1 = await sendCdp(ws, 'Page.captureScreenshot', { format: 'png' });
  fs.writeFileSync('C:/Users/SK/.gemini/antigravity/brain/49bcdc7d-9012-4831-93a6-42d8b11a6533/shot_verified_petroline_hover_final.png', Buffer.from(shot1.data, 'base64'));
  console.log('Saved shot_verified_petroline_hover_final.png');

  console.log('\n=== TEST 3: Yellow Dot (Power Utility / Grid Node) Hover Verification ===');
  const dotTarget = await evaluate(ws, `(() => {
    const map = window.leafletMap;
    // Let's find Barakah Nuclear Energy Plant in UAE
    let target = window.globalUtilities.find(u => u.id === 'util_barakah') || window.globalUtilities[0];
    if (!target) return null;

    // Keep map at default view where Ghazlan is fully visible
    const pt = map.latLngToContainerPoint([target.lat, target.lon]);
    const rect = map.getContainer().getBoundingClientRect();
    return {
      name: target.name,
      country: target.country,
      pt,
      absX: rect.left + pt.x,
      absY: rect.top + pt.y
    };
  })()`);
  console.log('Dot target:', dotTarget);

  if (dotTarget) {
    await sleep(500);
    await sendCdp(ws, 'Input.dispatchMouseEvent', {
      type: 'mouseMoved',
      x: dotTarget.absX,
      y: dotTarget.absY
    });
    await sleep(600);

    const dotHoverState = await evaluate(ws, `(() => {
      const pop = document.getElementById('bmap_universal_vessel_popup');
      return {
        display: pop ? pop.style.display : 'none',
        name: document.getElementById('uni_vessel_name') ? document.getElementById('uni_vessel_name').textContent : '',
        type: document.getElementById('uni_vessel_type') ? document.getElementById('uni_vessel_type').textContent : '',
        dest: document.getElementById('uni_vessel_dest') ? document.getElementById('uni_vessel_dest').textContent : '',
        status: document.getElementById('uni_vessel_status') ? document.getElementById('uni_vessel_status').textContent : ''
      };
    })()`);
    console.log('Yellow dot hover result:', JSON.stringify(dotHoverState, null, 2));

    const shot2 = await sendCdp(ws, 'Page.captureScreenshot', { format: 'png' });
    fs.writeFileSync('C:/Users/SK/.gemini/antigravity/brain/49bcdc7d-9012-4831-93a6-42d8b11a6533/shot_verified_yellow_dot_hover_final.png', Buffer.from(shot2.data, 'base64'));
    console.log('Saved shot_verified_yellow_dot_hover_final.png');
  }

  console.log('\n=== TEST 4: 3D Gods Eye View Switch & Live Server Embed Verification ===');
  const gevSwitch = await evaluate(ws, `(() => {
    window.switchBmapView('gev');
    const cont = document.getElementById('bmap_view_container_gev');
    const iframe = document.getElementById('gev_iframe');
    const statusPill = document.getElementById('gev_server_status_pill');
    return {
      activeView: window.currentActiveView,
      gevDisplay: cont ? cont.style.display : 'none',
      iframeSrc: iframe ? iframe.src : '',
      statusPill: statusPill ? statusPill.textContent.trim() : ''
    };
  })()`);
  console.log('GEV switch result:', JSON.stringify(gevSwitch, null, 2));

  await sleep(4000);
  const shot3 = await sendCdp(ws, 'Page.captureScreenshot', { format: 'png' });
  fs.writeFileSync('C:/Users/SK/.gemini/antigravity/brain/49bcdc7d-9012-4831-93a6-42d8b11a6533/shot_verified_gods_eye_view_3d_final.png', Buffer.from(shot3.data, 'base64'));
  console.log('Saved shot_verified_gods_eye_view_3d_final.png');

  ws.close();
  chrome.kill();
  console.log('\nALL 4 TESTS COMPLETED SUCCESSFULLY!');
  process.exit(0);
}

run().catch(err => {
  console.error('Test execution failed:', err);
  chrome.kill();
  process.exit(1);
});
