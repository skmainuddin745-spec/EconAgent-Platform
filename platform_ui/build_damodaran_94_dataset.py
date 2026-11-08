import os
import pandas as pd
import json

base_dir = r"F:\documents\SOIC\Damodaran_Data\01_Current_Data_by_Category"
tax_path = r"F:\documents\SOIC\Damodaran_Data\03_Industry_Taxonomy_Company_Lookup\indname.xlsx"

def get_clean_industry_table(file_path):
    xl = pd.ExcelFile(file_path)
    sname = 'Industry Averages' if 'Industry Averages' in xl.sheet_names else xl.sheet_names[0]
    df = pd.read_excel(file_path, sheet_name=sname)
    h_row = None
    for r in range(min(25, len(df))):
        for cell in df.iloc[r]:
            if str(cell).strip().lower() == 'industry name':
                h_row = r
                break
        if h_row is not None:
            break
    if h_row is None:
        return None
    headers = [str(c).strip() for c in df.iloc[h_row].tolist()]
    res = df.iloc[h_row+1:].copy()
    res.columns = headers
    res = res.dropna(subset=[headers[0]])
    res = res[~res[headers[0]].astype(str).str.contains('Total|Average|Date updated|Notes', case=False, na=False)]
    return res

# 1. Load WACC
wacc_df = get_clean_industry_table(os.path.join(base_dir, "03_Cost_of_Capital", "waccGlobal.xls"))
# 2. Load Beta
beta_df = get_clean_industry_table(os.path.join(base_dir, "02_Risk_and_Discount_Rates", "betaGlobal.xls"))
# 3. Load Margin
margin_df = get_clean_industry_table(os.path.join(base_dir, "10_Margins_and_Profitability", "marginGlobal.xls"))
# 4. Load VEBITDA
vebitda_df = get_clean_industry_table(os.path.join(base_dir, "14_Valuation_Multiples", "vebitdaGlobal.xls"))
# 5. Load EVA
eva_df = get_clean_industry_table(os.path.join(base_dir, "05_Return_on_Capital_and_EVA", "EVAGlobal.xls"))

# 6. Load Taxonomy to map Industry Group to GICS Primary Sector
df_tax = pd.read_excel(tax_path)
ind_to_sector = {}
for _, row in df_tax.dropna(subset=['Industry Group', 'Primary Sector']).iterrows():
    ig = str(row['Industry Group']).strip()
    ps = str(row['Primary Sector']).strip()
    if ig not in ind_to_sector:
        ind_to_sector[ig] = ps

# Map industry names to Damodaran 94 list
industries_data = []

