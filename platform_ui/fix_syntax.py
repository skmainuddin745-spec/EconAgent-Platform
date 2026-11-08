with open('platform_ui/bmap_js_template.js', 'r', encoding='utf-8') as f:
    text = f.read()

bad_block = """    if (viewId === 'gev') {
      window.checkGodsEyeServerStatus();
      if (!gevHeartbeatTimer) {
        gevHeartbeatTimer = setInterval(function() {
          if (currentActiveView === 'gev') {
            window.checkGodsEyeServerStatus(false);
          }
        }, 3000);
      }
    } else {
      if (gevHeartbeatTimer) {
        clearInterval(gevHeartbeatTimer);
        gevHeartbeatTimer = null;
      }
    } else if (viewId === 'map' && leafletMap) {"""

good_block = """    if (viewId !== 'gev' && gevHeartbeatTimer) {
      clearInterval(gevHeartbeatTimer);
      gevHeartbeatTimer = null;
    }

    if (viewId === 'gev') {
      window.checkGodsEyeServerStatus();
      if (!gevHeartbeatTimer) {
        gevHeartbeatTimer = setInterval(function() {
          if (currentActiveView === 'gev') {
            window.checkGodsEyeServerStatus(false);
          }
        }, 3000);
      }
    } else if (viewId === 'map' && leafletMap) {"""

if bad_block in text:
    text = text.replace(bad_block, good_block, 1)
    print("Fixed syntax error in bmap_js_template.js")
    with open('platform_ui/bmap_js_template.js', 'w', encoding='utf-8') as f:
        f.write(text)
else:
    print("Warning: bad_block not found")

