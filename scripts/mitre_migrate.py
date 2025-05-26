#!/usr/bin/env python3
import os
import re
import shutil
from pathlib import Path

MITRE_DIR = Path("mitre")
TECHNIQUES_DIR = MITRE_DIR / "techniques"
TACTICS_DIR = MITRE_DIR / "tactics"
SUMMARY_FILE = Path("SUMMARY.md")


# Helper to parse tactics from a technique file
def parse_tactics_from_technique(md_path):
    with open(md_path, "r", encoding="utf-8") as f:
        content = f.read()
    match = re.search(r"- Tactics: (.+)", content)
    if not match:
        return []
    # Find all [TAxxxx](...)
    return re.findall(r"\[(TA[0-9]+)\]", match.group(1))


# Helper to parse Name from a markdown file
def parse_name_from_md(md_path):
    with open(md_path, "r", encoding="utf-8") as f:
        content = f.read()
    match = re.search(r"- Name: ([^\n]+)", content)
    if match:
        return match.group(1).strip()
    return md_path.stem


# Helper to update links in a markdown file
def update_links(md_path, tactic_id=None):
    with open(md_path, "r", encoding="utf-8") as f:
        content = f.read()
    # Update links to tactics
    content = re.sub(
        r"\[(TA[0-9]+)\]\(\.\./tactics/TA[0-9]+\.md\)",
        lambda m: f"[{m.group(1)}](../{m.group(1)}/{m.group(1)}.md)",
        content,
    )
    # Update links to techniques
    content = re.sub(
        r"\[(T[0-9]+(\.[0-9]+)?)\]\(\.\./techniques/([^)]+)\)",
        lambda m: f"[{m.group(1)}](../techniques/{m.group(1)}.md)"
        if tactic_id
        else f"[{m.group(1)}]({m.group(1)}.md)",
        content,
    )
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(content)


def extract_name_and_summary(md_path):
    name = None
    summary = None
    try:
        with open(md_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
        # Extract Name
        for i, line in enumerate(lines):
            if line.strip().startswith("- Name:"):
                name = line.split(":", 1)[1].strip()
                break
        # Extract summary from Introduction (first paragraph)
        intro = []
        in_intro = False
        for line in lines:
            if line.strip().startswith("## Introduction"):
                in_intro = True
                continue
            if in_intro:
                if line.strip().startswith("##") and not line.strip().startswith(
                    "## Introduction"
                ):
                    break
                intro.append(line.rstrip())
        # Get first non-empty paragraph
        summary = ""
        paragraph = []
        for l in intro:
            if l == "" and paragraph:
                break
            paragraph.append(l)
        summary = " ".join(paragraph).strip()
    except Exception:
        name = None
        summary = None
    return name, summary


def generate_mitre_summary_section():
    mitre_dir = Path("mitre")
    tactic_dirs = sorted(
        [d for d in mitre_dir.iterdir() if d.is_dir() and d.name.startswith("TA")]
    )
    summary_lines = []
    summary_lines.append("## MITRE\n")
    # Build a map of all techniques and sub-techniques
    technique_files = sorted((mitre_dir / "techniques").glob("T*.md"))
    techniques = {}
    subtechniques = {}
    for tfile in technique_files:
        tid = tfile.stem
        if "." in tid:
            parent = tid.split(".")[0]
            subtechniques.setdefault(parent, []).append(tid)
        else:
            techniques[tid] = tfile
    for tactic_dir in tactic_dirs:
        tid = tactic_dir.name
        tactic_md = tactic_dir / f"{tid}.md"
        if not tactic_md.exists():
            continue
        t_name, t_summary = extract_name_and_summary(
            mitre_dir / "tactics" / f"{tid}.md"
        )
        if not t_name:
            t_name = tid
        if not t_summary:
            t_summary = ""
        if t_summary:
            summary_lines.append(
                f"* [{t_name} ({tid})](mitre/{tid}/{tid}.md) - {t_summary}"
            )
        else:
            summary_lines.append(f"* [{t_name} ({tid})](mitre/{tid}/{tid}.md)")
        # Find all techniques for this tactic
        for tech_id, tfile in sorted(techniques.items()):
            tactics = parse_tactics_from_technique(tfile)
            if tid not in tactics:
                continue
            tech_name, _ = extract_name_and_summary(tfile)
            if not tech_name:
                tech_name = tech_id
            summary_lines.append(
                f"  * [{tech_name} ({tech_id})](mitre/{tid}/{tech_id}.md)"
            )
            # List sub-techniques
            for sub_id in sorted(subtechniques.get(tech_id, [])):
                subfile = mitre_dir / "techniques" / f"{sub_id}.md"
                sub_name, _ = extract_name_and_summary(subfile)
                if not sub_name:
                    sub_name = sub_id
                sub_tactics = parse_tactics_from_technique(subfile)
                if tid not in sub_tactics:
                    continue
                summary_lines.append(
                    f"    * [{sub_name} ({sub_id})](mitre/{tid}/{sub_id}.md)"
                )
    summary_lines.append(
        "* [All Techniques](mitre/techniques/) — Complete list of techniques."
    )
    return "\n".join(summary_lines)


def update_mitre_summary_md(target_file="MITRE_SUMMARY.md"):
    summary_path = Path(target_file)
    new_section = generate_mitre_summary_section()
    with open(summary_path, "w", encoding="utf-8") as f:
        f.write(new_section)


def main():
    # 1. Remove any TA* directories and 'common' in mitre/, leave 'tactics' and 'techniques' untouched
    for item in MITRE_DIR.iterdir():
        if item.name == "mitre_migrate.py" or item.name in ["tactics", "techniques"]:
            continue
        if item.is_dir() and (item.name.startswith("TA") or item.name == "common"):
            shutil.rmtree(item)
        elif item.is_file():
            item.unlink()

    # 2. Gather tactics and techniques
    tactic_files = list((TACTICS_DIR).glob("TA*.md"))
    technique_files = list((TECHNIQUES_DIR).glob("T*.md"))
    tactic_ids = [f.stem for f in tactic_files]
    technique_map = {}  # TID -> [tactic_ids]
    for tfile in technique_files:
        tactics = parse_tactics_from_technique(tfile)
        technique_map[tfile.stem] = tactics

    # 3. Create tactic dirs and copy tactic files, symlink techniques
    for tactic_file in tactic_files:
        tid = tactic_file.stem
        tdir = MITRE_DIR / tid
        tdir.mkdir(exist_ok=True)
        tactic_link = tdir / f"{tid}.md"
        tactic_target = os.path.relpath(tactic_file, tdir)
        if tactic_link.exists() or tactic_link.is_symlink():
            tactic_link.unlink()
        os.symlink(tactic_target, tactic_link)
        update_links(tactic_link)
        # Symlink techniques for this tactic
        for tname, tactics in technique_map.items():
            if tid in tactics:
                link = tdir / f"{tname}.md"
                target = os.path.relpath(TECHNIQUES_DIR / f"{tname}.md", tdir)
                if link.exists() or link.is_symlink():
                    link.unlink()
                os.symlink(target, link)

    # 4. Update links in technique files (should point to tactics and other techniques correctly)
    for tfile in technique_files:
        update_links(tfile)

    # 5. Build MITRE_SUMMARY.md tree with names
    update_mitre_summary_md()

    # 6. (Optional) Remove old 'tactics' after migration
    # Uncomment the following line if you want to remove it automatically:
    # shutil.rmtree(TACTICS_DIR)


if __name__ == "__main__":
    main()
