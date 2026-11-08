# EconAgent Platform: Agent Taxonomy & Mathematical Specifications

> **System ID:** `ECON-AGENT-SPEC-V2`  
> **Platform Version:** EconAgent Terminal Platform v2.1.0  
> **Author:** Sk. Mainuddin ([sk.mainuddin745@gmail.com](mailto:sk.mainuddin745@gmail.com))  
> **Verification:** 18 Specialized Agents · 251 Derived Empirical Results  

---

## 1. Mathematical Taxonomy & Specifications

This document defines the mathematical models, tabular data sources, aggregation algorithms, confidence scoring, and sanity-bounding corridors for all 18 economic analysis agents.

```
┌──────────────────────────────────────────────────────────────────────────────────┐
│                             AGENT DOMAIN TAXONOMY                                │
├───────────────────────┬──────────────────────────┬───────────────────────────────┤
│ Macroeconomic Risk    │ Micro Fundamentals       │ Strategic & Structural        │
│ ──────────────────    │ ──────────────────       │ ──────────────────────        │
│ 01. ERPAnalysisAgent  │ 03. MarginsAgent         │ 13. CorporateGovernanceAgent  │
│ 02. BetaAnalysisAgent │ 04. ValuationMultiples   │ 14. IntangiblesGoodwillAgent  │
│ 07. CostOfCapitalWACC │ 05. GrowthRateAgent      │ 15. OptionVolatilityAgent     │
│ 10. TaxRateAgent      │ 06. CapitalStructure     │ 16. FinancingFlowsAgent       │
│                       │ 08. DividendPayoutAgent  │ 17. SOICTechnicalRanking      │
│                       │ 09. WorkingCapitalAgent  │ 18. OilTankerCommodityAgent   │
│                       │ 11. CapexReinvestment    │                               │
│                       │ 12. EconomicValueAdded   │                               │
└───────────────────────┴──────────────────────────┴───────────────────────────────┘
```

---

### Agent 01: ERPAnalysisAgent (`MACRO_ERP`)
- **Primary Source:** `ctrypremJuly26.xlsx`, `histimpl.xls`
- **Theoretical Basis:** Implied forward-looking Equity Risk Premium via multi-stage DCF on market index cash distributions.
- **Mathematical Formulation:**
  $$\text{Index}_0 = \sum_{t=1}^5 \frac{\text{CF}_t}{(1 + r)^t} + \frac{\text{CF}_5 (1 + g)}{(r - g)(1 + r)^5}, \quad \text{ERP} = r - R_f$$
  $$\text{Country ERP} = \text{Mature ERP} + \text{CDS Spread} \times \left(\frac{\sigma_{\text{Equity}}}{\sigma_{\text{Bonds}}}\right)$$
- **Sanity Bounds:** $0.001 \le \text{ERP} \le 0.300$ ($0.1\%$ to $30.0\%$)
- **Empirical Outputs:**
  - US Implied ERP: **4.40 %** (Confidence: `HIGH`)
  - Global Implied ERP Median: **7.17 %** ($n=205$ sovereign entities)

---

### Agent 02: BetaAnalysisAgent (`MICRO_BETA`)
- **Primary Source:** `betas.xls`, `totalbeta.xls` across 8 global regions.
- **Theoretical Basis:** CAPM Systematic Risk & Total Risk decomposed via the Hamada Equation.
- **Mathematical Formulation:**
  $$\beta_L = \beta_U \left[ 1 + (1 - T) \frac{D}{E} \right]$$
  $$\text{Total Beta} = \frac{\sigma_{\text{asset}}}{\sigma_{\text{market}}} = \frac{\beta_{\text{market}}}{\rho_{\text{asset, market}}}$$
- **Sanity Bounds:** $0.0 \le \beta \le 5.0$
- **Empirical Outputs:** 8 Regional systematic beta vectors. Global median unlevered $\beta_U = 0.94$, levered $\beta_L = 1.12$.

---

### Agent 03: MarginsAgent (`MICRO_MARGINS`)
- **Primary Source:** `margin.xls` across 8 geographic regions.
- **Theoretical Basis:** Dupont Profitability decomposition across operating layers.
- **Mathematical Formulation:**
  $$\text{Gross Margin} = \frac{\text{Revenues} - \text{COGS}}{\text{Revenues}}$$
  $$\text{EBITDA Margin} = \frac{\text{Operating Income} + \text{D\&A}}{\text{Revenues}}$$
  $$\text{Net Profit Margin} = \frac{\text{Net Income}}{\text{Revenues}}$$
- **Sanity Bounds:** $-1.00 \le \text{Margin} \le 1.00$ ($-100\%$ to $+100\%$)
- **Empirical Outputs:** 32 granular results (4 margin tiers $\times$ 8 global regions).

---

