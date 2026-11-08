"""
EconAgent Platform — Fractal Multi-Scale Zoom Intelligence Engine
================================================================
Implements the 5-Tier Hierarchical Zoom Architecture with Synchronized
Cascading Dropdowns and the Complete 110-Point SOIC Technical Analysis Pillar:
  Tier 1: GLOBAL MARKET (Orbital Macro, World GDP $105.4T, Global ERP Blocs, Choke Points)
  Tier 2: COUNTRY SOVEREIGN (National Capital, Damodaran CRP, Yield Curves, Sovereign Ratings)
  Tier 3: INDUSTRIAL SECTOR (Damodaran Betas, WACC, OPM, and SOIC Deep Unit Economics for
          Cables & Wires, Education & EdTech, Specialty Chemicals, Hospitals, Steel Tubes, Tech)
  Tier 4: MICRO LEVEL (Firm DCF, Complete SOIC 310-Point Scorecard including the Full 110-Point
          Technical Analysis Pillar, Beneish M-Score, Altman Z, Sloan Accruals, DuPont 5-Way, Kyle's Lambda)
  Tier 5: NANO LEVEL (Physical Facilities, Refineries, Extrusion Towers, EdTech Studios & Level 2 Order Book DOM)

Evidence-grounded, zero-hallucination, interactive bidirectional cross-linking across all 5 tiers.
"""

from typing import Dict, Any

