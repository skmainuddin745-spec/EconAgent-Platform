const { spawn } = require('child_process');

const chrome = spawn('C:/Program Files/Google/Chrome/Application/chrome.exe', [
  '--headless=new', '--remote-debugging-port=9293', '--disable-gpu', '--no-sandbox', '--window-size=1600,1050', 'about:blank'
]);

setTimeout(async () => {
  try {
    let ws = null;
    for (let i = 0; i < 15; i++) {
      try {
        const res = await fetch('http://127.0.0.1:9293/json');
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

    await send('Page.navigate', { url: 'file:///F:/documents/SOIC/EconAgent_Platform/platform_ui/EconAgent_Dashboard.html' });
    await new Promise(r => setTimeout(r, 3000));

    const evalRes = await send('Runtime.evaluate', {
      expression: `(() => {
        const titansTab = Array.from(document.querySelectorAll('.tab')).find(t => (t.getAttribute('onclick')||'').includes('titans'));
        if (titansTab) titansTab.click();

        const el700 = document.elementFromPoint(800, 700);
        const el700Info = el700 ? {
          tagName: el700.tagName,
          id: el700.id,
          className: el700.className,
          outerHTML: el700.outerHTML.slice(0, 300),
          parentElement: el700.parentElement ? {
            tagName: el700.parentElement.tagName,
            id: el700.parentElement.id,
            className: el700.parentElement.className
          } : null,
          style: {
            background: window.getComputedStyle(el700).backgroundColor,
            height: window.getComputedStyle(el700).height,
            width: window.getComputedStyle(el700).width,
            position: window.getComputedStyle(el700).position
          }
        } : null;

        // Where is #titans?
        const titansDiv = document.getElementById('titans');
        const rect = titansDiv ? titansDiv.getBoundingClientRect() : null;

        return { el700Info, rect: rect ? { top: rect.top, left: rect.left, width: rect.width, height: rect.height } : null };
      })()`,
      returnByValue: true
    });

    console.log('Result:', JSON.stringify(evalRes.result.value, null, 2));

    chrome.kill();
    process.exit(0);
  } catch (err) {
    console.error(err);
    chrome.kill();
    process.exit(1);
  }
}, 1500);

