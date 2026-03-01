#!/usr/bin/env python3
"""
Generate a simple English summary file for skills/ based on SKILL.md frontmatter.

Writes `summaries/skill_en.md` with a short table: Skill Name | Summary
"""
import os
import re
import glob


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


def main():
    base = os.path.join(os.getcwd(), "skills")
    outdir = os.path.join(os.getcwd(), "summaries")
    os.makedirs(outdir, exist_ok=True)
    entries = []
    for path in glob.glob(os.path.join(base, "**", "SKILL.md"), recursive=True):
        text = None
        try:
            with open(path, "r", encoding="utf-8") as f:
                text = f.read()
        except Exception:
            continue
        fm = extract_frontmatter(text)
        name = fm.get('name') or fm.get('title') or os.path.basename(os.path.dirname(path))
        desc = fm.get('description') or first_paragraph(text)
        desc_short = desc.splitlines()[0][:120]
        rel = os.path.relpath(path, os.getcwd()).replace('\\\\', '/')
        entries.append((name, desc_short, rel))

    # sort by name
    entries.sort(key=lambda x: x[0].lower())

    out_path = os.path.join(outdir, "skill_en.md")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write("# Skill Summary\n\n")
        f.write("This file lists all skills with a short English summary.\n\n")
        f.write("| Skill Name | Summary | Source |\n")
        f.write("|---|---|---|\n")
        for name, desc, rel in entries:
            f.write(f"| {name} | {desc} | {rel} |\n")

    print(f"Wrote {len(entries)} skills to {out_path}")


if __name__ == '__main__':
    main()
