import pandas as pd
import json

tax_path = r"F:\documents\SOIC\Damodaran_Data\03_Industry_Taxonomy_Company_Lookup\indname.xlsx"
df_tax = pd.read_excel(tax_path)
print("Total rows:", len(df_tax))

# Clean records
records = []
for _, row in df_tax.iterrows():
    name = str(row['Company Name']).strip()
    ticker = str(row['Exchange:Ticker']).strip() if pd.notna(row['Exchange:Ticker']) else ''
    industry = str(row['Industry Group']).strip() if pd.notna(row['Industry Group']) else ''
    sector = str(row['Primary Sector']).strip() if pd.notna(row['Primary Sector']) else ''
    country = str(row['Country']).strip() if pd.notna(row['Country']) else ''
    region = str(row['Sub Group']).strip() if pd.notna(row['Sub Group']) else ''
    
    if name and name != 'nan':
        records.append({
            'n': name,
            't': ticker,
            'i': industry,
            's': sector,
            'c': country,
            'r': region
        })

print(f"Valid records: {len(records)}")
# Sample
print("Sample 3:", records[:3])

# Save as compact JSON
out_path = r"F:\documents\SOIC\EconAgent_Platform\platform_ui\global_company_directory.json"
with open(out_path, 'w', encoding='utf-8') as f:
    json.dump(records, f, ensure_ascii=False)

import os
print(f"File size: {os.path.getsize(out_path) / 1024 / 1024:.2f} MB")

