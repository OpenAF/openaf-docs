# Sigil: object inspection and parameter validation

The core `js/openafsigil.js` module defines `$$` for inspecting and modifying objects and `_$` for validating parameters. These helpers are available in OpenAF scripts without loading an extra library.

## Object Inspection API (`$$`)

```javascript
var user = { name: "Alice", roles: ["admin", "dev"], meta: { active: true } };
print($$(user).get("meta.active"));      // true
print($$(user).get("roles[0]"));         // admin
print($$(user).getI("META.ACTIVE"));     // true
$$(user).set("meta.level", 5);
$$(user).unset("meta.active");
print($$(user).isMap());                 // true
print($$($$(user).get("roles")).isArray()); // true
```

`get` and `getI` return the selected value, not another builder. Wrap the returned value in `$$` to inspect its type. Create a fresh `$$` wrapper for each independent path operation: path traversal changes the wrapper's current object. `getI` resolves map keys case-insensitively.

## Fluent Parameter Validation API (`_$`)

```javascript
function createUser(name, age) {
  name = _$(name, "name").check(v => isString(v) && v.length > 0).$_();
  age = _$(age, "age").check(v => isNumber(v) && v >= 18 && v <= 120).default(21);
  return { name: name, age: age };
}
print(createUser("Alice", 30));
```

Finish a builder with `.$_()` or `.default(...)`. Use one combined predicate when all conditions must hold. See [parameter validation](../medium/parameter-validation.md#snapshot-compatibility) for current chaining behavior, conversion rules and source defects affecting individual helpers.

## Overview & Syntax

Object paths use dot and bracket notation, such as `meta.level` or `roles[0]`. These paths are separate from [JMESPath queries](openaf-reference.md#path--jmespath-inspired-query--transform) and [Handlebars templates](../cheat-sheet/templating.md).

## Sigil Handlers & Types

The pinned core does not expose a `$sigil` macro evaluator or a `<sigil:sec ...>` tag engine. Use the actual APIs for the value you need:

| Value | API |
| --- | --- |
| Environment variable | `getEnv("NAME")` |
| Template from a context map | `$t("Hello {{name}}", { name: "Alice" })` |
| Computed configuration | Compute the value explicitly in a job and pass it to `$job` |
| Secret-store access | `$sec(...)` with the configured repository and bucket |

## Filter Pipelines & Transformations

Perform transformations in JavaScript or use the documented Handlebars helpers. Shell `${NAME:-default}` syntax belongs to the shell; OpenAF does not automatically expand it in arbitrary YAML strings.

```javascript
var name = _$(getEnv("DOCS_NAME")).isString().default("Guest");
print($t("Hello {{name}}", { name: name.toUpperCase() }));
```

## JavaScript Macro API (`$sigil`)

Older prose described `$sigil.setHandler` and `ow.format.sigil`; these APIs are absent from this source snapshot. Use [templates](../cheat-sheet/templating.md), [dollar helpers](openaf-dollar-functions.md), and the [secret API reference](../../reference/ow_sec.md) instead.

## oJob Sigil Integration

Place parameter validation under `check.in` / `check.out`; job `exec` is executable code. Environment arguments, computed values and Handlebars expansion each have their own contracts. See the [oJob YAML reference](../ojob/ojob-yaml-reference.md), [validation examples](../medium/parameter-validation.md#ojob-integration), and [source ODoc reference](../../reference/scopesigil.md).
