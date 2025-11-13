---
layout: default
title: SLON format
parent: Concepts
nav_order: 99
---

# SLON format

[SLON](https://github.com/nmaguiar/slon) (Single Line Object Notation) is a lightweight data serialization format designed to
compress JSON-like structures into a concise, human-readable syntax. It keeps the familiar concepts of maps and arrays while
trimming unnecessary characters, making it easier to scan large payloads in logs or share configuration snippets inline.

## Why SLON?

* **Compact syntax** – Braces and commas are optional when the structure is unambiguous, allowing records to fit on a single
  line without sacrificing readability.
* **JSON-compatible** – Every SLON document can be converted to JSON and vice versa, enabling quick interchange between
  OpenAF helpers that expect JSON and those that accept SLON.
* **Human-friendly defaults** – Strings can be quoted only when needed, and key-value pairs rely on `:` separators, so editing
  data by hand is straightforward.

## Working with SLON in OpenAF

OpenAF includes multiple helpers to convert data back and forth between JSON and SLON:

* `AF.toSLON()` / `AF.toCSLON()` – render maps or arrays to SLON (optionally with ANSI colors for terminals).
* `AF.fromSLON()` / `AF.fromJSSLON()` – parse SLON strings back into OpenAF objects.
* `$toSLON`, `$cslon`, `$oafp` – templating helpers that emit or parse SLON documents inline.

Because SLON is interchangeable with JSON, documentation frequently mentions parameters that accept "JSON/SLON" values. You can
freely decide which notation is more convenient for you, and OpenAF will transparently parse the data.

For complete syntax details and reference implementations, visit the [SLON GitHub repository](https://github.com/nmaguiar/slon).
