#!/usr/bin/env python3
"""Generate source-derived documentation from explicit, pinned source exports.

Requires PyYAML. Sources are directories named as in source-map.json, each with
a .source-revision file. Never reads installed help or changes a source checkout.
"""
import argparse
import html
import json
from pathlib import Path
import posixpath
import re
import subprocess
import tempfile
from urllib.parse import unquote, urlsplit

import yaml

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "utils/source-map.json"


def frontmatter(text):
    match = re.match(r"\A---\n(.*?)\n---\n", text, re.S)
    return (yaml.safe_load(match[1]) or {}, text[match.end():]) if match else ({}, text)


def outside_code(text, fn):
    result, fence = [], None
    for line in text.splitlines(keepends=True):
        marker = re.match(r"^\s{0,3}(`{3,}|~{3,})", line)
        if marker:
            token = marker[1]
            if fence is None:
                fence = token
            elif token[0] == fence[0] and len(token) >= len(fence):
                fence = None
            result.append(line)
        else:
            result.append(line if fence else fn(line))
    return "".join(result)


def source_url(manifest, repo, path, image=False):
    data = manifest["repositories"][repo]
    base = "https://raw.githubusercontent.com" if image else "https://github.com"
    middle = "" if image else "/blob"
    return f'{base}/{data["repository"]}{middle}/{data["revision"]}/{path}'


def rewrite_links(text, repo, source, destination, manifest):
    mapping = {}
    for item in manifest["imports"] + manifest["copies"]:
        mapping.setdefault((item["repository"], item["source"]), item["destination"])
    mapping[("openaf", "docs/index.md")] = "docs/guides/index.md"
    mapping[("openaf", "README.md")] = "index.md"

    def replace(match):
        prefix, target, suffix = match.groups()
        target = target.strip()
        title = ""
        if ' "' in target:
            target, title = target.split(' "', 1)
            title = ' "' + title
        parsed = urlsplit(target.strip("<>"))
        if parsed.scheme or parsed.netloc or parsed.path.startswith("/"):
            return match[0]
        path = posixpath.normpath(posixpath.join(posixpath.dirname(source), unquote(parsed.path))) if parsed.path else source
        if not parsed.path:
            link = ""
        elif (repo, path) in mapping:
            link = posixpath.relpath(mapping[(repo, path)], posixpath.dirname(destination))
        else:
            link = source_url(manifest, repo, path, prefix.startswith("!"))
        if parsed.query:
            link += "?" + parsed.query
        if parsed.fragment:
            # Upstream GitHub fragment spelling can differ from Kramdown IDs.
            fragment = manifest.get("anchor_corrections", {}).get(parsed.fragment, parsed.fragment)
            link += "#" + fragment
        return prefix + link + title + suffix

    return outside_code(text, lambda line: re.sub(r"(!?\[[^\]\n]*\]\()([^\)\n]+)(\))", replace, line))


def page(title, parent, body, grand="Guides", extra=None):
    meta = {"layout": "default", "title": title, "parent": parent}
    if grand:
        meta["grand_parent"] = grand
    if extra:
        meta.update(extra)
    # These source documents do not contain Liquid raw delimiters. Fail rather
    # than silently corrupt an upstream document if this changes.
    if "{% endraw" in body or "{% raw" in body:
        raise ValueError("Source contains raw delimiters; escape them explicitly before import")
    return "---\n" + yaml.safe_dump(meta, sort_keys=False, allow_unicode=True) + "---\n\n{% raw %}\n" + body.strip() + "\n{% endraw %}\n"


def cell(value):
    return html.escape(str(value), quote=False).replace("|", "&#124;").replace("\n", " ")


