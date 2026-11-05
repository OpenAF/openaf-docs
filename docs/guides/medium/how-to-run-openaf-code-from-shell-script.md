---
layout: default
title: How to run OpenAF code from shell script
parent: Medium
grand_parent: Guides
---

# How to run OpenAF code from shell script

Use `oaf -f myScript.js` for a separate script, `-c` for inline code, or `-i script -p` to read a script from standard input. These examples use local data and require no external API.

## Inline code

Single quotes protect JavaScript dollar signs and double quotes from shell expansion:

```sh
oaf -c 'print($path({ person: { name: "Ana" } }, "person.name"))'
```

Capture standard output in a POSIX shell script:

```sh
#!/bin/sh
name=$(oaf -c 'print("Ana")')
printf 'Hi %s\n' "$name"
```

Use `printErr` for diagnostics that should not become part of the captured value. Quote shell variable expansions when using the result.

## Multiline code

A quoted heredoc delimiter disables shell expansion inside the JavaScript block, including `$` functions and template literals:

```sh
#!/bin/sh
output=$(oaf -i script -p <<'OPENAF_SCRIPT'
var person = { name: "Ana", surname: "Silva", phone: "123-456" };
print(person.name + " " + person.surname + ";" + person.phone);
OPENAF_SCRIPT
)
printf '%s\n' "$output"
```

This prints `Ana Silva;123-456`. To pass values from the shell, export environment variables and read them with `getEnv("NAME")`, or pass arguments using the CLI's documented `-e` option. See the [CLI guide](../advanced/cli.md).
