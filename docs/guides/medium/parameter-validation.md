---
layout: default
title: Parameter Validation
parent: Medium
grand_parent: Guides
---

# Parameter Validation with _$()

OpenAF provides a powerful parameter validation system through the `_$()` function, enabling type checking, value constraints, transformations, and automatic error handling with fluent, chainable syntax.

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## Overview

The `_$()` function allows you to:
- **Validate parameter types** (string, number, array, map, etc.)
- **Apply constraints** (range, regex, equality checks)
- **Transform values** (type conversion, defaults)
- **Chain validations** for complex rules
- **Automatic error throwing** with descriptive messages

---

## Basic Usage

### Simple Type Validation

```javascript
function greet(name) {
  _$(name, "name").isString().$_();

  print("Hello, " + name + "!");
}

greet("Alice");  // Works
greet(123);      // Throws: name is not a string
```

### Validation with Default

```javascript
function greet(name) {
  name = _$(name, "name").isString().default("Guest");

  print("Hello, " + name + "!");
}

greet("Alice");     // Hello, Alice!
greet(undefined);   // Hello, Guest!
```

---

## Type Validators

### isString()

```javascript
_$(username, "username").isString().$_();
```

### isNumber()

```javascript
_$(age, "age").isNumber().$_();
```

### isArray()

```javascript
_$(items, "items").isArray().$_();
```

### isMap() / isObject()

```javascript
_$(config, "config").isMap().$_();
```

### isBoolean()

```javascript
_$(enabled, "enabled").isBoolean().$_();
```

### isFunction()

```javascript
_$(callback, "callback").isFunction().$_();
```

### isDate()

```javascript
_$(timestamp, "timestamp").isDate().$_();
```

### isDef() / isUnDef()

```javascript
// Ensure value is defined
_$(value, "value").isDef().$_();

// Ensure value is undefined
_$(optional, "optional").isUnDef().$_();
```

---

## Value Constraints

### Range Validation

```javascript
// Number in range
_$(port, "port").isNumber().inRange(1, 65535).$_();

// Age between 0 and 150
_$(age, "age").isNumber().inRange(0, 150).$_();
```

### Equality Checks

```javascript
// Equals specific value
_$(status, "status").isString().equals("active").$_();

// Does not equal
_$(username, "username").isString().notEquals("").$_();
```

### OneOf (Enum)

```javascript
// Must be one of these values
_$(level, "level")
  .isString()
  .oneOf(["debug", "info", "warn", "error"])
  .$_();

// With numbers
_$(priority, "priority")
  .isNumber()
  .oneOf([1, 2, 3, 4, 5])
  .$_();
```

### Pattern Matching (Regex)

```javascript
// Email validation
_$(email, "email")
  .isString()
  .match(/^[^\s@]+@[^\s@]+\.[^\s@]+$/)
  .$_();

// Phone number
_$(phone, "phone")
  .isString()
  .match(/^\d{3}-\d{3}-\d{4}$/)
  .$_();

// Alphanumeric
_$(code, "code")
  .isString()
  .match(/^[a-zA-Z0-9]+$/)
  .$_();
```

### anyOf / check

```javascript
// Custom validation function
_$(value, "value")
  .check(v => v > 0 && v < 100, "Value must be between 0 and 100")
  .$_();

// Multiple conditions (any can be true)
_$(input, "input")
  .anyOf([
    v => isString(v),
    v => isNumber(v)
  ])
  .$_();
```

---

## Type Conversion

### toNumber()

```javascript
var age = _$(args.age, "age").toNumber();
// "25" → 25
// 25 → 25
```

### toString()

```javascript
var id = _$(args.id, "id").toString();
// 123 → "123"
// "abc" → "abc"
```

### toBoolean()

```javascript
var enabled = _$(args.enabled, "enabled").toBoolean();
// "true" → true
// "false" → false
// 1 → true
// 0 → false
```

### toDate()

```javascript
var date = _$(args.date, "date").toDate();
// "2024-01-15" → Date object
// 1705276800000 → Date object
```

---

## Default Values

### default()

