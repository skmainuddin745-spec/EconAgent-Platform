# Downloaded Skills — Analysis & Reference Suite

This directory contains utility scripts to download, inspect, and analyze external AI agent skill frameworks and prompt engineering patterns.

## Cloned Reference Repositories
The following reference repositories can be downloaded using `clone_skills.py`:
- `superpowers` ([obra/superpowers](https://github.com/obra/superpowers))
- `anthropic-skills` ([anthropics/skills](https://github.com/anthropics/skills))
- `ui-ux-pro-max-skill` ([nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill))
- `claude-mem` ([thedotmack/claude-mem](https://github.com/thedotmack/claude-mem))
- `awesome-claude-code` ([hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code))

*(Note: Cloned third-party repository directories are git-ignored to keep the repository lightweight and self-contained. Run `python clone_skills.py` to clone shallow copies for local research.)*

## Analysis & Inspection Scripts
- `clone_skills.py`: Clones shallow `--depth 1` copies of all 5 reference repositories.
- `analyze_all.py`: Traverses each cloned repository and extracts structural statistics, markdown guides, and code templates.
- `inspect_skills.py`: Inspects prompt architectures and multi-agent coordination hooks.
- `list_skills_detail.py`: Catalogs tool signatures and JSON schemas across the skills corpus.
- `read_key_skills.py`: Reads and parses primary skill definition files.

