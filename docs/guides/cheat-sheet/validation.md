---
layout: default
title: Validation
parent: Cheat sheet
grand_parent: Guides
---

# Validation Cheat Sheet

Quick reference for parameter validation using `_$()` and oJob `check.in`/`check.out`.

---

## Basic _$() Syntax

```javascript
// Validate and throw error if invalid
_$(value, "paramName").isString().$_();

// Validate with default (doesn't throw)
var val = _$(value, "paramName").isString().default("defaultValue");

// Type conversion
var num = _$(value, "paramName").toNumber();
```

---

## Type Validators

| Validator | Description | Example |
|-----------|-------------|---------|
| `isString()` | Must be a string | `_$(name, "name").isString().$_()` |
| `isNumber()` | Must be a number | `_$(age, "age").isNumber().$_()` |
| `isArray()` | Must be an array | `_$(items, "items").isArray().$_()` |
| `isMap()` | Must be an object/map | `_$(config, "config").isMap().$_()` |
| `isBoolean()` | Must be true/false | `_$(enabled, "enabled").isBoolean().$_()` |
| `isFunction()` | Must be a function | `_$(callback, "callback").isFunction().$_()` |
| `isDate()` | Must be a Date object | `_$(timestamp, "timestamp").isDate().$_()` |
| `isDef()` | Must be defined | `_$(value, "value").isDef().$_()` |
| `isUnDef()` | Must be undefined | `_$(value, "value").isUnDef().$_()` |

---

## Value Constraints

| Constraint | Description | Example |
|------------|-------------|---------|
| `equals(val)` | Must equal specific value | `_$(status, "status").equals("active").$_()` |
| `notEquals(val)` | Must not equal value | `_$(username, "username").notEquals("").$_()` |
| `oneOf([...])` | Must be one of array values | `_$(level, "level").oneOf(["debug","info","warn"]).$_()` |
| `inRange(min, max)` | Must be in numeric range | `_$(port, "port").inRange(1, 65535).$_()` |
| `match(regex)` | Must match regex pattern | `_$(email, "email").match(/^\S+@\S+$/).$_()` |
| `check(fn, msg)` | Custom validation function | `_$(age, "age").check(v => v >= 18, "Must be 18+").$_()` |

---

## Type Conversion

| Converter | Description | Example |
|-----------|-------------|---------|
| `toNumber()` | Convert to number | `var n = _$(val, "val").toNumber()` |
| `toString()` | Convert to string | `var s = _$(val, "val").toString()` |
| `toBoolean()` | Convert to boolean | `var b = _$(val, "val").toBoolean()` |
| `toDate()` | Convert to Date | `var d = _$(val, "val").toDate()` |

---

## Default Values

```javascript
// Simple default
var timeout = _$(args.timeout, "timeout").default(30000);

// Default with type check
var port = _$(args.port, "port").isNumber().default(8080);

// Default with conversion
var age = _$(args.age, "age").toNumber().default(18);

// Default object
var config = _$(args.config, "config").isMap().default({
  host: "localhost",
  port: 3000
});
```

---

## Common Patterns

### Email Validation

```javascript
_$(email, "email")
  .isString()
  .match(/^[^\s@]+@[^\s@]+\.[^\s@]+$/)
  .$_();
```

### Username Validation

```javascript
_$(username, "username")
  .isString()
  .match(/^[a-zA-Z0-9_]{3,20}$/)
  .$_();
```

### Port Number

```javascript
var port = _$(args.port, "port")
  .toNumber()
  .isNumber()
  .inRange(1, 65535)
  .default(8080);
```

### URL Validation

```javascript
_$(url, "url")
  .isString()
  .match(/^https?:\/\/.+/)
  .$_();
```

### Phone Number

```javascript
_$(phone, "phone")
  .isString()
  .match(/^\d{3}-\d{3}-\d{4}$/)
  .$_();
```

### Password Strength

```javascript
_$(password, "password")
  .isString()
  .check(v => v.length >= 8, "Min 8 characters")
  .check(v => /[A-Z]/.test(v), "Need uppercase")
  .check(v => /[a-z]/.test(v), "Need lowercase")
  .check(v => /[0-9]/.test(v), "Need number")
  .$_();
```

### Non-Empty String

```javascript
_$(value, "value")
  .isString()
  .notEquals("")
  .$_();
```

### Positive Number

```javascript
_$(amount, "amount")
  .isNumber()
  .check(v => v > 0, "Must be positive")
  .$_();
```

---

## Chaining Examples

### String with Multiple Rules

```javascript
_$(username, "username")
  .isString()                    // Type check
  .notEquals("")                 // Not empty
  .match(/^[a-zA-Z0-9]+$/)      // Alphanumeric
  .check(v => v.length >= 3 && v.length <= 20, "3-20 chars")
  .$_();
```

### Number with Conversion and Range

```javascript
var age = _$(args.age, "age")
  .toNumber()                    // Convert to number
  .isNumber()                    // Validate is number
  .inRange(0, 150)              // Valid range
  .default(18);                  // Default value
```