### Agent 04: ValuationMultiplesAgent (`MICRO_MULTIPLES`)
- **Primary Source:** `pedata.xls`, `pbvdata.xls`, `vebitda.xls`, `psdata.xls`
- **Theoretical Basis:** Relative valuation distribution across industry cross-sections.
- **Mathematical Formulation:**
  $$\frac{P}{E} = \frac{P_0}{\text{EPS}_1} = \frac{\text{Payout} (1 + g)}{r - g}$$
  $$\frac{\text{EV}}{\text{EBITDA}} = \frac{\text{Market Equity} + \text{Debt} + \text{Preferred} - \text{Cash}}{\text{EBITDA}}$$
  $$\frac{P}{B} = \frac{\text{ROE} - g}{r - g}$$
- **Sanity Bounds:** $0.0 \le \text{Multiple} \le 500.0$
- **Empirical Outputs:** 24 regional multiple benchmarks.

---

### Agent 05: GrowthRateAgent (`MICRO_GROWTH`)
- **Primary Source:** `fundgr.xls`, `histgr.xls`
- **Theoretical Basis:** Fundamental reinvestment equation vs historical growth.
- **Mathematical Formulation:**
  $$g_{\text{fundamental}} = \text{Retention Ratio} (b) \times \text{ROE} = (1 - \text{Payout}) \times \text{ROE}$$
  $$g_{\text{operating}} = \text{Reinvestment Rate} \times \text{ROIC}$$
- **Sanity Bounds:** $-0.50 \le g \le 1.00$ ($-50\%$ to $+100\%$)
- **Empirical Outputs:** 11 metrics tracking positive vs negative fundamental growth across global regions.

---

### Agent 06: CapitalStructureAgent (`MICRO_CAPSTRUCT`)
- **Primary Source:** `dbtfund.xls`
- **Theoretical Basis:** Capital structure leverage distribution and debt tolerance.
- **Mathematical Formulation:**
  $$\text{Debt-to-Equity} = \frac{\text{Total Debt}}{\text{Market Equity}}, \quad \text{Debt-to-Capital} = \frac{D}{D + E}$$
- **Sanity Bounds:** $0.0 \le \frac{D}{E} \le 10.0$
- **Empirical Outputs:** 6 regional leverage distributions.

---

### Agent 07: CostOfCapitalAgent (`MACRO_WACC`)
- **Primary Source:** `wacc.xls`
- **Theoretical Basis:** Enterprise hurdle rate under market value weighting.
- **Mathematical Formulation:**
  $$\text{WACC} = \left(\frac{E}{V}\right) [R_f + \beta_L (\text{ERP})] + \left(\frac{D}{V}\right) K_d (1 - T)$$
- **Sanity Bounds:** $0.001 \le \text{WACC} \le 0.500$ ($0.1\%$ to $50.0\%$)
- **Empirical Outputs:** 8 Regional WACC medians and hurdle distributions.

---

### Agent 08: DividendPayoutAgent (`MICRO_DIVIDEND`)
- **Primary Source:** `divfund.xls`
- **Theoretical Basis:** Cash dividend yield and net dividend coverage.
- **Mathematical Formulation:**
  $$\text{Payout Ratio} = \frac{\text{Dividends}}{\text{Net Income}}, \quad \text{Dividend Yield} = \frac{\text{Dividends per Share}}{\text{Price}}$$
- **Sanity Bounds:** $0.00 \le \text{Payout} \le 5.00$
- **Empirical Outputs:** 20 granular payout and yield metrics across 8 economies.

---

### Agent 09: WorkingCapitalAgent (`MICRO_WORKCAP`)
- **Primary Source:** `wcdata.xls`
- **Theoretical Basis:** Operating cash cycle and working capital efficiency.
- **Mathematical Formulation:**
  $$\text{Cash Conversion Cycle} = \text{DIO} + \text{DSO} - \text{DPO}$$
  $$\text{Non-Cash WC / Sales} = \frac{(\text{Current Assets} - \text{Cash}) - (\text{Current Liabilities} - \text{Short Debt})}{\text{Revenues}}$$
- **Sanity Bounds:** $-0.50 \le \frac{\text{NCWC}}{\text{Sales}} \le 1.00$
- **Empirical Outputs:** 32 operational working capital metrics.

---

### Agent 10: TaxRateAgent (`MICRO_TAXRATE`)
- **Primary Source:** `taxrate.xls`
- **Theoretical Basis:** Marginal statutory rate vs effective cash tax rate wedge.
- **Mathematical Formulation:**
  $$\text{Effective Tax Rate} = \frac{\text{Taxes Paid / Accrued}}{\text{Taxable Income}}$$
- **Sanity Bounds:** $0.00 \le T_c \le 0.60$
- **Empirical Outputs:** 16 regional statutory and cash tax rates.

---

### Agent 11: CapexReinvestmentAgent (`MICRO_CAPEX`)
- **Primary Source:** `capex.xls`
- **Theoretical Basis:** Expansionary vs maintenance reinvestment ratio.
- **Mathematical Formulation:**
  $$\text{CapEx / Depreciation} = \frac{\text{Capital Expenditures}}{\text{Depreciation \& Amortization}}$$
  $$\text{Ratio} > 1.0 \implies \text{Expansionary Asset Growth}$$