```javascript
// Use default if undefined
var timeout = _$(args.timeout, "timeout")
  .isNumber()
  .default(30000);

// Default with type conversion
var port = _$(args.port, "port")
  .toNumber()
  .default(8080);

// Default for complex types
var config = _$(args.config, "config")
  .isMap()
  .default({
    host: "localhost",
    port: 3000
  });
```

---

## Chaining Validations

### Multiple Constraints

```javascript
// Username: string, not empty, alphanumeric, 3-20 chars
_$(username, "username")
  .isString()
  .notEquals("")
  .match(/^[a-zA-Z0-9]+$/)
  .check(v => v.length >= 3 && v.length <= 20, "Length must be 3-20")
  .$_();
```

### Complex Validation Chain

```javascript
// Port number with all checks
var port = _$(args.port, "port")
  .toNumber()                    // Convert to number
  .isNumber()                    // Validate it's a number
  .inRange(1, 65535)            // Valid port range
  .default(8080);               // Default if undefined

// Email with transformation
var email = _$(args.email, "email")
  .isString()                   // Must be string
  .notEquals("")                // Not empty
  .check(v => v.toLowerCase())  // Convert to lowercase
  .match(/^[^\s@]+@[^\s@]+\.[^\s@]+$/)  // Valid format
  .$_();
```

---

## Common Patterns

### Pattern 1: Function Parameter Validation

```javascript
function createUser(username, email, age, config) {
  // Validate all parameters
  _$(username, "username")
    .isString()
    .notEquals("")
    .match(/^[a-zA-Z0-9_]+$/)
    .$_();

  _$(email, "email")
    .isString()
    .match(/^[^\s@]+@[^\s@]+\.[^\s@]+$/)
    .$_();

  age = _$(age, "age")
    .toNumber()
    .isNumber()
    .inRange(13, 120)
    .default(18);

  config = _$(config, "config")
    .isMap()
    .default({
      notifications: true,
      theme: "light"
    });

  // Now safe to use parameters
  var user = {
    username: username,
    email: email,
    age: age,
    config: config
  };

  return user;
}
```

### Pattern 2: API Request Validation

```javascript
function handleAPIRequest(request) {
  // Validate method
  _$(request.method, "request.method")
    .isString()
    .oneOf(["GET", "POST", "PUT", "DELETE"])
    .$_();

  // Validate headers
  _$(request.headers, "request.headers")
    .isMap()
    .$_();

  // Validate authorization
  _$(request.headers.authorization, "authorization")
    .isString()
    .notEquals("")
    .match(/^Bearer .+$/)
    .$_();

  // Validate body for POST/PUT
  if (request.method == "POST" || request.method == "PUT") {
    _$(request.body, "request.body")
      .isMap()
      .$_();
  }

  // Process request
  return processRequest(request);
}
```

### Pattern 3: Configuration Validation

```javascript
function loadConfig(configFile) {
  var config = io.readFileYAML(configFile);

  // Validate server config
  _$(config.server, "config.server").isMap().$_();

  config.server.host = _$(config.server.host, "server.host")
    .isString()
    .default("localhost");

  config.server.port = _$(config.server.port, "server.port")
    .toNumber()
    .isNumber()
    .inRange(1, 65535)
    .default(8080);

  // Validate database config
  _$(config.database, "config.database").isMap().$_();

  _$(config.database.url, "database.url")
    .isString()
    .match(/^jdbc:/)
    .$_();

  _$(config.database.user, "database.user")
    .isString()
    .notEquals("")
    .$_();

  // Validate optional features
  config.features = _$(config.features, "config.features")
    .isMap()
    .default({});

  config.features.logging = _$(config.features.logging, "features.logging")
    .toBoolean()
    .default(true);

  return config;
}
```

### Pattern 4: Array Element Validation

