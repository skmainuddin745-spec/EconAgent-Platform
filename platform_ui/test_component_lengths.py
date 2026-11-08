from institutional_giants_engine import build_institutional_giants_section
from soic_sector_models_component import build_soic_sector_models_section
from top_notch_framework_engine import build_top_notch_framework_section

t_sec = build_institutional_giants_section()
s_sec = build_soic_sector_models_section()
p_sec = build_top_notch_framework_section()

print('titans section len:', len(t_sec))
print('soic_sectors section len:', len(s_sec))
print('topnotch section len:', len(p_sec))

