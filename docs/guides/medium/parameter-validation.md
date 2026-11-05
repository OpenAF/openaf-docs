---
layout: default
title: Parameter Validation
parent: Medium
grand_parent: Guides
---

{% raw %}
<!-- Preserve earlier section bookmarks. -->
<a id="table-of-contents"></a>
<a id="overview"></a>
<a id="simple-type-validation"></a>
<a id="validation-with-default"></a>
<a id="isstring"></a>
<a id="isnumber"></a>
<a id="isarray"></a>
<a id="ismap--isobject"></a>
<a id="isboolean"></a>
<a id="isfunction"></a>
<a id="isdate"></a>
<a id="isdef--isundef"></a>
<a id="range-validation"></a>
<a id="equality-checks"></a>
<a id="oneof-enum"></a>
<a id="pattern-matching-regex"></a>
<a id="anyof--check"></a>
<a id="tonumber"></a>
<a id="tostring"></a>
<a id="toboolean"></a>
<a id="todate"></a>
<a id="default"></a>
<a id="chaining-validations"></a>
<a id="multiple-constraints"></a>
<a id="complex-validation-chain"></a>
<a id="common-patterns"></a>
<a id="pattern-1-function-parameter-validation"></a>
<a id="pattern-2-api-request-validation"></a>
<a id="pattern-3-configuration-validation"></a>
<a id="pattern-4-array-element-validation"></a>
<a id="job-input-validation"></a>
<a id="complex-job-validation"></a>
<a id="output-validation"></a>
<a id="error-handling"></a>
<a id="throw-errors-with-_"></a>
<a id="get-value-without-throwing"></a>
<a id="custom-error-messages"></a>
<a id="try-catch-pattern"></a>
<a id="advanced-techniques"></a>
<a id="custom-validators"></a>
<a id="conditional-validation"></a>
<a id="validation-builder"></a>
<a id="best-practices"></a>
<a id="1-validate-early"></a>
<a id="2-use-meaningful-names"></a>
<a id="3-combine-with-defaults"></a>
<a id="4-document-validation-rules"></a>
<a id="5-use-type-conversion"></a>
<a id="complete-example"></a>


# Parameter Validation with _$()

`_$(value, "name")` returns a validation builder. Call `.$_()` to require and return a value, or `.default(fallback)` to return a fallback when the input is undefined. Conversions also return the builder, so they need a terminal call.

This guide follows the [pinned source snapshot](../../source-snapshot.md). Its validation implementation has compatibility quirks described below. The examples use one complete predicate where several conditions must all hold.

## Basic Usage

```javascript
function greet(name) {
  name = _$(name, "name").isString().default("Guest");
  return "Hello, " + name + "!";
}

print(greet("Alice"));    // Hello, Alice!
print(greet(undefined));  // Hello, Guest!
// greet(123) throws; a default does not replace an invalid defined value.
```

## Type Validators

Use `isString`, `isNumber`, `isTNumber`, `isBoolean`, `isArray`, `isMap`, `isObject`, `isDate`, `isRegExp`, `isFunction`, `isJavaObject`, or `isInstanceOf(Type)` followed by a terminal call. Global `isDef(value)` and `isUnDef(value)` test presence; they are not methods on this builder. `.$_()` requires a defined value.

```javascript
var config = _$({ host: "localhost" }, "config").isMap().$_();
var count = _$("42", "count").toNumber().check(v => isNumber(v) && isFinite(v)).$_();
```

## Value Constraints

For a condition that must satisfy several rules, place all rules inside a single `check` predicate. Guard access to string or map properties with a type check in that predicate.

```javascript
function validPort(value) {
  return _$(value, "port").toNumber()
    .check(v => isNumber(v) && isFinite(v) && Math.floor(v) === v && v >= 1 && v <= 65535,
           "port must be an integer from 1 to 65535")
    .default(8080);
}

print(validPort("443"));     // 443
print(validPort(undefined)); // 8080
// validPort("70000") throws.
```