def generate_imports(sources, manifest, output, repository=None):
    generated = {}
    for item in manifest["imports"]:
        if repository and item["repository"] != repository:
            continue
        source = sources / item["repository"] / item["source"]
        text = source.read_text()
        destination = item["destination"]
        existing = ROOT / destination
        old, _ = frontmatter(existing.read_text()) if existing.exists() else ({}, "")
        first = re.search(r"^# (.+)$", text, re.M)
        title = item.get("title", old.get("title", first[1] if first else source.stem))
        for correction in item.get("corrections", []):
            if correction["old"] not in text:
                raise ValueError(f"Stale source correction in {destination}: {correction['old']}")
            text = text.replace(correction["old"], correction["new"])
        if item.get("body_file"):
            text = (ROOT / item["body_file"]).read_text()
        else:
            text = rewrite_links(text, item["repository"], item["source"], destination, manifest)
        origin = source_url(manifest, item["repository"], item["source"])
        revision = manifest["repositories"][item["repository"]]["revision"][:8]
        note = f'> Source: [{item["repository"]} `{revision}`]({origin}). See [documentation baseline]({posixpath.relpath("docs/source-snapshot.md", posixpath.dirname(destination))}) for availability and verification.\n\n'
        if item.get("body_file"):
            note += "> This page is curated against the implementation to correct discrepancies in the upstream prose.\n\n"
        if item["repository"] == "openaf-opacks":
            note += "> Build and test commands use the package's source directory; installation and library examples use the installed oPack.\n\n"
        if item.get("legacy_anchors"):
            note += "<!-- Preserve earlier section bookmarks. -->\n" + "\n".join(
                '<a id="' + html.escape(anchor, quote=True) + '"></a>' for anchor in item["legacy_anchors"]) + "\n\n"
        generated[destination] = page(title, item["parent"], note + text, item.get("grand_parent", "Guides"))
    for item in manifest["copies"]:
        if repository and item["repository"] != repository:
            continue
        generated[item["destination"]] = (sources / item["repository"] / item["source"]).read_text()
    if repository and repository != "openaf":
        return generated
    syntax = (sources / "openaf/docs/ojob-all.yaml").read_text()
    generated["docs/guides/cheat-sheet/ojob-all.md"] = page("oJob reference", "cheat-sheet",
        "# oJob reference\n\nThe annotated syntax below follows the [source baseline](../../source-snapshot.md). "
        "It illustrates configuration options and is not a runnable job. Use `ojob -syntax` for your installed runtime.\n\n"
        "[Download the YAML reference](../../examples/ojob-all.yaml). See the [oJob guide](../ojob/ojob-yaml-reference.md) for explanations.\n\n"
        "## Reference\n\n```yaml\n" + syntax.rstrip() + "\n```\n")
    return generated


def generate_reference(sources, manifest, runtime):
    with tempfile.TemporaryDirectory(prefix="openaf-reference-") as tmp:
        config, result = Path(tmp) / "config.json", Path(tmp) / "reference.json"
        config.write_text(json.dumps({"source": str(sources / "openaf"), "output": str(result)}))
        command = (["java", "-jar", str(runtime)] if str(runtime).endswith(".jar") else [str(runtime)])
        subprocess.run(command + ["-f", str(ROOT / "utils/exportReference.js"), "-e", "config=" + str(config)], check=True,
                       stdout=subprocess.DEVNULL)
        data = json.loads(result.read_text())
    generated, keys = {}, {}
    rev = manifest["repositories"]["openaf"]["revision"][:8]
    index = f"# Reference\n\nGenerated from OpenAF `{rev}` source ODoc entries, including Markdown-formatted entries. [Source baseline](../source-snapshot.md).\n\n"
    for subject, entries in sorted(data["docs"].items()):
        if subject == "index":
            continue
        filename = subject.replace(".", "_") + ".md"
        destination = "docs/reference/" + filename
        source = Path(data["subjects"][subject]).relative_to(sources / "openaf").as_posix()
        body = f"## {subject}\n\n[Source: `{rev}`]({source_url(manifest, 'openaf', source)}) · [Baseline](../source-snapshot.md)\n\n"
        keys[subject] = []
        for key, entry in sorted(entries.items()):
            keys[subject].append(key)
            body += "### " + key + "\n\n`" + entry["k"].replace("`", "'") + "`\n\n"
            text = entry["t"]
            text = re.sub(r"(?m)^[ \t]+", lambda match: match[0].expandtabs(4), text)
            corrections = manifest.get("reference_corrections", {}).get(subject, {}).get(key, [])
            for correction in corrections:
                if correction["old"] not in text:
                    raise ValueError(f"Stale reference correction: {subject}/{key}")
                text = text.replace(correction["old"], correction["new"])
            if corrections:
                body += "> Example formatting/syntax corrected against the implementation; the signature is unchanged.\n\n"
            if entry.get("format") == "markdown":
                # Keep entry headings below the API heading in the site TOC.
                text = outside_code(text, lambda line: re.sub(r"^(#{1,6}) ", lambda m: "#" * min(6, len(m[1]) + 3) + " ", line))
                body += text.strip() + "\n\n"
            else:
                longest = max([len(x) for x in re.findall(r"`+", text)] + [3])
                fence = "`" * (longest + 1)
                body += fence + "text\n" + text.strip() + "\n" + fence + "\n\n"
        generated[destination] = page(subject, "Reference", body, "OpenAF docs")
        index += f"- [{subject}]({filename}) — {len(entries)} entries\n"
    generated["docs/reference/index.md"] = page("Reference", "OpenAF docs", index, None,
                                                      {"has_children": True, "nav_order": 4})
    generated["utils/reference-keys.json"] = json.dumps(keys, indent=2) + "\n"
    return generated


