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

Translation / AI agent workflow

- The script now emits translation queues for AI agents in `summaries/to_translate/` as JSONL files:
  - `agents_to_translate.jsonl` — entries to translate for `agent_en.md` → `agent_ja.md`
  - `skills_to_translate.jsonl` — entries to translate for `skill_en.md` → `skill_ja.md`
- These files are intended to be consumed by your AI agent (using `.github/prompts/summarize_changes.prompt.md`) which should output JSON objects with `summary` (Japanese) and `changelog_line` fields. The agent is responsible for writing `summaries/agent_ja.md` and `summaries/skill_ja.md` if desired.