### Enum with Default

```javascript
var level = _$(args.level, "level")
  .isString()
  .oneOf(["debug", "info", "warn", "error"])
  .default("info");
```

---

## oJob Validation Syntax

### Basic Input Validation

```yaml
jobs:
  - name: My Job
    check:
      in:
        username: isString
        age: isNumber
        email: isString
```

### With Defaults

```yaml
jobs:
  - name: My Job
    check:
      in:
        port: isNumber.default(8080)
        timeout: isNumber.default(30000)
        enabled: isBoolean.default(true)
```

### With Constraints

```yaml
jobs:
  - name: My Job
    check:
      in:
        username: isString.notEquals("")
        age: isNumber.inRange(0,150)
        email: isString.match("^\\S+@\\S+$")
        status: isString.oneOf(["active","inactive"])
```

### Complex Validation

```yaml
jobs:
  - name: My Job
    check:
      in:
        # String, not empty, alphanumeric, 3-20 chars
        username: isString.notEquals("").match("^[a-zA-Z0-9]{3,20}$")

        # Number, convert if needed, range, default
        port: toNumber.isNumber.inRange(1,65535).default(8080)

        # Email format
        email: isString.match("^[^\\s@]+@[^\\s@]+\\.[^\\s@]+$")

        # Enum with default
        role: isString.oneOf(["user","admin","moderator"]).default("user")
```

### Output Validation

```yaml
jobs:
  - name: Calculate Total
    check:
      in:
        items: isArray
      out:
        total: isNumber.check(">= 0")
        currency: isString.default("USD")
    exec: |
      args.total = calculateTotal(args.items);
      args.currency = "USD";
```

### Array Elements

```yaml
jobs:
  - name: Process Items
    check:
      in:
        items: isArray.check("items.length > 0")
        items[].id: isString
        items[].quantity: isNumber.check("> 0")
        items[].price: isNumber.check(">= 0")
```

---

## Custom Checks

### JavaScript Function

```javascript
_$(value, "value")
  .check(v => {
    // Custom validation logic
    return v.startsWith("prefix-") && v.length > 10;
  }, "Must start with 'prefix-' and be > 10 chars")
  .$_();
```

### Multiple Conditions

```javascript
_$(data, "data")
  .isMap()
  .check(v => isDef(v.id), "Missing id")
  .check(v => isDef(v.name), "Missing name")
  .check(v => v.items && v.items.length > 0, "Need items")
  .$_();
```

### In oJob

```yaml
check:
  in:
    data: isMap.check("isDef(data.id) && isDef(data.name)")
```

---

## Conditional Validation

```javascript
function validate(args) {
  // Always validate type
  _$(args.type, "type").oneOf(["personal", "business"]).$_();

  // Conditional based on type
  if (args.type == "business") {
    _$(args.companyName, "companyName").isString().$_();
    _$(args.taxId, "taxId").isString().match(/^\d{9}$/).$_();
  } else {
    _$(args.firstName, "firstName").isString().$_();
    _$(args.lastName, "lastName").isString().$_();
  }
}
```

---

## Quick Reference Card

### Validation Flow

```javascript
_$(value, "name")              // Start validation
  .toNumber()                  // Convert (optional)
  .isNumber()                  // Type check
  .inRange(1, 100)            // Constraint
  .default(50)                // Default (optional)
  .$_();                      // Execute (throw) or omit (return)
```

### Most Common

```javascript
// Required string
_$(val, "val").isString().$_();

// Optional string with default
var val = _$(val, "val").isString().default("default");

// Required number in range
_$(val, "val").isNumber().inRange(1, 100).$_();

// Optional number with default
var val = _$(val, "val").toNumber().default(10);

// Enum
_$(val, "val").oneOf(["a", "b", "c"]).$_();

// Not empty
_$(val, "val").isString().notEquals("").$_();
```

---

## Error Messages

### Default Error

```javascript
_$(username, "username").isString().$_();
// Error: username is not a string
```

### Custom Error

```javascript
_$(age, "age")
  .check(v => v >= 18, "You must be 18 or older")
  .$_();
// Error: You must be 18 or older
```

---

## Tips

✅ **Validate early** - Check parameters at function start
✅ **Use meaningful names** - Makes errors clearer
✅ **Chain wisely** - Order matters: convert → validate → constrain → default
✅ **Provide defaults** - Makes APIs more user-friendly
✅ **Custom messages** - Use `.check(fn, msg)` for business rules
✅ **Document rules** - Add comments explaining validation logic

❌ **Don't over-validate** - Balance safety with usability
❌ **Don't repeat** - Extract common validations to functions
❌ **Don't ignore errors** - Always handle validation failures

---

## See Also

- [Parameter Validation Guide](../medium/parameter-validation.md)
- [oJob Reference](../../concepts/oJob.html)
- [OpenAF Scope Reference](../../reference/scope.md)