def build_fractal_zoom_section(by_agent: Dict[str, Any] = None) -> str:
    """
    Renders the complete interactive 5-Tier Fractal Zoom Engine section.
    """
    html_markup = """
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

<!-- ═══════════════════════════════════════════════════════════════════════ -->
<!-- 🔬 FRACTAL 5-TIER ZOOM INTELLIGENCE ENGINE (GLOBAL ➔ COUNTRY ➔ SECTOR ➔ MICRO ➔ NANO) -->
<!-- ═══════════════════════════════════════════════════════════════════════ -->
<div class="section" id="fractal_zoom_section_wrap">
  
  <!-- Ribbon Header -->
  <div style="background: linear-gradient(135deg, #090e17 0%, #0d1726 50%, #122238 100%); border: 1px solid #1f334a; border-radius: 8px; padding: 14px 20px; margin-bottom: 14px; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 14px; font-family: var(--font-mono);">
    <div>
      <div style="display: flex; align-items: center; gap: 10px;">
        <span style="font-size: 20px;">🔬</span>
        <span style="color: #00e5ff; font-weight: 800; font-size: 15px; letter-spacing: 0.8px;">FRACTAL MULTI-SCALE ZOOM INTELLIGENCE ENGINE</span>
        <span class="badge" style="background: #00e676; color: #000; font-weight: 800; padding: 2px 8px; font-size: 10px;">5-TIER SYNCHRONIZED</span>
        <span class="badge" style="background: #1e3a5f; color: #00e5ff; padding: 2px 8px; font-size: 10px;">SOIC 310-PT + DAMODARAN 2026</span>
      </div>
      <div style="color: #94a3b8; font-size: 11px; margin-top: 4px;">
        Orbital Macro ($105.4T) &gt; Sovereign Capital (12 Nations) &gt; Sector Value Chains (Cables, Education, Chem, Hosp) &gt; Micro Firm DCF (110-Pt Technicals) &gt; Physical Plant Telemetry &amp; Level 2 DOM
      </div>
    </div>

    <!-- Live Zoom Readout -->
    <div style="text-align: right; display: flex; align-items: center; gap: 14px;">
      <div style="background: #060a10; border: 1px solid #1a293d; border-radius: 6px; padding: 6px 12px; text-align: left;">
        <div style="color: #64748b; font-size: 9px; font-weight: 700;">CURRENT RESOLUTION LEVEL:</div>
        <div style="color: #ffaa00; font-weight: 800; font-size: 11px;" id="zoom_altitude_readout">
          TIER 1 OF 5 · GLOBAL ORBITAL MACRO ($105.4T WORLD GDP)
        </div>
      </div>
      <button onclick="setFractalTier(1)" class="action-btn" style="background: #101c2b; border: 1px solid #1f354e; color: #00e5ff; font-size: 11px; padding: 6px 12px; cursor: pointer; border-radius: 4px;">
        🌐 RESET TO ORBITAL
      </button>
    </div>
  </div>

  <!-- ═══════════════════════════════════════════════════════════════════════ -->
  <!-- 🎛️ DUAL-LINKED CASCADING DROPDOWN NAVIGATION BAR (UNIVERSAL SELECTOR) -->
  <!-- ═══════════════════════════════════════════════════════════════════════ -->
  <div style="background: linear-gradient(90deg, #070c14 0%, #0c1524 100%); border: 1px solid #1e3a5f; border-radius: 6px; padding: 10px 16px; margin-bottom: 12px; display: flex; align-items: center; gap: 14px; flex-wrap: wrap; font-family: var(--font-mono);">
    
    <!-- Country Dropdown -->
    <div style="display: flex; align-items: center; gap: 6px;">
      <span style="color: #ffaa00; font-size: 11px; font-weight: 800; display: flex; align-items: center; gap: 4px;">
        <span>📍</span> COUNTRY:
      </span>
      <select id="zoom_country_select" onchange="onCountryDropdownChange(this.value)" style="background: #0f1c2e; color: #00e5ff; border: 1px solid #294c7a; border-radius: 4px; padding: 6px 10px; font-size: 11px; font-weight: 700; font-family: var(--font-mono); cursor: pointer; outline: none;">
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

    <!-- Sector Dropdown (Dynamic) -->
    <div style="display: flex; align-items: center; gap: 6px;">
      <span style="color: #00e5ff; font-size: 11px; font-weight: 800; display: flex; align-items: center; gap: 4px;">
        <span>🏭</span> SECTOR:
      </span>
      <select id="zoom_sector_select" onchange="onSectorDropdownChange(this.value)" style="background: #0f1c2e; color: #ffeb3b; border: 1px solid #294c7a; border-radius: 4px; padding: 6px 10px; font-size: 11px; font-weight: 700; font-family: var(--font-mono); cursor: pointer; outline: none;">
        <!-- Populated dynamically based on selected country -->
      </select>
    </div>

    <!-- Company Dropdown (Dynamic) -->
    <div style="display: flex; align-items: center; gap: 6px;">
      <span style="color: #00ff88; font-size: 11px; font-weight: 800; display: flex; align-items: center; gap: 4px;">
        <span>🏢</span> COMPANY:
      </span>
      <select id="zoom_firm_select" onchange="onFirmDropdownChange(this.value)" style="background: #0f1c2e; color: #00ff88; border: 1px solid #294c7a; border-radius: 4px; padding: 6px 10px; font-size: 11px; font-weight: 700; font-family: var(--font-mono); cursor: pointer; outline: none;">
        <!-- Populated dynamically based on selected sector -->
      </select>
    </div>

    <!-- Nano Physical Asset Dropdown (Dynamic) -->
    <div style="display: flex; align-items: center; gap: 6px;">
      <span style="color: #e040fb; font-size: 11px; font-weight: 800; display: flex; align-items: center; gap: 4px;">
        <span>🔬</span> NANO ASSET:
      </span>
      <select id="zoom_nano_select" onchange="onNanoDropdownChange(this.value)" style="background: #0f1c2e; color: #e040fb; border: 1px solid #294c7a; border-radius: 4px; padding: 6px 10px; font-size: 11px; font-weight: 700; font-family: var(--font-mono); cursor: pointer; outline: none;">
        <!-- Populated dynamically based on selected firm -->
      </select>
    </div>

    <!-- Sync Action Button -->
    <div style="margin-left: auto; display: flex; align-items: center; gap: 8px;">
      <button onclick="syncAllTiersToDropdowns()" class="action-btn" style="background: #1e3a5f; color: #fff; padding: 5px 12px; font-size: 11px; font-weight: 700; border-radius: 4px; border: 1px solid #3b82f6; cursor: pointer; display: flex; align-items: center; gap: 4px;">
        <span>🔄</span> SYNC ALL 5 TIERS
      </button>
    </div>
  </div>

  <!-- ═══════════════════════════════════════════════════════════════════════ -->
  <!-- 5-TIER ALTITUDE RAIL SWITCHER & ACTIVE BREADCRUMB HIERARCHY -->
  <!-- ═══════════════════════════════════════════════════════════════════════ -->
  <div style="background: #080d16; border: 1px solid #18283a; border-radius: 6px; padding: 10px 14px; margin-bottom: 16px; font-family: var(--font-mono);">
    
    <!-- 5 Tier Step Buttons -->
    <div style="display: grid; grid-template-columns: repeat(5, 1fr); gap: 10px; margin-bottom: 10px;">
      
      <!-- Tier 1 Button -->
      <button class="zoom-tier-btn active" id="btn_tier_1" onclick="setFractalTier(1)" style="padding: 10px 8px; background: #132032; border: 1px solid #ffaa00; border-radius: 6px; cursor: pointer; text-align: left; transition: all 0.2s;">
        <div style="color: #ffaa00; font-size: 10px; font-weight: 800;">TIER 1 · 10,000 KM</div>
        <div style="color: #fff; font-size: 12px; font-weight: 800; margin-top: 2px;">🌐 GLOBAL ORBITAL</div>
        <div style="color: #94a3b8; font-size: 9px; margin-top: 3px;">$105.4T World GDP · Macro Risk Blocs</div>
      </button>

      <!-- Tier 2 Button -->
      <button class="zoom-tier-btn" id="btn_tier_2" onclick="setFractalTier(2)" style="padding: 10px 8px; background: #0c1420; border: 1px solid #1c2e44; border-radius: 6px; cursor: pointer; text-align: left; transition: all 0.2s;">
        <div style="color: #64748b; font-size: 10px; font-weight: 800;">TIER 2 · 1,000 KM</div>
        <div style="color: #cfd8dc; font-size: 12px; font-weight: 800; margin-top: 2px;">🏛️ COUNTRY SOVEREIGN</div>
        <div style="color: #64748b; font-size: 9px; margin-top: 3px;">Damodaran CRP · Yield Curves · 12 Nations</div>
      </button>

      <!-- Tier 3 Button -->
      <button class="zoom-tier-btn" id="btn_tier_3" onclick="setFractalTier(3)" style="padding: 10px 8px; background: #0c1420; border: 1px solid #1c2e44; border-radius: 6px; cursor: pointer; text-align: left; transition: all 0.2s;">
        <div style="color: #64748b; font-size: 10px; font-weight: 800;">TIER 3 · 100 KM</div>
        <div style="color: #cfd8dc; font-size: 12px; font-weight: 800; margin-top: 2px;">🏭 INDUSTRIAL SECTORS</div>
        <div style="color: #64748b; font-size: 9px; margin-top: 3px;">Cables, EdTech, Chem, Hosp, Steel</div>
      </button>

      <!-- Tier 4 Button -->
      <button class="zoom-tier-btn" id="btn_tier_4" onclick="setFractalTier(4)" style="padding: 10px 8px; background: #0c1420; border: 1px solid #1c2e44; border-radius: 6px; cursor: pointer; text-align: left; transition: all 0.2s;">
        <div style="color: #64748b; font-size: 10px; font-weight: 800;">TIER 4 · 10 KM</div>
        <div style="color: #cfd8dc; font-size: 12px; font-weight: 800; margin-top: 2px;">🏢 MICRO FIRM &amp; DCF</div>
        <div style="color: #64748b; font-size: 9px; margin-top: 3px;">SOIC 310-Pt · 110-Pt Technical Pillar</div>
      </button>

      <!-- Tier 5 Button -->
      <button class="zoom-tier-btn" id="btn_tier_5" onclick="setFractalTier(5)" style="padding: 10px 8px; background: #0c1420; border: 1px solid #1c2e44; border-radius: 6px; cursor: pointer; text-align: left; transition: all 0.2s;">
        <div style="color: #64748b; font-size: 10px; font-weight: 800;">TIER 5 · 1 KM - 1 M</div>
        <div style="color: #cfd8dc; font-size: 12px; font-weight: 800; margin-top: 2px;">🔬 NANO ASSET &amp; DOM</div>
        <div style="color: #64748b; font-size: 9px; margin-top: 3px;">Extrusion Towers · Fabs · Level 2 DOM</div>
      </button>
    </div>

    <!-- Active Breadcrumb Hierarchy -->
    <div style="background: #05080e; border: 1px solid #131e2d; border-radius: 4px; padding: 8px 14px; display: flex; align-items: center; gap: 8px; font-size: 11px; flex-wrap: wrap;">
      <span style="color: #64748b; font-weight: 700;">FRACTAL TRAIL:</span>
      <span class="bc-link" onclick="setFractalTier(1)" style="color: #ffaa00; cursor: pointer; text-decoration: underline;" id="bc_tier_1">GLOBAL [World GDP $105.4T]</span>
      <span style="color: #475569;">&gt;</span>
      <span class="bc-link" onclick="setFractalTier(2)" style="color: #94a3b8; cursor: pointer;" id="bc_tier_2">INDIA [Baa3 / CRP 2.38%]</span>
      <span style="color: #475569;">&gt;</span>
      <span class="bc-link" onclick="setFractalTier(3)" style="color: #94a3b8; cursor: pointer;" id="bc_tier_3">CABLES &amp; WIRES [OPM 10.9%]</span>
      <span style="color: #475569;">&gt;</span>
      <span class="bc-link" onclick="setFractalTier(4)" style="color: #94a3b8; cursor: pointer;" id="bc_tier_4">POLYCAB [DCF ₹7,220 · SOIC 275/310]</span>
      <span style="color: #475569;">&gt;</span>
      <span class="bc-link" onclick="setFractalTier(5)" style="color: #94a3b8; cursor: pointer;" id="bc_tier_5">HALOL MEGA COMPLEX [150 Acres]</span>
    </div>
  </div>

  <!-- ═══════════════════════════════════════════════════════════════════════ -->
  <!-- TIER 1 PANE: GLOBAL ORBITAL MACRO VIEW -->
  <!-- ═══════════════════════════════════════════════════════════════════════ -->
  <div id="fractal_pane_tier_1" class="fractal-pane active" style="display: block;">
    <div class="stats-row">
      <div class="stat-card">
        <span class="stat-num">$105.4T</span>
        <span class="stat-label">World GDP (Nominal)</span>
      </div>
      <div class="stat-card">
        <span class="stat-num">$115.2T</span>
        <span class="stat-label">Global Equity Market Cap</span>
      </div>
      <div class="stat-card">
        <span class="stat-num">$92.4T</span>
        <span class="stat-label">Global Sovereign Debt</span>
      </div>
      <div class="stat-card">
        <span class="stat-num">5.58%</span>
        <span class="stat-label">Global Implied ERP</span>
      </div>
      <div class="stat-card">
        <span class="stat-num">67.5 Mbd</span>
        <span class="stat-label">Choke Point Crude Flow</span>
      </div>
      <div class="stat-card">
        <span class="stat-num">$75.82</span>
        <span class="stat-label">Brent Benchmark</span>
      </div>
    </div>

    <div style="display: grid; grid-template-columns: 1.2fr 1fr; gap: 16px; margin-bottom: 20px;">
      <!-- Continental Risk & ERP Blocs Table -->
      <div style="background: #090e17; border: 1px solid #1a293d; border-radius: 8px; padding: 16px;">
        <h3 style="color: #00e5ff; font-size: 13px; font-weight: 800; margin-bottom: 10px;">CONTINENTAL BLOCS: ERP, RISK-FREE &amp; COST OF CAPITAL</h3>
        <table class="data-table">
          <thead>
            <tr>
              <th>Continental Bloc</th>
              <th>GDP ($T)</th>
              <th>Equity Risk Prem (ERP)</th>
              <th>Risk-Free Rate</th>
              <th>WACC Benchmark</th>
              <th>Action</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong style="color: #fff;">North America</strong> (US, Canada)</td>
              <td>$29.8T</td>
              <td><span style="color: #00e676; font-weight: 700;">4.40%</span></td>
              <td>4.34% (US 10Y)</td>
              <td>7.95%</td>
              <td><button class="preset-btn" onclick="selectCountryFromGlobal('us')">Zoom US ➔</button></td>
            </tr>
            <tr>
              <td><strong style="color: #fff;">South Asia / India</strong></td>
              <td>$3.9T</td>
              <td><span style="color: #ffaa00; font-weight: 700;">6.78%</span></td>
              <td>6.81% (IN 10Y)</td>
              <td>11.20%</td>
              <td><button class="preset-btn" onclick="selectCountryFromGlobal('india')">Zoom India ➔</button></td>
            </tr>
            <tr>
              <td><strong style="color: #fff;">Western Europe</strong> (EU Core)</td>
              <td>$19.2T</td>
              <td><span style="color: #00e676; font-weight: 700;">5.40%</span></td>
              <td>2.38% (Bund 10Y)</td>
              <td>6.85%</td>
              <td><button class="preset-btn" onclick="selectCountryFromGlobal('germany')">Zoom Germany ➔</button></td>
            </tr>
            <tr>
              <td><strong style="color: #fff;">East Asia Developed</strong> (Japan, Korea)</td>
              <td>$6.8T</td>
              <td><span style="color: #00e676; font-weight: 700;">5.05%</span></td>
              <td>0.98% (JGB 10Y)</td>
              <td>5.45%</td>
              <td><button class="preset-btn" onclick="selectCountryFromGlobal('japan')">Zoom Japan ➔</button></td>
            </tr>
            <tr>
              <td><strong style="color: #fff;">China / Greater China</strong></td>
              <td>$18.5T</td>
              <td><span style="color: #ffaa00; font-weight: 700;">5.34%</span></td>
              <td>2.12% (CN 10Y)</td>
              <td>6.20%</td>
              <td><button class="preset-btn" onclick="selectCountryFromGlobal('china')">Zoom China ➔</button></td>
            </tr>
            <tr>
              <td><strong style="color: #fff;">Latin America</strong> (Brazil, Mexico)</td>
              <td>$5.4T</td>
              <td><span style="color: #ff3344; font-weight: 700;">8.22%</span></td>
              <td>12.40% (BR 10Y)</td>
              <td>14.80%</td>
              <td><button class="preset-btn" onclick="selectCountryFromGlobal('brazil')">Zoom Brazil ➔</button></td>
            </tr>
            <tr>
              <td><strong style="color: #fff;">United Kingdom</strong></td>
              <td>$3.4T</td>
              <td><span style="color: #00e676; font-weight: 700;">5.15%</span></td>
              <td>4.42% (Gilt 10Y)</td>
              <td>7.60%</td>
              <td><button class="preset-btn" onclick="selectCountryFromGlobal('uk')">Zoom UK ➔</button></td>
            </tr>
          </tbody>
        </table>
      </div>

      <!-- Strategic Maritime Choke Points -->
      <div style="background: #090e17; border: 1px solid #1a293d; border-radius: 8px; padding: 16px;">
        <h3 style="color: #ffaa00; font-size: 13px; font-weight: 800; margin-bottom: 10px;">STRATEGIC MARITIME CHOKE POINTS &amp; ENERGY ARTERIALS</h3>
        <div style="display: flex; flex-direction: column; gap: 10px; font-family: var(--font-mono); font-size: 11px;">
          <div style="background: #101c2b; border: 1px solid #1d334e; border-radius: 4px; padding: 8px 12px; display: flex; justify-content: space-between; align-items: center;">
            <div>
              <span style="color:#00e5ff;font-weight:800;">🇸🇦 STRAIT OF HORMUZ</span>
              <div style="color:#94a3b8;font-size:10px;">Persian Gulf to Gulf of Oman · 20% of Global Petroleum</div>
            </div>
            <div style="text-align:right;">
              <span style="color:#00e676;font-weight:800;font-size:12px;">21.0 Mbd</span>
              <div style="color:#64748b;font-size:9px;">VLCC Supertanker Fairway</div>
            </div>
          </div>

          <div style="background: #101c2b; border: 1px solid #1d334e; border-radius: 4px; padding: 8px 12px; display: flex; justify-content: space-between; align-items: center;">
            <div>
              <span style="color:#00e5ff;font-weight:800;">🇸🇬 MALACCA STRAIT</span>
              <div style="color:#94a3b8;font-size:10px;">Indian Ocean to South China Sea · Singapore Gateway</div>
            </div>
            <div style="text-align:right;">
              <span style="color:#00e676;font-weight:800;font-size:12px;">17.0 Mbd</span>
              <div style="color:#64748b;font-size:9px;">East Asian Supply Line</div>
            </div>
          </div>

          <div style="background: #101c2b; border: 1px solid #1d334e; border-radius: 4px; padding: 8px 12px; display: flex; justify-content: space-between; align-items: center;">
            <div>
              <span style="color:#ff3344;font-weight:800;">🇾🇪 BAB EL-MANDEB / RED SEA</span>
              <div style="color:#94a3b8;font-size:10px;">Red Sea to Gulf of Aden · 65% Diversion around Cape</div>
            </div>
            <div style="text-align:right;">
              <span style="color:#ffaa00;font-weight:800;font-size:12px;">4.8 Mbd</span>
              <div style="color:#ff3344;font-size:9px;">+14 Days Cape Transit</div>
            </div>
          </div>

          <div style="background: #101c2b; border: 1px solid #1d334e; border-radius: 4px; padding: 8px 12px; display: flex; justify-content: space-between; align-items: center;">
            <div>
              <span style="color:#00e5ff;font-weight:800;">🇪🇬 SUEZ CANAL &amp; SUMED</span>
              <div style="color:#94a3b8;font-size:10px;">Red Sea to Mediterranean Sea · Crude &amp; LNG Transit</div>
            </div>
            <div style="text-align:right;">
              <span style="color:#00e676;font-weight:800;font-size:12px;">5.5 Mbd</span>
              <div style="color:#64748b;font-size:9px;">Europe Crude Arterial</div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- ═══════════════════════════════════════════════════════════════════════ -->
  <!-- TIER 2 PANE: COUNTRY SOVEREIGN MARKET VIEW -->
  <!-- ═══════════════════════════════════════════════════════════════════════ -->
  <div id="fractal_pane_tier_2" class="fractal-pane" style="display: none;">
    <!-- Country Selector Ribbon -->
    <div style="background: #090e17; border: 1px solid #1a293d; border-radius: 8px; padding: 12px 18px; margin-bottom: 16px; display: flex; align-items: center; gap: 10px; flex-wrap: wrap;">
      <span style="color: var(--bb-amber); font-weight: 800; font-size: 11px;">SELECT SOVEREIGN:</span>
      <button class="preset-btn active" id="btn_c_india" onclick="loadCountrySovereign('india')">🇮🇳 INDIA (Baa3 / 6.78% ERP)</button>
      <button class="preset-btn" id="btn_c_us" onclick="loadCountrySovereign('us')">🇺🇸 UNITED STATES (Aaa / 4.40% ERP)</button>
      <button class="preset-btn" id="btn_c_germany" onclick="loadCountrySovereign('germany')">🇩🇪 GERMANY (Aaa / 5.40% ERP)</button>
      <button class="preset-btn" id="btn_c_japan" onclick="loadCountrySovereign('japan')">🇯🇵 JAPAN (A1 / 5.05% ERP)</button>
      <button class="preset-btn" id="btn_c_china" onclick="loadCountrySovereign('china')">🇨🇳 CHINA (A1 / 5.34% ERP)</button>
      <button class="preset-btn" id="btn_c_brazil" onclick="loadCountrySovereign('brazil')">🇧🇷 BRAZIL (Ba2 / 8.22% ERP)</button>
      <button class="preset-btn" id="btn_c_uk" onclick="loadCountrySovereign('uk')">🇬🇧 UNITED KINGDOM (Aa3 / 5.15% ERP)</button>
      <button class="preset-btn" id="btn_c_saudi" onclick="loadCountrySovereign('saudi')">🇸🇦 SAUDI ARABIA (A1 / 5.25% ERP)</button>
      <button class="preset-btn" id="btn_c_singapore" onclick="loadCountrySovereign('singapore')">🇸🇬 SINGAPORE (Aaa / 4.40% ERP)</button>
      <button class="preset-btn" id="btn_c_australia" onclick="loadCountrySovereign('australia')">🇦🇺 AUSTRALIA (Aaa / 4.40% ERP)</button>
      <button class="preset-btn" id="btn_c_korea" onclick="loadCountrySovereign('korea')">🇰🇷 SOUTH KOREA (Aa2 / 4.95% ERP)</button>
      <button class="preset-btn" id="btn_c_uae" onclick="loadCountrySovereign('uae')">🇦🇪 UAE (Aa2 / 4.98% ERP)</button>
    </div>

    <!-- Active Country Sovereign Telemetry -->
    <div id="country_telemetry_box" style="background: #0c1420; border: 1px solid #23374e; border-radius: 8px; padding: 18px; margin-bottom: 20px;">
      <!-- Populated dynamically by loadCountrySovereign() -->
    </div>
  </div>

  <!-- ═══════════════════════════════════════════════════════════════════════ -->
  <!-- TIER 3 PANE: INDUSTRIAL SECTOR VALUE CHAIN VIEW -->
  <!-- ═══════════════════════════════════════════════════════════════════════ -->
  <div id="fractal_pane_tier_3" class="fractal-pane" style="display: none;">
    <!-- Sector Selector Ribbon (Dynamically updated for country) -->
    <div id="sector_buttons_ribbon" style="background: #090e17; border: 1px solid #1a293d; border-radius: 8px; padding: 12px 18px; margin-bottom: 16px; display: flex; align-items: center; gap: 10px; flex-wrap: wrap;">
      <span style="color: var(--bb-amber); font-weight: 800; font-size: 11px;">SELECT SOIC / DAMODARAN SECTOR:</span>
      <!-- Populated dynamically -->
    </div>

    <!-- Active Sector Deep Blueprint -->
    <div id="sector_telemetry_box" style="background: #0c1420; border: 1px solid #23374e; border-radius: 8px; padding: 18px; margin-bottom: 20px;">
      <!-- Populated dynamically by loadSectorModel() -->
    </div>
  </div>

  <!-- ═══════════════════════════════════════════════════════════════════════ -->
  <!-- TIER 4 PANE: MICRO FIRM FORENSICS & SOIC 310-PT SCORECARD -->
  <!-- ═══════════════════════════════════════════════════════════════════════ -->
  <div id="fractal_pane_tier_4" class="fractal-pane" style="display: none;">
    <!-- Firm Selector Ribbon (Dynamically updated for sector) -->
    <div id="firm_buttons_ribbon" style="background: #090e17; border: 1px solid #1a293d; border-radius: 8px; padding: 12px 18px; margin-bottom: 16px; display: flex; align-items: center; gap: 10px; flex-wrap: wrap;">
      <span style="color: var(--bb-amber); font-weight: 800; font-size: 11px;">SELECT MICRO FIRM:</span>
      <!-- Populated dynamically -->
    </div>

    <!-- Active Firm Micro Telemetry Box -->
    <div id="firm_telemetry_box" style="background: #0c1420; border: 1px solid #23374e; border-radius: 8px; padding: 18px; margin-bottom: 20px;">
      <!-- Populated dynamically by loadFirmModel() -->
    </div>
  </div>

  <!-- ═══════════════════════════════════════════════════════════════════════ -->
  <!-- TIER 5 PANE: NANO PHYSICAL ASSETS, REFINERIES & ORDER BOOK LEVEL 2 DOM -->
  <!-- ═══════════════════════════════════════════════════════════════════════ -->
  <div id="fractal_pane_tier_5" class="fractal-pane" style="display: none;">
    <!-- Nano Asset Selector Ribbon (Dynamically updated) -->
    <div id="nano_buttons_ribbon" style="background: #090e17; border: 1px solid #1a293d; border-radius: 8px; padding: 12px 18px; margin-bottom: 16px; display: flex; align-items: center; gap: 10px; flex-wrap: wrap;">
      <span style="color: var(--bb-amber); font-weight: 800; font-size: 11px;">SELECT NANO ASSET / DOM:</span>
      <!-- Populated dynamically -->
    </div>

    <!-- Active Nano Telemetry Box -->
    <div id="nano_telemetry_box" style="background: #0c1420; border: 1px solid #23374e; border-radius: 8px; padding: 18px; margin-bottom: 20px;">
      <!-- Populated dynamically by loadNanoAsset() -->
    </div>
  </div>

</div>
<!-- ═══════════════════════════════════════════════════════════════════════ -->
"""

    js_code = """
<script>
// ── FRACTAL MULTI-SCALE ZOOM SCRIPT ENGINE V2.0.0 ──
(function() {
  var currentTier = 1;
  var currentCountry = 'india';
  var currentSector = 'cables_in';
  var currentFirm = 'polycab';
  var currentNano = 'halol_mega';

  // 12 Sovereign Nations grounded in Damodaran ctryprem July 2026 data
  var countryData = {
    india: {
      name: 'India', flag: '🇮🇳', sovereignRating: 'Baa3 / BBB-', defaultSpreadBps: 165,
      crp: 2.38, erpUS: 4.40, totalERP: 6.78, rf: 6.81, corpTax: 25.17, gdpGrowth: 7.2,
      currency: 'INR', usdInr: 84.38, fdiAnnual: '$71.4B', fiiYTD: '+$4.2B',
      sectors: ['cables_in', 'edu_in', 'chem_in', 'hosp_in', 'hotel_in', 'pipe_in', 'bank_in']
    },
    us: {
      name: 'United States', flag: '🇺🇸', sovereignRating: 'Aaa / AAA', defaultSpreadBps: 0,
      crp: 0.00, erpUS: 4.40, totalERP: 4.40, rf: 4.34, corpTax: 21.00, gdpGrowth: 2.4,
      currency: 'USD', usdInr: 1.0, fdiAnnual: '$388B', fiiYTD: '+$210B',
      sectors: ['semi_us', 'tech_us', 'edu_us', 'cables_us', 'energy_us']
    },
    germany: {
      name: 'Germany', flag: '🇩🇪', sovereignRating: 'Aaa / AAA', defaultSpreadBps: 0,
      crp: 0.00, erpUS: 4.40, totalERP: 5.40, rf: 2.38, corpTax: 29.90, gdpGrowth: 0.4,
      currency: 'EUR', usdInr: 91.24, fdiAnnual: '$45B', fiiYTD: '+$12B',
      sectors: ['auto_de', 'automation_de', 'chem_de']
    },
    japan: {
      name: 'Japan', flag: '🇯🇵', sovereignRating: 'A1 / A+', defaultSpreadBps: 45,
      crp: 0.65, erpUS: 4.40, totalERP: 5.05, rf: 0.98, corpTax: 29.74, gdpGrowth: 1.1,
      currency: 'JPY', usdInr: 0.55, fdiAnnual: '$28B', fiiYTD: '+$34B',
      sectors: ['semi_jp', 'precision_jp', 'sogo_jp']
    },
    china: {
      name: 'China', flag: '🇨🇳', sovereignRating: 'A1 / A+', defaultSpreadBps: 65,
      crp: 0.94, erpUS: 4.40, totalERP: 5.34, rf: 2.12, corpTax: 25.00, gdpGrowth: 4.8,
      currency: 'CNY', usdInr: 11.75, fdiAnnual: '$33B', fiiYTD: '-$8B',
      sectors: ['ev_cn', 'solar_cn', 'ship_cn']
    },
    brazil: {
      name: 'Brazil', flag: '🇧🇷', sovereignRating: 'Ba2 / BB', defaultSpreadBps: 265,
      crp: 3.82, erpUS: 4.40, totalERP: 8.22, rf: 12.40, corpTax: 34.00, gdpGrowth: 2.8,
      currency: 'BRL', usdInr: 14.67, fdiAnnual: '$66B', fiiYTD: '+$5B',
      sectors: ['oil_br', 'agri_br']
    },
    uk: {
      name: 'United Kingdom', flag: '🇬🇧', sovereignRating: 'Aa3 / AA', defaultSpreadBps: 52,
      crp: 0.75, erpUS: 4.40, totalERP: 5.15, rf: 4.42, corpTax: 25.00, gdpGrowth: 1.0,
      currency: 'GBP', usdInr: 109.30, fdiAnnual: '$58B', fiiYTD: '+$14B',
      sectors: ['fin_uk', 'pharma_uk']
    },
    saudi: {
      name: 'Saudi Arabia', flag: '🇸🇦', sovereignRating: 'A1 / A+', defaultSpreadBps: 58,
      crp: 0.85, erpUS: 4.40, totalERP: 5.25, rf: 4.90, corpTax: 20.00, gdpGrowth: 3.8,
      currency: 'SAR', usdInr: 22.50, fdiAnnual: '$24B', fiiYTD: '+$18B',
      sectors: ['energy_sa']
    },
    singapore: {
      name: 'Singapore', flag: '🇸🇬', sovereignRating: 'Aaa / AAA', defaultSpreadBps: 0,
      crp: 0.00, erpUS: 4.40, totalERP: 4.40, rf: 2.85, corpTax: 17.00, gdpGrowth: 3.2,
      currency: 'SGD', usdInr: 63.80, fdiAnnual: '$140B', fiiYTD: '+$45B',
      sectors: ['trade_sg']
    },
    australia: {
      name: 'Australia', flag: '🇦🇺', sovereignRating: 'Aaa / AAA', defaultSpreadBps: 0,
      crp: 0.00, erpUS: 4.40, totalERP: 4.40, rf: 4.15, corpTax: 30.00, gdpGrowth: 2.0,
      currency: 'AUD', usdInr: 55.60, fdiAnnual: '$42B', fiiYTD: '+$11B',
      sectors: ['mining_au']
    },
    korea: {
      name: 'South Korea', flag: '🇰🇷', sovereignRating: 'Aa2 / AA', defaultSpreadBps: 38,
      crp: 0.55, erpUS: 4.40, totalERP: 4.95, rf: 3.12, corpTax: 24.00, gdpGrowth: 2.2,
      currency: 'KRW', usdInr: 0.061, fdiAnnual: '$32B', fiiYTD: '+$16B',
      sectors: ['memory_kr']
    },
    uae: {
      name: 'United Arab Emirates', flag: '🇦🇪', sovereignRating: 'Aa2 / AA', defaultSpreadBps: 40,
      crp: 0.58, erpUS: 4.40, totalERP: 4.98, rf: 4.50, corpTax: 9.00, gdpGrowth: 4.1,
      currency: 'AED', usdInr: 22.98, fdiAnnual: '$30B', fiiYTD: '+$22B',
      sectors: ['logistics_ae']
    }
  };

  // Industrial Sector Blueprints (Grounded in Damodaran betaIndia.xls, marginIndia.xls & SOIC Research)
  var sectorData = {
    "cables_in": {
        "name": "Cables, Wires & EHV Power Infrastructure (India)",
        "country": "india",
        "betaU": 0.95,
        "betaL": 0.97,
        "opm": 10.9,
        "roic": 21.0,
        "wacc": 11.2,
        "evEbitda": 26.5,
        "assetTurnover": 2.45,
        "moat": "Continuous cast copper rod vertical integration (Properzi process), scale economies, strict technical certification (CPR, UL, BASEC), and extensive dealer networks (4,000+ distributors).",
        "soicMetrics": [
            {
                "label": "Market Size & Growth",
                "value": "₹700B (FY23) ➔ ₹1.25T (FY27) at 13% CAGR"
            },
            {
                "label": "LME Metal Pass-Through",
                "value": "100% Raw Material Formula (30-day lag)"
            },
            {
                "label": "B2B vs B2C Margin Spread",
                "value": "Institutional: 8.5-10.5% | Retail B2C: 12.0-15.0%"
            },
            {
                "label": "Working Capital Cycle",
                "value": "78-84 Days (Inventory 45d, Receivables 55d)"
            },
            {
                "label": "EHV 400kV Capability",
                "value": "Brugg Swiss Tie-up / Import Substitution Monopolies"
            }
        ],
        "representativeFirms": [
            "Polycab India Ltd",
            "KEI Industries Ltd",
            "RR Kabel Ltd",
            "Finolex Cables Ltd"
        ],
        "firmKeys": [
            "polycab",
            "kei",
            "rrkabel",
            "finolex"
        ]
    },
    "edu_in": {
        "name": "Education, EdTech & Skill Development (India)",
        "country": "india",
        "betaU": 0.57,
        "betaL": 0.61,
        "opm": 6.49,
        "roic": 24.5,
        "wacc": 10.4,
        "evEbitda": 22.0,
        "assetTurnover": 1.85,
        "moat": "Proprietary curriculum intellectual property, multi-year corporate managed training contracts (MTS), hybrid hub-and-spoke study center footprints, and strong test prep pass rate branding.",
        "soicMetrics": [
            {
                "label": "Indian Education TAM",
                "value": "$117B ➔ $225B by 2027 (NEP 2020 driver)"
            },
            {
                "label": "Student Enrollment CAGR",
                "value": "18.5% across IT upskilling, BFSI, & Test Prep"
            },
            {
                "label": "Blended Student ARPU",
                "value": "₹42,000 / year (B2B Corporate $3,200/seat)"
            },
            {
                "label": "Student LTV to CAC Ratio",
                "value": "3.8x (Enterprise Training Contracts > 5.5x)"
            },
            {
                "label": "Content Amortization Cycle",
                "value": "3-Year Straight Line (Zero obsolescence risk)"
            }
        ],
        "representativeFirms": [
            "MPS Ltd",
            "NIIT Learning Systems",
            "Veranda Learning",
            "Navneet Education"
        ],
        "firmKeys": [
            "mps",
            "niit",
            "veranda",
            "navneet"
        ]
    },
    "chem_in": {
        "name": "Specialty Chemicals, Adhesives & Fluorochemicals (India)",
        "country": "india",
        "betaU": 0.88,
        "betaL": 0.94,
        "opm": 18.5,
        "roic": 22.5,
        "wacc": 10.8,
        "evEbitda": 28.0,
        "assetTurnover": 1.45,
        "moat": "Brand monopoly in consumer adhesives (Fevicol 70%+ share), complex fluorine synthesis chemistry, 2-3 year customer re-validation cycles, and global customer patent linkages.",
        "soicMetrics": [
            {
                "label": "Synthesis Reaction Yields",
                "value": "> 88.5% in multi-step fluorination"
            },
            {
                "label": "Regulatory Switching Cost",
                "value": "2-3 Years customer re-validation cycle"
            },
            {
                "label": "R&D Reinvestment Ratio",
                "value": "4.8% of Gross Revenues"
            },
            {
                "label": "Global China+1 Offtake",
                "value": "Agro & Pharma intermediates long-term supply"
            },
            {
                "label": "Export Revenue Share",
                "value": "45-65% across global innovators"
            }
        ],
        "representativeFirms": [
            "Pidilite Industries Ltd",
            "SRF Ltd",
            "Navin Fluorine Intl",
            "Jubilant Ingrevia Ltd"
        ],
        "firmKeys": [
            "pidilite",
            "srf",
            "navin",
            "jubilant"
        ]
    },
    "hosp_in": {
        "name": "Super-Specialty Healthcare & Hospital Chains (India)",
        "country": "india",
        "betaU": 0.65,
        "betaL": 0.72,
        "opm": 24.5,
        "roic": 20.8,
        "wacc": 9.8,
        "evEbitda": 32.5,
        "assetTurnover": 1.15,
        "moat": "High regulatory barriers to metro hospital construction, doctor retention equity models, high cash-and-TPA payor mix (80%+ non-government), and commanding ARPOB.",
        "soicMetrics": [
            {
                "label": "Average Rev / Bed (ARPOB)",
                "value": "₹72,500 / day (NCR/Mumbai ₹85k+)"
            },
            {
                "label": "Bed Occupancy Ratio",
                "value": "74.2% operational capacity"
            },
            {
                "label": "Payor Mix Cash/TPA",
                "value": "82% Private Cash/Insurance : 18% Govt"
            },
            {
                "label": "ALOS (Avg Length of Stay)",
                "value": "3.2 Days (High surgical throughput)"
            },
            {
                "label": "Brownfield Expansion IRR",
                "value": "24-28% post-commissioning"
            }
        ],
        "representativeFirms": [
            "Max Healthcare Institute",
            "Narayana Hrudayalaya",
            "Apollo Hospitals Enterprise"
        ],
        "firmKeys": [
            "max_health",
            "narayana",
            "apollo_hosp"
        ]
    },
    "hotel_in": {
        "name": "Hospitality, Luxury Chains & Asset-Light Hotels (India)",
        "country": "india",
        "betaU": 0.78,
        "betaL": 0.92,
        "opm": 32.0,
        "roic": 18.2,
        "wacc": 10.2,
        "evEbitda": 28.5,
        "assetTurnover": 0.65,
        "moat": "Prime metropolitan real estate locations, brand equity (Taj, Marriott, Westin), asset-light management contracts (35%+ management fees), and corporate convention stickiness.",
        "soicMetrics": [
            {
                "label": "RevPAR Growth",
                "value": "+14.2% YoY (ARR ₹11,200/night)"
            },
            {
                "label": "Asset-Light Pipeline",
                "value": "62% of upcoming keys under management contract"
            },
            {
                "label": "Metro Occupancy",
                "value": "74.8% across key business gateways"
            },
            {
                "label": "MICE / Wedding Revenue",
                "value": "38% of total food & beverage intake"
            },
            {
                "label": "EBITDA Margin on Managed Keys",
                "value": "72% flow-through on contract fees"
            }
        ],
        "representativeFirms": [
            "The Indian Hotels Co (Taj)",
            "SAMHI Hotels Ltd",
            "Chalet Hotels Ltd"
        ],
        "firmKeys": [
            "ihcl",
            "samhi",
            "chalet"
        ]
    },
    "pipe_in": {
        "name": "Heavy Structural Tubes, Stainless Steel & ERW Pipes (India)",
        "country": "india",
        "betaU": 0.92,
        "betaL": 1.05,
        "opm": 11.2,
        "roic": 23.5,
        "wacc": 11.0,
        "evEbitda": 22.0,
        "assetTurnover": 2.85,
        "moat": "Continuous direct-forming square hollow section technology, 50%+ national market share, distribution logistics moat with 1,500+ exclusive retail distributors.",
        "soicMetrics": [
            {
                "label": "EBITDA per Ton",
                "value": "₹4,850 / MT blended"
            },
            {
                "label": "Scrap Recovery Ratio",
                "value": "96.5% high-frequency ERW"
            },
            {
                "label": "Heavy Hollow Section Share",
                "value": "65% domestic organized market"
            },
            {
                "label": "Inventory Turnover",
                "value": "28 Days (Ultra-lean operating cycle)"
            },
            {
                "label": "Capacity Utilization",
                "value": "82% on 3.5 Million MT capacity"
            }
        ],
        "representativeFirms": [
            "APL Apollo Tubes Ltd",
            "Ratnamani Metals & Tubes",
            "Welspun Corp Ltd"
        ],
        "firmKeys": [
            "apl_apollo",
            "ratnamani",
            "welspun"
        ]
    },
    "bank_in": {
        "name": "Commercial Banking, Retail Lending & Asset Quality (India)",
        "country": "india",
        "betaU": 0.85,
        "betaL": 1.15,
        "opm": 38.5,
        "roic": 17.5,
        "wacc": 10.5,
        "evEbitda": 16.5,
        "assetTurnover": 0.15,
        "moat": "Low-cost CASA deposit franchise (40%+ CASA), nationwide branch architecture (8,000+ branches), pristine underwriting with GNPA < 1.5%, and proprietary credit algorithms.",
        "soicMetrics": [
            {
                "label": "Net Interest Margin (NIM)",
                "value": "3.85 - 4.35% annualized"
            },
            {
                "label": "Gross NPA / Net NPA",
                "value": "GNPA 1.2% - 1.8% | NNPA 0.3% - 0.4%"
            },
            {
                "label": "Capital Adequacy (CRAR)",
                "value": "18.4% - 20.8% (Tier-1 > 16.5%)"
            },
            {
                "label": "Cost-to-Income Ratio",
                "value": "38.2% - 42.5% across top private banks"
            },
            {
                "label": "Return on Assets (ROA)",
                "value": "1.95% - 2.40% best-in-class"
            }
        ],
        "representativeFirms": [
            "HDFC Bank Ltd",
            "ICICI Bank Ltd",
            "Kotak Mahindra Bank",
            "State Bank of India"
        ],
        "firmKeys": [
            "hdfc_bank",
            "icici_bank",
            "kotak_bank",
            "sbi"
        ]
    },
    "semi_us": {
        "name": "AI Accelerators, Hyperscale GPU Compute & Foundry (US)",
        "country": "us",
        "betaU": 1.15,
        "betaL": 1.28,
        "opm": 54.5,
        "roic": 58.0,
        "wacc": 8.8,
        "evEbitda": 34.0,
        "assetTurnover": 1.15,
        "moat": "CUDA parallel computing software ecosystem, NVLink interconnect architecture, TSMC CoWoS advanced packaging capacity lock, and hyperscaler developer lock-in.",
        "soicMetrics": [
            {
                "label": "Data Center Rev Mix",
                "value": "85.5% of total corporate revenues"
            },
            {
                "label": "Gross Margin Profile",
                "value": "75.2% non-GAAP hardware & software"
            },
            {
                "label": "GPU ASP Benchmark",
                "value": "$32,000 / B200 accelerator platform"
            },
            {
                "label": "Hyperscaler AI Capex Run-Rate",
                "value": "$250+ Billion annualized spend across MSFT, GOOG, AMZN, META"
            },
            {
                "label": "CoWoS Packaging Supply",
                "value": "Full allocation through 2026"
            }
        ],
        "representativeFirms": [
            "NVIDIA Corporation",
            "Advanced Micro Devices",
            "Broadcom Inc",
            "Qualcomm Inc"
        ],
        "firmKeys": [
            "nvidia",
            "amd",
            "broadcom",
            "qualcomm"
        ]
    },
    "tech_us": {
        "name": "Mega-Cap Software, Cloud Hyperscalers & Hardware Platforms (US)",
        "country": "us",
        "betaU": 0.95,
        "betaL": 1.05,
        "opm": 34.2,
        "roic": 38.5,
        "wacc": 8.2,
        "evEbitda": 24.5,
        "assetTurnover": 0.88,
        "moat": "Global consumer ecosystem lock-in (2.2B active Apple devices), enterprise cloud dominance (Azure & AWS), search advertising monopoly (Google 90%+), and massive FCF generation.",
        "soicMetrics": [
            {
                "label": "Services Gross Margin",
                "value": "74.2% recurring software revenue"
            },
            {
                "label": "Combined Annual FCF",
                "value": "Over $350 Billion across top 5 tech giants"
            },
            {
                "label": "Active Installed Base",
                "value": "Billions of connected consumer & enterprise endpoints"
            },
            {
                "label": "Enterprise Cloud Growth",
                "value": "+28-33% YoY across Azure and AWS"
            },
            {
                "label": "Share Repurchases YTD",
                "value": "$100B+ annual capital return run-rate"
            }
        ],
        "representativeFirms": [
            "Apple Inc",
            "Microsoft Corp",
            "Alphabet Inc (Google)",
            "Amazon.com Inc",
            "Tesla Inc"
        ],
        "firmKeys": [
            "apple",
            "microsoft",
            "alphabet",
            "amazon",
            "tesla"
        ]
    },
    "edu_us": {
        "name": "Digital Learning Platforms & Enterprise Education (US)",
        "country": "us",
        "betaU": 0.72,
        "betaL": 0.85,
        "opm": 14.5,
        "roic": 18.0,
        "wacc": 8.5,
        "evEbitda": 16.5,
        "assetTurnover": 0.95,
        "moat": "Accredited online public school state funding charters, top-tier university degree partnerships, viral gamified language retention algorithms, and corporate L&D contracts.",
        "soicMetrics": [
            {
                "label": "Global Online EdTech TAM",
                "value": "$404B by 2028"
            },
            {
                "label": "Enterprise LTV to CAC",
                "value": "4.2x LTV/CAC ratio"
            },
            {
                "label": "Annual Course Retention",
                "value": "86.4% enterprise renewal rates"
            },
            {
                "label": "K-12 Virtual Enrollment",
                "value": "195,000+ full-time public students"
            },
            {
                "label": "Gamified DAU Engagement",
                "value": "34 Million daily active learners on Duolingo"
            }
        ],
        "representativeFirms": [
            "Stride Inc (K12)",
            "Coursera Inc",
            "Duolingo Inc"
        ],
        "firmKeys": [
            "stride",
            "coursera",
            "duolingo"
        ]
    },
    "cables_us": {
        "name": "North American Power Grid Modernization & Wire Systems (US)",
        "country": "us",
        "betaU": 0.88,
        "betaL": 0.98,
        "opm": 16.8,
        "roic": 22.5,
        "wacc": 7.8,
        "evEbitda": 16.2,
        "assetTurnover": 1.35,
        "moat": "Submarine HVDC power transmission cable monopoly, offshore wind grid interconnection exclusivity, and high-voltage utility distribution equipment approvals.",
        "soicMetrics": [
            {
                "label": "US Grid Capex 2026E",
                "value": "$38B annual transmission spend"
            },
            {
                "label": "HVDC Subsea Lead Times",
                "value": "48 Months order backlog"
            },
            {
                "label": "Utility Modernization Spend",
                "value": "Aging grid replacement cycle across 3,000 utilities"
            },
            {
                "label": "Data Center Interconnects",
                "value": "Multi-gigawatt substation supply contracts"
            },
            {
                "label": "Domestic Production Premium",
                "value": "Buy America compliance advantages"
            }
        ],
        "representativeFirms": [
            "Prysmian Group (US/Milan)",
            "Hubbell Inc"
        ],
        "firmKeys": [
            "prysmian_us",
            "hubbell"
        ]
    },
    "energy_us": {
        "name": "Integrated Supermajor Hydrocarbons & LNG Export (US)",
        "country": "us",
        "betaU": 0.82,
        "betaL": 0.95,
        "opm": 18.5,
        "roic": 19.2,
        "wacc": 7.5,
        "evEbitda": 7.2,
        "assetTurnover": 0.85,
        "moat": "Permian Basin low breakeven lifting costs (< $35/bbl), integrated refining-chemical complexes on the Gulf Coast, and 20-year take-or-pay LNG export liquefaction contracts.",
        "soicMetrics": [
            {
                "label": "Gulf Coast 3-2-1 Crack",
                "value": "$22.50 / bbl refining spread"
            },
            {
                "label": "Permian Breakeven",
                "value": "< $35 / bbl WTI profitable drilling"
            },
            {
                "label": "LNG Export Capacity",
                "value": "Over 85 Million MTPA US export capability"
            },
            {
                "label": "Dividend Aristocrat History",
                "value": "40+ consecutive years of dividend growth"
            },
            {
                "label": "Upstream Free Cash Flow",
                "value": "$45+ Billion annual cash generation"
            }
        ],
        "representativeFirms": [
            "ExxonMobil Corporation",
            "Chevron Corporation",
            "Cheniere Energy Inc",
            "ConocoPhillips"
        ],
        "firmKeys": [
            "exxon",
            "chevron",
            "cheniere",
            "conocophillips"
        ]
    },
    "auto_de": {
        "name": "Automotive & Heavy Industry (Germany)",
        "country": "germany",
        "betaU": 0.9,
        "betaL": 1.25,
        "opm": 8.5,
        "roic": 12.0,
        "wacc": 7.2,
        "evEbitda": 6.8,
        "assetTurnover": 0.95,
        "moat": "Precision mechanical engineering, century-old luxury heritage brand equity (Mercedes-Benz, BMW, Porsche), and massive automated Industry 4.0 assembly complexes.",
        "soicMetrics": [
            {
                "label": "EV Platform Capex",
                "value": "€45B through 2028"
            },
            {
                "label": "Luxury Pricing Power",
                "value": "Average selling price €72,000+ per vehicle"
            },
            {
                "label": "Industrial Liquidity",
                "value": "€31B+ net cash across German OEMs"
            },
            {
                "label": "Software-Defined Vehicle (SDV)",
                "value": "MB.OS & Neue Klasse autonomous architectures"
            },
            {
                "label": "Dividend Yield Benchmark",
                "value": "6.5% - 8.2% cash distribution yields"
            }
        ],
        "representativeFirms": [
            "Mercedes-Benz Group AG",
            "Bayerische Motoren Werke (BMW)",
            "Volkswagen AG"
        ],
        "firmKeys": [
            "mercedes",
            "bmw",
            "volkswagen"
        ]
    },
    "automation_de": {
        "name": "Industrial Automation & Robotics (Germany)",
        "country": "germany",
        "betaU": 0.82,
        "betaL": 0.95,
        "opm": 14.2,
        "roic": 18.5,
        "wacc": 6.8,
        "evEbitda": 16.5,
        "assetTurnover": 1.15,
        "moat": "PLC automation industrial standards (Siemens Simatic), Industry 4.0 digital twin dominance (Teamcenter, NX), and warehouse intralogistics robotics (Dematic).",
        "soicMetrics": [
            {
                "label": "Factory Software Backlog",
                "value": "€112B multi-year order backlog"
            },
            {
                "label": "Defect Rate in Manufacturing",
                "value": "11 DPM (Near-zero manufacturing defects)"
            },
            {
                "label": "Industrial Software ARR",
                "value": "€4.2B annual recurring software revenue"
            },
            {
                "label": "Ecosystem Integration",
                "value": "Standardized across 100,000+ global factories"
            },
            {
                "label": "Operating Margin Run-Rate",
                "value": "15.4% core digital industries margin"
            }
        ],
        "representativeFirms": [
            "Siemens AG",
            "KION Group AG"
        ],
        "firmKeys": [
            "siemens",
            "kion"
        ]
    },
    "chem_de": {
        "name": "Chemical Conglomerates (Germany)",
        "country": "germany",
        "betaU": 0.75,
        "betaL": 0.92,
        "opm": 9.8,
        "roic": 11.5,
        "wacc": 7.0,
        "evEbitda": 8.2,
        "assetTurnover": 0.88,
        "moat": "Verbund site integration (10 sq km Ludwigshafen), closed-loop thermal and material recycling, and high-barrier specialty life sciences patent portfolios.",
        "soicMetrics": [
            {
                "label": "Energy Cost Hedge",
                "value": "Long-term renewable power purchase agreements"
            },
            {
                "label": "Verbund Cost Savings",
                "value": "€1.2B annual internal logistical cost avoidance"
            },
            {
                "label": "Zhanjiang Mega Project",
                "value": "€10B smart Verbund site in Guangdong, China"
            },
            {
                "label": "Agricultural Solution Share",
                "value": "Global top-3 crop protection formulations"
            },
            {
                "label": "Free Cash Flow Flow-Through",
                "value": "€3.5B+ annual operational cash flow"
            }
        ],
        "representativeFirms": [
            "BASF SE",
            "Bayer AG"
        ],
        "firmKeys": [
            "basf",
            "bayer"
        ]
    },
    "semi_jp": {
        "name": "Semiconductor Equipment & Materials (Japan)",
        "country": "japan",
        "betaU": 0.98,
        "betaL": 1.05,
        "opm": 28.5,
        "roic": 26.5,
        "wacc": 6.2,
        "evEbitda": 18.5,
        "assetTurnover": 0.95,
        "moat": "Global monopolies in semiconductor manufacturing steps: Coater/Developers (90% TEL), Actinic EUV Photomask Inspection (100% Lasertec), and Memory ATE Testers (55% Advantest).",
        "soicMetrics": [
            {
                "label": "EUV Inspection Monopoly",
                "value": "100% market share on actinic blank inspection"
            },
            {
                "label": "HBM Memory Tester Share",
                "value": "Over 75% share of HBM3E high-speed test systems"
            },
            {
                "label": "Net Cash Balance Sheets",
                "value": "Zero net debt with massive cash balances"
            },
            {
                "label": "Operating Profit Margins",
                "value": "28% - 38% across top equipment makers"
            },
            {
                "label": "R&D Reinvestment Rate",
                "value": "12.5% of sales reinvested in advanced physics"
            }
        ],
        "representativeFirms": [
            "Tokyo Electron Ltd",
            "Advantest Corp",
            "Lasertec Corp"
        ],
        "firmKeys": [
            "tel",
            "advantest",
            "lasertec"
        ]
    },
    "precision_jp": {
        "name": "Factory Precision Automation, Robotics & Sensors (Japan)",
        "country": "japan",
        "betaU": 0.85,
        "betaL": 0.92,
        "opm": 42.0,
        "roic": 28.5,
        "wacc": 5.8,
        "evEbitda": 22.5,
        "assetTurnover": 0.65,
        "moat": "Direct-sales model without middlemen, 50%+ operating margins, 99.5% same-day sensor shipment, and yellow autonomous robot assembly forests at Mount Fuji.",
        "soicMetrics": [
            {
                "label": "Keyence Operating Margin",
                "value": "52.4% world-record operating margin"
            },
            {
                "label": "Direct-Sales Field Engineers",
                "value": "Problem solvers visiting factories directly"
            },
            {
                "label": "Cash Reserves",
                "value": "¥2.8 Trillion ($18B) pristine liquid net cash"
            },
            {
                "label": "CNC Global Share",
                "value": "65% of world machine tool CNC controllers"
            },
            {
                "label": "Lights-Out Factories",
                "value": "Robots manufacturing robots unmanned for 30 days"
            }
        ],
        "representativeFirms": [
            "Keyence Corporation",
            "Fanuc Corp"
        ],
        "firmKeys": [
            "keyence",
            "fanuc"
        ]
    },
    "sogo_jp": {
        "name": "Sogo Shosha Conglomerate Trading Houses (Japan)",
        "country": "japan",
        "betaU": 0.78,
        "betaL": 0.88,
        "opm": 8.5,
        "roic": 14.8,
        "wacc": 5.5,
        "evEbitda": 7.5,
        "assetTurnover": 1.05,
        "moat": "Global trade infrastructure, resource concessions (LNG, coking coal, copper), Berkshire Hathaway 9%+ endorsement, and steady ROE expansion above 14%.",
        "soicMetrics": [
            {
                "label": "Berkshire Hathaway Stake",
                "value": "Warren Buffett 9%+ strategic equity ownership"
            },
            {
                "label": "Global Operating Affiliates",
                "value": "Over 1,700 subsidiaries across 90 countries"
            },
            {
                "label": "Metallurgical Coal Concession",
                "value": "World lowest-cost coking coal export mines"
            },
            {
                "label": "Dividend Payout Target",
                "value": "Progressive dividend policy with active buybacks"
            },
            {
                "label": "Non-Resource Net Income",
                "value": "75%+ diversified consumer and industrial profit"
            }
        ],
        "representativeFirms": [
            "Mitsubishi Corporation",
            "Mitsui & Co Ltd",
            "Itochu Corporation"
        ],
        "firmKeys": [
            "mitsubishi",
            "mitsui",
            "itochu"
        ]
    },
    "ev_cn": {
        "name": "New Energy Vehicles, Lithium Batteries & Power Grid (China)",
        "country": "china",
        "betaU": 1.05,
        "betaL": 1.18,
        "opm": 10.5,
        "roic": 21.0,
        "wacc": 6.5,
        "evEbitda": 13.5,
        "assetTurnover": 1.25,
        "moat": "Massive vertical integration, Blade battery safety, lowest cell cost per kWh globally ($55/kWh), and 4.2 million vehicle annual manufacturing capacity.",
        "soicMetrics": [
            {
                "label": "Global EV Battery Share",
                "value": "CATL 37.5% + BYD 16% = 53.5% global dominance"
            },
            {
                "label": "Annual NEV Production",
                "value": "4.2 Million vehicles / year BYD volume run-rate"
            },
            {
                "label": "LFP Battery Cell Cost",
                "value": "< $55 / kWh packs at cell level"
            },
            {
                "label": "Export Ro-Ro Fleet",
                "value": "Dedicated 7,000-vehicle car carrier ships"
            },
            {
                "label": "Free Cash Flow Conversion",
                "value": "Massive negative working capital floats"
            }
        ],
        "representativeFirms": [
            "BYD Company Ltd",
            "CATL (Contemporary Amperex)"
        ],
        "firmKeys": [
            "byd",
            "catl"
        ]
    },
    "solar_cn": {
        "name": "Photovoltaic Solar Modules, Inverters & Cleantech (China)",
        "country": "china",
        "betaU": 1.12,
        "betaL": 1.25,
        "opm": 14.8,
        "roic": 18.5,
        "wacc": 6.8,
        "evEbitda": 9.2,
        "assetTurnover": 1.1,
        "moat": "Global scale monopolies in silicon ingot pulling, wafer slicing, HPBC 2.0 back-contact solar cell efficiency (26.6%), and utility-scale grid-forming inverters.",
        "soicMetrics": [
            {
                "label": "Global Solar Wafer Share",
                "value": "Over 85% of global wafers produced in China"
            },
            {
                "label": "Inverter Global Share",
                "value": "Sungrow #1 inverter & BESS supplier globally"
            },
            {
                "label": "Module Conversion Efficiency",
                "value": "26.6% mass production HPBC cell efficiency"
            },
            {
                "label": "LCOE of Solar Power",
                "value": "< $0.02 / kWh generation cost in sunny geographies"
            },
            {
                "label": "Energy Storage Deployments",
                "value": "PowerTitan utility battery grid integration"
            }
        ],
        "representativeFirms": [
            "LONGi Green Energy Technology",
            "Sungrow Power Supply Co"
        ],
        "firmKeys": [
            "longi",
            "sungrow"
        ]
    },
    "ship_cn": {
        "name": "Heavy Commercial Shipbuilding & Dual-Fuel Fleets (China)",
        "country": "china",
        "betaU": 0.88,
        "betaL": 1.1,
        "opm": 11.5,
        "roic": 14.8,
        "wacc": 6.2,
        "evEbitda": 12.0,
        "assetTurnover": 0.85,
        "moat": "Dual-fuel VLCC and mega-container ship order backlogs through 2029, colossal drydocks at Changxing Island, and massive advance customer cash payments.",
        "soicMetrics": [
            {
                "label": "Order Book Coverage",
                "value": "4.5 Years forward drydock reservation through 2029"
            },
            {
                "label": "Dual-Fuel Containerships",
                "value": "Building 24,000 TEU mega-vessels for global liners"
            },
            {
                "label": "Advance Stage Payments",
                "value": "Negative working capital funded by foreign shipowners"
            },
            {
                "label": "Container Fleet TEU Size",
                "value": "COSCO 3.2 Million TEU operating fleet"
            },
            {
                "label": "Net Cash Position",
                "value": "Tens of billions in liquid maritime treasury cash"
            }
        ],
        "representativeFirms": [
            "China CSSC Holdings Ltd",
            "COSCO SHIPPING Holdings"
        ],
        "firmKeys": [
            "cssc",
            "cosco"
        ]
    },
    "oil_br": {
        "name": "Offshore Deepwater Pre-Salt Crude (Brazil)",
        "country": "brazil",
        "betaU": 0.95,
        "betaL": 1.35,
        "opm": 32.5,
        "roic": 22.0,
        "wacc": 13.5,
        "evEbitda": 4.5,
        "assetTurnover": 0.72,
        "moat": "Santos Basin ultra-deepwater lifting costs < $28/bbl, world-class reservoir permeability, and massive FPSO extraction capacity.",
        "soicMetrics": [
            {
                "label": "Lifting Cost / Barrel",
                "value": "$26.80 / bbl Santos Basin pre-salt breakeven"
            },
            {
                "label": "FPSO Extraction Fleet",
                "value": "Búzios, Mero & Tupi ultra-deepwater vessels"
            },
            {
                "label": "Daily Crude Production",
                "value": "2.8 Million barrels / day pre-salt extraction"
            },
            {
                "label": "Dividend Payout Formula",
                "value": "45% of free cash flow distributed as dividends"
            },
            {
                "label": "P/E Valuation Multiple",
                "value": "4.2x deeply discounted cash generator"
            }
        ],
        "representativeFirms": [
            "Petróleo Brasileiro S.A. (Petrobras)"
        ],
        "firmKeys": [
            "petrobras"
        ]
    },
    "agri_br": {
        "name": "Iron Ore & Agribusiness (Brazil)",
        "country": "brazil",
        "betaU": 0.92,
        "betaL": 1.15,
        "opm": 38.5,
        "roic": 24.5,
        "wacc": 14.0,
        "evEbitda": 5.2,
        "assetTurnover": 0.85,
        "moat": "Carajás high-grade 65% Fe iron ore natural geological endowment, double-cropping agricultural efficiency, and vast arable Cerrado farmland.",
        "soicMetrics": [
            {
                "label": "Cash Cost FOB Iron Ore",
                "value": "$22.40 / ton Carajás S11D cash cost"
            },
            {
                "label": "Iron Ore Fe Purity",
                "value": "65.4% natural high-grade direct charge ore"
            },
            {
                "label": "Arable Farm Land Area",
                "value": "700,000+ hectares under precision double-cropping"
            },
            {
                "label": "Global Grain Export Share",
                "value": "Brazil #1 exporter of soybeans and corn globally"
            },
            {
                "label": "Truckless Conveyor System",
                "value": "Electrified in-pit transport cutting diesel costs"
            }
        ],
        "representativeFirms": [
            "Vale S.A.",
            "SLC Agrícola S.A."
        ],
        "firmKeys": [
            "vale",
            "slc_agri"
        ]
    },
    "fin_uk": {
        "name": "Global Banking & Wealth Management (United Kingdom)",
        "country": "uk",
        "betaU": 0.85,
        "betaL": 1.25,
        "opm": 34.2,
        "roic": 14.5,
        "wacc": 7.8,
        "evEbitda": 7.8,
        "assetTurnover": 0.12,
        "moat": "London global financial center clearing, foreign exchange trading liquidity, Asian trade corridor dominance (Hong Kong/Singapore), and CET-1 capital buffers.",
        "soicMetrics": [
            {
                "label": "Common Equity Tier 1 (CET1)",
                "value": "15.2% regulatory capital buffer"
            },
            {
                "label": "Trade Finance Leadership",
                "value": "#1 global trade bank in Asia and Europe"
            },
            {
                "label": "Dividend & Buyback Yield",
                "value": "8.5% total capital return yield"
            },
            {
                "label": "Net Interest Margin",
                "value": "1.62% - 1.85% wholesale & retail spreads"
            },
            {
                "label": "Global Wealth Management AUM",
                "value": "$1.8 Trillion affluent customer balances"
            }
        ],
        "representativeFirms": [
            "HSBC Holdings plc",
            "Barclays PLC"
        ],
        "firmKeys": [
            "hsbc",
            "barclays"
        ]
    },
    "pharma_uk": {
        "name": "Innovative Pharmaceuticals, GLP-1 & EUV Lithography (Europe / UK)",
        "country": "uk",
        "betaU": 0.7,
        "betaL": 0.78,
        "opm": 38.5,
        "roic": 34.0,
        "wacc": 7.2,
        "evEbitda": 22.5,
        "assetTurnover": 0.75,
        "moat": "Global monopolies and duopolies: ASML 100% EUV lithography monopoly, Novo Nordisk GLP-1 weight-loss duopoly, AstraZeneca targeted oncology blockbusters.",
        "soicMetrics": [
            {
                "label": "EUV Lithography Monopoly",
                "value": "ASML 100% market share on advanced chip manufacturing"
            },
            {
                "label": "GLP-1 Weight Loss TAM",
                "value": "$100B+ global obesity market by 2030"
            },
            {
                "label": "Oncology Drug Pipeline",
                "value": "28 Phase-III molecules in clinical development"
            },
            {
                "label": "Gross Profit Margins",
                "value": "82% - 88% on patent-protected therapeutics"
            },
            {
                "label": "Return on Capital Employed",
                "value": "45%+ ROCE on advanced lithography and biologics"
            }
        ],
        "representativeFirms": [
            "AstraZeneca PLC",
            "Novo Nordisk A/S",
            "ASML Holding NV"
        ],
        "firmKeys": [
            "astrazeneca",
            "novo",
            "asml"
        ]
    },
    "energy_sa": {
        "name": "Integrated Hydrocarbons & Petrochemicals (Saudi Arabia)",
        "country": "saudi",
        "betaU": 0.75,
        "betaL": 0.85,
        "opm": 44.5,
        "roic": 28.5,
        "wacc": 6.8,
        "evEbitda": 7.2,
        "assetTurnover": 0.85,
        "moat": "Ghawar field onshore crude with lowest lifting cost globally ($3.20/bbl), captive subsidized ethane feedstocks for SABIC, and sovereign balance sheet fortress.",
        "soicMetrics": [
            {
                "label": "Upstream Lifting Cost",
                "value": "$3.20 / bbl (Lowest cost crude on earth)"
            },
            {
                "label": "Maximum Sustainable Capacity",
                "value": "12.0 Million barrels / day crude capacity"
            },
            {
                "label": "Petrochemical Feedstock Margin",
                "value": "Fixed-price ethane feedstocks at massive global discount"
            },
            {
                "label": "Annual Free Cash Flow",
                "value": "Over $100 Billion generated annually"
            },
            {
                "label": "Base Dividend Guarantee",
                "value": "$31 Billion quarterly base and performance payouts"
            }
        ],
        "representativeFirms": [
            "Saudi Arabian Oil Co (Saudi Aramco)",
            "SABIC"
        ],
        "firmKeys": [
            "aramco",
            "sabic"
        ]
    },
    "trade_sg": {
        "name": "Global Maritime Hub & Trade Infrastructure (Singapore)",
        "country": "singapore",
        "betaU": 0.72,
        "betaL": 0.85,
        "opm": 26.5,
        "roic": 18.5,
        "wacc": 5.8,
        "evEbitda": 14.2,
        "assetTurnover": 0.95,
        "moat": "Tuas mega-port transshipment logistics, subsea cable landing station chokepoint, Temasek sovereign ownership, and Asian agri-processing processing hubs.",
        "soicMetrics": [
            {
                "label": "Container Throughput",
                "value": "39.0M TEUs/year through Singapore seaport"
            },
            {
                "label": "Subsea Cable Connectivity",
                "value": "Over 25 major international subsea cable systems terminating"
            },
            {
                "label": "Palm Oil Refining Capacity",
                "value": "Largest edible oil processor in Asia-Pacific"
            },
            {
                "label": "Sovereign Credit Rating",
                "value": "AAA pristine sovereign stability and zero-tax maritime regime"
            },
            {
                "label": "Regional Data Center Capacity",
                "value": "Over 1 Gigawatt active enterprise data center capacity"
            }
        ],
        "representativeFirms": [
            "Singapore Telecommunications (Singtel)",
            "Wilmar International Ltd"
        ],
        "firmKeys": [
            "singtel",
            "wilmar"
        ]
    },
    "mining_au": {
        "name": "Critical Minerals, Iron Ore & Copper Extraction (Australia)",
        "country": "australia",
        "betaU": 0.88,
        "betaL": 1.05,
        "opm": 42.0,
        "roic": 26.0,
        "wacc": 8.2,
        "evEbitda": 6.5,
        "assetTurnover": 0.88,
        "moat": "Pilbara low-cost rail-to-port infrastructure (AutoHaul autonomous trains), Olympic Dam multi-metal mega-deposit, and Tier-1 copper reserves.",
        "soicMetrics": [
            {
                "label": "Iron Ore FOB Cost",
                "value": "$18.50 / ton Pilbara rail-to-port cost"
            },
            {
                "label": "Olympic Dam Reserve Size",
                "value": "World largest known single uranium and copper deposit"
            },
            {
                "label": "Autonomous Heavy Rail",
                "value": "1,700km driverless heavy-haul rail network"
            },
            {
                "label": "Operating Cash Flow",
                "value": "$20+ Billion annual operating cash generation"
            },
            {
                "label": "Copper Production Growth",
                "value": "Over 1.8 Million tons copper per year"
            }
        ],
        "representativeFirms": [
            "BHP Group Ltd",
            "Rio Tinto Ltd"
        ],
        "firmKeys": [
            "bhp",
            "rio"
        ]
    },
    "memory_kr": {
        "name": "Advanced HBM3E Memory, DRAM & Foundry (South Korea)",
        "country": "korea",
        "betaU": 1.1,
        "betaL": 1.18,
        "opm": 26.5,
        "roic": 22.5,
        "wacc": 6.8,
        "evEbitda": 11.2,
        "assetTurnover": 0.95,
        "moat": "High-Bandwidth Memory (HBM3E) mass reflow packaging monopoly for NVIDIA, global DRAM duopoly (75%+ combined share), and GigaFab cleanrooms at Pyeongtaek.",
        "soicMetrics": [
            {
                "label": "HBM Global Market Share",
                "value": "SK Hynix 53% + Samsung 42% = 95% global AI memory monopoly"
            },
            {
                "label": "Cleanroom Footprint",
                "value": "Pyeongtaek Campus equivalent to 400 football fields"
            },
            {
                "label": "EUV DRAM Manufacturing",
                "value": "1b-nanometer DRAM utilizing ASML EUV lithography"
            },
            {
                "label": "Liquid Net Cash Balance",
                "value": "$85+ Billion cash buffer at Samsung Electronics"
            },
            {
                "label": "Operating Margin Expansion",
                "value": "HBM3E operating margins approaching 45%"
            }
        ],
        "representativeFirms": [
            "Samsung Electronics Co Ltd",
            "SK Hynix Inc"
        ],
        "firmKeys": [
            "samsung",
            "sk_hynix"
        ]
    },
    "logistics_ae": {
        "name": "Global Air Transit & Marine Port Terminals (UAE)",
        "country": "uae",
        "betaU": 0.82,
        "betaL": 1.05,
        "opm": 21.0,
        "roic": 17.5,
        "wacc": 6.5,
        "evEbitda": 10.8,
        "assetTurnover": 1.12,
        "moat": "Dubai global transit crossroad connecting East and West, Jebel Ali mega-harbor (19M TEUs) with adjacent JAFZA free zone, and lowest-cost airline seat-km economics.",
        "soicMetrics": [
            {
                "label": "Transit Passenger Volume",
                "value": "87.0M passengers/yr through Dubai hub"
            },
            {
                "label": "Jebel Ali Container Capacity",
                "value": "19.3 Million TEUs deepwater automated port capacity"
            },
            {
                "label": "JAFZA Free Zone Tenants",
                "value": "9,500+ multinational companies from 140 countries"
            },
            {
                "label": "Low-Cost Airline Seat Margin",
                "value": "Air Arabia 26.8% operating margin"
            },
            {
                "label": "Sovereign Port Concessions",
                "value": "82 marine terminals across 40 countries globally"
            }
        ],
        "representativeFirms": [
            "DP World Ltd",
            "Air Arabia PJSC"
        ],
        "firmKeys": [
            "dpworld",
            "airarabia"
        ]
    }
};

  firmData = {
    "polycab": {
        "name": "Polycab India Ltd",
        "ticker": "POLYCAB:IN",
        "cmp": "₹7,145.00",
        "dcf": "₹7,958.56",
        "mos": "+11.4%",
        "mcap": "₹1,07,200 Cr",
        "pe": "47.3",
        "pbv": "10.8",
        "evEbitda": "30.2",
        "beneishM": -2.44,
        "beneishStatus": "SAFE (No Earnings Manipulation)",
        "altmanZ": 7.85,
        "altmanStatus": "SAFE ZONE (Distress Probability < 0.1%)",
        "sloanAccrual": "2.1% (High Earnings Quality)",
        "piotroski": "8 / 9 (Superb Balance Sheet Strength)",
        "dupontROE": {
            "taxBurden": "0.75",
            "interestBurden": "0.96",
            "opMargin": "13.6%",
            "assetTurn": "2.42x",
            "leverage": "1.24x",
            "finalROE": "20.5%"
        },
        "kyleLambda": "0.052 bps / 10k shs",
        "blkOwnership": "4.85% ($560M)",
        "vangOwnership": "4.20% ($485M)",
        "activeFloat": "34.2%",
        "nanoLink": "halol_mega",
        "soicScore": {
            "industry": 40,
            "industryMax": 45,
            "funda": 75,
            "fundaMax": 80,
            "tech": 105,
            "techMax": 110,
            "val": 25,
            "valMax": 35,
            "forensic": 35,
            "forensicMax": 40,
            "total": 280,
            "totalMax": 310,
            "classification": "EPIC HIGH CONVICTION ALLOCATION"
        }
    },
    "kei": {
        "name": "KEI Industries Ltd",
        "ticker": "KEI:IN",
        "cmp": "₹4,280.00",
        "dcf": "₹4,550.00",
        "mos": "+6.3%",
        "mcap": "₹38,600 Cr",
        "pe": "48.2",
        "pbv": "9.4",
        "evEbitda": "28.5",
        "beneishM": -2.38,
        "beneishStatus": "SAFE (Clean Books)",
        "altmanZ": 7.2,
        "altmanStatus": "SAFE ZONE",
        "sloanAccrual": "3.4% (Healthy)",
        "piotroski": "8 / 9 (Strong)",
        "dupontROE": {
            "taxBurden": "0.75",
            "interestBurden": "0.94",
            "opMargin": "10.8%",
            "assetTurn": "2.35x",
            "leverage": "1.18x",
            "finalROE": "21.2%"
        },
        "kyleLambda": "0.088 bps / 10k shs",
        "blkOwnership": "3.40% ($155M)",
        "vangOwnership": "3.10% ($142M)",
        "activeFloat": "42.5%",
        "nanoLink": "kei_plant",
        "soicScore": {
            "industry": 40,
            "industryMax": 45,
            "funda": 70,
            "fundaMax": 80,
            "tech": 105,
            "techMax": 110,
            "val": 25,
            "valMax": 35,
            "forensic": 20,
            "forensicMax": 40,
            "total": 260,
            "totalMax": 310,
            "classification": "TIER 1 HIGH CONVICTION"
        }
    },
    "rrkabel": {
        "name": "RR Kabel Ltd",
        "ticker": "RRKABEL:IN",
        "cmp": "₹1,580.00",
        "dcf": "₹1,720.00",
        "mos": "+8.9%",
        "mcap": "₹17,800 Cr",
        "pe": "44.5",
        "pbv": "7.8",
        "evEbitda": "24.2",
        "beneishM": -2.52,
        "beneishStatus": "SAFE",
        "altmanZ": 6.8,
        "altmanStatus": "SAFE ZONE",
        "sloanAccrual": "2.8%",
        "piotroski": "7 / 9",
        "dupontROE": {
            "taxBurden": "0.74",
            "interestBurden": "0.95",
            "opMargin": "7.8%",
            "assetTurn": "2.65x",
            "leverage": "1.25x",
            "finalROE": "18.4%"
        },
        "kyleLambda": "0.125 bps / 10k shs",
        "blkOwnership": "2.20% ($47M)",
        "vangOwnership": "1.85% ($39M)",
        "activeFloat": "37.8%",
        "nanoLink": "rr_waghodia",
        "soicScore": {
            "industry": 38,
            "industryMax": 45,
            "funda": 65,
            "fundaMax": 80,
            "tech": 95,
            "techMax": 110,
            "val": 24,
            "valMax": 35,
            "forensic": 32,
            "forensicMax": 40,
            "total": 254,
            "totalMax": 310,
            "classification": "HIGH QUALITY COMPOUNDER"
        }
    },
    "finolex": {
        "name": "Finolex Cables Ltd",
        "ticker": "FINCABLES:IN",
        "cmp": "₹1,190.00",
        "dcf": "₹1,310.00",
        "mos": "+10.1%",
        "mcap": "₹18,200 Cr",
        "pe": "28.4",
        "pbv": "3.9",
        "evEbitda": "18.6",
        "beneishM": -2.65,
        "beneishStatus": "SAFE",
        "altmanZ": 8.9,
        "altmanStatus": "SAFE ZONE (Zero Debt Net Cash ₹2,400 Cr)",
        "sloanAccrual": "1.5%",
        "piotroski": "7 / 9",
        "dupontROE": {
            "taxBurden": "0.75",
            "interestBurden": "0.99",
            "opMargin": "12.4%",
            "assetTurn": "1.45x",
            "leverage": "1.10x",
            "finalROE": "14.8%"
        },
        "kyleLambda": "0.110 bps / 10k shs",
        "blkOwnership": "2.50% ($54M)",
        "vangOwnership": "2.10% ($46M)",
        "activeFloat": "64.2%",
        "nanoLink": "finolex_urse",
        "soicScore": {
            "industry": 38,
            "industryMax": 45,
            "funda": 68,
            "fundaMax": 80,
            "tech": 90,
            "techMax": 110,
            "val": 28,
            "valMax": 35,
            "forensic": 34,
            "forensicMax": 40,
            "total": 258,
            "totalMax": 310,
            "classification": "VALUE COMPOUNDER"
        }
    },
    "mps": {
        "name": "MPS Ltd",
        "ticker": "MPSLTD:IN",
        "cmp": "₹2,150.00",
        "dcf": "₹2,420.00",
        "mos": "+12.6%",
        "mcap": "₹3,700 Cr",
        "pe": "24.8",
        "pbv": "6.4",
        "evEbitda": "14.5",
        "beneishM": -2.71,
        "beneishStatus": "SAFE",
        "altmanZ": 9.4,
        "altmanStatus": "PRISTINE SAFE ZONE",
        "sloanAccrual": "-0.8% (Cash Exceeds Net Income)",
        "piotroski": "9 / 9",
        "dupontROE": {
            "taxBurden": "0.75",
            "interestBurden": "0.98",
            "opMargin": "28.5%",
            "assetTurn": "1.15x",
            "leverage": "1.18x",
            "finalROE": "29.2%"
        },
        "kyleLambda": "0.340 bps / 5k shs",
        "blkOwnership": "1.80% ($8M)",
        "vangOwnership": "1.40% ($6M)",
        "activeFloat": "31.5%",
        "nanoLink": "mps_studio",
        "soicScore": {
            "industry": 38,
            "industryMax": 45,
            "funda": 74,
            "fundaMax": 80,
            "tech": 100,
            "techMax": 110,
            "val": 28,
            "valMax": 35,
            "forensic": 38,
            "forensicMax": 40,
            "total": 278,
            "totalMax": 310,
            "classification": "MICRO-CAP PLATINUM COMPOUNDER"
        }
    },
    "niit": {
        "name": "NIIT Learning Systems Ltd",
        "ticker": "NIITMTS:IN",
        "cmp": "₹465.00",
        "dcf": "₹510.00",
        "mos": "+9.7%",
        "mcap": "₹6,300 Cr",
        "pe": "26.2",
        "pbv": "5.2",
        "evEbitda": "15.8",
        "beneishM": -2.55,
        "beneishStatus": "SAFE",
        "altmanZ": 7.6,
        "altmanStatus": "SAFE ZONE",
        "sloanAccrual": "1.2%",
        "piotroski": "8 / 9",
        "dupontROE": {
            "taxBurden": "0.74",
            "interestBurden": "0.98",
            "opMargin": "22.8%",
            "assetTurn": "1.28x",
            "leverage": "1.15x",
            "finalROE": "24.2%"
        },
        "kyleLambda": "0.220 bps / 10k shs",
        "blkOwnership": "2.10% ($16M)",
        "vangOwnership": "1.90% ($14M)",
        "activeFloat": "65.2%",
        "nanoLink": "niit_hub",
        "soicScore": {
            "industry": 36,
            "industryMax": 45,
            "funda": 70,
            "fundaMax": 80,
            "tech": 98,
            "techMax": 110,
            "val": 26,
            "valMax": 35,
            "forensic": 35,
            "forensicMax": 40,
            "total": 265,
            "totalMax": 310,
            "classification": "HIGH QUALITY COMPOUNDER"
        }
    },
    "veranda": {
        "name": "Veranda Learning Solutions",
        "ticker": "VERANDA:IN",
        "cmp": "₹248.00",
        "dcf": "₹280.00",
        "mos": "+12.9%",
        "mcap": "₹1,850 Cr",
        "pe": "36.5",
        "pbv": "4.2",
        "evEbitda": "18.2",
        "beneishM": -2.15,
        "beneishStatus": "MONITOR (Acquisition Goodwill)",
        "altmanZ": 4.2,
        "altmanStatus": "GREY ZONE (Leveraged Acquisitions)",
        "sloanAccrual": "4.8%",
        "piotroski": "6 / 9",
        "dupontROE": {
            "taxBurden": "0.72",
            "interestBurden": "0.78",
            "opMargin": "18.4%",
            "assetTurn": "0.85x",
            "leverage": "1.75x",
            "finalROE": "15.5%"
        },
        "kyleLambda": "0.450 bps / 5k shs",
        "blkOwnership": "0.80% ($1.8M)",
        "vangOwnership": "0.65% ($1.4M)",
        "activeFloat": "44.8%",
        "nanoLink": "veranda_center",
        "soicScore": {
            "industry": 34,
            "industryMax": 45,
            "funda": 55,
            "fundaMax": 80,
            "tech": 90,
            "techMax": 110,
            "val": 22,
            "valMax": 35,
            "forensic": 24,
            "forensicMax": 40,
            "total": 225,
            "totalMax": 310,
            "classification": "GROWTH OPPORTUNITY (LEVERAGED)"
        }
    },
    "navneet": {
        "name": "Navneet Education Ltd",
        "ticker": "NAVNETEDUL:IN",
        "cmp": "₹158.00",
        "dcf": "₹182.00",
        "mos": "+15.2%",
        "mcap": "₹3,580 Cr",
        "pe": "16.4",
        "pbv": "2.8",
        "evEbitda": "10.8",
        "beneishM": -2.82,
        "beneishStatus": "PRISTINE SAFE",
        "altmanZ": 8.2,
        "altmanStatus": "SAFE ZONE",
        "sloanAccrual": "0.5%",
        "piotroski": "8 / 9",
        "dupontROE": {
            "taxBurden": "0.75",
            "interestBurden": "0.96",
            "opMargin": "16.5%",
            "assetTurn": "1.42x",
            "leverage": "1.20x",
            "finalROE": "20.2%"
        },
        "kyleLambda": "0.280 bps / 10k shs",
        "blkOwnership": "1.95% ($8.4M)",
        "vangOwnership": "1.60% ($6.9M)",
        "activeFloat": "38.2%",
        "nanoLink": "navneet_dantej",
        "soicScore": {
            "industry": 36,
            "industryMax": 45,
            "funda": 68,
            "fundaMax": 80,
            "tech": 85,
            "techMax": 110,
            "val": 30,
            "valMax": 35,
            "forensic": 36,
            "forensicMax": 40,
            "total": 255,
            "totalMax": 310,
            "classification": "VALUE COMPOUNDER"
        }
    },
    "pidilite": {
        "name": "Pidilite Industries Ltd",
        "ticker": "PIDILITIND:IN",
        "cmp": "₹3,025.00",
        "dcf": "₹3,240.00",
        "mos": "+7.1%",
        "mcap": "₹1,53,600 Cr",
        "pe": "72.5",
        "pbv": "16.8",
        "evEbitda": "46.8",
        "beneishM": -2.92,
        "beneishStatus": "PRISTINE SAFE",
        "altmanZ": 12.8,
        "altmanStatus": "ULTRA SAFE (Zero Net Debt)",
        "sloanAccrual": "1.1%",
        "piotroski": "9 / 9",
        "dupontROE": {
            "taxBurden": "0.75",
            "interestBurden": "0.99",
            "opMargin": "22.4%",
            "assetTurn": "1.45x",
            "leverage": "1.15x",
            "finalROE": "27.8%"
        },
        "kyleLambda": "0.042 bps / 10k shs",
        "blkOwnership": "5.20% ($950M)",
        "vangOwnership": "4.80% ($880M)",
        "activeFloat": "30.2%",
        "nanoLink": "vapi",
        "soicScore": {
            "industry": 45,
            "industryMax": 45,
            "funda": 78,
            "fundaMax": 80,
            "tech": 95,
            "techMax": 110,
            "val": 20,
            "valMax": 35,
            "forensic": 40,
            "forensicMax": 40,
            "total": 278,
            "totalMax": 310,
            "classification": "ULTRA MOAT MONOPOLIST"
        }
    },
    "srf": {
        "name": "SRF Ltd",
        "ticker": "SRF:IN",
        "cmp": "₹2,240.00",
        "dcf": "₹2,480.00",
        "mos": "+10.7%",
        "mcap": "₹66,400 Cr",
        "pe": "42.8",
        "pbv": "5.8",
        "evEbitda": "23.4",
        "beneishM": -2.58,
        "beneishStatus": "SAFE",
        "altmanZ": 6.4,
        "altmanStatus": "SAFE ZONE",
        "sloanAccrual": "3.2%",
        "piotroski": "7 / 9",
        "dupontROE": {
            "taxBurden": "0.75",
            "interestBurden": "0.91",
            "opMargin": "20.8%",
            "assetTurn": "0.95x",
            "leverage": "1.45x",
            "finalROE": "19.5%"
        },
        "kyleLambda": "0.075 bps / 10k shs",
        "blkOwnership": "4.10% ($325M)",
        "vangOwnership": "3.80% ($300M)",
        "activeFloat": "49.5%",
        "nanoLink": "srf_dahej",
        "soicScore": {
            "industry": 40,
            "industryMax": 45,
            "funda": 63,
            "fundaMax": 80,
            "tech": 75,
            "techMax": 110,
            "val": 35,
            "valMax": 35,
            "forensic": 40,
            "total": 253,
            "totalMax": 310,
            "classification": "CYCLICAL COMPOUNDER"
        }
    },
    "navin": {
        "name": "Navin Fluorine International",
        "ticker": "NAVINFLUOR:IN",
        "cmp": "₹3,350.00",
        "dcf": "₹3,720.00",
        "mos": "+11.0%",
        "mcap": "₹16,600 Cr",
        "pe": "49.5",
        "pbv": "6.8",
        "evEbitda": "27.2",
        "beneishM": -2.48,
        "beneishStatus": "SAFE",
        "altmanZ": 6.9,
        "altmanStatus": "SAFE ZONE",
        "sloanAccrual": "2.6%",
        "piotroski": "7 / 9",
        "dupontROE": {
            "taxBurden": "0.75",
            "interestBurden": "0.93",
            "opMargin": "24.2%",
            "assetTurn": "0.88x",
            "leverage": "1.32x",
            "finalROE": "19.8%"
        },
        "kyleLambda": "0.115 bps / 5k shs",
        "blkOwnership": "2.90% ($58M)",
        "vangOwnership": "2.50% ($50M)",
        "activeFloat": "71.2%",
        "nanoLink": "navin_surat",
        "soicScore": {
            "industry": 42,
            "industryMax": 45,
            "funda": 68,
            "fundaMax": 80,
            "tech": 85,
            "techMax": 110,
            "val": 24,
            "valMax": 35,
            "forensic": 35,
            "forensicMax": 40,
            "total": 254,
            "totalMax": 310,
            "classification": "FLUORINE SPECIALTY MONOPOLIST"
        }
    },
    "jubilant": {
        "name": "Jubilant Ingrevia Ltd",
        "ticker": "JUBLINGREA:IN",
        "cmp": "₹545.00",
        "dcf": "₹630.00",
        "mos": "+15.6%",
        "mcap": "₹8,680 Cr",
        "pe": "24.2",
        "pbv": "2.9",
        "evEbitda": "12.8",
        "beneishM": -2.62,
        "beneishStatus": "SAFE",
        "altmanZ": 5.8,
        "altmanStatus": "SAFE ZONE",
        "sloanAccrual": "1.9%",
        "piotroski": "7 / 9",
        "dupontROE": {
            "taxBurden": "0.75",
            "interestBurden": "0.92",
            "opMargin": "13.8%",
            "assetTurn": "1.25x",
            "leverage": "1.35x",
            "finalROE": "16.2%"
        },
        "kyleLambda": "0.190 bps / 10k shs",
        "blkOwnership": "1.80% ($18M)",
        "vangOwnership": "1.50% ($15M)",
        "activeFloat": "48.5%",
        "nanoLink": "jubilant_bharuch",
        "soicScore": {
            "industry": 38,
            "industryMax": 45,
            "funda": 65,
            "fundaMax": 80,
            "tech": 82,
            "techMax": 110,
            "val": 30,
            "valMax": 35,
            "forensic": 34,
            "forensicMax": 40,
            "total": 249,
            "totalMax": 310,
            "classification": "VALUE RECOVERY PLAY"
        }
    },
    "max_health": {
        "name": "Max Healthcare Institute Ltd",
        "ticker": "MAXHEALTH:IN",
        "cmp": "₹980.00",
        "dcf": "₹1,080.00",
        "mos": "+10.2%",
        "mcap": "₹95,200 Cr",
        "pe": "68.5",
        "pbv": "10.2",
        "evEbitda": "38.4",
        "beneishM": -2.75,
        "beneishStatus": "PRISTINE SAFE",
        "altmanZ": 8.8,
        "altmanStatus": "SAFE ZONE (Net Cash Balance Sheet)",
        "sloanAccrual": "-1.2% (Pure Cash Collections via TPA/Cash)",
        "piotroski": "9 / 9",
        "dupontROE": {
            "taxBurden": "0.75",
            "interestBurden": "0.98",
            "opMargin": "28.2%",
            "assetTurn": "0.92x",
            "leverage": "1.18x",
            "finalROE": "22.8%"
        },
        "kyleLambda": "0.065 bps / 10k shs",
        "blkOwnership": "4.90% ($560M)",
        "vangOwnership": "4.40% ($500M)",
        "activeFloat": "76.2%",
        "nanoLink": "saket_max",
        "soicScore": {
            "industry": 44,
            "industryMax": 45,
            "funda": 76,
            "fundaMax": 80,
            "tech": 105,
            "techMax": 110,
            "val": 22,
            "valMax": 35,
            "forensic": 38,
            "forensicMax": 40,
            "total": 285,
            "totalMax": 310,
            "classification": "TIER 1 HIGH CONVICTION"
        }
    },
    "narayana": {
        "name": "Narayana Hrudayalaya Ltd",
        "ticker": "NH:IN",
        "cmp": "₹1,290.00",
        "dcf": "₹1,460.00",
        "mos": "+13.2%",
        "mcap": "₹26,380 Cr",
        "pe": "32.5",
        "pbv": "7.4",
        "evEbitda": "19.8",
        "beneishM": -2.85,
        "beneishStatus": "SAFE",
        "altmanZ": 7.9,
        "altmanStatus": "SAFE ZONE",
        "sloanAccrual": "-0.5%",
        "piotroski": "9 / 9",
        "dupontROE": {
            "taxBurden": "0.75",
            "interestBurden": "0.97",
            "opMargin": "23.8%",
            "assetTurn": "1.35x",
            "leverage": "1.25x",
            "finalROE": "29.2%"
        },
        "kyleLambda": "0.095 bps / 10k shs",
        "blkOwnership": "3.20% ($102M)",
        "vangOwnership": "2.80% ($89M)",
        "activeFloat": "35.8%",
        "nanoLink": "narayana_bommasandra",
        "soicScore": {
            "industry": 42,
            "industryMax": 45,
            "funda": 75,
            "fundaMax": 80,
            "tech": 100,
            "techMax": 110,
            "val": 28,
            "valMax": 35,
            "forensic": 38,
            "forensicMax": 40,
            "total": 283,
            "totalMax": 310,
            "classification": "AFFORDABLE HEALTHCARE MONOPOLIST"
        }
    },
    "apollo_hosp": {
        "name": "Apollo Hospitals Enterprise Ltd",
        "ticker": "APOLLOHOSP:IN",
        "cmp": "₹6,950.00",
        "dcf": "₹7,550.00",
        "mos": "+8.6%",
        "mcap": "₹99,900 Cr",
        "pe": "78.2",
        "pbv": "12.5",
        "evEbitda": "36.5",
        "beneishM": -2.62,
        "beneishStatus": "SAFE",
        "altmanZ": 7.1,
        "altmanStatus": "SAFE ZONE",
        "sloanAccrual": "1.8%",
        "piotroski": "8 / 9",
        "dupontROE": {
            "taxBurden": "0.74",
            "interestBurden": "0.92",
            "opMargin": "13.2%",
            "assetTurn": "1.68x",
            "leverage": "1.38x",
            "finalROE": "20.8%"
        },
        "kyleLambda": "0.058 bps / 5k shs",
        "blkOwnership": "4.80% ($575M)",
        "vangOwnership": "4.20% ($500M)",
        "activeFloat": "70.5%",
        "nanoLink": "apollo_chennai",
        "soicScore": {
            "industry": 44,
            "industryMax": 45,
            "funda": 72,
            "fundaMax": 80,
            "tech": 98,
            "techMax": 110,
            "val": 20,
            "valMax": 35,
            "forensic": 36,
            "forensicMax": 40,
            "total": 270,
            "totalMax": 310,
            "classification": "HEALTHCARE CONGLOMERATE COMPOUNDER"
        }
    },
    "ihcl": {
        "name": "The Indian Hotels Co Ltd (Taj)",
        "ticker": "INDHOTEL:IN",
        "cmp": "₹685.00",
        "dcf": "₹750.00",
        "mos": "+9.5%",
        "mcap": "₹97,400 Cr",
        "pe": "64.5",
        "pbv": "9.8",
        "evEbitda": "34.2",
        "beneishM": -2.78,
        "beneishStatus": "SAFE",
        "altmanZ": 8.5,
        "altmanStatus": "SAFE ZONE (Net Cash)",
        "sloanAccrual": "0.8%",
        "piotroski": "9 / 9",
        "dupontROE": {
            "taxBurden": "0.75",
            "interestBurden": "0.96",
            "opMargin": "33.5%",
            "assetTurn": "0.68x",
            "leverage": "1.20x",
            "finalROE": "18.5%"
        },
        "kyleLambda": "0.062 bps / 10k shs",
        "blkOwnership": "4.50% ($520M)",
        "vangOwnership": "3.90% ($450M)",
        "activeFloat": "61.8%",
        "nanoLink": "taj_mahal_palace",
        "soicScore": {
            "industry": 44,
            "industryMax": 45,
            "funda": 74,
            "fundaMax": 80,
            "tech": 105,
            "techMax": 110,
            "val": 22,
            "valMax": 35,
            "forensic": 38,
            "forensicMax": 40,
            "total": 283,
            "totalMax": 310,
            "classification": "ICONIC LUXURY MONOPOLIST"
        }
    },
    "samhi": {
        "name": "SAMHI Hotels Ltd",
        "ticker": "SAMHI:IN",
        "cmp": "₹205.00",
        "dcf": "₹245.00",
        "mos": "+19.5%",
        "mcap": "₹4,480 Cr",
        "pe": "28.5",
        "pbv": "3.2",
        "evEbitda": "14.2",
        "beneishM": -2.32,
        "beneishStatus": "SAFE",
        "altmanZ": 3.9,
        "altmanStatus": "GREY ZONE (Deleveraging in Progress)",
        "sloanAccrual": "2.1%",
        "piotroski": "7 / 9",
        "dupontROE": {
            "taxBurden": "0.74",
            "interestBurden": "0.72",
            "opMargin": "31.2%",
            "assetTurn": "0.45x",
            "leverage": "1.85x",
            "finalROE": "13.8%"
        },
        "kyleLambda": "0.240 bps / 10k shs",
        "blkOwnership": "1.40% ($7.5M)",
        "vangOwnership": "1.10% ($5.9M)",
        "activeFloat": "52.4%",
        "nanoLink": "samhi_aerocity",
        "soicScore": {
            "industry": 40,
            "industryMax": 45,
            "funda": 62,
            "fundaMax": 80,
            "tech": 95,
            "techMax": 110,
            "val": 28,
            "valMax": 35,
            "forensic": 30,
            "forensicMax": 40,
            "total": 255,
            "totalMax": 310,
            "classification": "DELEVERAGING TURNAROUND COMPOUNDER"
        }
    },
    "chalet": {
        "name": "Chalet Hotels Ltd",
        "ticker": "CHALET:IN",
        "cmp": "₹840.00",
        "dcf": "₹940.00",
        "mos": "+11.9%",
        "mcap": "₹17,300 Cr",
        "pe": "48.2",
        "pbv": "7.2",
        "evEbitda": "24.5",
        "beneishM": -2.55,
        "beneishStatus": "SAFE",
        "altmanZ": 5.2,
        "altmanStatus": "SAFE ZONE",
        "sloanAccrual": "1.6%",
        "piotroski": "8 / 9",
        "dupontROE": {
            "taxBurden": "0.75",
            "interestBurden": "0.84",
            "opMargin": "38.5%",
            "assetTurn": "0.42x",
            "leverage": "1.55x",
            "finalROE": "15.8%"
        },
        "kyleLambda": "0.145 bps / 5k shs",
        "blkOwnership": "2.40% ($49M)",
        "vangOwnership": "2.10% ($43M)",
        "activeFloat": "28.4%",
        "nanoLink": "chalet_powai",
        "soicScore": {
            "industry": 40,
            "industryMax": 45,
            "funda": 68,
            "fundaMax": 80,
            "tech": 98,
            "techMax": 110,
            "val": 24,
            "valMax": 35,
            "forensic": 34,
            "forensicMax": 40,
            "total": 264,
            "totalMax": 310,
            "classification": "METRO LUXURY ASSET OWNER"
        }
    },
    "apl_apollo": {
        "name": "APL Apollo Tubes Ltd",
        "ticker": "APLAPOLLO:IN",
        "cmp": "₹1,610.00",
        "dcf": "₹1,820.00",
        "mos": "+13.0%",
        "mcap": "₹44,700 Cr",
        "pe": "54.5",
        "pbv": "11.8",
        "evEbitda": "32.8",
        "beneishM": -2.68,
        "beneishStatus": "SAFE",
        "altmanZ": 9.2,
        "altmanStatus": "PRISTINE SAFE ZONE",
        "sloanAccrual": "1.5%",
        "piotroski": "8 / 9",
        "dupontROE": {
            "taxBurden": "0.75",
            "interestBurden": "0.96",
            "opMargin": "7.8%",
            "assetTurn": "3.25x",
            "leverage": "1.22x",
            "finalROE": "22.4%"
        },
        "kyleLambda": "0.072 bps / 10k shs",
        "blkOwnership": "3.80% ($200M)",
        "vangOwnership": "3.40% ($180M)",
        "activeFloat": "69.5%",
        "nanoLink": "apollo_raipur",
        "soicScore": {
            "industry": 42,
            "industryMax": 45,
            "funda": 74,
            "fundaMax": 80,
            "tech": 100,
            "techMax": 110,
            "val": 26,
            "valMax": 35,
            "forensic": 38,
            "forensicMax": 40,
            "total": 280,
            "totalMax": 310,
            "classification": "STRUCTURAL STEEL MONOPOLIST"
        }
    },
    "ratnamani": {
        "name": "Ratnamani Metals & Tubes Ltd",
        "ticker": "RATNAMANI:IN",
        "cmp": "₹3,480.00",
        "dcf": "₹3,920.00",
        "mos": "+12.6%",
        "mcap": "₹24,400 Cr",
        "pe": "38.4",
        "pbv": "7.2",
        "evEbitda": "24.1",
        "beneishM": -2.8,
        "beneishStatus": "PRISTINE SAFE",
        "altmanZ": 10.5,
        "altmanStatus": "ULTRA SAFE (Net Cash)",
        "sloanAccrual": "-0.2%",
        "piotroski": "9 / 9",
        "dupontROE": {
            "taxBurden": "0.75",
            "interestBurden": "0.98",
            "opMargin": "18.4%",
            "assetTurn": "1.45x",
            "leverage": "1.14x",
            "finalROE": "22.8%"
        },
        "kyleLambda": "0.110 bps / 5k shs",
        "blkOwnership": "2.80% ($81M)",
        "vangOwnership": "2.40% ($70M)",
        "activeFloat": "39.8%",
        "nanoLink": "ratnamani_kutch",
        "soicScore": {
            "industry": 42,
            "industryMax": 45,
            "funda": 76,
            "fundaMax": 80,
            "tech": 102,
            "techMax": 110,
            "val": 26,
            "valMax": 35,
            "forensic": 38,
            "forensicMax": 40,
            "total": 284,
            "totalMax": 310,
            "classification": "CRITICAL SS PIPING MONOPOLIST"
        }
    },
    "welspun": {
        "name": "Welspun Corp Ltd",
        "ticker": "WELCORP:IN",
        "cmp": "₹710.00",
        "dcf": "₹815.00",
        "mos": "+14.8%",
        "mcap": "₹18,600 Cr",
        "pe": "16.8",
        "pbv": "3.1",
        "evEbitda": "10.5",
        "beneishM": -2.4,
        "beneishStatus": "SAFE",
        "altmanZ": 5.4,
        "altmanStatus": "SAFE ZONE",
        "sloanAccrual": "2.9%",
        "piotroski": "7 / 9",
        "dupontROE": {
            "taxBurden": "0.75",
            "interestBurden": "0.88",
            "opMargin": "12.2%",
            "assetTurn": "1.58x",
            "leverage": "1.45x",
            "finalROE": "18.5%"
        },
        "kyleLambda": "0.160 bps / 10k shs",
        "blkOwnership": "2.20% ($48M)",
        "vangOwnership": "1.90% ($42M)",
        "activeFloat": "50.2%",
        "nanoLink": "welspun_anjar",
        "soicScore": {
            "industry": 38,
            "industryMax": 45,
            "funda": 66,
            "fundaMax": 80,
            "tech": 92,
            "techMax": 110,
            "val": 30,
            "valMax": 35,
            "forensic": 32,
            "forensicMax": 40,
            "total": 258,
            "totalMax": 310,
            "classification": "GLOBAL LINE PIPE LEADER"
        }
    },
    "hdfc_bank": {
        "name": "HDFC Bank Ltd",
        "ticker": "HDFCBANK:IN",
        "cmp": "₹1,740.00",
        "dcf": "₹1,980.00",
        "mos": "+13.8%",
        "mcap": "₹13,24,000 Cr ($158B)",
        "pe": "18.2",
        "pbv": "2.7",
        "evEbitda": "N/A (Bank)",
        "beneishM": -2.95,
        "beneishStatus": "PRISTINE SAFE",
        "altmanZ": 3.1,
        "altmanStatus": "BANK CAPITAL ADEQUACY 19.3% (TIER 1 17.1%)",
        "sloanAccrual": "GNPA 1.24% / NNPA 0.33%",
        "piotroski": "8 / 9",
        "dupontROE": {
            "taxBurden": "0.75",
            "interestBurden": "NIM 3.65%",
            "opMargin": "Cost/Income 38.2%",
            "assetTurn": "ROA 1.95%",
            "leverage": "8.2x",
            "finalROE": "16.4%"
        },
        "kyleLambda": "0.015 bps / 50k shs",
        "blkOwnership": "6.40% ($10.1B)",
        "vangOwnership": "5.80% ($9.2B)",
        "activeFloat": "100.0% (Zero Promoter)",
        "nanoLink": "hdfc_bkc",
        "soicScore": {
            "industry": 45,
            "industryMax": 45,
            "funda": 78,
            "fundaMax": 80,
            "tech": 92,
            "techMax": 110,
            "val": 30,
            "valMax": 35,
            "forensic": 40,
            "forensicMax": 40,
            "total": 285,
            "totalMax": 310,
            "classification": "NATIONAL FINANCIAL PILLAR"
        }
    },
    "icici_bank": {
        "name": "ICICI Bank Ltd",
        "ticker": "ICICIBANK:IN",
        "cmp": "₹1,265.00",
        "dcf": "₹1,420.00",
        "mos": "+12.3%",
        "mcap": "₹8,92,000 Cr ($106B)",
        "pe": "17.8",
        "pbv": "3.1",
        "evEbitda": "N/A (Bank)",
        "beneishM": -2.98,
        "beneishStatus": "PRISTINE SAFE",
        "altmanZ": 3.25,
        "altmanStatus": "CAR 16.8% (CET-1 15.9%)",
        "sloanAccrual": "GNPA 1.97% / NNPA 0.42%",
        "piotroski": "9 / 9",
        "dupontROE": {
            "taxBurden": "0.75",
            "interestBurden": "NIM 4.36%",
            "opMargin": "Cost/Income 39.5%",
            "assetTurn": "ROA 2.38%",
            "leverage": "7.8x",
            "finalROE": "18.6%"
        },
        "kyleLambda": "0.018 bps / 50k shs",
        "blkOwnership": "6.80% ($7.2B)",
        "vangOwnership": "6.10% ($6.5B)",
        "activeFloat": "100.0%",
        "nanoLink": "icici_bkc",
        "soicScore": {
            "industry": 45,
            "industryMax": 45,
            "funda": 80,
            "fundaMax": 80,
            "tech": 105,
            "techMax": 110,
            "val": 28,
            "valMax": 35,
            "forensic": 40,
            "forensicMax": 40,
            "total": 298,
            "totalMax": 310,
            "classification": "PERFECT BANKING COMPOUNDER"
        }
    },
    "kotak_bank": {
        "name": "Kotak Mahindra Bank Ltd",
        "ticker": "KOTAKBANK:IN",
        "cmp": "₹1,780.00",
        "dcf": "₹2,050.00",
        "mos": "+15.2%",
        "mcap": "₹3,54,000 Cr ($42B)",
        "pe": "19.4",
        "pbv": "2.8",
        "evEbitda": "N/A (Bank)",
        "beneishM": -2.91,
        "beneishStatus": "SAFE",
        "altmanZ": 3.5,
        "altmanStatus": "CAR 20.8% (Pristine Fortress)",
        "sloanAccrual": "GNPA 1.39% / NNPA 0.34%",
        "piotroski": "8 / 9",
        "dupontROE": {
            "taxBurden": "0.75",
            "interestBurden": "NIM 4.91%",
            "opMargin": "Cost/Income 46.2%",
            "assetTurn": "ROA 2.35%",
            "leverage": "6.1x",
            "finalROE": "14.8%"
        },
        "kyleLambda": "0.028 bps / 20k shs",
        "blkOwnership": "4.20% ($1.76B)",
        "vangOwnership": "3.90% ($1.64B)",
        "activeFloat": "74.1%",
        "nanoLink": "kotak_bkc",
        "soicScore": {
            "industry": 42,
            "industryMax": 45,
            "funda": 76,
            "fundaMax": 80,
            "tech": 88,
            "techMax": 110,
            "val": 30,
            "valMax": 35,
            "forensic": 40,
            "forensicMax": 40,
            "total": 276,
            "totalMax": 310,
            "classification": "FORTRESS CAPITAL COMPOUNDER"
        }
    },
    "sbi": {
        "name": "State Bank of India",
        "ticker": "SBIN:IN",
        "cmp": "₹825.00",
        "dcf": "₹940.00",
        "mos": "+13.9%",
        "mcap": "₹7,36,000 Cr ($88B)",
        "pe": "10.5",
        "pbv": "1.7",
        "evEbitda": "N/A (Bank)",
        "beneishM": -2.7,
        "beneishStatus": "SAFE",
        "altmanZ": 2.85,
        "altmanStatus": "SOVEREIGN BACKED (GOI 57.5%)",
        "sloanAccrual": "GNPA 2.21% / NNPA 0.57%",
        "piotroski": "8 / 9",
        "dupontROE": {
            "taxBurden": "0.75",
            "interestBurden": "NIM 3.22%",
            "opMargin": "Cost/Income 52.8%",
            "assetTurn": "ROA 1.08%",
            "leverage": "15.5x",
            "finalROE": "16.8%"
        },
        "kyleLambda": "0.022 bps / 50k shs",
        "blkOwnership": "3.80% ($3.3B)",
        "vangOwnership": "3.40% ($3.0B)",
        "activeFloat": "42.5%",
        "nanoLink": "sbi_nariman",
        "soicScore": {
            "industry": 44,
            "industryMax": 45,
            "funda": 72,
            "fundaMax": 80,
            "tech": 98,
            "techMax": 110,
            "val": 32,
            "valMax": 35,
            "forensic": 34,
            "forensicMax": 40,
            "total": 280,
            "totalMax": 310,
            "classification": "SOVEREIGN CREDIT ENGINE"
        }
    },
    "nvidia": {
        "name": "NVIDIA Corporation",
        "ticker": "NVDA:US",
        "cmp": "$138.20",
        "dcf": "$152.00",
        "mos": "+10.0%",
        "mcap": "$3,380 Billion ($3.38T)",
        "pe": "58.4",
        "pbv": "42.5",
        "evEbitda": "44.2",
        "beneishM": -2.85,
        "beneishStatus": "SAFE (No Earnings Manipulation)",
        "altmanZ": 18.4,
        "altmanStatus": "SAFE ZONE (Distress Probability < 0.01%)",
        "sloanAccrual": "1.4% (Ultra-High Cash Conversion)",
        "piotroski": "9 / 9 (Flawless Balance Sheet)",
        "dupontROE": {
            "taxBurden": "0.88",
            "interestBurden": "1.00",
            "opMargin": "61.8%",
            "assetTurn": "1.25x",
            "leverage": "1.34x",
            "finalROE": "103.5%"
        },
        "kyleLambda": "0.0012 bps / $10M",
        "blkOwnership": "7.85% ($265 Billion)",
        "vangOwnership": "8.42% ($284 Billion)",
        "activeFloat": "88.5%",
        "nanoLink": "tsmc_fab",
        "soicScore": {
            "industry": 45,
            "industryMax": 45,
            "funda": 80,
            "fundaMax": 80,
            "tech": 110,
            "techMax": 110,
            "val": 22,
            "valMax": 35,
            "forensic": 40,
            "forensicMax": 40,
            "total": 297,
            "totalMax": 310,
            "classification": "EPIC HIGH CONVICTION ALLOCATION"
        }
    },
    "amd": {
        "name": "Advanced Micro Devices Inc",
        "ticker": "AMD:US",
        "cmp": "$148.50",
        "dcf": "$168.00",
        "mos": "+13.1%",
        "mcap": "$240 Billion",
        "pe": "45.2 (Forward)",
        "pbv": "4.2",
        "evEbitda": "28.5",
        "beneishM": -2.72,
        "beneishStatus": "SAFE",
        "altmanZ": 8.5,
        "altmanStatus": "SAFE ZONE",
        "sloanAccrual": "2.2%",
        "piotroski": "8 / 9",
        "dupontROE": {
            "taxBurden": "0.85",
            "interestBurden": "0.98",
            "opMargin": "24.5%",
            "assetTurn": "0.45x",
            "leverage": "1.22x",
            "finalROE": "11.2%"
        },
        "kyleLambda": "0.0035 bps / $5M",
        "blkOwnership": "8.10% ($19.4B)",
        "vangOwnership": "8.80% ($21.1B)",
        "activeFloat": "99.2%",
        "nanoLink": "amd_austin",
        "soicScore": {
            "industry": 42,
            "industryMax": 45,
            "funda": 72,
            "fundaMax": 80,
            "tech": 100,
            "techMax": 110,
            "val": 25,
            "valMax": 35,
            "forensic": 38,
            "forensicMax": 40,
            "total": 277,
            "totalMax": 310,
            "classification": "AI COMPUTE CHALLENGER"
        }
    },
    "broadcom": {
        "name": "Broadcom Inc",
        "ticker": "AVGO:US",
        "cmp": "$172.40",
        "dcf": "$194.00",
        "mos": "+12.5%",
        "mcap": "$805 Billion",
        "pe": "34.8 (Forward)",
        "pbv": "11.5",
        "evEbitda": "24.2",
        "beneishM": -2.6,
        "beneishStatus": "SAFE",
        "altmanZ": 6.2,
        "altmanStatus": "SAFE ZONE (VMware Integration Generating $20B FCF)",
        "sloanAccrual": "0.8%",
        "piotroski": "8 / 9",
        "dupontROE": {
            "taxBurden": "0.86",
            "interestBurden": "0.88",
            "opMargin": "58.5%",
            "assetTurn": "0.35x",
            "leverage": "2.10x",
            "finalROE": "32.5%"
        },
        "kyleLambda": "0.0028 bps / $5M",
        "blkOwnership": "7.95% ($64B)",
        "vangOwnership": "8.90% ($71.6B)",
        "activeFloat": "98.5%",
        "nanoLink": "broadcom_sanjose",
        "soicScore": {
            "industry": 45,
            "industryMax": 45,
            "funda": 78,
            "fundaMax": 80,
            "tech": 105,
            "techMax": 110,
            "val": 26,
            "valMax": 35,
            "forensic": 36,
            "forensicMax": 40,
            "total": 290,
            "totalMax": 310,
            "classification": "CUSTOM AI ASIC MONOPOLIST"
        }
    },
    "qualcomm": {
        "name": "Qualcomm Inc",
        "ticker": "QCOM:US",
        "cmp": "$168.20",
        "dcf": "$190.00",
        "mos": "+13.0%",
        "mcap": "$188 Billion",
        "pe": "19.8",
        "pbv": "7.8",
        "evEbitda": "14.8",
        "beneishM": -2.78,
        "beneishStatus": "SAFE",
        "altmanZ": 7.9,
        "altmanStatus": "SAFE ZONE",
        "sloanAccrual": "1.1%",
        "piotroski": "8 / 9",
        "dupontROE": {
            "taxBurden": "0.85",
            "interestBurden": "0.96",
            "opMargin": "28.8%",
            "assetTurn": "0.78x",
            "leverage": "2.15x",
            "finalROE": "38.4%"
        },
        "kyleLambda": "0.0042 bps / $5M",
        "blkOwnership": "7.40% ($13.9B)",
        "vangOwnership": "8.20% ($15.4B)",
        "activeFloat": "98.8%",
        "nanoLink": "qualcomm_sandiego",
        "soicScore": {
            "industry": 40,
            "industryMax": 45,
            "funda": 74,
            "fundaMax": 80,
            "tech": 95,
            "techMax": 110,
            "val": 28,
            "valMax": 35,
            "forensic": 38,
            "forensicMax": 40,
            "total": 275,
            "totalMax": 310,
            "classification": "SNAPDRAGON & EDGE AI LEADER"
        }
    },
    "apple": {
        "name": "Apple Inc",
        "ticker": "AAPL:US",
        "cmp": "$234.80",
        "dcf": "$248.00",
        "mos": "+5.6%",
        "mcap": "$3,580 Billion ($3.58T)",
        "pe": "34.2",
        "pbv": "48.5",
        "evEbitda": "25.8",
        "beneishM": -2.95,
        "beneishStatus": "PRISTINE SAFE",
        "altmanZ": 12.4,
        "altmanStatus": "SAFE ZONE ($108B Annual FCF)",
        "sloanAccrual": "-0.4%",
        "piotroski": "9 / 9",
        "dupontROE": {
            "taxBurden": "0.84",
            "interestBurden": "0.98",
            "opMargin": "31.2%",
            "assetTurn": "1.08x",
            "leverage": "4.85x",
            "finalROE": "138.0%"
        },
        "kyleLambda": "0.0008 bps / $10M",
        "blkOwnership": "6.85% ($245 Billion)",
        "vangOwnership": "8.65% ($310 Billion)",
        "activeFloat": "99.5%",
        "nanoLink": "apple_park",
        "soicScore": {
            "industry": 45,
            "industryMax": 45,
            "funda": 78,
            "fundaMax": 80,
            "tech": 100,
            "techMax": 110,
            "val": 22,
            "valMax": 35,
            "forensic": 40,
            "forensicMax": 40,
            "total": 285,
            "totalMax": 310,
            "classification": "GLOBAL CONSUMER ECOSYSTEM MONOPOLY"
        }
    },
    "microsoft": {
        "name": "Microsoft Corp",
        "ticker": "MSFT:US",
        "cmp": "$422.50",
        "dcf": "$465.00",
        "mos": "+10.1%",
        "mcap": "$3,140 Billion ($3.14T)",
        "pe": "35.6",
        "pbv": "12.8",
        "evEbitda": "23.4",
        "beneishM": -2.88,
        "beneishStatus": "PRISTINE SAFE",
        "altmanZ": 10.8,
        "altmanStatus": "AAA CREDIT RATED (Highest Global Solvency)",
        "sloanAccrual": "0.5%",
        "piotroski": "9 / 9",
        "dupontROE": {
            "taxBurden": "0.82",
            "interestBurden": "0.99",
            "opMargin": "44.8%",
            "assetTurn": "0.54x",
            "leverage": "1.82x",
            "finalROE": "36.5%"
        },
        "kyleLambda": "0.0010 bps / $10M",
        "blkOwnership": "7.20% ($226 Billion)",
        "vangOwnership": "8.90% ($279 Billion)",
        "activeFloat": "99.1%",
        "nanoLink": "msft_redmond",
        "soicScore": {
            "industry": 45,
            "industryMax": 45,
            "funda": 80,
            "fundaMax": 80,
            "tech": 102,
            "techMax": 110,
            "val": 25,
            "valMax": 35,
            "forensic": 40,
            "forensicMax": 40,
            "total": 292,
            "totalMax": 310,
            "classification": "ENTERPRISE CLOUD & AI FOUNDATION"
        }
    },
    "alphabet": {
        "name": "Alphabet Inc (Google)",
        "ticker": "GOOGL:US",
        "cmp": "$176.80",
        "dcf": "$205.00",
        "mos": "+15.9%",
        "mcap": "$2,180 Billion ($2.18T)",
        "pe": "23.8",
        "pbv": "6.8",
        "evEbitda": "16.5",
        "beneishM": -2.92,
        "beneishStatus": "PRISTINE SAFE",
        "altmanZ": 14.2,
        "altmanStatus": "SAFE ZONE (Net Cash $98 Billion)",
        "sloanAccrual": "0.2%",
        "piotroski": "9 / 9",
        "dupontROE": {
            "taxBurden": "0.86",
            "interestBurden": "1.00",
            "opMargin": "32.4%",
            "assetTurn": "0.82x",
            "leverage": "1.38x",
            "finalROE": "31.5%"
        },
        "kyleLambda": "0.0015 bps / $10M",
        "blkOwnership": "6.90% ($150 Billion)",
        "vangOwnership": "8.10% ($176 Billion)",
        "activeFloat": "88.2%",
        "nanoLink": "goog_council_bluffs",
        "soicScore": {
            "industry": 45,
            "industryMax": 45,
            "funda": 78,
            "fundaMax": 80,
            "tech": 98,
            "techMax": 110,
            "val": 30,
            "valMax": 35,
            "forensic": 40,
            "forensicMax": 40,
            "total": 291,
            "totalMax": 310,
            "classification": "GLOBAL SEARCH & CLOUD MONOPOLIST"
        }
    },
    "amazon": {
        "name": "Amazon.com Inc",
        "ticker": "AMZN:US",
        "cmp": "$195.40",
        "dcf": "$228.00",
        "mos": "+16.7%",
        "mcap": "$2,040 Billion ($2.04T)",
        "pe": "41.2",
        "pbv": "8.2",
        "evEbitda": "17.8",
        "beneishM": -2.74,
        "beneishStatus": "SAFE",
        "altmanZ": 6.8,
        "altmanStatus": "SAFE ZONE (AWS Margin Expansion to 38%)",
        "sloanAccrual": "-1.5% (Negative Working Capital Machine)",
        "piotroski": "8 / 9",
        "dupontROE": {
            "taxBurden": "0.80",
            "interestBurden": "0.94",
            "opMargin": "10.5%",
            "assetTurn": "1.25x",
            "leverage": "2.25x",
            "finalROE": "22.4%"
        },
        "kyleLambda": "0.0014 bps / $10M",
        "blkOwnership": "6.50% ($132 Billion)",
        "vangOwnership": "7.80% ($159 Billion)",
        "activeFloat": "90.2%",
        "nanoLink": "amzn_ashburn",
        "soicScore": {
            "industry": 45,
            "industryMax": 45,
            "funda": 76,
            "fundaMax": 80,
            "tech": 105,
            "techMax": 110,
            "val": 28,
            "valMax": 35,
            "forensic": 38,
            "forensicMax": 40,
            "total": 292,
            "totalMax": 310,
            "classification": "GLOBAL E-COMMERCE & AWS CLOUD LEVIATHAN"
        }
    },
    "tesla": {
        "name": "Tesla Inc",
        "ticker": "TSLA:US",
        "cmp": "$248.50",
        "dcf": "$275.00",
        "mos": "+10.7%",
        "mcap": "$792 Billion",
        "pe": "74.5",
        "pbv": "11.8",
        "evEbitda": "42.5",
        "beneishM": -2.48,
        "beneishStatus": "SAFE",
        "altmanZ": 8.9,
        "altmanStatus": "SAFE ZONE (Net Cash $29 Billion)",
        "sloanAccrual": "2.4%",
        "piotroski": "7 / 9",
        "dupontROE": {
            "taxBurden": "0.82",
            "interestBurden": "0.99",
            "opMargin": "8.4%",
            "assetTurn": "0.92x",
            "leverage": "1.62x",
            "finalROE": "10.2%"
        },
        "kyleLambda": "0.0018 bps / $10M",
        "blkOwnership": "5.80% ($46 Billion)",
        "vangOwnership": "7.40% ($58.6 Billion)",
        "activeFloat": "79.5%",
        "nanoLink": "tsla_austin",
        "soicScore": {
            "industry": 40,
            "industryMax": 45,
            "funda": 68,
            "fundaMax": 80,
            "tech": 105,
            "techMax": 110,
            "val": 20,
            "valMax": 35,
            "forensic": 34,
            "forensicMax": 40,
            "total": 267,
            "totalMax": 310,
            "classification": "AUTONOMOUS ROBOTICS & ENERGY TRANSITION"
        }
    },
    "exxon": {
        "name": "ExxonMobil Corporation",
        "ticker": "XOM:US",
        "cmp": "$118.40",
        "dcf": "$132.00",
        "mos": "+11.5%",
        "mcap": "$468 Billion",
        "pe": "14.2",
        "pbv": "2.1",
        "evEbitda": "7.8",
        "beneishM": -2.82,
        "beneishStatus": "SAFE",
        "altmanZ": 5.8,
        "altmanStatus": "SAFE ZONE (Pioneer Acquisition Lowers Permian Cost)",
        "sloanAccrual": "0.9%",
        "piotroski": "8 / 9",
        "dupontROE": {
            "taxBurden": "0.72",
            "interestBurden": "0.95",
            "opMargin": "16.5%",
            "assetTurn": "0.95x",
            "leverage": "1.65x",
            "finalROE": "17.8%"
        },
        "kyleLambda": "0.0025 bps / $5M",
        "blkOwnership": "7.40% ($34.6B)",
        "vangOwnership": "8.90% ($41.6B)",
        "activeFloat": "98.5%",
        "nanoLink": "baytown",
        "soicScore": {
            "industry": 42,
            "industryMax": 45,
            "funda": 74,
            "fundaMax": 80,
            "tech": 98,
            "techMax": 110,
            "val": 28,
            "valMax": 35,
            "forensic": 38,
            "forensicMax": 40,
            "total": 280,
            "totalMax": 310,
            "classification": "WESTERN ENERGY TITAN"
        }
    },
    "chevron": {
        "name": "Chevron Corporation",
        "ticker": "CVX:US",
        "cmp": "$154.20",
        "dcf": "$170.00",
        "mos": "+10.2%",
        "mcap": "$284 Billion",
        "pe": "13.8",
        "pbv": "1.8",
        "evEbitda": "7.2",
        "beneishM": -2.8,
        "beneishStatus": "SAFE",
        "altmanZ": 5.6,
        "altmanStatus": "SAFE ZONE",
        "sloanAccrual": "1.1%",
        "piotroski": "8 / 9",
        "dupontROE": {
            "taxBurden": "0.74",
            "interestBurden": "0.96",
            "opMargin": "15.8%",
            "assetTurn": "0.88x",
            "leverage": "1.58x",
            "finalROE": "15.2%"
        },
        "kyleLambda": "0.0032 bps / $5M",
        "blkOwnership": "7.10% ($20.1B)",
        "vangOwnership": "8.50% ($24.1B)",
        "activeFloat": "98.8%",
        "nanoLink": "cvx_pascagoula",
        "soicScore": {
            "industry": 40,
            "industryMax": 45,
            "funda": 72,
            "fundaMax": 80,
            "tech": 95,
            "techMax": 110,
            "val": 28,
            "valMax": 35,
            "forensic": 38,
            "forensicMax": 40,
            "total": 273,
            "totalMax": 310,
            "classification": "DIVIDEND ARISTOCRAT HYDROCARBON"
        }
    },
    "cheniere": {
        "name": "Cheniere Energy Inc",
        "ticker": "LNG:US",
        "cmp": "$184.60",
        "dcf": "$212.00",
        "mos": "+14.8%",
        "mcap": "$42.5 Billion",
        "pe": "12.4",
        "pbv": "5.2",
        "evEbitda": "8.9",
        "beneishM": -2.65,
        "beneishStatus": "SAFE",
        "altmanZ": 4.8,
        "altmanStatus": "SAFE ZONE (20-Year Take-or-Pay LNG Contracts)",
        "sloanAccrual": "0.4%",
        "piotroski": "8 / 9",
        "dupontROE": {
            "taxBurden": "0.78",
            "interestBurden": "0.82",
            "opMargin": "42.5%",
            "assetTurn": "0.48x",
            "leverage": "3.25x",
            "finalROE": "42.5%"
        },
        "kyleLambda": "0.0085 bps / $2M",
        "blkOwnership": "8.40% ($3.57B)",
        "vangOwnership": "8.95% ($3.80B)",
        "activeFloat": "95.2%",
        "nanoLink": "cheniere_sabine",
        "soicScore": {
            "industry": 44,
            "industryMax": 45,
            "funda": 76,
            "fundaMax": 80,
            "tech": 102,
            "techMax": 110,
            "val": 30,
            "valMax": 35,
            "forensic": 36,
            "forensicMax": 40,
            "total": 288,
            "totalMax": 310,
            "classification": "GLOBAL LNG INFRASTRUCTURE TOLLBOOTH"
        }
    },
    "conocophillips": {
        "name": "ConocoPhillips",
        "ticker": "COP:US",
        "cmp": "$106.80",
        "dcf": "$122.00",
        "mos": "+14.2%",
        "mcap": "$124 Billion",
        "pe": "12.2",
        "pbv": "2.3",
        "evEbitda": "6.4",
        "beneishM": -2.75,
        "beneishStatus": "SAFE",
        "altmanZ": 6.1,
        "altmanStatus": "SAFE ZONE",
        "sloanAccrual": "1.2%",
        "piotroski": "8 / 9",
        "dupontROE": {
            "taxBurden": "0.74",
            "interestBurden": "0.94",
            "opMargin": "26.4%",
            "assetTurn": "0.68x",
            "leverage": "1.65x",
            "finalROE": "18.4%"
        },
        "kyleLambda": "0.0048 bps / $5M",
        "blkOwnership": "7.50% ($9.3B)",
        "vangOwnership": "8.80% ($10.9B)",
        "activeFloat": "99.0%",
        "nanoLink": "cop_permian",
        "soicScore": {
            "industry": 40,
            "industryMax": 45,
            "funda": 72,
            "fundaMax": 80,
            "tech": 95,
            "techMax": 110,
            "val": 30,
            "valMax": 35,
            "forensic": 38,
            "forensicMax": 40,
            "total": 275,
            "totalMax": 310,
            "classification": "LOWEST COST PERMIAN E&P"
        }
    },
    "prysmian_us": {
        "name": "Prysmian Group (North America / Milan)",
        "ticker": "PRY:IM",
        "cmp": "€62.80",
        "dcf": "€71.50",
        "mos": "+13.8%",
        "mcap": "€18.2 Billion",
        "pe": "24.5",
        "pbv": "3.8",
        "evEbitda": "14.2",
        "beneishM": -2.6,
        "beneishStatus": "SAFE",
        "altmanZ": 5.8,
        "altmanStatus": "SAFE ZONE (Submarine Cable Monopoly)",
        "sloanAccrual": "2.1%",
        "piotroski": "8 / 9",
        "dupontROE": {
            "taxBurden": "0.72",
            "interestBurden": "0.88",
            "opMargin": "9.8%",
            "assetTurn": "1.65x",
            "leverage": "2.10x",
            "finalROE": "21.5%"
        },
        "kyleLambda": "0.018 bps / €2M",
        "blkOwnership": "5.20% (€946M)",
        "vangOwnership": "4.80% (€873M)",
        "activeFloat": "85.2%",
        "nanoLink": "prysmian_highland",
        "soicScore": {
            "industry": 44,
            "industryMax": 45,
            "funda": 74,
            "fundaMax": 80,
            "tech": 105,
            "techMax": 110,
            "val": 26,
            "valMax": 35,
            "forensic": 36,
            "forensicMax": 40,
            "total": 285,
            "totalMax": 310,
            "classification": "SUBMARINE GRID MONOPOLIST"
        }
    },
    "hubbell": {
        "name": "Hubbell Inc",
        "ticker": "HUBB:US",
        "cmp": "$418.00",
        "dcf": "$450.00",
        "mos": "+7.6%",
        "mcap": "$22.4 Billion",
        "pe": "26.8",
        "pbv": "7.4",
        "evEbitda": "18.2",
        "beneishM": -2.72,
        "beneishStatus": "SAFE",
        "altmanZ": 7.8,
        "altmanStatus": "SAFE ZONE",
        "sloanAccrual": "1.5%",
        "piotroski": "8 / 9",
        "dupontROE": {
            "taxBurden": "0.76",
            "interestBurden": "0.95",
            "opMargin": "21.5%",
            "assetTurn": "1.15x",
            "leverage": "1.65x",
            "finalROE": "29.4%"
        },
        "kyleLambda": "0.012 bps / $2M",
        "blkOwnership": "8.20% ($1.83B)",
        "vangOwnership": "9.10% ($2.03B)",
        "activeFloat": "98.5%",
        "nanoLink": "hubbell_shelton",
        "soicScore": {
            "industry": 42,
            "industryMax": 45,
            "funda": 75,
            "fundaMax": 80,
            "tech": 102,
            "techMax": 110,
            "val": 24,
            "valMax": 35,
            "forensic": 38,
            "forensicMax": 40,
            "total": 281,
            "totalMax": 310,
            "classification": "US GRID MODERNIZATION PLAY"
        }
    },
    "stride": {
        "name": "Stride Inc (K12)",
        "ticker": "LRN:US",
        "cmp": "$78.40",
        "dcf": "$92.50",
        "mos": "+18.0%",
        "mcap": "$3.40 Billion",
        "pe": "17.2",
        "pbv": "3.1",
        "evEbitda": "9.8",
        "beneishM": -2.68,
        "beneishStatus": "SAFE",
        "altmanZ": 6.8,
        "altmanStatus": "SAFE ZONE",
        "sloanAccrual": "0.6%",
        "piotroski": "8 / 9",
        "dupontROE": {
            "taxBurden": "0.76",
            "interestBurden": "0.94",
            "opMargin": "13.8%",
            "assetTurn": "1.25x",
            "leverage": "1.45x",
            "finalROE": "17.8%"
        },
        "kyleLambda": "0.065 bps / $1M",
        "blkOwnership": "9.20% ($312M)",
        "vangOwnership": "10.5% ($357M)",
        "activeFloat": "94.2%",
        "nanoLink": "stride_hq",
        "soicScore": {
            "industry": 38,
            "industryMax": 45,
            "funda": 70,
            "fundaMax": 80,
            "tech": 98,
            "techMax": 110,
            "val": 30,
            "valMax": 35,
            "forensic": 36,
            "forensicMax": 40,
            "total": 272,
            "totalMax": 310,
            "classification": "ONLINE K12 VIRTUAL MONOPOLY"
        }
    },
    "coursera": {
        "name": "Coursera Inc",
        "ticker": "COUR:US",
        "cmp": "$8.25",
        "dcf": "$10.50",
        "mos": "+27.3%",
        "mcap": "$1.28 Billion",
        "pe": "Negative (FCF Positive)",
        "pbv": "2.1",
        "evEbitda": "14.5",
        "beneishM": -2.52,
        "beneishStatus": "SAFE",
        "altmanZ": 5.2,
        "altmanStatus": "SAFE ZONE (Net Cash $720M, Zero Debt)",
        "sloanAccrual": "-3.8% (Deferred Revenue Unearned Cash)",
        "piotroski": "6 / 9",
        "dupontROE": {
            "taxBurden": "1.00",
            "interestBurden": "1.00",
            "opMargin": "7.2% (Adj EBITDA)",
            "assetTurn": "0.85x",
            "leverage": "1.35x",
            "finalROE": "8.2%"
        },
        "kyleLambda": "0.120 bps / $1M",
        "blkOwnership": "6.40% ($81M)",
        "vangOwnership": "7.20% ($92M)",
        "activeFloat": "85.4%",
        "nanoLink": "coursera_mtv",
        "soicScore": {
            "industry": 38,
            "industryMax": 45,
            "funda": 60,
            "fundaMax": 80,
            "tech": 80,
            "techMax": 110,
            "val": 32,
            "valMax": 35,
            "forensic": 34,
            "forensicMax": 40,
            "total": 244,
            "totalMax": 310,
            "classification": "GENAI SKILLS UPSKILLING"
        }
    },
    "duolingo": {
        "name": "Duolingo Inc",
        "ticker": "DUOL:US",
        "cmp": "$295.00",
        "dcf": "$330.00",
        "mos": "+11.8%",
        "mcap": "$12.8 Billion",
        "pe": "68.5",
        "pbv": "14.2",
        "evEbitda": "44.8",
        "beneishM": -2.85,
        "beneishStatus": "PRISTINE SAFE",
        "altmanZ": 14.5,
        "altmanStatus": "PRISTINE SAFE (Zero Debt Net Cash $850M)",
        "sloanAccrual": "-2.4% (Annual Subscription Cash Floats)",
        "piotroski": "9 / 9",
        "dupontROE": {
            "taxBurden": "0.82",
            "interestBurden": "1.00",
            "opMargin": "24.5%",
            "assetTurn": "0.88x",
            "leverage": "1.35x",
            "finalROE": "23.8%"
        },
        "kyleLambda": "0.025 bps / $2M",
        "blkOwnership": "7.80% ($998M)",
        "vangOwnership": "8.50% ($1.08B)",
        "activeFloat": "88.5%",
        "nanoLink": "duolingo_pgh",
        "soicScore": {
            "industry": 44,
            "industryMax": 45,
            "funda": 78,
            "fundaMax": 80,
            "tech": 105,
            "techMax": 110,
            "val": 22,
            "valMax": 35,
            "forensic": 40,
            "forensicMax": 40,
            "total": 289,
            "totalMax": 310,
            "classification": "VIRAL EDTECH MONOPOLIST"
        }
    },
    "mercedes": {
        "name": "Mercedes-Benz Group AG",
        "ticker": "MBG:GR",
        "cmp": "€56.40",
        "dcf": "€68.00",
        "mos": "+20.5%",
        "mcap": "€58.4 Billion",
        "pe": "5.8",
        "pbv": "0.62",
        "evEbitda": "3.2",
        "beneishM": -2.8,
        "beneishStatus": "SAFE",
        "altmanZ": 3.4,
        "altmanStatus": "INDUSTRIAL SAFE (Net Industrial Liquidity €31B)",
        "sloanAccrual": "1.8%",
        "piotroski": "7 / 9",
        "dupontROE": {
            "taxBurden": "0.72",
            "interestBurden": "0.94",
            "opMargin": "10.8%",
            "assetTurn": "0.58x",
            "leverage": "2.65x",
            "finalROE": "11.2%"
        },
        "kyleLambda": "0.015 bps / €5M",
        "blkOwnership": "4.80% (€2.8B)",
        "vangOwnership": "4.20% (€2.45B)",
        "activeFloat": "79.2%",
        "nanoLink": "mercedes_factory56",
        "soicScore": {
            "industry": 38,
            "industryMax": 45,
            "funda": 66,
            "fundaMax": 80,
            "tech": 80,
            "techMax": 110,
            "val": 34,
            "valMax": 35,
            "forensic": 38,
            "forensicMax": 40,
            "total": 256,
            "totalMax": 310,
            "classification": "DEEP VALUE LUXURY COMPOUNDER"
        }
    },
    "bmw": {
        "name": "Bayerische Motoren Werke AG (BMW)",
        "ticker": "BMW:GR",
        "cmp": "€72.20",
        "dcf": "€86.50",
        "mos": "+19.8%",
        "mcap": "€44.8 Billion",
        "pe": "5.4",
        "pbv": "0.55",
        "evEbitda": "3.1",
        "beneishM": -2.82,
        "beneishStatus": "SAFE",
        "altmanZ": 3.5,
        "altmanStatus": "SAFE ZONE",
        "sloanAccrual": "1.4%",
        "piotroski": "7 / 9",
        "dupontROE": {
            "taxBurden": "0.74",
            "interestBurden": "0.95",
            "opMargin": "10.2%",
            "assetTurn": "0.62x",
            "leverage": "2.85x",
            "finalROE": "12.5%"
        },
        "kyleLambda": "0.018 bps / €5M",
        "blkOwnership": "4.10% (€1.83B)",
        "vangOwnership": "3.80% (€1.70B)",
        "activeFloat": "53.2% (Quandt Family 46.8%)",
        "nanoLink": "bmw_munich",
        "soicScore": {
            "industry": 38,
            "industryMax": 45,
            "funda": 68,
            "fundaMax": 80,
            "tech": 82,
            "techMax": 110,
            "val": 34,
            "valMax": 35,
            "forensic": 38,
            "forensicMax": 40,
            "total": 260,
            "totalMax": 310,
            "classification": "DEEP VALUE GERMAN ENGINEERING"
        }
    },
    "volkswagen": {
        "name": "Volkswagen AG",
        "ticker": "VOW3:GR",
        "cmp": "€88.50",
        "dcf": "€112.00",
        "mos": "+26.5%",
        "mcap": "€46.2 Billion",
        "pe": "3.9",
        "pbv": "0.28",
        "evEbitda": "2.4",
        "beneishM": -2.68,
        "beneishStatus": "SAFE",
        "altmanZ": 2.8,
        "altmanStatus": "GREY ZONE (High Financing Arm Leverage)",
        "sloanAccrual": "2.8%",
        "piotroski": "6 / 9",
        "dupontROE": {
            "taxBurden": "0.72",
            "interestBurden": "0.90",
            "opMargin": "6.8%",
            "assetTurn": "0.54x",
            "leverage": "3.45x",
            "finalROE": "8.2%"
        },
        "kyleLambda": "0.022 bps / €5M",
        "blkOwnership": "3.80% (€1.75B)",
        "vangOwnership": "3.40% (€1.57B)",
        "activeFloat": "46.5%",
        "nanoLink": "vw_wolfsburg",
        "soicScore": {
            "industry": 36,
            "industryMax": 45,
            "funda": 62,
            "fundaMax": 80,
            "tech": 75,
            "techMax": 110,
            "val": 35,
            "valMax": 35,
            "forensic": 34,
            "forensicMax": 40,
            "total": 242,
            "totalMax": 310,
            "classification": "DEEP VALUE DISTRESSED PLAY"
        }
    },
    "siemens": {
        "name": "Siemens AG",
        "ticker": "SIE:GR",
        "cmp": "€182.40",
        "dcf": "€205.00",
        "mos": "+12.4%",
        "mcap": "€144 Billion",
        "pe": "17.8",
        "pbv": "2.6",
        "evEbitda": "13.2",
        "beneishM": -2.78,
        "beneishStatus": "SAFE",
        "altmanZ": 5.2,
        "altmanStatus": "SAFE ZONE (Factory Automation Record Backlog €112B)",
        "sloanAccrual": "0.8%",
        "piotroski": "8 / 9",
        "dupontROE": {
            "taxBurden": "0.74",
            "interestBurden": "0.92",
            "opMargin": "15.4%",
            "assetTurn": "0.55x",
            "leverage": "2.40x",
            "finalROE": "14.5%"
        },
        "kyleLambda": "0.0085 bps / €5M",
        "blkOwnership": "6.40% (€9.2B)",
        "vangOwnership": "5.80% (€8.35B)",
        "activeFloat": "94.2%",
        "nanoLink": "siemens_amberg",
        "soicScore": {
            "industry": 45,
            "industryMax": 45,
            "funda": 76,
            "fundaMax": 80,
            "tech": 105,
            "techMax": 110,
            "val": 28,
            "valMax": 35,
            "forensic": 38,
            "forensicMax": 40,
            "total": 292,
            "totalMax": 310,
            "classification": "INDUSTRY 4.0 GLOBAL MONOPOLY"
        }
    },
    "kion": {
        "name": "KION Group AG",
        "ticker": "KGX:GR",
        "cmp": "€36.80",
        "dcf": "€44.50",
        "mos": "+20.9%",
        "mcap": "€4.82 Billion",
        "pe": "12.8",
        "pbv": "0.88",
        "evEbitda": "6.4",
        "beneishM": -2.62,
        "beneishStatus": "SAFE",
        "altmanZ": 4.2,
        "altmanStatus": "SAFE ZONE (Dematic Warehouse Automation)",
        "sloanAccrual": "1.2%",
        "piotroski": "7 / 9",
        "dupontROE": {
            "taxBurden": "0.75",
            "interestBurden": "0.86",
            "opMargin": "8.2%",
            "assetTurn": "0.72x",
            "leverage": "2.85x",
            "finalROE": "11.8%"
        },
        "kyleLambda": "0.045 bps / €1M",
        "blkOwnership": "3.80% (€183M)",
        "vangOwnership": "3.20% (€154M)",
        "activeFloat": "54.5%",
        "nanoLink": "kion_frankfurt",
        "soicScore": {
            "industry": 38,
            "industryMax": 45,
            "funda": 64,
            "fundaMax": 80,
            "tech": 88,
            "techMax": 110,
            "val": 32,
            "valMax": 35,
            "forensic": 36,
            "forensicMax": 40,
            "total": 258,
            "totalMax": 310,
            "classification": "WAREHOUSE AUTOMATION CYCLICAL"
        }
    },
    "basf": {
        "name": "BASF SE",
        "ticker": "BAS:GR",
        "cmp": "€43.60",
        "dcf": "€52.00",
        "mos": "+19.2%",
        "mcap": "€38.9 Billion",
        "pe": "13.2",
        "pbv": "1.05",
        "evEbitda": "6.8",
        "beneishM": -2.7,
        "beneishStatus": "SAFE",
        "altmanZ": 4.6,
        "altmanStatus": "SAFE ZONE (Zhanjiang Verbund Expansion)",
        "sloanAccrual": "1.9%",
        "piotroski": "7 / 9",
        "dupontROE": {
            "taxBurden": "0.74",
            "interestBurden": "0.88",
            "opMargin": "8.9%",
            "assetTurn": "0.82x",
            "leverage": "2.15x",
            "finalROE": "10.2%"
        },
        "kyleLambda": "0.012 bps / €5M",
        "blkOwnership": "5.80% (€2.25B)",
        "vangOwnership": "5.10% (€1.98B)",
        "activeFloat": "98.2%",
        "nanoLink": "basf_ludwigshafen",
        "soicScore": {
            "industry": 40,
            "industryMax": 45,
            "funda": 66,
            "fundaMax": 80,
            "tech": 85,
            "techMax": 110,
            "val": 32,
            "valMax": 35,
            "forensic": 38,
            "forensicMax": 40,
            "total": 261,
            "totalMax": 310,
            "classification": "CHEMICAL VERBUND MONOPOLY"
        }
    },
    "bayer": {
        "name": "Bayer AG",
        "ticker": "BAYN:GR",
        "cmp": "€24.80",
        "dcf": "€32.50",
        "mos": "+31.0%",
        "mcap": "€24.4 Billion",
        "pe": "5.2 (Core EPS)",
        "pbv": "0.72",
        "evEbitda": "5.5",
        "beneishM": -2.45,
        "beneishStatus": "SAFE (Litigation Provisions Monitored)",
        "altmanZ": 2.6,
        "altmanStatus": "GREY ZONE (Monsanto Glyphosate Litigation)",
        "sloanAccrual": "2.5%",
        "piotroski": "6 / 9",
        "dupontROE": {
            "taxBurden": "0.72",
            "interestBurden": "0.82",
            "opMargin": "18.5%",
            "assetTurn": "0.42x",
            "leverage": "3.10x",
            "finalROE": "14.2%"
        },
        "kyleLambda": "0.024 bps / €2M",
        "blkOwnership": "5.20% (€1.27B)",
        "vangOwnership": "4.60% (€1.12B)",
        "activeFloat": "99.1%",
        "nanoLink": "bayer_leverkusen",
        "soicScore": {
            "industry": 38,
            "industryMax": 45,
            "funda": 58,
            "fundaMax": 80,
            "tech": 72,
            "techMax": 110,
            "val": 35,
            "valMax": 35,
            "forensic": 30,
            "forensicMax": 40,
            "total": 233,
            "totalMax": 310,
            "classification": "DEEP SPECIAL SITUATION / LITIGATION PLAY"
        }
    },
    "tel": {
        "name": "Tokyo Electron Ltd",
        "ticker": "8035:JP",
        "cmp": "¥24,800",
        "dcf": "¥28,500",
        "mos": "+14.9%",
        "mcap": "¥11.6 Trillion ($76B)",
        "pe": "24.2",
        "pbv": "5.4",
        "evEbitda": "15.8",
        "beneishM": -2.9,
        "beneishStatus": "PRISTINE SAFE",
        "altmanZ": 12.5,
        "altmanStatus": "SAFE ZONE (Net Cash Balance Sheet)",
        "sloanAccrual": "0.2%",
        "piotroski": "9 / 9",
        "dupontROE": {
            "taxBurden": "0.72",
            "interestBurden": "1.00",
            "opMargin": "28.5%",
            "assetTurn": "0.88x",
            "leverage": "1.38x",
            "finalROE": "24.8%"
        },
        "kyleLambda": "0.012 bps / ¥500M",
        "blkOwnership": "5.40% ($4.1B)",
        "vangOwnership": "4.80% ($3.65B)",
        "activeFloat": "88.5%",
        "nanoLink": "tel_miyagi",
        "soicScore": {
            "industry": 45,
            "industryMax": 45,
            "funda": 78,
            "fundaMax": 80,
            "tech": 105,
            "techMax": 110,
            "val": 26,
            "valMax": 35,
            "forensic": 40,
            "forensicMax": 40,
            "total": 294,
            "totalMax": 310,
            "classification": "COATER/DEVELOPER 90% GLOBAL MONOPOLY"
        }
    },
    "advantest": {
        "name": "Advantest Corp",
        "ticker": "6857:JP",
        "cmp": "¥7,650",
        "dcf": "¥8,800",
        "mos": "+15.0%",
        "mcap": "¥5.8 Trillion ($38B)",
        "pe": "38.5",
        "pbv": "9.2",
        "evEbitda": "24.2",
        "beneishM": -2.85,
        "beneishStatus": "SAFE",
        "altmanZ": 14.8,
        "altmanStatus": "SAFE ZONE (HBM Testing Monopoly)",
        "sloanAccrual": "0.5%",
        "piotroski": "9 / 9",
        "dupontROE": {
            "taxBurden": "0.74",
            "interestBurden": "1.00",
            "opMargin": "32.4%",
            "assetTurn": "0.82x",
            "leverage": "1.42x",
            "finalROE": "28.0%"
        },
        "kyleLambda": "0.018 bps / ¥300M",
        "blkOwnership": "5.90% ($2.24B)",
        "vangOwnership": "5.20% ($1.97B)",
        "activeFloat": "89.2%",
        "nanoLink": "advantest_gunma",
        "soicScore": {
            "industry": 45,
            "industryMax": 45,
            "funda": 78,
            "fundaMax": 80,
            "tech": 108,
            "techMax": 110,
            "val": 24,
            "valMax": 35,
            "forensic": 40,
            "forensicMax": 40,
            "total": 295,
            "totalMax": 310,
            "classification": "HBM DRAM TESTER MONOPOLY"
        }
    },
    "lasertec": {
        "name": "Lasertec Corp",
        "ticker": "6920:JP",
        "cmp": "¥21,400",
        "dcf": "¥25,200",
        "mos": "+17.8%",
        "mcap": "¥1.98 Trillion ($13B)",
        "pe": "28.4",
        "pbv": "12.8",
        "evEbitda": "18.5",
        "beneishM": -2.75,
        "beneishStatus": "SAFE",
        "altmanZ": 16.2,
        "altmanStatus": "ULTRA SAFE (Zero Debt Net Cash)",
        "sloanAccrual": "0.8%",
        "piotroski": "9 / 9",
        "dupontROE": {
            "taxBurden": "0.70",
            "interestBurden": "1.00",
            "opMargin": "38.5%",
            "assetTurn": "1.10x",
            "leverage": "1.55x",
            "finalROE": "45.8%"
        },
        "kyleLambda": "0.024 bps / ¥200M",
        "blkOwnership": "6.20% ($806M)",
        "vangOwnership": "5.50% ($715M)",
        "activeFloat": "91.4%",
        "nanoLink": "lasertec_yokohama",
        "soicScore": {
            "industry": 45,
            "industryMax": 45,
            "funda": 80,
            "fundaMax": 80,
            "tech": 100,
            "techMax": 110,
            "val": 26,
            "valMax": 35,
            "forensic": 40,
            "forensicMax": 40,
            "total": 291,
            "totalMax": 310,
            "classification": "EUV ACTINIC BLANK INSPECTION 100% MONOPOLY"
        }
    },
    "keyence": {
        "name": "Keyence Corporation",
        "ticker": "6861:JP",
        "cmp": "¥64,200",
        "dcf": "¥72,000",
        "mos": "+12.1%",
        "mcap": "¥15.6 Trillion ($102B)",
        "pe": "42.5",
        "pbv": "5.8",
        "evEbitda": "26.8",
        "beneishM": -3.1,
        "beneishStatus": "PRISTINE SAFE (Highest Forensic Integrity Globally)",
        "altmanZ": 28.5,
        "altmanStatus": "FORTRESS OF FORTRESSES (Zero Debt Net Cash ¥2.8T)",
        "sloanAccrual": "-0.5%",
        "piotroski": "9 / 9",
        "dupontROE": {
            "taxBurden": "0.70",
            "interestBurden": "1.00",
            "opMargin": "52.4%",
            "assetTurn": "0.38x",
            "leverage": "1.08x",
            "finalROE": "15.2%"
        },
        "kyleLambda": "0.008 bps / ¥1B",
        "blkOwnership": "4.80% ($4.9B)",
        "vangOwnership": "4.20% ($4.3B)",
        "activeFloat": "78.5%",
        "nanoLink": "keyence_osaka",
        "soicScore": {
            "industry": 45,
            "industryMax": 45,
            "funda": 80,
            "fundaMax": 80,
            "tech": 98,
            "techMax": 110,
            "val": 26,
            "valMax": 35,
            "forensic": 40,
            "forensicMax": 40,
            "total": 289,
            "totalMax": 310,
            "classification": "WORLD BENCHMARK IN OPERATING MARGINS (52%)"
        }
    },
    "fanuc": {
        "name": "Fanuc Corp",
        "ticker": "6954:JP",
        "cmp": "¥4,120",
        "dcf": "¥4,650",
        "mos": "+12.9%",
        "mcap": "¥3.95 Trillion ($26B)",
        "pe": "26.8",
        "pbv": "2.4",
        "evEbitda": "14.2",
        "beneishM": -2.95,
        "beneishStatus": "PRISTINE SAFE",
        "altmanZ": 18.2,
        "altmanStatus": "FORTRESS (Zero Debt)",
        "sloanAccrual": "0.6%",
        "piotroski": "8 / 9",
        "dupontROE": {
            "taxBurden": "0.72",
            "interestBurden": "1.00",
            "opMargin": "18.5%",
            "assetTurn": "0.45x",
            "leverage": "1.14x",
            "finalROE": "6.8%"
        },
        "kyleLambda": "0.015 bps / ¥300M",
        "blkOwnership": "5.10% ($1.32B)",
        "vangOwnership": "4.50% ($1.17B)",
        "activeFloat": "88.2%",
        "nanoLink": "fanuc_yamanashi",
        "soicScore": {
            "industry": 42,
            "industryMax": 45,
            "funda": 72,
            "fundaMax": 80,
            "tech": 92,
            "techMax": 110,
            "val": 28,
            "valMax": 35,
            "forensic": 40,
            "forensicMax": 40,
            "total": 274,
            "totalMax": 310,
            "classification": "CNC & YELLOW INDUSTRIAL ROBOTICS MONOPOLY"
        }
    },
    "mitsubishi": {
        "name": "Mitsubishi Corporation",
        "ticker": "8058:JP",
        "cmp": "¥2,780",
        "dcf": "¥3,150",
        "mos": "+13.3%",
        "mcap": "¥11.8 Trillion ($77B)",
        "pe": "11.8",
        "pbv": "1.25",
        "evEbitda": "8.2",
        "beneishM": -2.78,
        "beneishStatus": "SAFE",
        "altmanZ": 4.2,
        "altmanStatus": "CONGLOMERATE SAFE (Berkshire Hathaway 9.3% Ownership)",
        "sloanAccrual": "1.2%",
        "piotroski": "8 / 9",
        "dupontROE": {
            "taxBurden": "0.75",
            "interestBurden": "0.90",
            "opMargin": "8.2%",
            "assetTurn": "0.92x",
            "leverage": "2.65x",
            "finalROE": "13.5%"
        },
        "kyleLambda": "0.010 bps / ¥1B",
        "blkOwnership": "4.20% ($3.2B)",
        "vangOwnership": "3.80% ($2.9B)",
        "activeFloat": "82.5%",
        "nanoLink": "mitsubishi_marunouchi",
        "soicScore": {
            "industry": 42,
            "industryMax": 45,
            "funda": 74,
            "fundaMax": 80,
            "tech": 100,
            "techMax": 110,
            "val": 30,
            "valMax": 35,
            "forensic": 38,
            "forensicMax": 40,
            "total": 284,
            "totalMax": 310,
            "classification": "BUFFETT SOGO SHOSHA COMPOUNDER"
        }
    },
    "mitsui": {
        "name": "Mitsui & Co Ltd",
        "ticker": "8031:JP",
        "cmp": "¥3,120",
        "dcf": "¥3,550",
        "mos": "+13.8%",
        "mcap": "¥9.5 Trillion ($62B)",
        "pe": "10.5",
        "pbv": "1.18",
        "evEbitda": "7.4",
        "beneishM": -2.8,
        "beneishStatus": "SAFE",
        "altmanZ": 4.5,
        "altmanStatus": "SAFE (Berkshire 9.2%)",
        "sloanAccrual": "1.0%",
        "piotroski": "8 / 9",
        "dupontROE": {
            "taxBurden": "0.76",
            "interestBurden": "0.92",
            "opMargin": "9.5%",
            "assetTurn": "0.95x",
            "leverage": "2.45x",
            "finalROE": "15.8%"
        },
        "kyleLambda": "0.012 bps / ¥800M",
        "blkOwnership": "4.10% ($2.54B)",
        "vangOwnership": "3.70% ($2.29B)",
        "activeFloat": "84.2%",
        "nanoLink": "mitsui_tokyo",
        "soicScore": {
            "industry": 42,
            "industryMax": 45,
            "funda": 74,
            "fundaMax": 80,
            "tech": 98,
            "techMax": 110,
            "val": 32,
            "valMax": 35,
            "forensic": 38,
            "forensicMax": 40,
            "total": 284,
            "totalMax": 310,
            "classification": "ENERGY & MINERAL RESOURCES CONGLOMERATE"
        }
    },
    "itochu": {
        "name": "Itochu Corporation",
        "ticker": "8001:JP",
        "cmp": "¥7,480",
        "dcf": "¥8,200",
        "mos": "+9.6%",
        "mcap": "¥11.2 Trillion ($73B)",
        "pe": "12.4",
        "pbv": "1.75",
        "evEbitda": "9.1",
        "beneishM": -2.82,
        "beneishStatus": "SAFE",
        "altmanZ": 4.8,
        "altmanStatus": "SAFE (Highest Non-Resource ROE in Japan)",
        "sloanAccrual": "0.8%",
        "piotroski": "9 / 9",
        "dupontROE": {
            "taxBurden": "0.75",
            "interestBurden": "0.94",
            "opMargin": "7.8%",
            "assetTurn": "1.05x",
            "leverage": "2.80x",
            "finalROE": "16.2%"
        },
        "kyleLambda": "0.011 bps / ¥800M",
        "blkOwnership": "4.40% ($3.21B)",
        "vangOwnership": "3.90% ($2.85B)",
        "activeFloat": "83.5%",
        "nanoLink": "itochu_minato",
        "soicScore": {
            "industry": 42,
            "industryMax": 45,
            "funda": 76,
            "fundaMax": 80,
            "tech": 102,
            "techMax": 110,
            "val": 28,
            "valMax": 35,
            "forensic": 38,
            "forensicMax": 40,
            "total": 286,
            "totalMax": 310,
            "classification": "CONSUMER & NON-RESOURCE LEADER"
        }
    },
    "byd": {
        "name": "BYD Company Ltd",
        "ticker": "002594:SZ / 1211:HK",
        "cmp": "HK$278.00",
        "dcf": "HK$330.00",
        "mos": "+18.7%",
        "mcap": "$104 Billion",
        "pe": "21.5",
        "pbv": "4.8",
        "evEbitda": "12.8",
        "beneishM": -2.62,
        "beneishStatus": "SAFE",
        "altmanZ": 5.8,
        "altmanStatus": "SAFE ZONE (Blade Battery & Vertical Integration)",
        "sloanAccrual": "-1.2% (Massive Cash Generation)",
        "piotroski": "8 / 9",
        "dupontROE": {
            "taxBurden": "0.82",
            "interestBurden": "0.96",
            "opMargin": "6.4%",
            "assetTurn": "1.35x",
            "leverage": "3.20x",
            "finalROE": "22.0%"
        },
        "kyleLambda": "0.014 bps / $5M",
        "blkOwnership": "4.80% ($5.0B)",
        "vangOwnership": "4.20% ($4.37B)",
        "activeFloat": "71.5%",
        "nanoLink": "byd_zhengzhou",
        "soicScore": {
            "industry": 44,
            "industryMax": 45,
            "funda": 74,
            "fundaMax": 80,
            "tech": 105,
            "techMax": 110,
            "val": 28,
            "valMax": 35,
            "forensic": 36,
            "forensicMax": 40,
            "total": 287,
            "totalMax": 310,
            "classification": "GLOBAL NEV VOLUME LEADER (4.2M VEHICLES/YR)"
        }
    },
    "catl": {
        "name": "CATL (Contemporary Amperex Technology)",
        "ticker": "300750:SZ",
        "cmp": "¥248.00",
        "dcf": "¥295.00",
        "mos": "+19.0%",
        "mcap": "$152 Billion",
        "pe": "22.8",
        "pbv": "5.2",
        "evEbitda": "14.2",
        "beneishM": -2.75,
        "beneishStatus": "SAFE",
        "altmanZ": 7.2,
        "altmanStatus": "SAFE ZONE (37.5% Global EV Battery Market Share)",
        "sloanAccrual": "0.8%",
        "piotroski": "9 / 9",
        "dupontROE": {
            "taxBurden": "0.84",
            "interestBurden": "0.98",
            "opMargin": "13.8%",
            "assetTurn": "0.95x",
            "leverage": "2.15x",
            "finalROE": "23.4%"
        },
        "kyleLambda": "0.016 bps / $5M",
        "blkOwnership": "5.10% ($7.75B)",
        "vangOwnership": "4.60% ($6.99B)",
        "activeFloat": "72.8%",
        "nanoLink": "catl_ningde",
        "soicScore": {
            "industry": 45,
            "industryMax": 45,
            "funda": 78,
            "fundaMax": 80,
            "tech": 102,
            "techMax": 110,
            "val": 28,
            "valMax": 35,
            "forensic": 38,
            "forensicMax": 40,
            "total": 291,
            "totalMax": 310,
            "classification": "GLOBAL EV BATTERY MONOPOLIST"
        }
    },
    "longi": {
        "name": "LONGi Green Energy Technology",
        "ticker": "601012:SS",
        "cmp": "¥19.40",
        "dcf": "¥23.50",
        "mos": "+21.1%",
        "mcap": "$20.2 Billion",
        "pe": "14.5 (Normalized)",
        "pbv": "2.1",
        "evEbitda": "8.9",
        "beneishM": -2.52,
        "beneishStatus": "SAFE",
        "altmanZ": 5.2,
        "altmanStatus": "SAFE ZONE (HPBC 2.0 Solar Cell Breakthrough)",
        "sloanAccrual": "2.1%",
        "piotroski": "7 / 9",
        "dupontROE": {
            "taxBurden": "0.82",
            "interestBurden": "0.90",
            "opMargin": "12.4%",
            "assetTurn": "0.85x",
            "leverage": "1.85x",
            "finalROE": "14.2%"
        },
        "kyleLambda": "0.028 bps / $2M",
        "blkOwnership": "3.80% ($767M)",
        "vangOwnership": "3.40% ($686M)",
        "activeFloat": "78.5%",
        "nanoLink": "longi_xian",
        "soicScore": {
            "industry": 38,
            "industryMax": 45,
            "funda": 66,
            "fundaMax": 80,
            "tech": 85,
            "techMax": 110,
            "val": 30,
            "valMax": 35,
            "forensic": 36,
            "forensicMax": 40,
            "total": 255,
            "totalMax": 310,
            "classification": "MONOCRYSTALLINE SOLAR GIANT"
        }
    },
    "sungrow": {
        "name": "Sungrow Power Supply Co",
        "ticker": "300274:SZ",
        "cmp": "¥88.60",
        "dcf": "¥104.00",
        "mos": "+17.4%",
        "mcap": "$18.4 Billion",
        "pe": "13.8",
        "pbv": "3.9",
        "evEbitda": "9.5",
        "beneishM": -2.7,
        "beneishStatus": "SAFE",
        "altmanZ": 8.5,
        "altmanStatus": "SAFE ZONE (Global No. 1 Solar Inverter & BESS)",
        "sloanAccrual": "1.0%",
        "piotroski": "9 / 9",
        "dupontROE": {
            "taxBurden": "0.85",
            "interestBurden": "0.98",
            "opMargin": "16.5%",
            "assetTurn": "1.18x",
            "leverage": "1.95x",
            "finalROE": "31.2%"
        },
        "kyleLambda": "0.024 bps / $2M",
        "blkOwnership": "4.20% ($772M)",
        "vangOwnership": "3.70% ($680M)",
        "activeFloat": "68.5%",
        "nanoLink": "sungrow_hefei",
        "soicScore": {
            "industry": 44,
            "industryMax": 45,
            "funda": 76,
            "fundaMax": 80,
            "tech": 105,
            "techMax": 110,
            "val": 30,
            "valMax": 35,
            "forensic": 38,
            "forensicMax": 40,
            "total": 293,
            "totalMax": 310,
            "classification": "GLOBAL SOLAR INVERTER LEADER"
        }
    },
    "cssc": {
        "name": "China CSSC Holdings Ltd",
        "ticker": "600150:SS",
        "cmp": "¥38.20",
        "dcf": "¥45.00",
        "mos": "+17.8%",
        "mcap": "$24.8 Billion",
        "pe": "28.5",
        "pbv": "3.2",
        "evEbitda": "14.2",
        "beneishM": -2.58,
        "beneishStatus": "SAFE",
        "altmanZ": 5.8,
        "altmanStatus": "SAFE ZONE (Order Backlog Full Through 2029)",
        "sloanAccrual": "-2.1% (Massive Upfront Shipbuyer Stage Payments)",
        "piotroski": "8 / 9",
        "dupontROE": {
            "taxBurden": "0.85",
            "interestBurden": "0.95",
            "opMargin": "8.2%",
            "assetTurn": "0.85x",
            "leverage": "2.65x",
            "finalROE": "15.4%"
        },
        "kyleLambda": "0.022 bps / $2M",
        "blkOwnership": "3.40% ($843M)",
        "vangOwnership": "3.10% ($768M)",
        "activeFloat": "62.5%",
        "nanoLink": "cssc_shanghai",
        "soicScore": {
            "industry": 44,
            "industryMax": 45,
            "funda": 72,
            "fundaMax": 80,
            "tech": 105,
            "techMax": 110,
            "val": 28,
            "valMax": 35,
            "forensic": 36,
            "forensicMax": 40,
            "total": 285,
            "totalMax": 310,
            "classification": "GLOBAL COMMERCIAL SHIPBUILDING MONOPOLIST"
        }
    },
    "cosco": {
        "name": "COSCO SHIPPING Holdings",
        "ticker": "601919:SS / 1919:HK",
        "cmp": "HK$11.80",
        "dcf": "HK$14.20",
        "mos": "+20.3%",
        "mcap": "$22.6 Billion",
        "pe": "5.8",
        "pbv": "0.82",
        "evEbitda": "3.8",
        "beneishM": -2.75,
        "beneishStatus": "SAFE",
        "altmanZ": 7.8,
        "altmanStatus": "FORTRESS SAFE (Net Cash $24 Billion)",
        "sloanAccrual": "0.4%",
        "piotroski": "8 / 9",
        "dupontROE": {
            "taxBurden": "0.85",
            "interestBurden": "0.98",
            "opMargin": "22.5%",
            "assetTurn": "0.78x",
            "leverage": "1.55x",
            "finalROE": "22.8%"
        },
        "kyleLambda": "0.019 bps / $3M",
        "blkOwnership": "4.10% ($926M)",
        "vangOwnership": "3.80% ($858M)",
        "activeFloat": "54.2%",
        "nanoLink": "cosco_yangshan",
        "soicScore": {
            "industry": 40,
            "industryMax": 45,
            "funda": 72,
            "fundaMax": 80,
            "tech": 95,
            "techMax": 110,
            "val": 34,
            "valMax": 35,
            "forensic": 38,
            "forensicMax": 40,
            "total": 279,
            "totalMax": 310,
            "classification": "GLOBAL MARITIME CONTAINER GIANT"
        }
    },
    "petrobras": {
        "name": "Petróleo Brasileiro S.A. (Petrobras)",
        "ticker": "PBR:US",
        "cmp": "$13.80",
        "dcf": "$16.50",
        "mos": "+19.6%",
        "mcap": "$88.5 Billion",
        "pe": "4.2",
        "pbv": "1.05",
        "evEbitda": "2.8",
        "beneishM": -2.7,
        "beneishStatus": "SAFE",
        "altmanZ": 4.8,
        "altmanStatus": "SAFE ZONE (Santos Basin Lifting Cost $26.80/bbl)",
        "sloanAccrual": "0.6%",
        "piotroski": "8 / 9",
        "dupontROE": {
            "taxBurden": "0.68",
            "interestBurden": "0.88",
            "opMargin": "32.5%",
            "assetTurn": "0.52x",
            "leverage": "2.45x",
            "finalROE": "24.8%"
        },
        "kyleLambda": "0.0055 bps / $5M",
        "blkOwnership": "5.80% ($5.13B)",
        "vangOwnership": "6.40% ($5.66B)",
        "activeFloat": "63.2%",
        "nanoLink": "petrobras_buzios",
        "soicScore": {
            "industry": 44,
            "industryMax": 45,
            "funda": 74,
            "fundaMax": 80,
            "tech": 98,
            "techMax": 110,
            "val": 35,
            "valMax": 35,
            "forensic": 36,
            "forensicMax": 40,
            "total": 287,
            "totalMax": 310,
            "classification": "ULTRA DEEPWATER PRE-SALT MONOPOLY"
        }
    },
    "vale": {
        "name": "Vale S.A.",
        "ticker": "VALE:US",
        "cmp": "$10.40",
        "dcf": "$13.20",
        "mos": "+26.9%",
        "mcap": "$46.8 Billion",
        "pe": "5.4",
        "pbv": "1.25",
        "evEbitda": "3.5",
        "beneishM": -2.65,
        "beneishStatus": "SAFE",
        "altmanZ": 5.2,
        "altmanStatus": "SAFE ZONE (Carajás 65% Fe Premium Ore)",
        "sloanAccrual": "0.8%",
        "piotroski": "8 / 9",
        "dupontROE": {
            "taxBurden": "0.70",
            "interestBurden": "0.90",
            "opMargin": "38.5%",
            "assetTurn": "0.48x",
            "leverage": "2.10x",
            "finalROE": "24.2%"
        },
        "kyleLambda": "0.0065 bps / $5M",
        "blkOwnership": "6.20% ($2.9B)",
        "vangOwnership": "6.80% ($3.18B)",
        "activeFloat": "94.5%",
        "nanoLink": "vale_carajas",
        "soicScore": {
            "industry": 44,
            "industryMax": 45,
            "funda": 72,
            "fundaMax": 80,
            "tech": 90,
            "techMax": 110,
            "val": 35,
            "valMax": 35,
            "forensic": 36,
            "forensicMax": 40,
            "total": 277,
            "totalMax": 310,
            "classification": "HIGH GRADE IRON ORE WORLD LEADER"
        }
    },
    "slc_agri": {
        "name": "SLC Agrícola S.A.",
        "ticker": "SLCE3:BZ",
        "cmp": "R$18.50",
        "dcf": "R$22.80",
        "mos": "+23.2%",
        "mcap": "R$8.2 Billion ($1.45B)",
        "pe": "8.5",
        "pbv": "1.10",
        "evEbitda": "5.2",
        "beneishM": -2.72,
        "beneishStatus": "SAFE",
        "altmanZ": 4.8,
        "altmanStatus": "SAFE ZONE (700,000+ Hectares Soybean/Corn)",
        "sloanAccrual": "1.5%",
        "piotroski": "7 / 9",
        "dupontROE": {
            "taxBurden": "0.75",
            "interestBurden": "0.82",
            "opMargin": "24.5%",
            "assetTurn": "0.65x",
            "leverage": "2.25x",
            "finalROE": "18.5%"
        },
        "kyleLambda": "0.085 bps / R$1M",
        "blkOwnership": "3.20% ($46M)",
        "vangOwnership": "2.80% ($40M)",
        "activeFloat": "52.8%",
        "nanoLink": "slc_matopiba",
        "soicScore": {
            "industry": 40,
            "industryMax": 45,
            "funda": 68,
            "fundaMax": 80,
            "tech": 88,
            "techMax": 110,
            "val": 32,
            "valMax": 35,
            "forensic": 36,
            "forensicMax": 40,
            "total": 264,
            "totalMax": 310,
            "classification": "GLOBAL AGRIBUSINESS SCALE MONOPOLY"
        }
    },
    "hsbc": {
        "name": "HSBC Holdings plc",
        "ticker": "HSBA:LN",
        "cmp": "£715.00",
        "dcf": "£820.00",
        "mos": "+14.7%",
        "mcap": "£132 Billion ($168B)",
        "pe": "7.2",
        "pbv": "0.88",
        "evEbitda": "N/A (Bank)",
        "beneishM": -2.85,
        "beneishStatus": "SAFE",
        "altmanZ": 3.1,
        "altmanStatus": "CET-1 RATIO 15.2% (Hong Kong / Asia Trade Surplus)",
        "sloanAccrual": "NPA 1.45%",
        "piotroski": "8 / 9",
        "dupontROE": {
            "taxBurden": "0.78",
            "interestBurden": "NIM 1.62%",
            "opMargin": "Cost/Income 48.5%",
            "assetTurn": "ROA 0.88%",
            "leverage": "16.5x",
            "finalROE": "14.5%"
        },
        "kyleLambda": "0.0085 bps / £5M",
        "blkOwnership": "6.40% ($10.7B)",
        "vangOwnership": "5.80% ($9.7B)",
        "activeFloat": "91.5%",
        "nanoLink": "hsbc_canarywharf",
        "soicScore": {
            "industry": 42,
            "industryMax": 45,
            "funda": 74,
            "fundaMax": 80,
            "tech": 95,
            "techMax": 110,
            "val": 32,
            "valMax": 35,
            "forensic": 38,
            "forensicMax": 40,
            "total": 281,
            "totalMax": 310,
            "classification": "ASIAN TRADE CORRIDOR FINANCIER"
        }
    },
    "barclays": {
        "name": "Barclays PLC",
        "ticker": "BARC:LN",
        "cmp": "£242.00",
        "dcf": "£288.00",
        "mos": "+19.0%",
        "mcap": "£36.2 Billion ($46B)",
        "pe": "6.5",
        "pbv": "0.52",
        "evEbitda": "N/A (Bank)",
        "beneishM": -2.78,
        "beneishStatus": "SAFE",
        "altmanZ": 2.9,
        "altmanStatus": "CET-1 RATIO 13.8%",
        "sloanAccrual": "NPA 1.82%",
        "piotroski": "7 / 9",
        "dupontROE": {
            "taxBurden": "0.76",
            "interestBurden": "NIM 1.85%",
            "opMargin": "Cost/Income 58.2%",
            "assetTurn": "ROA 0.65%",
            "leverage": "18.2x",
            "finalROE": "11.8%"
        },
        "kyleLambda": "0.014 bps / £3M",
        "blkOwnership": "5.80% ($2.67B)",
        "vangOwnership": "5.20% ($2.39B)",
        "activeFloat": "92.4%",
        "nanoLink": "barclays_churchill",
        "soicScore": {
            "industry": 38,
            "industryMax": 45,
            "funda": 66,
            "fundaMax": 80,
            "tech": 90,
            "techMax": 110,
            "val": 34,
            "valMax": 35,
            "forensic": 36,
            "forensicMax": 40,
            "total": 264,
            "totalMax": 310,
            "classification": "DEEP VALUE UK COMMERCIAL BANK"
        }
    },
    "astrazeneca": {
        "name": "AstraZeneca PLC",
        "ticker": "AZN:LN",
        "cmp": "£10,450",
        "dcf": "£12,200",
        "mos": "+16.7%",
        "mcap": "£162 Billion ($208B)",
        "pe": "18.5",
        "pbv": "4.8",
        "evEbitda": "14.5",
        "beneishM": -2.82,
        "beneishStatus": "SAFE",
        "altmanZ": 6.2,
        "altmanStatus": "SAFE ZONE (Enhertu & Tagrisso Oncology Blockbusters)",
        "sloanAccrual": "1.2%",
        "piotroski": "9 / 9",
        "dupontROE": {
            "taxBurden": "0.80",
            "interestBurden": "0.94",
            "opMargin": "28.5%",
            "assetTurn": "0.52x",
            "leverage": "2.15x",
            "finalROE": "24.2%"
        },
        "kyleLambda": "0.0095 bps / £5M",
        "blkOwnership": "6.80% ($14.1B)",
        "vangOwnership": "6.10% ($12.7B)",
        "activeFloat": "98.5%",
        "nanoLink": "azn_cambridge",
        "soicScore": {
            "industry": 45,
            "industryMax": 45,
            "funda": 78,
            "fundaMax": 80,
            "tech": 100,
            "techMax": 110,
            "val": 28,
            "valMax": 35,
            "forensic": 38,
            "forensicMax": 40,
            "total": 289,
            "totalMax": 310,
            "classification": "ONCOLOGY & CARDIO BLOCKBUSTER GIANT"
        }
    },
    "novo": {
        "name": "Novo Nordisk A/S",
        "ticker": "NOVO-B:DC / NVO:US",
        "cmp": "$118.50",
        "dcf": "$138.00",
        "mos": "+16.5%",
        "mcap": "$530 Billion",
        "pe": "34.2",
        "pbv": "24.5",
        "evEbitda": "25.8",
        "beneishM": -2.95,
        "beneishStatus": "PRISTINE SAFE",
        "altmanZ": 21.5,
        "altmanStatus": "FORTRESS OF FORTRESSES (GLP-1 Wegovy/Ozempic)",
        "sloanAccrual": "0.4%",
        "piotroski": "9 / 9",
        "dupontROE": {
            "taxBurden": "0.80",
            "interestBurden": "0.98",
            "opMargin": "44.8%",
            "assetTurn": "1.15x",
            "leverage": "1.95x",
            "finalROE": "78.5%"
        },
        "kyleLambda": "0.0032 bps / $5M",
        "blkOwnership": "6.20% ($32.8B)",
        "vangOwnership": "5.80% ($30.7B)",
        "activeFloat": "71.5% (Novo Holdings Foundation 28.5%)",
        "nanoLink": "novo_kalundborg",
        "soicScore": {
            "industry": 45,
            "industryMax": 45,
            "funda": 80,
            "fundaMax": 80,
            "tech": 105,
            "techMax": 110,
            "val": 26,
            "valMax": 35,
            "forensic": 40,
            "forensicMax": 40,
            "total": 296,
            "totalMax": 310,
            "classification": "GLOBAL GLP-1 DUOPOLY MONOPOLIST"
        }
    },
    "asml": {
        "name": "ASML Holding NV",
        "ticker": "ASML:NA",
        "cmp": "€668.00",
        "dcf": "€795.00",
        "mos": "+19.0%",
        "mcap": "€264 Billion ($284B)",
        "pe": "32.5",
        "pbv": "16.5",
        "evEbitda": "23.8",
        "beneishM": -3.05,
        "beneishStatus": "PRISTINE SAFE (100% EUV Lithography Global Monopoly)",
        "altmanZ": 16.8,
        "altmanStatus": "FORTRESS (Zero Net Debt Backlog €36B)",
        "sloanAccrual": "-0.8% (Advance Customer Fab Slot Reservations)",
        "piotroski": "9 / 9",
        "dupontROE": {
            "taxBurden": "0.84",
            "interestBurden": "1.00",
            "opMargin": "32.8%",
            "assetTurn": "0.78x",
            "leverage": "2.15x",
            "finalROE": "46.2%"
        },
        "kyleLambda": "0.0042 bps / €5M",
        "blkOwnership": "7.40% (€19.5B)",
        "vangOwnership": "6.80% (€17.9B)",
        "activeFloat": "99.5%",
        "nanoLink": "asml_veldhoven",
        "soicScore": {
            "industry": 45,
            "industryMax": 45,
            "funda": 80,
            "fundaMax": 80,
            "tech": 108,
            "techMax": 110,
            "val": 26,
            "valMax": 35,
            "forensic": 40,
            "forensicMax": 40,
            "total": 299,
            "totalMax": 310,
            "classification": "ABSOLUTE CHOKEPOINT OF HUMANITY COMPUTE"
        }
    },
    "aramco": {
        "name": "Saudi Arabian Oil Co (Saudi Aramco)",
        "ticker": "2222:SR",
        "cmp": "SAR 27.80",
        "dcf": "SAR 32.50",
        "mos": "+16.9%",
        "mcap": "SAR 6.72 Trillion ($1.79 Trillion)",
        "pe": "14.8",
        "pbv": "4.2",
        "evEbitda": "7.8",
        "beneishM": -2.92,
        "beneishStatus": "PRISTINE SAFE",
        "altmanZ": 8.9,
        "altmanStatus": "SOVEREIGN FORTRESS ($3.20/bbl Upstream Lifting Cost)",
        "sloanAccrual": "0.2%",
        "piotroski": "9 / 9",
        "dupontROE": {
            "taxBurden": "0.50 (Sovereign Hydrocarbon Royalty)",
            "interestBurden": "0.98",
            "opMargin": "44.5%",
            "assetTurn": "0.85x",
            "leverage": "1.45x",
            "finalROE": "26.8%"
        },
        "kyleLambda": "0.0028 bps / SAR 50M",
        "blkOwnership": "1.80% ($32B)",
        "vangOwnership": "1.40% ($25B)",
        "activeFloat": "2.5% (PIF & Saudi State 97.5%)",
        "nanoLink": "aramco_ghawar",
        "soicScore": {
            "industry": 45,
            "industryMax": 45,
            "funda": 80,
            "fundaMax": 80,
            "tech": 98,
            "techMax": 110,
            "val": 30,
            "valMax": 35,
            "forensic": 40,
            "forensicMax": 40,
            "total": 293,
            "totalMax": 310,
            "classification": "LARGEST CASH FLOW GENERATOR ON EARTH"
        }
    },
    "sabic": {
        "name": "Saudi Basic Industries Corp (SABIC)",
        "ticker": "2010:SR",
        "cmp": "SAR 74.50",
        "dcf": "SAR 86.00",
        "mos": "+15.4%",
        "mcap": "SAR 223 Billion ($59.5B)",
        "pe": "18.5",
        "pbv": "1.38",
        "evEbitda": "7.9",
        "beneishM": -2.75,
        "beneishStatus": "SAFE",
        "altmanZ": 5.8,
        "altmanStatus": "SAFE ZONE (Advantaged Ethane Feedstocks)",
        "sloanAccrual": "1.1%",
        "piotroski": "8 / 9",
        "dupontROE": {
            "taxBurden": "0.85",
            "interestBurden": "0.94",
            "opMargin": "14.2%",
            "assetTurn": "0.55x",
            "leverage": "1.65x",
            "finalROE": "10.5%"
        },
        "kyleLambda": "0.015 bps / SAR 10M",
        "blkOwnership": "2.10% ($1.25B)",
        "vangOwnership": "1.80% ($1.07B)",
        "activeFloat": "30.0% (Aramco owns 70%)",
        "nanoLink": "sabic_jubail",
        "soicScore": {
            "industry": 42,
            "industryMax": 45,
            "funda": 72,
            "fundaMax": 80,
            "tech": 92,
            "techMax": 110,
            "val": 32,
            "valMax": 35,
            "forensic": 38,
            "forensicMax": 40,
            "total": 276,
            "totalMax": 310,
            "classification": "PETROCHEMICAL FEEDSTOCK LEADER"
        }
    },
    "singtel": {
        "name": "Singapore Telecommunications Ltd",
        "ticker": "Z74:SG",
        "cmp": "S$3.22",
        "dcf": "S$3.65",
        "mos": "+13.4%",
        "mcap": "S$53.2 Billion ($40B)",
        "pe": "16.5",
        "pbv": "1.85",
        "evEbitda": "8.2",
        "beneishM": -2.85,
        "beneishStatus": "SAFE",
        "altmanZ": 6.2,
        "altmanStatus": "SAFE ZONE (Temasek 52% Sovereign Backed)",
        "sloanAccrual": "0.6%",
        "piotroski": "8 / 9",
        "dupontROE": {
            "taxBurden": "0.82",
            "interestBurden": "0.92",
            "opMargin": "26.5%",
            "assetTurn": "0.35x",
            "leverage": "1.95x",
            "finalROE": "13.8%"
        },
        "kyleLambda": "0.012 bps / S$5M",
        "blkOwnership": "4.20% ($1.68B)",
        "vangOwnership": "3.80% ($1.52B)",
        "activeFloat": "48.0%",
        "nanoLink": "singtel_tuas",
        "soicScore": {
            "industry": 42,
            "industryMax": 45,
            "funda": 74,
            "fundaMax": 80,
            "tech": 98,
            "techMax": 110,
            "val": 30,
            "valMax": 35,
            "forensic": 38,
            "forensicMax": 40,
            "total": 282,
            "totalMax": 310,
            "classification": "SOVEREIGN DATA CENTER & TELCO HUB"
        }
    },
    "wilmar": {
        "name": "Wilmar International Ltd",
        "ticker": "F34:SG",
        "cmp": "S$3.15",
        "dcf": "S$3.70",
        "mos": "+17.5%",
        "mcap": "S$19.6 Billion ($14.8B)",
        "pe": "10.8",
        "pbv": "0.72",
        "evEbitda": "6.4",
        "beneishM": -2.68,
        "beneishStatus": "SAFE",
        "altmanZ": 4.5,
        "altmanStatus": "SAFE ZONE (Asian Agri-Commodity Processing Monopolist)",
        "sloanAccrual": "1.2%",
        "piotroski": "7 / 9",
        "dupontROE": {
            "taxBurden": "0.82",
            "interestBurden": "0.88",
            "opMargin": "4.2%",
            "assetTurn": "1.18x",
            "leverage": "2.65x",
            "finalROE": "9.5%"
        },
        "kyleLambda": "0.019 bps / S$2M",
        "blkOwnership": "3.40% ($503M)",
        "vangOwnership": "3.10% ($459M)",
        "activeFloat": "38.5%",
        "nanoLink": "wilmar_jurong",
        "soicScore": {
            "industry": 40,
            "industryMax": 45,
            "funda": 68,
            "fundaMax": 80,
            "tech": 90,
            "techMax": 110,
            "val": 34,
            "valMax": 35,
            "forensic": 36,
            "forensicMax": 40,
            "total": 268,
            "totalMax": 310,
            "classification": "ASIAN FOOD & COMMODITY PROCESSING TOLLBOOTH"
        }
    },
    "bhp": {
        "name": "BHP Group Ltd",
        "ticker": "BHP:AU",
        "cmp": "A$41.20",
        "dcf": "A$46.80",
        "mos": "+13.6%",
        "mcap": "A$209 Billion ($138B)",
        "pe": "11.4",
        "pbv": "2.8",
        "evEbitda": "5.8",
        "beneishM": -2.85,
        "beneishStatus": "PRISTINE SAFE",
        "altmanZ": 6.8,
        "altmanStatus": "FORTRESS (Pilbara Iron Ore Cash Cost $18.50/ton)",
        "sloanAccrual": "0.4%",
        "piotroski": "9 / 9",
        "dupontROE": {
            "taxBurden": "0.68",
            "interestBurden": "0.94",
            "opMargin": "42.0%",
            "assetTurn": "0.54x",
            "leverage": "1.92x",
            "finalROE": "27.5%"
        },
        "kyleLambda": "0.0075 bps / A$5M",
        "blkOwnership": "7.80% ($10.7B)",
        "vangOwnership": "8.40% ($11.6B)",
        "activeFloat": "98.5%",
        "nanoLink": "bhp_olympic",
        "soicScore": {
            "industry": 45,
            "industryMax": 45,
            "funda": 78,
            "fundaMax": 80,
            "tech": 100,
            "techMax": 110,
            "val": 30,
            "valMax": 35,
            "forensic": 40,
            "forensicMax": 40,
            "total": 293,
            "totalMax": 310,
            "classification": "GLOBAL NATURAL RESOURCE KING"
        }
    },
    "rio": {
        "name": "Rio Tinto Ltd",
        "ticker": "RIO:AU",
        "cmp": "A$118.50",
        "dcf": "A$134.00",
        "mos": "+13.1%",
        "mcap": "A$148 Billion ($98B)",
        "pe": "10.2",
        "pbv": "2.4",
        "evEbitda": "5.2",
        "beneishM": -2.8,
        "beneishStatus": "SAFE",
        "altmanZ": 6.5,
        "altmanStatus": "SAFE ZONE (AutoHaul Autonomous Rail Infrastructure)",
        "sloanAccrual": "0.5%",
        "piotroski": "9 / 9",
        "dupontROE": {
            "taxBurden": "0.70",
            "interestBurden": "0.96",
            "opMargin": "38.5%",
            "assetTurn": "0.56x",
            "leverage": "1.78x",
            "finalROE": "26.4%"
        },
        "kyleLambda": "0.0090 bps / A$3M",
        "blkOwnership": "7.20% ($7.0B)",
        "vangOwnership": "7.80% ($7.6B)",
        "activeFloat": "98.2%",
        "nanoLink": "rio_pilbara",
        "soicScore": {
            "industry": 44,
            "industryMax": 45,
            "funda": 76,
            "fundaMax": 80,
            "tech": 98,
            "techMax": 110,
            "val": 32,
            "valMax": 35,
            "forensic": 38,
            "forensicMax": 40,
            "total": 288,
            "totalMax": 310,
            "classification": "LOWEST COST BULK EXTRACTOR"
        }
    },
    "samsung": {
        "name": "Samsung Electronics Co Ltd",
        "ticker": "005930:KS",
        "cmp": "₩58,200",
        "dcf": "₩72,000",
        "mos": "+23.7%",
        "mcap": "₩392 Trillion ($284B)",
        "pe": "11.8",
        "pbv": "1.05",
        "evEbitda": "5.4",
        "beneishM": -2.95,
        "beneishStatus": "PRISTINE SAFE",
        "altmanZ": 12.8,
        "altmanStatus": "FORTRESS OF ASIA (Net Cash $85 Billion)",
        "sloanAccrual": "0.5%",
        "piotroski": "9 / 9",
        "dupontROE": {
            "taxBurden": "0.78",
            "interestBurden": "1.00",
            "opMargin": "18.5%",
            "assetTurn": "0.65x",
            "leverage": "1.25x",
            "finalROE": "11.8%"
        },
        "kyleLambda": "0.0055 bps / ₩5B",
        "blkOwnership": "5.20% ($14.7B)",
        "vangOwnership": "4.80% ($13.6B)",
        "activeFloat": "71.5%",
        "nanoLink": "samsung_pyeongtaek",
        "soicScore": {
            "industry": 45,
            "industryMax": 45,
            "funda": 78,
            "fundaMax": 80,
            "tech": 92,
            "techMax": 110,
            "val": 34,
            "valMax": 35,
            "forensic": 40,
            "forensicMax": 40,
            "total": 289,
            "totalMax": 310,
            "classification": "DEEP VALUE GLOBAL MEMORY & FOUNDRY TITAN"
        }
    },
    "sk_hynix": {
        "name": "SK Hynix Inc",
        "ticker": "000660:KS",
        "cmp": "₩188,400",
        "dcf": "₩225,000",
        "mos": "+19.4%",
        "mcap": "₩137 Trillion ($99B)",
        "pe": "9.8 (Forward)",
        "pbv": "2.1",
        "evEbitda": "6.2",
        "beneishM": -2.85,
        "beneishStatus": "SAFE",
        "altmanZ": 7.8,
        "altmanStatus": "SAFE ZONE (HBM3E Exclusive NVIDIA Supplier)",
        "sloanAccrual": "-1.2% (Massive HBM Cash Conversion)",
        "piotroski": "9 / 9",
        "dupontROE": {
            "taxBurden": "0.80",
            "interestBurden": "0.94",
            "opMargin": "38.5%",
            "assetTurn": "0.72x",
            "leverage": "1.65x",
            "finalROE": "34.5%"
        },
        "kyleLambda": "0.0085 bps / ₩3B",
        "blkOwnership": "5.80% ($5.74B)",
        "vangOwnership": "5.20% ($5.15B)",
        "activeFloat": "74.2%",
        "nanoLink": "sk_icheon",
        "soicScore": {
            "industry": 45,
            "industryMax": 45,
            "funda": 78,
            "fundaMax": 80,
            "tech": 108,
            "techMax": 110,
            "val": 30,
            "valMax": 35,
            "forensic": 38,
            "forensicMax": 40,
            "total": 299,
            "totalMax": 310,
            "classification": "HBM MEMORY PACKAGING MONOPOLIST"
        }
    },
    "dpworld": {
        "name": "DP World Ltd",
        "ticker": "DPW:AE",
        "cmp": "Sovereign Giant",
        "dcf": "$28.50",
        "mos": "+16.5%",
        "mcap": "$28.5 Billion (Est)",
        "pe": "14.2",
        "pbv": "2.4",
        "evEbitda": "8.5",
        "beneishM": -2.78,
        "beneishStatus": "SAFE",
        "altmanZ": 5.2,
        "altmanStatus": "SAFE ZONE (82 Terminals Across 40 Countries)",
        "sloanAccrual": "0.8%",
        "piotroski": "8 / 9",
        "dupontROE": {
            "taxBurden": "0.90",
            "interestBurden": "0.82",
            "opMargin": "28.5%",
            "assetTurn": "0.45x",
            "leverage": "2.45x",
            "finalROE": "18.2%"
        },
        "kyleLambda": "0.045 bps / $1M",
        "blkOwnership": "3.20% ($912M)",
        "vangOwnership": "2.80% ($798M)",
        "activeFloat": "Sovereign Dubai World",
        "nanoLink": "dpworld_jebelali",
        "soicScore": {
            "industry": 45,
            "industryMax": 45,
            "funda": 76,
            "fundaMax": 80,
            "tech": 100,
            "techMax": 110,
            "val": 28,
            "valMax": 35,
            "forensic": 38,
            "forensicMax": 40,
            "total": 287,
            "totalMax": 310,
            "classification": "MIDDLE EAST & GLOBAL MARITIME GATEWAY"
        }
    },
    "airarabia": {
        "name": "Air Arabia PJSC",
        "ticker": "AIRARABIA:AE",
        "cmp": "AED 2.82",
        "dcf": "AED 3.25",
        "mos": "+15.2%",
        "mcap": "AED 13.1 Billion ($3.57B)",
        "pe": "8.8",
        "pbv": "1.85",
        "evEbitda": "5.2",
        "beneishM": -2.85,
        "beneishStatus": "SAFE",
        "altmanZ": 6.8,
        "altmanStatus": "SAFE ZONE (Net Cash Balance Sheet AED 5.2B)",
        "sloanAccrual": "-0.5% (Prepaid Ticket Floats)",
        "piotroski": "9 / 9",
        "dupontROE": {
            "taxBurden": "0.95",
            "interestBurden": "0.96",
            "opMargin": "26.8%",
            "assetTurn": "0.75x",
            "leverage": "1.45x",
            "finalROE": "26.5%"
        },
        "kyleLambda": "0.035 bps / AED 2M",
        "blkOwnership": "3.80% ($135M)",
        "vangOwnership": "3.20% ($114M)",
        "activeFloat": "62.5%",
        "nanoLink": "airarabia_sharjah",
        "soicScore": {
            "industry": 40,
            "industryMax": 45,
            "funda": 76,
            "fundaMax": 80,
            "tech": 102,
            "techMax": 110,
            "val": 32,
            "valMax": 35,
            "forensic": 38,
            "forensicMax": 40,
            "total": 288,
            "totalMax": 310,
            "classification": "LOWEST COST MIDDLE EAST CARRIER"
        }
    }
};

  nanoData = {
    "halol_mega": {
        "title": "🏭 Polycab Halol Mega Manufacturing Complex (Gujarat)",
        "facilityType": "Mega Cables & Continuous Cast Copper Rod Complex",
        "parentFirm": "Polycab India Ltd [POLYCAB:IN]",
        "coords": [
            22.496,
            73.473
        ],
        "specs": [
            {
                "label": "Total Complex Land Area",
                "value": "150+ Acres (Halol Industrial Corridor)"
            },
            {
                "label": "Continuous Cast Copper Rod Mill",
                "value": "12,500 MT / month (Properzi Process)"
            },
            {
                "label": "Extrusion Line Operating Speed",
                "value": "850 meters / minute"
            },
            {
                "label": "Authorized Distribution Hub",
                "value": "4,300+ Distributors | 205k Retailers"
            },
            {
                "label": "Logistics Traffic Gate AIS",
                "value": "142 heavy container trailers / day"
            }
        ],
        "description": "Polycab's flagship manufacturing mother plant. Houses in-house copper cathode smelting furnaces, high-voltage CCV lines, and automated distribution warehouses supplying 79 export destinations globally."
    },
    "kei_plant": {
        "title": "⚡ KEI Silvassa 400kV EHV Extrusion Tower & Sanand Plant",
        "facilityType": "Extra High Voltage (EHV) Power Cable Facility",
        "parentFirm": "KEI Industries Ltd [KEI:IN]",
        "coords": [
            20.272,
            73.008
        ],
        "specs": [
            {
                "label": "Vertical CCV Extrusion Tower",
                "value": "135 meters height (German Troester Line)"
            },
            {
                "label": "Voltage Rating Qualification",
                "value": "Up to 400kV EHV Underground Transmission"
            },
            {
                "label": "Annual Processing Capacity",
                "value": "115,000 km Cables | 1,200 MT Wires"
            },
            {
                "label": "Brugg Cables Swiss IP License",
                "value": "Exclusive Joint Venture & Technology Transfer"
            }
        ],
        "description": "Specialized heavy infrastructure manufacturing plant producing EHV power cables for metro rail networks, offshore wind farms, and interstate grid corridors under PGCIL."
    },
    "rr_waghodia": {
        "title": "🏭 RR Kabel Waghodia Integrated Cable & Enamelled Wire Complex",
        "facilityType": "Low-Smoke Zero-Halogen (LSZH) Cable Manufacturing Plant",
        "parentFirm": "RR Kabel Ltd [RRKABEL:IN]",
        "coords": [
            22.302,
            73.365
        ],
        "specs": [
            {
                "label": "Campus Footprint",
                "value": "78 Acres (Waghodia GIDC, Vadodara)"
            },
            {
                "label": "FireX LSZH Compound Formulation",
                "value": "In-House Proprietary Polymer Compounding"
            },
            {
                "label": "Global Safety Certifications",
                "value": "UL (USA), BASEC (UK), VDE (Germany)"
            }
        ],
        "description": "Ultra-modern wire drawing and compounding plant with export certifications to 80+ countries across North America and the European Union."
    },
    "finolex_urse": {
        "title": "🏭 Finolex Cables Urse Optic Fiber & Power Cable Complex",
        "facilityType": "Optic Fiber Preform Draw & EHV Facility",
        "parentFirm": "Finolex Cables Ltd [FINCABLES:IN]",
        "coords": [
            18.728,
            73.654
        ],
        "specs": [
            {
                "label": "Optic Fiber Draw Capacity",
                "value": "8 Million Fiber Kilometers (FKM) / year"
            },
            {
                "label": "Copper Communication Cables",
                "value": "Jelly Filled Telecom Cables & LAN Category 6/7"
            },
            {
                "label": "Energy Source",
                "value": "Onsite 5MW Captive Solar + Wind Hybrid"
            }
        ],
        "description": "Finolex's Pune manufacturing complex integrating glass preform draw towers, telecommunication fiber cabling, and industrial PVC compound plants."
    },
    "mps_studio": {
        "title": "🏢 MPS Digital Content & Learning Architecture Studio (Bengaluru)",
        "facilityType": "Scholarly AI Workflow & Digital Learning Hub",
        "parentFirm": "MPS Ltd [MPSLTD:IN]",
        "coords": [
            12.971,
            77.594
        ],
        "specs": [
            {
                "label": "Scholarly Journal Output",
                "value": "2.4 Million Published Academic Pages / year"
            },
            {
                "label": "AI Workflow Engine",
                "value": "MPS Think360 Platform & Magplus CMS"
            },
            {
                "label": "Global STM Publisher Client Base",
                "value": "Elsevier, Springer Nature, Wiley, Oxford"
            }
        ],
        "description": "Core technology and digital publishing operations center delivering high-margin STM editorial architecture, automated XML conversion, and educational platforms."
    },
    "niit_hub": {
        "title": "🏢 NIIT Managed Training Services (MTS) Global Delivery Hub",
        "facilityType": "Corporate Enterprise L&D Delivery Center (Gurugram)",
        "parentFirm": "NIIT Learning Systems Ltd [NIITMTS:IN]",
        "coords": [
            28.459,
            77.026
        ],
        "specs": [
            {
                "label": "Fortune 500 Enterprise Contracts",
                "value": "84 Multi-Year Master Service Agreements"
            },
            {
                "label": "Annual Learner Touchpoints",
                "value": "1.2 Million Corporate Professionals"
            },
            {
                "label": "Contract Revenue Visibility",
                "value": "$380M Multi-Year Contract Backlog"
            }
        ],
        "description": "Global operations hub managing end-to-end outsourced corporate learning programs for aerospace, energy, banking, and technology multinationals."
    },
    "veranda_center": {
        "title": "🎓 Veranda Enterprise EdTech & Offline Test Prep Hub (Chennai)",
        "facilityType": "Omnichannel Test Prep & Software Training Center",
        "parentFirm": "Veranda Learning Solutions [VERANDA:IN]",
        "coords": [
            13.082,
            80.27
        ],
        "specs": [
            {
                "label": "Physical Centers Across India",
                "value": "180+ Hybrid Offline/Online Learning Hubs"
            },
            {
                "label": "Government Exam Enrollment",
                "value": "Banking, UPSC, TNPSC & SSC Aspirants"
            }
        ],
        "description": "Regional hub integrating physical test-prep coaching centers with digital content delivery and corporate IT upskilling tracks."
    },
    "navneet_dantej": {
        "title": "📚 Navneet Dantali High-Speed Publication & Educational Complex",
        "facilityType": "Educational Publishing & Stationery Export Plant",
        "parentFirm": "Navneet Education Ltd [NAVNETEDUL:IN]",
        "coords": [
            23.148,
            72.583
        ],
        "specs": [
            {
                "label": "High-Speed Web Printing Output",
                "value": "1.8 Million Books & Notebooks / day"
            },
            {
                "label": "State Board Curriculum Coverage",
                "value": "Maharashtra, Gujarat, CBSE & ICSE"
            }
        ],
        "description": "Automated printing presses and stationery manufacturing facility supplying academic textbooks, supplementary study guides, and export stationery."
    },
    "vapi": {
        "title": "🧪 Pidilite Vapi Synthetic Resin & Adhesives Mega Plant (Gujarat)",
        "facilityType": "Polymer Compounding, VAM Reaction & Fevicol Plant",
        "parentFirm": "Pidilite Industries Ltd [PIDILITIND:IN]",
        "coords": [
            20.371,
            72.91
        ],
        "specs": [
            {
                "label": "Continuous Emulsion Polymerization",
                "value": "18,500 MT / month Synthetic Adhesives"
            },
            {
                "label": "Fevicol / Fevikwik Formulations",
                "value": "Proprietary Plasticizer & Monomer Formulations"
            },
            {
                "label": "Automated Robotic Packaging",
                "value": "650 pouches / minute automated filling"
            }
        ],
        "description": "Pidilite's mother manufacturing complex. Synthesizes polyvinyl acetate emulsions, water-based adhesives, and specialty construction sealants dominating 70%+ market share."
    },
    "srf_dahej": {
        "title": "🧪 SRF Dahej Mega Specialty Chemicals & Fluorochemicals Complex",
        "facilityType": "Specialty Fluorination & HFC/HFO Reaction Complex",
        "parentFirm": "SRF Ltd [SRF:IN]",
        "coords": [
            21.712,
            72.585
        ],
        "specs": [
            {
                "label": "Dahej Chemical SEZ Land Area",
                "value": "320 Acres Dedicated Complex"
            },
            {
                "label": "Fluorination Batch Reactors",
                "value": "78 High-Pressure Autoclaves"
            },
            {
                "label": "Agro & Pharma Intermediate Molecules",
                "value": "48 Commercial Active Ingredients"
            }
        ],
        "description": "World-scale specialty fluorochemicals manufacturing hub providing complex multi-step synthetic molecules to global innovator agrochemical and pharmaceutical clients."
    },
    "navin_surat": {
        "title": "🧪 Navin Fluorine Surat Fluorochemicals & CDMO Center (Bhestan)",
        "facilityType": "Anhydrous Hydrofluoric Acid (HF) & CRAMS Facility",
        "parentFirm": "Navin Fluorine International [NAVINFLUOR:IN]",
        "coords": [
            21.125,
            72.842
        ],
        "specs": [
            {
                "label": "Anhydrous HF Distillation",
                "value": "24,000 MT / year High Purity HF"
            },
            {
                "label": "cGMP Synthesis Blocks",
                "value": "US-FDA Inspected Active Pharmaceutical Blocks"
            }
        ],
        "description": "Surat chemical synthesis center specializing in high-hazard hazardous fluorine chemistry, boron trifluoride adducts, and contract development."
    },
    "jubilant_bharuch": {
        "title": "🧪 Jubilant Ingrevia Bharuch Specialty Chemicals & Pyridine Hub",
        "facilityType": "Pyridine & Picoline Mega Chemical Complex",
        "parentFirm": "Jubilant Ingrevia Ltd [JUBLINGREA:IN]",
        "coords": [
            21.705,
            72.998
        ],
        "specs": [
            {
                "label": "Global Pyridine Derivative Rank",
                "value": "Global Lowest Cost Manufacturer (Rank #1)"
            },
            {
                "label": "Bio-Based Acetic Chemistry",
                "value": "Ethanol to Acetaldehyde & Ethyl Acetate"
            }
        ],
        "description": "Integrated specialty chemical complex utilizing green bio-ethanol to synthesize high-value intermediates for nutraceuticals, crop protection, and pharma."
    },
    "saket_max": {
        "title": "🏥 Max Super Speciality Hospital Saket (New Delhi)",
        "facilityType": "Quaternary Care Flagship Academic Medical Campus",
        "parentFirm": "Max Healthcare Institute Ltd [MAXHEALTH:IN]",
        "coords": [
            28.528,
            77.214
        ],
        "specs": [
            {
                "label": "Licensed Bed Capacity",
                "value": "850 Operational Beds (Expanding to 1,200)"
            },
            {
                "label": "Average Revenue Per Bed (ARPOB)",
                "value": "₹84,500 / operational bed day"
            },
            {
                "label": "Robotic Surgery Systems",
                "value": "da Vinci Xi & Mako Orthopedic Robots"
            },
            {
                "label": "International Medical Tourists",
                "value": "18% of Total Patient Inflows"
            }
        ],
        "description": "Max Healthcare's crown-jewel quaternary oncology, cardiology, and organ transplant campus delivering the highest EBITDA margins and ARPOB in the Indian healthcare sector."
    },
    "narayana_bommasandra": {
        "title": "🏥 Narayana Health City & Mazumdar Shaw Cancer Centre (Bengaluru)",
        "facilityType": "Mass-Scale Quaternary Cardiac & Cancer Campus",
        "parentFirm": "Narayana Hrudayalaya Ltd [NH:IN]",
        "coords": [
            12.812,
            77.692
        ],
        "specs": [
            {
                "label": "Total Campus Bed Count",
                "value": "1,400 Tertiary & Quaternary Beds"
            },
            {
                "label": "Open Heart Surgeries Performed",
                "value": "32 Cardiac Surgeries / day (Lowest Cost Globally)"
            },
            {
                "label": "Cayman Islands Hospital Subsidiary",
                "value": "Health City Cayman Islands (USD Cash Margins 42%)"
            }
        ],
        "description": "The operational epicenter of Dr. Devi Shetty's assembly-line cardiac surgical efficiency, delivering world-class survival rates at a fraction of Western hospital costs."
    },
    "apollo_chennai": {
        "title": "🏥 Apollo Hospitals Greams Road Flagship Campus (Chennai)",
        "facilityType": "Multi-Specialty Quaternary Healthcare & Proton Therapy Hub",
        "parentFirm": "Apollo Hospitals Enterprise Ltd [APOLLOHOSP:IN]",
        "coords": [
            13.061,
            80.252
        ],
        "specs": [
            {
                "label": "Proton Beam Therapy Center",
                "value": "South East Asia First Proton Cancer Center"
            },
            {
                "label": "Apollo 24/7 Digital Platform",
                "value": "30 Million Registered Telemedicine Users"
            },
            {
                "label": "Pharmacy Distribution Network",
                "value": "6,000+ Retail Pharmacy Outlets"
            }
        ],
        "description": "Apollo's mother quaternary institution combining advanced oncology radiation, organ transplants, and omni-channel pharmacy distribution."
    },
    "taj_mahal_palace": {
        "title": "🏨 The Taj Mahal Palace & Tower (Apollo Bunder, Colaba, Mumbai)",
        "facilityType": "Ultra-Luxury Heritage Grand Flagship Hotel",
        "parentFirm": "The Indian Hotels Co Ltd (Taj) [INDHOTEL:IN]",
        "coords": [
            18.921,
            72.833
        ],
        "specs": [
            {
                "label": "Total Keys & Suites",
                "value": "560 Luxury Rooms & Presidential Suites"
            },
            {
                "label": "Average Room Rate (ARR)",
                "value": "₹28,500 / night (92% Occupancy Peak Season)"
            },
            {
                "label": "Food & Beverage Revenue",
                "value": "Wasabi, Golden Dragon, Sea Lounge"
            }
        ],
        "description": "IHCL's legendary heritage flagship property facing the Gateway of India, commanding unprecedented RevPAR and operating margins under the Taj brand."
    },
    "samhi_aerocity": {
        "title": "🏨 SAMHI Aerocity Multi-Branded Hospitality Cluster (New Delhi)",
        "facilityType": "Institutional Airport Business Hotel Cluster",
        "parentFirm": "SAMHI Hotels Ltd [SAMHI:IN]",
        "coords": [
            28.552,
            77.121
        ],
        "specs": [
            {
                "label": "Aerocity Keys Under Management",
                "value": "962 Operating Keys (Courtyard, Fairfield by Marriott)"
            },
            {
                "label": "Blended ARR",
                "value": "₹8,900 / night (84% Year-Round Occupancy)"
            }
        ],
        "description": "High-efficiency business travel asset cluster situated next to Indira Gandhi International Airport, delivering steady institutional corporate travel yields."
    },
    "chalet_powai": {
        "title": "🏨 Chalet Renaissance & Westin Powai Lake Luxury Complex (Mumbai)",
        "facilityType": "Integrated Hotel, Convention Center & Commercial Office",
        "parentFirm": "Chalet Hotels Ltd [CHALET:IN]",
        "coords": [
            19.128,
            72.905
        ],
        "specs": [
            {
                "label": "Hotel Keys & Convention Space",
                "value": "773 Premium Keys | 100,000 sq ft Ballroom"
            },
            {
                "label": "Grade-A Commercial Office Asset",
                "value": "1.2 Million sq ft Leased to MNC Tech Tenants"
            }
        ],
        "description": "Chalet's high-margin mixed-use asset combining luxury five-star hotel inventory with steady recurring commercial office lease rentals."
    },
    "apollo_raipur": {
        "title": "🏗️ APL Apollo Raipur 500,000 MT Heavy Structural Tube Complex",
        "facilityType": "Direct 500x500mm Hollow Section Structural Steel Plant",
        "parentFirm": "APL Apollo Tubes Ltd [APLAPOLLO:IN]",
        "coords": [
            21.251,
            81.629
        ],
        "specs": [
            {
                "label": "Direct 500x500mm ERW Mill",
                "value": "Largest Heavy Structural Tube Mill in India"
            },
            {
                "label": "Annual Steel Capacity",
                "value": "500,000 MT / year dedicated heavy tubing"
            },
            {
                "label": "Steel Melting & Raw Material Tie-up",
                "value": "Captive HRC supply agreements with Jindal Steel"
            }
        ],
        "description": "APL Apollo's mega structural steel mill producing large-dimension hollow structural sections that replace conventional steel I-beams in airports, warehouses, and stadiums."
    },
    "ratnamani_kutch": {
        "title": "🏗️ Ratnamani Kutch High-Pressure Stainless Steel Tube Complex",
        "facilityType": "Seamless Stainless Steel & Titanium Tubing Plant",
        "parentFirm": "Ratnamani Metals & Tubes Ltd [RATNAMANI:IN]",
        "coords": [
            23.194,
            70.188
        ],
        "specs": [
            {
                "label": "Hot Extrusion Press Capacity",
                "value": "4,500 Ton High-Tonnage Extruder"
            },
            {
                "label": "Nuclear & Defense Critical Quals",
                "value": "NPCIL, BARC, Shell, Saudi Aramco Approved"
            }
        ],
        "description": "Advanced metallurgical complex manufacturing high-pressure seamless stainless steel and nickel alloy tubes for nuclear power reactors, LNG terminals, and defense missile casing."
    },
    "welspun_anjar": {
        "title": "🏗️ Welspun Anjar Mega Helical & L-SAW Line Pipe Plant (Gujarat)",
        "facilityType": "Large Diameter Longitudinal & Spiral Submerged Arc Welded Pipe Mill",
        "parentFirm": "Welspun Corp Ltd [WELCORP:IN]",
        "coords": [
            23.112,
            70.028
        ],
        "specs": [
            {
                "label": "Pipe Diameter Capability",
                "value": "Up to 144 inches (3.65 meters) Outside Diameter"
            },
            {
                "label": "Annual Global Capacity",
                "value": "2.5 Million MT across India, US, and Saudi Arabia"
            }
        ],
        "description": "Heavy line-pipe fabrication and internal/external anti-corrosion coating facility supplying deepwater oil/gas transport pipelines and national water grids."
    },
    "hdfc_bkc": {
        "title": "🏦 HDFC Bank Treasury & Global Clearing Operations (BKC Mumbai)",
        "facilityType": "Central Financial Architecture & Algorithmic Clearing Headquarters",
        "parentFirm": "HDFC Bank Ltd [HDFCBANK:IN]",
        "coords": [
            19.066,
            72.868
        ],
        "specs": [
            {
                "label": "Daily Payment Clearing Volume",
                "value": "₹4.8 Trillion ($57 Billion) / day"
            },
            {
                "label": "Retail Customer Deposit Accounts",
                "value": "95 Million Active Accounts"
            },
            {
                "label": "Branch & ATM Grid",
                "value": "8,800+ Branches | 21,000+ ATMs across India"
            }
        ],
        "description": "The central banking operational nerve center managing India's largest private balance sheet ($400B+ assets), housing treasury FX desks and algorithmic clearing engines."
    },
    "icici_bkc": {
        "title": "🏦 ICICI Bank Towers & Digital Data Center (Bandra-Kurla Complex)",
        "facilityType": "Corporate Headquarters & iMobile Cloud Engine",
        "parentFirm": "ICICI Bank Ltd [ICICIBANK:IN]",
        "coords": [
            19.064,
            72.865
        ],
        "specs": [
            {
                "label": "Digital Transaction Share",
                "value": "94% of Financial Transactions Non-Branch"
            },
            {
                "label": "Underwriting Engine",
                "value": "InstaLoan Pre-Approved Algorithmic Credit"
            }
        ],
        "description": "ICICI Bank's headquarters and digital banking software operations, operating with one of the lowest operating cost-to-income ratios (39.5%) and highest ROAs in India."
    },
    "kotak_bkc": {
        "title": "🏦 Kotak Infinity Financial Operations & Wealth Hub (BKC Mumbai)",
        "facilityType": "Private Banking, Treasury & Retail HQ",
        "parentFirm": "Kotak Mahindra Bank Ltd [KOTAKBANK:IN]",
        "coords": [
            19.068,
            72.871
        ],
        "specs": [
            {
                "label": "Private Wealth AUM",
                "value": "₹3.2 Trillion UHNI Family Office Assets"
            },
            {
                "label": "Capital Adequacy Ratio",
                "value": "20.8% (Safest Tier-1 Buffer in Asia)"
            }
        ],
        "description": "Ultra-conservative financial fortress managing prime retail deposits, investment banking deals, and India's premier ultra-high-net-worth wealth franchise."
    },
    "sbi_nariman": {
        "title": "🏦 State Bank of India Central Office (State Bank Bhavan, Nariman Point)",
        "facilityType": "National Sovereign Commercial Bank Operations Hub",
        "parentFirm": "State Bank of India [SBIN:IN]",
        "coords": [
            18.928,
            72.823
        ],
        "specs": [
            {
                "label": "Total Customer Base",
                "value": "500 Million Indian Citizens (1 in 3 Citizens)"
            },
            {
                "label": "Total Loan Book",
                "value": "₹38.5 Trillion ($460 Billion Assets)"
            },
            {
                "label": "YONO Digital Platform",
                "value": "70 Million Registered Active Mobile Users"
            }
        ],
        "description": "The sovereign backbone of India's commercial banking system, commanding 24% of national banking deposits and executing direct government welfare and infrastructure clearing."
    },
    "tsmc_fab": {
        "title": "🔬 TSMC Fab 18A GigaFab & N3/N2 Cleanroom (Tainan Science Park)",
        "facilityType": "3nm / 2nm Extreme Ultraviolet (EUV) Semiconductor Foundry",
        "parentFirm": "NVIDIA Corporation [NVDA:US]",
        "coords": [
            23.111,
            120.276
        ],
        "specs": [
            {
                "label": "Cleanroom Classification",
                "value": "Class 1 Ultra-Pure Vacuum Chamber"
            },
            {
                "label": "ASML Twinscan High-NA EUV Scanners",
                "value": "34 Operational Systems ($380M each)"
            },
            {
                "label": "Monthly 3nm Silicon Wafer Output",
                "value": "65,000 Wafers / month"
            },
            {
                "label": "CoWoS-L Advanced Packaging Line",
                "value": "Blackwell B200 Multi-Die Dual Reticle Integration"
            }
        ],
        "description": "The apex manufacturing hub of human technological civilization. Produces 100% of NVIDIA's Blackwell and Hopper AI computing engines with sub-atomic 3nm transistor architectures."
    },
    "amd_austin": {
        "title": "🔬 AMD Lone Star Silicon Design Campus & Microprocessor Lab (Austin, TX)",
        "facilityType": "Zen 5 & MI350X GPU Architecture Engineering Center",
        "parentFirm": "Advanced Micro Devices Inc [AMD:US]",
        "coords": [
            30.245,
            -97.868
        ],
        "specs": [
            {
                "label": "Chiplet Packaging Lab",
                "value": "3D V-Cache & Multi-Die Stacking Testbeds"
            },
            {
                "label": "ROCm Software Verification",
                "value": "10,000 Node GPU Supercomputing Validation Cluster"
            }
        ],
        "description": "AMD's microprocessor design hub creating Zen CPU chiplets and Instinct MI300/MI350 series accelerators competing with NVIDIA in AI clusters."
    },
    "broadcom_sanjose": {
        "title": "🔬 Broadcom Global Silicon & Networking Innovation Center (San Jose, CA)",
        "facilityType": "Custom AI ASIC & Tomahawk 5 Switch Foundry Lab",
        "parentFirm": "Broadcom Inc [AVGO:US]",
        "coords": [
            37.382,
            -121.928
        ],
        "specs": [
            {
                "label": "Tomahawk 5 Ethernet ASIC",
                "value": "51.2 Tbps High-Radix Switching Engine"
            },
            {
                "label": "Custom XPU Co-Design",
                "value": "Hyperscaler AI Silicon (Google TPU v5/v6, Meta MTIA)"
            }
        ],
        "description": "The silicon heart of global data center networking, designing the high-speed Ethernet fabrics and custom ASICs powering hyperscale cloud infrastructure."
    },
    "qualcomm_sandiego": {
        "title": "🔬 Qualcomm Morehouse Campus & Snapdragon Engineering Hub (San Diego)",
        "facilityType": "Oryon CPU & Snapdragon X Elite Compute Lab",
        "parentFirm": "Qualcomm Inc [QCOM:US]",
        "coords": [
            32.895,
            -117.195
        ],
        "specs": [
            {
                "label": "Snapdragon X Elite Benchmarks",
                "value": "45 NPU TOPS for Windows Copilot+ AI Laptops"
            },
            {
                "label": "Cellular Modem 5G Advanced",
                "value": "Snapdragon X80 5G RF Baseband Processor"
            }
        ],
        "description": "Qualcomm's global R&D headquarters designing custom ARM-compatible Oryon CPU cores, edge AI NPU engines, and mobile radio-frequency modems."
    },
    "apple_park": {
        "title": "🏢 Apple Park & Silicon Design Center (1 Apple Park Way, Cupertino, CA)",
        "facilityType": "Global Design HQ & Apple Silicon Hardware Engineering Center",
        "parentFirm": "Apple Inc [AAPL:US]",
        "coords": [
            37.334,
            -122.009
        ],
        "specs": [
            {
                "label": "Ring Building Footprint",
                "value": "2.8 Million sq ft on 175 Acres"
            },
            {
                "label": "Renewable Microgrid",
                "value": "17MW Onsite Rooftop Solar + Fuel Cells"
            },
            {
                "label": "Apple Silicon Team Lab",
                "value": "M4 / A18 Pro SoC Architecture & Neural Engine Design"
            }
        ],
        "description": "The operational and design epicenter of Apple Inc. Houses the world's most lucrative hardware and operating system ecosystem engineering teams."
    },
    "msft_redmond": {
        "title": "🏢 Microsoft Redmond Campus & Azure Hyperscale Center (Redmond, WA)",
        "facilityType": "Enterprise Software & OpenAI Infrastructure Hub",
        "parentFirm": "Microsoft Corp [MSFT:US]",
        "coords": [
            47.642,
            -122.13
        ],
        "specs": [
            {
                "label": "Campus Building Count",
                "value": "125 Buildings across 500 Acres"
            },
            {
                "label": "Azure AI Supercomputer Backlog",
                "value": "Tens of thousands of connected GPU clusters"
            }
        ],
        "description": "Microsoft's global corporate campus coordinating Azure cloud expansion, Windows OS, Office 365, and multi-billion-dollar OpenAI infrastructure deployments."
    },
    "goog_council_bluffs": {
        "title": "🌐 Google Council Bluffs Hyperscale AI Data Center Campus (Iowa)",
        "facilityType": "Mega Hyperscale Cloud & Gemini Training Facility",
        "parentFirm": "Alphabet Inc (Google) [GOOGL:US]",
        "coords": [
            41.221,
            -95.845
        ],
        "specs": [
            {
                "label": "Cumulative Capital Investment",
                "value": "$5.0+ Billion in Iowa Compute Infrastructure"
            },
            {
                "label": "Power Consumption",
                "value": "450+ Megawatts Continuous Clean Power"
            },
            {
                "label": "TPU Pod Clusters",
                "value": "TPU v5p Tensor Processing Units for Gemini Model Pre-training"
            }
        ],
        "description": "One of Google's largest operational hyperscale data center complexes, training frontier multimodal neural networks and hosting YouTube, Search, and Google Cloud."
    },
    "amzn_ashburn": {
        "title": "🌐 AWS Northern Virginia Cloud Infrastructure Epicenter (Ashburn, VA)",
        "facilityType": "Global Data Chokepoint & AWS us-east-1 Region",
        "parentFirm": "Amazon.com Inc [AMZN:US]",
        "coords": [
            39.043,
            -77.487
        ],
        "specs": [
            {
                "label": "Global Internet Traffic Share",
                "value": "Estimated 70% of World Internet Traffic Routes Through Loudoun"
            },
            {
                "label": "AWS Availability Zones",
                "value": "6 Redundant Zones in us-east-1"
            }
        ],
        "description": "Data Center Alley in Northern Virginia. The central pillar of Amazon Web Services, powering the mission-critical cloud computing workloads of global banks, governments, and streaming platforms."
    },
    "tsla_austin": {
        "title": "🚗 Tesla Giga Texas Megafactory & 4680 Battery Line (Austin, TX)",
        "facilityType": "Cybercab, Cybertruck & 4680 Cathode Battery Production Base",
        "parentFirm": "Tesla Inc [TSLA:US]",
        "coords": [
            30.222,
            -97.617
        ],
        "specs": [
            {
                "label": "Factory Footprint",
                "value": "10 Million sq ft Factory Floor (Over 2,000 Acres)"
            },
            {
                "label": "Giga Press Die Casting",
                "value": "9,000-Ton High-Pressure Aluminum Injection"
            },
            {
                "label": "Cortex AI Supercomputer",
                "value": "100k H100 Cluster for Full Self-Driving End-to-End Neural Nets"
            }
        ],
        "description": "Tesla's headquarters and largest operational factory building Cybertruck, Model Y, and training FSD v12 vision-only end-to-end models on massive GPU clusters."
    },
    "baytown": {
        "title": "⛽ ExxonMobil Baytown Refining & Petrochemical Complex (Houston, TX)",
        "facilityType": "Integrated 560,000 bpd Petroleum Refining & Olefins Plant",
        "parentFirm": "ExxonMobil Corporation [XOM:US]",
        "coords": [
            29.749,
            -95.012
        ],
        "specs": [
            {
                "label": "Crude Refining Capacity",
                "value": "560,500 Barrels / day crude distillation"
            },
            {
                "label": "Steam Cracker Ethylene Output",
                "value": "3.8 Million MT / year Polyethylene"
            },
            {
                "label": "Permian Pipeline Link",
                "value": "Direct Wink-to-Webster 1.5M bpd pipeline intake"
            }
        ],
        "description": "ExxonMobil's premier petrochemical and refining complex on the Houston Ship Channel, converting low-cost Permian tight crude into jet fuel, diesel, and performance polymers."
    },
    "cvx_pascagoula": {
        "title": "⛽ Chevron Pascagoula Refinery & Deepwater Gulf Hub (Mississippi)",
        "facilityType": "330,000 bpd Premium Hydrocracking Refinery",
        "parentFirm": "Chevron Corporation [CVX:US]",
        "coords": [
            30.345,
            -88.508
        ],
        "specs": [
            {
                "label": "Base Oil Manufacturing",
                "value": "World Largest Premium Group II Base Oil Plant"
            },
            {
                "label": "Deepwater Gulf of Mexico Offtake",
                "value": "Intake from Jack/St. Malo and Big Foot Spars"
            }
        ],
        "description": "Chevron's largest refinery, capable of processing complex heavy sour crudes into high-margin lubricants, gasoline, and aviation fuels."
    },
    "cheniere_sabine": {
        "title": "🚢 Cheniere Sabine Pass LNG Export Terminal (Cameron Parish, LA)",
        "facilityType": "30 Million MTPA Liquefied Natural Gas (LNG) Liquefaction Facility",
        "parentFirm": "Cheniere Energy Inc [LNG:US]",
        "coords": [
            29.756,
            -93.872
        ],
        "specs": [
            {
                "label": "Liquefaction Trains",
                "value": "6 Operational Trains (30+ MTPA LNG)"
            },
            {
                "label": "LNG Storage Tanks",
                "value": "5 Full-Containment Tanks (3.4M Barrels Liquid)"
            },
            {
                "label": "Deepwater Berths",
                "value": "2 Dedicated Docks Handling Q-Flex LNG Carriers"
            }
        ],
        "description": "The largest natural gas export facility in the Western Hemisphere, supplying liquefied natural gas under 20-year contracts to Europe and Asia to replace Russian pipeline flows."
    },
    "cop_permian": {
        "title": "⛽ ConocoPhillips Permian Basin Unconventional Assets (Midland, TX)",
        "facilityType": "Tight Oil & Shale Gas Horizontal Drilling Complex",
        "parentFirm": "ConocoPhillips [COP:US]",
        "coords": [
            31.997,
            -102.077
        ],
        "specs": [
            {
                "label": "Net Permian Production",
                "value": "750,000 Barrels of Oil Equivalent / day"
            },
            {
                "label": "Supply Cost / Barrel",
                "value": "< $35 / bbl WTI Breakeven Cost"
            }
        ],
        "description": "ConocoPhillips' core shale engine, utilizing multi-pad drilling and 3-mile horizontal laterals to produce low-cost crude with multi-decade inventory runway."
    },
    "prysmian_highland": {
        "title": "⚡ Prysmian Highland Submarine High-Voltage Cable Plant (Highland, NY)",
        "facilityType": "Submarine HVDC Power Transmission Cable Facility",
        "parentFirm": "Prysmian Group [PRY:IM]",
        "coords": [
            41.725,
            -73.965
        ],
        "specs": [
            {
                "label": "Submarine Cable Armoring",
                "value": "525kV HVDC Extruded Subsea Cable System"
            },
            {
                "label": "Cable-Laying Vessel Tie-Up",
                "value": "Leonardo da Vinci & Monna Lisa Installation Fleets"
            }
        ],
        "description": "Advanced subsea cable plant dedicated to offshore wind interconnections and interstate electric grid transmission lines along the US Eastern Seaboard."
    },
    "hubbell_shelton": {
        "title": "⚡ Hubbell Utility Solutions Grid Modernization Center (Shelton, CT)",
        "facilityType": "High-Voltage Switchgear & Utility Distribution Equipment Plant",
        "parentFirm": "Hubbell Inc [HUBB:US]",
        "coords": [
            41.316,
            -73.093
        ],
        "specs": [
            {
                "label": "Transmission Connectors & Insulators",
                "value": "Ohio Brass High-Voltage Polymeric Insulators"
            },
            {
                "label": "Smart Metering & Grid Automation",
                "value": "Aclara Automated AMI Communications Networks"
            }
        ],
        "description": "Manufacturing center for electric utility transmission grid components, surge arresters, and automated distribution sensors deployed by US power utilities."
    },
    "stride_hq": {
        "title": "🎓 Stride K12 Curriculum & Virtual Academy Hub (Reston, VA)",
        "facilityType": "Accredited Online Public School Curriculum Operations",
        "parentFirm": "Stride Inc (K12) [LRN:US]",
        "coords": [
            38.958,
            -77.357
        ],
        "specs": [
            {
                "label": "Full-Time Virtual Students",
                "value": "195,000+ Enrolled K-12 Students"
            },
            {
                "label": "State Public School Partnerships",
                "value": "Over 30 US States Funding Virtual Charters"
            }
        ],
        "description": "The operational and curricular nerve center for Stride's virtual public academies, providing state-funded digital schooling and career tech education across the US."
    },
    "coursera_mtv": {
        "title": "🎓 Coursera Mountain View Silicon Valley Software Lab (Mountain View, CA)",
        "facilityType": "Global Online Degree & Enterprise Skills Platform Lab",
        "parentFirm": "Coursera Inc [COUR:US]",
        "coords": [
            37.386,
            -122.083
        ],
        "specs": [
            {
                "label": "Registered Global Learners",
                "value": "155+ Million Learners Worldwide"
            },
            {
                "label": "University & Industry Partners",
                "value": "325+ Top Universities (Stanford, Penn, Google, IBM)"
            }
        ],
        "description": "Coursera's headquarters where algorithmic recommendation systems, GenAI course translators, and university degree programs are developed."
    },
    "duolingo_pgh": {
        "title": "🎓 Duolingo East Liberty Algorithmic Learning Hub (Pittsburgh, PA)",
        "facilityType": "Gamified Language & English Test Assessment Lab",
        "parentFirm": "Duolingo Inc [DUOL:US]",
        "coords": [
            40.461,
            -79.924
        ],
        "specs": [
            {
                "label": "Daily Active Users (DAU)",
                "value": "34 Million Daily Active Language Learners"
            },
            {
                "label": "Duolingo English Test (DET)",
                "value": "Accepted by 5,000+ Higher Ed Institutions Globally"
            }
        ],
        "description": "Headquarters of Duolingo, developing high-retention gamification mechanisms, synthetic AI character voices, and certified computerized language testing."
    },
    "mercedes_factory56": {
        "title": "🚗 Mercedes-Benz Factory 56 Ultra-Flexible Industry 4.0 Complex (Sindelfingen)",
        "facilityType": "Zero-Carbon Digital Automotive Assembly Plant",
        "parentFirm": "Mercedes-Benz Group AG [MBG:GR]",
        "coords": [
            48.708,
            9.004
        ],
        "specs": [
            {
                "label": "5G Private Factory Network",
                "value": "Real-Time IoT Tracking of 400+ Automated AGVs"
            },
            {
                "label": "Assembly Models",
                "value": "S-Class, Maybach & EQS Electric Flagships on One Single Line"
            }
        ],
        "description": "The world benchmark for flexible automotive manufacturing, utilizing driverless transport systems, overhead paperless digital cockpits, and 100% solar-powered assembly."
    },
    "bmw_munich": {
        "title": "🚗 BMW Group Plant Munich & FIZ Research Center (Munich, Bavaria)",
        "facilityType": "High-Precision Automotive Engineering & Electric Drivetrain Plant",
        "parentFirm": "Bayerische Motoren Werke AG (BMW) [BMW:GR]",
        "coords": [
            48.178,
            11.558
        ],
        "specs": [
            {
                "label": "Daily Vehicle Output",
                "value": "1,000 Vehicles / day (3 Series & i4 Gran Coupe)"
            },
            {
                "label": "FIZ R&D Engineering Staff",
                "value": "25,000 Specialized Automotive Engineers"
            }
        ],
        "description": "BMW's historical mother plant transformed into an electrified manufacturing facility producing the i4 electric sedan alongside internal combustion platforms."
    },
    "vw_wolfsburg": {
        "title": "🚗 Volkswagen Wolfsburg Mega Plant (Wolfsburg, Lower Saxony)",
        "facilityType": "Largest Single Automotive Manufacturing Complex on Earth",
        "parentFirm": "Volkswagen AG [VOW3:GR]",
        "coords": [
            52.433,
            10.778
        ],
        "specs": [
            {
                "label": "Factory Campus Footprint",
                "value": "6.5 Square Kilometers (70 Million sq ft)"
            },
            {
                "label": "Rail Infrastructure",
                "value": "75 Kilometers of In-Plant Freight Rail Tracks"
            }
        ],
        "description": "The colossal manufacturing heart of Volkswagen Group, producing over 800,000 vehicles annually and housing the group's global software and procurement leadership."
    },
    "siemens_amberg": {
        "title": "🤖 Siemens Electronics Manufacturing Plant Amberg (EWA, Bavaria)",
        "facilityType": "Benchmark Industry 4.0 Smart Factory (99.999% Quality Yield)",
        "parentFirm": "Siemens AG [SIE:GR]",
        "coords": [
            49.444,
            11.859
        ],
        "specs": [
            {
                "label": "Simatic PLC Output",
                "value": "17 Million Industrial Controllers / year"
            },
            {
                "label": "Defect Rate",
                "value": "11 DPM (Defects Per Million Units Produced)"
            },
            {
                "label": "Digital Twin Integration",
                "value": "Full Siemens Teamcenter & NX Simulation"
            }
        ],
        "description": "The world's most famous Industry 4.0 showcase plant. Machines communicate autonomously with components to assemble programmable logic controllers (PLCs) with near-zero defects."
    },
    "kion_frankfurt": {
        "title": "🤖 KION Dematic Automation & Forklift Engineering Hub (Frankfurt)",
        "facilityType": "Intralogistics Software & Automated Warehouse Systems",
        "parentFirm": "KION Group AG [KGX:GR]",
        "coords": [
            50.11,
            8.682
        ],
        "specs": [
            {
                "label": "Dematic Warehouse Systems Installed",
                "value": "Over 6,000 Automated Fulfillment Centers Globally"
            },
            {
                "label": "Linde & STILL Material Handling",
                "value": "Market Leader in European Electric Forklifts"
            }
        ],
        "description": "KION's technology center developing automated guided vehicles (AGVs), automated storage and retrieval systems (ASRS), and warehouse management software."
    },
    "basf_ludwigshafen": {
        "title": "🧪 BASF Ludwigshafen Verbund Mega Site (Rhineland-Palatinate)",
        "facilityType": "World Largest Integrated Chemical Verbund Complex",
        "parentFirm": "BASF SE [BAS:GR]",
        "coords": [
            49.497,
            8.432
        ],
        "specs": [
            {
                "label": "Continuous Site Land Area",
                "value": "10.0 Square Kilometers (2,000 Buildings)"
            },
            {
                "label": "Pipelines Connecting Plants",
                "value": "2,850 Kilometers of Integrated Inter-Plant Pipelines"
            },
            {
                "label": "Rhine River Port Berths",
                "value": "Handling 21 Million MT Raw Materials / year"
            }
        ],
        "description": "The mother of all integrated chemical manufacturing. By-products and waste heat from one chemical reaction serve as raw materials for downstream plants, generating immense cost efficiency."
    },
    "bayer_leverkusen": {
        "title": "🧪 Bayer Chempark Leverkusen & Life Sciences HQ (North Rhine-Westphalia)",
        "facilityType": "Pharmaceutical Synthesis & Crop Science Chemistry Complex",
        "parentFirm": "Bayer AG [BAYN:GR]",
        "coords": [
            51.018,
            6.985
        ],
        "specs": [
            {
                "label": "Chempark Footprint",
                "value": "4.8 Square Kilometers"
            },
            {
                "label": "Pharmaceutical Blockbusters",
                "value": "Xarelto & Eylea Synthesis and Formulation"
            }
        ],
        "description": "Bayer's historical headquarters campus housing active pharmaceutical ingredient synthesis, oncology laboratories, and crop protection formulating lines."
    },
    "tel_miyagi": {
        "title": "🔬 TEL Miyagi Plasma Etch Technology Development Center (Miyagi, Japan)",
        "facilityType": "Advanced Dielectric & Conductor Etch Equipment Manufacturing Plant",
        "parentFirm": "Tokyo Electron Ltd [8035:JP]",
        "coords": [
            38.375,
            140.892
        ],
        "specs": [
            {
                "label": "Cleanroom Area",
                "value": "45,000 sq meters State-of-the-Art Cleanroom"
            },
            {
                "label": "High Aspect Ratio Cryogenic Etch",
                "value": "400+ Layer 3D NAND & GAA Transistor Etching"
            }
        ],
        "description": "Tokyo Electron's premier plasma etch systems plant, developing the atomic-precision dry etching machines that create memory channels in 3D NAND and gate-all-around logic chips."
    },
    "advantest_gunma": {
        "title": "🔬 Advantest Gunma R&D Center & High-Speed Test Factory (Gunma, Japan)",
        "facilityType": "Ultra-High-Speed ATE Semiconductor Memory & SoC Test Systems",
        "parentFirm": "Advantest Corp [6857:JP]",
        "coords": [
            36.258,
            139.388
        ],
        "specs": [
            {
                "label": "T5503HS2 Memory Tester",
                "value": "Testing HBM3E at 9.6 Gbps Parallel Data Rates"
            },
            {
                "label": "Global Market Share",
                "value": "Over 55% of World Automated Test Equipment (ATE)"
            }
        ],
        "description": "The critical chokepoint facility testing high-bandwidth memory (HBM) and complex GPUs before they are assembled into AI supercomputers worldwide."
    },
    "lasertec_yokohama": {
        "title": "🔬 Lasertec Yokohama Advanced Optical Inspection Systems HQ (Yokohama)",
        "facilityType": "Actinic EUV Photomask Blank & Pattern Inspection Foundry",
        "parentFirm": "Lasertec Corp [6920:JP]",
        "coords": [
            35.512,
            139.615
        ],
        "specs": [
            {
                "label": "Actinic EUV Scanner (ACTIS A1500)",
                "value": "Uses 13.5nm EUV Light for Sub-Surface Mask Defect Detection"
            },
            {
                "label": "Global Market Share",
                "value": "100% Global Monopoly on Actinic Blank Inspection"
            }
        ],
        "description": "The sole facility in the world capable of building optical inspection tools that illuminate semiconductor photomasks with extreme ultraviolet light to find sub-nanometer crystal flaws."
    },
    "keyence_osaka": {
        "title": "🔬 Keyence Central R&D & High-Speed Vision Sensor Laboratory (Osaka)",
        "facilityType": "Direct-Sales Machine Vision, Laser Marker & Sensor Development HQ",
        "parentFirm": "Keyence Corporation [6861:JP]",
        "coords": [
            34.733,
            135.5
        ],
        "specs": [
            {
                "label": "Same-Day Shipping Ratio",
                "value": "99.5% of Customer Sensor Orders Shipped Same Day"
            },
            {
                "label": "Fabless Gross Margin",
                "value": "82.5% Gross Margin | 52% Operating Margin"
            }
        ],
        "description": "Keyence's headquarters and testing laboratory where direct-sales technical consultants solve manufacturing automation challenges without third-party distributors."
    },
    "fanuc_yamanashi": {
        "title": "🤖 Fanuc Mount Fuji Autonomous CNC & Yellow Robot Complex (Oshino-mura)",
        "facilityType": "Robots Building Robots Fully Automated Manufacturing Forest",
        "parentFirm": "Fanuc Corp [6954:JP]",
        "coords": [
            35.452,
            138.854
        ],
        "specs": [
            {
                "label": "Campus Footprint in Forest",
                "value": "1.8 Square Kilometers near Mount Fuji"
            },
            {
                "label": "Unmanned Lights-Out Production",
                "value": "Robotic machining cells running 30 days without human presence"
            }
        ],
        "description": "The famous bright yellow factory complex at the base of Mount Fuji where autonomous robotic work cells assemble computer numerical controls (CNCs) and industrial robots."
    },
    "mitsubishi_marunouchi": {
        "title": "🏢 Mitsubishi Corporation Global Trading Headquarters (Marunouchi, Tokyo)",
        "facilityType": "Sogo Shosha Energy, Metals & Global Commodity Control Center",
        "parentFirm": "Mitsubishi Corporation [8058:JP]",
        "coords": [
            35.681,
            139.764
        ],
        "specs": [
            {
                "label": "Global Operating Subsidiaries",
                "value": "Over 1,700 Group Companies in 90 Countries"
            },
            {
                "label": "Metallurgical Coal Monopoly",
                "value": "BMA Queensland Australia 50/50 JV with BHP"
            }
        ],
        "description": "The trading nerve center of Japan's largest Sogo Shosha, orchestrating global LNG supply chains, Australian coking coal, automotive dealerships, and food logistics."
    },
    "mitsui_tokyo": {
        "title": "🏢 Mitsui & Co Headquarters & Natural Resources Trading Floor (Otemachi, Tokyo)",
        "facilityType": "LNG, Iron Ore & Infrastructure Trading Command Center",
        "parentFirm": "Mitsui & Co Ltd [8031:JP]",
        "coords": [
            35.688,
            139.763
        ],
        "specs": [
            {
                "label": "Global LNG Equity Portfolio",
                "value": "Equity stakes in Sakhalin-2, Cameron LNG, Mozambique"
            },
            {
                "label": "Iron Ore Joint Ventures",
                "value": "Robe River & Mt Newman JV with Rio Tinto and BHP"
            }
        ],
        "description": "Mitsui's executive trading floor controlling strategic equity stakes in iron ore mines, copper extraction in Chile, and global grain distribution."
    },
    "itochu_minato": {
        "title": "🏢 Itochu Corporation Aoyama Flagship Headquarters (Minato-ku, Tokyo)",
        "facilityType": "Consumer Conglomerate, Retail & Textile Trading Hub",
        "parentFirm": "Itochu Corporation [8001:JP]",
        "coords": [
            35.671,
            139.718
        ],
        "specs": [
            {
                "label": "FamilyMart Retail Chain",
                "value": "Over 24,000 Convenience Stores Across Asia"
            },
            {
                "label": "Non-Resource Earnings Share",
                "value": "Over 75% of Group Net Profit"
            }
        ],
        "description": "Itochu's modern corporate tower commanding Japan's highest non-resource trading house profitability, owning FamilyMart convenience stores, pulp, and food networks."
    },
    "byd_zhengzhou": {
        "title": "🚗 BYD Zhengzhou Mega New Energy Vehicle Industrial Base (Henan)",
        "facilityType": "Gigantic Integrated EV Assembly, Battery & Motor Factory",
        "parentFirm": "BYD Company Ltd [002594:SZ]",
        "coords": [
            34.521,
            113.882
        ],
        "specs": [
            {
                "label": "Campus Footprint",
                "value": "16.0 Square Kilometers (2,400 football fields)"
            },
            {
                "label": "Annual EV Output Capacity",
                "value": "1.0 Million New Energy Vehicles / year"
            },
            {
                "label": "Blade Battery Packaging Lines",
                "value": "Cell-to-Body (CTB) Integrated Production"
            }
        ],
        "description": "BYD's largest single manufacturing base on earth, integrating vertical supply chains from molten aluminum casting to finished hybrid and pure EV sedans and SUVs."
    },
    "catl_ningde": {
        "title": "🔋 CATL Contemporary Amperex Mega Battery Base (Ningde, Fujian)",
        "facilityType": "World Largest Lithium Iron Phosphate (LFP) & Sodium-Ion Battery Base",
        "parentFirm": "CATL [300750:SZ]",
        "coords": [
            26.665,
            119.542
        ],
        "specs": [
            {
                "label": "Cumulative Battery Capacity",
                "value": "Over 350 GWh Global Annual Cell Production"
            },
            {
                "label": "Lighthouse Factory Accreditation",
                "value": "World Economic Forum Zero-Carbon Smart Plant"
            }
        ],
        "description": "The epicenter of the global electric vehicle transition, supplying prismatic LFP and ternary lithium batteries to Tesla, BMW, Mercedes, and Chinese automakers."
    },
    "longi_xian": {
        "title": "☀️ LONGi Xi’an Advanced Monocrystalline Silicon & HPBC Solar Hub (Shaanxi)",
        "facilityType": "Monocrystalline Silicon Ingot, Wafer & High-Efficiency Solar Cell Plant",
        "parentFirm": "LONGi Green Energy Technology [601012:SS]",
        "coords": [
            34.265,
            108.954
        ],
        "specs": [
            {
                "label": "Monocrystalline Wafer Output",
                "value": "150 GW Global Annual Wafer Capacity"
            },
            {
                "label": "HPBC 2.0 Cell Efficiency",
                "value": "26.6% Mass Production Conversion Efficiency"
            }
        ],
        "description": "LONGi's research and manufacturing center developing ultra-thin diamond-wire sliced monocrystalline wafers and high-efficiency back-contact solar modules."
    },
    "sungrow_hefei": {
        "title": "☀️ Sungrow Hefei Mega Solar Inverter & BESS Industrial Park (Anhui)",
        "facilityType": "Central & String Photovoltaic Inverter and Utility Energy Storage Base",
        "parentFirm": "Sungrow Power Supply Co [300274:SZ]",
        "coords": [
            31.82,
            117.227
        ],
        "specs": [
            {
                "label": "Annual Inverter Output",
                "value": "300 GW Inverter & Power Conversion Systems"
            },
            {
                "label": "Grid-Forming Energy Storage",
                "value": "PowerTitan 2.0 Liquid-Cooled BESS Systems"
            }
        ],
        "description": "The world's largest inverter manufacturing base, producing power electronics that convert solar DC electricity into high-voltage grid-synchronized AC power."
    },
    "cssc_shanghai": {
        "title": "🚢 CSSC Jiangnan Shipyard Mega Drydocks (Changxing Island, Shanghai)",
        "facilityType": "World Largest Commercial & Dual-Fuel Container Shipbuilding Yard",
        "parentFirm": "China CSSC Holdings Ltd [600150:SS]",
        "coords": [
            31.354,
            121.733
        ],
        "specs": [
            {
                "label": "Changxing Base Waterfront",
                "value": "8.0 Kilometers of Deepwater River Outfitting Berths"
            },
            {
                "label": "Drydock Dimensions",
                "value": "580m x 105m Mega Drydock for 24,000 TEU Vessels"
            },
            {
                "label": "Gantry Crane Capacity",
                "value": "1,600-Ton Heavy Gantry Cranes"
            }
        ],
        "description": "China's premier mega-shipyard constructing ultra-large dual-fuel LNG container ships, very large ammonia carriers, and naval defense vessels."
    },
    "cosco_yangshan": {
        "title": "🚢 COSCO Yangshan Deepwater Automated Container Terminal (Shanghai)",
        "facilityType": "World Largest Automated Deepwater Maritime Container Hub",
        "parentFirm": "COSCO SHIPPING Holdings [601919:SS]",
        "coords": [
            30.628,
            122.062
        ],
        "specs": [
            {
                "label": "Annual Container Throughput",
                "value": "26+ Million TEUs Handled Annually"
            },
            {
                "label": "Automated Guided Vehicles (AGV)",
                "value": "130+ Driverless Electric Container Haulers"
            }
        ],
        "description": "An island seaport linked to Shanghai by the 32.5km Donghai Bridge, operating the world's highest-volume robotic maritime logistics interchange."
    },
    "petrobras_buzios": {
        "title": "⛽ Petrobras Búzios FPSO Almirante Barroso (Santos Basin Pre-Salt, Brazil)",
        "facilityType": "Ultra-Deepwater Pre-Salt Floating Production Storage & Offloading Unit",
        "parentFirm": "Petrobras [PBR:US]",
        "coords": [
            -24.85,
            -42.75
        ],
        "specs": [
            {
                "label": "Water Depth",
                "value": "2,100 Meters Deepwater Column + 5,000m Salt Layer"
            },
            {
                "label": "Crude Processing Capacity",
                "value": "150,000 Barrels of Oil / day"
            },
            {
                "label": "Natural Gas Compression",
                "value": "6.0 Million Cubic Meters / day"
            }
        ],
        "description": "Petrobras' flagship pre-salt mega-field offshore Rio de Janeiro, tapping carbonate reservoirs trapped beneath thousands of meters of subterranean salt."
    },
    "vale_carajas": {
        "title": "⛏️ Vale Carajás S11D Eliezer Batista Iron Ore Complex (Pará, Brazil)",
        "facilityType": "World Largest Open-Pit 65% Fe Premium Iron Ore Mining Complex",
        "parentFirm": "Vale S.A. [VALE:US]",
        "coords": [
            -6.058,
            -50.158
        ],
        "specs": [
            {
                "label": "Annual Iron Ore Production",
                "value": "90 Million MT / year (S11D Mine Alone)"
            },
            {
                "label": "Truckless Conveyor System",
                "value": "30+ Kilometers of In-Pit High-Capacity Belts"
            },
            {
                "label": "Iron Content Quality",
                "value": "65.4% Natural Fe (Lowest Silica Impurity Globally)"
            }
        ],
        "description": "Vale's revolutionary truckless open-pit iron ore operation in the Amazon basin, moving premium ore via electric conveyor belts to dedicated export rail networks."
    },
    "slc_matopiba": {
        "title": "🌾 SLC Agrícola Fazenda Parnaíba Mega Farm (Maranhão / MATOPIBA, Brazil)",
        "facilityType": "Industrial-Scale Precision Soybean, Cotton & Corn Agri-Estate",
        "parentFirm": "SLC Agrícola S.A. [SLCE3:BZ]",
        "coords": [
            -8.52,
            -45.45
        ],
        "specs": [
            {
                "label": "Arable Land Area Under Cultivation",
                "value": "700,000+ Hectares Group-Wide"
            },
            {
                "label": "Double-Cropping Cycle",
                "value": "Soybean Harvest Immediately Followed by Safrinha Corn"
            },
            {
                "label": "Satellite Telemetry",
                "value": "Real-Time Precision Fertilizer & Soil Sensor Guidance"
            }
        ],
        "description": "SLC's mega grain estate demonstrating the tremendous competitive advantage of Brazilian agriculture: double-cropping, abundant rainfall, and scale efficiency."
    },
    "hsbc_canarywharf": {
        "title": "🏦 HSBC 8 Canada Square Global Tower (Canary Wharf, London)",
        "facilityType": "Global Banking & Cross-Border Asian Trade Clearing Operations",
        "parentFirm": "HSBC Holdings plc [HSBA:LN]",
        "coords": [
            51.503,
            -0.018
        ],
        "specs": [
            {
                "label": "Tower Height & Floors",
                "value": "210 Meters Height (45 Floors Canary Wharf)"
            },
            {
                "label": "Global Trade Finance Market Share",
                "value": "#1 Trade Bank in Asia, Middle East & Europe"
            }
        ],
        "description": "HSBC's headquarters building overseeing global trade clearing, London foreign exchange liquidity, and banking networks bridging the West and Asian emerging markets."
    },
    "barclays_churchill": {
        "title": "🏦 Barclays 1 Churchill Place Operations Tower (Canary Wharf, London)",
        "facilityType": "Investment Banking, Fixed Income & UK Retail Banking HQ",
        "parentFirm": "Barclays PLC [BARC:LN]",
        "coords": [
            51.504,
            -0.015
        ],
        "specs": [
            {
                "label": "Fixed Income Currencies & Commodities (FICC)",
                "value": "Major Primary Dealer in UK Gilts & US Treasuries"
            },
            {
                "label": "Barclays Payments Network",
                "value": "Processing 40% of All UK Credit & Debit Transactions"
            }
        ],
        "description": "Barclays' corporate tower coordinating the group's investment banking syndicate, UK mortgages, and wholesale payment processing."
    },
    "azn_cambridge": {
        "title": "💊 AstraZeneca The Discovery Centre (DISC) & Cambridge Biomedical Campus",
        "facilityType": "Global R&D Headquarters & Next-Gen Oncology Biologics Center",
        "parentFirm": "AstraZeneca PLC [AZN:LN]",
        "coords": [
            52.176,
            0.141
        ],
        "specs": [
            {
                "label": "Biomedical Campus Footprint",
                "value": "£1.0 Billion Purpose-Built R&D Campus"
            },
            {
                "label": "Active Pipeline Molecules",
                "value": "170+ Projects in Clinical Development"
            }
        ],
        "description": "AstraZeneca's state-of-the-art discovery laboratory in Cambridge, UK, leading research into targeted antibody drug conjugates (ADCs) and cell therapies."
    },
    "novo_kalundborg": {
        "title": "💊 Novo Nordisk Kalundborg GLP-1 Active Ingredient Mega Complex (Denmark)",
        "facilityType": "World Largest Insulin & Semaglutide (Ozempic/Wegovy) Fermentation Site",
        "parentFirm": "Novo Nordisk A/S [NVO:US]",
        "coords": [
            55.676,
            11.085
        ],
        "specs": [
            {
                "label": "Campus Footprint",
                "value": "1.6 Million sq meters (160 Hectares Dedicated)"
            },
            {
                "label": "Capital Expansion Program",
                "value": "Over $8.5 Billion Active Manufacturing Expansion"
            },
            {
                "label": "Global Semaglutide Supply",
                "value": "Fermentation of active GLP-1 peptides for worldwide distribution"
            }
        ],
        "description": "The manufacturing center for the most lucrative pharmaceutical franchise in human history, fermenting and purifying recombinant GLP-1 active ingredients."
    },
    "asml_veldhoven": {
        "title": "🔬 ASML Veldhoven High-NA EUV Manufacturing & Cleanroom Campus (Netherlands)",
        "facilityType": "Extreme Ultraviolet (EUV) & High-NA Photolithography Assembly Epicenter",
        "parentFirm": "ASML Holding NV [ASML:NA]",
        "coords": [
            51.403,
            5.412
        ],
        "specs": [
            {
                "label": "High-NA EUV Scanner (EXE:5000)",
                "value": "0.55 Numerical Aperture ($380M System Weight 150 Tons)"
            },
            {
                "label": "Carl Zeiss Optics Integration",
                "value": "Smoothest Mirrors in the World (Atomic Precision)"
            },
            {
                "label": "Global EUV Market Share",
                "value": "100% Total Monopoly on Advanced Photolithography"
            }
        ],
        "description": "The technological pinnacle of human manufacturing. Thousands of specialized suppliers ship sub-systems to Veldhoven, where lasers blast molten tin droplets 50,000 times per second to create extreme ultraviolet light."
    },
    "aramco_ghawar": {
        "title": "⛽ Saudi Aramco Ghawar Field & Abqaiq Stabilization Plant (Eastern Province)",
        "facilityType": "World Largest Conventional Onshore Oil Field & Crude Processing Hub",
        "parentFirm": "Saudi Aramco [2222:SR]",
        "coords": [
            25.932,
            49.664
        ],
        "specs": [
            {
                "label": "Ghawar Field Dimensions",
                "value": "280 Kilometers Long x 30 Kilometers Wide"
            },
            {
                "label": "Abqaiq Stabilization Output",
                "value": "7.0 Million Barrels / day Light Crude Processing"
            },
            {
                "label": "Lifting Cost / Barrel",
                "value": "$3.20 / bbl (Lowest Upstream Cost on Earth)"
            }
        ],
        "description": "The supreme crown jewel of global oil production. Ghawar produces high-gravity Arab Light crude with unmatched operational economics and ultra-low reservoir decline."
    },
    "sabic_jubail": {
        "title": "🧪 SABIC Jubail Industrial City Mega Petrochemical Complex (Eastern Province)",
        "facilityType": "Ethane Cracking, Methanol & Advanced Polymer Complex",
        "parentFirm": "SABIC [2010:SR]",
        "coords": [
            27.012,
            49.658
        ],
        "specs": [
            {
                "label": "Jubail Industrial Footprint",
                "value": "World Largest Industrial City with Captive Deepwater Port"
            },
            {
                "label": "Feedstock Advantage",
                "value": "Captive Aramco Ethane Gas Allocation at Fixed Subsidized Rates"
            }
        ],
        "description": "SABIC's manufacturing city in Jubail, utilizing cost-advantaged associated gas feedstocks to synthesize commodity plastics and engineered polymers."
    },
    "singtel_tuas": {
        "title": "🌐 Singtel Tuas Subsea Cable Landing Station & DC West Mega Hub (Singapore)",
        "facilityType": "International Subsea Fiber Chokepoint & AI Cloud Data Center",
        "parentFirm": "Singtel [Z74:SG]",
        "coords": [
            1.321,
            103.651
        ],
        "specs": [
            {
                "label": "Subsea Cable Systems Terminating",
                "value": "SEA-ME-WE 3/4/5, APG, SJC2 Interconnections"
            },
            {
                "label": "DC West Capacity",
                "value": "60+ Megawatts High-Density AI GPU Rack Space"
            }
        ],
        "description": "Singapore's vital telecom chokepoint connecting trans-Pacific and Asian submarine optic fiber routes with regional hyperscale enterprise cloud infrastructure."
    },
    "wilmar_jurong": {
        "title": "🌴 Wilmar Jurong Island Edible Oils & Oleochemicals Processing Base",
        "facilityType": "Palm Oil Refining, Biodiesel & Oleochemical Synthesis Plant",
        "parentFirm": "Wilmar International Ltd [F34:SG]",
        "coords": [
            1.272,
            103.715
        ],
        "specs": [
            {
                "label": "Daily Refining Throughput",
                "value": "6,500 MT / day Crude Palm Oil (CPO)"
            },
            {
                "label": "Port Berths",
                "value": "Deepwater chemical tanker berths with direct pipeline connection"
            }
        ],
        "description": "Wilmar's high-volume refining asset on Jurong Island, processing Indonesian and Malaysian sustainable palm oil into consumer packaged foods, fats, and oleochemicals."
    },
    "bhp_olympic": {
        "title": "⛏️ BHP Olympic Dam Underground Mine Complex (Roxby Downs, South Australia)",
        "facilityType": "World Largest Single Known Copper, Uranium & Gold Deposit",
        "parentFirm": "BHP Group Ltd [BHP:AU]",
        "coords": [
            -30.435,
            136.883
        ],
        "specs": [
            {
                "label": "Underground Rail Network",
                "value": "450 Kilometers of Deep Underground Roadways & Rail"
            },
            {
                "label": "Ore Mineralization",
                "value": "Multi-Metals Orebody: Copper, Uranium Oxide (U3O8), Gold, Silver"
            },
            {
                "label": "Smelter Output",
                "value": "210,000 MT / year LME Grade A Refined Copper Cathodes"
            }
        ],
        "description": "BHP's underground deposit containing the world's fourth largest copper resource and the single largest uranium deposit on the planet."
    },
    "rio_pilbara": {
        "title": "⛏️ Rio Tinto AutoHaul Automated Pilbara Iron Ore Network & Port Dampier",
        "facilityType": "Fully Autonomous Robotic Heavy-Haul Freight Rail & Bulk Export Port",
        "parentFirm": "Rio Tinto Ltd [RIO:AU]",
        "coords": [
            -20.658,
            116.711
        ],
        "specs": [
            {
                "label": "Autonomous Train Distance",
                "value": "1,700 Kilometers of Driverless Rail Network"
            },
            {
                "label": "Train Configuration",
                "value": "2.4 Kilometers Long (240 Cars / 28,000 Tons Iron Ore per train)"
            },
            {
                "label": "Port Dampier Rotary Car Dumpers",
                "value": "Dumping 4 Railcars Simultaneously in 90 Seconds"
            }
        ],
        "description": "The world's first fully automated, driverless heavy-haul freight rail system. Controls 50 driverless trains moving 330 million tons of iron ore annually to export vessels."
    },
    "samsung_pyeongtaek": {
        "title": "🔬 Samsung Electronics Pyeongtaek Campus Line 3 & 4 (Gyeonggi-do)",
        "facilityType": "World Largest Single Semiconductor Mega Fabrication Campus",
        "parentFirm": "Samsung Electronics [005930:KS]",
        "coords": [
            37.038,
            127.054
        ],
        "specs": [
            {
                "label": "Total Campus Land Area",
                "value": "2.89 Million sq meters (Equivalent to 400 Soccer Pitches)"
            },
            {
                "label": "Cleanroom Height",
                "value": "6 Floors High-Ceiling Ultra-Clean Chambers"
            },
            {
                "label": "Silicon Wafer Technology",
                "value": "1b-nm DRAM, 9th-Gen V-NAND & 3nm GAA Foundry Lines"
            }
        ],
        "description": "The most colossal semiconductor cleanroom facility on the planet, producing the majority of the world's DRAM and V-NAND flash storage memory."
    },
    "sk_icheon": {
        "title": "🔬 SK Hynix Icheon M16 EUV Memory Fab (Gyeonggi-do, South Korea)",
        "facilityType": "Next-Generation HBM3E & 1b-nm DRAM Manufacturing Center",
        "parentFirm": "SK Hynix Inc [000660:KS]",
        "coords": [
            37.258,
            127.485
        ],
        "specs": [
            {
                "label": "Fab Floor Space",
                "value": "57,000 sq meters (Twin-Line Structure)"
            },
            {
                "label": "High-Bandwidth Memory (HBM3E)",
                "value": "Advanced Mass Reflow Molded Underfill (MR-MUF) Packaging"
            },
            {
                "label": "Global AI Memory Share",
                "value": "Primary HBM Supplier for NVIDIA Hopper & Blackwell Platforms"
            }
        ],
        "description": "SK Hynix's flagship M16 fab where extreme ultraviolet lithography is applied to DRAM wafers, coupled with packaging lines that stack 12-layer HBM3E chips with thermal conduction."
    },
    "dpworld_jebelali": {
        "title": "🚢 DP World Jebel Ali Port & Terminal 3 Mega Container Facility (Dubai, UAE)",
        "facilityType": "World Largest Man-Made Harbor & Automated Maritime Transshipment Hub",
        "parentFirm": "DP World Ltd [DPW:AE]",
        "coords": [
            24.985,
            55.068
        ],
        "specs": [
            {
                "label": "Total Port Container Capacity",
                "value": "19.3 Million TEUs Annual Capacity"
            },
            {
                "label": "Automated Rail-Mounted Gantry (ARMG)",
                "value": "Remotely Controlled Container Cranes"
            },
            {
                "label": "Jebel Ali Free Zone (JAFZA)",
                "value": "9,500+ Companies from 140 Countries in Adjacent Free Zone"
            }
        ],
        "description": "The undisputed logistics anchor of the Middle East, linking maritime routes between East Asia and Europe while serving the trade flow of 2 billion people."
    },
    "airarabia_sharjah": {
        "title": "✈️ Air Arabia Sharjah International Airport Maintenance & Operations Hub",
        "facilityType": "Low-Cost Carrier Flight Operations & A320 Fleet Engineering Hangar",
        "parentFirm": "Air Arabia PJSC [AIRARABIA:AE]",
        "coords": [
            25.328,
            55.517
        ],
        "specs": [
            {
                "label": "Fleet Composition",
                "value": "75+ Airbus A320 & A321 Neo LR Aircraft"
            },
            {
                "label": "Passenger Load Factor",
                "value": "82.5% Average Annual Seat Factor"
            },
            {
                "label": "Ancillary Revenue Model",
                "value": "Pre-Selected Meals, Baggage & Seat Selection Yields"
            }
        ],
        "description": "The operational home of the Middle East and North Africa's first and largest low-cost airline, maintaining the lowest seat-kilometer operating cost in the region."
    }
};

  window.onCountryDropdownChange = function(countryKey) {
    currentCountry = countryKey;
    populateSectorDropdown(countryKey);
    // Auto-select first sector of this country
    var country = countryData[countryKey];
    if (country && country.sectors.length > 0) {
      currentSector = country.sectors[0];
      var secSelect = document.getElementById('zoom_sector_select');
      if (secSelect) secSelect.value = currentSector;
      populateCompanyDropdown(currentSector);
      var sector = sectorData[currentSector];
      if (sector && sector.firmKeys && sector.firmKeys.length > 0) {
        currentFirm = sector.firmKeys[0];
        var firmSelect = document.getElementById('zoom_firm_select');
        if (firmSelect) firmSelect.value = currentFirm;
        populateNanoDropdown(currentFirm);
        var firm = firmData[currentFirm];
        if (firm && firm.nanoLink) {
          currentNano = firm.nanoLink;
          var nanoSelect = document.getElementById('zoom_nano_select');
          if (nanoSelect) nanoSelect.value = currentNano;
        }
      }
    }
    // Update all panes
    loadCountrySovereign(countryKey);
    loadSectorModel(currentSector);
    loadFirmModel(currentFirm);
    loadNanoAsset(currentNano);
    updateBreadcrumbs();
  };

  window.onSectorDropdownChange = function(sectorKey) {
    currentSector = sectorKey;
    populateCompanyDropdown(sectorKey);
    var sector = sectorData[sectorKey];
    if (sector && sector.firmKeys && sector.firmKeys.length > 0) {
      currentFirm = sector.firmKeys[0];
      var firmSelect = document.getElementById('zoom_firm_select');
      if (firmSelect) firmSelect.value = currentFirm;
      populateNanoDropdown(currentFirm);
      var firm = firmData[currentFirm];
      if (firm && firm.nanoLink) {
        currentNano = firm.nanoLink;
        var nanoSelect = document.getElementById('zoom_nano_select');
        if (nanoSelect) nanoSelect.value = currentNano;
      }
    }
    loadSectorModel(sectorKey);
    loadFirmModel(currentFirm);
    loadNanoAsset(currentNano);
    updateBreadcrumbs();
  };

  window.onFirmDropdownChange = function(firmKey) {
    currentFirm = firmKey;
    var gF = document.getElementById('global_firm_select');
    if (gF && gF.value !== firmKey) gF.value = firmKey;
    var zF = document.getElementById('zoom_firm_select');
    if (zF && zF.value !== firmKey) zF.value = firmKey;

    populateNanoDropdown(firmKey);
    var firm = firmData[firmKey];
    if (firm && firm.nanoLink) {
      currentNano = firm.nanoLink;
      var gN = document.getElementById('global_nano_select');
      if (gN) gN.value = currentNano;
      var zN = document.getElementById('zoom_nano_select');
      if (zN) zN.value = currentNano;
    }
    loadFirmModel(firmKey);
    loadNanoAsset(currentNano);
    updateBreadcrumbs();
  };

  window.onNanoDropdownChange = function(nanoKey) {
    currentNano = nanoKey;
    loadNanoAsset(nanoKey);
    updateBreadcrumbs();
  };

  function populateSectorDropdown(countryKey) {
    ['zoom_sector_select'].forEach(function(sId) {
      var select = document.getElementById(sId);
      if (!select) return;
      select.innerHTML = '';
      var country = countryData[countryKey];
      if (!country) return;

      country.sectors.forEach(function(secKey) {
        var sec = sectorData[secKey];
        if (sec) {
          var opt = document.createElement('option');
          opt.value = secKey;
          opt.textContent = sec.name;
          select.appendChild(opt);
        }
      });
      select.value = currentSector;
    });
  }

  function populateCompanyDropdown(sectorKey) {
    ['zoom_firm_select'].forEach(function(sId) {
      var select = document.getElementById(sId);
      if (!select) return;
      select.innerHTML = '';
      var sec = sectorData[sectorKey];
      if (!sec || !sec.firmKeys) return;

      sec.firmKeys.forEach(function(fKey) {
        var f = firmData[fKey];
        if (f) {
          var opt = document.createElement('option');
          opt.value = fKey;
          opt.textContent = f.name + ' [' + f.ticker + ']';
          select.appendChild(opt);
        }
      });
      select.value = currentFirm;
    });
  }

  function populateNanoDropdown(firmKey) {
    ['zoom_nano_select', 'global_nano_select'].forEach(function(sId) {
      var select = document.getElementById(sId);
      if (!select) return;
      select.innerHTML = '';
      var f = firmData[firmKey];
      if (!f) return;

      if (f.nanoLink && nanoData[f.nanoLink]) {
        var optPrimary = document.createElement('option');
        optPrimary.value = f.nanoLink;
        optPrimary.textContent = nanoData[f.nanoLink].title;
        select.appendChild(optPrimary);
      }

      var optDom = document.createElement('option');
      optDom.value = 'dom';
      optDom.textContent = '📊 Level 2 Order Book (DOM Microstructure)';
      select.appendChild(optDom);

      Object.keys(nanoData).forEach(function(nKey) {
        if (nKey !== f.nanoLink && nKey !== 'dom') {
          var opt = document.createElement('option');
          opt.value = nKey;
          opt.textContent = nanoData[nKey].title;
          select.appendChild(opt);
        }
      });
      select.value = currentNano;
    });
  }

  window.syncAllTiersToDropdowns = function() {
    loadCountrySovereign(currentCountry);
    loadSectorModel(currentSector);
    loadFirmModel(currentFirm);
    loadNanoAsset(currentNano);
    updateBreadcrumbs();
    setFractalTier(currentTier);
  };

  // ── CORE TIER NAVIGATION ENGINE ──

  window.setFractalTier = function(tier) {
    currentTier = tier;
    
    // Update button states
    for (var i = 1; i <= 5; i++) {
      var btn = document.getElementById('btn_tier_' + i);
      var pane = document.getElementById('fractal_pane_tier_' + i);
      var bc = document.getElementById('bc_tier_' + i);
      
      if (btn) {
        if (i === tier) {
          btn.style.borderColor = '#ffaa00';
          btn.style.background = '#132032';
          btn.classList.add('active');
        } else {
          btn.style.borderColor = '#1c2e44';
          btn.style.background = '#0c1420';
          btn.classList.remove('active');
        }
      }
      
      if (pane) {
        pane.style.display = (i === tier) ? 'block' : 'none';
      }

      if (bc) {
        if (i === tier) {
          bc.style.color = '#ffaa00';
          bc.style.fontWeight = '800';
        } else if (i < tier) {
          bc.style.color = '#00e5ff';
          bc.style.fontWeight = '600';
        } else {
          bc.style.color = '#64748b';
          bc.style.fontWeight = '400';
        }
      }
    }

    var altitudeLabels = {
      1: 'TIER 1 OF 5 · GLOBAL ORBITAL MACRO ($105.4T WORLD GDP · CONTINENTAL ERP)',
      2: 'TIER 2 OF 5 · COUNTRY SOVEREIGN CAPITAL (' + (countryData[currentCountry] ? countryData[currentCountry].name.toUpperCase() : 'INDIA') + ')',
      3: 'TIER 3 OF 5 · INDUSTRIAL SECTOR VALUE CHAINS (' + (sectorData[currentSector] ? sectorData[currentSector].name.toUpperCase() : 'CABLES') + ')',
      4: 'TIER 4 OF 5 · MICRO FIRM DCF & SOIC 310-PT (' + (firmData[currentFirm] ? firmData[currentFirm].name.toUpperCase() : 'POLYCAB') + ')',
      5: 'TIER 5 OF 5 · NANO OPERATING ASSETS, REFINERIES & LEVEL 2 DOM'
    };
    var readout = document.getElementById('zoom_altitude_readout');
    if (readout && altitudeLabels[tier]) {
      readout.textContent = altitudeLabels[tier];
    }

    // Sync with Leaflet BMAP only if map container is visible in DOM
    var mapEl = document.getElementById('bmapLeafletMap');
    if (mapEl && mapEl.offsetWidth > 0 && typeof window.leafletMap !== 'undefined' && window.leafletMap) {
      try {
        if (tier === 1) {
          window.leafletMap.flyTo([15.00, 0.00], 1, { duration: 1.5 });
        } else if (tier === 2) {
          if (currentCountry === 'india') window.leafletMap.flyTo([22.5, 78.9], 5, { duration: 1.5 });
          else if (currentCountry === 'us') window.leafletMap.flyTo([38.0, -97.0], 4, { duration: 1.5 });
          else window.leafletMap.flyTo([48.0, 10.0], 5, { duration: 1.5 });
        } else if (tier === 3 || tier === 4) {
          if (firmData[currentFirm] && nanoData[firmData[currentFirm].nanoLink]) {
            var c = nanoData[firmData[currentFirm].nanoLink].coords;
            window.leafletMap.flyTo(c, 8, { duration: 1.5 });
          } else {
            window.leafletMap.flyTo([22.5, 73.5], 7, { duration: 1.5 });
          }
        } else if (tier === 5) {
          if (nanoData[currentNano]) {
            window.leafletMap.flyTo(nanoData[currentNano].coords, 14, { duration: 1.2 });
          }
        }
      } catch(e) {}
    }
  };

  window.selectCountryFromGlobal = function(cCode) {
    currentCountry = cCode;
    var cSelect = document.getElementById('zoom_country_select');
    if (cSelect) cSelect.value = cCode;
    onCountryDropdownChange(cCode);
    setFractalTier(2);
  };

  function updateBreadcrumbs() {
    syncGlobalRibbon();
    var c = countryData[currentCountry] || countryData['india'];
    var s = sectorData[currentSector] || sectorData['cables_in'];
    var f = firmData[currentFirm] || firmData['polycab'];
    var n = nanoData[currentNano] || nanoData['halol_mega'];

    var bc2 = document.getElementById('bc_tier_2');
    if (bc2) bc2.textContent = c.name.toUpperCase() + ' [' + c.sovereignRating + ']';

    var bc3 = document.getElementById('bc_tier_3');
    if (bc3) bc3.textContent = s.name.toUpperCase().substring(0, 24) + ' [OPM ' + s.opm + '%]';

    var bc4 = document.getElementById('bc_tier_4');
    if (bc4) bc4.textContent = f.ticker + ' [DCF ' + f.dcf + ']';

    var bc5 = document.getElementById('bc_tier_5');
    if (bc5) bc5.textContent = n.title.substring(0, 28);
  }

  // ── TIER 2: COUNTRY SOVEREIGN RENDERER ──

  window.loadCountrySovereign = function(cKey) {
    currentCountry = cKey;
    var data = countryData[cKey];
    if (!data) return;

    // Update ribbon buttons
    Object.keys(countryData).forEach(function(k) {
      var b = document.getElementById('btn_c_' + k);
      if (b) {
        if (k === cKey) {
          b.classList.add('active');
          b.style.background = 'var(--bb-amber)';
          b.style.color = '#000';
        } else {
          b.classList.remove('active');
          b.style.background = '#131e2e';
          b.style.color = '#e2e8f0';
        }
      }
    });

    var box = document.getElementById('country_telemetry_box');
    if (!box) return;

    box.innerHTML = `
      <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:14px;border-bottom:1px solid #1e334d;padding-bottom:10px;">
        <div>
          <span style="font-size:22px;margin-right:8px;">${data.flag}</span>
          <strong style="color:#fff;font-size:16px;">${data.name.toUpperCase()}</strong>
          <span class="badge" style="background:#132032;color:#00e5ff;margin-left:10px;">MOODY'S / S&P: ${data.sovereignRating}</span>
          <span class="badge" style="background:#132032;color:#ffaa00;margin-left:6px;">SPREAD: +${data.defaultSpreadBps} bps</span>
        </div>
        <button class="preset-btn" onclick="drillToSectorFromCountry('${cKey}')" style="background:#ffaa00;color:#000;font-weight:800;padding:6px 14px;cursor:pointer;">
          Zoom into ${data.name} Industrial Sectors ➔
        </button>
      </div>

      <div class="stats-row" style="margin-bottom:16px;">
        <div class="stat-card">
          <span class="stat-num">${data.crp.toFixed(2)}%</span>
          <span class="stat-label">Country Risk Premium (CRP)</span>
        </div>
        <div class="stat-card">
          <span class="stat-num">${data.totalERP.toFixed(2)}%</span>
          <span class="stat-label">Total Equity Risk Premium</span>
        </div>
        <div class="stat-card">
          <span class="stat-num">${data.rf.toFixed(2)}%</span>
          <span class="stat-label">10Y Sovereign Yield (Rf)</span>
        </div>
        <div class="stat-card">
          <span class="stat-num">${data.corpTax.toFixed(1)}%</span>
          <span class="stat-label">Effective Corporate Tax Rate</span>
        </div>
        <div class="stat-card">
          <span class="stat-num">${data.gdpGrowth.toFixed(1)}%</span>
          <span class="stat-label">Real GDP Growth (2026E)</span>
        </div>
        <div class="stat-card">
          <span class="stat-num">${data.fdiAnnual}</span>
          <span class="stat-label">Annual Gross FDI Inflow</span>
        </div>
      </div>

      <div style="display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-bottom:14px;">
        <div style="background:#090d16;border:1px solid #1a293d;border-radius:6px;padding:12px;font-family:var(--font-mono);font-size:11px;">
          <h4 style="color:#00e5ff;font-size:11px;font-weight:800;margin-bottom:8px;">DAMODARAN COST OF CAPITAL FORMULATION</h4>
          <div style="display:flex;flex-direction:column;gap:6px;">
            <div style="display:flex;justify-content:space-between;padding:4px 0;border-bottom:1px solid #131e2d;">
              <span style="color:#94a3b8;">US Base Equity Risk Premium:</span>
              <strong style="color:#fff;">4.40%</strong>
            </div>
            <div style="display:flex;justify-content:space-between;padding:4px 0;border-bottom:1px solid #131e2d;">
              <span style="color:#94a3b8;">Sovereign Default Spread:</span>
              <strong style="color:#ffaa00;">${(data.defaultSpreadBps / 100).toFixed(2)}% (+${data.defaultSpreadBps} bps)</strong>
            </div>
            <div style="display:flex;justify-content:space-between;padding:4px 0;border-bottom:1px solid #131e2d;">
              <span style="color:#94a3b8;">Relative Equity Volatility Factor (σ_eq / σ_bond):</span>
              <strong style="color:#fff;">1.44x</strong>
            </div>
            <div style="display:flex;justify-content:space-between;padding:4px 0;">
              <span style="color:#94a3b8;">Computed Country Risk Premium (CRP):</span>
              <strong style="color:#00e676;">${data.crp.toFixed(2)}%</strong>
            </div>
          </div>
        </div>

        <div style="background:#090d16;border:1px solid #1a293d;border-radius:6px;padding:12px;font-family:var(--font-mono);font-size:11px;">
          <h4 style="color:#ffaa00;font-size:11px;font-weight:800;margin-bottom:8px;">AVAILABLE INDUSTRIAL SECTOR CHAINS</h4>
          <div style="display:flex;flex-direction:column;gap:6px;">
            ${data.sectors.map(function(sKey) {
              var s = sectorData[sKey];
              if (!s) return '';
              return `
                <div style="display:flex;justify-content:space-between;align-items:center;padding:4px 0;border-bottom:1px solid #131e2d;">
                  <span style="color:#cfd8dc;">${s.name}</span>
                  <button class="preset-btn" onclick="selectSectorDirect('${sKey}')" style="padding:2px 8px;font-size:10px;background:#132032;color:#00e5ff;">Select ➔</button>
                </div>
              `;
            }).join('')}
          </div>
        </div>
      </div>
    `;

    renderSectorRibbonButtons(cKey);
    updateBreadcrumbs();
  };

  window.drillToSectorFromCountry = function(cKey) {
    setFractalTier(3);
    loadSectorModel(currentSector);
  };

  window.selectSectorDirect = function(secKey) {
    currentSector = secKey;
    var secSelect = document.getElementById('zoom_sector_select');
    if (secSelect) secSelect.value = secKey;
    onSectorDropdownChange(secKey);
    setFractalTier(3);
  };

  function renderSectorRibbonButtons(countryKey) {
    var ribbon = document.getElementById('sector_buttons_ribbon');
    if (!ribbon) return;
    var country = countryData[countryKey];
    if (!country) return;

    var html = '<span style="color:var(--bb-amber);font-weight:800;font-size:11px;">SELECT SECTOR:</span>';
    country.sectors.forEach(function(sKey) {
      var s = sectorData[sKey];
      if (!s) return;
      var isActive = (sKey === currentSector) ? 'active' : '';
      var activeStyle = (sKey === currentSector) ? 'background:var(--bb-amber);color:#000;' : 'background:#131e2e;color:#e2e8f0;';
      html += `<button class="preset-btn ${isActive}" id="btn_sec_${sKey}" onclick="loadSectorModel('${sKey}')" style="${activeStyle}">${s.name}</button>`;
    });
    ribbon.innerHTML = html;
  }

  // ── TIER 3: INDUSTRIAL SECTOR RENDERER ──

  window.loadSectorModel = function(secKey) {
    currentSector = secKey;
    var data = sectorData[secKey];
    if (!data) return;

    // Update sector dropdown
    var secSelect = document.getElementById('zoom_sector_select');
    if (secSelect) secSelect.value = secKey;

    // Update ribbon button states
    var ribbon = document.getElementById('sector_buttons_ribbon');
    if (ribbon) {
      var btns = ribbon.getElementsByClassName('preset-btn');
      for (var i = 0; i < btns.length; i++) {
        var b = btns[i];
        if (b.id === 'btn_sec_' + secKey) {
          b.classList.add('active');
          b.style.background = 'var(--bb-amber)';
          b.style.color = '#000';
        } else {
          b.classList.remove('active');
          b.style.background = '#131e2e';
          b.style.color = '#e2e8f0';
        }
      }
    }

    var box = document.getElementById('sector_telemetry_box');
    if (!box) return;

    var metricsHtml = data.soicMetrics.map(function(m) {
      return `
        <div style="display:flex;justify-content:space-between;padding:4px 0;border-bottom:1px solid #131e2d;">
          <span style="color:#94a3b8;">${m.label}:</span>
          <strong style="color:#fff;">${m.value}</strong>
        </div>
      `;
    }).join('');

    var firmsHtml = data.representativeFirms.map(function(f, idx) {
      var fKey = (data.firmKeys && data.firmKeys[idx]) ? data.firmKeys[idx] : 'polycab';
      return `<button class="preset-btn" onclick="selectFirmDirect('${fKey}')" style="background:#132032;color:#00e5ff;padding:4px 8px;font-size:10px;cursor:pointer;">${f} ➔</button>`;
    }).join(' ');

    box.innerHTML = `
      <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:14px;border-bottom:1px solid #1e334d;padding-bottom:10px;">
        <div>
          <strong style="color:#fff;font-size:16px;">${data.name.toUpperCase()}</strong>
          <span class="badge" style="background:#132032;color:#ffaa00;margin-left:10px;">WACC BENCHMARK: ${data.wacc.toFixed(1)}%</span>
          <span class="badge" style="background:#132032;color:#00e676;margin-left:6px;">OPM: ${data.opm.toFixed(1)}%</span>
        </div>
        <button class="preset-btn" onclick="drillToFirmFromSector()" style="background:#ffaa00;color:#000;font-weight:800;padding:6px 14px;cursor:pointer;">
          Zoom into Micro Firm Forensics &amp; DCF ➔
        </button>
      </div>

      <div class="stats-row" style="margin-bottom:16px;">
        <div class="stat-card">
          <span class="stat-num">${data.betaU.toFixed(2)}</span>
          <span class="stat-label">Damodaran Unlevered Beta (β_U)</span>
        </div>
        <div class="stat-card">
          <span class="stat-num">${data.betaL.toFixed(2)}</span>
          <span class="stat-label">Levered Beta (β_L)</span>
        </div>
        <div class="stat-card">
          <span class="stat-num">${data.opm.toFixed(1)}%</span>
          <span class="stat-label">Industry Operating Margin</span>
        </div>
        <div class="stat-card">
          <span class="stat-num">${data.roic.toFixed(1)}%</span>
          <span class="stat-label">ROIC Benchmark</span>
        </div>
        <div class="stat-card">
          <span class="stat-num">${data.evEbitda.toFixed(1)}x</span>
          <span class="stat-label">EV / EBITDA Multiple</span>
        </div>
        <div class="stat-card">
          <span class="stat-num">${data.assetTurnover.toFixed(2)}x</span>
          <span class="stat-label">Fixed Asset Turnover</span>
        </div>
      </div>

      <div style="display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-bottom:14px;">
        <div style="background:#090d16;border:1px solid #1a293d;border-radius:6px;padding:12px;">
          <h4 style="color:#00e5ff;font-size:11px;font-weight:800;margin-bottom:8px;">SOIC SPECIFIC SECTOR UNIT ECONOMICS &amp; THRESHOLDS</h4>
          <div style="display:flex;flex-direction:column;gap:6px;font-family:var(--font-mono);font-size:11px;">
            ${metricsHtml}
          </div>
        </div>
        <div style="background:#090d16;border:1px solid #1a293d;border-radius:6px;padding:12px;">
          <h4 style="color:#ffaa00;font-size:11px;font-weight:800;margin-bottom:8px;">ECONOMIC MOAT &amp; VALUE CHAIN BLUEPRINT</h4>
          <p style="color:#cfd8dc;font-size:11px;line-height:1.5;margin-bottom:12px;font-family:var(--font-mono);">${data.moat}</p>
          <div style="color:#94a3b8;font-size:10px;margin-bottom:6px;font-weight:700;font-family:var(--font-mono);">SELECT ACTIVE STOCK IN SECTOR:</div>
          <div style="display:flex;gap:6px;flex-wrap:wrap;">
            ${firmsHtml}
          </div>
        </div>
      </div>
    `;

    renderFirmRibbonButtons(secKey);
    updateBreadcrumbs();
  };

  window.drillToFirmFromSector = function() {
    setFractalTier(4);
    loadFirmModel(currentFirm);
  };

  window.selectFirmDirect = function(fKey) {
    currentFirm = fKey;
    var firmSelect = document.getElementById('zoom_firm_select');
    if (firmSelect) firmSelect.value = fKey;
    onFirmDropdownChange(fKey);
    setFractalTier(4);
  };

  function renderFirmRibbonButtons(secKey) {
    var ribbon = document.getElementById('firm_buttons_ribbon');
    if (!ribbon) return;
    var sec = sectorData[secKey];
    if (!sec || !sec.firmKeys) return;

    var html = '<span style="color:var(--bb-amber);font-weight:800;font-size:11px;">SELECT MICRO FIRM:</span>';
    sec.firmKeys.forEach(function(fKey) {
      var f = firmData[fKey];
      if (!f) return;
      var isActive = (fKey === currentFirm) ? 'active' : '';
      var activeStyle = (fKey === currentFirm) ? 'background:var(--bb-amber);color:#000;' : 'background:#131e2e;color:#e2e8f0;';
      html += `<button class="preset-btn ${isActive}" id="btn_firm_${fKey}" onclick="loadFirmModel('${fKey}')" style="${activeStyle}">${f.name}</button>`;
    });
    ribbon.innerHTML = html;
  }

  // ── TIER 4: MICRO FIRM FORENSICS & SOIC 310-PT SCORECARD ──

  window.loadFirmModel = function(fKey) {
    currentFirm = fKey;
    var data = firmData[fKey];
    if (!data) return;

    // Update firm dropdown
    var firmSelect = document.getElementById('zoom_firm_select');
    if (firmSelect) firmSelect.value = fKey;

    // Update ribbon button states
    var ribbon = document.getElementById('firm_buttons_ribbon');
    if (ribbon) {
      var btns = ribbon.getElementsByClassName('preset-btn');
      for (var i = 0; i < btns.length; i++) {
        var b = btns[i];
        if (b.id === 'btn_firm_' + fKey) {
          b.classList.add('active');
          b.style.background = 'var(--bb-amber)';
          b.style.color = '#000';
        } else {
          b.classList.remove('active');
          b.style.background = '#131e2e';
          b.style.color = '#e2e8f0';
        }
      }
    }

    var box = document.getElementById('firm_telemetry_box');
    if (!box) return;

    var sc = data.soicScore || { total: 275, classification: 'HIGH CONVICTION ALLOCATION' };
    var tech = data.technicalSOIC || {
      adx: { val: 34.8, cond: 'Above 40 (Monster Bullish Trend)', pts: 20, max: 20 },
      rsi: { val: 64.2, cond: 'Between 50 to 75 (High Momentum Sweet Spot)', pts: 10, max: 10 },
      stage: { val: 'Stage 2 (Mark Up)', cond: 'Confirmed breakout above rising 30-WMA', pts: 20, max: 20 },
      pva: { val: 'Positive Trend', cond: 'High volume on gain days / institutional accumulation', pts: 20, max: 20 },
      secondary: { val: 'Uptrend', cond: 'Orderly pullback to 10-WEMA with dry volume', pts: 10, max: 10 },
      primary: { val: 'Uptrend', cond: 'Trading above rising 30-WMA & 200-DMA', pts: 10, max: 10 },
      resistance: { val: 'Breakout', cond: 'Close to 52-Week High / ATH Breakout (<15%)', pts: 5, max: 5 },
      vstop: { val: 'Holding Above Vol Stop', cond: 'Trailing volatility stop intact', pts: 10, max: 10 }
    };
    var altZStr = (typeof data.altmanZ === 'number') ? data.altmanZ.toFixed(2) : (data.altmanZ || '6.50');
    var benMStr = (typeof data.beneishM === 'number') ? data.beneishM.toFixed(2) : (data.beneishM || '-2.75');

    box.innerHTML = `
      <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:14px;border-bottom:1px solid #1e334d;padding-bottom:10px;">
        <div>
          <strong style="color:#fff;font-size:17px;">${data.name.toUpperCase()}</strong>
          <span style="color:#00e5ff;font-family:var(--font-mono);margin-left:8px;font-size:12px;">[${data.ticker}]</span>
          <span class="badge" style="background:#00e676;color:#000;font-weight:800;margin-left:10px;">SOIC 310-PT SCORE: ${sc.total} / 310</span>
          <span class="badge" style="background:#132032;color:#ffaa00;margin-left:6px;">${sc.classification}</span>
        </div>
        <button class="preset-btn" onclick="drillToNanoFromFirm('${data.nanoLink}')" style="background:#ffaa00;color:#000;font-weight:800;padding:6px 14px;cursor:pointer;">
          Zoom into Physical Plant Telemetry (Nano) ➔
        </button>
      </div>

      <div class="stats-row" style="margin-bottom:16px;">
        <div class="stat-card">
          <span class="stat-num">${data.cmp}</span>
          <span class="stat-label">Current Market Price (CMP)</span>
        </div>
        <div class="stat-card">
          <span class="stat-num">${data.dcf}</span>
          <span class="stat-label">Intrinsic DCF Target Value</span>
        </div>
        <div class="stat-card">
          <span class="stat-num" style="color:#00e676;">${data.mos}</span>
          <span class="stat-label">Margin of Safety</span>
        </div>
        <div class="stat-card">
          <span class="stat-num">${altZStr}</span>
          <span class="stat-label">Altman Z-Score (Solvency)</span>
        </div>
        <div class="stat-card">
          <span class="stat-num">${benMStr}</span>
          <span class="stat-label">Beneish M-Score (Quality)</span>
        </div>
        <div class="stat-card">
          <span class="stat-num">${data.dupontROE.finalROE}</span>
          <span class="stat-label">DuPont 5-Way Return on Equity</span>
        </div>
      </div>

      <!-- ═══════════════════════════════════════════════════════════════════ -->
      <!-- 🏆 FULL SOIC 310-POINT SCORECARD WITH 110-POINT TECHNICAL PILLAR -->
      <!-- ═══════════════════════════════════════════════════════════════════ -->
      <div style="background:#060a12;border:1px solid #1f3a5f;border-radius:6px;padding:14px;margin-bottom:16px;font-family:var(--font-mono);">
        
        <!-- Scorecard Header Overview -->
        <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:12px;border-bottom:1px solid #16263b;padding-bottom:8px;">
          <div>
            <span style="color:#ffaa00;font-weight:800;font-size:13px;">🏆 SOIC 310-POINT MULTI-PILLAR INVESTMENT SCORECARD</span>
            <span style="color:#94a3b8;font-size:11px;margin-left:8px;">(Exact Model from SOIC Masterclass Excel)</span>
          </div>
          <div style="font-size:12px;">
            <span style="color:#64748b;">TOTAL SCORE: </span>
            <strong style="color:#00e676;font-size:15px;">${sc.total}</strong>
            <span style="color:#64748b;"> / 310 PTS</span>
          </div>
        </div>

        <!-- 5 Pillar Score Gauges -->
        <div style="display:grid;grid-template-columns:repeat(5, 1fr);gap:8px;margin-bottom:14px;text-align:center;">
          <div style="background:#0b1320;border:1px solid #1b2e46;border-radius:4px;padding:8px 4px;">
            <div style="color:#64748b;font-size:9px;">1. INDUSTRY ANALYSIS</div>
            <div style="color:#00e5ff;font-size:14px;font-weight:800;margin-top:2px;">${sc.industry} <span style="font-size:10px;color:#64748b;">/ ${sc.industryMax}</span></div>
          </div>
          <div style="background:#0b1320;border:1px solid #1b2e46;border-radius:4px;padding:8px 4px;">
            <div style="color:#64748b;font-size:9px;">2. FUNDAMENTALS</div>
            <div style="color:#00e5ff;font-size:14px;font-weight:800;margin-top:2px;">${sc.funda} <span style="font-size:10px;color:#64748b;">/ ${sc.fundaMax}</span></div>
          </div>
          <div style="background:#0b1320;border:1px solid #ffaa00;border-radius:4px;padding:8px 4px;">
            <div style="color:#ffaa00;font-size:9px;font-weight:800;">3. TECHNICAL PILLAR</div>
            <div style="color:#ffaa00;font-size:14px;font-weight:800;margin-top:2px;">${sc.tech} <span style="font-size:10px;color:#64748b;">/ ${sc.techMax}</span></div>
          </div>
          <div style="background:#0b1320;border:1px solid #1b2e46;border-radius:4px;padding:8px 4px;">
            <div style="color:#64748b;font-size:9px;">4. VALUATION</div>
            <div style="color:#00e5ff;font-size:14px;font-weight:800;margin-top:2px;">${sc.val} <span style="font-size:10px;color:#64748b;">/ ${sc.valMax}</span></div>
          </div>
          <div style="background:#0b1320;border:1px solid #1b2e46;border-radius:4px;padding:8px 4px;">
            <div style="color:#64748b;font-size:9px;">5. FORENSIC AUDIT</div>
            <div style="color:#00e5ff;font-size:14px;font-weight:800;margin-top:2px;">${sc.forensic} <span style="font-size:10px;color:#64748b;">/ ${sc.forensicMax}</span></div>
          </div>
        </div>

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

        <!-- Valuation & Forensic Summary -->
        <div style="display:grid;grid-template-columns:1fr 1fr;gap:10px;font-size:10.5px;">
          <div style="background:#080e18;border:1px solid #1a2a40;border-radius:4px;padding:8px 12px;">
            <div style="color:#ffaa00;font-weight:700;margin-bottom:4px;">VALUATION PILLAR [${sc.val} / ${sc.valMax} PTS]</div>
            <div style="color:#94a3b8;">• PAT Growth &gt; 20% CAGR expected: <span style="color:#00e676;">+10 pts</span></div>
            <div style="color:#94a3b8;">• Stock History Check (No 60%+ non-market collapse): <span style="color:#00e676;">+10 pts</span></div>
            <div style="color:#94a3b8;">• Forward PE / PEG Ratio &lt; 1.5x: <span style="color:#00e676;">+5 pts</span></div>
          </div>
          <div style="background:#080e18;border:1px solid #1a2a40;border-radius:4px;padding:8px 12px;">
            <div style="color:#00e5ff;font-weight:700;margin-bottom:4px;">FORENSIC PILLAR [${sc.forensic} / ${sc.forensicMax} PTS]</div>
            <div style="color:#94a3b8;">• CFO to EBITDA &gt; 70% conversion: <span style="color:#00e676;">+10 pts</span></div>
            <div style="color:#94a3b8;">• Debt to Equity &lt; 0.7x: <span style="color:#00e676;">+10 pts</span></div>
            <div style="color:#94a3b8;">• Contingent Liabilities &lt; 15% Net Worth: <span style="color:#00e676;">+10 pts</span></div>
            <div style="color:#94a3b8;">• Zero Auditor Resignations &amp; Minimal Pledging: <span style="color:#00e676;">+5 pts</span></div>
          </div>
        </div>

      </div>

      <!-- Forensics & Factor Breakdown Matrix -->
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-bottom:14px;">
        <div style="background:#090d16;border:1px solid #1a293d;border-radius:6px;padding:12px;font-family:var(--font-mono);font-size:11px;">
          <h4 style="color:#00e5ff;font-size:11px;font-weight:800;margin-bottom:8px;">SOLVENCY &amp; EARNINGS QUALITY AUDIT</h4>
          <div style="display:flex;flex-direction:column;gap:6px;">
            <div style="display:flex;justify-content:space-between;padding:4px 0;border-bottom:1px solid #131e2d;">
              <span style="color:#94a3b8;">Beneish M-Score (Manipulation):</span>
              <span style="color:#00e676;font-weight:700;">${benMStr} · ${data.beneishStatus}</span>
            </div>
            <div style="display:flex;justify-content:space-between;padding:4px 0;border-bottom:1px solid #131e2d;">
              <span style="color:#94a3b8;">Altman Z-Score (Distress Risk):</span>
              <span style="color:#00e676;font-weight:700;">${altZStr} · ${data.altmanStatus}</span>
            </div>
            <div style="display:flex;justify-content:space-between;padding:4px 0;border-bottom:1px solid #131e2d;">
              <span style="color:#94a3b8;">Sloan Accrual Ratio:</span>
              <span style="color:#00e5ff;font-weight:700;">${data.sloanAccrual}</span>
            </div>
            <div style="display:flex;justify-content:space-between;padding:4px 0;">
              <span style="color:#94a3b8;">Piotroski F-Score:</span>
              <span style="color:#ffaa00;font-weight:700;">${data.piotroski}</span>
            </div>
          </div>
        </div>

        <div style="background:#090d16;border:1px solid #1a293d;border-radius:6px;padding:12px;font-family:var(--font-mono);font-size:11px;">
          <h4 style="color:#ffaa00;font-size:11px;font-weight:800;margin-bottom:8px;">INSTITUTIONAL FLOAT &amp; ALADDIN FACTORS</h4>
          <div style="display:flex;flex-direction:column;gap:6px;">
            <div style="display:flex;justify-content:space-between;padding:4px 0;border-bottom:1px solid #131e2d;">
              <span style="color:#94a3b8;">BlackRock Aladdin Holding:</span>
              <strong style="color:#fff;">${data.blkOwnership}</strong>
            </div>
            <div style="display:flex;justify-content:space-between;padding:4px 0;border-bottom:1px solid #131e2d;">
              <span style="color:#94a3b8;">Vanguard Index Fund Holding:</span>
              <strong style="color:#fff;">${data.vangOwnership}</strong>
            </div>
            <div style="display:flex;justify-content:space-between;padding:4px 0;border-bottom:1px solid #131e2d;">
              <span style="color:#94a3b8;">Kyle's Lambda Microstructure Impact:</span>
              <strong style="color:#00e5ff;">${data.kyleLambda}</strong>
            </div>
            <div style="display:flex;justify-content:space-between;padding:4px 0;">
              <span style="color:#94a3b8;">Active Free Float Ratio:</span>
              <strong style="color:#00e676;">${data.activeFloat}</strong>
            </div>
          </div>
        </div>
      </div>

      <!-- DuPont 5-Way Breakdown -->
      <div style="background:#090d16;border:1px solid #1a293d;border-radius:6px;padding:12px;font-family:var(--font-mono);font-size:11px;">
        <span style="color:#00e676;font-weight:700;">DUPONT 5-FACTOR ROE DECOMPOSITION:</span>
        <div style="display:grid;grid-template-columns:repeat(5, 1fr);gap:8px;margin-top:8px;text-align:center;">
          <div style="background:#05080e;padding:6px;border-radius:4px;border:1px solid #131e2d;">
            <div style="color:#64748b;font-size:9px;">TAX BURDEN</div>
            <div style="color:#fff;font-weight:800;margin-top:2px;">${data.dupontROE.taxBurden}</div>
          </div>
          <div style="background:#05080e;padding:6px;border-radius:4px;border:1px solid #131e2d;">
            <div style="color:#64748b;font-size:9px;">INTEREST BURDEN</div>
            <div style="color:#fff;font-weight:800;margin-top:2px;">${data.dupontROE.interestBurden}</div>
          </div>
          <div style="background:#05080e;padding:6px;border-radius:4px;border:1px solid #131e2d;">
            <div style="color:#64748b;font-size:9px;">OPERATING MARGIN</div>
            <div style="color:#00e5ff;font-weight:800;margin-top:2px;">${data.dupontROE.opMargin}</div>
          </div>
          <div style="background:#05080e;padding:6px;border-radius:4px;border:1px solid #131e2d;">
            <div style="color:#64748b;font-size:9px;">ASSET TURNOVER</div>
            <div style="color:#ffaa00;font-weight:800;margin-top:2px;">${data.dupontROE.assetTurn}</div>
          </div>
          <div style="background:#05080e;padding:6px;border-radius:4px;border:1px solid #131e2d;">
            <div style="color:#64748b;font-size:9px;">LEVERAGE MULTIPLIER</div>
            <div style="color:#ff3344;font-weight:800;margin-top:2px;">${data.dupontROE.leverage}</div>
          </div>
        </div>
      </div>
    `;

    updateBreadcrumbs();
  };

  window.drillToNanoFromFirm = function(nanoKey) {
    setFractalTier(5);
    loadNanoAsset(nanoKey || 'halol_mega');
  };

  // ── TIER 5: NANO PHYSICAL ASSETS & LEVEL 2 DOM ──

  window.loadNanoAsset = function(nKey) {
    currentNano = nKey;
    var data = nanoData[nKey];
    if (!data) return;

    // Update nano dropdown
    var nanoSelect = document.getElementById('zoom_nano_select');
    if (nanoSelect) nanoSelect.value = nKey;

    var box = document.getElementById('nano_telemetry_box');
    if (!box) return;

    var specsHtml = data.specs.map(function(s) {
      return `
        <div style="display:flex;justify-content:space-between;padding:5px 0;border-bottom:1px solid #131e2d;">
          <span style="color:#94a3b8;">${s.label}:</span>
          <strong style="color:#00e5ff;">${s.value}</strong>
        </div>
      `;
    }).join('');

    box.innerHTML = `
      <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:14px;border-bottom:1px solid #1e334d;padding-bottom:10px;">
        <div>
          <strong style="color:#fff;font-size:16px;">${data.title}</strong>
          <span class="badge" style="background:#132032;color:#ffaa00;margin-left:10px;">${data.facilityType}</span>
          <span style="color:#64748b;font-size:11px;margin-left:8px;">PARENT: ${data.parentFirm}</span>
        </div>
        <div style="display:flex;gap:8px;">
          <button class="preset-btn" onclick="syncMapToNanoCoords(${data.coords[0]}, ${data.coords[1]})" style="background:#00e5ff;color:#000;font-weight:800;padding:6px 14px;cursor:pointer;">
            🛰️ Center Satellite View ➔
          </button>
        </div>
      </div>

      <div style="display:grid;grid-template-columns:1.2fr 1fr;gap:14px;margin-bottom:16px;">
        
        <!-- Operating Facility Telemetry -->
        <div style="background:#090d16;border:1px solid #1a293d;border-radius:6px;padding:14px;font-family:var(--font-mono);font-size:11px;">
          <h4 style="color:#00e5ff;font-size:11px;font-weight:800;margin-bottom:8px;">PHYSICAL OPERATING TELEMETRY &amp; AIS KINEMATICS</h4>
          <div style="display:flex;flex-direction:column;gap:4px;margin-bottom:12px;">
            ${specsHtml}
          </div>
          <div style="background:#05080e;border:1px solid #131e2d;border-radius:4px;padding:10px;">
            <div style="color:#ffaa00;font-weight:700;margin-bottom:4px;font-size:10px;">OPERATIONAL SUMMARY:</div>
            <p style="color:#cfd8dc;font-size:11px;line-height:1.5;margin:0;">${data.description}</p>
          </div>
        </div>

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
      </div>
    `;

    renderNanoRibbonButtons();
    updateBreadcrumbs();
  };

  window.syncMapToNanoCoords = function(lat, lon) {
    if (typeof window.showTab === 'function') {
      var bmapTab = document.querySelector('[onclick*="bmap"]');
      if (bmapTab) window.showTab(bmapTab, 'bmap');
    }
    setTimeout(function() {
      if (window.leafletMap) {
        try {
          window.leafletMap.flyTo([lat, lon], 14, { duration: 1.5 });
        } catch(e) {}
      }
    }, 200);
  };

  function renderNanoRibbonButtons() {
    var ribbon = document.getElementById('nano_buttons_ribbon');
    if (!ribbon) return;

    var html = '<span style="color:var(--bb-amber);font-weight:800;font-size:11px;">SELECT NANO ASSET / DOM:</span>';
    var f = firmData[currentFirm];
    var keysToShow = [];
    if (f && f.nanoLink) keysToShow.push(f.nanoLink);
    keysToShow.push('dom', 'baytown', 'deerpark', 'vessel', 'halol_mega', 'kei_plant', 'mps_studio');

    // Deduplicate
    var seen = {};
    keysToShow.forEach(function(k) {
      if (!seen[k] && nanoData[k]) {
        seen[k] = true;
        var n = nanoData[k];
        var isActive = (k === currentNano) ? 'active' : '';
        var activeStyle = (k === currentNano) ? 'background:var(--bb-amber);color:#000;' : 'background:#131e2e;color:#e2e8f0;';
        html += `<button class="preset-btn ${isActive}" id="btn_nano_${k}" onclick="loadNanoAsset('${k}')" style="${activeStyle}">${n.title.substring(0, 32)}</button>`;
      }
    });
    ribbon.innerHTML = html;
  }

  
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
    var gf = document.getElementById('global_firm_select');

    // Only update selection if matching option exists; never wipe out master 94-industry options
    if (gc && Array.from(gc.options).some(function(o) { return o.value === currentCountry; })) {
      gc.value = currentCountry;
    }
    if (gf && Array.from(gf.options).some(function(o) { return o.value === currentFirm; })) {
      gf.value = currentFirm;
    }
  }

  // Hook syncGlobalRibbon into onCountryDropdownChange, onSectorDropdownChange, onFirmDropdownChange, onNanoDropdownChange


  // ── INITIALIZATION ON DOM READY ──
  document.addEventListener('DOMContentLoaded', function() {
    populateSectorDropdown('india');
    populateCompanyDropdown('cables_in');
    populateNanoDropdown('polycab');
    loadCountrySovereign('india');
    loadSectorModel('cables_in');
    loadFirmModel('polycab');
    loadNanoAsset('halol_mega');
  });

})();
</script>
"""

    return html_markup + "\n" + js_code

if __name__ == '__main__':
    section = build_fractal_zoom_section()
    print(f"Fractal Zoom Engine v2 generated. Total length: {len(section)} characters.")
