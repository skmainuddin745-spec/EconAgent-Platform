import os

path = r"F:\documents\SOIC\EconAgent_Platform\platform_ui\bmap_html_template.html"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

OLD_STR = """    <div style="background: #090f1a; border-top: 1px solid #1e334d; padding: 8px 16px; display: flex; justify-content: flex-end;">
      <button onclick="closeAllDatasetsModal()" style="background: #1e3a5f; color: #00e5ff; border: 1px solid #3b82f6; border-radius: 3px; padding: 5px 14px; font-size: 10.5px; font-weight: 800; cursor: pointer;">Done</button>
    </div>
  </div>
</div>"""

NEW_STR = """    <div style="background: #090f1a; border-top: 1px solid #1e334d; padding: 8px 16px; display: flex; justify-content: flex-end;">
      <button onclick="closeAllDatasetsModal()" style="background: #1e3a5f; color: #00e5ff; border: 1px solid #3b82f6; border-radius: 3px; padding: 5px 14px; font-size: 10.5px; font-weight: 800; cursor: pointer;">Done</button>
    </div>
  </div>
</div>
</div> <!-- END bmap_view_container_map -->"""

assert OLD_STR in text, "OLD_STR not found in bmap_html_template.html"
text = text.replace(OLD_STR, NEW_STR)

with open(path, "w", encoding="utf-8") as f:
    f.write(text)

print("Added missing </div> to close bmap_view_container_map.")

