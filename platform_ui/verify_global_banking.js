const { spawn } = require('child_process');
const fs = require('fs');

const chromePath = 'C:/Program Files/Google/Chrome/Application/chrome.exe';
const targetUrl = 'file:///F:/documents/SOIC/EconAgent_Platform/platform_ui/EconAgent_Dashboard.html';
const port = 9322;

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

  console.log('=== TEST 1: Page Load & BMAP Tab Activation ===');
  console.log('Console Errors count:', pageErrors.length);

  await evaluate(ws, `window.showTab(null, 'bmap');`);
  await sleep(800);

  console.log('\n=== TEST 2: Global Banking Network Dataset Audit ===');
  const datasetCheck = await evaluate(ws, `(() => {
    const titans = window.globalBankingTitans ? window.globalBankingTitans.length : 0;
    const usBranches = window.branchesCompact ? window.branchesCompact.length : 0;
    const sampleIndia = (window.globalBankingTitans || []).find(g => g.country === 'India');
    const sampleGcc = (window.globalBankingTitans || []).find(g => g.country === 'Saudi Arabia');
    const sampleEurope = (window.globalBankingTitans || []).find(g => g.country === 'Switzerland');
    return {
      titansCount: titans,
      usBranchesCount: usBranches,
      sampleIndia: sampleIndia ? { name: sampleIndia.name, regulator: sampleIndia.regulator, assets: sampleIndia.assetsM } : null,
      sampleGcc: sampleGcc ? { name: sampleGcc.name, regulator: sampleGcc.regulator, assets: sampleGcc.assetsM } : null,
      sampleEurope: sampleEurope ? { name: sampleEurope.name, regulator: sampleEurope.regulator, assets: sampleEurope.assetsM } : null
    };
  })()`);
  console.log('Dataset check:', JSON.stringify(datasetCheck, null, 2));

  console.log('\n=== TEST 3: Regional Jurisdiction Filter Tests ===');
  const regionsToTest = ['ALL', 'GLOBAL', 'INDIA', 'GCC', 'EUROPE', 'ASIA', 'US'];
  for (const reg of regionsToTest) {
    const regResult = await evaluate(ws, `(() => {
      const regSelect = document.getElementById('filter_bank_region');
      if (regSelect) {
        regSelect.value = '${reg}';
        window.filterBankBranches();
      }
      const lbl = document.getElementById('lbl_bank_dep_val');
      return {
        region: '${reg}',
        label: lbl ? lbl.textContent : null
      };
    })()`);
    console.log(`Region [${reg}]:`, regResult);
  }

  console.log('\n=== TEST 4: Click Global Bank & Inspect Dossier ===');
  const inspectResult = await evaluate(ws, `(() => {
    // Select India & Click State Bank of India
    const sbi = (window.globalBankingTitans || []).find(g => g.id === 'bank_sbi_hq');
    if (sbi && typeof window.showUniversalInspector === 'function') {
      window.showUniversalInspector('bank_branch', sbi, [sbi.lat, sbi.lon]);
    }
    const pop = document.getElementById('bmap_universal_vessel_popup');
    return {
      popupVisible: pop ? pop.style.display : 'none',
      name: document.getElementById('uni_vessel_name') ? document.getElementById('uni_vessel_name').textContent : null,
      type: document.getElementById('uni_vessel_type') ? document.getElementById('uni_vessel_type').textContent : null,
      stat: document.getElementById('uni_vessel_status') ? document.getElementById('uni_vessel_status').textContent : null,
      owner: document.getElementById('uni_vessel_owner') ? document.getElementById('uni_vessel_owner').textContent : null,
      dest: document.getElementById('uni_vessel_dest') ? document.getElementById('uni_vessel_dest').textContent : null,
      berth: document.getElementById('uni_vessel_berth') ? document.getElementById('uni_vessel_berth').textContent : null
    };
  })()`);
  console.log('SBI Universal Inspector Dossier:', JSON.stringify(inspectResult, null, 2));

  // Take screenshot of Global Banking Hubs
  const shotData = await sendCdp(ws, 'Page.captureScreenshot', { format: 'png' });
  fs.writeFileSync('C:/Users/SK/.gemini/antigravity/brain/49bcdc7d-9012-4831-93a6-42d8b11a6533/shot_global_banking_verified.png', Buffer.from(shotData.data, 'base64'));
  console.log('\nScreenshot saved to shot_global_banking_verified.png');

  console.log('\nTotal Runtime Errors:', pageErrors.length);
  if (pageErrors.length) console.log(pageErrors);

  ws.close();
  chrome.kill();
  console.log('\nGLOBAL BANKING NETWORK AUDIT COMPLETE!');
}

run().catch(e => {
  console.error('Audit failed:', e);
  chrome.kill();
});