# Famous titan stocks mapped to industries
TITAN_MAPPINGS = {
    'Semiconductor': ['NVDA:US (NVIDIA)', 'TSM:US (TSMC)', 'ASML:NA (ASML)', '005930:KS (Samsung)'],
    'Semiconductor Equip': ['ASML:NA (ASML)', 'AMAT:US (Applied Materials)', 'LRCX:US (Lam Research)', '8035:JP (Tokyo Electron)'],
    'Software (System & Application)': ['MSFT:US (Microsoft)', 'ORCL:US (Oracle)', 'SAP:GY (SAP)', 'CRM:US (Salesforce)'],
    'Computers/Peripherals': ['AAPL:US (Apple)', 'DELL:US (Dell)', 'HPQ:US (HP)'],
    'Information Services': ['GOOGL:US (Alphabet)', 'META:US (Meta)', 'BABA:US (Alibaba)', 'TCEHY:US (Tencent)'],
    'Oil/Gas (Integrated)': ['2222:SR (Saudi Aramco)', 'XOM:US (ExxonMobil)', 'CVX:US (Chevron)', 'SHEL:LN (Shell)', 'TTE:FP (TotalEnergies)'],
    'Oil/Gas (Production and Exploration)': ['COP:US (ConocoPhillips)', 'EOG:US (EOG Resources)', 'OXY:US (Occidental)'],
    'Metals & Mining': ['BHP:AU (BHP Group)', 'RIO:LN (Rio Tinto)', 'VALE:BR (Vale)', 'FCX:US (Freeport-McMoRan)'],
    'Steel': ['APLAPOLLO:IN (APL Apollo)', 'NUE:US (Nucor)', '5401:JP (Nippon Steel)', 'TATASTEEL:IN (Tata Steel)'],
    'Auto & Truck': ['TSLA:US (Tesla)', '7203:JP (Toyota)', '1211:HK (BYD)', 'VOW3:GY (Volkswagen)', 'RACE:US (Ferrari)'],
    'Bank (Money Center)': ['JPM:US (JPMorgan Chase)', 'BAC:US (Bank of America)', 'C:US (Citigroup)', 'HSBA:LN (HSBC)'],
    'Banks (Regional)': ['HDFCBANK:IN (HDFC Bank)', 'ICICIBANK:IN (ICICI Bank)', 'D05:SG (DBS Bank)', '8306:JP (Mitsubishi UFJ)'],
    'Drugs (Pharmaceutical)': ['LLY:US (Eli Lilly)', 'NOVO:DC (Novo Nordisk)', 'PFE:US (Pfizer)', 'ROG:SW (Roche)', 'SUNPHARMA:IN (Sun Pharma)'],
    'Healthcare Products': ['JNJ:US (Johnson & Johnson)', 'ABT:US (Abbott)', 'MDT:US (Medtronic)'],
    'Hospitals/Healthcare Facilities': ['NH:IN (Narayana Hrudayalaya)', 'HCA:US (HCA Healthcare)', 'MAXHEALTH:IN (Max Healthcare)'],
    'Electrical Equipment': ['POLYCAB:IN (Polycab)', 'KEI:IN (KEI Industries)', 'SIE:GY (Siemens AG)', 'SU:FP (Schneider Electric)', 'PRY:IM (Prysmian)'],
    'Chemical (Specialty)': ['PIDILITIND:IN (Pidilite)', 'BAS:GY (BASF)', 'LIN:US (Linde)', '4063:JP (Shin-Etsu Chemical)'],
    'Retail (General)': ['WMT:US (Walmart)', 'COST:US (Costco)', 'TGT:US (Target)', 'TRENT:IN (Trent)'],
    'Apparel': ['MC:FP (LVMH)', 'RMS:FP (Hermes)', 'NKE:US (Nike)', 'INDITEX:MC (Inditex/Zara)'],
    'Aerospace/Defense': ['LMT:US (Lockheed Martin)', 'RTX:US (RTX)', 'BA:US (Boeing)', 'AIR:FP (Airbus)', 'RHM:GY (Rheinmetall)'],
    'Telecom (Wireless)': ['T:US (AT&T)', 'VZ:US (Verizon)', 'BHARTIARTL:IN (Bharti Airtel)', '9432:JP (NTT)'],
    'Power': ['NEE:US (NextEra Energy)', 'SO:US (Southern Co)', 'NTPC:IN (NTPC)', 'IBE:MC (Iberdrola)']
}

