# Documentation revision audit — 5 November 2026

## Scope and provenance

The baseline is the four upstream default-branch commits in [source-map.json](source-map.json). Local sibling branch heads, staged changes and untracked files were excluded. The source exporter was exercised against a second fresh export; generation from that export produced no drift.

The original repository contained 294 Markdown files: 293 published pages and the contributor README. This revision inventories all 345 resulting published pages, including 52 new pages. The page-level inventory in [page-audit.json](page-audit.json) records disposition, provenance, API-name hints and content hashes. Every page receives structure/link checks. Retained pages were screened, not individually integration-tested.

Coverage includes:

- 85 mapped source-document imports, including two curated replacements and explicit corrections to inaccurate source prose.
- 16 copied source/example files and the rendered annotated oJob YAML catalog.
- 39 ODoc subjects with 1,823 API entries, extracted from the committed source mapping. Existing API URLs remain in place; Markdown ODoc is rendered as Markdown.
- All five canonical oafp development documents, with the core-bundled processor documented separately.
- All 25 oJob-common modules and 120 job names. The README reference is supplemented by the complete module inventory.
- All 126 package manifests, 19 focused package README guides, and a JDBC guide. Packages without a README link directly to their manifest.
- All nine guide sections in navigation, refreshed counters, source-baseline notices, local-link repairs and compatibility anchors for replaced sections.

## Substantive corrections

| Area | Evidence and resulting change |
| --- | --- |
| Validation | `js/openafsigil.js`: removed nonexistent `match`, `inRange`, `isEmail`, length and key helpers; terminal calls now return converted values. Documented the implementation's grouped-check behavior, inverted equality/UUID checks, non-returning range helpers and broken prefix helpers. Combined predicates are tested on success and failure. |
| Sigil | The source defines `$$` / `_$`, not the macro engine described by the former upstream guide. Replaced invented `$sigil`, tag and filter APIs with actual environment, template, object-path and validation APIs. |
| MCP | `oJobMCP.yaml` / `owrap.server.js`: corrected port configuration and explicit HTTP startup, tested real tool dispatch, documented authentication and HTTP/STDIO result conversion, replaced incorrect REST response handling and clarified error results. |
| Metrics | `owrap.metrics.js`: callback registration, array-valued metric selection, collector/channel lifecycle and the strict OpenMetrics argument now match the implementation. |
| Plugins / databases | Corrected HTTP server loading, optional XLS/Ignite requirements, SSH lifecycle, ZIP byte input, JDBC loaders and H2 examples. Fixed metadata method spelling. |
| Older examples | Repaired JavaScript syntax, SQL template calls, MongoDB calls, digest spelling, IPv6 flags, Windows JVM options, Java version/path guidance, kubectl resource syntax, shell quoting and obsolete external-demo dependencies. |
| Source imports | Recorded corrections for GitHub/Kramdown anchor differences, invalid reference snippets, missing upstream test paths and stale helper names. Curated imports are labelled explicitly. |
| Rendering | Balanced Liquid raw blocks and code fences, corrected languages for signatures/data fragments, repaired navigation parents and regenerated all section indexes. |

## Validation evidence

[validation-summary.json](validation-summary.json) records the final results and source-matched runtime fingerprint. Reproduction commands are in the [contributor README](../README.md).

- Built OpenAF from a temporary copy of pinned core source using Java 27. The generated JAR reports `20261105`; that is a build stamp, not a newly published stable release. JAR SHA-256: `50084e58f13c09b2a2abf08aebfb4c49c74cf90a9098166f71ddae601034bfe6`.
- Upstream authoring runner: 13 passed, 1 optional Badgen integration skipped.
- Documentation runtime fixtures: 11 passed, including validation rejection, ZIP roundtrip, metrics, H2, graph/time-series persistence and core-bundled jq/H2 processor cases.
- Documentation MCP fixture: 4 checks passed over an ephemeral local HTTP port. Upstream MCP notification suite: 18 checks, 0 failures.
- JavaScript syntax: 851 complete fences compiled. 267 transcripts or abbreviated/spread-containing snippets were listed separately; syntax checks do not establish runtime correctness.
- Tooling regression tests: 4 passed. Source exports, generator check mode, oJob reference wrapper and index regeneration were exercised.
- Jekyll rendered 345 HTML pages. Local rendered targets and anchors were crawled; final counts are in the summary. Desktop browser inspection covered the homepage, package catalog and a Markdown API-reference page, including tables, navigation and code blocks.

## Limits and upstream follow-up

1. The standalone oafp source build references absent `src/include/inputLineFns.js`. No replacement was fabricated. Processor runtime checks cover the explicitly identified core-bundled implementation; the standalone development documentation is source-reviewed.
2. oJob-common's README references absent `tests/openmetrics.js`. The imported page identifies this discrepancy instead of advertising that command as runnable. Available MCP regression tests and direct core OpenMetrics fixtures were used.
3. Runtime helper defects remain upstream. The site documents workarounds and records corrections in its manifest; it does not alter any sibling runtime or repository.
4. Cloud/provider credentials, optional native packages, GUI behavior, remote ojob.io jobs, nAttrMon and every external URL were not integration-tested. Their prerequisites and scope remain explicit. The package catalog reflects manifest declarations, including old metadata, rather than claiming every package was built or installed.
5. The installed remote-theme branch remains as configured. Gem versions are locked; content generation is deterministic, while a future remote-theme change can affect rendering.

No changes were committed, pushed or published. The four sibling working-tree states were checked against their initial snapshots.
