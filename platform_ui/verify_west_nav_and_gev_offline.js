const { spawn } = require('child_process');
const fs = require('fs');

const chrome = spawn('C:/Program Files/Google/Chrome/Application/chrome.exe', [
  '--headless=new', '--remote-debugging-port=9298', '--disable-gpu', '--no-sandbox', '--window-size=1600,1050', 'about:blank'
]);

setTimeout(async () => {
  try {
    let ws = null;
    for (let i = 0; i < 15; i++) {
      try {
        const res = await fetch('http://127.0.0.1:9298/json');
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

    if (!ws) {
      console.error('Cannot connect to Chrome');
      chrome.kill();
      process.exit(1);
    }

    const consoleLogs = [];
    const exceptions = [];

    ws.addEventListener('message', e => {
      const data = JSON.parse(e.data);
      if (data.method === 'Runtime.consoleAPICalled') {
        consoleLogs.push(data.params);
      }
      if (data.method === 'Runtime.exceptionThrown') {
        exceptions.push(data.params);
      }
    });

    let id = 1;
    const send = (m, p) => new Promise((resolve) => {
      const cur = id++;
      const h = e => { const d = JSON.parse(e.data); if (d.id === cur) { ws.removeEventListener('message', h); resolve(d.result); } };
      ws.addEventListener('message', h);
      ws.send(JSON.stringify({ id: cur, method: m, params: p }));
    });

    await send('Runtime.enable');
    await send('Page.enable');

    console.log('Navigating to EconAgent_Dashboard.html...');
    await send('Page.navigate', { url: 'file:///F:/documents/SOIC/EconAgent_Platform/platform_ui/EconAgent_Dashboard.html' });
    await new Promise(r => setTimeout(r, 4000));

    // Test 1: Navigation West (North America)
    console.log('Testing Navigation West...');
    const westRes = await send('Runtime.evaluate', {
      expression: `(() => {
        // Ensure on bmap tab
        showTab(null, 'bmap');
        const btnWest = document.getElementById('btn_bmap_nav_west');
        if (btnWest) btnWest.click();

        return {
          btnWestFound: !!btnWest,
          center: leafletMap ? leafletMap.getCenter() : null,
          zoom: leafletMap ? leafletMap.getZoom() : null,
          bankBranchesActive: activeLayers.bank_branches,
          naturalGasActive: activeLayers.natural_gas,
          scopeLabel: document.getElementById('bmap_scope_label')?.textContent
        };
      })()`,
      returnByValue: true
    });
    console.log('West Nav Result (Immediate):', JSON.stringify(westRes.result.value, null, 2));

    // Wait for flyTo transition
    await new Promise(r => setTimeout(r, 1500));

    const westResAfter = await send('Runtime.evaluate', {
      expression: `(() => {
        return {
          center: leafletMap ? leafletMap.getCenter() : null,
          zoom: leafletMap ? leafletMap.getZoom() : null,
          renderedBranchCount: datasetLayerGroups['bank_branches'] ? datasetLayerGroups['bank_branches'].getLayers().length : 0,
          renderedGasPipelineCount: datasetLayerGroups['natural_gas'] ? datasetLayerGroups['natural_gas'].getLayers().length : 0
        };
      })()`,
      returnByValue: true
    });
    console.log('West Nav Result (After 1.5s):', JSON.stringify(westResAfter.result.value, null, 2));

    // Capture screenshot of North America
    const shotWest = await send('Page.captureScreenshot', { format: 'png' });
    fs.writeFileSync('C:/Users/SK/.gemini/antigravity/brain/49bcdc7d-9012-4831-93a6-42d8b11a6533/shot_verified_nav_west_north_america.png', Buffer.from(shotWest.data, 'base64'));
    console.log('Saved shot_verified_nav_west_north_america.png');

    // Test 2: Navigation East (Hormuz)
    console.log('Testing Navigation East...');
    await send('Runtime.evaluate', {
      expression: `(() => {
        const btnEast = document.getElementById('btn_bmap_nav_east');
        if (btnEast) btnEast.click();
      })()`
    });
    await new Promise(r => setTimeout(r, 1500));

    const eastRes = await send('Runtime.evaluate', {
      expression: `(() => {
        return {
          center: leafletMap ? leafletMap.getCenter() : null,
          zoom: leafletMap ? leafletMap.getZoom() : null,
          scopeLabel: document.getElementById('bmap_scope_label')?.textContent
        };
      })()`,
      returnByValue: true
    });
    console.log('East Nav Result:', JSON.stringify(eastRes.result.value, null, 2));

    // Test 3: God's Eye View 3D Offline Fallback
    console.log("Testing God's Eye View 3D Offline Fallback...");
    const gevRes = await send('Runtime.evaluate', {
      expression: `(() => {
        switchBmapView('gev');
        const iframe = document.getElementById('gev_iframe');
        const fallback = document.getElementById('gev_fallback_box');
        const statusPill = document.getElementById('gev_server_status_pill');

        return {
          iframeDisplay: iframe ? window.getComputedStyle(iframe).display : null,
          iframeSrc: iframe ? iframe.src : null,
          fallbackDisplay: fallback ? window.getComputedStyle(fallback).display : null,
          fallbackText: fallback ? fallback.innerText.slice(0, 120) : null,
          statusText: statusPill ? statusPill.innerText : null
        };
      })()`,
      returnByValue: true
    });
    console.log('GEV Offline Fallback Result:', JSON.stringify(gevRes.result.value, null, 2));

    await new Promise(r => setTimeout(r, 800));

    const shotGevFallback = await send('Page.captureScreenshot', { format: 'png' });
    fs.writeFileSync('C:/Users/SK/.gemini/antigravity/brain/49bcdc7d-9012-4831-93a6-42d8b11a6533/shot_verified_gev_offline_fallback.png', Buffer.from(shotGevFallback.data, 'base64'));
    console.log('Saved shot_verified_gev_offline_fallback.png');

    // Test 4: Financial Titans Tab
    console.log('Testing Financial Titans Tab...');
    const titanRes = await send('Runtime.evaluate', {
      expression: `(() => {
        showTab(null, 'titans');
        const titansDiv = document.getElementById('titans');
        return {
          activeClass: titansDiv ? titansDiv.className : null,
          display: titansDiv ? window.getComputedStyle(titansDiv).display : null,
          offsetHeight: titansDiv ? titansDiv.offsetHeight : 0,
          subpaneBlkDisplay: window.getComputedStyle(document.getElementById('titan_subpane_blk')).display,
          headerText: titansDiv ? titansDiv.querySelector('h2')?.innerText : null
        };
      })()`,
      returnByValue: true
    });
    console.log('Titans Tab Result:', JSON.stringify(titanRes.result.value, null, 2));

    const shotTitans = await send('Page.captureScreenshot', { format: 'png' });
    fs.writeFileSync('C:/Users/SK/.gemini/antigravity/brain/49bcdc7d-9012-4831-93a6-42d8b11a6533/shot_verified_titans_tab_rendered.png', Buffer.from(shotTitans.data, 'base64'));
    console.log('Saved shot_verified_titans_tab_rendered.png');

    console.log(`Total exceptions: ${exceptions.length}`);
    exceptions.forEach(ex => console.log('EX:', ex.exceptionDetails.text, ex.exceptionDetails.exception?.description));

    chrome.kill();
    process.exit(0);
  } catch (err) {
    console.error('Error:', err);
    chrome.kill();
    process.exit(1);
  }
}, 1500);

