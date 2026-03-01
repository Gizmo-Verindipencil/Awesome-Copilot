# generate_summaries.py

Minimal prototype to detect changes under `agents/` and `skills/` and append
human-readable summaries to `summaries/` and `changelog.md`.

Quick run (from repo root):

```bash
python scripts/generate_summaries.py --base HEAD~1 --out changelog.md --summaries-dir summaries/
```

Notes:

- The script uses `git` and is dependency-free.
- It uses simple frontmatter extraction and paragraph heuristics (no LLM).
- For better summaries, integrate an LLM and replace `summary` generation.