# Sector fallback mapping
SECTOR_MAP = {
    'Advertising': 'Communication Services', 'Aerospace/Defense': 'Industrials', 'Air Transport': 'Industrials',
    'Apparel': 'Consumer Discretionary', 'Auto & Truck': 'Consumer Discretionary', 'Auto Parts': 'Consumer Discretionary',
    'Bank (Money Center)': 'Financials', 'Banks (Regional)': 'Financials', 'Beverage (Alcoholic)': 'Consumer Staples',
    'Beverage (Soft)': 'Consumer Staples', 'Broadcasting': 'Communication Services', 'Brokerage & Investment Banking': 'Financials',
    'Building Materials': 'Industrials', 'Business & Consumer Services': 'Industrials', 'Cable TV': 'Communication Services',
    'Chemical (Basic)': 'Materials', 'Chemical (Diversified)': 'Materials', 'Chemical (Specialty)': 'Materials',
    'Coal & Related Energy': 'Energy', 'Commercial Services': 'Industrials', 'Computer Services': 'Information Technology',
    'Computers/Peripherals': 'Information Technology', 'Construction Supplies': 'Industrials', 'Diversified': 'Industrials',
    'Drugs (Biotechnology)': 'Health Care', 'Drugs (Pharmaceutical)': 'Health Care', 'Education': 'Consumer Discretionary',
    'Electrical Equipment': 'Industrials', 'Electronics (Consumer & Office)': 'Consumer Discretionary',
    'Electronics (General)': 'Information Technology', 'Engineering/Construction': 'Industrials',
    'Entertainment': 'Communication Services', 'Environmental & Waste Services': 'Industrials',
    'Farming/Agriculture': 'Consumer Staples', 'Financial Svcs. (Non-bank & Insurance)': 'Financials',
    'Food Processing': 'Consumer Staples', 'Food Wholesalers': 'Consumer Staples', 'Furnishings': 'Consumer Discretionary',
    'Green & Renewable Energy': 'Utilities', 'Healthcare Products': 'Health Care', 'Healthcare Support Services': 'Health Care',
    'Heathcare Information and Technology': 'Health Care', 'Homebuilding': 'Consumer Discretionary',
    'Hospitals/Healthcare Facilities': 'Health Care', 'Hotel/Gaming': 'Consumer Discretionary',
    'Household Products': 'Consumer Staples', 'Information Services': 'Communication Services',
    'Insurance (General)': 'Financials', 'Insurance (Life)': 'Financials', 'Insurance (Prop/Cas.)': 'Financials',
    'Investments & Asset Management': 'Financials', 'Machinery': 'Industrials', 'Manufacturing (Foundry)': 'Industrials',
    'Marine Transportation': 'Industrials', 'Metals & Mining': 'Materials', 'Office Equipment & Supplies': 'Industrials',
    'Oil/Gas (Integrated)': 'Energy', 'Oil/Gas (Production and Exploration)': 'Energy',
    'Oil/Gas Distribution': 'Utilities', 'Oilfield Svcs/Equip.': 'Energy', 'Packaging & Container': 'Materials',
    'Paper/Forest Products': 'Materials', 'Power': 'Utilities', 'Precious Metals': 'Materials',
    'Publishing & Information': 'Communication Services', 'R.E.I.T.': 'Real Estate', 'Real Estate (Development)': 'Real Estate',
    'Real Estate (General/Diversified)': 'Real Estate', 'Real Estate (Operations & Services)': 'Real Estate',
    'Recreation': 'Consumer Discretionary', 'Reinsurance': 'Financials', 'Restaurant/Dining': 'Consumer Discretionary',
    'Retail (Automotive)': 'Consumer Discretionary', 'Retail (Building Supply)': 'Consumer Discretionary',
    'Retail (Distributors)': 'Consumer Discretionary', 'Retail (General)': 'Consumer Discretionary',
    'Retail (Grocery and Food)': 'Consumer Staples', 'Retail (Online)': 'Consumer Discretionary',
    'Retail (Special Lines)': 'Consumer Discretionary', 'Rubber& Tires': 'Consumer Discretionary',
    'Semiconductor': 'Information Technology', 'Semiconductor Equip': 'Information Technology',
    'Shipbuilding': 'Industrials', 'Software (Entertainment)': 'Communication Services',
    'Software (Internet)': 'Information Technology', 'Software (System & Application)': 'Information Technology',
    'Steel': 'Materials', 'Telecom (Wireless)': 'Communication Services', 'Telecom. Equipment': 'Information Technology',
    'Telecom. Services': 'Communication Services', 'Tobacco': 'Consumer Staples', 'Transportation': 'Industrials',
    'Transportation (Railroads)': 'Industrials', 'Trucking': 'Industrials', 'Utility (General)': 'Utilities',
    'Utility (Water)': 'Utilities'
}

