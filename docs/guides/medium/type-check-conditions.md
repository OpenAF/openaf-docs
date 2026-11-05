---
layout: default
title: Type-check conditions
parent: Medium
grand_parent: Guides
---

{% raw %}
# Type-check conditions

`_$(value, "name")` builds a validation chain. Finish it with `.$_()` to require a value or `.default(fallback)` to supply a value only when it is undefined. An invalid defined value still throws; the fallback is not a replacement for invalid input.

```javascript
var port = _$("8080", "port").toNumber().check(v => isNumber(v) && v >= 1 && v <= 65535).$_();
var label = _$(undefined, "label").isString().default("untitled");
```

| Condition | Meaning |
| --- | --- |
| `isString`, `isNumber`, `isBoolean` | Check the corresponding value type |
| `isArray`, `isMap`, `isObject` | Check the container type |
| `isDate`, `isFunction`, `isRegExp`, `isJavaObject` | Check specialized values |
| `isInstanceOf(Type)` | Check JavaScript `instanceof` |
| `isNotNull()` | Reject an explicitly null value |
| `oneOf(values)` | Check a scalar against an allowed list |
| `anyOf(values)` | Check that every element of an input array belongs to an allowed list |
| `less`, `lessEquals`, `greater`, `greaterEquals` | Numeric comparisons |
| `check(predicate, message)` | Apply an explicit predicate |
| `isSchema(schema, message, options)` | Validate against JSON Schema |

Conversions such as `toNumber()` and `toString()` return the validation chain, not the converted value. Finish the chain before assigning its result.

## Snapshot compatibility

A group of chained checks accepts a defined value when at least one check passes in this snapshot. Use one combined predicate when every condition must hold. Global `isDef` and `isUnDef` are not builder methods. The regex helper is `regexp`, and there is no `inRange`. See the [full compatibility notes](parameter-validation.md#snapshot-compatibility), including `starts` / `notStarts` limitations.

In the [November source snapshot](../../source-snapshot.md), the implementation of `equals` and `notEquals` tests the opposite of their names, `between` and `betweenEquals` do not return the chain, and the chain's `isUUID` rejects a matching UUID. Until those upstream behaviors change, use explicit predicates:

```javascript
_$("ready").check(v => v === "ready").$_();
_$(3).check(v => isNumber(v) && v >= 1 && v <= 5).$_();
_$("123e4567-e89b-12d3-a456-426614174000").check(v => isUUID(v)).$_();
```

These are documentation workarounds, not runtime changes. See [validation](../cheat-sheet/validation.md), [parameter validation](parameter-validation.md), and the [source implementation](https://github.com/OpenAF/openaf/blob/06414cd9204e918daa1e2971ce904783299db333/js/openafsigil.js).
{% endraw %}
