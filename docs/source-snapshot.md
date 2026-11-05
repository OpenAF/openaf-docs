---
layout: default
title: Documentation baseline
parent: OpenAF docs
nav_order: 5
---

# Documentation baseline

This revision describes the upstream default branches checked on **5 November 2026**. It documents source behavior; it does not announce a stable release or imply that every package mirror already contains these changes.

| Source | Branch | Revision |
| --- | --- | --- |
| [OpenAF](https://github.com/OpenAF/openaf) | `master` | [06414cd9](https://github.com/OpenAF/openaf/commit/06414cd9204e918daa1e2971ce904783299db333) |
| [oJob-common](https://github.com/OpenAF/oJob-common) | `master` | [130addf4](https://github.com/OpenAF/oJob-common/commit/130addf46fb52ca733da6a66bf7b990430006caf) |
| [oafp](https://github.com/OpenAF/oafp) | `main` | [35a922f9](https://github.com/OpenAF/oafp/commit/35a922f9cc218a31f032e6c95e1c743a24a7fd68) |
| [openaf-opacks](https://github.com/OpenAF/openaf-opacks) | `master` | [87b07e97](https://github.com/OpenAF/openaf-opacks/commit/87b07e9774902bccee8bf16632201e319dcfca0d) |

Check the runtime and processor you actually use:

```sh
oaf -c 'print(getVersion()); print(getDistribution());'
oafp -v
oafp help=usage
opack list
```

The OpenAF distribution bundles an oafp implementation. The `oafp` development repository and the `oafproc` oPack have separate update histories. The [usage](guides/oafp/oafp-usage.md), [filters](guides/oafp/oafp-filters.md), [templates](guides/oafp/oafp-template.md), [examples](guides/oafp/oafp-basic-examples.md), and [JSON Schema guide](guides/oafp/json-schemas.md) follow the pinned **oafp development source**. Check installed help before using a newly documented option. The [core processor overview](guides/oafp/oafp-reference.md) follows the OpenAF source snapshot.

## Changes covered by this revision

- [Graph channels](guides/advanced/channel-graph.md) and [time-series channels](guides/advanced/channel-timeseries.md): persistence, backing channels, retention, traversal, metrics and queries.
- [Desktop windows and terminal views](guides/advanced/desktop.md), the optional [JavaFX provider](guides/opacks/plugin-desktopjavafx.md), and the [screen reference](reference/ow_screen.md).
- [LLM decisions](guides/advanced/llm-decisions.md), [provider APIs](guides/advanced/ow-ai-gpttypes.md), [schema output](guides/advanced/openai-schema-hooks.md), and [MCP authentication](guides/advanced/mcp-oauth.md).
- [JDBC execution policy](guides/advanced/jdbc-url-policy.md), [Jakarta XML Binding migration](guides/advanced/jakarta-xml-binding-migration.md), CLI and console improvements, and Markdown-aware [ODoc](guides/advanced/odoc.md).
- [oJob-common modules](guides/ojob/ojob-common-modules.md), including HTTP/REST metrics, file-browsing restrictions, MCP authorization, file operations and watchdog behavior.
- The corrected oafp query pipeline, streaming semantics, DSV, Base64, HTTP input/output, map comparison, charts and shell completion.
- The [complete oPack catalog](guides/opacks/catalog.md), with focused guides for Lambda/MicroVM, gRPC, AWS, AI providers, observability, data integrations and desktop tools.

The [October snapshot](guides/advanced/october-2026.md) remains available as historical context. Follow current topic guides for current contracts.

## How to interpret examples

Guides identify required libraries, external services and credentials where relevant. Commands that deploy resources, modify databases or manage system services require a suitable test environment and deliberate configuration. Source review and local fixture tests do not establish provider account access, production readiness, GUI behavior or support on every operating system.

Examples involving nAttrMon, the remote ojob.io catalog or other repositories retain their own upstream requirements. Their external implementations are outside these four source snapshots.

The repository's contributor README explains how to reproduce imports, reference generation, link checks and the site build. Source mappings and review evidence are maintained under `utils/`.

## Source discrepancies handled here

Some upstream prose describes APIs that are absent or behave differently in the implementation. The [core overview](guides/advanced/openaf-reference.md), [Sigil guide](guides/advanced/sigil.md) and [validation guides](guides/medium/parameter-validation.md#snapshot-compatibility) contain reviewed corrections. The [MCP guide](guides/ojob/build-mcp-server.md#tool-result-conversion) distinguishes HTTP and STDIO result conversion. These are documentation corrections; the upstream runtimes have not been changed by this site revision.

The pinned standalone oafp build references a missing `src/include/inputLineFns.js`. Its development-source documentation is included, but the local processor smoke tests use the processor bundled in the pinned OpenAF build. Cloud, native GUI and external-service examples remain dependent on their own environments.
