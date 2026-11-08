import os

for root, dirs, files in os.walk('platform_ui'):
    for file in files:
        if file.endswith(('.py', '.js', '.html')):
            full_path = os.path.join(root, file)
            try:
                with open(full_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    if 'switchTitanTab' in content:
                        print(f"Found in {full_path}")
            except Exception:
                pass

