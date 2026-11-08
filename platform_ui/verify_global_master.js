const { spawn } = require('child_process');
const fs = require('fs');

const chromePath = 'C:/Program Files/Google/Chrome/Application/chrome.exe';
const targetUrl = 'file:///F:/documents/SOIC/EconAgent_Platform/platform_ui/EconAgent_Dashboard.html';
const port = 9333;

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
  try {
    await sleep(1500);
    const res = await fetch(`http://127.0.0.1:${port}/json`);
    const pages = await res.json();
    const ws = new WebSocket(pages[0].webSocketDebuggerUrl);
    await new Promise(r => ws.addEventListener('open', r));

    const pageErrors = [];
    ws.addEventListener('message', (event) => {
      const data = JSON.parse(event.data);
      if (data.method === 'Runtime.exceptionThrown') {
        pageErrors.push(data.params.exceptionDetails);
      }
    });

    await sendCdp(ws, 'Page.enable');
    await sendCdp(ws, 'Runtime.enable');

    console.log('[1/7] Navigating to Dashboard...');
    await sendCdp(ws, 'Page.navigate', { url: targetUrl });
    await sleep(2500);

    console.log('[2/7] Switching to BMAP Tankers & Flows tab...');
    await evaluate(ws, `
      (function() {
        var tabs = Array.from(document.querySelectorAll('button, div, span'));
        var bTab = tabs.find(el => el.textContent && el.textContent.includes('BMAP Tankers'));
        if (bTab) bTab.click();
        else if (window.switchAppTab) window.switchAppTab('bmap');
      })()
    `);
    await sleep(1500);

    console.log('[3/7] Auditing Global Pipelines & Banking Datasets in Memory...');
    const auditData = await evaluate(ws, `
      ({
        globalBankingCount: (window.globalBankingTitans || []).length,
        usBranchesCount: (window.branchesCompact || []).length,
        crudePipelinesCount: (window.crudePipelines || []).length,
        gasPipelinesCount: (window.gasPipelines || []).length,
        sampleGas: (window.gasPipelines || []).map(p => ({ name: p.name, scope: p.scope })),
        sampleCrude: (window.crudePipelines || []).map(p => ({ name: p.name, scope: p.scope }))
      })
    `);
    console.log('Dataset Audit:', JSON.stringify(auditData, null, 2));

    console.log('[4/7] Auditing Map Content Drawer (Natural Gas & Bank Branches Cards)...');
    const drawerAudit = await evaluate(ws, `
      (function() {
        if (typeof window.toggleMapContentDrawer === 'function') {
          var drawer = document.getElementById('bmap_map_content_drawer');
          if (drawer && (drawer.style.display === 'none' || drawer.style.transform === 'translateX(100%)')) {
            window.toggleMapContentDrawer();
          }
        }
        var ngCardText = document.getElementById('bmap_dataset_cards_container') ? document.getElementById('bmap_dataset_cards_container').innerText : '';
        
        // Test slider at 4700M
        var slider = document.getElementById('slider_bank_dep');
        if (slider) {
          slider.value = 4700;
          if (typeof window.filterBankBranches === 'function') window.filterBankBranches();
        }
        var lblBank = document.getElementById('lbl_bank_dep_val') ? document.getElementById('lbl_bank_dep_val').innerText : '';

        return {
          ngCardTextFound: ngCardText.includes('Natural Gas & Global Energy Pipelines'),
          hasNoPipelinesNAm: !ngCardText.includes('Pipelines (N.Am.)'),
          lblBankAt4700: lblBank
        };
      })()
    `);
    console.log('Drawer Audit:', JSON.stringify(drawerAudit, null, 2));

    console.log('[5/7] Switching to GEV 3D Workstation and Auditing Dual Mode...');
    const gevAudit = await evaluate(ws, `
      (function() {
        if (typeof window.switchBmapView === 'function') window.switchBmapView('gev');
        var gevCont = document.getElementById('bmap_view_container_gev');
        var isVisible = gevCont && gevCont.style.display !== 'none';
        var nativeCont = document.getElementById('gev_native_cesium_container');
        var iframeCont = document.getElementById('gev_iframe');
        var pill = document.getElementById('gev_server_status_pill');
        return {
          gevVisible: isVisible,
          nativeDisplay: nativeCont ? nativeCont.style.display : null,
          iframeDisplay: iframeCont ? iframeCont.style.display : null,
          pillText: pill ? pill.innerText : null
        };
      })()
    `);
    console.log('GEV 3D Initial Audit:', JSON.stringify(gevAudit, null, 2));

    await sleep(1500);

    console.log('[6/7] Testing Server Mode (Port 4173 connection to running microservice)...');
    const serverModeAudit = await evaluate(ws, `
      (async function() {
        if (typeof window.set3DMode === 'function') window.set3DMode('server');
        await new Promise(r => setTimeout(r, 1200));
        var iframeCont = document.getElementById('gev_iframe');
        var fallbackBox = document.getElementById('gev_fallback_box');
        var pill = document.getElementById('gev_server_status_pill');
        return {
          iframeDisplay: iframeCont ? iframeCont.style.display : null,
          iframeSrc: iframeCont ? iframeCont.src : null,
          fallbackDisplay: fallbackBox ? fallbackBox.style.display : null,
          pillText: pill ? pill.innerText : null
        };
      })()
    `);
    console.log('Server Mode Audit:', JSON.stringify(serverModeAudit, null, 2));

    // Capture screenshot
    const shot = await sendCdp(ws, 'Page.captureScreenshot', { format: 'png' });
    const shotPath = 'C:/Users/SK/.gemini/antigravity/brain/49bcdc7d-9012-4831-93a6-42d8b11a6533/shot_verify_global_gev_dual.png';
    fs.writeFileSync(shotPath, Buffer.from(shot.data, 'base64'));
    console.log('Screenshot saved to:', shotPath);

    console.log('[7/7] Page exceptions encountered:', pageErrors.length);
    if (pageErrors.length > 0) {
      console.log('Exceptions:', JSON.stringify(pageErrors, null, 2));
    }

    ws.close();
    chrome.kill();
    process.exit(0);

  } catch(err) {
    console.error('Test execution failed:', err);
    chrome.kill();
    process.exit(1);
  }
}

run();

