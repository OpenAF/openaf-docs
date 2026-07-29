---
layout: default
title: $path
parent: Concepts
grand_parent: OpenAF docs
---

# $path

There are several "helpers" in OpenAF to help to "query" array of maps that help to make code cleaner. For a complete list (like $from) see on the end of this document.

_$path_ is based on [JMESPath library](http://jmespath.org) that makes it pratical to perform queries with just a string query but can be difficult to "read". To help understanding JMESPath where is a quick guide.

## Input

_$path_ can be used to query both javascript maps and arrays. Let's use an example of a map with an array that you can easily replicate:

````javascript
var obj = io.listFiles(getOpenAFPath())
````

Now you can access the _files_ array of the resulting map _obj_ as well as any of the maps inside the _files_ array:

````javascript
isMap( obj )
// true
isArray( $path(obj, "files") )
// true
isMap( $path(obj, "files[0]") )
// true
$path(obj, "files[0].filename")
// openaf-sb
````

## Queries

There are 6 main categories of queries:

| Category | Description |
|:---------|:------------|
| __Slicing__ | When querying arrays it's possible to _"slice"_ them in different ways (examples: the first five; from the third to the fifth; the first two; the last element; etc.). |
| __MultiSelect__ | As with projections it's also possible to _"project"_ multiple fields. |
| __Filters__ | It's possible to apply simple conditions (including using functions) to query an array. |
| __Projections__ | Given the inputs it's possible to _"project"_ any fields necessary even if in keys. |
| __Pipe__ | Using the same unix "pipe" mechanism it's possible to apply different categories of queries in sequence. |
| __Functions__ | It's possible to apply a set of built-in functions over the queried fields and use the result also to build _"filters"_ |

### Slicing

Slicing arrays makes it easy to filter for specific records on an array:

````javascript
$path([1,2,3,4,5,6,7,8,9,10], "[0:5]")
// [1, 2, 3, 4, 5]
$path([1,2,3,4,5,6,7,8,9,10], "[::2]")
// [1, 3, 5, 7, 9]
$path([1,2,3,4,5,6,7,8,9,10], "[::3]")
// [1, 4, 7, 10]
$path([1,2,3,4,5,6,7,8,9,10], "[::-1]")
// [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
$path([1,2,3,4,5,6,7,8,9,10], "[::-2]")
// [10, 8, 6, 4, 2]
$path([1,2,3,4,5,6,7,8,9,10], "[-1]")
// 10
$path([1,2,3,4,5,6,7,8,9,10], "[-5::]")
// [6, 7, 8, 9, 10]
$path([1,2,3,4,5,6,7,8,9,10], "[-5::2]")
// [6, 8, 10]

$path(obj, "files[0:5]")   // or $path(obj.files, "[0:5]")
// An array with the first 5 elements
$path(obj, "files[:5]")
// Again, the same array with the first 5 elements
````

### Multi-select

Given an input if nothing is specified all fields will be output. If you provide a specific field, only that one will be output. But it's possible to specify multi-fields:

````javascript
$path(obj, "files[].[filename, size]")
// an array where each element is another array where the first value is _filename_ and the second is _size_
$path(obj, "files[].{f: filename, s: size}")
// an array where each element is a map where _f_ is the value of 'filename' and _s_ is the value of 'size'
````

### Filter

Given an input it's possible to use the existing fields to filter the result:

````javascript
$path(obj, "files[?size>`1000000`]")
// an array with the files whose size is bigger than 1MB
$path(obj, "files[?filename=='openaf.jar']")
// an array with one entry where filename is "openaf.jar"
$path(obj, "files[?filename=='openaf.jar'].size")
// an array with one entry with the size value of the filename is "openaf.jar"
````

### Projections

Projecting specific fields from an array of maps:

````javascript
$path(obj, "files[].filename")
// An array of each value of "filename" on the "files" array
$path([ { x: 1, y: -1 },  {x: 2, y: 2 } ], "[].x")
// [1, 2]
$path({ x: 1, y: -1, z: 0 }, "*")
// [1, -1, 0]
$path([ { point: { x: 1,y: -1 }, level: { x: -99, y: 99 } }, { point: {x: 2, y: 2 } } ], "[].*.x")
// [[ 1, -99], [ 2 ]]
````

### Pipe

Very quickly you might need to apply a sequence of filters, slicing, multi-selects and projections:

````javascript
$path(obj, "files[?size>`1000000`] | [?filename=='openaf.jar']")
// An array with the element whose 'filename' is "openaf.jar" and whose 'size' is bigger than 1MB
$path(obj, "files[?size>`1000000`] | [?filename=='openaf.jar'] | [0]")
// The first element of an array with the element whose 'filename' is "openaf.jar" and whose 'size' is bigger than 1MB
$path(obj, "files[?size>`1000000`] | [?filename=='openaf.jar'] | [0].filename")
// The 'filename' of the first element of an array with the element whose 'filename' is "openaf.jar" and whose 'size' is bigger than 1MB
$path(obj, "files[?size>`1000000`] | [?filename=='openaf.jar'] | [0] | @.filename")
// Same as the previous result
````

### Functions

It's possible to apply functions to fields and arrays on the expression used in _$path_:

| Function | Description | Example |
|:---------|:------------|:--------|
| abs(number) | The absolute value of a numeric field | ````$path([{x:1,y:-1},{x:2,y:2}], "[].{y:abs(y)}")````|
| avg(arrayNumber) | The average value of an array of numeric fields | ````$path([ {x:1,y:-1}, {x:2,y:2} ], "avg([].y)")```` |
| contains(string/array, any) | Returns true of false if a string field contains a specific value | ````$path(obj, "files[?contains(filename, 'openaf.jar') == `true`")````
| ceil(numer) | Returns the smallest integer that is equal or less than a specific numeric field value | ````$path([{x: 1.2, y: -1.8},{x: 2.2, y: 2.0}], "[].ceil(y)")```` |
| ends_with(string, array) | Returns true if a field has the provided suffix | ````$path(obj, "files[?ends_with(filename, '.jar')]")```` |
| floor(number) | Returns the greatest integer that is equal or greater than a specific numeric field value | ````$path([ {x:1.2,y:-1.8}, {x:2.2,y:2.0} ], "[].floor(y)")```` |
| join(string, arrayString) | Returns a delimited list with the values of a specific array field | ````$path(obj, "join(', ', files[].filename)")````|
| keys(object) | Returns a list of fields for a corresponding map | ````$path(obj, "keys(files[0])")```` |
| length(string/array/object) | Returns the size of any array or list | ````$path(obj, "length(keys(files[0]))")```` |
| map(expression, array) | Returns an array mapping  | ````$path(obj, "map(&filename == 'openaf.jar', files[])"```` |
| max(number) | Returns the maximum of a numeric field | ````$path(obj, "max(files[].size)")```` |
| max_by(array, expression) | Returns the element for which the expression is the maximum | ````$path(obj, "max_by(files[], &size)")```` |
| merge(object, object) | Returns the merge of two objects | ````$path([{x:1},{y:0}], "merge([0],[1]))```` |
| min(number) | Returns the minimum of a numeric field | ````$path(obj, "min(files[].size)")```` |
| min_by(array, expression) | Returns the element for which the expression is the minimum | ````$path(obj, "min_by(files[], &size)")```` |
| not_null(any) | Returns the non-null value between the provided fields | ````$path([{a:null,b:1}, {a:2,b:null}], "[].not_null(a,b)")```` |
| reverse(array) | Reverse the provided array | ````$path([1,2,3], "reverse(@)")```` |
| sort(array) | Sorts the provided array | ````$path([3,1,2], "sort(@)")````
| sort_by(array, expression) | Sorts the provided array by the provided expression | ````$path(obj, "sort_by(files[], &size)")```` |
| starts_with(string, array) | Returns true if a field has the provided prefix | ````$path(obj, "files[?starts_with(filename, 'openaf.jar')]")```` |
| sum(array) | Sums the numberic field of a provided array | ````$path(obj, "sum(files[].size)")```` |
| to_array(any) | Transforms any input into an array | ````$path(obj, "to_array(`true`)")```` |
| to_string(any) | Transforms any input into a string | ````$path(obj, "to_string(`123`)")```` |
| to_number(any) | Transforms any input into a number | ````$path(obj, "to_number(`123`)")```` |
| type(any) | Returns the type of any input | ````$path(obj, "type(to_number(`123`))")```` |
| values(a) | Returns an array with all the values of a map | ````$path(obj, "values(files[0])")```` |

### 🧠 Custom JMESPath functions in OpenAF

These are **extra functions** added to the standard JMESPath syntax — think of them as a fusion between JMESPath and JavaScript power, tailored for data transformation.

🧰 **Popular & Useful Custom Functions**

| Function | Description | Example |
|:---------|:------------|:--------|
| ```amerge(x, y)``` | Deep merge two objects/arrays | ```amerge({a:1}, {b:2})``` → {a:1,b:2} |
| ```assign(obj, path, val)``` | Mutate/assign a value in an object at a path | ```assign([0], "status", "done")``` |
| ```assignp(pathExpr, key, val)``` | Assign using a path query | ```assignp('[?id=1]', "valid", true)``` |
| ```a2m(keys, values)``` | Create a map from two arrays | ```a2m(["k1","k2"], [1,2])``` → {k1:1,k2:2} |
| ```a4m(arr, "key")``` | Convert array to map using a field as key | ```a4m([{id:1},{id:2}], "id")``` |
| ```concat(x, y)``` | Concatenate two arrays or strings | ```concat("foo", "bar")``` → "foobar" |
| ```ch(name, op, arg1, arg2)``` | Interact with a channel (etcd, mvs, etc.) | ```ch("mych", "get", "key")``` |
| ```chq(name, op, max, value)``` | Queue semantics (push/pop/shift/size/get) backed by a named channel | ```chq("__events", "push", `3`, @)``` |

> Check more in [oAFp filters](../guides/oafp/oafp-filters.md)

### 🔌 **Using ch() in oafp for OpenAF channels access**

The ch(name, op, ...) function lets you interact with any OpenAF-supported channel directly from a JMESPath expression.

**🔧 Function Signature**

```javascript
ch("channelName", "operation", arg1?, arg2?)
```

| Parameter | Meaning | 
|:---------|:--------|
| channelName | The name of the channel you want to interact with. |
| operation | The operation you want to perform on the channel. One of: get, set, unset, size, unsetAll, getAll, getKeys |
| arg1 / arg2 | Additional arguments, Key/value or additional data depending on the operation. |

**🔁 Operations**

| Operation | Description |
|:---------|:------------|
| ```get``` | Get a value by key |
| ```set``` | Set a value by key |
| ```unset``` | Delete a key |
| ```getAll``` | Get entire key-value map |
| ```getKeys``` | List all keys |
| ```unsetAll``` | Delete all keys |
| ```size``` | Get total number of keys |

**🧪 Examples using oafp**

✅ *Set a key in MVStore*

```bash
oafp data='[{id: 1, name: "Alice"}]' in=json\
  chs="(type: mvs, options: (file: db.mvs))"\
  path="ch('store', 'set', 'user:1', [0])"
```

Then check the data on MVStore:

```bash
oafp in=ch inch="(type: mvs, options: (file: db.mvs))" data="()" inchall=true
```

🔍 *Get all keys from etcd*

```bash
oafp in=ch inch="(type: etcd3, options: (host: localhost, port: 2379), lib: 'etcd3.js')" inchall=true data="()" out=ndjson
```

🧹 *Delete a specific key*

```bash
oafp chs="(name: store, type: mvs, options: (file: db.mvs))"\
     path="ch('store', 'unset', '(user:1)', '')"\
     data="()"
```

📥 *Get a value from Redis*

```bash
oafp chs="(name: cache, type: redis, options: (host: redis.local, port: 6379))"\
     path="ch('cache', 'get', '(session: abc)')"
     data="()"
```

### 🔌 **Using chq() for channel-backed queues**

`chq(name, op, max, value)` gives `$path(...)` expressions queue semantics (push/pop/shift/size/get) backed by an
auto-created "simple" channel named `name`. It is a lightweight alternative to writing imperative channel code when an
expression just needs a rolling buffer or event queue.

**🔧 Function Signature**

```javascript
chq(channelName, operation, max, value?)
```

| Parameter | Meaning |
|:---------|:--------|
| channelName | The name of the (auto-created if missing) backing channel. |
| operation | One of: push (alias add), pop, shift, size, get (alias all). |
| max | For push, the maximum number of entries to retain (oldest entries are shifted out once exceeded). Ignored for other operations. |
| value | The value to push. Required for push/add, ignored otherwise. |

**🧪 Examples**

```javascript
$path({ id: 1 }, "chq('__events', 'push', `3`, @)");  // push into queue, keep at most 3 entries
$path({}, "chq('__events', 'size', `3`, @)");         // current queue size
$path({}, "chq('__events', 'get', `3`, @)");          // full queue contents
$path({}, "chq('__events', 'shift', `3`, @)");        // remove oldest entry
$path({}, "chq('__events', 'pop', `3`, @)");          // remove newest entry
```

# Other libraries in OpenAF

* _$from_ - See more in [$from](OpenAF-nLinq.md)
* _$stream_ - Based on the old [StreamJS library](https://github.com/winterbe/streamjs)