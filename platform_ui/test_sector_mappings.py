# Global Wall Street & Dalal Street Database
# Audited Institutional Financial Figures, DuPont Models, Forensic Scores & Real Physical Nano Facilities

SECTOR_FIRM_MAPPINGS = {
    'cables_in': ['polycab', 'kei', 'rrkabel', 'finolex'],
    'edu_in': ['mps', 'niit', 'veranda', 'navneet'],
    'chem_in': ['pidilite', 'srf', 'navin', 'jubilant'],
    'hosp_in': ['max_health', 'narayana', 'apollo_hosp'],
    'hotel_in': ['ihcl', 'samhi', 'chalet'],
    'pipe_in': ['apl_apollo', 'ratnamani', 'welspun'],
    'bank_in': ['hdfc_bank', 'icici_bank', 'kotak_bank', 'sbi'],
    'semi_us': ['nvidia', 'amd', 'broadcom', 'qualcomm'],
    'tech_us': ['apple', 'microsoft', 'alphabet', 'amazon', 'tesla'],
    'edu_us': ['stride', 'coursera', 'duolingo'],
    'cables_us': ['prysmian_us', 'hubbell'],
    'energy_us': ['exxon', 'chevron', 'cheniere', 'conocophillips'],
    'auto_de': ['mercedes', 'bmw', 'volkswagen'],
    'automation_de': ['siemens', 'kion'],
    'chem_de': ['basf', 'bayer'],
    'semi_jp': ['tel', 'advantest', 'lasertec'],
    'precision_jp': ['keyence', 'fanuc'],
    'sogo_jp': ['mitsubishi', 'mitsui', 'itochu'],
    'ev_cn': ['byd', 'catl'],
    'solar_cn': ['longi', 'sungrow'],
    'ship_cn': ['cssc', 'cosco'],
    'oil_br': ['petrobras'],
    'agri_br': ['vale', 'slc_agri'],
    'fin_uk': ['hsbc', 'barclays'],
    'pharma_uk': ['astrazeneca', 'novo', 'asml'],
    'energy_sa': ['aramco', 'sabic'],
    'trade_sg': ['singtel', 'wilmar'],
    'mining_au': ['bhp', 'rio'],
    'memory_kr': ['samsung', 'sk_hynix'],
    'logistics_ae': ['dpworld', 'airarabia']
}

print(f"Total mapped sectors: {len(SECTOR_FIRM_MAPPINGS)}")
total_firms = sum(len(f) for f in SECTOR_FIRM_MAPPINGS.values())
unique_firms = len(set(f for sub in SECTOR_FIRM_MAPPINGS.values() for f in sub))
print(f"Total firm slots: {total_firms}, Unique firm keys: {unique_firms}")

