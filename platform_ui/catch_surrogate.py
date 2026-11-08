import sys
sys.path.append('F:/documents/SOIC/EconAgent_Platform/platform_ui')
import generate_dashboard

# monkey-patch open in generate_dashboard to see the html string
original_open = open
def debug_open(file, mode="r", encoding=None, errors=None, **kwargs):
    if "EconAgent_Dashboard.html" in str(file) and "w" in mode:
        return original_open(file, mode, encoding="utf-8", errors="surrogateescape", **kwargs)
    return original_open(file, mode, encoding=encoding, errors=errors, **kwargs)

generate_dashboard.open = debug_open

path = generate_dashboard.generate_dashboard()
print("Wrote file with surrogateescape!")

# Now inspect the file to find where the surrogate is!
with original_open(path, "r", encoding="utf-8", errors="surrogateescape") as f:
    content = f.read()

surrogates = [(i, c, hex(ord(c))) for i, c in enumerate(content) if 0xD800 <= ord(c) <= 0xDFFF]
print(f"Total surrogates found: {len(surrogates)}")
for i, c, h in surrogates[:10]:
    print(f"Pos {i}: {h}")
    print("Context:", repr(content[max(0, i-50):i+50]))

