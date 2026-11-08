with open('platform_ui/bmap_html_template.html', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace('>Bank Branches (US)</div>', '>Bank Branches & Global Wealth Hubs</div>')
text = text.replace('>Branch Deposit Amounts</div>', '>Worldwide G-SIBs & FDIC Deposits</div>')

with open('platform_ui/bmap_html_template.html', 'w', encoding='utf-8') as f:
    f.write(text)
print('Updated legend in bmap_html_template.html!')

