import os
import re
import subprocess

def build_v3():
    print("Building v3 platform with universal cascading ribbon, interactive SOIC sandbox, live DCF sliders, and DOM execution...")

    # Step 1: Read fractal_zoom_engine.py
    zoom_path = r'F:\documents\SOIC\EconAgent_Platform\platform_ui\fractal_zoom_engine.py'
    with open(zoom_path, 'r', encoding='utf-8') as f:
        zoom_code = f.read()

    # Step 2: Inject Interactive SOIC Sandbox, DCF Sliders, and Level 2 DOM Engine into fractal_zoom_engine.py
    # We will replace loadFirmModel and loadNanoAsset with the enhanced interactive versions
    
    # 2a. Interactive Technical Table Generator
    interactive_tech_table = """
        <!-- ⚡ DEEP 110-POINT TECHNICAL ANALYSIS MASTERCLASS RULEBOOK SANDBOX -->
        <div style="background:#080e18;border:1px solid #203a5e;border-radius:6px;padding:12px;margin-bottom:12px;">
          <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:8px;flex-wrap:wrap;gap:8px;">
            <div>
              <span style="color:#00e5ff;font-size:11px;font-weight:800;">⚡ 110-POINT TECHNICAL ANALYSIS MASTERCLASS RULEBOOK (INTERACTIVE SANDBOX)</span>
              <div style="color:#64748b;font-size:9.5px;">Click any condition pill to simulate parameter shifts and recalculate the SOIC 310-pt score in real time.</div>
            </div>
            <div style="display:flex;align-items:center;gap:8px;">
              <span class="badge" id="live_tech_score_badge" style="background:#ffaa00;color:#000;font-weight:800;font-size:11px;">TECH: <span id="dyn_tech_score">${sc.tech}</span> / 110 PTS</span>
              <button onclick="resetTechScores()" style="background:#132032;color:#94a3b8;border:1px solid #1e334d;padding:2px 8px;font-size:9.5px;border-radius:3px;cursor:pointer;">↺ Reset Baseline</button>
            </div>
          </div>

          <table class="data-table" style="font-size:10px;margin-bottom:0;" id="interactive_tech_table">
            <thead>
              <tr style="background:#0b1422;">
                <th>Parameter</th>
                <th>SOIC Rule &amp; Condition Options (Click to Test)</th>
                <th>Live Status</th>
                <th>Points Awarded</th>
              </tr>
            </thead>
            <tbody>
              <!-- 1. ADX 14 -->
              <tr>
                <td><strong style="color:#fff;">Weekly ADX 14</strong></td>
                <td>
                  <div style="display:flex;gap:4px;flex-wrap:wrap;">
                    <button class="tech-pill-btn ${tech.adx.pts === 20 ? 'active-pill' : ''}" id="pill_adx_20" onclick="adjustTechParam('adx', 20, 'Above 40 (Monster Bullish Trend)')">&gt;40 [20 pts]</button>
                    <button class="tech-pill-btn ${tech.adx.pts === 10 ? 'active-pill' : ''}" id="pill_adx_10" onclick="adjustTechParam('adx', 10, '20 to 40 (Healthy Developing Trend)')">20-40 [10 pts]</button>
                    <button class="tech-pill-btn ${tech.adx.pts === 0 ? 'active-pill' : ''}" id="pill_adx_0" onclick="adjustTechParam('adx', 0, 'Below 20 (No Trend / Choppy Rangebound)')">&lt;20 [0 pts]</button>
                  </div>
                </td>
                <td><span id="txt_adx_status" style="color:#00e5ff;">${tech.adx.val} · ${tech.adx.cond}</span></td>
                <td><strong style="color:#00e676;" id="txt_adx_pts">+${tech.adx.pts}</strong> / 20</td>
              </tr>

              <!-- 2. RSI 14 -->
              <tr>
                <td><strong style="color:#fff;">Weekly RSI 14</strong></td>
                <td>
                  <div style="display:flex;gap:4px;flex-wrap:wrap;">
                    <button class="tech-pill-btn ${tech.rsi.pts === 10 ? 'active-pill' : ''}" id="pill_rsi_10" onclick="adjustTechParam('rsi', 10, 'Between 50 to 75 (High Momentum Sweet Spot)')">50-75 [10 pts]</button>
                    <button class="tech-pill-btn ${tech.rsi.pts === 0 && tech.rsi.val > 75 ? 'active-pill' : ''}" id="pill_rsi_over" onclick="adjustTechParam('rsi', 0, 'Above 75 (Overbought Reversion Risk)')">&gt;75 [0 pts]</button>
                    <button class="tech-pill-btn ${tech.rsi.pts === 0 && tech.rsi.val <= 50 ? 'active-pill' : ''}" id="pill_rsi_under" onclick="adjustTechParam('rsi', 0, 'Below 50 (Weak Momentum / Bear Zone)')">&lt;50 [0 pts]</button>
                  </div>
                </td>
                <td><span id="txt_rsi_status" style="color:#00e5ff;">${tech.rsi.val} · ${tech.rsi.cond}</span></td>
                <td><strong style="color:#00e676;" id="txt_rsi_pts">+${tech.rsi.pts}</strong> / 10</td>
              </tr>

              <!-- 3. Stan Weinstein Stage Analysis -->
              <tr>
                <td><strong style="color:#fff;">Weinstein Stage Analysis</strong></td>
                <td>
                  <div style="display:flex;gap:4px;flex-wrap:wrap;">
                    <button class="tech-pill-btn ${tech.stage.pts === 20 ? 'active-pill' : ''}" id="pill_stage_2" onclick="adjustTechParam('stage', 20, 'Stage 2 (Mark-Up Breakout above 30-WMA)')">Stage 2 [20 pts]</button>
                    <button class="tech-pill-btn ${tech.stage.pts === 5 ? 'active-pill' : ''}" id="pill_stage_1" onclick="adjustTechParam('stage', 5, 'Stage 1 (Accumulation / Base Building)')">Stage 1 [5 pts]</button>
                    <button class="tech-pill-btn ${tech.stage.pts === 0 && tech.stage.val.includes('Stage 3') ? 'active-pill' : ''}" id="pill_stage_3" onclick="adjustTechParam('stage', 0, 'Stage 3 (Distribution / Churn)')">Stage 3 [0 pts]</button>
                    <button class="tech-pill-btn ${tech.stage.pts === 0 && tech.stage.val.includes('Stage 4') ? 'active-pill' : ''}" id="pill_stage_4" onclick="adjustTechParam('stage', 0, 'Stage 4 (Mark-Down / Falling Knife)')">Stage 4 [0 pts]</button>
                  </div>
                </td>
                <td><span id="txt_stage_status" style="color:#ffaa00;">${tech.stage.val} · ${tech.stage.cond}</span></td>
                <td><strong style="color:#00e676;" id="txt_stage_pts">+${tech.stage.pts}</strong> / 20</td>
              </tr>

              <!-- 4. Price Volume Action -->
              <tr>
                <td><strong style="color:#fff;">Price Volume Action (PVA)</strong></td>
                <td>
                  <div style="display:flex;gap:4px;flex-wrap:wrap;">
                    <button class="tech-pill-btn ${tech.pva.pts === 20 ? 'active-pill' : ''}" id="pill_pva_20" onclick="adjustTechParam('pva', 20, 'Positive Trend (High Volume on Gain Days)')">+ve Trend [20 pts]</button>
                    <button class="tech-pill-btn ${tech.pva.pts === 10 ? 'active-pill' : ''}" id="pill_pva_10" onclick="adjustTechParam('pva', 10, 'Neutral Volume Action')">Neutral [10 pts]</button>
                    <button class="tech-pill-btn ${tech.pva.pts === 0 ? 'active-pill' : ''}" id="pill_pva_0" onclick="adjustTechParam('pva', 0, 'Distribution (High Volume on Down Days)')">Distribution [0 pts]</button>
                  </div>
                </td>
                <td><span id="txt_pva_status" style="color:#00e676;">${tech.pva.val} · ${tech.pva.cond}</span></td>
                <td><strong style="color:#00e676;" id="txt_pva_pts">+${tech.pva.pts}</strong> / 20</td>
              </tr>

              <!-- 5. Secondary Trend -->
              <tr>
                <td><strong style="color:#fff;">Secondary Trend</strong></td>
                <td>
                  <div style="display:flex;gap:4px;flex-wrap:wrap;">
                    <button class="tech-pill-btn ${tech.secondary.pts === 10 ? 'active-pill' : ''}" id="pill_sec_10" onclick="adjustTechParam('secondary', 10, 'Uptrend Pullback to 10-WEMA / 50-DMA')">Uptrend [10 pts]</button>
                    <button class="tech-pill-btn ${tech.secondary.pts === 5 ? 'active-pill' : ''}" id="pill_sec_5" onclick="adjustTechParam('secondary', 5, 'Sideways Consolidation')">Sideways [5 pts]</button>
                    <button class="tech-pill-btn ${tech.secondary.pts === 0 ? 'active-pill' : ''}" id="pill_sec_0" onclick="adjustTechParam('secondary', 0, 'Downtrend Breakdown')">Downtrend [0 pts]</button>
                  </div>
                </td>
                <td><span id="txt_secondary_status" style="color:#00e5ff;">${tech.secondary.val} · ${tech.secondary.cond}</span></td>
                <td><strong style="color:#00e676;" id="txt_secondary_pts">+${tech.secondary.pts}</strong> / 10</td>
              </tr>

              <!-- 6. Primary Macro Trend -->
              <tr>
                <td><strong style="color:#fff;">Primary Macro Trend</strong></td>
                <td>
                  <div style="display:flex;gap:4px;flex-wrap:wrap;">
                    <button class="tech-pill-btn ${tech.primary.pts === 10 ? 'active-pill' : ''}" id="pill_prim_10" onclick="adjustTechParam('primary', 10, 'Trading above rising 30-WMA & 200-DMA')">Above 200D [10 pts]</button>
                    <button class="tech-pill-btn ${tech.primary.pts === 5 ? 'active-pill' : ''}" id="pill_prim_5" onclick="adjustTechParam('primary', 5, 'Flat Moving Averages')">Flat [5 pts]</button>
                    <button class="tech-pill-btn ${tech.primary.pts === 0 ? 'active-pill' : ''}" id="pill_prim_0" onclick="adjustTechParam('primary', 0, 'Below declining 200-DMA')">Below 200D [0 pts]</button>
                  </div>
                </td>
                <td><span id="txt_primary_status" style="color:#00e5ff;">${tech.primary.val} · ${tech.primary.cond}</span></td>
                <td><strong style="color:#00e676;" id="txt_primary_pts">+${tech.primary.pts}</strong> / 10</td>
              </tr>

              <!-- 7. Resistance Proximity -->
              <tr>
                <td><strong style="color:#fff;">Resistance Proximity</strong></td>
                <td>
                  <div style="display:flex;gap:4px;flex-wrap:wrap;">
                    <button class="tech-pill-btn ${tech.resistance.pts === 5 ? 'active-pill' : ''}" id="pill_res_5" onclick="adjustTechParam('resistance', 5, 'Close to 52-Week High / ATH Breakout (<15%)')">Breakout [5 pts]</button>
                    <button class="tech-pill-btn ${tech.resistance.pts === 0 ? 'active-pill' : ''}" id="pill_res_0" onclick="adjustTechParam('resistance', 0, 'Heavy Overhead Supply Overhang')">Resistance [0 pts]</button>
                  </div>
                </td>
                <td><span id="txt_res_status" style="color:#00e676;">${tech.resistance.val} · ${tech.resistance.cond}</span></td>
                <td><strong style="color:#00e676;" id="txt_res_pts">+${tech.resistance.pts}</strong> / 5</td>
              </tr>

              <!-- 8. V-Stop Trailing Volatility Stop -->
              <tr>
                <td><strong style="color:#fff;">V-Stop Trailing Stop</strong></td>
                <td>
                  <div style="display:flex;gap:4px;flex-wrap:wrap;">
                    <button class="tech-pill-btn ${tech.vstop.pts === 10 ? 'active-pill' : ''}" id="pill_vstop_10" onclick="adjustTechParam('vstop', 10, 'Positive Green (Holding above Weekly/Monthly ATR stop)')">Green (+10 pts)</button>
                    <button class="tech-pill-btn ${tech.vstop.pts === 0 ? 'active-pill' : ''}" id="pill_vstop_0" onclick="adjustTechParam('vstop', 0, 'Negative Red (Trailing Stop Breached)')">Red [0 pts]</button>
                  </div>
                </td>
                <td><span id="txt_vstop_status" style="color:#00e676;">${tech.vstop.val} · ${tech.vstop.cond}</span></td>
                <td><strong style="color:#00e676;" id="txt_vstop_pts">+${tech.vstop.pts}</strong> / 10</td>
              </tr>
            </tbody>
          </table>
        </div>

        <!-- ⚡ REAL-TIME DCF SENSITIVITY MATRIX & INTRINSIC VALUE RE-CALCULATOR -->
        <div style="background:#070c16;border:1px solid #1f3a5f;border-radius:6px;padding:12px;margin-bottom:12px;font-family:var(--font-mono);">
          <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:10px;flex-wrap:wrap;gap:8px;">
            <div>
              <span style="color:#00ff88;font-size:11px;font-weight:800;">⚡ REAL-TIME DCF SENSITIVITY CALCULATOR</span>
              <span style="color:#94a3b8;font-size:9.5px;margin-left:6px;">(Adjust WACC, Growth, and OPM to test intrinsic valuation)</span>
            </div>
            <span class="badge" id="live_dcf_signal" style="background:#00e676;color:#000;font-weight:800;font-size:10px;">${data.mos.includes('+') ? 'UNDERVALUED (' + data.mos + ' MoS)' : 'FAIR VALUE'}</span>
          </div>

          <div style="display:grid;grid-template-columns:repeat(3, 1fr);gap:12px;margin-bottom:10px;">
            <div>
              <div style="display:flex;justify-content:space-between;font-size:10px;margin-bottom:2px;">
                <span style="color:#94a3b8;">DISCOUNT RATE (WACC):</span>
                <strong style="color:#00e5ff;" id="lbl_dcf_wacc">11.2%</strong>
              </div>
              <input type="range" id="slider_dcf_wacc" min="8.0" max="15.0" step="0.1" value="11.2" oninput="updateInteractiveDCF()" style="width:100%;accent-color:#00e5ff;cursor:pointer;">
            </div>

            <div>
              <div style="display:flex;justify-content:space-between;font-size:10px;margin-bottom:2px;">
                <span style="color:#94a3b8;">TERMINAL GROWTH (g):</span>
                <strong style="color:#ffaa00;" id="lbl_dcf_g">5.0%</strong>
              </div>
              <input type="range" id="slider_dcf_g" min="3.0" max="6.5" step="0.1" value="5.0" oninput="updateInteractiveDCF()" style="width:100%;accent-color:#ffaa00;cursor:pointer;">
            </div>

            <div>
              <div style="display:flex;justify-content:space-between;font-size:10px;margin-bottom:2px;">
                <span style="color:#94a3b8;">TARGET OPERATING MARGIN:</span>
                <strong style="color:#00ff88;" id="lbl_dcf_margin">${data.dupontROE.opMargin}</strong>
              </div>
              <input type="range" id="slider_dcf_margin" min="5.0" max="40.0" step="0.5" value="${parseFloat(data.dupontROE.opMargin)}" oninput="updateInteractiveDCF()" style="width:100%;accent-color:#00ff88;cursor:pointer;">
            </div>
          </div>

          <div style="background:#04070d;border:1px solid #142236;border-radius:4px;padding:8px 12px;display:flex;justify-content:space-between;align-items:center;font-size:10.5px;flex-wrap:wrap;gap:8px;">
            <div>
              <span style="color:#94a3b8;">INTRINSIC DCF TARGET: </span>
              <strong style="color:#fff;font-size:13px;" id="val_dcf_target">${data.dcf}</strong>
              <span style="color:#64748b;margin-left:6px;">(CMP: <span id="val_dcf_cmp">${data.cmp}</span>)</span>
            </div>
            <div>
              <span style="color:#94a3b8;">DYNAMIC MARGIN OF SAFETY: </span>
              <strong style="color:#00e676;font-size:13px;" id="val_dcf_mos">${data.mos}</strong>
            </div>
            <button onclick="resetInteractiveDCF()" style="background:#132032;color:#94a3b8;border:1px solid #1e334d;padding:3px 8px;font-size:9.5px;border-radius:3px;cursor:pointer;">↺ Reset DCF Baseline</button>
          </div>
        </div>
"""

    # 2b. Interactive DOM Order Book Generator
    interactive_dom_box = """
        <!-- Microstructure Level 2 Order Book DOM Simulator -->
        <div style="background:#090d16;border:1px solid #1a293d;border-radius:6px;padding:14px;font-family:var(--font-mono);font-size:10px;">
          <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:8px;">
            <span style="color:#ffaa00;font-weight:800;">LEVEL 2 ORDER BOOK DEPTH (DOM MICROSTRUCTURE)</span>
            <span style="color:#00e676;font-size:9px;">● LIVE 850ns TICK</span>
          </div>

          <div style="display:grid;grid-template-columns:1fr 1fr;gap:8px;margin-bottom:8px;">
            <!-- Bid Side -->
            <div>
              <div style="color:#00e676;font-weight:700;border-bottom:1px solid #1e334d;padding-bottom:2px;margin-bottom:4px;">BIDS (BUY DEPTH)</div>
              <div style="display:flex;justify-content:space-between;color:#94a3b8;padding:2px 0;"><span id="dom_bid_p1">3,410.25</span><span style="color:#00e676;" id="dom_bid_s1">4,200</span></div>
              <div style="display:flex;justify-content:space-between;color:#94a3b8;padding:2px 0;"><span id="dom_bid_p2">3,410.00</span><span style="color:#00e676;" id="dom_bid_s2">8,500</span></div>
              <div style="display:flex;justify-content:space-between;color:#94a3b8;padding:2px 0;"><span id="dom_bid_p3">3,409.75</span><span style="color:#00e676;" id="dom_bid_s3">12,400</span></div>
              <div style="display:flex;justify-content:space-between;color:#94a3b8;padding:2px 0;"><span id="dom_bid_p4">3,409.50</span><span style="color:#00e676;" id="dom_bid_s4">16,800</span></div>
              <div style="display:flex;justify-content:space-between;color:#94a3b8;padding:2px 0;"><span id="dom_bid_p5">3,409.00</span><span style="color:#00e676;" id="dom_bid_s5">24,000</span></div>
            </div>

            <!-- Ask Side -->
            <div>
              <div style="color:#ff3344;font-weight:700;border-bottom:1px solid #1e334d;padding-bottom:2px;margin-bottom:4px;">ASKS (SELL DEPTH)</div>
              <div style="display:flex;justify-content:space-between;color:#94a3b8;padding:2px 0;"><span id="dom_ask_p1">3,410.50</span><span style="color:#ff3344;" id="dom_ask_s1">2,100</span></div>
              <div style="display:flex;justify-content:space-between;color:#94a3b8;padding:2px 0;"><span id="dom_ask_p2">3,410.75</span><span style="color:#ff3344;" id="dom_ask_s2">5,400</span></div>
              <div style="display:flex;justify-content:space-between;color:#94a3b8;padding:2px 0;"><span id="dom_ask_p3">3,411.00</span><span style="color:#ff3344;" id="dom_ask_s3">9,200</span></div>
              <div style="display:flex;justify-content:space-between;color:#94a3b8;padding:2px 0;"><span id="dom_ask_p4">3,411.25</span><span style="color:#ff3344;" id="dom_ask_s4">14,500</span></div>
              <div style="display:flex;justify-content:space-between;color:#94a3b8;padding:2px 0;"><span id="dom_ask_p5">3,411.50</span><span style="color:#ff3344;" id="dom_ask_s5">19,800</span></div>
            </div>
          </div>

          <div style="background:#05080e;border:1px solid #131e2d;border-radius:4px;padding:6px;display:flex;justify-content:space-between;font-size:9px;margin-bottom:8px;">
            <span>SPREAD: <strong style="color:#fff;" id="dom_spread">0.25 bps</strong></span>
            <span>OFI: <strong style="color:#00e676;" id="dom_ofi">+0.28 (BULLISH)</strong></span>
            <span>VPIN: <strong style="color:#00e5ff;" id="dom_vpin">0.142</strong></span>
            <span>KYLE'S IMPACT: <strong style="color:#ffaa00;" id="dom_kyle">+0.42 bps</strong></span>
          </div>

          <!-- Interactive Block Order Actions -->
          <div style="display:flex;gap:4px;flex-wrap:wrap;">
            <button onclick="injectDomBlockOrder('BUY', 10000)" style="background:#064e3b;color:#34d399;border:1px solid #059669;padding:3px 6px;font-size:9px;font-weight:700;border-radius:3px;cursor:pointer;">+ BUY 10k BLOCK</button>
            <button onclick="injectDomBlockOrder('SELL', 10000)" style="background:#7f1d1d;color:#f87171;border:1px solid #dc2626;padding:3px 6px;font-size:9px;font-weight:700;border-radius:3px;cursor:pointer;">- SELL 10k BLOCK</button>
            <button onclick="injectDomBlockOrder('ALADDIN', 50000)" style="background:#1e3a5f;color:#60a5fa;border:1px solid #3b82f6;padding:3px 6px;font-size:9px;font-weight:700;border-radius:3px;cursor:pointer;">⚡ 50k ALADDIN VWAP</button>
            <button onclick="resetDomOrderBook()" style="background:#0f172a;color:#94a3b8;border:1px solid #334155;padding:3px 6px;font-size:9px;border-radius:3px;cursor:pointer;">↺ RESET DOM</button>
          </div>
        </div>
"""

    # Replace the static technical table in zoom_code with interactive_tech_table
    pattern_tech = r'<!-- ⚡ DEEP 110-POINT TECHNICAL ANALYSIS[\s\S]*?</table>\s*</div>'
    if re.search(pattern_tech, zoom_code):
        zoom_code = re.sub(pattern_tech, interactive_tech_table.strip(), zoom_code, count=1)
        print("Successfully injected interactive technical table sandbox and real-time DCF calculator.")
    else:
        print("Warning: pattern_tech not matched.")

    # Replace static DOM with interactive_dom_box
    pattern_dom = r'<!-- Microstructure Level 2 Order Book DOM Simulator -->[\s\S]*?</div>\s*</div>\s*</div>\s*`;'
    replacement_dom = interactive_dom_box.strip() + "\n      </div>\n    `;"
    if re.search(pattern_dom, zoom_code):
        zoom_code = re.sub(pattern_dom, replacement_dom, zoom_code, count=1)
        print("Successfully injected interactive Level 2 DOM block order simulator.")
    else:
        print("Warning: pattern_dom not matched.")

    # Inject JS functions for adjustTechParam, updateInteractiveDCF, injectDomBlockOrder, syncGlobalDropdowns
    js_interactive_funcs = """
  // ── INTERACTIVE SOIC TECHNICAL SCORE SANDBOX ENGINE ──
  var activeTechScores = {};

  window.adjustTechParam = function(paramKey, pts, label) {
    if (!activeTechScores[currentFirm]) {
      var f = firmData[currentFirm];
      activeTechScores[currentFirm] = JSON.parse(JSON.stringify(f.technicalSOIC));
    }
    var tObj = activeTechScores[currentFirm];
    if (tObj[paramKey]) {
      tObj[paramKey].pts = pts;
      tObj[paramKey].cond = label;
    }

    // Recompute total tech score
    var sumTech = 0;
    Object.keys(tObj).forEach(function(k) {
      if (tObj[k] && typeof tObj[k].pts === 'number') {
        sumTech += tObj[k].pts;
      }
    });

    var f = firmData[currentFirm];
    var baseFunda = f.soicScore.funda;
    var baseInd = f.soicScore.industry;
    var baseVal = f.soicScore.val;
    var baseForensic = f.soicScore.forensic;
    var grandTotal = baseInd + baseFunda + sumTech + baseVal + baseForensic;

    // Update UI elements
    var dynTech = document.getElementById('dyn_tech_score');
    if (dynTech) dynTech.textContent = sumTech;
    var txtPts = document.getElementById('txt_' + paramKey + '_pts');
    if (txtPts) txtPts.textContent = '+' + pts;
    var txtStatus = document.getElementById('txt_' + paramKey + '_status');
    if (txtStatus) txtStatus.textContent = label;

    // Update active pill styling
    var rowPills = document.querySelectorAll('#interactive_tech_table tr button');
    rowPills.forEach(function(btn) {
      if (btn.id.startsWith('pill_' + paramKey)) {
        if (btn.id === 'pill_' + paramKey + '_' + pts) {
          btn.classList.add('active-pill');
          btn.style.background = '#00e676';
          btn.style.color = '#000';
          btn.style.fontWeight = '700';
        } else {
          btn.classList.remove('active-pill');
          btn.style.background = '#132032';
          btn.style.color = '#94a3b8';
          btn.style.fontWeight = '400';
        }
      }
    });

    // Update live badge
    var b = document.getElementById('live_tech_score_badge');
    if (b) {
      b.style.background = (sumTech >= 100) ? '#00e676' : ((sumTech >= 80) ? '#00e5ff' : '#ffaa00');
    }
  };

  window.resetTechScores = function() {
    if (activeTechScores[currentFirm]) {
      delete activeTechScores[currentFirm];
    }
    loadFirmModel(currentFirm);
  };

  // ── REAL-TIME DCF SENSITIVITY CALCULATOR ──
  window.updateInteractiveDCF = function() {
    var f = firmData[currentFirm];
    if (!f) return;

    var wacc = parseFloat(document.getElementById('slider_dcf_wacc').value);
    var g = parseFloat(document.getElementById('slider_dcf_g').value);
    var margin = parseFloat(document.getElementById('slider_dcf_margin').value);

    document.getElementById('lbl_dcf_wacc').textContent = wacc.toFixed(1) + '%';
    document.getElementById('lbl_dcf_g').textContent = g.toFixed(1) + '%';
    document.getElementById('lbl_dcf_margin').textContent = margin.toFixed(1) + '%';

    // Parse CMP
    var cleanCMP = parseFloat(f.cmp.replace(/[^0-9.]/g, '')) || 100.0;
    var baseDCF = parseFloat(f.dcf.replace(/[^0-9.]/g, '')) || 115.0;

    // Gordon Growth sensitivity formula: Value proportional to (Margin / WACC - g)
    var baseWacc = 11.2, baseG = 5.0;
    var baseSpread = (baseWacc - baseG) / 100.0;
    var dynSpread = Math.max(0.015, (wacc - g) / 100.0);
    var marginFactor = margin / Math.max(5.0, parseFloat(f.dupontROE.opMargin) || 12.0);

    var dynDCF = baseDCF * (baseSpread / dynSpread) * (0.5 + 0.5 * marginFactor);
    var mosPct = ((dynDCF - cleanCMP) / dynDCF) * 100.0;

    var prefix = f.cmp.includes('$') ? '$' : '₹';
    document.getElementById('val_dcf_target').textContent = prefix + dynDCF.toFixed(2);
    document.getElementById('val_dcf_mos').textContent = (mosPct >= 0 ? '+' : '') + mosPct.toFixed(1) + '%';
    document.getElementById('val_dcf_mos').style.color = (mosPct >= 10) ? '#00e676' : ((mosPct >= 0) ? '#ffaa00' : '#ff3344');

    var sig = document.getElementById('live_dcf_signal');
    if (sig) {
      if (mosPct >= 15.0) {
        sig.textContent = 'HIGH CONVICTION BUY (' + mosPct.toFixed(1) + '% MoS)';
        sig.style.background = '#00e676';
        sig.style.color = '#000';
      } else if (mosPct >= 0.0) {
        sig.textContent = 'FAIR VALUE (' + mosPct.toFixed(1) + '% MoS)';
        sig.style.background = '#ffaa00';
        sig.style.color = '#000';
      } else {
        sig.textContent = 'OVERVALUED / TRIM (' + mosPct.toFixed(1) + '% MoS)';
        sig.style.background = '#ff3344';
        sig.style.color = '#fff';
      }
    }
  };

  window.resetInteractiveDCF = function() {
    loadFirmModel(currentFirm);
  };

  // ── LEVEL 2 DOM INTERACTIVE BLOCK ORDER SIMULATOR ──
  var domDelta = 0;
  window.injectDomBlockOrder = function(side, shares) {
    if (side === 'BUY') {
      domDelta += shares;
      var s1 = document.getElementById('dom_bid_s1');
      if (s1) s1.textContent = (parseInt(s1.textContent.replace(/,/g, '')) + shares).toLocaleString();
      var ofi = document.getElementById('dom_ofi');
      if (ofi) { ofi.textContent = '+0.48 (VERY BULLISH)'; ofi.style.color = '#00e676'; }
      var kyle = document.getElementById('dom_kyle');
      if (kyle) kyle.textContent = '+0.85 bps (Slippage)';
    } else if (side === 'SELL') {
      domDelta -= shares;
      var a1 = document.getElementById('dom_ask_s1');
      if (a1) a1.textContent = (parseInt(a1.textContent.replace(/,/g, '')) + shares).toLocaleString();
      var ofi = document.getElementById('dom_ofi');
      if (ofi) { ofi.textContent = '-0.35 (BEARISH PRESSURE)'; ofi.style.color = '#ff3344'; }
      var kyle = document.getElementById('dom_kyle');
      if (kyle) kyle.textContent = '+0.92 bps (Slippage)';
    } else if (side === 'ALADDIN') {
      var s1 = document.getElementById('dom_bid_s1');
      if (s1) s1.textContent = (parseInt(s1.textContent.replace(/,/g, '')) + Math.round(shares*0.6)).toLocaleString();
      var a1 = document.getElementById('dom_ask_s1');
      if (a1) a1.textContent = (parseInt(a1.textContent.replace(/,/g, '')) + Math.round(shares*0.4)).toLocaleString();
      var vpin = document.getElementById('dom_vpin');
      if (vpin) vpin.textContent = '0.088 (OPTIMAL EXECUTION)';
      var kyle = document.getElementById('dom_kyle');
      if (kyle) kyle.textContent = '+0.15 bps (MINIMAL SLIPPAGE)';
    }
  };

  window.resetDomOrderBook = function() {
    loadNanoAsset(currentNano);
  };

  // ── GLOBAL EXPOSURES & BIDIRECTIONAL SYNC ──
  window.countryData = countryData;
  window.sectorData = sectorData;
  window.firmData = firmData;
  window.nanoData = nanoData;
  window.getCurrentZoomState = function() {
    return {
      tier: currentTier, country: currentCountry, sector: currentSector, firm: currentFirm, nano: currentNano
    };
  };

  // Sync to global top ribbon
  function syncGlobalRibbon() {
    var gc = document.getElementById('global_country_select');
    var gs = document.getElementById('global_sector_select');
    var gf = document.getElementById('global_firm_select');
    var gn = document.getElementById('global_nano_select');

    if (gc && gc.value !== currentCountry) gc.value = currentCountry;
    if (gs && countryData[currentCountry]) {
      gs.innerHTML = '';
      countryData[currentCountry].sectors.forEach(function(sKey) {
        var s = sectorData[sKey];
        if (s) {
          var o = document.createElement('option');
          o.value = sKey;
          o.textContent = s.name;
          gs.appendChild(o);
        }
      });
      gs.value = currentSector;
    }
    if (gf && sectorData[currentSector] && sectorData[currentSector].firmKeys) {
      gf.innerHTML = '';
      sectorData[currentSector].firmKeys.forEach(function(fKey) {
        var f = firmData[fKey];
        if (f) {
          var o = document.createElement('option');
          o.value = fKey;
          o.textContent = f.name + ' [' + f.ticker + ']';
          gf.appendChild(o);
        }
      });
      gf.value = currentFirm;
    }
    if (gn && firmData[currentFirm]) {
      gn.innerHTML = '';
      var f = firmData[currentFirm];
      if (f.nanoLink && nanoData[f.nanoLink]) {
        var o = document.createElement('option');
        o.value = f.nanoLink;
        o.textContent = nanoData[f.nanoLink].title;
        gn.appendChild(o);
      }
      var oDom = document.createElement('option');
      oDom.value = 'dom';
      oDom.textContent = '📊 Level 2 Order Book (DOM Microstructure)';
      gn.appendChild(oDom);
      gn.value = currentNano;
    }
  }

  // Hook syncGlobalRibbon into onCountryDropdownChange, onSectorDropdownChange, onFirmDropdownChange, onNanoDropdownChange
"""

    # Inject js_interactive_funcs before document.addEventListener in zoom_code
    pattern_init = r'// ── INITIALIZATION ON DOM READY ──'
    if pattern_init in zoom_code:
        zoom_code = zoom_code.replace(pattern_init, js_interactive_funcs + "\n\n  " + pattern_init)
        print("Successfully injected interactive JS functions.")
    else:
        print("Warning: pattern_init not matched.")

    # Also add syncGlobalRibbon() inside updateBreadcrumbs()
    if 'updateBreadcrumbs()' in zoom_code:
        zoom_code = zoom_code.replace('function updateBreadcrumbs() {', 'function updateBreadcrumbs() {\n    syncGlobalRibbon();')
        print("Successfully hooked syncGlobalRibbon into updateBreadcrumbs.")

    # Add style for .tech-pill-btn and .active-pill
    css_pills = """
<style>
.tech-pill-btn {
  background: #132032;
  color: #94a3b8;
  border: 1px solid #1c2e44;
  border-radius: 3px;
  padding: 2px 6px;
  font-size: 9px;
  cursor: pointer;
  transition: all 0.15s ease;
  font-family: var(--font-mono);
}
.tech-pill-btn:hover {
  background: #1e334d;
  color: #fff;
  border-color: #3b82f6;
}
.tech-pill-btn.active-pill {
  background: #00e676 !important;
  color: #000 !important;
  font-weight: 700 !important;
  border-color: #00e676 !important;
}
</style>
"""
    zoom_code = css_pills + "\n" + zoom_code

    with open(zoom_path, 'w', encoding='utf-8') as f:
        f.write(zoom_code)
    print(f"Updated {zoom_path}. Length: {len(zoom_code)} chars.")

    # Step 3: Update generate_dashboard.py to embed the Universal Cascading Master Ribbon above the tabs
    gen_path = r'F:\documents\SOIC\EconAgent_Platform\platform_ui\generate_dashboard.py'
    with open(gen_path, 'r', encoding='utf-8') as f:
        gen_code = f.read()

    global_ribbon_html = """
<!-- ── UNIVERSAL CASCADING MULTIFUNCTION SELECTOR RIBBON (CROSS-TAB INTERCONNECTED) ── -->
<div class="global-cascading-bar" style="background: linear-gradient(90deg, #060c14 0%, #0d1726 50%, #122137 100%); border: 1px solid #1f3a5f; border-bottom: 2px solid #00e5ff; border-radius: 6px; padding: 10px 16px; margin: 10px 0 12px 0; display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 12px; font-family: var(--font-mono); box-shadow: 0 4px 12px rgba(0,0,0,0.5);">
  <div style="display: flex; align-items: center; gap: 12px; flex-wrap: wrap;">
    
    <!-- Global Country Selector -->
    <div style="display: flex; align-items: center; gap: 6px;">
      <span style="color: #ffaa00; font-size: 11px; font-weight: 800; display: flex; align-items: center; gap: 4px;">
        <span>📍</span> GLOBAL COUNTRY:
      </span>
      <select id="global_country_select" onchange="syncGlobalCountryChange(this.value)" style="background: #0d1a2d; color: #00e5ff; border: 1px solid #294c7a; border-radius: 4px; padding: 5px 10px; font-size: 11px; font-weight: 700; font-family: var(--font-mono); cursor: pointer; outline: none;">
        <option value="india">🇮🇳 India (Baa3 / CRP 2.38%)</option>
        <option value="us">🇺🇸 United States (Aaa / CRP 0.00%)</option>
        <option value="germany">🇩🇪 Germany (Aaa / CRP 0.00%)</option>
        <option value="japan">🇯🇵 Japan (A1 / CRP 0.65%)</option>
        <option value="uk">🇬🇧 United Kingdom (Aa3 / CRP 0.75%)</option>
        <option value="china">🇨🇳 China (A1 / CRP 0.94%)</option>
        <option value="brazil">🇧🇷 Brazil (Ba2 / CRP 3.82%)</option>
        <option value="saudi">🇸🇦 Saudi Arabia (A1 / CRP 0.85%)</option>
        <option value="singapore">🇸🇬 Singapore (Aaa / CRP 0.00%)</option>
        <option value="australia">🇦🇺 Australia (Aaa / CRP 0.00%)</option>
        <option value="korea">🇰🇷 South Korea (Aa2 / CRP 0.55%)</option>
        <option value="uae">🇦🇪 UAE (Aa2 / CRP 0.58%)</option>
      </select>
    </div>

    <!-- Global Sector Selector -->
    <div style="display: flex; align-items: center; gap: 6px;">
      <span style="color: #00e5ff; font-size: 11px; font-weight: 800; display: flex; align-items: center; gap: 4px;">
        <span>🏭</span> INDUSTRIAL SECTOR:
      </span>
      <select id="global_sector_select" onchange="syncGlobalSectorChange(this.value)" style="background: #0d1a2d; color: #ffeb3b; border: 1px solid #294c7a; border-radius: 4px; padding: 5px 10px; font-size: 11px; font-weight: 700; font-family: var(--font-mono); cursor: pointer; outline: none;">
        <option value="cables_in">Cables, Wires &amp; EHV Power Infrastructure (India)</option>
        <option value="edu_in">Education, EdTech &amp; Skill Development (India)</option>
        <option value="chem_in">Specialty Chemicals &amp; Fluorine (India)</option>
        <option value="hosp_in">Hospitals &amp; Healthcare Facilities (India)</option>
        <option value="hotel_in">Hotels &amp; Hospitality (India)</option>
        <option value="pipe_in">Power Piping &amp; Structural Steel (India)</option>
        <option value="bank_in">Private Banking &amp; High-ROE NBFCs (India)</option>
      </select>
    </div>

    <!-- Global Active Company Selector -->
    <div style="display: flex; align-items: center; gap: 6px;">
      <span style="color: #00ff88; font-size: 11px; font-weight: 800; display: flex; align-items: center; gap: 4px;">
        <span>🏢</span> ACTIVE COMPANY:
      </span>
      <select id="global_firm_select" onchange="syncGlobalFirmChange(this.value)" style="background: #0d1a2d; color: #00ff88; border: 1px solid #294c7a; border-radius: 4px; padding: 5px 10px; font-size: 11px; font-weight: 700; font-family: var(--font-mono); cursor: pointer; outline: none;">
        <option value="polycab">Polycab India Ltd [POLYCAB:IN]</option>
        <option value="kei">KEI Industries Ltd [KEI:IN]</option>
        <option value="rrkabel">R R Kabel Ltd [RRKABEL:IN]</option>
        <option value="finolex">Finolex Cables Ltd [FINCABLES:IN]</option>
      </select>
    </div>

    <!-- Global Nano Asset Selector -->
    <div style="display: flex; align-items: center; gap: 6px;">
      <span style="color: #e040fb; font-size: 11px; font-weight: 800; display: flex; align-items: center; gap: 4px;">
        <span>🔬</span> NANO ASSET / DOM:
      </span>
      <select id="global_nano_select" onchange="syncGlobalNanoChange(this.value)" style="background: #0d1a2d; color: #e040fb; border: 1px solid #294c7a; border-radius: 4px; padding: 5px 10px; font-size: 11px; font-weight: 700; font-family: var(--font-mono); cursor: pointer; outline: none;">
        <option value="halol_mega">🏭 Polycab Halol Mega Manufacturing Complex (Gujarat)</option>
        <option value="dom">📊 Level 2 Order Book (DOM Microstructure)</option>
      </select>
    </div>
  </div>

  <!-- Direct Tab Jumps for Active Selection -->
  <div style="display: flex; align-items: center; gap: 8px;">
    <button onclick="jumpToTabForActiveFirm('zoom')" class="action-btn" style="background: #1e3a5f; color: #00e5ff; font-size: 10px; font-weight: 700; padding: 5px 10px; border-radius: 4px; border: 1px solid #3b82f6; cursor: pointer;">🔬 F1 ZOOM</button>
    <button onclick="jumpToTabForActiveFirm('soic')" class="action-btn" style="background: #1e3a5f; color: #ffaa00; font-size: 10px; font-weight: 700; padding: 5px 10px; border-radius: 4px; border: 1px solid #f59e0b; cursor: pointer;">🏆 F5 SOIC 310-PT</button>
    <button onclick="jumpToTabForActiveFirm('predictor')" class="action-btn" style="background: #1e3a5f; color: #00ff88; font-size: 10px; font-weight: 700; padding: 5px 10px; border-radius: 4px; border: 1px solid #10b981; cursor: pointer;">🔮 F2/F3 DCF</button>
    <button onclick="jumpToTabForActiveFirm('bmap')" class="action-btn" style="background: #1e3a5f; color: #e040fb; font-size: 10px; font-weight: 700; padding: 5px 10px; border-radius: 4px; border: 1px solid #c084fc; cursor: pointer;">🚢 F9 BMAP</button>
  </div>
</div>
"""

    if '<!-- ── UNIVERSAL CASCADING MULTIFUNCTION SELECTOR RIBBON' not in gen_code:
        pattern_tabs = r'(<!-- ── TABS ── -->)'
        gen_code = re.sub(pattern_tabs, global_ribbon_html + "\n\\1", gen_code, count=1)
        print("Successfully injected Universal Cascading Master Ribbon above tabs in generate_dashboard.py.")
    else:
        print("Global ribbon already present in generate_dashboard.py.")

    # Add global synchronization JS functions in generate_dashboard.py
    global_js_sync = """
// ── UNIVERSAL GLOBAL DROPDOWN MASTER SYNCHRONIZATION ──
function syncGlobalCountryChange(countryKey) {
  if (typeof window.onCountryDropdownChange === 'function') {
    window.onCountryDropdownChange(countryKey);
  }
}

function syncGlobalSectorChange(sectorKey) {
  if (typeof window.onSectorDropdownChange === 'function') {
    window.onSectorDropdownChange(sectorKey);
  }
}

function syncGlobalFirmChange(firmKey) {
  if (typeof window.onFirmDropdownChange === 'function') {
    window.onFirmDropdownChange(firmKey);
  }
}

function syncGlobalNanoChange(nanoKey) {
  if (typeof window.onNanoDropdownChange === 'function') {
    window.onNanoDropdownChange(nanoKey);
  }
}

function jumpToTabForActiveFirm(tabId) {
  showTab(null, tabId);
  if (tabId === 'zoom') {
    if (typeof window.setFractalTier === 'function') window.setFractalTier(4);
  } else if (tabId === 'bmap') {
    var nKey = document.getElementById('global_nano_select') ? document.getElementById('global_nano_select').value : 'halol_mega';
    if (window.nanoData && window.nanoData[nKey] && typeof window.syncMapToNanoCoords === 'function') {
      var c = window.nanoData[nKey].coords;
      window.syncMapToNanoCoords(c[0], c[1]);
    }
  }
}
"""

    if 'function syncGlobalCountryChange' not in gen_code:
        gen_code = gen_code.replace('function showTab(el, tabId) {', global_js_sync + "\n\nfunction showTab(el, tabId) {")
        print("Successfully injected syncGlobalCountryChange and jumpToTabForActiveFirm in generate_dashboard.py.")

    # Extend stockPresets with new tickers: POLYCAB, RRKABEL, FINOLEX, MPS, NIIT, VERANDA, NAVNEET, STRIDE, COURSERA
    ticker_extensions = """
    'POLYCAB': 'polycab', 'POLY': 'polycab',
    'RRKABEL': 'rrkabel', 'RR': 'rrkabel',
    'FINCABLES': 'finolex', 'FINOLEX': 'finolex',
    'MPS': 'mps', 'MPSLTD': 'mps',
    'NIIT': 'niit', 'NIITMTS': 'niit',
    'VERANDA': 'veranda',
    'NAVNEET': 'navneet',
    'STRIDE': 'stride', 'LRN': 'stride',
    'COURSERA': 'coursera', 'COUR': 'coursera',
"""
    if "'POLYCAB': 'polycab'" not in gen_code:
        gen_code = gen_code.replace("'PIDI': 'pidilite', 'PIDILITE': 'pidilite',", "'PIDI': 'pidilite', 'PIDILITE': 'pidilite',\n" + ticker_extensions)
        print("Successfully added new tickers to Bloomberg command stockPresets.")

    # Extend cmdMap with CABLES and EDUCATION
    cmd_extensions = """
    'CABLE': 'zoom', 'CABLES': 'zoom', 'WIRES': 'zoom',
    'EDU': 'zoom', 'EDUCATION': 'zoom', 'EDTECH': 'zoom',
"""
    if "'CABLE': 'zoom'" not in gen_code:
        gen_code = gen_code.replace("'ZOOM': 'zoom',", "'ZOOM': 'zoom',\n" + cmd_extensions)
        print("Successfully added CABLE and EDUCATION commands to Bloomberg cmdMap.")

    with open(gen_path, 'w', encoding='utf-8') as f:
        f.write(gen_code)
    print(f"Updated {gen_path}. Length: {len(gen_code)} chars.")

if __name__ == '__main__':
    build_v3()

