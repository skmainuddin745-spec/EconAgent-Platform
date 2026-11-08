with open('F:/documents/SOIC/EconAgent_Platform/platform_ui/fractal_zoom_engine.py', 'r', encoding='utf-8') as f:
    text = f.read()

pos_n = text.find('nanoData = {')
print(text[pos_n:pos_n+300])

# Find where nanoData ends
pos_next = text.find('var currentCountry =', pos_n)
if pos_next == -1:
    pos_next = text.find('window.', pos_n)
print('nanoData ends around:', pos_next)
print(text[pos_next-200:pos_next+200])

