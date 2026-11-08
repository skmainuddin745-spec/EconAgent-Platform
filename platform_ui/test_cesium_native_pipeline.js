const { spawn } = require('child_process');
const fs = require('fs');

const chrome = spawn('C:/Program Files/Google/Chrome/Application/chrome.exe', [
  '--headless=new', '--remote-debugging-port=9288', '--disable-gpu', '--no-sandbox', '--window-size=1600,1050', 'about:blank'
]);

setTimeout(async () => {
  try {
    let ws = null;
    for (let i = 0; i < 15; i++) {
      try {
        const res = await fetch('http://127.0.0.1:9288/json');
        if (res.ok) {
          const pages = await res.json();
          ws = new WebSocket(pages[0].webSocketDebuggerUrl);
          await new Promise(r => ws.addEventListener('open', r));
          break;
        }
      } catch (e) {
        await new Promise(r => setTimeout(r, 300));
      }
    }

    let id = 1;
    const send = (m, p) => new Promise((resolve) => {
      const cur = id++;
      const h = e => { const d = JSON.parse(e.data); if (d.id === cur) { ws.removeEventListener('message', h); resolve(d.result); } };
      ws.addEventListener('message', h);
      ws.send(JSON.stringify({ id: cur, method: m, params: p }));
    });

    await send('Runtime.enable');
    await send('Page.enable');

    await send('Page.navigate', { url: 'about:blank' });
    await new Promise(r => setTimeout(r, 1000));

    const testRes = await send('Runtime.evaluate', {
      expression: `(async () => {
        // 1. Inject Cesium CSS
        const link = document.createElement('link');
        link.rel = 'stylesheet';
        link.href = 'https://cesium.com/downloads/cesiumjs/releases/1.114/Build/Cesium/Widgets/widgets.css';
        document.head.appendChild(link);

        // 2. Inject Cesium JS
        await new Promise((resolve, reject) => {
          const s = document.createElement('script');
          s.src = 'https://cesium.com/downloads/cesiumjs/releases/1.114/Build/Cesium/Cesium.js';
          s.onload = resolve;
          s.onerror = reject;
          document.head.appendChild(s);
        });

        // 3. Create container
        const div = document.createElement('div');
        div.id = 'native_cesium_test';
        div.style.width = '1200px';
        div.style.height = '700px';
        document.body.appendChild(div);

        // 4. Initialize Viewer with dark / OpenStreetMap base
        const viewer = new Cesium.Viewer('native_cesium_test', {
          baseLayerPicker: false,
          geocoder: false,
          homeButton: false,
          infoBox: false,
          sceneModePicker: false,
          selectionIndicator: false,
          timeline: false,
          animation: false,
          navigationHelpButton: false,
          baseLayer: new Cesium.ImageryLayer(new Cesium.OpenStreetMapImageryProvider({
            url: 'https://tile.openstreetmap.org/'
          }))
        });

        // 5. Add 3D East-West Petroline pipeline
        viewer.entities.add({
          name: 'East-West Petroline',
          polyline: {
            positions: Cesium.Cartesian3.fromDegreesArray([
              50.15, 26.27, // Abqaiq
              46.72, 24.69, // Riyadh
              42.00, 24.20,
              38.06, 24.09  // Yanbu
            ]),
            width: 4,
            material: new Cesium.PolylineGlowMaterialProperty({
              glowPower: 0.3,
              color: Cesium.Color.CYAN
            })
          }
        });

        // 6. Add 3D AIS Tanker entity
        viewer.entities.add({
          name: 'JUBAIL TRADER',
          position: Cesium.Cartesian3.fromDegrees(56.2, 26.4),
          point: {
            pixelSize: 10,
            color: Cesium.Color.fromCssColorString('#00e676'),
            outlineColor: Cesium.Color.BLACK,
            outlineWidth: 2
          },
          label: {
            text: '🚢 JUBAIL TRADER (12.4 kn)',
            font: '11px monospace',
            fillColor: Cesium.Color.WHITE,
            outlineColor: Cesium.Color.BLACK,
            outlineWidth: 2,
            style: Cesium.LabelStyle.FILL_AND_OUTLINE,
            verticalOrigin: Cesium.VerticalOrigin.BOTTOM,
            pixelOffset: new Cesium.Cartesian2(0, -9)
          }
        });

        // 7. Fly to Hormuz
        viewer.camera.flyTo({
          destination: Cesium.Cartesian3.fromDegrees(50.0, 25.0, 1500000),
          duration: 0.5
        });

        return {
          entitiesCount: viewer.entities.values.length,
          canvasWidth: viewer.canvas.width,
          canvasHeight: viewer.canvas.height
        };
      })()`,
      awaitPromise: true,
      returnByValue: true
    });

    console.log('Result:', JSON.stringify(testRes.result.value, null, 2));

    await new Promise(r => setTimeout(r, 2000));

    const shot = await send('Page.captureScreenshot', { format: 'png' });
    fs.writeFileSync('C:/Users/SK/.gemini/antigravity/brain/49bcdc7d-9012-4831-93a6-42d8b11a6533/shot_native_cesium_3d_test.png', Buffer.from(shot.data, 'base64'));
    console.log('Saved shot_native_cesium_3d_test.png');

    chrome.kill();
    process.exit(0);
  } catch (err) {
    console.error(err);
    chrome.kill();
    process.exit(1);
  }
}, 1500);

