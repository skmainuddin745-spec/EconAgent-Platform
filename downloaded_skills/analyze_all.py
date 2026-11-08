import os
import json

BASE = r"F:\documents\SOIC\EconAgent_Platform\downloaded_skills"

def scan_repo(name):
    path = os.path.join(BASE, name)
    print("=" * 70)
    print(f"ANALYSIS OF: {name}")
    print("=" * 70)
    
    # 1. Structure
    dirs = []
    files = []
    for root, d_list, f_list in os.walk(path):
        rel = os.path.relpath(root, path)
        if ".git" in rel.split(os.sep):
            continue
        for d in d_list:
            dirs.append(os.path.join(rel, d))
        for f in f_list:
            files.append(os.path.join(rel, f))
            
    print(f"Total non-git directories: {len(dirs)}")
    print(f"Total non-git files: {len(files)}")
    
    # Key directories
    top_dirs = [d for d in dirs if os.path.dirname(d) in (".", "")]
    print(f"Top-level directories: {top_dirs}")
    
    # Skills / markdown docs
    md_files = [f for f in files if f.endswith(".md")]
    print(f"Markdown / Documentation files ({len(md_files)}):")
    for f in md_files[:15]:
        print(f"  - {f}")
        
    # Python / JS / JSON
    code_files = [f for f in files if f.endswith((".py", ".js", ".ts", ".json"))]
    print(f"Code / Data files ({len(code_files)}):")
    for f in code_files[:15]:
        print(f"  - {f}")

for r in ["superpowers", "anthropic-skills", "ui-ux-pro-max-skill", "claude-mem", "awesome-claude-code"]:
    scan_repo(r)

