# F:\documents\SOIC\EconAgent_Platform\platform_ui\build_rich_engine.py
import json
import os
import sys

BASE_DIR = r"F:\documents\SOIC\EconAgent_Platform\platform_ui"
sys.path.insert(0, BASE_DIR)

from generate_full_bloomberg_suite import (
    CRUDE_PIPELINES,
    GAS_PIPELINES_NAM,
    BERTH_VISITS,
    MANHATTAN_STREET_BRANCHES,
    GREG_MORTIMER,
    WORLD_EQUITY_DATA,
    SPLC_NETWORKS,
    FXC_DATA,
    READ_NEWS_STORIES
)

print("Starting generation of comprehensive rich Bloomberg templates...")

# Let's write the HTML template
html_path = os.path.join(BASE_DIR, "bmap_html_template.html")
js_path = os.path.join(BASE_DIR, "bmap_js_template.js")

# We will write the files directly using Python file writing
