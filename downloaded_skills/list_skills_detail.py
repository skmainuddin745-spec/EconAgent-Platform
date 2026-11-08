import os

BASE = r"F:\documents\SOIC\EconAgent_Platform\downloaded_skills"

print("--- SUPERPOWERS SKILLS ---")
sp_skills = os.path.join(BASE, "superpowers", "skills")
if os.path.exists(sp_skills):
    for s in os.listdir(sp_skills):
        spath = os.path.join(sp_skills, s)
        print(" *", s)

print("\n--- ANTHROPIC SKILLS ---")
as_skills = os.path.join(BASE, "anthropic-skills", "skills")
if os.path.exists(as_skills):
    for s in os.listdir(as_skills):
        print(" *", s)

print("\n--- UI UX PRO MAX SKILLS & RULES ---")
uupm_skills = os.path.join(BASE, "ui-ux-pro-max-skill", ".claude", "skills")
if os.path.exists(uupm_skills):
    for s in os.listdir(uupm_skills):
        print(" *", s)

uupm_docs = os.path.join(BASE, "ui-ux-pro-max-skill", "docs")
if os.path.exists(uupm_docs):
    for d in os.listdir(uupm_docs)[:15]:
        print("   doc:", d)

print("\n--- CLAUDE-MEM CAPABILITIES ---")
cm_path = os.path.join(BASE, "claude-mem")
for item in os.listdir(cm_path)[:15]:
    print(" *", item)

