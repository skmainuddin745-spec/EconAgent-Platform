with open(r'F:\documents\SOIC\EconAgent_Platform\platform_ui\generate_dashboard.py', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = re.findall(r'<div[^>]+id=["\']predictor["\'][^>]*>', text)
print('id="predictor" tags:', matches)

idx = text.find('id="predictor"')
if idx != -1:
    print('Content of predictor div:')
    print(text[idx:idx+500])
else:
    print('id="predictor" NOT FOUND in generate_dashboard.py!')

