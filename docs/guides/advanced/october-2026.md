---
layout: default
title: "October 2026 source updates"
parent: Advanced
grand_parent: Guides
---

# October 2026 source updates

This refresh covers changes after `v20260728` through [OpenAF commit a5181af6](https://github.com/OpenAF/openaf/commit/a5181af6). The local JAR identifies itself as `20261014 nightly`; the committed version is `20261011` with a pending version bump. These pages document that source snapshot, without claiming a new stable release or historical compatibility for the new APIs. Check your installed version with `openaf -c 'print(getVersion());'`.

## AI and MCP

* [Stateless LLM decisions](llm-decisions.md) add `decide`, `rawDecide`, `decideWithStats`, and `getCapabilities` to `$llm`/`$gpt` and `ow.ai.gpt`. Named choice, boolean, and ordinal score questions return validated results. Native and structured strategies have different probability capabilities; failed requests never cause an automatic provider or strategy fallback.
* Native adapters include Ollama System One and explicit OpenAI, OpenRouter, and Microsoft Foundry contracts. [Adapter records](llm-decisions-contracts.md) distinguish synthetic fixtures from live inference. Foundry System One requires `decisionApi: "microsoft"`; deployment names and endpoints remain caller configuration.
* [JSON Schema output](llm-decisions.md#gemini-conversational-schema-output) now includes Gemini's provider-specific schema hook. [Provider wrappers](ow-ai-gpttypes.md) describe transport and usage reporting. Anthropic prompt caching uses cache-control markers without the previous beta header.
* [Localhost OAuth2](mcp-oauth.md) supports PKCE browser callbacks, credential refresh, and protected token storage. `$mcp` persistence remains opt-in. The [MCP reference](../../reference/scope.md#mcp) adds stdio working-directory/environment controls and opt-in modern protocol negotiation with `protocolVersion: "auto"`; existing callers keep the legacy handshake default.

## Queries, files, and interactive tools

* [`$jq`](jq.md) evaluates jq 1.6 syntax in the JVM, with variable binding and explicit zero/one/multiple-output handling. It collects results in memory and is independent of `$path` and `$from`.
* [`$path` now defaults to a Java engine](path-java.md), preserving OpenAF extension functions and custom callbacks. Set `__flags.ALTERNATIVES.path = false` to use the bundled JavaScript backend. Evaluation failures are propagated without retrying another backend.
* [`joniRegExp`](joni.md) provides reusable Oniguruma patterns, named captures, replacement, and splitting alongside existing regex helpers.
* [JSON extraction and independent-terminal prompts](json-extraction-and-prompts.md) introduce `io.scanJSON`, `io.copyJSONRange`, `io.extractJSON`, and `askConsole`. Stream extraction has explicit ownership, cancellation, and partial-output semantics.
* [oafp decisions and interactive JSON exploration](../oafp/october-features.md) cover decision input/enrichment and loaded or file-backed browsing. See the refreshed [oafp reference](../oafp/oafp-reference.md) for the wider processing pipeline.

## Authoring and operations

* Follow [From an OpenAF script to an oJob](../ojob/script-to-ojob.md), then [authoring recipes](../ojob/authoring-recipes.md) and [testing and troubleshooting](../ojob/authoring-testing.md). Downloadable examples cover files, local HTTP, processes, bounded workers, scheduling, and cleanup.
* The [oJob reference](../ojob/ojob-yaml-reference.md) clarifies argument sharing, interpolation, built-in jobs, language processes, and `-exportcode`/`-importcode`. Inspection commands load dependencies and are not plain YAML parsers.
* [Python integration](python-integration.md) documents subprocess/fork behavior, exception propagation, Python argv, and bidirectional bridge lifecycle. Updated reference signatures retain earlier calling forms.
* [JSON Schema validation](json-schema.md) covers draft selection, references, schema generation, and migration from bundled Ajv v6. [`$` helpers](openaf-dollar-functions.md) cover synchronization, process handling, and cleanup. Updated [concurrency references](../../reference/scope.md#pforeach) document timeouts and worker options.
* [Instrumentation](instrumentation.md) is opt-in: loading the module alone enables no capture. Providers can collect spans, logs, and metrics through bounded channels or forwarding.
* [Console and CLI](console.md) documentation covers JLine-backed interaction and terminal sizing with piped input. [CDS repacking](cds.md) validates archives before replacement and provides coverage fallbacks. [JavaScript compilation](native-compilation.md) handles large scripts with generated shards while preserving the existing loading interfaces.

The API refresh also covers channel destruction, server locks, ANSI width helpers, DB statement options, ZIP resource cleanup, and [offline help/Markdown docstrings](odoc.md). Start from the [reference navigation](../../reference/index.md) for exact signatures.

## Verification boundaries

Examples requiring provider accounts, model downloads, optional oPacks, a real interactive terminal, or platform-specific behavior require their own environment. Source contracts and local fixture checks do not establish live provider access, Windows behavior, or production deployment results.
