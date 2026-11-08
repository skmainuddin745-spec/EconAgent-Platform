import re
import os

BASE_DIR = r"F:\documents\SOIC\EconAgent_Platform\platform_ui"
html_path = os.path.join(BASE_DIR, "bmap_html_template.html")
with open(html_path, "r", encoding="utf-8") as f:
    text = f.read()

pos = text.find('id="bmap_view_container_gev"')
end_pos = text.find('id="bmap_view_container_table"', pos)
print('Current GEV container in bmap_html_template.html:')
print(text[pos:end_pos])

