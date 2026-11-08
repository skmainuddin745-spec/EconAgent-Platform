# F:\documents\SOIC\EconAgent_Platform\platform_ui\build_standalone_bmap.py
import sys
from bmap_tanker_component import build_bmap_tanker_section

def build_standalone():
    section_html = build_bmap_tanker_section()
    
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>BMAP <GO> — Bloomberg Professional Terminal — Global Maritime Vessel & Energy Flow Radar</title>
<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js"></script>
<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
<style>
  :root {{
    --bg: #05080f; --bg2: #090e17; --bg3: #0e1524; --bg4: #162035;
    --bb-amber: #ffaa00; --bb-green: #00e676; --bb-cyan: #00e5ff; --bb-red: #ff3344;
    --text: #e2e8f0; --text2: #94a3b8; --border: #1e293b;
    --font-mono: 'SFMono-Regular', Consolas, 'Liberation Mono', Menlo, Courier, monospace;
  }}
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{
    background: var(--bg);
    color: var(--text);
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
    font-size: 12px;
    line-height: 1.4;
    overflow-x: hidden;
  }}

  /* Bloomberg Header Ribbon */
  .bb-top-bar {{
    background: #03060c;
    border-bottom: 1px solid #162438;
    padding: 6px 20px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    gap: 12px;
    font-family: var(--font-mono);
    font-size: 11px;
  }}
  .bb-ticker-wrap {{ display: flex; align-items: center; gap: 12px; flex-wrap: wrap; }}
  .bb-amber {{ color: var(--bb-amber); font-weight: 700; }}
  .bb-cyan {{ color: var(--bb-cyan); font-weight: 700; }}
  .bb-green {{ color: var(--bb-green); font-weight: 700; }}
  .bb-red {{ color: var(--bb-red); font-weight: 700; }}

  /* Bloomberg Navigation Keys */
  .bb-hotkeys {{
    display: flex;
    gap: 6px;
    background: #090e17;
    border: 1px solid #1a2736;
    border-radius: 4px;
    padding: 3px 6px;
  }}
  .bb-key {{
    background: #111a28;
    color: var(--bb-amber);
    border: 1px solid #1e334d;
    padding: 2px 7px;
    border-radius: 3px;
    font-size: 10px;
    font-weight: 700;
    cursor: pointer;
    transition: all 0.15s ease;
  }}
  .bb-key:hover {{ background: #1a2b42; border-color: var(--bb-cyan); color: #fff; }}

  .container {{
    max-width: 1720px;
    margin: 0 auto;
    padding: 16px 20px;
  }}

  .badge {{
    display: inline-flex;
    align-items: center;
    padding: 2px 7px;
    border-radius: 3px;
    font-size: 10px;
    font-weight: 700;
    font-family: var(--font-mono);
  }}

  .action-btn {{
    background: #132032;
    color: #94a3b8;
    border: 1px solid #1e334d;
    border-radius: 3px;
    padding: 4px 10px;
    font-size: 10.5px;
    font-family: var(--font-mono);
    cursor: pointer;
    transition: all 0.15s ease;
  }}
  .action-btn:hover {{ background: #1e334d; color: #fff; border-color: #3b82f6; }}
  .action-btn.active {{ background: #1e3a5f; color: #00e5ff; border-color: #3b82f6; font-weight: 700; }}

  .data-table {{
    width: 100%;
    border-collapse: collapse;
    font-family: var(--font-mono);
  }}
  .data-table th {{
    background: #090f1a;
    color: #94a3b8;
    padding: 7px 10px;
    text-align: left;
    font-size: 10px;
    border-bottom: 1px solid #1c2e44;
  }}
  .data-table td {{
    padding: 7px 10px;
    border-bottom: 1px solid #0f1826;
    color: #cbd5e1;
  }}
  .data-table tr:hover td {{ background: #0c1422; }}
</style>
</head>
<body>

<!-- Bloomberg Terminal Header Bar -->
<div class="bb-top-bar">
  <div class="bb-ticker-wrap">
    <span class="bb-amber" style="font-size: 13px; font-weight: 900;">BLOOMBERG TERMINAL</span>
    <span style="color: #475569;">|</span>
    <span class="bb-cyan">BMAP &lt;GO&gt;</span>
    <span style="color: #64748b;">GLOBAL MARITIME TANKER RADAR</span>
    <span style="color: #475569;">|</span>
    <span>BRENT CRUDE: <strong class="bb-amber">$75.82</strong> <span class="bb-green">+0.42%</span></span>
    <span style="color: #475569;">|</span>
    <span>WTI: <strong class="bb-amber">$71.40</strong> <span class="bb-green">+0.38%</span></span>
    <span style="color: #475569;">|</span>
    <span>VLCC TD3C (MEG-CHINA): <strong class="bb-green">68.5 WS ($48,500/d)</strong></span>
  </div>

  <div class="bb-hotkeys">
    <div class="bb-key" onclick="window.location.href='EconAgent_Dashboard.html';">F1 ZOOM</div>
    <div class="bb-key" onclick="window.location.href='EconAgent_Dashboard.html';">F2 DCF</div>
    <div class="bb-key" onclick="window.location.href='EconAgent_Dashboard.html';">F5 SOIC</div>
    <div class="bb-key" style="background:#1e3a5f;color:#00e5ff;border-color:#3b82f6;">F9 BMAP</div>
    <div class="bb-key" onclick="window.location.href='EconAgent_Dashboard.html';">F10 MACRO</div>
    <div class="bb-key" onclick="window.location.href='EconAgent_Dashboard.html';">MASTER DASHBOARD ➔</div>
  </div>
</div>

<div class="container">
  {section_html}
</div>

</body>
</html>
"""
    output_path = r'F:\documents\SOIC\EconAgent_Platform\platform_ui\Bloomberg_BMAP_Terminal.html'
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Standalone BMAP generated: {output_path} ({len(html)} bytes)")

if __name__ == '__main__':
    build_standalone()