def package_group(directory):
    if directory.startswith("jdbc-"):
        return "JDBC drivers"
    if directory in {"AWS", "GCP", "GCS", "S3", "Kube", "Docker", "DockerRegistry", "OpenAFLambda", "OpenAFLambdaLayers", "ScaleWay", "BunnyNet"}:
        return "Cloud and infrastructure"
    if directory in {"OpenAI", "ghcopilot", "MCPAuthd", "OpenAPI", "GPU", "lucene", "FalkorDB"}:
        return "AI, APIs and computation"
    if directory.startswith("plugin-") or directory in {"D3SVG", "XChart", "Mermaid", "KaTeX", "jexer", "lanterna", "inBrowser", "Mac", "Robot", "playwright"}:
        return "Plugins, interfaces and visualization"
    if directory in {"Redis", "Mongo", "Kafka", "Tika", "Avro", "Parquet", "rocksdb", "etcd3", "cq", "CHManager", "oafproc", "ElasticSearch"}:
        return "Data, files and channels"
    return "Automation and utilities"


def generate_catalog(sources, manifest):
    root = sources / "openaf-opacks"
    packages = []
    guides = {x["source"].split("/")[0]: Path(x["destination"]).name
              for x in manifest["imports"] if x["repository"] == "openaf-opacks"}
    for path in sorted(root.glob("*/.package.*")):
        if path.suffix not in {".yaml", ".json"}:
            continue
        data = yaml.safe_load(path.read_text())
        packages.append((path.parent.name, data, path.relative_to(root).as_posix()))
    body = f"# oPack catalog\n\nThis catalog covers **{len(packages)} packages** in the [pinned upstream snapshot](../../source-snapshot.md). Package names and requirements come from their manifests. Install with `opack install <name>` and load the documented entry point; an installation does not automatically load every library.\n\n"
    body += "Versions below identify source package metadata, not a guarantee that a package mirror has published that revision. Requirements are the declared package dependencies; linked guides describe extra services, native libraries and credentials. A source/manifest link means no root README is available.\n\n"
    body += "For package management see [oPacks](../advanced/opacks.md). For database connections see [JDBC drivers](jdbc-drivers.md) and [JDBC URL policy](../advanced/jdbc-url-policy.md).\n\n"
    records = []
    for group in sorted({package_group(p[0]) for p in packages}):
        body += f"## {group}\n\n| Package / install | Purpose | Version / declared requirements | Documentation |\n| --- | --- | --- | --- |\n"
        for directory, data, manifest_path in packages:
            if package_group(directory) != group:
                continue
            readme = directory + "/README.md"
            has_readme = (root / readme).exists()
            link = f'[{"README" if has_readme else "Source / manifest"}]({source_url(manifest, "openaf-opacks", readme if has_readme else manifest_path)})'
            if directory in guides:
                link = f'[Guide]({guides[directory]}) · ' + link
            deps = "; ".join(f"{k} {v}" for k, v in (data.get("dependencies") or {}).items()) or "No package dependencies declared"
            name = str(data["name"])
            body += f'| **{cell(name)}**<br>`opack install {cell(name)}` | {cell(data.get("description", ""))} | `{cell(data.get("version", ""))}`<br>{cell(deps)} | {link} |\n'
            records.append({"directory": directory, "name": name, "manifest": manifest_path, "has_readme": has_readme, "guide": guides.get(directory)})
        body += "\n"
    return {"docs/guides/opacks/catalog.md": page("oPack catalog", "oPacks", body),
            "utils/package-catalog.json": json.dumps(sorted(records, key=lambda x: x["directory"]), indent=2) + "\n"}


