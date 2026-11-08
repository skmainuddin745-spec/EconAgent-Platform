# Test building the macro-micro correlation subpane markup
import json

macro_subpane_html = """
    <!-- ══════════════════════════════════════════════════════════════════════════ -->
    <!-- SUB-PANE 5: GLOBAL WALL STREET CROSS-ASSET CORRELATION & SENSITIVITY     -->
    <!-- ══════════════════════════════════════════════════════════════════════════ -->
    <div id="titan_subpane_macro" style="display:none;">
      
      <!-- Top Overview Banner -->
      <div style="background:var(--bg3);border:1px solid var(--border);border-radius:10px;padding:20px;margin-bottom:20px;">
        <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:16px;flex-wrap:wrap;gap:12px;">
          <div>
            <div style="font-size:11px;font-family:var(--font-mono);color:var(--bb-amber);font-weight:800;letter-spacing:1px;">WALL STREET &amp; DALAL STREET MACRO TRANSMISSION ENGINE</div>
            <div style="font-size:18px;font-weight:900;color:#fff;margin-top:2px;">🌐 Real-Time Cross-Asset Macro-Micro Correlation &amp; Sensitivity Matrix</div>
          </div>
          <div style="background:#090e17;border:1px solid #1e293b;border-radius:6px;padding:6px 14px;font-size:11px;font-family:var(--font-mono);color:#94a3b8;">
            Transmission Architecture: <span style="color:#00e5ff;font-weight:700;">Macro Rates/Commodities ➔ Corporate Financial Statements</span>
          </div>
        </div>

        <!-- 6 Live Benchmark Cards -->
        <div style="display:grid;grid-template-columns:repeat(auto-fit, minmax(210px, 1fr));gap:12px;margin-bottom:20px;">
          
          <div style="background:#090e17;border:1px solid #1e293b;border-radius:8px;padding:12px 14px;">
            <div style="font-size:10px;color:#94a3b8;font-family:var(--font-mono);display:flex;justify-content:space-between;">
              <span>LME COPPER (GRADE A)</span>
              <span style="color:#00e676;">+1.50%</span>
            </div>
            <div style="font-size:20px;font-weight:900;color:var(--bb-amber);margin:4px 0;" class="tabular-nums" id="macro_bench_copper">$9,450 / MT</div>
            <div style="font-size:10px;color:#64748b;">Direct COGS impact: <strong>Polycab (68%), KEI (65%)</strong></div>
          </div>

          <div style="background:#090e17;border:1px solid #1e293b;border-radius:8px;padding:12px 14px;">
            <div style="font-size:10px;color:#94a3b8;font-family:var(--font-mono);display:flex;justify-content:space-between;">
              <span>BRENT CRUDE OIL ICE</span>
              <span style="color:#00e676;">+1.49%</span>
            </div>
            <div style="font-size:20px;font-weight:900;color:#38bdf8;margin:4px 0;" class="tabular-nums" id="macro_bench_brent">$78.40 / bbl</div>
            <div style="font-size:10px;color:#64748b;">Aramco/Exxon Cash Flow ➔ <strong>Pidilite VAM Input</strong></div>
          </div>

          <div style="background:#090e17;border:1px solid #1e293b;border-radius:8px;padding:12px 14px;">
            <div style="font-size:10px;color:#94a3b8;font-family:var(--font-mono);display:flex;justify-content:space-between;">
              <span>DOMESTIC HRC STEEL</span>
              <span style="color:#00e676;">+1.20%</span>
            </div>
            <div style="font-size:20px;font-weight:900;color:#f59e0b;margin:4px 0;" class="tabular-nums" id="macro_bench_steel">₹54,500 / MT ($680)</div>
            <div style="font-size:10px;color:#64748b;">APL Apollo ERW spread: <strong>₹4,850/MT EBITDA</strong></div>
          </div>

          <div style="background:#090e17;border:1px solid #1e293b;border-radius:8px;padding:12px 14px;">
            <div style="font-size:10px;color:#94a3b8;font-family:var(--font-mono);display:flex;justify-content:space-between;">
              <span>US 10-YEAR BENCHMARK</span>
              <span style="color:#00e676;">-4 bps</span>
            </div>
            <div style="font-size:20px;font-weight:900;color:#a855f7;margin:4px 0;" class="tabular-nums" id="macro_bench_us10y">4.28% Yield</div>
            <div style="font-size:10px;color:#64748b;">Discount rate benchmark for <strong>Nasdaq 100 Multiples</strong></div>
          </div>

          <div style="background:#090e17;border:1px solid #1e293b;border-radius:8px;padding:12px 14px;">
            <div style="font-size:10px;color:#94a3b8;font-family:var(--font-mono);display:flex;justify-content:space-between;">
              <span>INDIA 10Y G-SEC YIELD</span>
              <span style="color:#00e676;">-2 bps</span>
            </div>
            <div style="font-size:20px;font-weight:900;color:#00e676;margin:4px 0;" class="tabular-nums" id="macro_bench_in10y">7.18% Yield</div>
            <div style="font-size:10px;color:#64748b;">Dalal Street Risk-Free Rate (CRP: <strong>2.38% Baa3</strong>)</div>
          </div>

          <div style="background:#090e17;border:1px solid #1e293b;border-radius:8px;padding:12px 14px;">
            <div style="font-size:10px;color:#94a3b8;font-family:var(--font-mono);display:flex;justify-content:space-between;">
              <span>USD / INR FX RATE</span>
              <span style="color:#f43f5e;">+0.05%</span>
            </div>
            <div style="font-size:20px;font-weight:900;color:#fb7185;margin:4px 0;" class="tabular-nums" id="macro_bench_usdinr">₹84.38 / USD</div>
            <div style="font-size:10px;color:#64748b;">Export tailwind: <strong>IT, Pharma &amp; Cable Exports</strong></div>
          </div>

        </div>

        <!-- ── REAL-TIME STRESS-TESTING INTERACTIVE SLIDERS ── -->
        <div style="background:#090e17;border:1px solid #203a5e;border-radius:8px;padding:18px;margin-bottom:20px;">
          <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:14px;flex-wrap:wrap;gap:10px;">
            <div style="font-weight:800;font-size:13px;color:#00e5ff;font-family:var(--font-mono);">
              ⚡ INTERACTIVE CROSS-ASSET MACRO SHOCK SIMULATOR (DRAG SLIDERS TO TRANSMIT TO CORPORATE BALANCE SHEETS)
            </div>
            <button onclick="resetMacroSliders()" style="background:#132032;color:#94a3b8;border:1px solid #1c2e44;padding:3px 10px;font-size:10px;font-weight:700;border-radius:3px;cursor:pointer;">Reset to Defaults</button>
          </div>

          <div style="display:grid;grid-template-columns:1fr 1fr;gap:20px;">
            <div>
              <div style="display:flex;justify-content:space-between;font-size:11px;font-family:var(--font-mono);margin-bottom:4px;">
                <span style="color:#94a3b8;">LME Copper Price Shock:</span>
                <strong id="lbl_slider_copper" style="color:var(--bb-amber);">0.0% ($9,450 / MT)</strong>
              </div>
              <input type="range" id="slider_copper" min="-25" max="25" step="1" value="0" oninput="runMacroTransmissionSim()" style="width:100%;accent-color:var(--bb-amber);cursor:pointer;">
              <div style="display:flex;justify-content:space-between;font-size:9px;color:#64748b;font-family:var(--font-mono);">
                <span>-25% ($7,087)</span>
                <span>Baseline ($9,450)</span>
                <span>+25% ($11,812)</span>
              </div>
            </div>

            <div>
              <div style="display:flex;justify-content:space-between;font-size:11px;font-family:var(--font-mono);margin-bottom:4px;">
                <span style="color:#94a3b8;">Brent Crude Oil Shock:</span>
                <strong id="lbl_slider_brent" style="color:#38bdf8;">$78.40 / bbl</strong>
              </div>
              <input type="range" id="slider_brent" min="50" max="120" step="1" value="78" oninput="runMacroTransmissionSim()" style="width:100%;accent-color:#38bdf8;cursor:pointer;">
              <div style="display:flex;justify-content:space-between;font-size:9px;color:#64748b;font-family:var(--font-mono);">
                <span>$50 (Bear Demand)</span>
                <span>$78.40 (Current)</span>
                <span>$120 (Geopolitical Spike)</span>
              </div>
            </div>

            <div>
              <div style="display:flex;justify-content:space-between;font-size:11px;font-family:var(--font-mono);margin-bottom:4px;">
                <span style="color:#94a3b8;">US 10-Year Treasury Yield Shock:</span>
                <strong id="lbl_slider_us10y" style="color:#a855f7;">4.28%</strong>
              </div>
              <input type="range" id="slider_us10y" min="300" max="600" step="5" value="428" oninput="runMacroTransmissionSim()" style="width:100%;accent-color:#a855f7;cursor:pointer;">
              <div style="display:flex;justify-content:space-between;font-size:9px;color:#64748b;font-family:var(--font-mono);">
                <span>3.00% (Aggressive Fed Cuts)</span>
                <span>4.28% (Baseline)</span>
                <span>6.00% (Inflationary Spike)</span>
              </div>
            </div>

            <div>
              <div style="display:flex;justify-content:space-between;font-size:11px;font-family:var(--font-mono);margin-bottom:4px;">
                <span style="color:#94a3b8;">USD / INR FX Rate Shock:</span>
                <strong id="lbl_slider_usdinr" style="color:#00e676;">₹84.38</strong>
              </div>
              <input type="range" id="slider_usdinr" min="8000" max="9000" step="25" value="8438" oninput="runMacroTransmissionSim()" style="width:100%;accent-color:#00e676;cursor:pointer;">
              <div style="display:flex;justify-content:space-between;font-size:9px;color:#64748b;font-family:var(--font-mono);">
                <span>₹80.00 (INR Appreciation)</span>
                <span>₹84.38 (Current)</span>
                <span>₹90.00 (Emerging Market Depreciation)</span>
              </div>
            </div>
          </div>
        </div>

        <!-- ── TRANSMISSION MATRIX RESULTS TABLE ── -->
        <div style="background:#090e17;border:1px solid #1e293b;border-radius:8px;padding:16px;overflow-x:auto;">
          <div style="font-weight:800;font-size:12px;color:#fff;margin-bottom:12px;font-family:var(--font-mono);display:flex;justify-content:space-between;align-items:center;">
            <span>📊 TRANSMISSION SENSITIVITY OUTPUT: LIVE IMPACT ACROSS CORPORATE BALANCE SHEETS</span>
            <span style="color:#94a3b8;font-size:10px;">Calculated Dynamically via Monte Carlo Sensitivity Matrix</span>
          </div>
          <table style="width:100%;border-collapse:collapse;font-size:11px;font-family:var(--font-mono);text-align:left;">
            <thead>
              <tr style="border-bottom:1px solid #233448;color:#94a3b8;font-size:10px;">
                <th style="padding:8px 6px;">COMPANY / TICKER</th>
                <th style="padding:8px 6px;">SECTOR / ECONOMY</th>
                <th style="padding:8px 6px;">PRIMARY TRANSMISSION CHOP</th>
                <th style="padding:8px 6px;">EBITDA IMPACT</th>
                <th style="padding:8px 6px;">WORKING CAPITAL DELTA</th>
                <th style="padding:8px 6px;">WACC / MULTIPLE SHIFT</th>
                <th style="padding:8px 6px;text-align:right;">INTRINSIC DCF VALUE</th>
              </tr>
            </thead>
            <tbody id="macro_trans_tbody">
              <!-- Dynamically populated by runMacroTransmissionSim() -->
            </tbody>
          </table>
        </div>

      </div>

    </div>
"""
print("Markup length:", len(macro_subpane_html))

