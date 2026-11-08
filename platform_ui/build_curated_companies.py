import pandas as pd
import json

tax_path = r"F:\documents\SOIC\Damodaran_Data\03_Industry_Taxonomy_Company_Lookup\indname.xlsx"
df = pd.read_excel(tax_path)

# Let's select key companies across all 94 industries and major exchanges (NYSE, Nasdaq, LSE, XETRA, TSE, SEHK, KOSDAQ, KRX, SGX, ASX, NSE, BSE, Tadawul, B3, SIX)
key_exchanges = ['NYSE', 'Nasdaq', 'LSE', 'XETRA', 'TSE', 'SEHK', 'ASX', 'NSE', 'BSE', 'ADX', 'DFM', 'SAU', 'SWX', 'B3', 'KRX']

# Sample top ~2,500 companies evenly across industries and countries
records = []
for ind, group in df.groupby('Industry Group'):
    # pick up to 30 top firms per industry
    sample = group.head(28)
    for _, row in sample.iterrows():
        name = str(row['Company Name']).strip()
        ticker = str(row['Exchange:Ticker']).strip() if pd.notna(row['Exchange:Ticker']) else ''
        industry = str(row['Industry Group']).strip() if pd.notna(row['Industry Group']) else ''
        sector = str(row['Primary Sector']).strip() if pd.notna(row['Primary Sector']) else ''
        country = str(row['Country']).strip() if pd.notna(row['Country']) else ''
        if name and name != 'nan':
            records.append([name, ticker, industry, country, sector])

print(f"Extracted {len(records)} representative global companies across {df['Industry Group'].nunique()} industries.")

out_p = r"F:\documents\SOIC\EconAgent_Platform\platform_ui\global_top_companies_curated.json"
with open(out_p, 'w', encoding='utf-8') as f:
    json.dump(records, f, ensure_ascii=False)

import os
print(f"Curated JSON size: {os.path.getsize(out_p) / 1024:.2f} KB")

