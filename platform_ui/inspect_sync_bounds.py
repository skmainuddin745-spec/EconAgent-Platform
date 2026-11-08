with open(r'F:\documents\SOIC\EconAgent_Platform\platform_ui\generate_dashboard.py', 'r', encoding='utf-8') as f:
    text = f.read()

s1 = text.find('// ── UNIVERSAL GLOBAL DROPDOWN MASTER SYNCHRONIZATION ──')
s2 = text.find('// ── BLOOMBERG TERMINAL COMMAND LINE INTERPRETER')

print('s1:', s1)
print('s2:', s2)
print('Length of synchronization code:', s2 - s1)
print('Excerpt of end:\n', text[s2-300:s2])