`oneOf(values)` checks a scalar against an allowed array. `anyOf(values)` checks elements of an input array. Validate the input shape as part of a combined predicate if callers may pass either shape.

```javascript
var status = _$("active", "status")
  .check(v => isString(v) && ["active", "inactive"].indexOf(v) >= 0)
  .$_();
var username = _$("alice_1", "username")
  .check(v => isString(v) && /^[a-zA-Z0-9_]{3,20}$/.test(v))
  .$_();
```

The regex method is `regexp(/pattern/)`, not `match`. Numeric comparison methods include `less`, `lessEquals`, `greater`, and `greaterEquals`; there is no `inRange` method.

## Type Conversion

`toNumber()`, `toString()`, `toBoolean()`, `toDate()`, `toArray()` and `toMap()` convert the current value and return the builder. `toArray()` splits comma-separated text, and `toMap()` parses JSON text. `toBoolean()` interprets a string as true only when its trimmed lowercase value is `true`; other strings become false. Validate the original vocabulary first if arbitrary strings should be rejected.

```javascript
var amount = _$("12.5", "amount").toNumber().check(v => isFinite(v)).$_();
var enabled = _$("true", "enabled").oneOf(["true", "false"]).$_() === "true";
```

## Default Values

`.default(value)` terminates the chain. Do not call `.$_()` after it. An invalid defined input still throws. Predicates are evaluated even when the input is missing, so avoid dereferencing a missing value.

```javascript
var title = _$(undefined, "title")
  .check(v => isString(v) && v.length > 0)
  .default("Untitled");
```

## Custom Validation

`check` accepts either a function or an expression string whose input variable is `v`:

```javascript
var total = _$(15, "total").check("isNumber(v) && v >= 0").$_();
```

For reusable validation, wrap the builder in a function and return the terminal result. Keep explicit checks for failure paths in your tests, particularly when converting user input.

## oJob Integration

`check.in` and `check.out` use the same builder. The expression variable is `v`, not the argument's field name. This complete job validates input and output:

```yaml
todo:
- name: Calculate total
  args:
    items:
    - price: 5
      quantity: 3
jobs:
- name: Calculate total
  check:
    in:
      items: 'check(v => isArray(v) && v.length > 0)'
    out:
      total: 'check(v => isNumber(v) && isFinite(v) && v >= 0)'
  exec: |
    args.items.forEach(item => {
      _$(item, "item").check(v => isMap(v) && isNumber(v.price) && v.price >= 0
        && isNumber(v.quantity) && v.quantity > 0).$_();
    });
    args.total = args.items.reduce((sum, item) => sum + item.price * item.quantity, 0);
    print(args.total);
```

For optional fields, `port: toNumber.check(v => isNumber(v) && v >= 1 && v <= 65535).default(8080)` supplies a default. Array element validation is explicit in the job above; do not assume `items[].price` is a supported `check` path.

## Snapshot Compatibility

In this source revision, a group of chained validators accepts a defined value when **at least one** check passes. Do not assume `.isNumber().check(range)` requires both checks. Use a single combined predicate, or make separate terminal validation calls for independent requirements.

There are also source defects in several helpers: `equals` and `notEquals` reject the opposite values to what their names suggest, `between` and `betweenEquals` do not return the builder, `isUUID` rejects a matching UUID, and `starts` / `notStarts` reference an undefined variable. Use predicates such as `v => v === "active"`, `v => isUUID(v)`, and `v => isString(v) && v.startsWith("prefix-")` instead.

These workarounds describe the pinned implementation, not a runtime fix. Review them when updating the baseline. Source: [`js/openafsigil.js`](https://github.com/OpenAF/openaf/blob/06414cd9204e918daa1e2971ce904783299db333/js/openafsigil.js).

## See Also

- [Validation cheat sheet](../cheat-sheet/validation.md)
- [Type-check conditions](type-check-conditions.md)
- [oJob YAML reference](../ojob/ojob-yaml-reference.md)
- [Testing OpenAF and oJob](../ojob/testing-openaf.md)
{% endraw %}
