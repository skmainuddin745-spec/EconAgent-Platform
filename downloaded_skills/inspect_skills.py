import os

BASE_DIR = r"F:\documents\SOIC\EconAgent_Platform\downloaded_skills"
repos = ["superpowers", "anthropic-skills", "ui-ux-pro-max-skill", "claude-mem", "awesome-claude-code"]

for repo in repos:
    rpath = os.path.join(BASE_DIR, repo)
    print("=" * 60)
    print(f"REPOSITORY: {repo}")
    print("=" * 60)
    if not os.path.exists(rpath):
        print(f"Directory not found: {rpath}")
        continue
    
    # List top-level items
    items = os.listdir(rpath)
    print("Top-level items:", items[:12])
    
    # Look for README
    readme_name = next((f for f in items if f.lower().startswith("readme")), None)
    if readme_name:
        rfile = os.path.join(rpath, readme_name)
        with open(rfile, "r", encoding="utf-8", errors="ignore") as f:
            lines = f.readlines()
            print(f"\n--- {readme_name} (First 20 lines) ---")
            for l in lines[:20]:
                print(l.rstrip())
    
    # Look for skill/plugin definitions
    skill_files = []
    for root, dirs, files in os.walk(rpath):
        for f in files:
            if f.endswith((".md", ".json", ".py", ".js", ".ts", ".sh")):
                skill_files.append(os.path.relpath(os.path.join(root, f), rpath))
    print(f"\nTotal text/code files: {len(skill_files)}")
    print("Sample files:", skill_files[:10])
    print("\n")

