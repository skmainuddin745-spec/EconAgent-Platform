with open('platform_ui/bmap_js_template.js', 'r', encoding='utf-8') as f:
    text = f.read()

old_second_def = """  window.checkGodsEyeServerStatus = function() {
    var iframe = document.getElementById('gev_iframe');
    var statusPill = document.getElementById('gev_server_status_pill');
    var fallbackBox = document.getElementById('gev_fallback_box');
    
    // Check if Vite port 4173 is responding
    fetch('http://localhost:4173', { mode: 'no-cors' })
      .then(function() {
        if (statusPill) {
          statusPill.innerHTML = '<span style="color:#00e676;">●</span> VITE 3D SERVER ONLINE (Port 4173)';
          statusPill.style.background = 'rgba(16,185,129,0.15)';
          statusPill.style.borderColor = '#10b981';
          statusPill.style.color = '#34d399';
        }
        if (iframe) iframe.style.display = 'block';
        if (fallbackBox) fallbackBox.style.display = 'none';
      })
      .catch(function(err) {
        if (statusPill) {
          statusPill.innerHTML = '<span style="color:#ef4444;">●</span> VITE SERVER OFFLINE — Run Launch_Gods_Eye_View.bat';
          statusPill.style.background = 'rgba(239,68,68,0.15)';
          statusPill.style.borderColor = '#ef4444';
          statusPill.style.color = '#f87171';
        }
        if (fallbackBox) fallbackBox.style.display = 'block';
      });
  };"""

new_unified_def = """  window.checkGodsEyeServerStatus = function(forceReload) {
    var iframe = document.getElementById('gev_iframe');
    var statusPill = document.getElementById('gev_server_status_pill');
    var fallbackBox = document.getElementById('gev_fallback_box');

    return fetch('http://127.0.0.1:4173/?embed=1', { mode: 'no-cors', cache: 'no-store' })
      .then(function() {
        if (statusPill) {
          statusPill.innerHTML = '<span style="color:#00e676;">●</span> VITE 3D SERVER ONLINE (Port 4173)';
          statusPill.style.background = 'rgba(16,185,129,0.15)';
          statusPill.style.borderColor = '#10b981';
          statusPill.style.color = '#34d399';
        }
        if (fallbackBox) fallbackBox.style.display = 'none';
        if (iframe) {
          iframe.style.display = 'block';
          if (!iframe.src || iframe.src.indexOf('4173') === -1 || forceReload) {
            iframe.src = 'http://127.0.0.1:4173/?embed=1';
          }
        }
        return true;
      })
      .catch(function(err) {
        if (statusPill) {
          statusPill.innerHTML = '<span style="color:#ef4444;">●</span> VITE SERVER OFFLINE — Run Launch_Gods_Eye_View.bat';
          statusPill.style.background = 'rgba(239,68,68,0.15)';
          statusPill.style.borderColor = '#ef4444';
          statusPill.style.color = '#f87171';
        }
        if (iframe) {
          iframe.style.display = 'none';
          iframe.src = 'about:blank';
        }
        if (fallbackBox) fallbackBox.style.display = 'block';
        return false;
      });
  };"""

if old_second_def in text:
    text = text.replace(old_second_def, new_unified_def, 1)
    print("Replaced second definition successfully in bmap_js_template.js")
    with open('platform_ui/bmap_js_template.js', 'w', encoding='utf-8') as f:
        f.write(text)
else:
    print("Warning: old_second_def not found")

