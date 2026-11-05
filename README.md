# openaf-docs

![Concepts](.github/concepts.svg)
![Guides](.github/guides.svg)
![HowTo](.github/howto.svg)
![Reference](.github/reference.svg)

Documentation published at [docs.openaf.io](https://docs.openaf.io).

## Source baseline

The [public baseline page](docs/source-snapshot.md) records the upstream default-branch revisions covered by this refresh. [utils/source-map.json](utils/source-map.json) pins each repository and maps source files to their existing site URLs. Source availability and published stable/nightly availability are different; this repository does not publish OpenAF releases.

The refresh includes all core `docs/` guides and plugin guides, the five canonical oafp documents, all 25 oJob-common modules (120 jobs), a catalog of all 126 oPacks, 19 selected package README guides, and a JDBC integration guide. The API reference extracts 1,823 ODoc entries across 39 subjects from committed sources, including Markdown ODoc. The separate oJob YAML reference retains its existing URL.

[Review notes](utils/revision-audit.md) describe corrections, evidence and remaining integration limits. [The page inventory](utils/page-audit.json) includes every published Markdown page; it distinguishes imports, curated replacements, editorial revisions and retained pages. A matching API name is a retrieval aid, not proof that an example executes correctly.

## Prepare reproducible source exports

Requirements: Python 3.12+ with PyYAML, Git, and a Java 21+ OpenAF runtime for extracting ODoc and executing examples. The site build uses Ruby/Bundler and the locked gems.

```sh
python3 -m venv /tmp/openaf-docs-venv
. /tmp/openaf-docs-venv/bin/activate
pip install -r utils/requirements.txt
python3 utils/prepare_sources.py --siblings .. --output /tmp/openaf-docs-sources --fetch-missing
```

The output directory must be absent or empty. The exporter reads Git objects from sibling repositories and exports the pinned commits. It ignores dirty working trees and never updates sibling branches or refs. With `--fetch-missing`, it fetches missing commits into its own temporary repositories. Without that option, missing commits cause a clear failure. Binary oPack artifacts are omitted because documentation generation does not use them.

Do not edit exported source files. To advance the baseline, deliberately update the manifest revisions, prepare a fresh export and review the resulting changes. Each import correction must match its original text; stale corrections fail generation. Curated replacements for inaccurate upstream prose live under `utils/overrides/` and require review when their source changes.

## Regenerate documentation

From the documentation repository root:

```sh
python3 utils/sync_docs.py --sources /tmp/openaf-docs-sources --runtime /path/to/openaf.jar
python3 utils/gen_indexes.py
python3 utils/audit_docs.py
```

`--runtime` accepts an OpenAF executable or JAR. Reference generation loads the pinned `js/odoc.js` and `buildos.js` source mapping, never `searchHelp()` from an installed release. `--only imports`, `reference`, `catalog` or `jobs` limits generation; `--only imports --repository oafp` refreshes just the five processor documents. `--output /tmp/site-source` writes source-derived outputs to a separate root for review. It does not create a complete site checkout.

`utils/genReference.yaml` and `utils/genOAFP.yaml` are oJob entry points for the same generator. They now require `sources`; their `output` argument is a **site root**, not a reference/oafp subdirectory. Run them from this repository root. `ojob docs/guides/index.yaml` regenerates all nine guide sections. The old five-section Handlebars index template has been retired.

Check generated content without changing it:

```sh
python3 utils/sync_docs.py --sources /tmp/openaf-docs-sources --runtime /path/to/openaf.jar --check
python3 utils/gen_indexes.py --check
python3 utils/audit_docs.py --check
```

## Validate and preview

```sh
python3 -m unittest discover -s utils -p 'test_tooling.py' -v
python3 utils/check_docs.py
bundle install
bundle exec jekyll build --destination /tmp/openaf-docs-site
python3 utils/check_docs.py --site /tmp/openaf-docs-site --report /tmp/openaf-docs-links.json
python3 -m http.server 8000 --bind 127.0.0.1 --directory /tmp/openaf-docs-site
```

Open `http://127.0.0.1:8000`. The validator checks front matter, navigation parents, fences, Liquid delimiters, local Markdown targets, and rendered local links/anchors/assets. It does not establish availability of every external URL. The remote theme requires network access when Jekyll builds; gems are locked, while the site's existing remote-theme branch remains unchanged.

Use `BUNDLE_PATH` and `BUNDLE_APP_CONFIG` pointing at temporary directories when installing validation gems without changing your normal Bundler environment. Generated site files and caches are ignored by Git.

## Execute documented examples

For source-matched validation, build OpenAF from a **copy** of the frozen core export in a temporary directory, following its build instructions. Do not build over a dirty sibling checkout or replace an installed runtime. Supply the resulting JAR explicitly:

```sh
python3 utils/check_examples.py --jar /tmp/openaf-docs-runtime/openaf.jar --report /tmp/openaf-docs-syntax.json
python3 utils/test_examples.py --jar /tmp/openaf-docs-runtime/openaf.jar --report /tmp/openaf-docs-examples.json
python3 utils/test_mcp.py --jar /tmp/openaf-docs-runtime/openaf.jar --sources /tmp/openaf-docs-sources --report /tmp/openaf-docs-mcp.json
python3 /tmp/openaf-docs-sources/openaf/tools/docs/test_examples.py --jar /tmp/openaf-docs-runtime/openaf.jar --report /tmp/openaf-authoring.json
```

The syntax checker compiles complete JavaScript fences without executing them and lists skipped transcripts/abbreviated snippets separately. Runtime tests extract actual documentation fences, use temporary working directories, and exercise validation failures, ZIP, metrics, H2, graph/time-series persistence and the core-bundled processor. Processor tests disable extra `__flags.OAFP.libs` in their own process to avoid installed-user extension dependencies. The MCP test starts and stops a temporary HTTP server and requires loopback socket access; optional package installation is replaced by the frozen source export in that fixture.

The upstream authoring runner also uses local HTTP fixtures. Its Badgen integration is optional and requires the package; it is not silently installed. GUI, cloud/provider, native-library and external-service examples need their own environments. The pinned standalone oafp build refers to missing `src/include/inputLineFns.js`; this revision does not substitute an invented file or claim to have validated that build.

## Editing conventions

Keep existing page URLs and meaningful section anchors. Use `utils/source-map.json` for imported pages, `utils/overrides/` for the explicitly curated imports, and edit authored pages directly. Put Liquid `{% raw %}` / `{% endraw %}` outside code fences when examples contain Handlebars. Use repository-relative Markdown links so the Jekyll relative-links plugin can produce correct URLs.

Refresh the existing `.github` counters with `.github/ojobs/updateCounters.yaml` when the Badgen dependency is available; counts exclude section index pages. The existing external oafp example-catalog workflow is separate from the pinned development-source imports. None of the local validation commands commits, pushes, deploys or publishes the site.
