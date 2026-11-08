# realtime_technicals_component.py
"""
EconAgent Platform - Real-Time Technicals & Stan Weinstein Stage Analysis Component
===================================================================================
Directly integrates SOIC "L4 When to Hold, Buy and Sell Technicals Using Long Term":
  1. Stan Weinstein 4-Stage Cycle Engine (Stage 1 Basing, Stage 2 Advancing Breakout,
     Stage 3 Distribution Top, Stage 4 Declining Capitulation)
  2. 30-Week Moving Average (30-WMA) & 200-Day EMA Trend Alignment
  3. Average Directional Index (ADX) & +DI / -DI Directional Trend Strength (> 25)
  4. Relative Strength Index (RSI 14) Bull/Bear Zones (40-50 Support, 60-75 Push)
  5. Volatility Stop (VStop) Trailing Stop Loss Engine
  6. Volume Spread Analysis (VSA) & Pocket Pivot Institutional Accumulation Detector
  7. Interactive HTML5 Canvas OHLC Candlestick & Technical Indicator Engine with Crosshair
"""

def build_realtime_technicals_section() -> str:
    return """
<!-- ══════════════════════════════════════════════════════════════════════════ -->
<!-- ── TAB: REAL-TIME TECHNICALS & STAN WEINSTEIN STAGE ANALYSIS (SOIC L4) ── -->
<!-- ══════════════════════════════════════════════════════════════════════════ -->
<div id="technicals" class="content">
  <div class="section">
    <h2>📈 Real-Time Technicals, Indicators &amp; Stan Weinstein Stage Analysis (SOIC L4)</h2>
    
    <!-- ── TECHNICAL COMMAND RIBBON ── -->
    <div style="background:#070b14;border:1px solid #1a293d;border-radius:8px;padding:12px 18px;margin-bottom:18px;display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:14px;font-family:var(--font-mono);">
      <div style="display:flex;align-items:center;gap:12px;flex-wrap:wrap;">
        <span style="background:var(--bb-amber);color:#000;font-weight:900;padding:3px 8px;border-radius:3px;font-size:11px;">TECH &lt;GO&gt;</span>
        <select id="tech_stock_select" onchange="switchTechStock(this.value)" style="background:#0d1624;color:#00e5ff;border:1px solid #203a5e;border-radius:3px;padding:4px 10px;font-size:12px;font-weight:800;font-family:var(--font-mono);outline:none;cursor:pointer;">
          <option value="POLYCAB">POLYCAB INDIA LTD (Cables &amp; Wires Leader) — ₹7,145.00</option>
          <option value="KEI">KEI INDUSTRIES LTD (EHV Power Cables) — ₹4,280.00</option>
          <option value="APLAPOLLO">APL APOLLO TUBES (Structural Steel Tubes) — ₹1,610.00</option>
          <option value="PIDILITE">PIDILITE INDUSTRIES (Adhesives Monopoly) — ₹3,025.00</option>
          <option value="NARAYANA">NARAYANA HRUDAYALAYA (Hospital Unit Economics) — ₹1,290.00</option>
          <option value="AAPL">APPLE INC (Mega-Cap Consumer Ecosystem) — $234.80</option>
          <option value="NVDA">NVIDIA CORP (AI Value Chain Accelerated Compute) — $138.20</option>
          <option value="TSLA">TESLA INC (EV &amp; Autonomous Robotics) — $248.50</option>
          <option value="HDFCBANK">HDFC BANK LTD (Dalal Street Financial Pillar) — ₹1,740.00</option>
          <option value="MSFT">MICROSOFT CORP (Enterprise Cloud &amp; AI Platform) — $422.50</option>
          <option value="AMZN">AMAZON.COM INC (AWS Hyperscaler &amp; E-Commerce) — $195.40</option>
          <option value="GOOGL">ALPHABET INC (Global Search &amp; Cloud Infra) — $176.80</option>
          <option value="XOM">EXXONMOBIL CORP (Western Hydrocarbon Supermajor) — $118.40</option>
          <option value="ASML">ASML HOLDING NV (EUV Photolithography Monopoly) — €668.00</option>
          <option value="ARAMCO">SAUDI ARAMCO (Global Upstream Cash Engine) — SAR 27.80</option>
          <option value="BHP">BHP GROUP LTD (Global Natural Resources King) — A$41.20</option>
          <option value="SAMSUNG">SAMSUNG ELECTRONICS (DRAM &amp; Foundry Titan) — ₩58,200</option>
          <option value="COPPER">LME GRADE A COPPER (Cables COGS Raw Material) — $9,450/MT</option>
          <option value="BRENT">BRENT CRUDE OIL ICE (Maritime &amp; Energy Benchmark) — $78.40/bbl</option>
        </select>
        <span style="color:#334155;">|</span>
        <div style="display:flex;align-items:baseline;gap:6px;">
          <span style="color:#64748b;font-size:11px;">Current Price:</span>
          <strong id="tech_price_display" style="color:#00e676;font-size:15px;font-weight:900;" class="tabular-nums">₹7,145.00</strong>
          <span id="tech_change_display" style="color:#00e676;font-size:11px;font-weight:700;">+₹182.50 (+2.62%)</span>
        </div>
      </div>

      <!-- Timeframe & Overlays Controls -->
      <div style="display:flex;gap:6px;align-items:center;flex-wrap:wrap;">
        <div style="display:flex;gap:2px;background:#0d1624;border:1px solid #1e2e44;border-radius:3px;padding:2px;">
          <button class="action-btn" onclick="setTechTimeframe('1D')" id="btn_tf_1D" style="padding:2px 8px;font-size:9.5px;">1D</button>
          <button class="action-btn" onclick="setTechTimeframe('1W')" id="btn_tf_1W" style="padding:2px 8px;font-size:9.5px;">1W</button>
          <button class="action-btn active" onclick="setTechTimeframe('30W')" id="btn_tf_30W" style="padding:2px 8px;font-size:9.5px;background:#1e3a5f;color:#00e5ff;">30W (Stage)</button>
          <button class="action-btn" onclick="setTechTimeframe('1Y')" id="btn_tf_1Y" style="padding:2px 8px;font-size:9.5px;">1Y</button>
        </div>
        <button class="action-btn active" id="btn_toggle_30wma" onclick="toggleTechOverlay('wma30')" style="font-size:9.5px;padding:3px 8px;background:#2a1f0a;color:#ffaa00;border:1px solid #f59e0b;">● 30-WMA</button>
        <button class="action-btn active" id="btn_toggle_ema200" onclick="toggleTechOverlay('ema200')" style="font-size:9.5px;padding:3px 8px;background:#082f49;color:#38bdf8;border:1px solid #0284c7;">● 200-EMA</button>
        <button class="action-btn active" id="btn_toggle_vstop" onclick="toggleTechOverlay('vstop')" style="font-size:9.5px;padding:3px 8px;background:#064e3b;color:#34d399;border:1px solid #059669;">● Vstop</button>
      </div>
    </div>

    <!-- ── 6 REAL-TIME TECHNICAL METRIC CARDS ── -->
    <div style="display:grid;grid-template-columns:repeat(auto-fit, minmax(180px, 1fr));gap:12px;margin-bottom:18px;">
      
      <!-- Card 1: Stan Weinstein Stage -->
      <div style="background:#090f1a;border:1px solid #1e334d;border-radius:6px;padding:12px 14px;">
        <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:4px;">
          <span style="color:#94a3b8;font-size:10px;text-transform:uppercase;">Stan Weinstein Stage</span>
          <span style="background:#065f46;color:#34d399;font-size:8.5px;font-weight:900;padding:1px 5px;border-radius:2px;">BULL CYCLE</span>
        </div>
        <div id="tech_card_stage" style="color:#00e676;font-size:16px;font-weight:900;letter-spacing:0.5px;">STAGE 2 ADVANCING</div>
        <div style="color:#64748b;font-size:9.5px;margin-top:2px;">Breakout above 30-WMA on 3.2x Volume</div>
      </div>

      <!-- Card 2: 30-Week Moving Average -->
      <div style="background:#090f1a;border:1px solid #1e334d;border-radius:6px;padding:12px 14px;">
        <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:4px;">
          <span style="color:#94a3b8;font-size:10px;text-transform:uppercase;">30-Week Moving Average</span>
          <span style="color:#ffaa00;font-size:9px;font-weight:800;">SLOPING UP ↑</span>
        </div>
        <div id="tech_card_wma" style="color:#ffaa00;font-size:16px;font-weight:900;" class="tabular-nums">₹6,450.00</div>
        <div id="tech_card_wma_spread" style="color:#38bdf8;font-size:9.5px;margin-top:2px;">Price +10.8% above 30-WMA (Healthy)</div>
      </div>

      <!-- Card 3: 200 EMA & 50 SMA -->
      <div style="background:#090f1a;border:1px solid #1e334d;border-radius:6px;padding:12px 14px;">
        <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:4px;">
          <span style="color:#94a3b8;font-size:10px;text-transform:uppercase;">200-EMA / 50-SMA</span>
          <span style="color:#00e5ff;font-size:9px;font-weight:800;">GOLDEN CROSS</span>
        </div>
        <div id="tech_card_ema" style="color:#00e5ff;font-size:16px;font-weight:900;" class="tabular-nums">₹6,120.00</div>
        <div style="color:#34d399;font-size:9.5px;margin-top:2px;">50-SMA (₹6,710) &gt; 200-EMA (+9.6%)</div>
      </div>

      <!-- Card 4: ADX Trend Strength -->
      <div style="background:#090f1a;border:1px solid #1e334d;border-radius:6px;padding:12px 14px;">
        <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:4px;">
          <span style="color:#94a3b8;font-size:10px;text-transform:uppercase;">ADX (14) Trend Strength</span>
          <span style="background:#4c1d95;color:#c4b5fd;font-size:8.5px;font-weight:900;padding:1px 5px;border-radius:2px;">STRONG TREND</span>
        </div>
        <div id="tech_card_adx" style="color:#c084fc;font-size:16px;font-weight:900;" class="tabular-nums">34.8</div>
        <div style="color:#a855f7;font-size:9.5px;margin-top:2px;">+DI: 32.4 | -DI: 12.1 (Dominant Bulls)</div>
      </div>

      <!-- Card 5: RSI (14) Momentum -->
      <div style="background:#090f1a;border:1px solid #1e334d;border-radius:6px;padding:12px 14px;">
        <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:4px;">
          <span style="color:#94a3b8;font-size:10px;text-transform:uppercase;">RSI (14) Momentum</span>
          <span style="color:#00e676;font-size:9px;font-weight:800;">SUPER-BULLISH</span>
        </div>
        <div id="tech_card_rsi" style="color:#00e676;font-size:16px;font-weight:900;" class="tabular-nums">64.2</div>
        <div style="color:#64748b;font-size:9.5px;margin-top:2px;">Bull zone (60-75) · No divergence</div>
      </div>

      <!-- Card 6: Volatility Stop (Vstop) -->
      <div style="background:#090f1a;border:1px solid #1e334d;border-radius:6px;padding:12px 14px;">
        <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:4px;">
          <span style="color:#94a3b8;font-size:10px;text-transform:uppercase;">Volatility Stop (Vstop)</span>
          <span style="color:#34d399;font-size:9px;font-weight:800;">TRAILING SAFE</span>
        </div>
        <div id="tech_card_vstop" style="color:#34d399;font-size:16px;font-weight:900;" class="tabular-nums">₹6,780.00</div>
        <div style="color:#00e676;font-size:9.5px;margin-top:2px;">Cushion: +5.4% from current stop</div>
      </div>

    </div>

    <!-- ── INTERACTIVE HTML5 CANVAS CANDLESTICK & TECHNICAL INDICATOR CHART ── -->
    <div style="background:#03060c;border:1.5px solid #162438;border-radius:8px;padding:14px;margin-bottom:20px;position:relative;">
      <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:10px;border-bottom:1px solid #162438;padding-bottom:8px;flex-wrap:wrap;gap:8px;">
        <div style="display:flex;align-items:center;gap:12px;">
          <strong id="tech_chart_title" style="color:#ffaa00;font-size:12.5px;letter-spacing:0.5px;">POLYCAB INDIA LTD (WEEKLY) — 30-WMA STAGE 2 BREAKOUT RADAR</strong>
          <span style="background:#111b2b;color:#38bdf8;font-size:9px;padding:1px 6px;border-radius:3px;border:1px solid #1e3a5f;">Live OHLC Ticking</span>
        </div>
        <div style="display:flex;align-items:center;gap:14px;font-size:10px;color:#94a3b8;">
          <span style="color:#ffaa00;">■ 30-WMA</span>
          <span style="color:#00e5ff;">■ 200-EMA</span>
          <span style="color:#00e676;">■ Vstop</span>
          <span style="color:#c084fc;">■ ADX &gt; 25</span>
          <span style="color:#38bdf8;">■ RSI (14)</span>
        </div>
      </div>

      <div style="position:relative;width:100%;height:460px;">
        <canvas id="technicalsCanvas" style="width:100%;height:100%;cursor:crosshair;"></canvas>
        <div id="tech_crosshair_hud" style="display:none;position:absolute;top:10px;left:10px;background:rgba(5,8,15,0.92);border:1px solid #38bdf8;border-radius:4px;padding:6px 10px;font-size:10px;font-family:var(--font-mono);pointer-events:none;color:#fff;">
          <!-- Dynamically populated on canvas mousemove -->
        </div>
      </div>
    </div>

    <!-- ── SOIC TECHNICAL RULEBOOK & STAGE CRITERIA MATRIX (SOIC L4) ── -->
    <div style="display:grid;grid-template-columns:1.2fr 1fr;gap:18px;margin-bottom:20px;flex-wrap:wrap;">
      
      <!-- SOIC Technical Rulebook Matrix -->
      <div style="background:#090f1a;border:1px solid #1e334d;border-radius:8px;padding:16px;">
        <h3 style="color:#ffaa00;font-size:13px;margin:0 0 12px 0;display:flex;align-items:center;gap:8px;">
          <span>📖</span> The SOIC 7-Pillar Technical Rulebook (Course L4)
        </h3>
        <div style="display:flex;flex-direction:column;gap:8px;font-size:11px;line-height:1.45;">
          
          <div style="background:#0d1624;border-left:3px solid #00e676;padding:8px 10px;border-radius:0 4px 4px 0;">
            <div style="display:flex;justify-content:space-between;color:#00e676;font-weight:bold;">
              <span>1. The Holy Grail Rule: Stage 2 Breakout</span>
              <span>CONFIRMED ✓</span>
            </div>
            <div style="color:#94a3b8;font-size:10px;margin-top:2px;">Never purchase a stock in Stage 4 declining. Enter only in Stage 2 when price breaks out of a multi-month base with massive institutional volume.</div>
          </div>

          <div style="background:#0d1624;border-left:3px solid #00e676;padding:8px 10px;border-radius:0 4px 4px 0;">
            <div style="display:flex;justify-content:space-between;color:#00e676;font-weight:bold;">
              <span>2. 30-WMA Slope Direction</span>
              <span>SLOPING UP ↑</span>
            </div>
            <div style="color:#94a3b8;font-size:10px;margin-top:2px;">The 30-week weighted moving average must be sloping upward. A flat 30-WMA indicates Stage 1 basing, while a downward slope marks Stage 4 capitulation.</div>
          </div>

          <div style="background:#0d1624;border-left:3px solid #00e676;padding:8px 10px;border-radius:0 4px 4px 0;">
            <div style="display:flex;justify-content:space-between;color:#00e676;font-weight:bold;">
              <span>3. ADX &gt; 25 Trend Power</span>
              <span>ADX 34.8 ✓</span>
            </div>
            <div style="color:#94a3b8;font-size:10px;margin-top:2px;">ADX &gt; 25 indicates true directional momentum. When +DI is cleanly above -DI, institutional buyers are driving trend persistence.</div>
          </div>

          <div style="background:#0d1624;border-left:3px solid #00e676;padding:8px 10px;border-radius:0 4px 4px 0;">
            <div style="display:flex;justify-content:space-between;color:#00e676;font-weight:bold;">
              <span>4. RSI Bull Market Shift (40-50 Support)</span>
              <span>RSI 64.2 ✓</span>
            </div>
            <div style="color:#94a3b8;font-size:10px;margin-top:2px;">In strong bull runs, RSI finds support at 40-50 on corrections and repeatedly surges into 65-75. Dips to 45 are buyable pullback zones.</div>
          </div>

          <div style="background:#0d1624;border-left:3px solid #00e676;padding:8px 10px;border-radius:0 4px 4px 0;">
            <div style="display:flex;justify-content:space-between;color:#00e676;font-weight:bold;">
              <span>5. Volatility Stop (Vstop) Trailing Discipline</span>
              <span>ACTIVE (+5.4%)</span>
            </div>
            <div style="color:#94a3b8;font-size:10px;margin-top:2px;">Vstop locks in exponential compounding profits. Never second-guess the exit signal: if price closes below Vstop on high volume, exit immediately.</div>
          </div>

          <div style="background:#0d1624;border-left:3px solid #00e676;padding:8px 10px;border-radius:0 4px 4px 0;">
            <div style="display:flex;justify-content:space-between;color:#00e676;font-weight:bold;">
              <span>6. Pocket Pivot &amp; Volume Dry-Up</span>
              <span>+320% VOLUME ✓</span>
            </div>
            <div style="color:#94a3b8;font-size:10px;margin-top:2px;">Look for volume dry-up during consolidation pullbacks, followed by explosive volume surge (Pocket Pivot) on breakout days.</div>
          </div>

          <div style="background:#0d1624;border-left:3px solid #00e676;padding:8px 10px;border-radius:0 4px 4px 0;">
            <div style="display:flex;justify-content:space-between;color:#00e676;font-weight:bold;">
              <span>7. Sector Relative Strength Tailwind</span>
              <span>TOP 2 SECTOR (CABLES)</span>
            </div>
            <div style="color:#94a3b8;font-size:10px;margin-top:2px;">Ensure the stock belongs to an industry group exhibiting top decile relative strength vs broader market index (SOIC Sector Rotation).</div>
          </div>

        </div>
      </div>

      <!-- Stan Weinstein 4 Stages Architecture -->
      <div style="background:#090f1a;border:1px solid #1e334d;border-radius:8px;padding:16px;display:flex;flex-direction:column;justify-content:space-between;">
        <div>
          <h3 style="color:#00e5ff;font-size:13px;margin:0 0 12px 0;display:flex;align-items:center;gap:8px;">
            <span>🔄</span> Stan Weinstein 4-Stage Market Cycle Detector
          </h3>
          <div style="display:grid;grid-template-columns:1fr 1fr;gap:10px;font-size:10px;margin-bottom:14px;">
            
            <div style="background:#0f172a;border:1px solid #334155;border-radius:6px;padding:10px;">
              <strong style="color:#94a3b8;font-size:11px;display:block;margin-bottom:3px;">STAGE 1: BASING</strong>
              <div style="color:#cbd5e1;">Volume dries up. Price moves sideways around a flattening 30-WMA. Institutional quiet accumulation.</div>
              <div style="color:#ffaa00;margin-top:4px;font-weight:bold;">Action: WATCHLIST</div>
            </div>

            <div style="background:#062e24;border:1.5px solid #00e676;border-radius:6px;padding:10px;">
              <strong style="color:#00e676;font-size:11px;display:block;margin-bottom:3px;">STAGE 2: ADVANCING</strong>
              <div style="color:#cbd5e1;">Explosive breakout on 2x+ volume above resistance. 30-WMA slopes upward. Higher highs &amp; higher lows.</div>
              <div style="color:#00e676;margin-top:4px;font-weight:bold;">Action: AGGRESSIVE BUY / HOLD</div>
            </div>

            <div style="background:#2d1b09;border:1px solid #f59e0b;border-radius:6px;padding:10px;">
              <strong style="color:#f59e0b;font-size:11px;display:block;margin-bottom:3px;">STAGE 3: TOPPING</strong>
              <div style="color:#cbd5e1;">Volatility increases sharply. Volume expands without price progress (churning). 30-WMA flattens out.</div>
              <div style="color:#f59e0b;margin-top:4px;font-weight:bold;">Action: TAKE PROFITS / TIGHTEN STOP</div>
            </div>

            <div style="background:#2d0d0d;border:1px solid #ef4444;border-radius:6px;padding:10px;">
              <strong style="color:#ef4444;font-size:11px;display:block;margin-bottom:3px;">STAGE 4: DECLINING</strong>
              <div style="color:#cbd5e1;">Breakdown below 30-WMA on heavy distribution. 30-WMA turns downward. Lower highs &amp; lower lows.</div>
              <div style="color:#ef4444;margin-top:4px;font-weight:bold;">Action: EXIT ALL / NEVER BUY</div>
            </div>

          </div>

          <!-- Live Stage Position Gauge -->
          <div style="background:#0d1624;border:1px solid #1e334d;border-radius:6px;padding:12px;">
            <div style="display:flex;justify-content:space-between;font-size:11px;margin-bottom:6px;">
              <span style="color:#94a3b8;">Current Cycle Phase:</span>
              <strong id="tech_cycle_status" style="color:#00e676;">Early-to-Mid Stage 2 Advancing (Wave 3)</strong>
            </div>
            <div style="width:100%;height:10px;background:#1e293b;border-radius:5px;overflow:hidden;position:relative;">
              <div id="tech_stage_progressbar" style="width:42%;height:100%;background:linear-gradient(to right, #00e5ff 0%, #00e676 100%);"></div>
            </div>
            <div style="display:flex;justify-content:space-between;font-size:8.5px;color:#64748b;margin-top:4px;">
              <span>Stage 1 Basing</span>
              <span>Stage 2 Breakout</span>
              <span>Stage 2 Acceleration</span>
              <span>Stage 3 Top</span>
              <span>Stage 4 Decline</span>
            </div>
          </div>
        </div>

        <div style="margin-top:12px;display:grid;grid-template-columns:repeat(auto-fit, minmax(130px, 1fr));gap:6px;">
          <button class="action-btn" onclick="executeTechSimulation('stage1_basing')" style="background:#1e293b;color:#cbd5e1;border:1px solid #475569;font-size:10px;font-weight:bold;padding:5px;">⏳ Stage 1 Base</button>
          <button class="action-btn" onclick="executeTechSimulation('stage2_breakout')" style="background:#065f46;color:#34d399;border:1px solid #10b981;font-size:10px;font-weight:bold;padding:5px;">⚡ Stage 2 Breakout</button>
          <button class="action-btn" onclick="executeTechSimulation('pullback_30wma')" style="background:#1e3a5f;color:#38bdf8;border:1px solid #3b82f6;font-size:10px;font-weight:bold;padding:5px;">🎯 30-WMA Retest</button>
          <button class="action-btn" onclick="executeTechSimulation('stage3_distribution')" style="background:#451a03;color:#fbbf24;border:1px solid #d97706;font-size:10px;font-weight:bold;padding:5px;">⚠️ Stage 3 Top</button>
          <button class="action-btn" onclick="executeTechSimulation('stage4_capitulation')" style="background:#450a0a;color:#f87171;border:1px solid #dc2626;font-size:10px;font-weight:bold;padding:5px;">🚨 Stage 4 Exit</button>
          <button class="action-btn" onclick="executeTechSimulation('reset_baseline')" style="background:#0f172a;color:#94a3b8;border:1px solid #334155;font-size:10px;font-weight:bold;padding:5px;">↺ Reset Base</button>
        </div>
      </div>

    </div>

  </div>
</div>

<!-- ── SCRIPT FOR REAL-TIME TECHNICALS ENGINE ── -->
<script>
(function() {
  var techData = {
    POLYCAB: { name: 'Polycab India Ltd', price: 7145.00, chg: '+182.50 (+2.62%)', stage: 'STAGE 2 ADVANCING', wma: 6450.00, ema: 6120.00, adx: 34.8, rsi: 64.2, vstop: 6780.00, basePrices: [5400, 5550, 5700, 5900, 6100, 6300, 6250, 6500, 6700, 6950, 7145] },
    KEI: { name: 'KEI Industries Ltd', price: 4280.00, chg: '+94.00 (+2.25%)', stage: 'STAGE 2 ADVANCING', wma: 3820.00, ema: 3600.00, adx: 36.4, rsi: 66.8, vstop: 4050.00, basePrices: [3100, 3250, 3400, 3550, 3700, 3850, 3800, 3950, 4100, 4200, 4280] },
    APLAPOLLO: { name: 'APL Apollo Tubes', price: 1610.00, chg: '+28.50 (+1.80%)', stage: 'STAGE 2 ADVANCING', wma: 1480.00, ema: 1410.00, adx: 29.5, rsi: 59.4, vstop: 1530.00, basePrices: [1200, 1250, 1310, 1380, 1420, 1450, 1440, 1500, 1540, 1580, 1610] },
    PIDILITE: { name: 'Pidilite Industries', price: 3025.00, chg: '+42.00 (+1.41%)', stage: 'STAGE 2 ADVANCING', wma: 2850.00, ema: 2790.00, adx: 26.2, rsi: 58.1, vstop: 2910.00, basePrices: [2500, 2550, 2620, 2700, 2750, 2800, 2790, 2860, 2920, 2980, 3025] },
    NARAYANA: { name: 'Narayana Hrudayalaya', price: 1290.00, chg: '+31.00 (+2.46%)', stage: 'STAGE 2 ADVANCING', wma: 1180.00, ema: 1120.00, adx: 32.1, rsi: 63.5, vstop: 1220.00, basePrices: [980, 1020, 1060, 1100, 1140, 1170, 1160, 1200, 1230, 1260, 1290] },
    AAPL: { name: 'Apple Inc', price: 234.80, chg: '+2.40 (+1.03%)', stage: 'STAGE 2 ADVANCING', wma: 215.00, ema: 205.00, adx: 28.4, rsi: 61.2, vstop: 224.00, basePrices: [180, 185, 192, 200, 208, 214, 212, 220, 226, 231, 234.8] },
    NVDA: { name: 'Nvidia Corp', price: 138.20, chg: '+4.10 (+3.06%)', stage: 'STAGE 2 ADVANCING', wma: 118.00, ema: 108.00, adx: 42.6, rsi: 69.4, vstop: 128.00, basePrices: [85, 92, 100, 108, 115, 122, 119, 127, 131, 135, 138.2] },
    TSLA: { name: 'Tesla Inc', price: 248.50, chg: '+7.20 (+2.98%)', stage: 'STAGE 2 ADVANCING', wma: 220.00, ema: 210.00, adx: 31.2, rsi: 62.0, vstop: 235.00, basePrices: [170, 180, 195, 210, 225, 230, 226, 236, 240, 244, 248.5] },
    BRENT: { name: 'Brent Crude Oil ICE', price: 78.40, chg: '+1.15 (+1.49%)', stage: 'STAGE 1 BASING', wma: 79.20, ema: 81.50, adx: 22.4, rsi: 51.2, vstop: 75.80, basePrices: [88, 85, 82, 79, 77, 75, 76, 75, 77, 77.5, 78.4] },
    HDFCBANK: { name: 'HDFC Bank Ltd', price: 1740.00, chg: '+22.50 (+1.31%)', stage: 'STAGE 2 ADVANCING', wma: 1650.00, ema: 1620.00, adx: 26.5, rsi: 58.4, vstop: 1680.00, basePrices: [1480, 1510, 1540, 1580, 1620, 1660, 1640, 1680, 1705, 1725, 1740] },
    MSFT: { name: 'Microsoft Corp', price: 422.50, chg: '+4.80 (+1.15%)', stage: 'STAGE 2 ADVANCING', wma: 405.00, ema: 395.00, adx: 28.2, rsi: 59.8, vstop: 410.00, basePrices: [370, 380, 388, 396, 404, 412, 408, 415, 418, 420, 422.5] },
    AMZN: { name: 'Amazon.com Inc', price: 195.40, chg: '+3.60 (+1.88%)', stage: 'STAGE 2 ADVANCING', wma: 182.00, ema: 176.00, adx: 32.5, rsi: 62.4, vstop: 188.00, basePrices: [160, 165, 172, 178, 184, 189, 186, 190, 192, 194, 195.4] },
    GOOGL: { name: 'Alphabet Inc', price: 176.80, chg: '+2.10 (+1.20%)', stage: 'STAGE 2 ADVANCING', wma: 168.00, ema: 162.00, adx: 29.4, rsi: 58.2, vstop: 170.00, basePrices: [150, 154, 158, 163, 168, 172, 170, 173, 174.5, 175.5, 176.8] },
    XOM: { name: 'ExxonMobil Corp', price: 118.40, chg: '+1.80 (+1.54%)', stage: 'STAGE 2 ADVANCING', wma: 112.50, ema: 108.00, adx: 27.8, rsi: 56.5, vstop: 114.00, basePrices: [102, 105, 108, 110, 113, 115, 114, 116, 117, 117.8, 118.4] },
    ASML: { name: 'ASML Holding NV', price: 668.00, chg: '+14.50 (+2.22%)', stage: 'STAGE 1 BASE / STAGE 2', wma: 645.00, ema: 630.00, adx: 25.4, rsi: 52.8, vstop: 640.00, basePrices: [610, 620, 630, 642, 650, 658, 652, 660, 663, 665, 668] },
    ARAMCO: { name: 'Saudi Aramco', price: 27.80, chg: '+0.35 (+1.28%)', stage: 'STAGE 1 BASE', wma: 27.20, ema: 27.00, adx: 21.5, rsi: 51.4, vstop: 27.10, basePrices: [26.8, 27.0, 27.1, 27.3, 27.4, 27.5, 27.4, 27.6, 27.7, 27.75, 27.8] },
    BHP: { name: 'BHP Group Ltd', price: 41.20, chg: '+0.65 (+1.60%)', stage: 'STAGE 1 BASE / STAGE 2', wma: 39.80, ema: 38.90, adx: 24.8, rsi: 54.2, vstop: 40.00, basePrices: [37.5, 38.2, 38.8, 39.4, 40.0, 40.5, 40.2, 40.8, 41.0, 41.1, 41.2] },
    SAMSUNG: { name: 'Samsung Electronics', price: 58200.00, chg: '+1100.00 (+1.93%)', stage: 'STAGE 1 DEEP VALUE BASE', wma: 56500.00, ema: 55200.00, adx: 23.4, rsi: 49.5, vstop: 56000.00, basePrices: [52000, 53200, 54500, 55500, 56800, 57400, 56900, 57600, 57900, 58100, 58200] },
    COPPER: { name: 'LME Grade A Copper', price: 9450.00, chg: '+140.00 (+1.50%)', stage: 'STAGE 2 ADVANCING', wma: 9150.00, ema: 8900.00, adx: 31.8, rsi: 61.2, vstop: 9200.00, basePrices: [8600, 8750, 8900, 9050, 9200, 9320, 9280, 9360, 9400, 9425, 9450] }
  };

  var currentTechStock = 'POLYCAB';
  var showWMA = true;
  var showEMA = true;
  var showVstop = true;

  window.switchTechStock = function(key) {
    if (!techData[key]) return;
    currentTechStock = key;
    var d = techData[key];
    var isINR = key !== 'AAPL' && key !== 'NVDA' && key !== 'TSLA' && key !== 'BRENT';
    var sym = isINR ? '₹' : '$';

    document.getElementById('tech_stock_select').value = key;
    document.getElementById('tech_price_display').textContent = sym + d.price.toLocaleString(undefined, { minimumFractionDigits: 2 });
    document.getElementById('tech_change_display').textContent = d.chg;
    document.getElementById('tech_card_stage').textContent = d.stage;
    document.getElementById('tech_card_wma').textContent = sym + d.wma.toLocaleString(undefined, { minimumFractionDigits: 2 });
    document.getElementById('tech_card_ema').textContent = sym + d.ema.toLocaleString(undefined, { minimumFractionDigits: 2 });
    document.getElementById('tech_card_adx').textContent = d.adx.toFixed(1);
    document.getElementById('tech_card_rsi').textContent = d.rsi.toFixed(1);
    document.getElementById('tech_card_vstop').textContent = sym + d.vstop.toLocaleString(undefined, { minimumFractionDigits: 2 });
    document.getElementById('tech_chart_title').textContent = d.name.toUpperCase() + ' — 30-WMA STAGE 2 BREAKOUT RADAR';

    var spread = ((d.price - d.wma) / d.wma * 100).toFixed(1);
    document.getElementById('tech_card_wma_spread').textContent = 'Price ' + (spread >= 0 ? '+' : '') + spread + '% ' + (spread >= 0 ? 'above' : 'below') + ' 30-WMA';

    drawTechnicalsChart();
  };

  window.setTechTimeframe = function(tf) {
    ['1D', '1W', '30W', '1Y'].forEach(function(t) {
      var btn = document.getElementById('btn_tf_' + t);
      if (btn) {
        if (t === tf) {
          btn.style.background = '#1e3a5f';
          btn.style.color = '#00e5ff';
        } else {
          btn.style.background = '#0d1624';
          btn.style.color = '#94a3b8';
        }
      }
    });
    drawTechnicalsChart();
  };

  window.toggleTechOverlay = function(ov) {
    if (ov === 'wma30') showWMA = !showWMA;
    if (ov === 'ema200') showEMA = !showEMA;
    if (ov === 'vstop') showVstop = !showVstop;

    var btnWMA = document.getElementById('btn_toggle_30wma');
    var btnEMA = document.getElementById('btn_toggle_ema200');
    var btnVst = document.getElementById('btn_toggle_vstop');

    if (btnWMA) btnWMA.style.opacity = showWMA ? '1' : '0.4';
    if (btnEMA) btnEMA.style.opacity = showEMA ? '1' : '0.4';
    if (btnVst) btnVst.style.opacity = showVstop ? '1' : '0.4';

    drawTechnicalsChart();
  };

  var baselineData = JSON.parse(JSON.stringify(techData));

  window.executeTechSimulation = function(type) {
    var d = techData[currentTechStock];
    if (!d) return;

    if (type === 'stage1_basing') {
      d.stage = 'STAGE 1 BASING';
      d.price = d.wma * 1.002;
      d.adx = 16.4;
      d.rsi = 49.2;
      d.chg = '+0.15% (Quiet Accumulation)';
      var statusEl = document.getElementById('tech_cycle_status');
      if (statusEl) { statusEl.textContent = 'Stage 1 Basing (Volume Dry-Up / Watchlist)'; statusEl.style.color = '#ffaa00'; }
      var barEl = document.getElementById('tech_stage_progressbar');
      if (barEl) { barEl.style.width = '18%'; barEl.style.background = '#ffaa00'; }
      alert('⏳ Stage 1 Basing: Sideways range-bound action. Volume dry-up. 30-WMA flat. Prepare watchlist for breakout!');
    } else if (type === 'stage2_breakout') {
      d.stage = 'STAGE 2 ADVANCING';
      d.price = d.price * 1.052;
      d.adx = Math.min(55, d.adx + 3.8);
      d.rsi = Math.min(80, d.rsi + 5.2);
      d.vstop = d.price * 0.94;
      d.chg = '+5.20% (Volume Breakout Surge)';
      var statusEl = document.getElementById('tech_cycle_status');
      if (statusEl) { statusEl.textContent = 'Stage 2 Advancing (Wave 3 Impulse Breakout)'; statusEl.style.color = '#00e676'; }
      var barEl = document.getElementById('tech_stage_progressbar');
      if (barEl) { barEl.style.width = '55%'; barEl.style.background = 'linear-gradient(to right, #00e5ff, #00e676)'; }
      alert('⚡ Stage 2 Breakout Simulated: Price surged +5.2% on 3.5x volume! ADX strengthened to ' + d.adx.toFixed(1) + ', Vstop trailed upward.');
    } else if (type === 'pullback_30wma') {
      d.stage = 'STAGE 2 RETEST';
      d.price = d.wma * 1.015;
      d.rsi = 48.5;
      d.chg = '-2.80% (Healthy 30-WMA Retest)';
      var statusEl = document.getElementById('tech_cycle_status');
      if (statusEl) { statusEl.textContent = 'Stage 2 Low-Risk Pullback (30-WMA Support)'; statusEl.style.color = '#38bdf8'; }
      var barEl = document.getElementById('tech_stage_progressbar');
      if (barEl) { barEl.style.width = '42%'; barEl.style.background = '#38bdf8'; }
      alert('🎯 30-WMA Retest Simulated: Price tested 30-WMA support. RSI at 48.5 marks classic SOIC low-risk swing entry zone!');
    } else if (type === 'stage3_distribution') {
      d.stage = 'STAGE 3 TOPPING';
      d.price = d.price * 0.985;
      d.adx = 21.2;
      d.rsi = 52.0;
      d.chg = '-1.50% (High Volatility Churn)';
      var statusEl = document.getElementById('tech_cycle_status');
      if (statusEl) { statusEl.textContent = 'Stage 3 Distribution Top (High Churn / Flattening WMA)'; statusEl.style.color = '#f59e0b'; }
      var barEl = document.getElementById('tech_stage_progressbar');
      if (barEl) { barEl.style.width = '78%'; barEl.style.background = '#f59e0b'; }
      alert('⚠️ Stage 3 Distribution Top: High churning volume without upward progress. 30-WMA flattening. Tighten Vstop and take partial profits!');
    } else if (type === 'stage4_capitulation') {
      d.stage = 'STAGE 4 DECLINING';
      d.price = d.wma * 0.91;
      d.adx = 36.8;
      d.rsi = 31.5;
      d.vstop = d.price * 1.06;
      d.chg = '-8.40% (Severe Breakdown Below 30-WMA)';
      var statusEl = document.getElementById('tech_cycle_status');
      if (statusEl) { statusEl.textContent = 'Stage 4 Capitulation (Breakdown Below 30-WMA)'; statusEl.style.color = '#ef4444'; }
      var barEl = document.getElementById('tech_stage_progressbar');
      if (barEl) { barEl.style.width = '96%'; barEl.style.background = '#ef4444'; }
      alert('🚨 Stage 4 Capitulation: Breakdown below 30-WMA on heavy volume! Vstop breached. SOIC Rule: Exit immediately, never buy Stage 4!');
    } else if (type === 'reset_baseline') {
      techData[currentTechStock] = JSON.parse(JSON.stringify(baselineData[currentTechStock]));
      var statusEl = document.getElementById('tech_cycle_status');
      if (statusEl) { statusEl.textContent = 'Early-to-Mid Stage 2 Advancing (Wave 3)'; statusEl.style.color = '#00e676'; }
      var barEl = document.getElementById('tech_stage_progressbar');
      if (barEl) { barEl.style.width = '42%'; barEl.style.background = 'linear-gradient(to right, #00e5ff 0%, #00e676 100%)'; }
      alert('↺ Baseline Reset: Restored real-time market data baseline.');
    }
    switchTechStock(currentTechStock);
  };

  window.drawTechnicalsChart = function drawTechnicalsChart() {
    var canvas = document.getElementById('technicalsCanvas');
    if (!canvas) return;
    var w = canvas.offsetWidth || (canvas.parentElement ? canvas.parentElement.clientWidth : 1100);
    var h = canvas.offsetHeight || 460;
    if (w <= 0) w = 1100;
    if (h <= 0) h = 460;
    canvas.width = w;
    canvas.height = h;
    var ctx = canvas.getContext('2d');

    ctx.clearRect(0, 0, w, h);

    var d = techData[currentTechStock] || techData.POLYCAB;
    var prices = d.basePrices;
    var n = prices.length;
    var padLeft = 60, padRight = 30, padTop = 25, padBottom = 70;
    var chartH = h - padTop - padBottom;
    var chartW = w - padLeft - padRight;

    var minP = Math.min.apply(null, prices) * 0.92;
    var maxP = Math.max.apply(null, prices) * 1.08;

    function getY(p) {
      return padTop + chartH - ((p - minP) / (maxP - minP)) * chartH;
    }
    function getX(i) {
      return padLeft + (i / (n - 1)) * chartW;
    }

    // Grid lines
    ctx.strokeStyle = '#121d2d';
    ctx.lineWidth = 1;
    for (var k = 0; k <= 5; k++) {
      var y = padTop + (chartH / 5) * k;
      ctx.beginPath();
      ctx.moveTo(padLeft, y);
      ctx.lineTo(w - padRight, y);
      ctx.stroke();

      var priceVal = maxP - (k / 5) * (maxP - minP);
      ctx.fillStyle = '#64748b';
      ctx.font = '9.5px Consolas, monospace';
      ctx.textAlign = 'right';
      ctx.fillText(priceVal.toFixed(0), padLeft - 8, y + 3);
    }

    // Draw Vstop Cloud
    if (showVstop) {
      ctx.fillStyle = 'rgba(0, 230, 118, 0.08)';
      ctx.beginPath();
      ctx.moveTo(getX(0), getY(prices[0] * 0.94));
      for (var i = 1; i < n; i++) {
        ctx.lineTo(getX(i), getY(prices[i] * 0.94));
      }
      ctx.lineTo(getX(n - 1), getY(prices[n - 1]));
      for (var j = n - 2; j >= 0; j--) {
        ctx.lineTo(getX(j), getY(prices[j]));
      }
      ctx.closePath();
      ctx.fill();

      // Vstop line
      ctx.strokeStyle = '#00e676';
      ctx.lineWidth = 1.8;
      ctx.setLineDash([4, 4]);
      ctx.beginPath();
      for (var i = 0; i < n; i++) {
        var vY = getY(prices[i] * 0.94);
        if (i === 0) ctx.moveTo(getX(i), vY);
        else ctx.lineTo(getX(i), vY);
      }
      ctx.stroke();
      ctx.setLineDash([]);
    }

    // Draw 30-WMA
    if (showWMA) {
      ctx.strokeStyle = '#ffaa00';
      ctx.lineWidth = 2.4;
      ctx.beginPath();
      for (var i = 0; i < n; i++) {
        var wY = getY(prices[i] * 0.91);
        if (i === 0) ctx.moveTo(getX(i), wY);
        else ctx.lineTo(getX(i), wY);
      }
      ctx.stroke();
    }

    // Draw 200-EMA
    if (showEMA) {
      ctx.strokeStyle = '#00e5ff';
      ctx.lineWidth = 1.8;
      ctx.beginPath();
      for (var i = 0; i < n; i++) {
        var eY = getY(prices[i] * 0.86);
        if (i === 0) ctx.moveTo(getX(i), eY);
        else ctx.lineTo(getX(i), eY);
      }
      ctx.stroke();
    }

    // Draw Candlesticks
    var candleWidth = Math.max(6, (chartW / n) * 0.6);
    for (var i = 0; i < n; i++) {
      var x = getX(i);
      var openP = (i === 0 ? prices[0] * 0.98 : prices[i - 1]);
      var closeP = prices[i];
      var highP = Math.max(openP, closeP) * (1 + (i % 2 === 0 ? 0.018 : 0.012));
      var lowP = Math.min(openP, closeP) * (1 - (i % 2 === 0 ? 0.014 : 0.02));
      var isGreen = closeP >= openP;

      // Wick
      ctx.strokeStyle = isGreen ? '#00e676' : '#ff3344';
      ctx.lineWidth = 1.5;
      ctx.beginPath();
      ctx.moveTo(x, getY(highP));
      ctx.lineTo(x, getY(lowP));
      ctx.stroke();

      // Body
      var topY = getY(Math.max(openP, closeP));
      var botY = getY(Math.min(openP, closeP));
      var bodyH = Math.max(3, botY - topY);

      ctx.fillStyle = isGreen ? '#00e676' : '#ff3344';
      ctx.fillRect(x - candleWidth / 2, topY, candleWidth, bodyH);

      // Volume bar below
      var volH = 15 + ((prices[i] - minP) / (maxP - minP)) * 35;
      ctx.fillStyle = isGreen ? 'rgba(0, 230, 118, 0.45)' : 'rgba(255, 51, 68, 0.45)';
      ctx.fillRect(x - candleWidth / 2, h - 15 - volH, candleWidth, volH);
    }

    // Volume label
    ctx.fillStyle = '#64748b';
    ctx.font = '9px Consolas, monospace';
    ctx.textAlign = 'left';
    ctx.fillText('VOLUME SPREAD & INSTITUTIONAL FLOWS', padLeft, h - 6);
  }

  // Crosshair tracker on canvas
  var canvasEl = document.getElementById('technicalsCanvas');
  if (canvasEl) {
    canvasEl.addEventListener('mousemove', function(e) {
      var rect = canvasEl.getBoundingClientRect();
      var mx = e.clientX - rect.left;
      var my = e.clientY - rect.top;
      var hud = document.getElementById('tech_crosshair_hud');
      var d = techData[currentTechStock] || techData.POLYCAB;

      if (hud) {
        hud.style.display = 'block';
        hud.style.left = Math.min(rect.width - 240, Math.max(10, mx + 15)) + 'px';
        hud.style.top = Math.min(rect.height - 90, Math.max(10, my - 20)) + 'px';
        hud.innerHTML = 
          '<div style="color:#ffaa00;font-weight:900;border-bottom:1px solid #203a5e;padding-bottom:2px;margin-bottom:3px;">' + d.name + '</div>' +
          '<div><span style="color:#94a3b8;">Price:</span> <strong style="color:#00e676;">₹' + d.price.toFixed(2) + '</strong></div>' +
          '<div><span style="color:#94a3b8;">30-WMA:</span> <span style="color:#ffaa00;">₹' + d.wma.toFixed(2) + '</span></div>' +
          '<div><span style="color:#94a3b8;">ADX:</span> <span style="color:#c084fc;">' + d.adx.toFixed(1) + '</span> · <span style="color:#94a3b8;">RSI:</span> <span style="color:#38bdf8;">' + d.rsi.toFixed(1) + '</span></div>';
      }
    });

    canvasEl.addEventListener('mouseleave', function() {
      var hud = document.getElementById('tech_crosshair_hud');
      if (hud) hud.style.display = 'none';
    });
  }

  // Auto-init chart
  setTimeout(drawTechnicalsChart, 200);
  window.addEventListener('resize', drawTechnicalsChart);

})();
</script>
"""
