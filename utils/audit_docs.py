#!/usr/bin/env python3
"""Inventory every published Markdown page and distinguish review evidence."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import subprocess

from sync_docs import ROOT, MANIFEST, frontmatter, write_outputs


def inventory():
    manifest = json.loads(MANIFEST.read_text())
    imports = {i["destination"]: i for i in manifest["imports"]}
    keys = json.loads((ROOT / "utils/reference-keys.json").read_text())
    known = {key for subject in keys.values() for key in subject}
    baseline = set(subprocess.check_output(["git", "ls-tree", "-r", "--name-only", manifest["site_baseline_revision"]], cwd=ROOT, text=True).splitlines())
    changed = set(subprocess.check_output(["git", "diff", "--name-only", manifest["site_baseline_revision"]], cwd=ROOT, text=True).splitlines())
    records = []
    for path in sorted(ROOT.rglob("*.md")):
        rel = path.relative_to(ROOT)
        if any(part.startswith(".") or part in {"utils", "vendor", "_site"} for part in rel.parts):
            continue
        filename = rel.as_posix()
        meta, body = frontmatter(path.read_text())
        if not meta.get("layout"):
            continue
        source, evidence = [], []
        if filename in imports:
            item = imports[filename]
            source = [{"repository": item["repository"], "path": item["source"],
                       "revision": manifest["repositories"][item["repository"]]["revision"]}]
            disposition = "source import"
            if item.get("body_file"):
                disposition = "curated implementation-based replacement"
                evidence.append(item["body_file"])
            elif item.get("corrections"):
                disposition = "source import with recorded corrections"
                evidence.append("utils/source-map.json corrections")
        elif filename.startswith("docs/reference/") and path.stem in {s.replace('.', '_') for s in keys}:
            disposition = "source ODoc extraction"
            source = [{"repository": "openaf", "revision": manifest["repositories"]["openaf"]["revision"],
                       "path": "buildos.js subject mapping"}]
        elif path.name == "index.md" and filename.startswith("docs/guides/"):
            disposition = "generated navigation"
            evidence.append("utils/gen_indexes.py")
        elif filename in {"docs/guides/opacks/catalog.md", "docs/guides/ojob/ojob-common-modules.md", "docs/guides/cheat-sheet/ojob-all.md"}:
            disposition = "generated source catalog"
            evidence.append("utils/sync_docs.py")
        else:
            disposition = "editorial revision" if filename in changed or filename not in baseline else "screened and retained"
        # Symbol matches aid retrieval; they are not proof of semantic correctness.
        mentioned = sorted(k for k in known if len(k) >= 5 and k in body)
        records.append({"page": filename, "title": meta["title"], "existed_at_start": filename in baseline,
                        "disposition": disposition, "source": source, "review_evidence": evidence,
                        "api_names_mentioned": mentioned, "external_examples": "ojob.io/" in body or "nAttrMon" in body,
                        "sha256": hashlib.sha256(path.read_bytes()).hexdigest()})
    return {"baseline_date": manifest["checked_on"],
            "method": "All pages receive structure, navigation and rendered-link checks. JavaScript syntax and runtime checks have separate reports. Symbol matches are retrieval hints, not semantic or execution proof. Screened-and-retained pages were not individually integration-tested.",
            "pages": records}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    report = inventory()
    changed = write_outputs({"utils/page-audit.json": json.dumps(report, indent=2) + "\n"}, ROOT, args.check)
    print(f'{len(report["pages"])} published pages inventoried')
    raise SystemExit(int(args.check and changed))
