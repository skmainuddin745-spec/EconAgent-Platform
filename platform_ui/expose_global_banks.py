with open('platform_ui/bmap_js_template.js', 'r', encoding='utf-8') as f:
    text = f.read()

target = "var globalBankingTitans = __GLOBAL_BANKING_JSON__;"
replacement = """var globalBankingTitans = __GLOBAL_BANKING_JSON__;
  window.globalBankingTitans = globalBankingTitans;
  window.branchesCompact = branchesCompact;"""

if target in text:
    text = text.replace(target, replacement, 1)
    with open('platform_ui/bmap_js_template.js', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Exposed globalBankingTitans and branchesCompact on window!")
else:
    print("Target not found!")

