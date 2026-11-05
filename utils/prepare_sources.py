#!/usr/bin/env python3
"""Export pinned Git objects without modifying sibling worktrees or their refs."""
import argparse
import io
import json
from pathlib import Path
import subprocess
import tarfile

from sync_docs import MANIFEST, ROOT


def run(*args):
    return subprocess.check_output(args, stderr=subprocess.PIPE)


def prepare(siblings, output, fetch_missing=False):
    manifest = json.loads(MANIFEST.read_text())
    if output.exists() and any(output.iterdir()):
        raise ValueError("Output must be absent or empty; existing exports are never overwritten")
    output.mkdir(parents=True, exist_ok=True)
    for name, spec in manifest["repositories"].items():
        source, dest = siblings / name, output / name
        objects = Path(run("git", "-C", str(source), "rev-parse", "--git-path", "objects").decode().strip())
        if not objects.is_absolute():
            objects = (source / objects).resolve()
        dest.mkdir()
        run("git", "init", "--quiet", str(dest))
        (dest / ".git/objects/info/alternates").write_text(str(objects) + "\n")
        revision = spec["revision"]
        try:
            run("git", "-C", str(dest), "cat-file", "-e", revision + "^{commit}")
        except subprocess.CalledProcessError:
            if not fetch_missing:
                raise RuntimeError(f"{name}: missing {revision}; rerun into an empty output with --fetch-missing")
            run("git", "-C", str(dest), "fetch", "--quiet", "--depth=1",
                "https://github.com/" + spec["repository"] + ".git", revision)
        names = run("git", "-C", str(dest), "ls-tree", "-r", "--name-only", revision).decode().splitlines()
        # Package binary dependencies are unnecessary for documentation imports.
        if name == "openaf-opacks":
            extensions = {".md", ".yaml", ".yml", ".json", ".java", ".js", ".hbs", ".py", ".xml", ".sh"}
            names = [n for n in names if Path(n).suffix.lower() in extensions]
        archive = run("git", "-C", str(dest), "archive", revision, "--", *names)
        with tarfile.open(fileobj=io.BytesIO(archive)) as tar:
            # data filter rejects absolute paths and escaping symlinks.
            tar.extractall(dest, filter="data")
        (dest / ".source-revision").write_text(revision + "\n")
        print(f"{name}: {revision} ({len(names)} source files)")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--siblings", type=Path, default=ROOT.parent)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--fetch-missing", action="store_true")
    args = parser.parse_args()
    prepare(args.siblings.resolve(), args.output.resolve(), args.fetch_missing)
