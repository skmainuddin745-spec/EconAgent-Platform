with open('platform_ui/bmap_js_template.js', 'r', encoding='utf-8') as f:
    js = f.read()

target = '''    } else {
      // Server mode (Port 4173)
      if (btnServer) { btnServer.style.background = '#0284c7'; btnServer.style.color = '#fff'; btnServer.style.borderColor = '#38bdf8'; }
      if (btnNative) { btnNative.style.background = '#0f172a'; btnNative.style.color = '#94a3b8'; btnNative.style.borderColor = '#1e293b'; }
      if (hudEngine) hudEngine.textContent = 'Bilawal Sidhu 3D Workstation (Port 4173)';
      window.checkGodsEyeServerStatus(true);
    }'''

replacement = '''    } else {
      // Server mode (Port 4173)
      if (btnServer) { btnServer.style.background = '#0284c7'; btnServer.style.color = '#fff'; btnServer.style.borderColor = '#38bdf8'; }
      if (btnNative) { btnNative.style.background = '#0f172a'; btnNative.style.color = '#94a3b8'; btnNative.style.borderColor = '#1e293b'; }
      if (hudEngine) hudEngine.textContent = 'Bilawal Sidhu 3D Workstation (Port 4173)';
      if (nativeEl) nativeEl.style.display = 'none';
      if (iframeEl) {
        iframeEl.style.display = 'block';
        if (!iframeEl.src || iframeEl.src.indexOf('4173') === -1) {
          iframeEl.src = 'http://127.0.0.1:4173/?embed=1';
        }
      }
      window.checkGodsEyeServerStatus(true);
    }'''

js = js.replace(target, replacement)

with open('platform_ui/bmap_js_template.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("Updated set3DMode in bmap_js_template.js!")

