#!/usr/bin/env python3
"""
Minimal prototype to generate summaries and changelog for agents/prompts.

Usage:
  python scripts/generate_summaries.py --base HEAD~1 --out changelog.md --summaries-dir summaries/

This script is intentionally dependency-free and uses `git` to find diffs.
It extracts simple frontmatter fields (`name`, `description`) when available
and writes human-readable entries to `changelog.md` and `summaries/*.md`.
"""
import argparse
import datetime
import os
import re
import subprocess
import sys
import glob


def run(cmd):
    proc = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return proc.returncode, proc.stdout.strip(), proc.stderr.strip()


def git_diff_name_status(base):
    # include 'skills/' as the target for prompt-like resources
    cmd = ["git", "diff", "--name-status", f"{base}..HEAD", "--", "agents/", "skills/"]
    rc, out, err = run(cmd)
    if rc != 0:
        print(err, file=sys.stderr)
        return []
    lines = [l for l in out.splitlines() if l.strip()]
    entries = []
    for line in lines:
        parts = line.split('\t')
        status = parts[0]
        path = parts[-1]
        entries.append((status, path))
    return entries


def get_file_at(commit, path):
    rc, out, err = run(["git", "show", f"{commit}:{path}"])
    if rc != 0:
        return None
    return out


def read_file(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except Exception:
        return None


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
    # remove frontmatter
    text = re.sub(r"^---.*?---\s*\n", "", text, flags=re.S)
    # find first non-empty paragraph
    parts = [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()]
    return parts[0] if parts else ""


def append_summary(summaries_dir, kind, date, path, status, summary, commit):
    filename = os.path.join(summaries_dir, f"{kind}_en.md")
    os.makedirs(summaries_dir, exist_ok=True)
    header = f"### {date} — {path} ({status})\n"
    entry = header + f"Summary: {summary}\nCommit: {commit}\n\n"
    with open(filename, "a", encoding="utf-8") as f:
        f.write(entry)


def append_changelog(out_path, date, items):
    header = f"## {date}\n\n"
    lines = [header]
    for it in items:
        lines.append(f"- {it['status']} {it['path']} — {it['short']} ({it['commit']})\n")
    with open(out_path, "a", encoding="utf-8") as f:
        f.writelines(lines)


def generate_skill_index(summaries_dir):
    """Scan skills/**/SKILL.md and write summaries/skill_en.md"""
    base = os.path.join(os.getcwd(), "skills")
    entries = []
    for path in glob.glob(os.path.join(base, "**", "SKILL.md"), recursive=True):
        try:
            with open(path, "r", encoding="utf-8") as f:
                text = f.read()
        except Exception:
            continue
        fm = extract_frontmatter(text)
        name = fm.get('name') or fm.get('title') or os.path.basename(os.path.dirname(path))
        desc = fm.get('description') or first_paragraph(text)
        desc_short = (desc.splitlines()[0] if desc else "")[:120]
        rel = os.path.relpath(path, os.getcwd()).replace('\\', '/')
        entries.append((name, desc_short, rel))

    entries.sort(key=lambda x: x[0].lower())
    out_path = os.path.join(summaries_dir, "skill_en.md")
    os.makedirs(summaries_dir, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write("# Skill Summary\n\n")
        f.write("This file lists all skills with a short English summary.\n\n")
        f.write("| Skill Name | Summary | Source |\n")
        f.write("|---|---|---|\n")
        for name, desc, rel in entries:
            f.write(f"| {name} | {desc} | {rel} |\n")
    return out_path


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--base", default="upstream/main", help="Base ref to compare (git)")
    p.add_argument("--out", default="changelog.md", help="Changelog output path")
    p.add_argument("--summaries-dir", default="summaries/", help="Summaries directory")
    args = p.parse_args()

    entries = git_diff_name_status(args.base)
    if not entries:
        print("No changes found (or git command failed).")
        return

    rc, commit_short, _ = run(["git", "rev-parse", "--short", "HEAD"])
    date = datetime.date.today().isoformat()

    changelog_items = []
    # prepare translation queues for AI agent
    to_translate_agents = []
    to_translate_skills = []
    for status, path in entries:
        if path.startswith("agents/"):
            kind = "agent"
        elif path.startswith("skills/"):
            kind = "skill"
        else:
            kind = "other"
        short = ""
        summary = ""
        if status == 'A':
            new = read_file(path)
            fm = extract_frontmatter(new)
            short = fm.get('name') or fm.get('title') or first_paragraph(new)[:80]
            summary = fm.get('description') or first_paragraph(new)[:300]
        elif status == 'M':
            old = get_file_at(args.base, path)
            new = read_file(path)
            # prefer frontmatter name
            fm_new = extract_frontmatter(new)
            short = fm_new.get('name') or first_paragraph(new)[:80]
            # create simple diff summary: show first paragraphs from old -> new
            old_p = first_paragraph(old)
            new_p = first_paragraph(new)
            if old_p and new_p and old_p.strip() != new_p.strip():
                summary = f"Updated: {old_p[:200]} -> {new_p[:200]}"
            else:
                summary = fm_new.get('description') or new_p[:300]
        elif status == 'D':
            short = os.path.basename(path)
            summary = "Deleted from repository."
        else:
            short = os.path.basename(path)
            summary = "Change detected."

        append_summary(args.summaries_dir, kind, date, path, status, summary, commit_short)
        changelog_items.append({"status": status, "path": path, "short": (short or ''), "commit": commit_short})
        payload = {"path": path, "status": status, "commit": commit_short, "summary_en": summary, "changelog_line_en": (short or '')}
        if kind == 'agent':
            to_translate_agents.append(payload)
        elif kind == 'skill':
            to_translate_skills.append(payload)

    append_changelog(args.out, date, changelog_items)
    print(f"Wrote {len(changelog_items)} items to {args.out} and summaries dir {args.summaries_dir}")

    # also regenerate full skill index
    skill_index = generate_skill_index(args.summaries_dir)
    print(f"Generated skill index: {skill_index}")

    # write translation queues as JSONL for AI agent processing (no API calls here)
    import json
    qdir = os.path.join(args.summaries_dir, "to_translate")
    os.makedirs(qdir, exist_ok=True)
    agents_q = os.path.join(qdir, "agents_to_translate.jsonl")
    skills_q = os.path.join(qdir, "skills_to_translate.jsonl")
    with open(agents_q, "w", encoding="utf-8") as f:
        for obj in to_translate_agents:
            f.write(json.dumps(obj, ensure_ascii=False) + "\n")
    with open(skills_q, "w", encoding="utf-8") as f:
        for obj in to_translate_skills:
            f.write(json.dumps(obj, ensure_ascii=False) + "\n")
    print(f"Wrote translation queues: {agents_q}, {skills_q}")


if __name__ == '__main__':
    main()
