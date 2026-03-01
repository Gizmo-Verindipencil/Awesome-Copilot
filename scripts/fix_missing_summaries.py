#!/usr/bin/env python3
"""
Fix missing entries in summaries/ for agents/ and skills/.

This script mirrors the checks in `check_summaries_consistency.py` and
appends missing agent entries to `summaries/agent_en.md` and missing skill
rows to `summaries/skill_en.md` using frontmatter or first-paragraph heuristics.

Run from repo root:
  python scripts/fix_missing_summaries.py
"""
from pathlib import Path
import re
import datetime


ROOT = Path.cwd()


def extract_frontmatter(text):
    if not text:
        return {}
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.S)
    res = {}
    if m:
        body = m.group(1)
        for line in body.splitlines():
            if ":" in line:
                k, v = line.split(":", 1)
                res[k.strip()] = v.strip().strip("'\"")
    return res


def first_paragraph(text):
    if not text:
        return ""
    text = re.sub(r"^---.*?---\s*\n", "", text, flags=re.S)
    parts = [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()]
    return parts[0] if parts else ""


def find_agent_files():
    return sorted([p for p in (ROOT / 'agents').rglob('*.agent.md')])


def parse_agent_summary_paths(md_path):
    if not md_path.exists():
        return []
    text = md_path.read_text(encoding='utf-8')
    paths = []
    for m in re.finditer(r"—\s*(?P<path>[\w\-\./]+)\s*\(", text):
        p = m.group('path')
        if p.startswith('agents/'):
            paths.append((ROOT / p).resolve())
    return paths


def find_skill_files():
    return sorted([p for p in (ROOT / 'skills').rglob('SKILL.md')])


def parse_skill_table_sources(md_path):
    if not md_path.exists():
        return []
    lines = md_path.read_text(encoding='utf-8').splitlines()
    sources = []
    for i, line in enumerate(lines):
        if line.strip().startswith('| Skill Name'):
            for row in lines[i+2:]:
                if not row.strip().startswith('|'):
                    break
                parts = [p.strip() for p in row.split('|')]
                if len(parts) >= 4:
                    src = parts[3]
                    if src and not src.startswith('http'):
                        sources.append((ROOT / src).resolve())
            break
    return sources


def append_agent_summary(md_path, date, relpath, summary, commit):
    md_path.parent.mkdir(parents=True, exist_ok=True)
    with md_path.open('a', encoding='utf-8') as f:
        f.write(f"### {date} — {relpath} (N)\n")
        f.write(f"Summary: {summary}\n")
        f.write(f"Commit: {commit}\n\n")


def append_skill_row(md_path, name, desc, source_rel):
    md_path.parent.mkdir(parents=True, exist_ok=True)
    with md_path.open('a', encoding='utf-8') as f:
        f.write(f"| {name} | {desc} | {source_rel} |\n")


def main():
    agent_files = find_agent_files()
    agent_summary_md = ROOT / 'summaries' / 'agent_en.md'
    agent_summary_paths = parse_agent_summary_paths(agent_summary_md)

    agent_files_set = set([p.resolve() for p in agent_files])
    agent_summary_set = set([p for p in agent_summary_paths])

    missing_agents = sorted([p for p in agent_files_set if p not in agent_summary_set])

    skill_files = find_skill_files()
    skill_summary_md = ROOT / 'summaries' / 'skill_en.md'
    skill_summary_sources = parse_skill_table_sources(skill_summary_md)

    skill_files_set = set([p.resolve() for p in skill_files])
    skill_summary_set = set([p for p in skill_summary_sources])
    missing_skills = sorted([p for p in skill_files_set if p not in skill_summary_set])

    date = datetime.date.today().isoformat()
    rc = 'HEAD'

    # append missing agents
    for p in missing_agents:
        try:
            text = p.read_text(encoding='utf-8')
        except Exception:
            continue
        fm = extract_frontmatter(text)
        name = fm.get('name') or fm.get('title') or p.stem
        desc = fm.get('description') or first_paragraph(text)
        short = (name if name else p.name)
        append_agent_summary(agent_summary_md, date, str(p.relative_to(ROOT)).replace('\\\\','/'), desc[:300], rc)

    # append missing skills as table rows
    for p in missing_skills:
        try:
            text = p.read_text(encoding='utf-8')
        except Exception:
            continue
        fm = extract_frontmatter(text)
        name = fm.get('name') or fm.get('title') or p.parent.name
        desc = fm.get('description') or first_paragraph(text)
        desc_short = (desc.splitlines()[0] if desc else '')[:120]
        source_rel = str(p.relative_to(ROOT)).replace('\\\\','/')
        append_skill_row(skill_summary_md, name, desc_short, source_rel)

    print(f'Appended {len(missing_agents)} agents and {len(missing_skills)} skills to summaries')


if __name__ == '__main__':
    main()
