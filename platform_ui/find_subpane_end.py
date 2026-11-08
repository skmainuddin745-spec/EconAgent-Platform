with open('F:/documents/SOIC/EconAgent_Platform/platform_ui/institutional_giants_engine.py', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find('id="titan_subpane_tick"')
pos_next = text.find('<!-- ── INTERACTIVE JAVASCRIPT LOGIC ── -->', pos)
print(text[pos_next-200:pos_next+200])

