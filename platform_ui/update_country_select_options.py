import os

curr_dir = r"F:\documents\SOIC\EconAgent_Platform\platform_ui"
with open(os.path.join(curr_dir, 'generate_dashboard.py'), 'r', encoding='utf-8') as f:
    code = f.read()

old_options = """      <select id="global_country_select" onchange="syncGlobalCountryChange(this.value)" style="background: #0d1a2d; color: #00e5ff; border: 1px solid #294c7a; border-radius: 4px; padding: 5px 10px; font-size: 11px; font-weight: 700; font-family: var(--font-mono); cursor: pointer; outline: none;">
        <option value="india">🇮🇳 India (Baa3 / CRP 2.38%)</option>
        <option value="us">🇺🇸 United States (Aaa / CRP 0.00%)</option>
        <option value="germany">🇩🇪 Germany (Aaa / CRP 0.00%)</option>
        <option value="japan">🇯🇵 Japan (A1 / CRP 0.65%)</option>
        <option value="uk">🇬🇧 United Kingdom (Aa3 / CRP 0.75%)</option>
        <option value="china">🇨🇳 China (A1 / CRP 0.94%)</option>
        <option value="brazil">🇧🇷 Brazil (Ba2 / CRP 3.82%)</option>
        <option value="saudi">🇸🇦 Saudi Arabia (A1 / CRP 0.85%)</option>
        <option value="singapore">🇸🇬 Singapore (Aaa / CRP 0.00%)</option>
        <option value="australia">🇦🇺 Australia (Aaa / CRP 0.00%)</option>
        <option value="korea">🇰🇷 South Korea (Aa2 / CRP 0.55%)</option>
        <option value="uae">🇦🇪 UAE (Aa2 / CRP 0.58%)</option>
      </select>"""

new_options = """      <select id="global_country_select" onchange="syncGlobalCountryChange(this.value)" style="background: #0d1a2d; color: #00e5ff; border: 1px solid #294c7a; border-radius: 4px; padding: 5px 10px; font-size: 11px; font-weight: 700; font-family: var(--font-mono); cursor: pointer; outline: none;">
        <option value="in" selected>🇮🇳 India (Baa3 / CRP 2.38%)</option>
        <option value="us">🇺🇸 United States (Aaa / CRP 0.00%)</option>
        <option value="tw">🇹🇼 Taiwan (Aa3 / CRP 0.60%)</option>
        <option value="nl">🇳🇱 Netherlands (Aaa / CRP 0.00%)</option>
        <option value="sa">🇸🇦 Saudi Arabia (A1 / CRP 0.85%)</option>
        <option value="de">🇩🇪 Germany (Aaa / CRP 0.00%)</option>
        <option value="jp">🇯🇵 Japan (A1 / CRP 0.65%)</option>
        <option value="kr">🇰🇷 South Korea (Aa2 / CRP 0.55%)</option>
        <option value="cn">🇨🇳 China (A1 / CRP 0.94%)</option>
        <option value="uk">🇬🇧 United Kingdom (Aa3 / CRP 0.75%)</option>
        <option value="fr">🇫🇷 France (Aa2 / CRP 0.40%)</option>
        <option value="ch">🇨🇭 Switzerland (Aaa / CRP 0.00%)</option>
        <option value="au">🇦🇺 Australia (Aaa / CRP 0.00%)</option>
        <option value="all">🌐 Global All-World (94 Damodaran Industries)</option>
      </select>"""

assert old_options in code, "old_options not found in generate_dashboard.py"
code = code.replace(old_options, new_options)

with open(os.path.join(curr_dir, 'generate_dashboard.py'), 'w', encoding='utf-8') as f:
    f.write(code)

print("Updated global_country_select options successfully!")

