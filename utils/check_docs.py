#!/usr/bin/env python3
"""Check Markdown structure and local links, optionally crawl a rendered site."""
import argparse
from collections import Counter
from html.parser import HTMLParser
import json
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit

from sync_docs import ROOT, frontmatter, outside_code


def markdown_checks(root):
    errors, pages, metadata = [], {}, {}
    for path in sorted(root.rglob("*.md")):
        rel = path.relative_to(root)
        if any(part.startswith(".") or part in {"vendor", "_site", "utils"} for part in rel.parts):
            continue
        text = path.read_text()
        try:
            meta, body = frontmatter(text)
        except Exception as exc:
            errors.append(f"{rel}: invalid front matter: {exc}")
            continue
        if rel.as_posix() != "README.md" and not meta.get("title"):
            errors.append(f"{rel}: missing page title")
        pages[path] = body
        metadata[path] = meta
        fence = None
        for number, line in enumerate(body.splitlines(), 1):
            match = re.match(r"^\s{0,3}(`{3,}|~{3,})(.*)$", line)
            if match:
                marker, tail = match.groups()
                if fence is None:
                    fence = (marker, number)
                elif marker[0] == fence[0][0] and len(marker) >= len(fence[0]) and not tail.strip():
                    fence = None
        if fence:
            errors.append(f"{rel}: unclosed code fence near body line {fence[1]}")
        if body.count("{% raw %}") != body.count("{% endraw %}"):
            errors.append(f"{rel}: unbalanced Liquid raw delimiters")
    titles = {str(m.get("title")) for m in metadata.values()}
    for path, meta in metadata.items():
        for field in ["parent", "grand_parent"]:
            if meta.get(field) and str(meta[field]) not in titles:
                errors.append(f"{path.relative_to(root)}: unknown {field}: {meta[field]}")
    for path, body in pages.items():
        prose = outside_code(body, lambda line: line)
        # Remove fenced blocks while retaining ordinary prose and reference links.
        prose = re.sub(r"(?ms)^\s{0,3}(`{3,}|~{3,})[^\n]*\n.*?^\s{0,3}\1\s*$", "", prose)
        links = re.findall(r"!?\[[^\]\n]*\]\(([^)\n]+)\)", prose)
        links += re.findall(r'^\s*\[[^\]]+\]:\s*(\S+)', prose, re.M)
        for target in links:
            target = target.split(' "', 1)[0].strip("<>")
            parsed = urlsplit(target)
            if parsed.scheme or parsed.netloc or not parsed.path or "{{" in target:
                continue
            dest = (root / unquote(parsed.path).lstrip("/")) if parsed.path.startswith("/") else path.parent / unquote(parsed.path)
            options = [dest, dest.with_suffix(".md"), dest / "index.md"]
            if not any(candidate.exists() for candidate in options):
                errors.append(f"{path.relative_to(root)}: missing link {target}")
    return {"pages": len(pages), "errors": sorted(set(errors))}


class Document(HTMLParser):
    def __init__(self, text):
        super().__init__(convert_charrefs=True)
        self.ids, self.links = set(), []
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if "id" in attrs:
            self.ids.add(attrs["id"])
        if tag == "a" and "name" in attrs:
            self.ids.add(attrs["name"])
        for key in (["href"] if tag in {"a", "link"} else ["src"] if tag in {"img", "script", "iframe"} else []):
            if attrs.get(key):
                self.links.append(attrs[key])


def rendered_checks(site):
    site = site.resolve()
    documents = {path.resolve(): Document(path.read_text()) for path in site.rglob("*.html")}
    errors, count = [], 0
    for path, doc in documents.items():
        for link in doc.links:
            parsed = urlsplit(link)
            if parsed.scheme or parsed.netloc:
                continue
            count += 1
            dest = (site / unquote(parsed.path).lstrip("/")) if parsed.path.startswith("/") else path.parent / unquote(parsed.path)
            if not parsed.path:
                dest = path
            elif dest.is_dir():
                dest = dest / "index.html"
            elif not dest.exists() and not dest.suffix:
                dest = dest.with_suffix(".html")
            dest = dest.resolve()
            if not dest.exists():
                errors.append(f"{path.relative_to(site)}: missing rendered target {link}")
            elif parsed.fragment and dest in documents and unquote(parsed.fragment) not in documents[dest].ids:
                errors.append(f"{path.relative_to(site)}: missing rendered anchor {link}")
    return {"html_pages": len(documents), "local_links_checked": count, "errors": sorted(set(errors))}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--site", type=Path)
    parser.add_argument("--report", type=Path)
    args = parser.parse_args()
    report = {"markdown": markdown_checks(args.root.resolve())}
    if args.site:
        report["rendered"] = rendered_checks(args.site)
    if args.report:
        args.report.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))
    raise SystemExit(int(any(item["errors"] for item in report.values())))


if __name__ == "__main__":
    main()
