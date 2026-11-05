#!/usr/bin/env python3
"""Rebuild all guide landing pages from front matter; preserve section URLs."""
import argparse
import json
from pathlib import Path
from sync_docs import ROOT, frontmatter, page, write_outputs

SECTIONS = [
    ("beginner", "Beginner", "Start with installation, data, files and small scripts."),
    ("medium", "Medium", "Combine OpenAF APIs for operational tasks."),
    ("advanced", "Advanced", "Detailed APIs, integrations and runtime behavior."),
    ("oneliner", "OneLiner", "Short commands for common tasks."),
    ("ojobio", "oJobIO", "Use the remotely maintained ojob.io job catalog."),
    ("cheat-sheet", "cheat-sheet", "Quick syntax and command references."),
    ("ojob", "oJob", "Author, test and operate automation workflows."),
    ("oafp", "oafp", "Read, query, transform and output structured data."),
    ("opacks", "oPacks", "Find packages and follow integration guides."),
]


def generate(root):
    generated = {}
    main = "# Guides\n\nStart with [Getting started](beginner/getting-started.md), [script-to-oJob authoring](ojob/script-to-ojob.md), or the [oafp usage guide](oafp/oafp-usage.md). See the [source baseline](../source-snapshot.md) for the revisions covered.\n\n"
    for order, (directory, title, description) in enumerate(SECTIONS, 1):
        entries = []
        for path in sorted((root / "docs/guides" / directory).glob("*.md")):
            if path.name == "index.md":
                continue
            meta, _ = frontmatter(path.read_text())
            entries.append((str(meta.get("title", path.stem)), path.name))
        body = f"# {title}\n\n{description}\n\n"
        if directory == "opacks":
            body += "Browse the [complete package catalog](catalog.md), including JDBC drivers and packages without a standalone guide.\n\n"
        for label, filename in sorted(entries, key=lambda entry: entry[0].casefold()):
            body += f"- [{label}]({filename})\n"
        generated[f"docs/guides/{directory}/index.md"] = page(title, "Guides", body, "OpenAF docs", {"has_children": True, "nav_order": order})
        main += f"## [{title}]({directory}/index.md)\n\n{description} **{len(entries)} guides.**\n\n"
    generated["docs/guides/index.md"] = page("Guides", "OpenAF docs", main, None, {"has_children": True, "nav_order": 2})
    return generated


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    changed = write_outputs(generate(args.root), args.root, args.check)
    raise SystemExit(1 if changed and args.check else 0)
