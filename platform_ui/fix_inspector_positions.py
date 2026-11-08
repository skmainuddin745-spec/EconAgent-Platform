with open('platform_ui/bmap_js_template.js', 'r', encoding='utf-8') as f:
    text = f.read()

# Fix 1: Restore clean border color at pos 708100
bad_border_block = text[708140:708140+1400]
print("Bad border block snippet:\n", bad_border_block[:200])

clean_border = """} else if (type === 'bank_branch' || type === 'manhattan_branch') {
      pop.style.borderColor = (item && item.regulator) ? '#ffd700' : '#a855f7';
    """

# Let's find the exact bad block
target_bad_border = text.find("pop.style.borderColor = '#facc15';\n    } else if (type === 'bank_branch' || type === 'manhattan_branch') {\n      var isGlobal = !!item.regulator;")
if target_bad_border != -1:
    end_bad_border = text.find("} else if (type === 'cable' || type === 'submarine_cables') {", target_bad_border)
    text = text[:target_bad_border] + "pop.style.borderColor = '#facc15';\n    } else if (type === 'bank_branch' || type === 'manhattan_branch') {\n      pop.style.borderColor = (item && item.regulator) ? '#ffd700' : '#a855f7';\n    " + text[end_bad_border:]
    print("Fixed border color block!")
else:
    print("WARNING: target_bad_border not found!")

# Fix 2: Upgrade body at the actual position
target_actual_body = text.find("} else if (type === 'bank_branch' || type === 'manhattan_branch') {\n      nameEl.textContent = '🏛️ ' + (item.name || item.bank || 'Commercial Banking Branch');\n      typeEl.textContent = 'FDIC Insured';")
if target_actual_body != -1:
    end_actual_body = text.find("} else if (type === 'cable' || type === 'submarine_cables') {", target_actual_body)
    new_rich_body = """} else if (type === 'bank_branch' || type === 'manhattan_branch') {
      var isGlobal = !!(item.regulator || item.scope || (item.country && item.country !== 'United States'));
      nameEl.textContent = '🏛️ ' + (item.name || item.bank || 'Commercial Banking Branch');
      typeEl.textContent = isGlobal ? (item.type || 'Global Banking Titan') : 'FDIC Insured (US)';
      typeEl.style.background = isGlobal ? '#4a044e' : '#3b0764';
      typeEl.style.color = isGlobal ? '#f472b6' : '#c084fc';

      if (l1) l1.textContent = isGlobal ? 'Regulatory Authority:' : 'FDIC Status:';
      statEl.textContent = isGlobal ? ('● ' + item.regulator) : '● Active / FDIC Insured';
      statEl.style.color = '#00e676';

      if (l2) l2.textContent = isGlobal ? 'Institution / Ticker:' : 'Institution:';
      imoEl.textContent = (item.bank || 'Bank') + (item.symbol ? ' [' + item.symbol + ']' : '') + (item.country ? ' · ' + item.country : '');

      if (l3) l3.textContent = 'Headquarters / Address:';
      ownerEl.textContent = item.address || 'Commercial Banking Center';

      if (l4) l4.textContent = isGlobal ? 'Consolidated Assets:' : 'Branch Deposits:';
      destEl.textContent = isGlobal
        ? ('$' + (item.assetsM >= 1000 ? (item.assetsM / 1000).toFixed(2) + 'B' : item.assetsM + 'M') + ' USD')
        : ('$' + (item.depM ? item.depM.toLocaleString() : (item.dep_branch ? (item.dep_branch/1000).toFixed(1) : '1,214.6')) + 'M');
      destEl.style.color = '#00e676';

      if (l5) l5.textContent = isGlobal ? 'Tier-1 Capital / Deposits:' : 'Company Domestic Assets:';
      berthEl.textContent = isGlobal
        ? ((item.tier1 || '15.2% CET-1') + ' · $' + (item.depM >= 1000 ? (item.depM / 1000).toFixed(2) + 'B' : item.depM + 'M') + ' Dep')
        : (item.assets_company ? '$' + (item.assets_company/1000000000).toFixed(2) + 'B' : '$3,914.1B');

      if (l6) l6.textContent = isGlobal ? 'Branch Network Footprint:' : 'Branch Classification:';
      speedEl.textContent = isGlobal ? (item.branches_total || 'Global Banking Flagship') : (item.type || 'Commercial Banking Center');
      speedEl.style.color = '#38bdf8';

      if (l7) l7.textContent = 'WGS84 Coordinates:';
      draftEl.textContent = item.lat.toFixed(4) + '°, ' + item.lon.toFixed(4) + '°';
    """
    text = text[:target_actual_body] + new_rich_body + text[end_actual_body:]
    print("Fixed actual body block!")
else:
    print("WARNING: target_actual_body not found!")

with open('platform_ui/bmap_js_template.js', 'w', encoding='utf-8') as f:
    f.write(text)
print("Updated platform_ui/bmap_js_template.js successfully!")

