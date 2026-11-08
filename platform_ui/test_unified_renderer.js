const { spawn } = require('child_process');

const chromePath = 'C:/Program Files/Google/Chrome/Application/chrome.exe';
const targetUrl = 'file:///F:/documents/SOIC/EconAgent_Platform/platform_ui/Bloomberg_BMAP_Terminal.html';
const port = 9260;

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

  await sendCdp(ws, 'Page.enable');
  await sendCdp(ws, 'Page.navigate', { url: targetUrl });
  await sleep(3500);

  // Apply single master renderer fix dynamically in the browser to verify!
  const fixRes = await evaluate(ws, `(() => {
    // Create single unified master canvas renderer with tolerance: 14
    var master = L.canvas({ padding: 0.5, tolerance: 14 });

    // Clear all existing layer groups from map
    for (var k in datasetLayerGroups) {
      if (leafletMap.hasLayer(datasetLayerGroups[k])) {
        leafletMap.removeLayer(datasetLayerGroups[k]);
      }
    }

    // Remove old canvas elements
    var oldCanvases = document.querySelectorAll('.leaflet-pane canvas');
    oldCanvases.forEach(c => c.remove());

    // Re-create crude pipelines with master renderer
    var crudeGrp = L.layerGroup();
    crudePipelines.forEach(p => {
      var poly = L.polyline(p.coords, {
        renderer: master,
        color: '#00e5ff',
        weight: 6,
        opacity: 0.95
      });
      poly.on('mouseover mousemove', function(e) {
        window.hoveredPipe = p.name;
        showUniversalInspector('pipeline', p, e.latlng);
      });
      crudeGrp.addLayer(poly);
    });
    crudeGrp.addTo(leafletMap);

    // Re-create power plants (yellow dots) with master renderer
    var yellowGrp = L.layerGroup();
    globalUtilities.forEach(u => {
      var m = L.circleMarker([u.lat, u.lon], {
        renderer: master,
        radius: 6,
        fillColor: '#f59e0b',
        color: '#ffffff',
        weight: 1.5,
        fillOpacity: 0.85
      });
      m.on('mouseover mousemove', function(e) {
        window.hoveredDot = u.name;
        showUniversalInspector('power_plants', u, [u.lat, u.lon]);
      });
      yellowGrp.addLayer(m);
    });
    yellowGrp.addTo(leafletMap);

    // Also make sure legends container doesn't block mouse
    var leg = document.getElementById('bmap_legends_container');
    if (leg) leg.style.pointerEvents = 'none';

    return {
      canvasesNow: document.querySelectorAll('.leaflet-pane canvas').length,
      masterLayers: Object.keys(master._layers).length
    };
  })()`);
  console.log('Unified renderer test setup:', JSON.stringify(fixRes, null, 2));

  // Now test mousemove over Petroline midpoint
  const pipePos = await evaluate(ws, `(() => {
    var rect = document.getElementById('bmap_leaflet_map').getBoundingClientRect();
    var pt = leafletMap.latLngToContainerPoint([25.4, 46.5]);
    return { x: rect.left + pt.x, y: rect.top + pt.y };
  })()`);

  console.log('Moving mouse to Petroline at', pipePos);
  await sendCdp(ws, 'Input.dispatchMouseEvent', {
    type: 'mouseMoved',
    x: pipePos.x,
    y: pipePos.y
  });
  await sleep(500);

  const hoverTest = await evaluate(ws, `(() => {
    var pop = document.getElementById('bmap_universal_vessel_popup');
    return {
      hoveredPipe: window.hoveredPipe,
      inspectorDisplay: pop ? pop.style.display : 'none',
      inspectorName: document.getElementById('uni_vessel_name') ? document.getElementById('uni_vessel_name').textContent : null,
      inspectorDest: document.getElementById('uni_vessel_dest') ? document.getElementById('uni_vessel_dest').textContent : null
    };
  })()`);
  console.log('Hover result on Petroline after unified renderer:', JSON.stringify(hoverTest, null, 2));

  ws.close();
  chrome.kill();
}

run().catch(e => {
  console.error(e);
  chrome.kill();
});

