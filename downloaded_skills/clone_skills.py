import os
import subprocess

TARGET_DIR = r"F:\documents\SOIC\EconAgent_Platform\downloaded_skills"
os.makedirs(TARGET_DIR, exist_ok=True)

repos = [
    ("superpowers", "https://github.com/obra/superpowers.git"),
    ("anthropic-skills", "https://github.com/anthropics/skills.git"),
    ("ui-ux-pro-max-skill", "https://github.com/nextlevelbuilder/ui-ux-pro-max-skill.git"),
    ("claude-mem", "https://github.com/thedotmack/claude-mem.git"),
    ("awesome-claude-code", "https://github.com/hesreallyhim/awesome-claude-code.git")
]

for name, url in repos:
    dest = os.path.join(TARGET_DIR, name)
    if os.path.exists(dest):
        print(f"[{name}] already exists at {dest}")
    else:
        print(f"Cloning [{name}] from {url}...")
        cmd = ["git", "clone", "--depth", "1", url, dest]
        res = subprocess.run(cmd, capture_output=True, text=True)
        if res.returncode == 0:
            print(f"Successfully cloned [{name}].")
        else:
            print(f"Failed to clone [{name}]: {res.stderr}")

print("\nAll downloads finished. Listing directory contents:")
for item in os.listdir(TARGET_DIR):
    item_path = os.path.join(TARGET_DIR, item)
    print(f" - {item} ({'DIR' if os.path.isdir(item_path) else 'FILE'})")

