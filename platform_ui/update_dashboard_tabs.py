import os

BASE_DIR = r"F:\documents\SOIC\EconAgent_Platform\platform_ui"
dash_gen_path = os.path.join(BASE_DIR, "generate_dashboard.py")
with open(dash_gen_path, "r", encoding="utf-8") as f:
    code = f.read()

old_show_tab = """  if (tabId === 'technicals') {{
    if (typeof window.drawTechnicalsChart === 'function') {{
      setTimeout(window.drawTechnicalsChart, 40);
    }}
  }}

  // Auto-scroll to top of viewport if user was scrolled down deep
  var tabsBar = document.querySelector('.tabs');
  if (tabsBar && (window.scrollY > tabsBar.offsetTop + 30)) {{
    window.scrollTo({{ top: tabsBar.offsetTop, behavior: 'smooth' }});
  }}"""

new_show_tab = """  if (tabId === 'technicals') {{
    if (typeof window.drawTechnicalsChart === 'function') {{
      setTimeout(window.drawTechnicalsChart, 40);
    }}
  }} else if (tabId === 'titans') {{
    if (typeof window.switchTitanTab === 'function') {{
      setTimeout(function() {{ window.switchTitanTab('blk'); }}, 40);
    }}
  }} else if (tabId === 'soic_sectors') {{
    if (typeof window.switchSectorPane === 'function') {{
      setTimeout(function() {{ window.switchSectorPane('damodaran'); }}, 40);
    }}
  }} else if (tabId === 'topnotch') {{
    if (typeof window.switchTopNotchTab === 'function') {{
      setTimeout(function() {{ window.switchTopNotchTab('citadel'); }}, 40);
    }}
  }}

  // Auto-align viewport so active tab content is smoothly and fully visible
  var tabsBar = document.querySelector('.tabs');
  if (tabsBar) {{
    var tabsRect = tabsBar.getBoundingClientRect();
    if (tabsRect.top < 0 || tabsRect.bottom > window.innerHeight || window.scrollY > tabsBar.offsetTop + 10) {{
      tabsBar.scrollIntoView({{ behavior: 'smooth', block: 'start' }});
    }}
  }}"""

if old_show_tab in code:
    code = code.replace(old_show_tab, new_show_tab, 1)
    print("Updated showTab in generate_dashboard.py")
    with open(dash_gen_path, "w", encoding="utf-8") as f:
        f.write(code)
    print("Saved generate_dashboard.py")
else:
    print("Warning: old_show_tab not found in generate_dashboard.py")

