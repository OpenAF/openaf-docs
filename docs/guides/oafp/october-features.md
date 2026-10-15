---
layout: default
title: "Decisions and interactive JSON exploration"
parent: oafp
grand_parent: Guides
---

# Decisions and interactive JSON exploration

These features are present in the October OpenAF source snapshot. They require a matching runtime; use `oafp -v` and `oafp help=usage` to inspect your installed processor.

## Stateless decisions

`in=llmdecide` evaluates one complete state, including an array, against named questions. Supply a JSON, YAML, or SLON document containing `{state, questions, options?}`. Generate an editable request without credentials or inference:

```sh
oafp in=llmdecide llmdecidesample=gemini out=yaml > request.yaml
# Edit request.yaml, configure your provider, then execute:
oafp in=llmdecide file=request.yaml out=json
```

Model configuration comes from `OAFP_MODEL`, then `OAF_DECIDE_MODEL`, then `OAF_MODEL` when the preceding variable is absent. `llmoptions` supplies an explicit configuration instead. `llmdecidestats=true` returns `{response, stats}` from the same execution. Normal output filters apply; with statistics, answer paths start at `response.answers`.

The `llmdecide` **transform** instead evaluates each input entry. For example, save this as `classify.yaml`:

```yaml
questions:
  urgent:
    type: boolean
    instructions: Does this describe a service outage?
statePath: description
assign:
  urgent: answers.urgent.value
```

```sh
echo '[{"id":1,"description":"The API fails on every request"}]' | oafp llmdecide=classify.yaml out=json
```

Without `assign`, output consists of decision envelopes. With `assign`, destination fields map to `$path` expressions over each envelope and the original entry is copied. Existing destination fields fail unless the configuration explicitly sets `overwrite: true`. `statePath` selects each entry's text, object, or array state. Empty input arrays require no inference. `parallel=true` permits concurrent calls and should be chosen with provider limits in mind.

See [LLM decisions](../advanced/llm-decisions.md) for question types, native versus structured strategies, image formats, and probability semantics. Failures propagate without automatic provider/model/strategy fallback. Samples do not establish account access or model availability.

## Interactive JSON exploration

```sh
oafp file=records.json out=idesc
oafp file=large.json in=json out=idesc idescsource=stream
```

The default `idescsource=loaded` explores the in-memory result after normal input processing. `idescsource=stream` uses a file-backed UTF-8 JSON source with bounded previews, narrowing, bookmarks, and export. It avoids materializing the complete JSON value, but scanning still reads source bytes and remote or piped input may need a temporary local file.

Stream mode accepts JSON only and rejects pipeline filters/transforms such as `path`, `from`, `sql`, `jsondesc`, and `stream`; query or narrow inside the explorer, or use loaded mode. It requires an independent JSON source and does not accept `paramsfile=-`. Keep local input unchanged while exploring or exporting it.

Use the explorer's recipe action to save operations and bookmarks. Replay a saved recipe with:

```sh
oafp file=records.json idescrecipe=recipe.json out=json
oafp file=large.json in=json idescsource=stream idescrecipe=recipe.json out=json outfile=selected.json
```

The explorer opens an independent controlling terminal through `askConsole`, allowing data on stdin to remain separate from its UI. A controlling terminal is required for interactive browsing. The non-ANSI UI uses numbered choices; the ANSI UI uses terminal navigation. JSON export and recipe replay can be checked separately from actual terminal interaction.