```javascript
function processItems(items) {
  // Validate array
  _$(items, "items")
    .isArray()
    .check(arr => arr.length > 0, "Must have at least one item")
    .$_();

  // Validate each item
  items.forEach((item, idx) => {
    _$(item.id, `items[${idx}].id`)
      .isString()
      .notEquals("")
      .$_();

    _$(item.quantity, `items[${idx}].quantity`)
      .toNumber()
      .isNumber()
      .check(v => v > 0, "Quantity must be positive")
      .$_();

    item.price = _$(item.price, `items[${idx}].price`)
      .toNumber()
      .isNumber()
      .check(v => v >= 0, "Price cannot be negative")
      .default(0);
  });

  return items;
}
```

---

## oJob Integration

### Job Input Validation

```yaml
jobs:
  - name: Process User
    check:
      in:
        username: isString
        email: isString
        age: isNumber.inRange(13,120).default(18)
        active: isBoolean.default(true)
    exec: |
      // Parameters are already validated
      log("Processing user: " + args.username);
```

### Complex Job Validation

```yaml
jobs:
  - name: Create Order
    check:
      in:
        customerId: isString.notEquals("")
        items: isArray.check("items.length > 0")
        paymentMethod: isString.oneOf(["card","paypal","bank"])
        billingAddress: isMap
        shippingAddress: isMap.default(__).check("billingAddress")
        notes: isString.default("")
    exec: |
      log("Creating order for customer: " + args.customerId);
      log("Items: " + args.items.length);
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
        tax: isNumber.check(">= 0")
        currency: isString.default("USD")
    exec: |
      var total = 0;
      args.items.forEach(item => {
        total += item.price * item.quantity;
      });

      var tax = total * 0.1;

      args.total = total;
      args.tax = tax;
      args.currency = "USD";
```

---

## Error Handling

### Throw Errors with $_()

```javascript
// Throws error if validation fails
_$(value, "value").isString().$_();
```

### Get Value Without Throwing

```javascript
// Returns validated value, doesn't throw
var validated = _$(value, "value").isString().default("default");
```

### Custom Error Messages

```javascript
_$(age, "age")
  .isNumber()
  .check(v => v >= 18, "Must be 18 or older to register")
  .$_();
```

### Try-Catch Pattern

```javascript
try {
  _$(username, "username")
    .isString()
    .match(/^[a-zA-Z0-9]+$/)
    .$_();

  processUser(username);

} catch(e) {
  if (e.message.indexOf("username") >= 0) {
    log("Invalid username format");
  } else {
    throw e;
  }
}
```

---

## Advanced Techniques

### Custom Validators

```javascript
// Create reusable validator
function validateEmail(value, name) {
  return _$(value, name)
    .isString()
    .notEquals("")
    .match(/^[^\s@]+@[^\s@]+\.[^\s@]+$/)
    .$_();
}

// Use it
validateEmail(args.email, "email");
```

### Conditional Validation

```javascript
function validate(data) {
  // Always validate type
  _$(data.type, "type")
    .isString()
    .oneOf(["personal", "business"])
    .$_();

  // Conditional validation based on type
  if (data.type == "business") {
    _$(data.companyName, "companyName")
      .isString()
      .notEquals("")
      .$_();

    _$(data.taxId, "taxId")
      .isString()
      .match(/^\d{9}$/)
      .$_();
  }

  if (data.type == "personal") {
    _$(data.firstName, "firstName")
      .isString()
      .notEquals("")
      .$_();

    _$(data.lastName, "lastName")
      .isString()
      .notEquals("")
      .$_();
  }
}
```

### Validation Builder

```javascript
function buildValidator(config) {
  return function(value, name) {
    var validator = _$(value, name);

    if (config.type == "string") {
      validator = validator.isString();
    } else if (config.type == "number") {
      validator = validator.toNumber().isNumber();
    }

    if (isDef(config.default)) {
      validator = validator.default(config.default);
    }

    if (isDef(config.pattern)) {
      validator = validator.match(new RegExp(config.pattern));
    }

    if (isDef(config.oneOf)) {
      validator = validator.oneOf(config.oneOf);
    }

    return validator.$_();
  };
}

// Usage
var validateStatus = buildValidator({
  type: "string",
  oneOf: ["active", "inactive", "pending"],
  default: "active"
});

validateStatus(args.status, "status");
```

