with open(r'platform_ui\bmap_html_template.html', 'r', encoding='utf-8', errors='ignore') as f:
    for i, line in enumerate(f):
        if any(w in line for w in ['Bank Branches', 'Pipelines (N.Am.)', 'Natural Gas', 'filter_bank', 'filter_natgas', 'All States (US)']):
            print(f"{i}: {line.strip()[:120]}")

