const { spawn } = require('child_process');

const chrome = spawn('C:/Program Files/Google/Chrome/Application/chrome.exe', [
  '--headless=new', '--remote-debugging-port=9273', '--disable-gpu', '--no-sandbox', '--window-size=1600,1050', 'about:blank'
]);

setTimeout(async () => {
  try {
    let res = null;
    for (let i = 0; i < 10; i++) {
      try {
        res = await fetch('http://127.0.0.1:9273/json');
        if (res.ok) break;
      } catch (e) {
        await new Promise(r => setTimeout(r, 400));
      }
    }
    const [target] = await res.json();
    const ws = new WebSocket(target.webSocketDebuggerUrl);
    await new Promise(r => ws.addEventListener('open', r));
    let id = 1;
    const send = (m, p) => new Promise((resolve) => {
      const cur = id++;
      const h = e => { const d = JSON.parse(e.data); if (d.id === cur) { ws.removeEventListener('message', h); resolve(d.result); } };
      ws.addEventListener('message', h);
      ws.send(JSON.stringify({ id: cur, method: m, params: p }));
    });
    await send('Page.navigate', { url: 'file:///F:/documents/SOIC/EconAgent_Platform/platform_ui/Bloomberg_BMAP_Terminal.html' });
    await new Promise(r => setTimeout(r, 3000));
    
    const diag = await send('Runtime.evaluate', {
      expression: `(() => {
        const crudeGrp = window.datasetLayerGroups['crude_pipelines'];
        const isOnMap = window.leafletMap.hasLayer(crudeGrp);
        const layers = crudeGrp ? crudeGrp.getLayers().length : 0;
        const renderer = window.masterCanvasRenderer;
        const rendererMap = renderer ? !!renderer._map : false;
        const rendererLayers = renderer ? Object.keys(renderer._layers || {}).length : 0;
        
        const pt = window.leafletMap.latLngToContainerPoint([25.4, 46.5]);
        const rect = window.leafletMap.getContainer().getBoundingClientRect();
        const absX = rect.left + pt.x;
        const absY = rect.top + pt.y;
        const topEl = document.elementFromPoint(absX, absY);
        const isMasterCanvas = (topEl === renderer._container);

        // All canvases in the map
        const allCanvases = Array.from(document.querySelectorAll('canvas')).map(c => ({
          id: c.id,
          cls: c.className,
          isMaster: c === renderer._container,
          rect: c.getBoundingClientRect()
        }));

        const nonMasterCanvas = allCanvases.find(c => c.cls === 'leaflet-zoom-animated' && !c.isMaster);
        
        // Find which renderer owns the non-master canvas
        const map = window.leafletMap;
        let ownerRenderer = null;
        for (let id in map._layers) {
          const l = map._layers[id];
          if (l._container && l._container !== renderer._container && l._container.tagName === 'CANVAS') {
            ownerRenderer = { id, type: l.constructor.name, options: l.options };
          }
        }

        const rogueRenderer = map._layers["1809"];
        const rogueLayers = rogueRenderer && rogueRenderer._layers ? Object.keys(rogueRenderer._layers).map(k => {
          const l = rogueRenderer._layers[k];
          return { id: k, type: l.constructor.name, options: l.options, latlngs: l._latlngs || l._latlng };
        }) : [];

        return {
          isOnMap,
          layers,
          rendererMap,
          rendererLayers,
          pt, absX, absY,
          topElTag: topEl ? topEl.tagName : null,
          isMasterCanvas,
          rogueLayerCount: rogueLayers.length,
          rogueLayersSample: rogueLayers.slice(0, 5)
        };
      })()`,
      returnByValue: true
    });
    console.log('Crude Group Diag:', JSON.stringify(diag.result.value, null, 2));

    ws.close();
    chrome.kill();
    process.exit(0);
  } catch (err) {
    console.error(err);
    chrome.kill();
    process.exit(1);
  }
}, 1200);
