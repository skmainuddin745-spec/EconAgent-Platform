with open('platform_ui/bmap_js_template.js', 'r', encoding='utf-8') as f:
    text = f.read()

# Remove <script> from where it was
pos = text.find('<script>')
if pos != -1:
    text = text[:pos] + text[pos+8:]

# Put <script> at the very beginning
text = "<script>\n" + text.lstrip()

with open('platform_ui/bmap_js_template.js', 'w', encoding='utf-8') as f:
    f.write(text)

print("Placed <script> at line 1 of bmap_js_template.js successfully!")

