#!/usr/bin/env python3
"""Compile complete JavaScript fences without executing them.

Console transcripts and explicitly abbreviated snippets are counted separately.
This establishes syntax only, not API availability or runtime correctness.
"""
import argparse
import json
from pathlib import Path
import re
import subprocess
import tempfile

from sync_docs import ROOT


def collect(root):
    snippets, skipped = [], []
    for path in sorted((root / "docs").rglob("*.md")):
        text = path.read_text()
        for number, match in enumerate(re.finditer(r"(?ms)^(`{3,})(?:javascript|js)\s*\n(.*?)^\1\s*$", text)):
            code = match[2].replace("{% raw %}", "").replace("{% endraw %}", "")
            record = {"path": path.relative_to(root).as_posix(), "block": number,
                      "line": text[:match.start()].count("\n") + 1}
            if re.search(r"(?m)^\s*(?:>|openaf:|\| )", code):
                skipped.append(dict(record, reason="console transcript"))
            elif "..." in code:
                skipped.append(dict(record, reason="abbreviated snippet or spread syntax; manual review"))
            else:
                # The script launcher consumes the shebang before JS parsing.
                code = re.sub(r"\A#![^\n]*\n", "", code)
                snippets.append(dict(record, code=code))
    return snippets, skipped


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--jar", type=Path, required=True)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--report", type=Path)
    args = parser.parse_args()
    snippets, skipped = collect(args.root)
    with tempfile.TemporaryDirectory(prefix="openaf-doc-syntax-") as directory:
        work = Path(directory)
        data, runner = work / "snippets.json", work / "compile.js"
        data.write_text(json.dumps(snippets))
        runner.write_text('var results=[]; io.readFileJSON(__expr).forEach(r=>{try{new Function(r.code);}catch(e){delete r.code;r.error=String(e);results.push(r);}}); print(stringify(results));')
        proc = subprocess.run(["java", "-Duser.home=" + directory, "-jar", str(args.jar.resolve()),
                               "-f", str(runner), "-e", str(data)], cwd=work,
                              capture_output=True, text=True, timeout=60, check=True)
    report = {"compiled": len(snippets), "skipped": skipped, "errors": json.loads(proc.stdout)}
    if args.report:
        args.report.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({**report, "skipped": len(skipped)}, indent=2))
    raise SystemExit(int(bool(report["errors"])))
