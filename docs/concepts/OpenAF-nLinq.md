---
layout: default
title: $from
parent: Concepts
grand_parent: OpenAF docs
---

# $from

There are several "helpers" in OpenAF to help to "query" array of maps that help to make code cleaner. OpenAF extends JavaScript with $from(), a powerful helper for working with arrays (especially arrays of maps). It simplifies filtering, sorting, grouping, and transforming — much like a blend of SQL and LINQ. For a complete list (like JMESPath) see on the end of this document. [_nLinq_](https://github.com/nmaguiar/nLinq) is currently the most use one.

Quick examples:

````javascript
// How many contacts there are with email ending in @domain.com
$from( arrayOfContacts )
.ends("email", "@domain.com")
.count();

// Sort all contacts in @domain.com by first name and last name
$from( arrayOfContacts )
.ends("email", "@domain.com")
.sort("firstName", "lastName")
.select()
````

## 🆚 Native JS: A Side-by-Side

Why use $from() over native JavaScript?

* **More declarative** - you describe what you want, not how.
* **Chainable** - easy to build multi-step logic.
* **Cross-platform consistent** - works the same on all OpenAF-supported platforms.
* **Extensible** - integrates with OpenAF plugins and transformations cleanly.

### Example: 🔍 Filtering items > 1KB

**Native JavaScript:**

```javascript
files.filter(f => f.size > 1024);
```

**$from():**

```javascript
$from(files).greater("size", 1024).select();
```

✅ $from() version is more readable for complex filters and chains.

## 🧰 Use $from() when you need:

| Task | $from() benefit |
|----------------|-----------------|
| Filter by condition | .equals(), .greater(), .contains() etc. |
| Sort by one or more keys | .sort("aKey", "bKey") |
| Group items by key | .group("category") |
| Get distinct values | .distinct("fieldName") |
| Transform / map objects | .select(r => ({...})) |
| Aggregate (sum, count) | .sum("amount"), .count() |

## Check also:

* [$from() cheat-sheet](../guides/cheat-sheet/from.md)

# Reference

_nLinq_ queries are made through a series of calls divided into three main areas:

````javascript
var result = $from( aSourceArray )      // FROM part
             .equals("aKey1", aValue)   // WHERE part
             .greater("aKey2", 10)      //
             .select()                  // SELECT part
````

## FROM

The input should be primarially an array. If a map is provided it will be converted into an array. For streams it can also be a function.

### Simple array
````javascript
var inData  = [ 1, 2, 3 ];
var outData = $from(inData).select();
// [ 1, 2, 3 ]
````

### Array of maps
````javascript
var inData  = [ { a: 1 }, { a: 2 }, { a: 3 } ];
var outData = $from(inData).select();
// [ {a: 1}, {a: 2}, {a: 3} ]
````

### Simple map

````javascript
var inData  = { a: 1, b: 2, c: 3};
var outData = $from(inData).select();
// [ 1, 2, 3 ]
````

### Map of maps

````javascript
var inData  = { a1: { a: 1 }, a2: { a: 2 }, a3: { a: 3 } };
var outData = $from(inData).select();
// [ { a: 1, _key: "a1" }, { a: 2, _key: "a2" }, { a: 3, _key: "a3"} ]
````

### A function

````javascript
var ll = 0, sum = 0;
var fn = () => ll++;
$from(fn).limit(5).stream(r => sum += r);
// sum = 10 | ll = 6
````

## WHERE

### Restriciting prefixes and suffixes

Consider the following example:

````javascript
var names = [
  { first: "James", last: "Bond" },
  { first: "James", last: "Scott" },
  { first: "Louis", last: "Bond" }
];
````

| Method | Description | Example |
|--------|-------------|---------|
| starts | Restricts string fields prefix to a value | ````$from(names).starts("first", "J").select()```` |
| andStarts | Restricts string fields prefix to a value in addition to the previous restriction | ````$from(names).starts("first", "J").starts("last", "B").select()```` |
| notStarts | Restricts string fields that are not prefixed by a value | ````$from(names).notStarts("first", "J").select()```` |
| andNotStarts | Restricts string fields that are not prefixed by a value in addition to the previous restriction | ````$from(names).starts("first", "J").andNotStarts("last", "S").select()```` |
| orStarts | Restricts string fields prefix to a value in alternative to the previous restriction | ````$from(names).starts("first", "Ja").orStarts("last", "Bo").select()```` |
| orNotStarts | Restricts string fields prefix that are not prefixed by a value in alternative to the previous restriction | ````$from(names).starts("first", "Ja").orNotStarts("last", "Sc").select()```` |
| ends | Restricts string fields suffix to a value | ````$from(names).ends("last", "nd").select()```` |
| andEnds | Restricts string fields suffix to a value in addition to the previous restriction | ````$from(names).ends("first", "es").andEnds("last", "d").select()```` |
| notEnds | Restricts string fields that are not suffixed by a value | ````$from(names).notEnds("last", "Bond").select()```` |
| andNotEnds | Restricts string fields that are not suffixed by a value in addition to a previous restriction | ````$from(names).starts("first", "J").andNotEnds("last", "d").select()```` |
| orEnds | Restricts string fields that are suffixed by a value in alternative to a previous restriction | ````$from(names).starts("first", "J").orEnds("first", "d").select()```` |
| orNotEnds | Restricts string fields that are not suffixed by a value in alternative to a previous restriction | ````$from(names).starts("first", "J").orNotEnds("first", "s").select()```` |

### Restricting by equality

| Method | Description | Example |
|------|-------------|---------|
| andEquals | | |
| greaterEquals | | |
| andGreaterEquals | | |
| notGreaterEquals | | |
| andNotGreaterEquals | | |
| orGreaterEquals | | |
| orNotGreaterEquals | | |
| lessEquals | | |
| andLessEquals | | |
| andNotLessEquals | | |
| orLessEquals | | |
| orNotLessEquals | | |

### Restricting by value

| Method | Description | Example |
|------|-------------|---------|
| greater | | |
| andGreater | | |
| notGreater | | |
| andNotGreater | | |
| orGreater | | |
| orNotGreater | | |
| less | | | 
| andLess | | | 
| notLess | | | 
| andNotLess | | | 
| orLess | | | 
| orNotLess | | | 
| between | | |
| andBetween| | |
| andNotBetween| | |
| orBetween| | |
| orNotBetween| | |
| betweenEquals | | |
| andBetweenEquals | | |
| andNotBetweenEquals | | |
| orBetweenEquals | | |
| orNotBetweenEquals | | |

### Restricting by value matching

| Method | Description | Example |
|------|-------------|---------|
| contains | | | 
| andContains | | |
| andNotContains | | |
| orContains | | |
| orNotContains | | |
| empty | | | 
| andEmpty | | |
| andNotEmpty | | |
| orEmpty | | |
| orNotEmpty | | |
| match | | |
| andMatch | | |
| andNotMatch | | |
| orMatch | | |
| orNotMatch | | |

### Restricting by value type

| Method | Description | Example |
|------|-------------|---------|
| type | | |
| andType| | |
| andNotType| | |
| orType| | |
| orNotType| | |

| Method | Description | Example |
|------|-------------|---------|
| is | | |
| andIs | | |
| andNotIs | | |
| orIs | | |
| orNotIs | | |
| or | | |
| and | | |
| not | | |
| andNot | | | 
| orNot | | |

### Changing the current result set

| Method | Description | Example |
|------|-------------|---------|
| each | | |
| intersect | | |
| cartesian | | |
| except | | | 
| union | | |
| attach | | |
| sort | | |
| assign | | |
| join | | | 
| skip | | |
| take | | |
| skipTake | | |
| define | | |
| removed | | |
| stream | | |
| streamFn | | |

## SELECT

| Method | Description | Example |
|------|-------------|---------|
| select | Returns all fields from the original array | ````$from(anArray).select()```` |
| select (selected fields) | Returns specific fields with corresponding default values | ````$from(anArray).select({ f1: "n/a", f2: false })````
| select (transform function) | Returns the result of the transformation function | ````$from(anArray).select(r => ({ f1: r.f1, f2: r.a1 + r.a2 }))```` |
| min | Returns the minimum value of a field from the result | ````$from(anArrayOfTemperatures).min("temperature")```` |
| max | Returns the maximum value of a field from the result | ````$from(anArrayOfTemperatures).max("temperature")```` |
| average | Returns the average value of a field from the result | ````$from(anArrayOfTemperatures).average("temperature")```` |
| sum | Returns the sum value of a field from the result | ````$from(anArrayOfFiles).sum("size")```` |
| distinct | Returns an array of distinct values for a specific field from the result | ````$from(anArrayOfMeasures).distinct("measureName")```` |
| group | Returns a map grouping the array records by a specific field from the result | ````$from(anArrayOfTemperatures).group("city")```` |
| at | Returns a single entry of the result set | ````$from(anArray).at(23)```` |
| all | Returns true if all records from the original array are present on the final result set (false otherwise) | ````$from(anArray).all()```` |
| count | Returns the number of records of the final result set | ````$from(anArray).count()```` |
| first | Returns the first record of the final result set | ````$from(anArray).first()```` |
| last | Returns the last record of the final result set | ````$from(anArray).last()```` |
| any | Returns true if the result set has any record at all (false otherwise) | ````$from(anArray).any()```` |
| none | Returns true if the result set is empty (false otherwise) | ````$from(anArray).none()```` |
| reverse | Returns a reverse order result set | ````$from(anArray).reverse()```` |
| limit | Returns just a limited amount of records of the result set | ````$from(anArray).limit(5)```` |
| head | Returns a limited amount of the first records of the result set | ````$from(anArray).head(10)```` |
| tail | Returns a limited amount fo the last records of the result set | ````$from(anArray).tail(10)```` |


### Simple select

Return the current result set with the WHERE part applied:

````javascript
var result = $from([ 1, 2, 3 ]).select();
// [ 1, 2, 3 ]
````

### Select the fields

Return the current result set with the WHERE part restricting each map entry on the result to the fields provided and their default values in case they are not present:

````javascript
var inData = [ 
    { name: "Point 1", x: 1, y: -1 }, 
    { name: "Point 2", x: 5, y: -5 },
    { x: 3 }
]; 
var result = $from(inData).select({ x: 0, y: 0 });
// [ { x: 1, y: -1 },
//   { x: 5, y: -5 },
//   { x: 3, y: 0  } ]
````

### Transform function

The result set will be transformed by the provided function:

````javascript
var inData = [
    { name: "Vector 1", x1: 2, y1: -1, x2: 5, y2: -10 },
    { name: "Vector 2", x1: -2, y1: -1, x2: 5, y2: 10 }
];
var result = $from(inData).select(r => {
    var newResult = { name: r.name };

    newResult.distance = Math.round( Math.sqrt( Math.pow(r.x1-r.x2, 2) + Math.pow(r.y1-r.y2, 2)));

    return newResult;
});
// [ { name: "Vector 1", distance: 9 },
//   { name: "Vector 2", distance: 13} ]
````

# Other libraries in OpenAF

* _$path_ - Based on the [JMESPath library](http://jmespath.org) ([see more](OpenAF-path.md))
* _$stream_ - Based on the old [StreamJS library](https://github.com/winterbe/streamjs)

## Other query engines

Compare nLinq with [JMESPath and the Java `$path` backend](../guides/advanced/path-java.md), or [jq through `$jq`](../guides/advanced/jq.md). The APIs have different syntax, ordering, and value semantics.