# Index by industry name
wacc_dict = {str(row['Industry Name']).strip(): row for _, row in wacc_df.iterrows()} if wacc_df is not None else {}
beta_dict = {str(row['Industry Name']).strip(): row for _, row in beta_df.iterrows()} if beta_df is not None else {}
margin_dict = {str(row['Industry Name']).strip(): row for _, row in margin_df.iterrows()} if margin_df is not None else {}
vebitda_dict = {str(row['Industry Name']).strip(): row for _, row in vebitda_df.iterrows()} if vebitda_df is not None else {}
eva_dict = {str(row['Industry Name']).strip(): row for _, row in eva_df.iterrows()} if eva_df is not None else {}

all_industry_names = sorted(list(wacc_dict.keys()))

print(f"Total Unique Damodaran Industries: {len(all_industry_names)}")

for ind in all_industry_names:
    w_row = wacc_dict.get(ind, {})
    b_row = beta_dict.get(ind, {})
    m_row = margin_dict.get(ind, {})
    v_row = vebitda_dict.get(ind, {})
    e_row = eva_dict.get(ind, {})
    
    n_firms = int(w_row.get('Number of Firms', 0) or b_row.get('Number of firms', 0) or 0)
    beta = float(w_row.get('Beta', 1.0) or b_row.get('Beta', 1.0) or 1.0)
    unlev_beta = float(b_row.get('Unlevered beta', 0.8) or 0.8)
    cost_equity = float(w_row.get('Cost of Equity', 0.09) or 0.09)
    cost_debt = float(w_row.get('After-tax Cost of Debt', 0.04) or 0.04)
    wacc = float(w_row.get('Cost of Capital', 0.08) or 0.08)
    
    gross_margin = float(m_row.get('Gross Margin', 0.3) or 0.3)
    net_margin = float(m_row.get('Net Margin', 0.06) or 0.06)
    ebit_margin = float(m_row.get('Pre-tax Unadjusted Operating Margin', 0.12) or 0.12)
    
    # EV/EBITDA
    ev_ebitda = v_row.get('EV/EBITDA')
    if isinstance(ev_ebitda, pd.Series):
        ev_ebitda = ev_ebitda.iloc[0]
    ev_ebitda = float(ev_ebitda or 12.5) if pd.notna(ev_ebitda) else 12.5
    
    # ROC / EVA
    roc = float(e_row.get('ROC', 0.11) or 0.11) if pd.notna(e_row.get('ROC')) else 0.11
    eva_spread = float(e_row.get('(ROC - WACC)', roc - wacc) or (roc - wacc)) if pd.notna(e_row.get('(ROC - WACC)')) else (roc - wacc)
    
    sector = SECTOR_MAP.get(ind, ind_to_sector.get(ind, 'Industrials'))
    titans = TITAN_MAPPINGS.get(ind, [])
    
    industries_data.append({
        'name': ind,
        'sector': sector,
        'firms': n_firms,
        'beta': round(beta, 2),
        'unleveredBeta': round(unlev_beta, 2),
        'costEquityPct': round(cost_equity * 100, 2),
        'costDebtPct': round(cost_debt * 100, 2),
        'waccPct': round(wacc * 100, 2),
        'grossMarginPct': round(gross_margin * 100, 2),
        'ebitMarginPct': round(ebit_margin * 100, 2),
        'netMarginPct': round(net_margin * 100, 2),
        'evEbitda': round(ev_ebitda, 1),
        'rocPct': round(roc * 100, 2),
        'evaSpreadPct': round(eva_spread * 100, 2),
        'titans': titans
    })

print(f"Compiled {len(industries_data)} global industry records.")
print("Sample record:", json.dumps(industries_data[0], indent=2))

out_path = r"F:\documents\SOIC\EconAgent_Platform\platform_ui\damodaran_94_global_industries.json"
with open(out_path, 'w', encoding='utf-8') as f:
    json.dump(industries_data, f, indent=2, ensure_ascii=False)
print("Saved to", out_path)

