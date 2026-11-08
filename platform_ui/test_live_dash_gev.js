const puppeteer = require('puppeteer');
const path = require('path');

(async () => {
  const browser = await puppeteer.launch({
    headless: 'new',
    args: ['--no-sandbox', '--disable-setuid-sandbox', '--allow-file-access-from-files', '--use-gl=angle']
  });
  const page = await browser.newPage();
  await page.setViewport({ width: 1440, height: 900 });

  page.on('console', msg => console.log('PAGE LOG:', msg.text()));
  page.on('pageerror', err => console.log('PAGE ERROR:', err.message));

  const dashPath = 'file:///' + path.resolve(__dirname, 'EconAgent_Dashboard.html').replace(/\\/g, '/');
  console.log('Navigating to:', dashPath);
  await page.goto(dashPath, { waitUntil: 'domcontentloaded', timeout: 30000 });

  await new Promise(r => setTimeout(r, 2000));

  // Switch to BMAP tab
  await page.evaluate(() => {
    const tabs = Array.from(document.querySelectorAll('button, div, span'));
    const bmapTab = tabs.find(el => el.textContent && el.textContent.includes('BMAP Tankers'));
    if (bmapTab) bmapTab.click();
    else if (window.switchAppTab) window.switchAppTab('bmap');
  });

  await new Promise(r => setTimeout(r, 1500));

  // Check 3D view
  await page.evaluate(() => {
    if (window.switchBmapView) window.switchBmapView('gev');
  });

  await new Promise(r => setTimeout(r, 3000));

  const screenshotPath = 'C:/Users/SK/.gemini/antigravity/brain/49bcdc7d-9012-4831-93a6-42d8b11a6533/shot_live_gev_current_state.png';
  await page.screenshot({ path: screenshotPath });
  console.log('Screenshot saved to:', screenshotPath);

  await browser.close();
})();

