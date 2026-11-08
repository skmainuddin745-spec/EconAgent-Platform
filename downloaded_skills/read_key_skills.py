import os

BASE = r"F:\documents\SOIC\EconAgent_Platform\downloaded_skills"

def read_skill_summary(rel_path):
    fpath = os.path.join(BASE, rel_path)
    print("=" * 70)
    print(f"SKILL: {rel_path}")
    print("=" * 70)
    if not os.path.exists(fpath):
        print("Not found.")
        return
    with open(fpath, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()
    # Print first 40 lines
    lines = content.splitlines()
    for l in lines[:35]:
        print(l)

read_skill_summary(r"anthropic-skills\skills\frontend-design\SKILL.md")
read_skill_summary(r"anthropic-skills\skills\web-artifacts-builder\SKILL.md")
read_skill_summary(r"anthropic-skills\skills\canvas-design\SKILL.md")
read_skill_summary(r"ui-ux-pro-max-skill\.claude\skills\ui-ux-pro-max\SKILL.md")

