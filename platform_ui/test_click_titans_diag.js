const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch({
    headless: 'new',
    args: ['--no-sandbox', '--disable-web-security', '--allow-file-access-from-files']
  });
  const page = await browser.newPage();
  await page.setViewport({ width: 1600, height: 900 });

  const errors = [];
  page.on('console', msg => {
    if (msg.type() === 'error') {
      errors.push('CONSOLE ERROR: ' + msg.text());
    }
  });
  page.on('pageerror', err => {
    errors.push('PAGE ERROR: ' + err.toString());
  });

  const url = 'file:///F:/documents/SOIC/EconAgent_Platform/platform_ui/EconAgent_Dashboard.html';
  console.log('Loading:', url);
  await page.goto(url, { waitUntil: 'load', timeout: 30000 });
  await new Promise(r => setTimeout(r, 2000));

  console.log('Initial page loaded. Errors:', errors);

  // Find the titans tab
  console.log('Clicking titans tab...');
  const clicked = await page.evaluate(() => {
    const tabs = Array.from(document.querySelectorAll('.tab'));
    const tTab = tabs.find(t => (t.getAttribute('onclick') || '').includes('titans'));
    if (tTab) {
      tTab.click();
      return true;
    }
    return false;
  });
  console.log('Titans tab clicked:', clicked);
  await new Promise(r => setTimeout(r, 1000));

  console.log('Errors after clicking titans:', errors);

  // Check visibility and dimensions of #titans
  const titansInfo = await page.evaluate(() => {
    const el = document.getElementById('titans');
    if (!el) return { found: false };
    const rect = el.getBoundingClientRect();
    const computed = window.getComputedStyle(el);
    return {
      found: true,
      display: computed.display,
      visibility: computed.visibility,
      opacity: computed.opacity,
      width: rect.width,
      height: rect.height,
      top: rect.top,
      left: rect.left,
      classList: Array.from(el.classList),
      childCount: el.children.length,
      innerHTMLSnippet: el.innerHTML.slice(0, 300)
    };
  });
  console.log('Titans info:', titansInfo);

  await page.screenshot({ path: 'C:/Users/SK/.gemini/antigravity/brain/49bcdc7d-9012-4831-93a6-42d8b11a6533/shot_titans_diag.png' });
  console.log('Screenshot saved.');

  await browser.close();
})();

