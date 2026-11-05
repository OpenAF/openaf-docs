---
layout: default
title: Validation
parent: cheat-sheet
grand_parent: Guides
---

{% raw %}
<!-- Preserve earlier section bookmarks. -->
<a id="email-validation"></a>
<a id="username-validation"></a>
<a id="port-number"></a>
<a id="url-validation"></a>
<a id="phone-number"></a>
<a id="password-strength"></a>
<a id="non-empty-string"></a>
<a id="positive-number"></a>
<a id="chaining-examples"></a>
<a id="string-with-multiple-rules"></a>
<a id="number-with-conversion-and-range"></a>
<a id="enum-with-default"></a>
<a id="basic-input-validation"></a>
<a id="with-defaults"></a>
<a id="with-constraints"></a>
<a id="complex-validation"></a>
<a id="output-validation"></a>
<a id="array-elements"></a>
<a id="custom-checks"></a>
<a id="javascript-function"></a>
<a id="multiple-conditions"></a>
<a id="in-ojob"></a>
<a id="conditional-validation"></a>
<a id="quick-reference-card"></a>
<a id="validation-flow"></a>
<a id="most-common"></a>
<a id="default-error"></a>
<a id="custom-error"></a>
<a id="tips"></a>


# Validation Cheat Sheet

Use one complete predicate for requirements that must all hold. See [parameter validation](../medium/parameter-validation.md#snapshot-compatibility) for the pinned implementation's chaining behavior and helper limitations.

## Basic _$() Syntax

```javascript
var name = _$("Alice", "name").isString().$_();
var label = _$(undefined, "label").isString().default("Untitled");
var number = _$("42", "number").toNumber().check(v => isFinite(v)).$_();
```

`.$_()` requires a value; `.default(fallback)` permits an undefined value. Both return the final value. An invalid defined value still throws. Do not chain after either terminal call.

## Type Validators

| Requirement | Builder method |
| --- | --- |
| String, number, boolean | `isString()`, `isNumber()`, `isBoolean()` |
| Array or map | `isArray()`, `isMap()` |
| Date, function, regex | `isDate()`, `isFunction()`, `isRegExp()` |
| Object or instance | `isObject()`, `isInstanceOf(Type)` |
| Java object | `isJavaObject()` |
| Required value | Terminal `.$_()` |
| Optional value | Terminal `.default(value)` |

Global `isDef(value)` / `isUnDef(value)` are presence tests, not builder methods.

## Value Constraints

| Requirement | One predicate |
| --- | --- |
| Specific value | `.check(v => v === "active")` |
| Non-empty string | `.check(v => isString(v) && v.length > 0)` |
| Integer port | `.check(v => isNumber(v) && Math.floor(v) === v && v >= 1 && v <= 65535)` |
| Username pattern | `.check(v => isString(v) && /^[a-zA-Z0-9_]{3,20}$/.test(v))` |
| Scalar enum | `.check(v => isString(v) && ["info", "warn", "error"].indexOf(v) >= 0)` |
| UUID | `.check(v => isUUID(v))` |

The regex helper is `regexp(/pattern/)`. There are no builder methods named `match` or `inRange`.

## Type Conversion

Conversions return the builder. Finish with `.$_()` or `.default(...)`:

```javascript
var n = _$("10", "n").toNumber().check(v => isFinite(v)).$_();
var s = _$(10, "s").toString().$_();
var b = _$("true", "b").toBoolean().$_();
var d = _$("2026-11-05", "d").toDate().$_();
var a = _$("a, b", "a").toArray().$_();
var m = _$(' {"a":1} ', "m").toMap().$_();
```

## Default Values

```javascript
var timeout = _$(undefined, "timeout").isNumber().default(30000);
var config = _$(undefined, "config").isMap().default({ host: "localhost" });
```

## Common Patterns

```javascript
function validUsername(value) {
  return _$(value, "username")
    .check(v => isString(v) && /^[a-zA-Z0-9_]{3,20}$/.test(v), "invalid username")
    .$_();
}
```

## oJob Validation Syntax

```yaml
jobs:
- name: Validate request
  check:
    in:
      username: 'check(v => isString(v) && /^[a-zA-Z0-9_]{3,20}$/.test(v))'
      port: 'toNumber.check(v => isNumber(v) && v >= 1 && v <= 65535).default(8080)'
      role: 'check(v => isString(v) && ["user","admin"].indexOf(v) >= 0).default("user")'
    out:
      total: 'check(v => isNumber(v) && v >= 0)'
  exec: |
    args.total = 0;
```

The expression input is `v`. Validate array elements explicitly in job code. See the complete runnable [calculation example](../medium/parameter-validation.md#ojob-integration).

## Error Messages

```javascript
try {
  _$(15, "age").check(v => isNumber(v) && v >= 18, "You must be 18 or older").$_();
} catch (e) {
  printErr(String(e));
}
```

## See Also

- [Parameter validation](../medium/parameter-validation.md)
- [Type-check conditions](../medium/type-check-conditions.md)
- [oJob reference](../ojob/ojob-yaml-reference.md)
{% endraw %}