- **Sanity Bounds:** $0.0 \le \frac{\text{CapEx}}{\text{Depr}} \le 10.0$
- **Empirical Outputs:** 8 Regional CapEx intensity indices.

---

### Agent 12: EconomicValueAddedAgent (`MICRO_EVA`)
- **Primary Source:** `eva.xls`
- **Theoretical Basis:** Stern Stewart residual income and economic moat strength.
- **Mathematical Formulation:**
  $$\text{Excess Equity Spread} = \text{ROE} - K_e$$
  $$\text{EVA} = \text{Invested Capital} \times (\text{ROIC} - \text{WACC})$$
- **Sanity Bounds:** $-1.00 \le \text{Spread} \le 1.00$
- **Empirical Outputs:** 8 Regional economic excess return distributions.

---

### Agent 13: CorporateGovernanceAgent (`MICRO_GOVERNANCE`)
- **Primary Source:** `corpgov.xls`
- **Theoretical Basis:** Agency cost mitigation and ownership concentration.
- **Mathematical Formulation:**
  $$\text{Insider Concentration} = \sum_{i \in \text{Insiders}} w_i, \quad \text{Institutional Float} = \sum_{j \in \text{Inst}} w_j$$
- **Sanity Bounds:** $0.0 \le \text{Ownership} \le 100.0\%$
- **Empirical Outputs:** 24 governance metrics across global exchanges.

---

### Agent 14: IntangiblesGoodwillAgent (`MICRO_INTANGIBLES`)
- **Primary Source:** `goodwill.xls`
- **Theoretical Basis:** Balance-sheet quality, goodwill asset drag, and impairment risk.
- **Mathematical Formulation:**
  $$\text{Goodwill Drag} = \frac{\text{Goodwill}}{\text{Total Assets}}, \quad \text{Impairment Rate} = \frac{\text{Goodwill Impairment Charge}}{\text{Goodwill}_{t-1}}$$
- **Sanity Bounds:** $0.0 \le \frac{\text{Goodwill}}{\text{Assets}} \le 1.0$
- **Empirical Outputs:** 16 regional goodwill and intangibles metrics.

---

### Agent 15: OptionVolatilityAgent (`MICRO_VOLAT`)
- **Primary Source:** `optvar.xls`
- **Theoretical Basis:** Merton Structural Default Model and unobservable asset volatility inversion.
- **Mathematical Formulation:**
  $$V_E = V_A \mathcal{N}(d_1) - D e^{-rT} \mathcal{N}(d_2)$$
  $$\sigma_E = \left(\frac{V_A}{V_E}\right) \mathcal{N}(d_1) \sigma_A$$
- **Sanity Bounds:** $0.01 \le \sigma \le 5.00$ ($1\%$ to $500\%$)
- **Empirical Outputs:** 16 Equity and Asset Volatility parameters.

---

### Agent 16: FinancingFlowsAgent (`MICRO_FINFLOWS`)
- **Primary Source:** `finflow.xls`
- **Theoretical Basis:** Net primary financing flows, equity buybacks, and debt issuance.
- **Mathematical Formulation:**
  $$\text{Net Debt Capital Expansion} = \frac{\text{New Debt Issued} - \text{Debt Retired}}{\text{Total Capital}}$$
- **Sanity Bounds:** $-1.0 \times 10^{12} \le \text{Flow} \le 1.0 \times 10^{12}$
- **Empirical Outputs:** 16 metrics capturing global corporate capital returns and debt deleveraging cycles.

---

### Agent 17: SOICTechnicalRankingAgent (`SOIC_TECH_RANKING`)
- **Primary Source:** `SOIC Ranking Sheet.xlsx`, `Nifty & Indices Valuations.xlsx`
- **Theoretical Basis:** 310-Point Scorecard and Sectoral Rotation Momentum.
- **Mathematical Formulation:**
  $$\text{Score}_{310} = S_{\text{Ind}} (45) + S_{\text{Fund}} (80) + S_{\text{Tech}} (110) + S_{\text{Val}} (35) + S_{\text{Forensic}} (40)$$
- **Sanity Bounds:** $0.0 \le \text{Score} \le 310.0$
- **Empirical Outputs:** Institutional leaderboard and sectoral rotation percentiles across 9 index benchmarks.

---

### Agent 18: OilTankerCommodityAgent (`COMMODITY_TANKER_FLOWS`)
- **Primary Source:** `commodity.pdf`, AIS Vector Kinematics Telemetry.
- **Theoretical Basis:** Commodity price shock propagation and maritime transit delay modeling.
- **Mathematical Formulation:**
  $$\Delta \text{COGS} = \sum_k w_k \Delta P_k, \quad \Delta \text{Margin} = - w_{\text{crude}} \left(\frac{\Delta P_{\text{crude}}}{P_{\text{crude}}}\right) (1 - \text{PassThrough})$$
- **Sanity Bounds:** $0.0 \le \text{Volume} \le 100.0 \text{ Mbd}$
- **Empirical Outputs:** Global chokepoint telemetry and corporate DCF margin sensitivity vectors.

