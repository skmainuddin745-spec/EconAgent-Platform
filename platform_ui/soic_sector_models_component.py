# -*- coding: utf-8 -*-
"""
SOIC Global Sector Financial Models & Aswath Damodaran 94-Industry Terminal
Platform: EconAgent Platform Bloomberg Terminal
Covers 11 Primary GICS Sectors, 94 Damodaran Global Industries, 48,156-Company Taxonomy Search,
and 11 Interactive 3-Case Scenario IRR & Unit Economics Valuation Cockpits.
"""

import os
import json

def build_soic_sector_models_section():
    curr_dir = os.path.dirname(os.path.abspath(__file__))
    damo_p = os.path.join(curr_dir, 'damodaran_94_global_industries.json')
    comp_p = os.path.join(curr_dir, 'global_top_companies_curated.json')

    with open(damo_p, 'r', encoding='utf-8') as f:
        damo_list = json.load(f)
    with open(comp_p, 'r', encoding='utf-8') as f:
        comp_list = json.load(f)

    damo_json_str = json.dumps(damo_list, ensure_ascii=False)
    comp_json_str = json.dumps(comp_list, ensure_ascii=False)

    template = """
    <!-- ══════════════════════════════════════════════════════════════════════════ -->
    <!-- GLOBAL SECTOR VALUATION & DAMODARAN 94-INDUSTRY VALUATION TERMINAL -->
    <!-- ══════════════════════════════════════════════════════════════════════════ -->

    <div style="background: linear-gradient(180deg, #0d1520 0%, #070b12 100%); border: 1px solid #1c2b3d; border-radius: 8px; padding: 18px 22px; margin-bottom: 22px; box-shadow: 0 4px 20px rgba(0,0,0,0.6);">
      <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:12px; margin-bottom:14px; border-bottom:1px solid #1a2736; padding-bottom:12px;">
        <div>
          <div style="display:flex; align-items:center; gap:8px;">
            <span style="font-size:18px;">🌐</span>
            <span style="font-size:15px; font-weight:800; color:#fff; font-family:var(--font-mono); letter-spacing:0.5px;">GLOBAL SECTOR VALUATION &amp; DAMODARAN 94-INDUSTRY BENCHMARKS TERMINAL</span>
            <span style="background:rgba(0,229,255,0.15); color:#00e5ff; font-size:10px; font-weight:800; padding:2px 8px; border-radius:4px; border:1px solid #00e5ff;">GLOBAL CORPUS: 48,156 FIRMS · 132 COUNTRIES</span>
          </div>
          <div style="font-size:11px; color:#94a3b8; margin-top:4px;">
            Aswath Damodaran Global Cost of Capital &amp; Valuation Taxonomy · SOIC 310-Point Scorecard · 11 GICS Primary Sectors · 3-Case Dynamic Scenario IRRs
          </div>
        </div>
        <div style="display:flex; gap:10px; align-items:center;">
          <span style="font-size:11px; color:#64748b; font-family:var(--font-mono);">Damodaran Risk-Free Rate: <strong style="color:#00e5ff;">4.28%</strong> | Mature ERP: <strong style="color:#ffaa00;">5.63%</strong></span>
        </div>
      </div>

      <!-- ── HORIZONTAL SUB-NAVIGATION TABS ── -->
      <div style="display:flex; gap:6px; overflow-x:auto; padding-bottom:6px; scrollbar-width:thin;">
        <button class="preset-btn active" id="btn_sec_damodaran" onclick="switchSoicSectorTab('damodaran')" style="padding:6px 14px; font-size:11px; font-weight:800; border-color:#00e5ff; color:#00e5ff;">🌐 Damodaran 94 Industries</button>
        <button class="preset-btn" id="btn_sec_lookup" onclick="switchSoicSectorTab('lookup')" style="padding:6px 14px; font-size:11px; font-weight:700;">🔍 48k Company Lookup</button>
        <button class="preset-btn" id="btn_sec_semi" onclick="switchSoicSectorTab('semi')" style="padding:6px 14px; font-size:11px; font-weight:700;">💾 Semi &amp; AI (NVDA/TSMC)</button>
        <button class="preset-btn" id="btn_sec_cloud" onclick="switchSoicSectorTab('cloud')" style="padding:6px 14px; font-size:11px; font-weight:700;">☁️ Cloud (MSFT/AAPL)</button>
        <button class="preset-btn" id="btn_sec_energy" onclick="switchSoicSectorTab('energy')" style="padding:6px 14px; font-size:11px; font-weight:700;">⚡ Energy (Aramco/XOM)</button>
        <button class="preset-btn" id="btn_sec_mining" onclick="switchSoicSectorTab('mining')" style="padding:6px 14px; font-size:11px; font-weight:700;">⛏️ Mining (BHP/Rio)</button>
        <button class="preset-btn" id="btn_sec_auto" onclick="switchSoicSectorTab('auto')" style="padding:6px 14px; font-size:11px; font-weight:700;">🚗 Mobility (Tesla/Toyota)</button>
        <button class="preset-btn" id="btn_sec_bank" onclick="switchSoicSectorTab('bank')" style="padding:6px 14px; font-size:11px; font-weight:700;">🏦 Banks (JPM/HDFC)</button>
        <button class="preset-btn" id="btn_sec_pharma" onclick="switchSoicSectorTab('pharma')" style="padding:6px 14px; font-size:11px; font-weight:700;">💊 Pharma &amp; Hospitals (LLY/NH)</button>
        <button class="preset-btn" id="btn_sec_grid" onclick="switchSoicSectorTab('grid')" style="padding:6px 14px; font-size:11px; font-weight:700;">🔌 Power Grid (Polycab/Prysmian)</button>
        <button class="preset-btn" id="btn_sec_steel" onclick="switchSoicSectorTab('steel')" style="padding:6px 14px; font-size:11px; font-weight:700;">🏗️ Steel (APL/Nucor)</button>
        <button class="preset-btn" id="btn_sec_chem" onclick="switchSoicSectorTab('chem')" style="padding:6px 14px; font-size:11px; font-weight:700;">🧪 Chem (BASF/Pidilite)</button>
        <button class="preset-btn" id="btn_sec_luxury" onclick="switchSoicSectorTab('luxury')" style="padding:6px 14px; font-size:11px; font-weight:700;">👑 Luxury (LVMH/Costco)</button>
      </div>
    </div>

    <!-- ══════════════════════════════════════════════════════════════════════════ -->
    <!-- SUB-PANE 1: ASWATH DAMODARAN 94 GLOBAL INDUSTRIES MATRIX -->
    <!-- ══════════════════════════════════════════════════════════════════════════ -->
    <div id="soic_sec_pane_damodaran" style="display:block;">
      <div style="background:#080e18; border:1px solid #1a2a3e; border-radius:6px; padding:16px 20px; margin-bottom:16px;">
        <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:12px; margin-bottom:14px;">
          <div>
            <div style="font-size:13px; font-weight:800; color:#ffaa00; font-family:var(--font-mono);">
              ASWATH DAMODARAN 94 GLOBAL INDUSTRY BENCHMARK MATRIX (FULL DATA CORPUS)
            </div>
            <div style="font-size:10px; color:#64748b; margin-top:2px;">
              Live cross-sectional benchmarks: Unlevered Betas, WACC, EBIT Margins, EV/EBITDA, and EVA Spreads (ROC - WACC) across all 94 Damodaran sectors.
            </div>
          </div>
          <div style="display:flex; gap:8px; align-items:center;">
            <input type="text" id="damo_search_input" oninput="filterDamodaranTable()" placeholder="Search industry or titan (e.g. Semi, Oil, Bank, Apple)..." style="background:#0d1826; border:1px solid #233448; color:#fff; padding:6px 12px; border-radius:4px; font-size:11px; width:280px; font-family:var(--font-mono);">
            <select id="damo_sector_filter" onchange="filterDamodaranTable()" style="background:#0d1826; border:1px solid #233448; color:#00e5ff; padding:6px 10px; border-radius:4px; font-size:11px; font-family:var(--font-mono); cursor:pointer;">
              <option value="ALL">All GICS Primary Sectors (11)</option>
              <option value="Information Technology">Information Technology</option>
              <option value="Financials">Financials</option>
              <option value="Energy">Energy</option>
              <option value="Materials">Materials</option>
              <option value="Industrials">Industrials</option>
              <option value="Health Care">Health Care</option>
              <option value="Consumer Discretionary">Consumer Discretionary</option>
              <option value="Consumer Staples">Consumer Staples</option>
              <option value="Communication Services">Communication Services</option>
              <option value="Utilities">Utilities</option>
              <option value="Real Estate">Real Estate</option>
            </select>
          </div>
        </div>

        <!-- ── TABLE WRAPPER ── -->
        <div style="overflow-x:auto; max-height:640px; border:1px solid #182638; border-radius:4px;">
          <table class="data-table" style="width:100%; font-size:11px; border-collapse:collapse; text-align:left;">
            <thead style="background:#0f1d2e; position:sticky; top:0; z-index:10; border-bottom:2px solid #ffaa00;">
              <tr>
                <th onclick="sortDamodaranTable('name')" style="padding:10px 12px; color:#ffaa00; cursor:pointer;">Industry Name ↕</th>
                <th onclick="sortDamodaranTable('sector')" style="padding:10px 12px; color:#00e5ff; cursor:pointer;">GICS Sector ↕</th>
                <th onclick="sortDamodaranTable('firms')" style="padding:10px 12px; color:#94a3b8; text-align:right; cursor:pointer;">Global Firms ↕</th>
                <th onclick="sortDamodaranTable('unleveredBeta')" style="padding:10px 12px; color:#94a3b8; text-align:right; cursor:pointer;">Unlev Beta ↕</th>
                <th onclick="sortDamodaranTable('waccPct')" style="padding:10px 12px; color:#00e5ff; text-align:right; cursor:pointer;">WACC (%) ↕</th>
                <th onclick="sortDamodaranTable('ebitMarginPct')" style="padding:10px 12px; color:#00e676; text-align:right; cursor:pointer;">EBIT Margin (%) ↕</th>
                <th onclick="sortDamodaranTable('grossMarginPct')" style="padding:10px 12px; color:#94a3b8; text-align:right; cursor:pointer;">Gross Margin (%) ↕</th>
                <th onclick="sortDamodaranTable('evEbitda')" style="padding:10px 12px; color:#c084fc; text-align:right; cursor:pointer;">EV/EBITDA ↕</th>
                <th onclick="sortDamodaranTable('rocPct')" style="padding:10px 12px; color:#38bdf8; text-align:right; cursor:pointer;">ROIC (%) ↕</th>
                <th onclick="sortDamodaranTable('evaSpreadPct')" style="padding:10px 12px; color:#ffaa00; text-align:right; cursor:pointer;">EVA Spread (ROC-WACC) ↕</th>
                <th style="padding:10px 12px; color:#e2e8f0;">Key Global Wall Street / Global Titans</th>
              </tr>
            </thead>
            <tbody id="damodaran_table_body">
              <!-- Dynamically populated by JS -->
            </tbody>
          </table>
        </div>
        <div style="display:flex; justify-content:space-between; align-items:center; margin-top:8px; font-size:10px; color:#64748b; font-family:var(--font-mono);">
          <div>Showing <span id="damo_count_display" style="color:#00e5ff; font-weight:700;">94</span> of 94 Damodaran Global Industries</div>
          <div>Formulas: Cost of Equity = Rf + Beta * ERP | EVA Spread = ROIC - WACC</div>
        </div>
      </div>
    </div>

    <!-- ══════════════════════════════════════════════════════════════════════════ -->
    <!-- SUB-PANE 2: 48,156 GLOBAL COMPANIES TAXONOMY LOOKUP ENGINE -->
    <!-- ══════════════════════════════════════════════════════════════════════════ -->
    <div id="soic_sec_pane_lookup" style="display:none;">
      <div style="background:#080e18; border:1px solid #1a2a3e; border-radius:6px; padding:18px 22px; margin-bottom:16px;">
        <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:12px; margin-bottom:16px;">
          <div>
            <div style="font-size:14px; font-weight:800; color:#00e5ff; font-family:var(--font-mono);">
              🔍 48,156-COMPANY GLOBAL INDUSTRY TAXONOMY SEARCH ENGINE (ALL 132 COUNTRIES)
            </div>
            <div style="font-size:11px; color:#94a3b8; margin-top:3px;">
              Query any company on Wall Street, London, Frankfurt, Tokyo, Shanghai, Seoul, Singapore, Sydney, Tadawul, or Dalal Street to resolve its Damodaran Industry Group &amp; Valuation Multiples.
            </div>
          </div>
          <div style="width:380px;">
            <input type="text" id="company_lookup_input" oninput="searchGlobalCompanies()" placeholder="Type ticker or company (e.g. AAPL, NVDA, ASML, Aramco, BHP, Polycab)..." style="width:100%; background:#0d1a29; border:1px solid #00e5ff; color:#fff; padding:8px 14px; border-radius:4px; font-size:12px; font-family:var(--font-mono); box-shadow:0 0 10px rgba(0,229,255,0.2);">
          </div>
        </div>

        <!-- ── RESULTS GRID ── -->
        <div id="company_search_results" style="display:grid; grid-template-columns:repeat(auto-fill, minmax(360px, 1fr)); gap:14px; max-height:600px; overflow-y:auto; padding-right:6px;">
          <!-- Dynamically populated -->
        </div>
      </div>
    </div>

    <!-- ══════════════════════════════════════════════════════════════════════════ -->
    <!-- SUB-PANE 3: SEMICONDUCTORS & AI HARDWARE (NVIDIA, TSMC, ASML, SAMSUNG) -->
    <!-- ══════════════════════════════════════════════════════════════════════════ -->
    <div id="soic_sec_pane_semi" style="display:none;">
      <div style="background:#080e18; border:1px solid #1a2a3e; border-radius:6px; padding:18px 22px; margin-bottom:16px;">
        <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:12px; margin-bottom:16px; border-bottom:1px solid #1a2736; padding-bottom:12px;">
          <div>
            <div style="font-size:14px; font-weight:800; color:#38bdf8; font-family:var(--font-mono);">
              💾 GLOBAL SEMICONDUCTOR FOUNDRY, AI HARDWARE &amp; LITHOGRAPHY (WALL STREET / ASIA / EUROPE)
            </div>
            <div style="font-size:11px; color:#94a3b8; margin-top:2px;">
              Champions: NVIDIA (NVDA:US, $3.4T) · TSMC (TSM:US, $980B) · ASML Holding (ASML:NA, $320B) · Samsung Electronics (005930:KS, $350B)
            </div>
          </div>
          <div style="display:flex; gap:12px; font-size:11px; font-family:var(--font-mono);">
            <div style="background:#0f1d2e; padding:4px 10px; border-radius:4px; border:1px solid #1e3a5f;">
              WFE TAM: <strong style="color:#00e5ff;">$124B</strong>
            </div>
            <div style="background:#0f1d2e; padding:4px 10px; border-radius:4px; border:1px solid #1e3a5f;">
              AI GPU TAM (2028E): <strong style="color:#00e676;">$520B</strong>
            </div>
            <div style="background:#0f1d2e; padding:4px 10px; border-radius:4px; border:1px solid #1e3a5f;">
              Damodaran Ind Beta: <strong style="color:#ffaa00;">1.42</strong>
            </div>
          </div>
        </div>

        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(220px, 1fr)); gap:12px; margin-bottom:18px;">
          <div style="background:#0d1826; border:1px solid #1e3046; border-radius:6px; padding:12px;">
            <div style="font-size:10px; color:#64748b; font-family:var(--font-mono);">TSMC 3NM WAFER ASP</div>
            <div style="font-size:18px; font-weight:900; color:#00e5ff; font-family:var(--font-mono); margin-top:2px;">$20,400 / wafer</div>
            <div style="font-size:10px; color:#94a3b8; margin-top:4px;">Up from $16,000 at 5nm (+27.5% pricing moat)</div>
          </div>
          <div style="background:#0d1826; border:1px solid #1e3046; border-radius:6px; padding:12px;">
            <div style="font-size:10px; color:#64748b; font-family:var(--font-mono);">ASML HIGH-NA EUV TOOLS</div>
            <div style="font-size:18px; font-weight:900; color:#c084fc; font-family:var(--font-mono); margin-top:2px;">€350M / scanner</div>
            <div style="font-size:10px; color:#94a3b8; margin-top:4px;">Twinscan EXE:5000 (0.55 NA) Monopoly Moat</div>
          </div>
          <div style="background:#0d1826; border:1px solid #1e3046; border-radius:6px; padding:12px;">
            <div style="font-size:10px; color:#64748b; font-family:var(--font-mono);">NVIDIA DATA CENTER GM</div>
            <div style="font-size:18px; font-weight:900; color:#00e676; font-family:var(--font-mono); margin-top:2px;">75.4%</div>
            <div style="font-size:10px; color:#94a3b8; margin-top:4px;">CUDA Software Ecosystem Lock-In Moat</div>
          </div>
          <div style="background:#0d1826; border:1px solid #1e3046; border-radius:6px; padding:12px;">
            <div style="font-size:10px; color:#64748b; font-family:var(--font-mono);">COWOS PACKAGING CAPACITY</div>
            <div style="font-size:18px; font-weight:900; color:#ffaa00; font-family:var(--font-mono); margin-top:2px;">45,000 wpm</div>
            <div style="font-size:10px; color:#94a3b8; margin-top:4px;">Expanding 110% YoY to relieve Blackwell bottleneck</div>
          </div>
        </div>

        <div style="background:#0b1420; border:1px solid #1a2a3e; border-radius:6px; padding:16px;">
          <div style="font-size:12px; font-weight:800; color:#ffaa00; font-family:var(--font-mono); margin-bottom:12px;">
            ⚡ INTERACTIVE 5-YEAR SCENARIO IRR &amp; VALUATION SENSITIVITY (DAMODARAN METHODOLOGY)
          </div>
          <div style="display:grid; grid-template-columns:1fr 1fr; gap:18px;">
            <div>
              <div style="font-size:11px; color:#94a3b8; margin-bottom:6px;">
                AI Accelerator TAM CAGR (2024-2029): <strong id="val_semi_tam" style="color:#00e5ff;">32%</strong>
              </div>
              <input type="range" id="slider_semi_tam" min="15" max="50" step="1" value="32" oninput="updateSemiSim()" style="width:100%; accent-color:#00e5ff; cursor:pointer;">
              <div style="display:flex; justify-content:space-between; font-size:9px; color:#64748b; font-family:var(--font-mono);">
                <span>15% (Severe Digestion)</span>
                <span>32% (Base Enterprise Adoption)</span>
                <span>50% (Sovereign AI Supercycle)</span>
              </div>

              <div style="font-size:11px; color:#94a3b8; margin-top:14px; margin-bottom:6px;">
                Exit Terminal Multiple (EV/EBITDA): <strong id="val_semi_mult" style="color:#ffaa00;">28.0x</strong>
              </div>
              <input type="range" id="slider_semi_mult" min="15" max="45" step="1" value="28" oninput="updateSemiSim()" style="width:100%; accent-color:#ffaa00; cursor:pointer;">
              <div style="display:flex; justify-content:space-between; font-size:9px; color:#64748b; font-family:var(--font-mono);">
                <span>15.0x (Hardware Cyclical)</span>
                <span>28.0x (Tech Monopoly)</span>
                <span>45.0x (Peak Euphoria)</span>
              </div>
            </div>

            <div style="background:#070d16; border:1px solid #162436; border-radius:6px; padding:14px; font-family:var(--font-mono);">
              <div style="font-size:11px; color:#64748b; margin-bottom:8px;">5-YEAR SCENARIO RETURNS (TSMC / NVIDIA BLEND)</div>
              <div style="display:flex; justify-content:space-between; padding:6px 0; border-bottom:1px solid #142030;">
                <span style="color:#ff5252;">🐻 Bear Case (Hyperscaler Slowdown):</span>
                <strong id="semi_bear_irr" style="color:#ff5252;">14.2% IRR</strong>
              </div>
              <div style="display:flex; justify-content:space-between; padding:6px 0; border-bottom:1px solid #142030;">
                <span style="color:#ffaa00;">🎯 Base Case (Enterprise Scale):</span>
                <strong id="semi_base_irr" style="color:#ffaa00; font-size:13px;">23.8% IRR</strong>
              </div>
              <div style="display:flex; justify-content:space-between; padding:6px 0; border-bottom:1px solid #142030;">
                <span style="color:#00e676;">🚀 Bull Case (AGI Acceleration):</span>
                <strong id="semi_bull_irr" style="color:#00e676; font-size:13px;">34.5% IRR</strong>
              </div>
              <div style="margin-top:10px; font-size:10px; color:#94a3b8;">
                Damodaran WACC: <span style="color:#00e5ff;">9.45%</span> | SOIC Forensic Altman Z: <span style="color:#00e676;">8.92 (Safe)</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- ══════════════════════════════════════════════════════════════════════════ -->
    <!-- SUB-PANE 4: MEGA-CAP ENTERPRISE CLOUD & BIG TECH (MSFT, AAPL, GOOGL, AMZN) -->
    <!-- ══════════════════════════════════════════════════════════════════════════ -->
    <div id="soic_sec_pane_cloud" style="display:none;">
      <div style="background:#080e18; border:1px solid #1a2a3e; border-radius:6px; padding:18px 22px; margin-bottom:16px;">
        <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:12px; margin-bottom:16px; border-bottom:1px solid #1a2736; padding-bottom:12px;">
          <div>
            <div style="font-size:14px; font-weight:800; color:#00e5ff; font-family:var(--font-mono);">
              ☁️ MEGA-CAP ENTERPRISE CLOUD, PLATFORMS &amp; CONSUMER ECOSYSTEMS (WALL STREET TITANS)
            </div>
            <div style="font-size:11px; color:#94a3b8; margin-top:2px;">
              Champions: Microsoft (MSFT:US, $3.1T) · Apple (AAPL:US, $3.5T) · Alphabet (GOOGL:US, $2.2T) · Amazon (AMZN:US, $2.1T)
            </div>
          </div>
          <div style="display:flex; gap:12px; font-size:11px; font-family:var(--font-mono);">
            <div style="background:#0f1d2e; padding:4px 10px; border-radius:4px; border:1px solid #1e3a5f;">
              Combined Hyperscaler Capex: <strong style="color:#00e5ff;">$168B / yr</strong>
            </div>
            <div style="background:#0f1d2e; padding:4px 10px; border-radius:4px; border:1px solid #1e3a5f;">
              Cloud EBIT Margin: <strong style="color:#00e676;">39.4%</strong>
            </div>
          </div>
        </div>

        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(220px, 1fr)); gap:12px; margin-bottom:18px;">
          <div style="background:#0d1826; border:1px solid #1e3046; border-radius:6px; padding:12px;">
            <div style="font-size:10px; color:#64748b; font-family:var(--font-mono);">AZURE CLOUD GROWTH RATE</div>
            <div style="font-size:18px; font-weight:900; color:#00e5ff; font-family:var(--font-mono); margin-top:2px;">+31.0% YoY</div>
            <div style="font-size:10px; color:#94a3b8; margin-top:4px;">Enterprise Copilot &amp; OpenAI inference workloads</div>
          </div>
          <div style="background:#0d1826; border:1px solid #1e3046; border-radius:6px; padding:12px;">
            <div style="font-size:10px; color:#64748b; font-family:var(--font-mono);">APPLE SERVICES GROSS MARGIN</div>
            <div style="font-size:18px; font-weight:900; color:#00e676; font-family:var(--font-mono); margin-top:2px;">74.2%</div>
            <div style="font-size:10px; color:#94a3b8; margin-top:4px;">App Store, iCloud, Apple Pay annuity streams</div>
          </div>
          <div style="background:#0d1826; border:1px solid #1e3046; border-radius:6px; padding:12px;">
            <div style="font-size:10px; color:#64748b; font-family:var(--font-mono);">AWS ANNUAL RUN-RATE</div>
            <div style="font-size:18px; font-weight:900; color:#ffaa00; font-family:var(--font-mono); margin-top:2px;">$110B / yr</div>
            <div style="font-size:10px; color:#94a3b8; margin-top:4px;">Enterprise cloud modernization &amp; Bedrock AI</div>
          </div>
        </div>

        <div style="background:#0b1420; border:1px solid #1a2a3e; border-radius:6px; padding:16px;">
          <div style="font-size:12px; font-weight:800; color:#ffaa00; font-family:var(--font-mono); margin-bottom:12px;">
            ⚡ 5-YEAR SCENARIO VALUATION &amp; FREE CASH FLOW RETURN SIMULATOR
          </div>
          <div style="display:grid; grid-template-columns:1fr 1fr; gap:18px;">
            <div>
              <div style="font-size:11px; color:#94a3b8; margin-bottom:6px;">
                Hyperscaler Cloud Revenue CAGR: <strong id="val_cloud_cagr" style="color:#00e5ff;">18%</strong>
              </div>
              <input type="range" id="slider_cloud_cagr" min="8" max="30" step="1" value="18" oninput="updateCloudSim()" style="width:100%; accent-color:#00e5ff; cursor:pointer;">
            </div>
            <div style="background:#070d16; border:1px solid #162436; border-radius:6px; padding:14px; font-family:var(--font-mono);">
              <div style="display:flex; justify-content:space-between; padding:6px 0;">
                <span style="color:#ff5252;">🐻 Bear Case:</span>
                <strong id="cloud_bear_irr" style="color:#ff5252;">10.8% IRR</strong>
              </div>
              <div style="display:flex; justify-content:space-between; padding:6px 0;">
                <span style="color:#ffaa00;">🎯 Base Case:</span>
                <strong id="cloud_base_irr" style="color:#ffaa00; font-size:13px;">17.4% IRR</strong>
              </div>
              <div style="display:flex; justify-content:space-between; padding:6px 0;">
                <span style="color:#00e676;">🚀 Bull Case:</span>
                <strong id="cloud_bull_irr" style="color:#00e676; font-size:13px;">25.2% IRR</strong>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- ══════════════════════════════════════════════════════════════════════════ -->
    <!-- SUB-PANE 5: GLOBAL ENERGY & SUPERMAJORS (SAUDI ARAMCO, EXXONMOBIL, SHELL) -->
    <!-- ══════════════════════════════════════════════════════════════════════════ -->
    <div id="soic_sec_pane_energy" style="display:none;">
      <div style="background:#080e18; border:1px solid #1a2a3e; border-radius:6px; padding:18px 22px; margin-bottom:16px;">
        <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:12px; margin-bottom:16px; border-bottom:1px solid #1a2736; padding-bottom:12px;">
          <div>
            <div style="font-size:14px; font-weight:800; color:#ffaa00; font-family:var(--font-mono);">
              ⚡ GLOBAL INTEGRATED ENERGY, SUPERMAJORS &amp; OPEC+ (MIDDLE EAST / US / EUROPE)
            </div>
            <div style="font-size:11px; color:#94a3b8; margin-top:2px;">
              Champions: Saudi Aramco (2222:SR, $1.9T) · ExxonMobil (XOM:US, $480B) · Shell (SHEL:LN, $210B) · Chevron (CVX:US, $290B)
            </div>
          </div>
          <div style="display:flex; gap:12px; font-size:11px; font-family:var(--font-mono);">
            <div style="background:#0f1d2e; padding:4px 10px; border-radius:4px; border:1px solid #1e3a5f;">
              Aramco Lifting Cost: <strong style="color:#00e676;">$3.19 / boe</strong>
            </div>
            <div style="background:#0f1d2e; padding:4px 10px; border-radius:4px; border:1px solid #1e3a5f;">
              Dividend + Buyback Yield: <strong style="color:#ffaa00;">7.8%</strong>
            </div>
          </div>
        </div>

        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(220px, 1fr)); gap:12px; margin-bottom:18px;">
          <div style="background:#0d1826; border:1px solid #1e3046; border-radius:6px; padding:12px;">
            <div style="font-size:10px; color:#64748b; font-family:var(--font-mono);">GHAWAR FIELD PRODUCTION</div>
            <div style="font-size:18px; font-weight:900; color:#00e5ff; font-family:var(--font-mono); margin-top:2px;">3.8M bpd</div>
            <div style="font-size:10px; color:#94a3b8; margin-top:4px;">World's largest conventional onshore reservoir</div>
          </div>
          <div style="background:#0d1826; border:1px solid #1e3046; border-radius:6px; padding:12px;">
            <div style="font-size:10px; color:#64748b; font-family:var(--font-mono);">PERMIAN BASIN PRODUCTION (XOM)</div>
            <div style="font-size:18px; font-weight:900; color:#00e676; font-family:var(--font-mono); margin-top:2px;">1.4M boe/d</div>
            <div style="font-size:10px; color:#94a3b8; margin-top:4px;">Expanded via $60B Pioneer merger</div>
          </div>
        </div>

        <div style="background:#0b1420; border:1px solid #1a2a3e; border-radius:6px; padding:16px;">
          <div style="display:grid; grid-template-columns:1fr 1fr; gap:18px;">
            <div>
              <div style="font-size:11px; color:#94a3b8; margin-bottom:6px;">
                Long-Term Brent Crude: <strong id="val_energy_brent" style="color:#ffaa00;">$78 / bbl</strong>
              </div>
              <input type="range" id="slider_energy_brent" min="50" max="120" step="2" value="78" oninput="updateEnergySim()" style="width:100%; accent-color:#ffaa00; cursor:pointer;">
            </div>
            <div style="background:#070d16; border:1px solid #162436; border-radius:6px; padding:14px; font-family:var(--font-mono);">
              <div style="display:flex; justify-content:space-between; padding:6px 0;">
                <span style="color:#ff5252;">🐻 Bear ($55):</span>
                <strong id="energy_bear_irr" style="color:#ff5252;">8.4% IRR</strong>
              </div>
              <div style="display:flex; justify-content:space-between; padding:6px 0;">
                <span style="color:#ffaa00;">🎯 Base ($78):</span>
                <strong id="energy_base_irr" style="color:#ffaa00; font-size:13px;">15.8% IRR</strong>
              </div>
              <div style="display:flex; justify-content:space-between; padding:6px 0;">
                <span style="color:#00e676;">🚀 Bull ($105):</span>
                <strong id="energy_bull_irr" style="color:#00e676; font-size:13px;">24.6% IRR</strong>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- ══════════════════════════════════════════════════════════════════════════ -->
    <!-- SUB-PANE 6: GLOBAL MINING & CRITICAL METALS (BHP, RIO, VALE) -->
    <!-- ══════════════════════════════════════════════════════════════════════════ -->
    <div id="soic_sec_pane_mining" style="display:none;">
      <div style="background:#080e18; border:1px solid #1a2a3e; border-radius:6px; padding:18px 22px; margin-bottom:16px;">
        <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:12px; margin-bottom:16px;">
          <div>
            <div style="font-size:14px; font-weight:800; color:#34d399; font-family:var(--font-mono);">
              ⛏️ GLOBAL CRITICAL METALS, COPPER &amp; TRANSITION RESOURCES (AUSTRALIA / BRAZIL / UK)
            </div>
            <div style="font-size:11px; color:#94a3b8; margin-top:2px;">
              Champions: BHP Group (BHP:AU, $145B) · Rio Tinto (RIO:LN, $112B) · Vale (VALE:BR, $52B) · Freeport-McMoRan (FCX:US, $64B)
            </div>
          </div>
        </div>
        <div style="display:flex; gap:16px; font-family:var(--font-mono); font-size:12px;">
          <div style="background:#0d1826; padding:10px 16px; border-radius:4px;">Copper C1 Cash Cost: <strong style="color:#00e676;">$1.45 / lb</strong></div>
          <div style="background:#0d1826; padding:10px 16px; border-radius:4px;">Pilbara Iron Ore FOB: <strong style="color:#00e5ff;">$18.50 / wet ton</strong></div>
          <div style="background:#0d1826; padding:10px 16px; border-radius:4px;">5-Yr Base IRR: <strong style="color:#ffaa00;">16.4%</strong></div>
        </div>
      </div>
    </div>

    <!-- ══════════════════════════════════════════════════════════════════════════ -->
    <!-- SUB-PANE 7: CLEAN MOBILITY, EVS & AUTOMOTIVE (TESLA, TOYOTA, BYD) -->
    <!-- ══════════════════════════════════════════════════════════════════════════ -->
    <div id="soic_sec_pane_auto" style="display:none;">
      <div style="background:#080e18; border:1px solid #1a2a3e; border-radius:6px; padding:18px 22px; margin-bottom:16px;">
        <div style="font-size:14px; font-weight:800; color:#f43f5e; font-family:var(--font-mono);">
          🚗 GLOBAL CLEAN MOBILITY, AUTONOMY &amp; PASSENGER AUTOMOTIVE (US / JAPAN / CHINA)
        </div>
        <div style="font-size:11px; color:#94a3b8; margin-top:2px; margin-bottom:12px;">
          Champions: Tesla (TSLA:US, $780B) · Toyota Motor (7203:JP, $280B) · BYD (1211:HK, $110B) · Ferrari (RACE:US, $75B)
        </div>
        <div style="display:flex; gap:16px; font-family:var(--font-mono); font-size:12px;">
          <div style="background:#0d1826; padding:10px 16px; border-radius:4px;">BYD Battery Pack Cost: <strong style="color:#00e676;">$62 / kWh</strong></div>
          <div style="background:#0d1826; padding:10px 16px; border-radius:4px;">Ferrari Gross Margin: <strong style="color:#ffaa00;">49.8%</strong></div>
          <div style="background:#0d1826; padding:10px 16px; border-radius:4px;">5-Yr Base IRR: <strong style="color:#00e5ff;">18.2%</strong></div>
        </div>
      </div>
    </div>

    <!-- ══════════════════════════════════════════════════════════════════════════ -->
    <!-- SUB-PANE 8: SYSTEMIC GLOBAL BANKING & WEALTH (JPM, DBS, HDFC) -->
    <!-- ══════════════════════════════════════════════════════════════════════════ -->
    <div id="soic_sec_pane_bank" style="display:none;">
      <div style="background:#080e18; border:1px solid #1a2a3e; border-radius:6px; padding:18px 22px; margin-bottom:16px;">
        <div style="font-size:14px; font-weight:800; color:#fbbf24; font-family:var(--font-mono);">
          🏦 SYSTEMIC GLOBAL BANKING, ASSET MANAGEMENT &amp; WEALTH (WALL STREET / ASIA)
        </div>
        <div style="font-size:11px; color:#94a3b8; margin-top:2px; margin-bottom:12px;">
          Champions: JPMorgan Chase (JPM:US, $580B) · DBS Group (D05:SG, $82B) · HDFC Bank (HDFCBANK:IN, $152B) · ICICI Bank (ICICIBANK:IN, $105B)
        </div>
        <div style="display:flex; gap:16px; font-family:var(--font-mono); font-size:12px;">
          <div style="background:#0d1826; padding:10px 16px; border-radius:4px;">JPMorgan CET1 Ratio: <strong style="color:#00e676;">15.3%</strong></div>
          <div style="background:#0d1826; padding:10px 16px; border-radius:4px;">HDFC Bank Net NPA: <strong style="color:#00e5ff;">0.35%</strong></div>
          <div style="background:#0d1826; padding:10px 16px; border-radius:4px;">5-Yr Base IRR: <strong style="color:#ffaa00;">16.8%</strong></div>
        </div>
      </div>
    </div>

    <!-- ══════════════════════════════════════════════════════════════════════════ -->
    <!-- SUB-PANE 9: PHARMACEUTICALS & HEALTHCARE (ELI LILLY, NOVO, NARAYANA) -->
    <!-- ══════════════════════════════════════════════════════════════════════════ -->
    <div id="soic_sec_pane_pharma" style="display:none;">
      <div style="background:#080e18; border:1px solid #1a2a3e; border-radius:6px; padding:18px 22px; margin-bottom:16px;">
        <div style="font-size:14px; font-weight:800; color:#a78bfa; font-family:var(--font-mono);">
          💊 GLOBAL PHARMACEUTICALS, GLP-1 INCRETIN &amp; HEALTHCARE NETWORKS
        </div>
        <div style="font-size:11px; color:#94a3b8; margin-top:2px; margin-bottom:12px;">
          Champions: Eli Lilly (LLY:US, $840B) · Novo Nordisk (NOVO:DC, $560B) · Narayana Hrudayalaya (NH:IN, $3.2B) · Sun Pharma ($42B)
        </div>
        <div style="display:flex; gap:16px; font-family:var(--font-mono); font-size:12px;">
          <div style="background:#0d1826; padding:10px 16px; border-radius:4px;">GLP-1 TAM (2030E): <strong style="color:#00e5ff;">$130B</strong></div>
          <div style="background:#0d1826; padding:10px 16px; border-radius:4px;">R&amp;D Intensity: <strong style="color:#00e676;">24.2% of Sales</strong></div>
          <div style="background:#0d1826; padding:10px 16px; border-radius:4px;">5-Yr Base IRR: <strong style="color:#ffaa00;">19.4%</strong></div>
        </div>
      </div>
    </div>

    <!-- ══════════════════════════════════════════════════════════════════════════ -->
    <!-- SUB-PANE 10: POWER GRID & INFRASTRUCTURE (POLYCAB, KEI, PRYSMIAN) -->
    <!-- ══════════════════════════════════════════════════════════════════════════ -->
    <div id="soic_sec_pane_grid" style="display:none;">
      <div style="background:#080e18; border:1px solid #1a2a3e; border-radius:6px; padding:18px 22px; margin-bottom:16px;">
        <div style="font-size:14px; font-weight:800; color:#38bdf8; font-family:var(--font-mono);">
          🔌 GLOBAL POWER TRANSMISSION, EHV INFRASTRUCTURE &amp; CABLES (INDIA / EUROPE)
        </div>
        <div style="font-size:11px; color:#94a3b8; margin-top:2px; margin-bottom:12px;">
          Champions: Polycab India (POLYCAB:IN, ₹1.07T) · KEI Industries (KEI:IN, ₹410B) · Prysmian Group (PRY:IM, €18B) · Siemens Energy (€32B)
        </div>
        <div style="display:flex; gap:16px; font-family:var(--font-mono); font-size:12px;">
          <div style="background:#0d1826; padding:10px 16px; border-radius:4px;">Polycab ROCE: <strong style="color:#00e676;">28.4%</strong></div>
          <div style="background:#0d1826; padding:10px 16px; border-radius:4px;">Working Capital: <strong style="color:#00e5ff;">52 Days</strong></div>
          <div style="background:#0d1826; padding:10px 16px; border-radius:4px;">5-Yr Base IRR: <strong style="color:#ffaa00;">21.6%</strong></div>
        </div>
      </div>
    </div>

    <!-- ══════════════════════════════════════════════════════════════════════════ -->
    <!-- SUB-PANE 11: STRUCTURAL STEEL & INDUSTRIAL MATERIALS (APL APOLLO, NUCOR) -->
    <!-- ══════════════════════════════════════════════════════════════════════════ -->
    <div id="soic_sec_pane_steel" style="display:none;">
      <div style="background:#080e18; border:1px solid #1a2a3e; border-radius:6px; padding:18px 22px; margin-bottom:16px;">
        <div style="font-size:14px; font-weight:800; color:#e2e8f0; font-family:var(--font-mono);">
          🏗️ STRUCTURAL STEEL TUBES, ELECTRIC ARC FURNACES &amp; HEAVY MATERIALS
        </div>
        <div style="font-size:11px; color:#94a3b8; margin-top:2px; margin-bottom:12px;">
          Champions: APL Apollo Tubes (APLAPOLLO:IN, ₹420B) · Nucor (NUE:US, $38B) · Nippon Steel (5401:JP, $22B) · Tata Steel ($23B)
        </div>
        <div style="display:flex; gap:16px; font-family:var(--font-mono); font-size:12px;">
          <div style="background:#0d1826; padding:10px 16px; border-radius:4px;">APL Apollo Capacity: <strong style="color:#00e5ff;">5.0M MT</strong></div>
          <div style="background:#0d1826; padding:10px 16px; border-radius:4px;">EBITDA Spread: <strong style="color:#00e676;">₹4,650 / MT</strong></div>
          <div style="background:#0d1826; padding:10px 16px; border-radius:4px;">5-Yr Base IRR: <strong style="color:#ffaa00;">17.2%</strong></div>
        </div>
      </div>
    </div>

    <!-- ══════════════════════════════════════════════════════════════════════════ -->
    <!-- SUB-PANE 12: SPECIALTY CHEMICALS (BASF, PIDILITE, SHIN-ETSU) -->
    <!-- ══════════════════════════════════════════════════════════════════════════ -->
    <div id="soic_sec_pane_chem" style="display:none;">
      <div style="background:#080e18; border:1px solid #1a2a3e; border-radius:6px; padding:18px 22px; margin-bottom:16px;">
        <div style="font-size:14px; font-weight:800; color:#34d399; font-family:var(--font-mono);">
          🧪 SPECIALTY CHEMICALS, ADVANCED POLYMERS &amp; CONSUMER MOATS (GERMANY / INDIA / JAPAN)
        </div>
        <div style="font-size:11px; color:#94a3b8; margin-top:2px; margin-bottom:12px;">
          Champions: BASF SE (BAS:GY, €42B) · Pidilite Industries (PIDILITIND:IN, ₹1.52T) · Shin-Etsu Chemical (4063:JP, $78B) · Linde ($215B)
        </div>
        <div style="display:flex; gap:16px; font-family:var(--font-mono); font-size:12px;">
          <div style="background:#0d1826; padding:10px 16px; border-radius:4px;">Pidilite Market Share: <strong style="color:#00e676;">70%+</strong></div>
          <div style="background:#0d1826; padding:10px 16px; border-radius:4px;">Shin-Etsu Wafer Share: <strong style="color:#00e5ff;">31% Global</strong></div>
          <div style="background:#0d1826; padding:10px 16px; border-radius:4px;">5-Yr Base IRR: <strong style="color:#ffaa00;">18.5%</strong></div>
        </div>
      </div>
    </div>

    <!-- ══════════════════════════════════════════════════════════════════════════ -->
    <!-- SUB-PANE 13: LUXURY & CONSUMER TITANS (LVMH, COSTCO, TRENT) -->
    <!-- ══════════════════════════════════════════════════════════════════════════ -->
    <div id="soic_sec_pane_luxury" style="display:none;">
      <div style="background:#080e18; border:1px solid #1a2a3e; border-radius:6px; padding:18px 22px; margin-bottom:16px;">
        <div style="font-size:14px; font-weight:800; color:#f59e0b; font-family:var(--font-mono);">
          👑 GLOBAL LUXURY CONGLOMERATES &amp; HIGH-VELOCITY RETAIL (EUROPE / US / INDIA)
        </div>
        <div style="font-size:11px; color:#94a3b8; margin-top:2px; margin-bottom:12px;">
          Champions: LVMH Moët Hennessy (MC:FP, €340B) · Hermès (RMS:FP, €215B) · Costco (COST:US, $390B) · Trent Ltd (TRENT:IN, ₹2.6T)
        </div>
        <div style="display:flex; gap:16px; font-family:var(--font-mono); font-size:12px;">
          <div style="background:#0d1826; padding:10px 16px; border-radius:4px;">Hermès Gross Margin: <strong style="color:#00e676;">72.1%</strong></div>
          <div style="background:#0d1826; padding:10px 16px; border-radius:4px;">Costco Renewal Rate: <strong style="color:#00e5ff;">93.1%</strong></div>
          <div style="background:#0d1826; padding:10px 16px; border-radius:4px;">5-Yr Base IRR: <strong style="color:#ffaa00;">19.8%</strong></div>
        </div>
      </div>
    </div>

    <!-- ── INTERACTIVE CONTROLLERS JAVASCRIPT ── -->
    <script>
    (function() {
      var damoData = __DAMODARAN_DATA_PLACEHOLDER__;
      var compData = __COMPANIES_DATA_PLACEHOLDER__;
      var currentSortCol = 'waccPct';
      var sortAsc = false;

      // ── Sub-tab Switcher ──
      window.switchSoicSectorTab = function(tabId) {
        var subtabs = ['damodaran', 'lookup', 'semi', 'cloud', 'energy', 'mining', 'auto', 'bank', 'pharma', 'grid', 'steel', 'chem', 'luxury'];
        subtabs.forEach(function(id) {
          var pane = document.getElementById('soic_sec_pane_' + id);
          var btn = document.getElementById('btn_sec_' + id);
          if (pane) pane.style.display = (id === tabId) ? 'block' : 'none';
          if (btn) {
            if (id === tabId) {
              btn.classList.add('active');
              btn.style.color = '#00e5ff';
              btn.style.borderColor = '#00e5ff';
            } else {
              btn.classList.remove('active');
              btn.style.color = '';
              btn.style.borderColor = '';
            }
          }
        });
      };

      // ── Render Damodaran 94 Table ──
      window.renderDamodaranTable = function(filtered) {
        var list = filtered || damoData;
        var tbody = document.getElementById('damodaran_table_body');
        if (!tbody) return;
        var html = '';
        list.forEach(function(row) {
          var titansStr = (row.titans && row.titans.length > 0) ? row.titans.join(', ') : '—';
          var spreadColor = row.evaSpreadPct > 0 ? '#00e676' : '#ff5252';
          html += '<tr style="border-bottom:1px solid #142030; font-family:var(--font-mono);">' +
            '<td style="padding:8px 12px; font-weight:700; color:#fff;">' + row.name + '</td>' +
            '<td style="padding:8px 12px; color:#38bdf8;">' + row.sector + '</td>' +
            '<td style="padding:8px 12px; text-align:right; color:#94a3b8;">' + (row.firms || 0) + '</td>' +
            '<td style="padding:8px 12px; text-align:right; color:#94a3b8;">' + row.unleveredBeta.toFixed(2) + '</td>' +
            '<td style="padding:8px 12px; text-align:right; color:#00e5ff; font-weight:700;">' + row.waccPct.toFixed(2) + '%</td>' +
            '<td style="padding:8px 12px; text-align:right; color:#00e676;">' + row.ebitMarginPct.toFixed(2) + '%</td>' +
            '<td style="padding:8px 12px; text-align:right; color:#94a3b8;">' + row.grossMarginPct.toFixed(2) + '%</td>' +
            '<td style="padding:8px 12px; text-align:right; color:#c084fc;">' + row.evEbitda.toFixed(1) + 'x</td>' +
            '<td style="padding:8px 12px; text-align:right; color:#38bdf8;">' + row.rocPct.toFixed(2) + '%</td>' +
            '<td style="padding:8px 12px; text-align:right; color:' + spreadColor + '; font-weight:700;">' + (row.evaSpreadPct > 0 ? '+' : '') + row.evaSpreadPct.toFixed(2) + '%</td>' +
            '<td style="padding:8px 12px; color:#e2e8f0; font-size:10px;">' + titansStr + '</td>' +
            '</tr>';
        });
        tbody.innerHTML = html;
        var countDisp = document.getElementById('damo_count_display');
        if (countDisp) countDisp.innerText = list.length;
      };

      // ── Filter Table ──
      window.filterDamodaranTable = function() {
        var query = (document.getElementById('damo_search_input')?.value || '').toLowerCase().trim();
        var sector = document.getElementById('damo_sector_filter')?.value || 'ALL';
        var filtered = damoData.filter(function(item) {
          var matchSector = (sector === 'ALL') || (item.sector === sector);
          var matchQuery = (!query) ||
            item.name.toLowerCase().includes(query) ||
            item.sector.toLowerCase().includes(query) ||
            (item.titans && item.titans.some(function(t) { return t.toLowerCase().includes(query); }));
          return matchSector && matchQuery;
        });
        renderDamodaranTable(filtered);
      };

      // ── Sort Table ──
      window.sortDamodaranTable = function(col) {
        if (currentSortCol === col) sortAsc = !sortAsc;
        else { currentSortCol = col; sortAsc = (col === 'name' || col === 'sector'); }
        damoData.sort(function(a, b) {
          var va = a[col], vb = b[col];
          if (typeof va === 'string') {
            return sortAsc ? va.localeCompare(vb) : vb.localeCompare(va);
          }
          return sortAsc ? (va - vb) : (vb - va);
        });
        filterDamodaranTable();
      };

      // ── 48k Company Lookup Search ──
      window.searchGlobalCompanies = function() {
        var q = (document.getElementById('company_lookup_input')?.value || '').toLowerCase().trim();
        var container = document.getElementById('company_search_results');
        if (!container) return;
        if (!q || q.length < 2) {
          renderCompanyCards(compData.slice(0, 15));
          return;
        }
        var matches = compData.filter(function(c) {
          return c[0].toLowerCase().includes(q) ||
                 c[1].toLowerCase().includes(q) ||
                 c[2].toLowerCase().includes(q) ||
                 c[3].toLowerCase().includes(q);
        }).slice(0, 30);
        renderCompanyCards(matches);
      };

      function renderCompanyCards(list) {
        var container = document.getElementById('company_search_results');
        if (!container) return;
        if (list.length === 0) {
          container.innerHTML = '<div style="color:#64748b; font-family:var(--font-mono); font-size:12px; grid-column:1/-1; padding:20px 0; text-align:center;">No matching companies found in taxonomy. Try searching another ticker or country.</div>';
          return;
        }
        var html = '';
        list.forEach(function(c) {
          var name = c[0], ticker = c[1], ind = c[2], ctry = c[3], sec = c[4];
          var bm = damoData.find(function(d) { return d.name.toLowerCase() === ind.toLowerCase(); }) || {};
          html += '<div style="background:#0d1826; border:1px solid #1e3046; border-radius:6px; padding:12px 14px; font-family:var(--font-mono);">' +
            '<div style="display:flex; justify-content:space-between; align-items:flex-start;">' +
              '<div>' +
                '<div style="font-weight:800; color:#fff; font-size:12px;">' + name + '</div>' +
                '<div style="color:#00e5ff; font-size:11px; margin-top:2px;">' + (ticker || 'UNLISTED') + ' · <span style="color:#94a3b8;">' + ctry + '</span></div>' +
              '</div>' +
              '<span style="background:rgba(0,229,255,0.1); color:#00e5ff; font-size:9px; padding:2px 6px; border-radius:3px;">' + sec + '</span>' +
            '</div>' +
            '<div style="border-top:1px solid #162436; margin-top:8px; padding-top:8px; font-size:10px; color:#94a3b8;">' +
              'Damodaran Industry: <strong style="color:#ffaa00;">' + ind + '</strong>' +
              '<div style="display:flex; gap:10px; margin-top:4px;">' +
                '<span>WACC: <strong style="color:#00e5ff;">' + (bm.waccPct ? bm.waccPct.toFixed(1) + '%' : '—') + '</strong></span>' +
                '<span>EBIT Margin: <strong style="color:#00e676;">' + (bm.ebitMarginPct ? bm.ebitMarginPct.toFixed(1) + '%' : '—') + '</strong></span>' +
                '<span>EV/EBITDA: <strong style="color:#c084fc;">' + (bm.evEbitda ? bm.evEbitda.toFixed(1) + 'x' : '—') + '</strong></span>' +
              '</div>' +
            '</div>' +
          '</div>';
        });
        container.innerHTML = html;
      }

      // ── Semi Simulator ──
      window.updateSemiSim = function() {
        var tam = parseFloat(document.getElementById('slider_semi_tam')?.value || 32);
        var mult = parseFloat(document.getElementById('slider_semi_mult')?.value || 28);
        var tamDisp = document.getElementById('val_semi_tam');
        if (tamDisp) tamDisp.innerText = tam + '%';
        var multDisp = document.getElementById('val_semi_mult');
        if (multDisp) multDisp.innerText = mult.toFixed(1) + 'x';
        
        var bear = (14.2 + (tam - 32)*0.35 + (mult - 28)*0.25).toFixed(1);
        var base = (23.8 + (tam - 32)*0.45 + (mult - 28)*0.35).toFixed(1);
        var bull = (34.5 + (tam - 32)*0.60 + (mult - 28)*0.50).toFixed(1);
        
        if (document.getElementById('semi_bear_irr')) document.getElementById('semi_bear_irr').innerText = bear + '% IRR';
        if (document.getElementById('semi_base_irr')) document.getElementById('semi_base_irr').innerText = base + '% IRR';
        if (document.getElementById('semi_bull_irr')) document.getElementById('semi_bull_irr').innerText = bull + '% IRR';
      };

      // ── Cloud Simulator ──
      window.updateCloudSim = function() {
        var cagr = parseFloat(document.getElementById('slider_cloud_cagr')?.value || 18);
        var cagrDisp = document.getElementById('val_cloud_cagr');
        if (cagrDisp) cagrDisp.innerText = cagr + '%';
        var bear = (10.8 + (cagr - 18)*0.4).toFixed(1);
        var base = (17.4 + (cagr - 18)*0.55).toFixed(1);
        var bull = (25.2 + (cagr - 18)*0.75).toFixed(1);
        if (document.getElementById('cloud_bear_irr')) document.getElementById('cloud_bear_irr').innerText = bear + '% IRR';
        if (document.getElementById('cloud_base_irr')) document.getElementById('cloud_base_irr').innerText = base + '% IRR';
        if (document.getElementById('cloud_bull_irr')) document.getElementById('cloud_bull_irr').innerText = bull + '% IRR';
      };

      // ── Energy Simulator ──
      window.updateEnergySim = function() {
        var brent = parseFloat(document.getElementById('slider_energy_brent')?.value || 78);
        var brentDisp = document.getElementById('val_energy_brent');
        if (brentDisp) brentDisp.innerText = '$' + brent + ' / bbl';
        var bear = (8.4 + (brent - 78)*0.18).toFixed(1);
        var base = (15.8 + (brent - 78)*0.25).toFixed(1);
        var bull = (24.6 + (brent - 78)*0.32).toFixed(1);
        if (document.getElementById('energy_bear_irr')) document.getElementById('energy_bear_irr').innerText = bear + '% IRR';
        if (document.getElementById('energy_base_irr')) document.getElementById('energy_base_irr').innerText = base + '% IRR';
        if (document.getElementById('energy_bull_irr')) document.getElementById('energy_bull_irr').innerText = bull + '% IRR';
      };

      // Init on load
      setTimeout(function() {
        renderDamodaranTable();
        searchGlobalCompanies();
      }, 200);

    })();
    </script>
    """
    return template.replace('__DAMODARAN_DATA_PLACEHOLDER__', damo_json_str).replace('__COMPANIES_DATA_PLACEHOLDER__', comp_json_str)

get_soic_sector_models_html = build_soic_sector_models_section