def generate_jobs(sources, manifest):
    root = sources / "ojob-common"
    body = """# oJob-common module index

OpenAF provides built-in lowercase `ojob …` jobs through `ojob.yaml` / `includeOJob: true`. The **oJob-common** oPack supplies the modules below, normally containing `oJob …` jobs. Include only the modules your workflow needs. See the [job reference](ojob-common-reference.md) for arguments and examples.

```yaml
ojob:
  opacks:
    oJob-common: ">=20261030"
include:
- oJobBasics.yaml
todo:
- name: oJob Print args
  args:
    message: Hello
```

"""
    inventory = []
    for path in sorted(root.glob("*.yaml")):
        if path.name.startswith("."):
            continue
        data = yaml.safe_load(path.read_text()) or {}
        jobs = data.get("jobs", [])
        body += f'## {path.stem}\n\n[Source definition]({source_url(manifest, "ojob-common", path.name)}). '
        if data.get("include"):
            body += "Includes: " + ", ".join("`" + str(x) + "`" for x in data["include"]) + ". "
        body += "\n\n"
        if jobs:
            body += "| Job | Description from source help |\n| --- | --- |\n"
        for job in jobs:
            help_ = job.get("help", "")
            if isinstance(help_, dict):
                help_ = help_.get("text", "")
            description = str(help_).strip().split("\n")[0] if help_ else "See source definition and its argument checks."
            body += "| `" + cell(job["name"]) + "` | " + cell(description) + " |\n"
        inventory.append({"module": path.name, "jobs": [j["name"] for j in jobs]})
        body += "\n"
    return {"docs/guides/ojob/ojob-common-modules.md": page("oJob-common modules", "oJob", body),
            "utils/job-catalog.json": json.dumps(inventory, indent=2) + "\n"}


def write_outputs(generated, output, check):
    stale = []
    for filename, content in sorted(generated.items()):
        if filename.endswith(".md") or filename == "docs/examples/ojob-all.yaml":
            content = "\n".join(line.rstrip() for line in content.splitlines()) + "\n"
        path = output / filename
        if not path.exists() or path.read_text() != content:
            stale.append(filename)
            if not check:
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(content)
    print(json.dumps({"generated_files": len(generated), "changed_files": stale}, indent=2))
    return bool(stale)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--sources", type=Path, required=True)
    parser.add_argument("--output", type=Path, default=ROOT)
    parser.add_argument("--runtime", default="oaf", help="OpenAF executable or JAR; used only to parse pinned ODoc source")
    parser.add_argument("--only", choices=["imports", "reference", "catalog", "jobs", "all"], default="all")
    parser.add_argument("--repository", help="Limit --only imports to one repository")
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    manifest = json.loads(MANIFEST.read_text())
    if args.repository and (args.only != "imports" or args.repository not in manifest["repositories"]):
        parser.error("--repository requires --only imports and a repository from source-map.json")
    sources = args.sources.resolve()
    for name, spec in manifest["repositories"].items():
        revision = (sources / name / ".source-revision").read_text().strip()
        if revision != spec["revision"]:
            parser.error(f"Source revision mismatch for {name}: {revision}")
    generated = {}
    if args.only in {"imports", "all"}:
        generated.update(generate_imports(sources, manifest, args.output, args.repository))
    if args.only in {"reference", "all"}:
        generated.update(generate_reference(sources, manifest, args.runtime))
    if args.only in {"catalog", "all"}:
        generated.update(generate_catalog(sources, manifest))
    if args.only in {"jobs", "all"}:
        generated.update(generate_jobs(sources, manifest))
    changed = write_outputs(generated, args.output, args.check)
    raise SystemExit(1 if args.check and changed else 0)


if __name__ == "__main__":
    main()
