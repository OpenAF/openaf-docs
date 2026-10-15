---
layout: default
title: OpenAF Processor (oafp) Reference Guide
parent: oafp
grand_parent: Guides
---

# OpenAF Processor (oafp) Reference Guide

`oafp` reads data, applies queries and transformations, and formats the result. Invoke the generated `oafp` launcher. Use `oafp -v` to inspect your runtime, `oafp help=usage` for its option reference, and `oafp in="?"` / `oafp out="?"` to discover formats.

The [complete usage reference](oafp-usage.md) is synchronized with the processor bundled in `20261014 nightly`. [Decisions and interactive exploration](october-features.md) provides worked examples for October additions.

## Convert and query data

```sh
# Convert a JSON array to YAML
echo '[{"name":"Alice","age":30},{"name":"Bob","age":20}]' | oafp in=json out=yaml

# Select names with JMESPath
echo '[{"name":"Alice","age":30},{"name":"Bob","age":20}]' | oafp in=json path='[?age > `21`].name' out=json
```

Use [filters](oafp-filters.md) for JMESPath, SQL, and nLinq processing, and [templates](oafp-template.md) for custom output. These query languages have different syntax and semantics; see [`$path`](../advanced/path-java.md) for the runtime backend and [`$jq`](../advanced/jq.md) for the separate JavaScript helper. `$jq` does not introduce an oafp jq CLI option.

## Compose an oJob

The `(oafp)` shortcut passes a map of processor parameters to the built-in `ojob oafp` job:

```yaml
todo:
- Process records

jobs:
- name: Process records
  from:
  - (oafp):
      in: slon
      data: "(a: 1, b: 2)"
      out: key
      __key: records
  exec: |
    var records = $get("records");
    print(stringify(records));
```

The example prints an object with `a: 1` and `b: 2`. `out=key` stores the result using the named key; ordinary output formats write output. See the [shortcut tutorial](../ojob/oafp-shortcut.md) for a larger example and the [oJob reference](../ojob/ojob-yaml-reference.md) for argument flow.

## Operational notes

Configured processor libraries can require optional oPacks. Confirm the installed help and libraries when comparing behavior between installations. Use scratch directories for file output, keep credentials in your model/secret configuration, and test provider or interactive-terminal features in their own environment.
