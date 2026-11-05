---
layout: default
title: scopesigil
parent: Reference
grand_parent: OpenAF docs
---

{% raw %}
## scopesigil

[Source: `06414cd9`](https://github.com/OpenAF/openaf/blob/06414cd9204e918daa1e2971ce904783299db333/js/openafsigil.js) · [Baseline](../source-snapshot.md)

### $$.get

`$$.get(aPath) : Object`

Given `aObject` it will try to parse the `aPath` and retrieve the corresponding object under that path. Example:

```javascript
var a = { a : 1, b : { c: 2, d: [0, 1] } };

print($$(a).get("b.c")); // 2
sprint($$(a).get("b.d")); // [0, 1]
print($$(a).get("b.d[0]")); // 0
```

### $$.getI

`$$.getI(aPath) : Object`

Given `aObject` it will try to parse the `aPath` (in a case-insensitive way) and retrieve the corresponding object under that path. Example:

```javascript
var a = { a : 1, b : { c: 2, d: [0, 1] } };

print($$(a).getI("b.C")); // 2
sprint($$(a).getI("B.d")); // [0, 1]
print($$(a).getI("B.D[0]")); // 0
```

### $$.set

`$$.set(aPath, aNewValue) : Object`

Given `aObject` it will try to parse the `aPath` and set the corresponding object under that path to `aNewValue`. Example:

```javascript
var a = { a : 1, b : { c: 2, d: [0, 1] } };

sprint($$(a).set("b.c", 123)); // { a : 1, b : { c: 123, d: [0, 1] } }
```

### $$.unset

`$$.unset(aPath) : Object`

> Example formatting/syntax corrected against the implementation; the signature is unchanged.

Given `aObject` it will try to parse the `aPath` and unset the corresponding object under that path. Example:

```javascript
var a = { a : 1, b : { c: 2, d: [0, 1] } };

sprint($$(a).unset("b.c")); // { a : 1, b : { d: [0, 1] } }
```

### _$

`_$(aObject, anErrorMessagePrefix)`

Shortcut to facilitate argument pre-validation and promote defensive programming.

- `.default(aNewObject)`: `aObject`
  Checks if `aObject` is defined and returns `aObject`. If it's not defined it will return `aNewObject` (the default value).

- `$_(aMessage)`: `aObject`
  Throws an exception with `aMessage` if `aObject` is not defined otherwise returns `aObject`.
{% endraw %}
