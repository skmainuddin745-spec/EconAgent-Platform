import sys
sys.path.append('F:/documents/SOIC/EconAgent_Platform/platform_ui')
import generate_dashboard

analysis  = generate_dashboard.load_analysis()
manifest  = generate_dashboard.load_manifest()
papers    = generate_dashboard.load_papers()
by_agent  = analysis.get("by_agent", {})

sections = [
    ("erp", lambda: generate_dashboard.build_erp_section(by_agent)),
    ("beta", lambda: generate_dashboard.build_beta_section(by_agent)),
    ("margins", lambda: generate_dashboard.build_margins_section(by_agent)),
    ("multiples", lambda: generate_dashboard.build_multiples_section(by_agent)),
    ("growth", lambda: generate_dashboard.build_growth_section(by_agent)),
    ("capstruct", lambda: generate_dashboard.build_capstruct_section(by_agent)),
    ("wacc_div", lambda: generate_dashboard.build_wacc_dividend_section(by_agent)),
    ("workcap", lambda: generate_dashboard.build_workcap_section(by_agent)),
    ("taxrate", lambda: generate_dashboard.build_taxrate_section(by_agent)),
    ("fundamentals", lambda: generate_dashboard.build_fundamentals_section(by_agent)),
    ("agents", lambda: generate_dashboard.build_agents_section(by_agent)),
    ("papers", lambda: generate_dashboard.build_papers_section(papers)),
    ("arch", lambda: generate_dashboard.build_architecture_section()),
    ("bmap_tanker", lambda: generate_dashboard.build_bmap_tanker_section()),
    ("soic_sector_models", lambda: generate_dashboard.build_soic_sector_models_section()),
    ("institutional_giants", lambda: generate_dashboard.build_institutional_giants_section(by_agent)),
    ("topnotch_frameworks", lambda: generate_dashboard.build_topnotch_frameworks_section()),
    ("fractal_zoom", lambda: generate_dashboard.build_fractal_zoom_section(by_agent)),
    ("realtime_technicals", lambda: generate_dashboard.build_realtime_technicals_section()),
]

for name, fn in sections:
    try:
        val = fn()
        val.encode('utf-8')
        print(f"Section {name}: CLEAN ({len(val)} chars)")
    except UnicodeEncodeError as e:
        print(f"Section {name}: HAS SURROGATE! {e}")
        surrogates = [(i, c, hex(ord(c))) for i, c in enumerate(val) if 0xD800 <= ord(c) <= 0xDFFF]
        print(f"  Surrogates: {surrogates[:5]}")
        pos = surrogates[0][0]
        print("  Context around surrogate:", repr(val[max(0, pos-40):pos+40]))