---

## Best Practices

### 1. Validate Early

```javascript
function processOrder(order) {
  // Validate at the beginning
  _$(order, "order").isMap().$_();
  _$(order.id, "order.id").isString().$_();
  _$(order.items, "order.items").isArray().$_();

  // Now safe to process
  var total = calculateTotal(order.items);
  // ...
}
```

### 2. Use Meaningful Names

```javascript
// Good - clear parameter name
_$(userEmail, "userEmail").isString().$_();

// Bad - generic name
_$(value, "value").isString().$_();
```

### 3. Combine with Defaults

```javascript
// Provide sensible defaults
var timeout = _$(args.timeout, "timeout")
  .toNumber()
  .isNumber()
  .inRange(1, 300000)
  .default(30000);

var retries = _$(args.retries, "retries")
  .toNumber()
  .isNumber()
  .inRange(0, 10)
  .default(3);
```

### 4. Document Validation Rules

```javascript
/**
 * Creates a new user account
 * @param {string} username - Alphanumeric, 3-20 characters
 * @param {string} email - Valid email format
 * @param {number} age - Between 13 and 120, defaults to 18
 */
function createUser(username, email, age) {
  _$(username, "username")
    .isString()
    .match(/^[a-zA-Z0-9]+$/)
    .check(v => v.length >= 3 && v.length <= 20)
    .$_();

  _$(email, "email")
    .isString()
    .match(/^[^\s@]+@[^\s@]+\.[^\s@]+$/)
    .$_();

  age = _$(age, "age")
    .toNumber()
    .isNumber()
    .inRange(13, 120)
    .default(18);

  // Implementation...
}
```

### 5. Use Type Conversion

```javascript
// Convert and validate in one chain
var port = _$(args.port, "port")
  .toNumber()          // Convert first
  .isNumber()          // Then validate
  .inRange(1, 65535)
  .default(8080);
```

---

## Complete Example

```javascript
/**
 * REST API handler with full validation
 */
function handleCreateUser(request) {
  // Validate request structure
  _$(request, "request").isMap().$_();
  _$(request.body, "request.body").isMap().$_();

  var body = request.body;

  // Validate username
  _$(body.username, "username")
    .isString()
    .notEquals("")
    .match(/^[a-zA-Z0-9_]{3,20}$/)
    .check(v => !userExists(v), "Username already exists")
    .$_();

  // Validate email
  _$(body.email, "email")
    .isString()
    .notEquals("")
    .match(/^[^\s@]+@[^\s@]+\.[^\s@]+$/)
    .check(v => !emailExists(v), "Email already registered")
    .$_();

  // Validate password
  _$(body.password, "password")
    .isString()
    .check(v => v.length >= 8, "Password must be at least 8 characters")
    .check(v => /[A-Z]/.test(v), "Password must contain uppercase letter")
    .check(v => /[a-z]/.test(v), "Password must contain lowercase letter")
    .check(v => /[0-9]/.test(v), "Password must contain number")
    .$_();

  // Validate optional fields with defaults
  var age = _$(body.age, "age")
    .toNumber()
    .isNumber()
    .inRange(13, 120)
    .default(18);

  var role = _$(body.role, "role")
    .isString()
    .oneOf(["user", "admin", "moderator"])
    .default("user");

  var preferences = _$(body.preferences, "preferences")
    .isMap()
    .default({
      notifications: true,
      theme: "light",
      language: "en"
    });

  // Create user
  var user = {
    id: genUUID(),
    username: body.username,
    email: body.email.toLowerCase(),
    passwordHash: sha256(body.password),
    age: age,
    role: role,
    preferences: preferences,
    createdAt: nowUTC(),
    active: true
  };

  // Save user
  saveUser(user);

  // Return sanitized response (no password)
  delete user.passwordHash;
  return user;
}
```

---

## See Also

- [oJob Reference - Input/Output Validation](../../concepts/oJob.html)
- [OpenAF Scope Reference](../../reference/scope.md)
- [oJob Cheat Sheet](../cheat-sheet/ojob.md)
