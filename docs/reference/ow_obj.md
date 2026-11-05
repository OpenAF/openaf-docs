---
layout: default
title: ow.obj
parent: Reference
grand_parent: OpenAF docs
---

{% raw %}
## ow.obj

[Source: `06414cd9`](https://github.com/OpenAF/openaf/blob/06414cd9204e918daa1e2971ce904783299db333/js/owrap.obj.js) · [Baseline](../source-snapshot.md)

### ow.obj.big.create

`ow.obj.big.create(shouldCompressKeys) : Object`

Creates a "big" map object that compresses contents in memory. Optionally if `shouldCompressKeys` = true
the key map will also be compressed. See also:

- `ow.obj.big.set`
- `ow.obj.big.setAll`
- `ow.obj.big.get`
- `ow.obj.big.find`

### ow.obj.big.find

`ow.obj.big.find(aFunction) : Array`

````text
Will execute the provided aFunction providing each key available. For the keys where the function returns true the corresponding value will be gathered into the final resulting array.
````

### ow.obj.big.get

`ow.obj.big.get(aKeyMap) : Map`

Retrieves a value map given the provided `aKeyMap`.
Example:

```javascript
var big = ow.obj.big.create();
var data = [
        {"name": "Anne", "country": "USA", "company": "Wedo"},
        {"name": "Rui", "country": "Portugal", "company": "Wedo"},
        {"name": "Paulo", "country": "Portugal", "company": "Sonae"},
        {"name": "Peter", "country": "USA", "company": "ACME"},
        {"name": "Louis", "country": "USA", "company": "ACME"}
];
big.setAll(["name"], data);
big.get({"name": "Rui"}); // {"name": "Rui", "country": "Portugal", "company": "Wedo"}
```

### ow.obj.big.getSize

`ow.obj.big.getSize() : Number`

````text
Returns the current number of keys available.
````

### ow.obj.big.remove

`ow.obj.big.remove(aKeyMap)`

````text
Removes aKeyMap and corresponding value.
````

### ow.obj.big.set

`ow.obj.big.set(aKeyMap, aValueMap, aTimestamp)`

Sets `aValueMap` associated with a `aKeyMap`. Optionally you can set the internal `aTimestamp` for the record.
Example:

```javascript
var big = ow.obj.big.create();
big.set({"name": "Anne"}, {"name": "Anne", "country": "USA", "company": "Wedo"});
```

### ow.obj.big.setAll

`ow.obj.big.setAll(anArrayKeyNames, anArrayOfValues, aTimestamp)`

Given `anArrayOfValues` will set them internally using the keys on `anArrayKeyNames` to define
the corresponding keys. Optionally you can set the internal `aTimestamp` for the record.

Example:

```javascript
var big = ow.obj.big.create();
var data = [
        {"name": "Anne", "country": "USA", "company": "Wedo"},
        {"name": "Rui", "country": "Portugal", "company": "Wedo"},
        {"name": "Paulo", "country": "Portugal", "company": "Sonae"},
        {"name": "Peter", "country": "USA", "company": "ACME"},
        {"name": "Louis", "country": "USA", "company": "ACME"}
];
big.setAll(["name", "country"], data);
```

### ow.obj.diff

`ow.obj.diff(aOriginalJSON, aFinalJSON, optionsMap) : String`

Produces a string representation of the difference between `aOriginalJSON` and `aFinalJSON`.

Use `optionsMap` to control the output:

- `printColor: true`: immediately prints with ANSI colors when available.
- `justAnsi: true`: produces ANSI color codes without printing.
- `justChanges: true`: represents only the changed lines with the rest.
- `justDiff: true`: includes only the changed lines.

### ow.obj.filter

`ow.obj.filter(anObject, aMap) : Object`

Given `anObject` (either a map or array) will use `$from` with the options on `aMap` basically making all `$from` options map parameters.
If a "path" string is included it will fallback to `$path`. Example:

```yaml
filter:
  #fromKey: arr
  where:
  - cond: equals
    args:
    - isFile
    - true
  transform:
  - func: attach
    args:
    - lastAccess
    - !!js/eval elem => new Date(elem.lastAccess)
  - func: sort
    args:
    - "-size"
  select:
    filename: n/a
    size    : -1
  #selector:
  #  func: at
  #  args:
  #  - 0
```

### ow.obj.filterKeys

`ow.obj.filterKeys(anArrayKeyNames, aMap) : Map`

````text
Given aMap will return an equivalent Map with only the keys contained in the anArrayKeyNames. Note: doesn't traverse existing sub-maps.
````

### ow.obj.flatMap

`ow.obj.flatMap(data, separator) : Array/Map`

````text
Given data as an array of maps or a single map tries to produce an output with only one level of keys per map. Optionally you can provide a separator between parent keys and each key (defaults to '.').
````

### ow.obj.flatten

`ow.obj.flatten(arrayOfMaps, aSeparator, aNADefault) : Array`

````text
Converts any structured arrayOfMaps into a flat array of maps with only one level of keys. The map key path will be converted into a single key using aSeparator (defaults to "_") and the value will be represented as aNADefault (defaults to "") when no  value or key exists in other entries. For each array entry a new array element will be created replicated all other keys. Useful to convert data to output into CSV for example. Nested arrays of scalar values use the full parent path as their column name. aSeparator is literal, including regular-expression characters.
````

### ow.obj.fromArray2DB

`ow.obj.fromArray2DB(anArray, aDB, aDBTable, useParallel, caseSensitive, errorFn) : Number`

````text
Given anArray composed of maps where each key is a field name tries to insert into the aDBTable for a provided aDB. Optionally you can specify how many threads should be used with useParallel and use the case sensitive name of fields with caseSensitive = true. The errorFn, if defined, will be called with the exception, the sql statement and the value that caused the exception. This function doesn't perform any database commit. Returns the number of records inserted. (available after ow.loadObj())
````

### ow.obj.fromArray2Obj

`ow.obj.fromArray2Obj(anArray, aKey, dontRemove) : Array`

Tries to create a map of maps from the provided `anArrays`. Optionally if `aKey` is provided
it will be used to create the map keys (otherwise will fallback to "row[number]"). And can also
optionally indicate by `dontRemove` = true that `aKey` shouldn't be removed from each map.

```javascript
var a = [
  { "abc": "123", "xpt": "000", "key": "A1" },
  { "abc": "456", "xpt": "001", "key": "A2" },
  { "abc": "789", "xpt": "002", "key": "A3" }
]

fromArray2Obj(a, "key");
// {
//   "A1": { "abc": "123", "xpt": "000" },
//   "A2": { "abc": "456", "xpt": "001" },
//   "A3": { "abc": "789", "xpt": "002" }
// }
```

### ow.obj.fromArray2OrderedObj

`ow.obj.fromArray2OrderedObj(anArray) : Map`

````text
Converts the provided anArray into a Map where each array entry is converted to a map entry  which ordered will provide the same ordering found on the array. (available after ow.loadObj())
````

### ow.obj.fromDBRS

`ow.obj.fromDBRS(aDB, aSQL, anArrayOfBinds, aFunction, anErrorFunction)`

````text
Given a connected aDB the query aSQL will be executed (using the anArrayOfBinds) and the corresponding result set will be iterated. For each row the aFunction will be  called with the result of ow.obj.fromDBRS2Obj with doDates = true. If the function returns false the result set iteration will be immediatelly stopped. Any exception  thrown by aFunction will be handled by anErrorFunction (by default throws the exception).
````

### ow.obj.fromDBRS2Obj

`ow.obj.fromDBRS2Obj(aDBRS, doDates) : Map`

````text
Converts a Java database result set object (retrieved with DB.qsRS) into a map where the key is the name of the field in upper case. Optionally doDates will convert any SQL dates into javascript Date objects.
````

### ow.obj.fromJson

`ow.obj.fromJson(aJson) : Object`

Creates an object or objects, using the `aJson` and the indication of the object prototypes to use. This is based on JMix from
https://github.com/khayll/jsmix.
Example:

```javascript
var Point = function() {};
Point.prototype.getX = function() { return this.x; }
Point.prototype.getY = function() { return this.y; }

ow.obj.fromJson({ x: 1, y: 2 }).withObject(Point.prototype).build().getX(); // 1

var mylines = { "lines": [
   { "name": "line 1", "points": [ { x: 0, y: 0}, { x: 5, y: 6} ] },
   { "name": "line 2", "points": [ { x: -5, y: -5}, { x: 1, y: 3} ] },
]};

var res = ow.obj.fromJson(mylines).withObject(Point.prototype, "lines.*.points.*").build();
res.lines[1].points[1].getY(); // 3
```

### ow.obj.fromObj2Array

`ow.obj.fromObj2Array(anObj, aKey) : Array`

Tries to create an array of maps from the provided `anObj` map of maps. Optionally if `aKey` is provided
it will be added to each array map with the map key. Example:

```javascript
var a = {
   "A1": { "abc": "123", "xpt": "000" },
   "A2": { "abc": "456", "xpt": "001" },
   "A3": { "abc": "789", "xpt": "002" }
}

fromObj2Array(a, "key");
// [
//  { "key": "A1", "abc": "123", "xpt": "000" },
//  { "key": "A2", "abc": "456", "xpt": "001" },
//  { "key": "A3", "abc": "789", "xpt": "002" }
// ]
```

### ow.obj.fromObj2DBTableCreate

`ow.obj.fromObj2DBTableCreate(aTableName, aMapOrArray, aOverrideMap, enforceCase) : String`

````text
Returns a DB table create, for aTableName, from the provided aMapOrArray (only a few entries) key entries. To override the default field type guessing a aOverrideMap can  be provided with field entries and the corresponding type as value. Optionally if enforceCase = true table name and fields names will be enforced case by using double quotes.
````

### ow.obj.fromOrderedObj2Array

`ow.obj.fromOrderedObj2Array(aMap, aKeySortFunction) : Array`

````text
Converts a provided aMap into an array where each element will be composed from the maps entries ordered by the corresponding key. Optionally you can provide aKeySortFunction that will accept two arguments and work similarly to javascript's array sorting functions. (available after ow.loadObj())
````

### ow.obj.fuzzySearch

`ow.obj.fuzzySearch(anArrayOfKeys, anArrayOfObjects, searchString, fuseOptions) : Array`

Given `anArrayOfObjects` (similar objects) will fuzzy search the `searchString` on the values for the keys in `anArrayOfKeys`.
Returns an array of the most probable objects to match the `searchString` (you can use `fuseOptions` = { shouldSort: true } to
ensure that the array is ordered by score).
It uses the FuseJS library internally so `fuseOptions` can be used to add more options (check more in http://fusejs.io/).

For example:

```javascript
ow.obj.fuzzySearch(["n"], [{n: "World War I"}, {n: "World War II"}, {n: "Name a war"}, {n: "Name some war"}], "world");
```

### ow.obj.getPath

`ow.obj.getPath(aObject, aPath) : Object`

Given `aObject`, retrieves the value at `aPath` using dot notation or unquoted bracket indexes.
Returns undefined if a key is absent or an intermediate value is null, undefined or a scalar.
A null or scalar at the final path segment is returned unchanged. Example:

```javascript
var a = { a : 1, b : { c: 2, d: [0, 1] } };

print(ow.obj.getPath(a, "b.c")); // 2
sprint(ow.obj.getPath(a, "b.d")); // [0, 1]
print(ow.obj.getPath(a, "b.d[0]")); // 0
```

### ow.obj.http

`ow.obj.http(aURL, aRequestType, aIn, aRequestMap, isBytes, aTimeout, returnStream, options) : Object`

Creates a new instance of an HTTP client to be used to execute a request to `aURL` using `aRequestType` (GET, POST, PUT, DELETE, HEAD, PATCH, OPTIONS, TRACE).
Optionally you can provide `aIn` (the body of the request), `aRequestMap` (a map with the headers), `isBytes` (if the body is bytes), `aTimeout` (timeout in milliseconds),
`returnStream` (if the response should be a stream) and `options`, a map with the following keys:

- `timeout`: the connection timeout in milliseconds
- `readTimeout`: the read timeout in milliseconds
- `writeTimeout`: the write timeout in milliseconds
- `callTimeout`: the call timeout in milliseconds
- `followRedirects`: if should follow redirects
- `followSslRedirects`: if should follow ssl redirects
- `delayBuild`: if should delay the build of the client

Example:

```javascript
var http = ow.obj.http("http://www.google.com", "GET");
var res = http.exec();
```

### ow.obj.http.close

`ow.obj.http.close()`

````text
Closes the current http connection response (if any) and releases any pooled connections kept open by this http client (useful when a single http object is reused, e.g. through options.httpClient, to ensure idle keep-alive connections aren't left open).
````

### ow.obj.http.exec

`ow.obj.http.exec(aURL, aRequestType, aIn, aRequestMap, isBytes, aTimeout, returnStream, options) : Object`

````text
Executes a request to aURL with the provided aRequestType, aIn, aRequestMap, isBytes, aTimeout and returnStream. Optionally you can provide options. Returns a map with the response code, the content type and the response.
````

### ow.obj.http.get

`ow.obj.http.get(aURL, aIn, aRequestMap, isBytes, aTimeout, returnStream, options) : Object`

````text
Executes a GET request to aURL with the provided aIn, aRequestMap, isBytes, aTimeout and returnStream. Optionally you can provide options. Returns a map with the response code, the content type and the response.
````

### ow.obj.http.getBytes

`ow.obj.http.getBytes(aURL, aIn, aRequestMap, aTimeout, options) : Object`

````text
Executes a GET request to aURL with the provided aIn, aRequestMap, aTimeout and options. Returns the response as bytes.
````

### ow.obj.http.getCookieStore

`ow.obj.http.getCookieStore() : String`

````text
Returns the current cookie store name channel.
````

### ow.obj.http.getErrorResponse

`ow.obj.http.getErrorResponse(parseJson) : Object`

````text
Returns the response object with the response and responseBytes parsed as JSON if parseJson is true.
````

### ow.obj.http.getResponse

`ow.obj.http.getResponse() : Object`

````text
Returns the response object.
````

### ow.obj.http.getStream

`ow.obj.http.getStream(aURL, aIn, aRequestMap, aTimeout, options) : Object`

````text
Executes a GET request to aURL with the provided aIn, aRequestMap, aTimeout and options. Returns the response as a stream.
````

### ow.obj.http.head

`ow.obj.http.head(aURL, aIn, aRequestMap, isBytes, aTimeout) : Map`

````text
Executes a HEAD request to aURL with the provided aIn, aRequestMap, isBytes and aTimeout. Returns a map with the response headers.
````

### ow.obj.http.login

`ow.obj.http.login(aUser, aPassword, forceBasic, urlPartial)`

````text
Sets the login credentials to be used with the next request. If forceBasic is true it will always use basic authentication.
````

### ow.obj.http.post

`ow.obj.http.post(aURL, aIn, aRequestMap, isBytes, aTimeout, returnStream, options) : Object`

````text
Executes a POST request to aURL with the provided aIn, aRequestMap, isBytes, aTimeout and returnStream. Optionally you can provide options. Returns a map with the response code, the content type and the response.
````

### ow.obj.http.response

`ow.obj.http.response() : String`

````text
Returns the response as a string.
````

### ow.obj.http.responseBytes

`ow.obj.http.responseBytes() : Object`

````text
Returns the response as bytes.
````

### ow.obj.http.responseCode

`ow.obj.http.responseCode() : Number`

````text
Returns the response code.
````

### ow.obj.http.responseHeaders

`ow.obj.http.responseHeaders() : Map`

````text
Returns the response headers.
````

### ow.obj.http.responseStream

`ow.obj.http.responseStream() : Object`

````text
Returns the response as a stream.
````

### ow.obj.http.responseType

`ow.obj.http.responseType() : String`

````text
Returns the response content type.
````

### ow.obj.http.setCookieStore

`ow.obj.http.setCookieStore(aCh)`

````text
Sets the cookie store channel to be used with the current http object.
````

### ow.obj.http.setThrowExceptions

`ow.obj.http.setThrowExceptions(should)`

````text
Sets if the http object should throw exceptions or not.
````

### ow.obj.http.upload

`ow.obj.http.upload(aName, aFile)`

````text
Sets the file to be uploaded with the next request.
````

### ow.obj.http0.close

`ow.obj.http0.close()`

````text
Closes the current http connection response (if any) and shuts down the underlying Apache HTTP client, releasing any pooled connections it may be keeping open. The object remains usable afterwards: the next exec() call will transparently build a new underlying client.
````

### ow.obj.isSigned

`ow.obj.isSigned(aMap) : boolean`

````text
Verifies if the provided aMap was signed with ow.obj.sign function.
````

### ow.obj.key2array

`ow.obj.key2array(aMap, aREMatch, outkey, removeEmptys) : Object`

````text
Given aMap will return an array of values where the keys match the aREMatch regular expression. Optionally you can provide an outkey to have return map with a key with the resulting array. If removeEmptys is true it will remove any undefined, null or empty values.
````

### ow.obj.oneOf

`ow.obj.oneOf(anArray, aWeightField) : Object`

````text
Chooses a random object from the provided anArray. If aWeightField is provided that field should be  present in each object of anArray and it will be used to "weight" the probability of that element being choosen randomly.
````

### ow.obj.oneOfFn

`ow.obj.oneOfFn(anArrayFn, aWeightField) : Object`

````text
Equivalent to ow.obj.oneOf but each object is expected to have a field "fn" which should be a function. A random  object will be choosen and the corresponding function (fn) will be called. If aWeightField is provided that field should be  present in each object of anArray and it will be used to "weight" the probability of that element being choosen randomly.
````

### ow.obj.pmSchema.applySchema

`ow.obj.pmSchema.applySchema(aJavaPM, aSchema) : JavaParameterMap`

````text
Given aSchema (produced by ow.obj.pmSchema.fromJavaParameterMap) and aJavaPM (a Java Parameter Map) it  corrects the types where needed (for example: enforce that a integer should really be a long). The corrected Java Parameter Map is returned. If aJavaPM is not a Java Parameter Map it will try to convert to Map and return an output Map instead of JavaParameterMap.
````

### ow.obj.pmSchema.getSchema

`ow.obj.pmSchema.getSchema(aJavaPM) : Map`

````text
Builds a type schema from the provided aJavaPM (a Java Parameter Map) to be used with  ow.obj.pmSchema.toJavaParameterMap to enforce a schema of types. If aJavaPM is not a Java Parameter Map it will try to convert to one from a Map.
````

### ow.obj.pmSchema.makeKey

`ow.obj.pmSchema.makeKey(aJavaPM) : String`

````text
Produces a key for the aJavaPM (a Java parameter map or Map) to identify the provided map in a pmSchema when using ow.obj.applySchema.
````

### ow.obj.pool.AF

`ow.obj.pool.AF(url, timeout, conTimeout, dontUseTransaction)`

````text
Creates a pool setting with ow.obj.pool.setFactoryAF.
````

### ow.obj.pool.DB

`ow.obj.pool.DB(driver, url, login, pass, keepAliveFn, timeout)`

````text
Creates a pool setting with ow.obj.pool.setFactoryDB.
````

### ow.obj.pool.RAIDDB

`ow.obj.pool.RAIDDB(aAF, con, keepAlive, url, pass, useCIR, driver)`

````text
Creates a pool setting with ow.obj.pool.setFactoryRAIDDB.
````

### ow.obj.pool.SSH

`ow.obj.pool.SSH(host, port, login, pass, idkey, withCompression)`

````text
Creates a pool setting with ow.obj.pool.setFactorySSH.
````

### ow.obj.pool.add

`ow.obj.pool.add(aObject, inUse)`

````text
Adds aObject to the current pool. Optionally you can indicate if it should be add has checkout (inUse = true).
````

### ow.obj.pool.checkIn

`ow.obj.pool.checkIn(aObject, shouldKeep)`

````text
Returns the aObject instance back to the pool removing the mark that is in use. If shouldKeep = false the object instance will be removed from the pool (trying to call the closeFunction and ignoring any exception).
````

### ow.obj.pool.checkOut

`ow.obj.pool.checkOut() : Object`

````text
Tries to obtain an object instance from the pool and returns it marking it as in use. Throws an exception if no object is available even after retrying.
````

### ow.obj.pool.create

`ow.obj.pool.create() : Object`

````text
Creates an object pool with the ability to provide objects produce by a factory method and to close the objects when needed (if defined to have minimum and maximum number of objects in the pool). It's possible also to define a keep alive function.
````

### ow.obj.pool.setFactory

`ow.obj.pool.setFactory(aFactoryFunction, aCloseFunction, aKeepaliveFunction)`

````text
Sets the functions to use to create new object instances with a aFactoryFunction (this function should return a new object instance each time is called). aCloseFunction to be called whenever an object instances needs to be terminated. And an optionally aKeepaliveFunction, that receives a object instances as an argument, and should perform the necessary procedures to keep the object instance "alive" (think connections that timeout after not being used for a long time).
````

### ow.obj.pool.setFactoryAF

`ow.obj.pool.setFactoryAF(anURL, aTimeout, aConnectionTimeout, dontUseTransaction)`

````text
Setups: a factory function to create an AF object using anURL and tries to send a Ping operation; a close function to close the AF object connection; a keep alive function that sends a Ping operation.
````

### ow.obj.pool.setFactoryDB

`ow.obj.pool.setFactoryDB(aDriver, aURL, aLogin, aPassword, aKeepAliveFunction, aTimeoutInMs)`

````text
Setups: a factory function to create an DB object using aDriver, aURL, aLogin and aPassword; a close function to close the DB object connection; a keep alive function that tries to execute a select from dual.
````

### ow.obj.pool.setFactoryRAIDDB

`ow.obj.pool.setFactoryRAIDDB(anAF, aConn, aKeepAlive, aURL, aPassword, useCIR, aDriver)`

````text
Setups: a factory function to create an DB object using anAF and aConn connection name from the RAID/WAF server; a close function to close the DB object connection; a keep alive function that tries to execute a select from dual (you can override this function providing aKeepAlive function that receives a database object as argument).
````

### ow.obj.pool.setFactorySSH

`ow.obj.pool.setFactorySSH(aHost, aPort, aLogin, aPass, anIdentificationKey, withCompression)`

````text
Setups: a factory function to create an SSH object using aHost, aPort, aLogin, aPass, anIdentificationKey, withCompression; a close function to close the SSH object connection; a keep alive function that tries to execute a command "true".
````

### ow.obj.pool.setIncrementsOf

`ow.obj.pool.setIncrementsOf(aNumberOfInstances)`

````text
Sets the number of increments in object instances on the pool in case that a new object instances is needed
````

### ow.obj.pool.setKeepalive

`ow.obj.pool.setKeepalive(aTimeInSeconds)`

````text
Sets the aTimeInSeconds for the keep alive function to be called for all object instances in the pool. After setting to aTimeInSeconds > 0 the keep alive cycle will be started. Otherwise any existing keep alive cycle will be stopped. Note: don't forget to use ow.obj.pool.stop to keep the keep alive thread from running after you no longer need it.
````

### ow.obj.pool.setKeepaliveInMs

`ow.obj.pool.setKeepaliveInMs(aTimeInMs)`

````text
Sets the aTimeInMs for the keep alive function to be called for all object instances in the pool. After setting to aTimeInMs > 0 the keep alive cycle will be started. Otherwise any existing keep alive cycle will be stopped. Note: don't forget to use ow.obj.pool.stop to keep the keep alive thread from running after you no longer need it.
````

### ow.obj.pool.setMax

`ow.obj.pool.setMax(aMaxNumberOfInstances)`

````text
Sets the maximum number of object instances the pool can have.
````

### ow.obj.pool.setMin

`ow.obj.pool.setMin(aNumberOfInstances)`

````text
Sets the minimum number of object instances the pool should have. These will be created upon ow.obj.pool.start.
````

### ow.obj.pool.setRetry

`ow.obj.pool.setRetry(numberOfRetries)`

````text
Sets the number of retries to obtain a free object from the pool.
````

### ow.obj.pool.setTimeout

`ow.obj.pool.setTimeout(aTimeoutInMs)`

````text
Sets a timeout in ms between each retry to obtain a free object from the pool.
````

### ow.obj.pool.start

`ow.obj.pool.start()`

````text
Starts the object pool by creating the minimal number of object instances.
````

### ow.obj.pool.stop

`ow.obj.pool.stop()`

````text
Stops the object pool closing all object instances and any keep alive cycle.
````

### ow.obj.pool.use

`ow.obj.pool.use(aFunction)`

````text
Executes aFunction providing, as an argument, an object instance from the pool (equivalent to ow.obj.pool.checkOut). After the execution the object instance will be returned to the pool (equivalent to ow.obj.pool.checkIn). If the aFunction returns false the provided object instance will be removed from the pool (interpreting as something is wrong  with it).
````

### ow.obj.randomDateRange

`ow.obj.randomDateRange(aFormat, aMin, aMax) : Date`

Generates a random date between `aMin` date string and `aMax` date string which the corresponding format is determined
by `aFormat`. For example:

```javascript
randomDateRange("yyyyMMdd hhmm", "19991231 2300", "20000101 0200");
```

### ow.obj.randomRange

`ow.obj.randomRange(min, max) : Number`

````text
Generates a random long number between min and max.
````

### ow.obj.reorderArrayMap

`ow.obj.reorderArrayMap(aKs, aArray, removeUnDefs) : Array`

````text
Given an array of keys (aKs) will project those for all maps in aArray (the ones not included with be included after). Optionally if removeUnDefs = true it will not include keys with undefined fields (evaluated for every map in the array).
````

### ow.obj.rest.create

`ow.obj.rest.create(aBaseURI, aIndexMap, aDataRowMap, aLoginOrFunction, aPassword, aTimeout, aRequestMap, urlEncode, aHTTP, retBytes, options) : String`

````text
Tries to create a new aDataRowMap entry, identified by aIndexMap, on the REST aBaseURI service returning the reply as a string (uses the HTTP POST method). Optionally you can provide aLogin, aPassword and/or aTimeout for the REST request or use a function (aLoginOrFunction) that receives the HTTP object. If urlEncode=true the aDataRowMap will be converted into x-www-form-urlencoded instead of JSON. Optionally if retBytes = true returns a java stream.
````

### ow.obj.rest.exceptionParse

`ow.obj.rest.exceptionParse(anException) : Map`

````text
Tries to parse the response of a rest call exception and the response also if it's json.
````

### ow.obj.rest.get

`ow.obj.rest.get(aBaseURI, aIndexMap, aLoginOrFunction, aPassword, aTimeout, aRequestMap, aHTTP, retBytes, options) : String`

````text
Tries to obtain aIndexMap from the REST aBaseURI service returning as a string (uses the HTTP GET method). Optionally you can provide aLogin, aPassword and/or aTimeout for the REST request or use a function (aLoginOrFunction) that receives the HTTP object. Optionally if retBytes = true returns a java stream.
````

### ow.obj.rest.getContentLength

`ow.obj.rest.getContentLength(aBaseURI, aLoginOrFunction, aPassword, aTimeout, aRequestMap, aHTTP) : Number`

````text
Tries to get the content lenght for the given aBaseURI. Optionally you can provide aLogin, aPassword and/or aTimeout for the HTTP request or use a function (aLoginOrFunction) that receives the HTTP object.
````

### ow.obj.rest.head

`ow.obj.rest.head(aBaseURI, aIndexMap, aLoginOrFunction, aPassword, aTimeout, aRequestMap, aHTTP, options) : Map`

````text
Tries to get the header map with aIndexMap entry from the REST aBaseURI service returning the reply as a Map. Optionally you can provide aLogin, aPassword and/or aTimeout for the REST request or use a function (aLoginOrFunction) that receives the HTTP object.
````

### ow.obj.rest.jsonCreate

`ow.obj.rest.jsonCreate(aBaseURI, aIndexMap, aDataRowMap, aLoginOrFunction, aPassword, aTimeout, aRequestMap, urlEncode, aHTTP, retBytes, options) : Map`

````text
Tries to create a new aDataRowMap entry, identified by aIndexMap, on the REST aBaseURI service returning the reply as a map (uses the HTTP POST method). Optionally you can provide aLogin, aPassword and/or aTimeout for the REST request or use a function (aLoginOrFunction) that receives the HTTP object.  If urlEncode=true the aDataRowMap will be converted into x-www-form-urlencoded instead of JSON. Optionally if retBytes = true returns a java stream.
````

### ow.obj.rest.jsonGet

`ow.obj.rest.jsonGet(aBaseURI, aIndexMap, aLoginOrFunction, aPassword, aTimeout, aRequestMap, aHTTP, retBytes, options) : Map`

````text
Tries to obtain aIndexMap from the REST aBaseURI service returning as a map (uses the HTTP GET method). Optionally you can provide aLogin, aPassword and/or aTimeout for the REST request or use a function (aLoginOrFunction) that receives the HTTP object. Optionally if retBytes = true returns a java stream.
````

### ow.obj.rest.jsonPatch

`ow.obj.rest.jsonPatch(aBaseURI, aIndexMap, aDataRowMap, aLoginOrFunction, aPassword, aTimeout, urlEncode, aHTTP, retBytes, options) : Map`

````text
Tries to set aDataRowMap entry, identified by aIndexMap, on the REST aBaseURI service returning the reply as a map (uses the HTTP PATCH method). Optionally you can provide aLogin, aPassword and/or aTimeout for the REST request or use a function (aLoginOrFunction) that receives the HTTP object. If urlEncode=true the aDataRowMap will be converted into x-www-form-urlencoded instead of JSON. Optionally if retBytes = true returns a java stream.
````

### ow.obj.rest.jsonRemove

`ow.obj.rest.jsonRemove(aBaseURI, aIndexMap, aLoginOrFunction, aPassword, aTimeout, aRequestMap, aHTTP, retBytes, options) : Map`

````text
Tries to remove aIndexMap entry from the REST aBaseURI service returning the reply as a map (uses the HTTP DELETE method). Optionally you can provide aLogin, aPassword and/or aTimeout for the REST request or use a function (aLoginOrFunction) that receives the HTTP object. Optionally if retBytes = true returns a java stream.
````

### ow.obj.rest.jsonSet

`ow.obj.rest.jsonSet(aBaseURI, aIndexMap, aDataRowMap, aLoginOrFunction, aPassword, aTimeout, urlEncode, aHTTP, retBytes, options) : Map`

````text
Tries to set aDataRowMap entry, identified by aIndexMap, on the REST aBaseURI service returning the reply as a map (uses the HTTP PUT method). Optionally you can provide aLogin, aPassword and/or aTimeout for the REST request or use a function (aLoginOrFunction) that receives the HTTP object. If urlEncode=true the aDataRowMap will be converted into x-www-form-urlencoded instead of JSON. Optionally if retBytes = true returns a java stream.
````

### ow.obj.rest.jsonUpload

`ow.obj.rest.jsonUpload(aBaseURI, aIndexMap, aDataRowMap, aLoginOrFunction, aPassword, aTimeout, aRequestMap, urlEncode, aHTTP, retBytes, aMethod, options) : String`

````text
Tries to upload a new aDataRowMap entry (composed of name and in (a filename, a stream or an array of bytes)), identified by aIndexMap, on the REST aBaseURI service returning the reply as a map (uses the HTTP POST method or aMethod). Optionally you can provide aLogin, aPassword and/or aTimeout for the REST request or use a function (aLoginOrFunction) that receives the HTTP object. Optionally if retBytes = true returns a java stream.
````

### ow.obj.rest.patch

`ow.obj.rest.patch(aBaseURI, aIndexMap, aDataRowMap, aLoginOrFunction, aPassword, aTimeout, urlEncode, aHTTP, retBytes, options) : String`

````text
Tries to set aDataRowMap entry, identified by aIndexMap, on the REST aBaseURI service returning the reply as a string (uses the HTTP PATCH method). Optionally you can provide aLogin, aPassword and/or aTimeout for the REST request or use a function (aLoginOrFunction) that receives the HTTP object. If urlEncode=true the aDataRowMap will be converted into x-www-form-urlencoded instead of JSON. Optionally if retBytes = true returns a java stream.
````

### ow.obj.rest.remove

`ow.obj.rest.remove(aBaseURI, aIndexMap, aLoginOrFunction, aPassword, aTimeout, aRequestMap, aHTTP, retBytes, options) : String`

````text
Tries to remove aIndexMap entry from the REST aBaseURI service returning the reply as a string (uses the HTTP DELETE method). Optionally you can provide aLogin, aPassword and/or aTimeout for the REST request or use a function (aLoginOrFunction) that receives the HTTP object. Optionally if retBytes = true returns a java stream.
````

### ow.obj.rest.set

`ow.obj.rest.set(aBaseURI, aIndexMap, aDataRowMap, aLoginOrFunction, aPassword, aTimeout, urlEncode, aHTTP, retBytes, options) : String`

````text
Tries to set aDataRowMap entry, identified by aIndexMap, on the REST aBaseURI service returning the reply as a string (uses the HTTP PUT method). Optionally you can provide aLogin, aPassword and/or aTimeout for the REST request or use a function (aLoginOrFunction) that receives the HTTP object. If urlEncode=true the aDataRowMap will be converted into x-www-form-urlencoded instead of JSON. Optionally if retBytes = true returns a java stream.
````

### ow.obj.rest.upload

`ow.obj.rest.upload(aBaseURI, aIndexMap, aDataRowMap, aLoginOrFunction, aPassword, aTimeout, aRequestMap, urlEncode, aHTTP, retBytes, aMethod, options) : String`

````text
Tries to upload a new aDataRowMap entry (composed of name and in (a filename, a stream or an array of bytes)), identified by aIndexMap, on the REST aBaseURI service returning the reply as a string (uses the HTTP POST method or aMethod). Optionally you can provide aLogin, aPassword and/or aTimeout for the REST request or use a function (aLoginOrFunction) that receives the HTTP object. Optionally if retBytes = true returns a java stream.
````

### ow.obj.rest.writeIndexes

`ow.obj.rest.writeIndexes(aPropsMap) : String`

````text
Given a map of REST API indexes (aPropsMap) will return a corresponding URI.
````

### ow.obj.rest.writeQuery

`ow.obj.rest.writeQuery(aMap) : String`

Given `aMap` will return a URL query string. Example:

```javascript
"http://some.thing/other/stuff?" + ow.obj.rest.writeQuery({ a: 1, b: 2 });
```

### ow.obj.schemaAdd

`ow.obj.schemaAdd(aKey, aSchema)`

````text
Registers a JSON Schema under aKey in its selected draft engine. Keys and root $ids cannot collide across drafts. Register referenced schemas in the same draft before compiling a schema that uses them.
````

### ow.obj.schemaCheck

`ow.obj.schemaCheck(aSchema) : Boolean`

````text
Checks whether aSchema is valid in its selected dialect, returning true/false. Unsupported dialects and configuration errors are thrown; this does not validate application data.
````

### ow.obj.schemaCompile

`ow.obj.schemaCompile(aSchema) : Function`

````text
Compiles a JSON Schema into a reusable validator returning true/false with details in its errors property. The root $schema selects the draft; absent means draft-07. Compilation errors are thrown.
````

### ow.obj.schemaGenerator

`ow.obj.schemaGenerator(aJson, aId, aRequiredArray, aDescriptionTmpl) : Map`

Given `aJson`, tries to generate a base [JSON Schema](http://json-schema.org/understanding-json-schema/index.html), with an optional `aId` and descriptions based on `aDescriptionTmpl`.

The description template accepts `id`, `required`, `json`, `_detail` (a boolean indicating when the template is used for items), `type`, `format` and `key`.

The generator emits draft-07 and infers array items from the first sample item. Review the result and validate it with `schemaCheck`.

Special notation:

- Regular expression: a string starting and ending with `/`.
- Numeric range: use `[` (inclusive) or `]` (exclusive), for example `"[2, 4["`.
- Enumeration: wrap a string representing an array of values in `(` and `)`, for example `"([ 'red', 'blue', 'green' ])"`.

### ow.obj.schemaInit

`ow.obj.schemaInit(aOptions)`

````text
Initializes JSON Schema validation once per process. Without options, enables $data, $comment and useDefaults (which can modify validated data). Explicit options replace these defaults; later calls do not reconfigure it. Schemas select draft-07 (the default), draft-2019-09 or draft-2020-12 through $schema. See https://ajv.js.org/options.html and docs/json-schema.md for options and compatibility notes.
````

### ow.obj.schemaRemove

`ow.obj.schemaRemove(aKey)`

````text
Removes schemas by key/$id, regular expression, or schema object across the draft engines. Without aKey, removes all application schemas, retaining built-in meta-schemas and initialization options.
````

### ow.obj.schemaSampleGenerator

`ow.obj.schemaSampleGenerator(aJsonSchema) : Map`

````text
Tries to generate a sample JSON map based on the provided aJsonSchema. There is no guarantee that the generated sample is valid.
````

### ow.obj.schemaValidate

`ow.obj.schemaValidate(aSchema, aData, aErrorOptions) : boolean`

````text
Validates data against a schema object or registered key/$id. Returns true on success; throws an error string on invalid data. aErrorOptions supports dataVar (default args) and separator. Defaults can modify aData. For boolean validation use schemaCompile(aSchema)(aData). See docs/json-schema.md.
````

### ow.obj.searchArray

`ow.obj.searchArray(anArray, aPartialMap, useRegEx, ignoreCase, useParallel) : Array`

Searches `anArray` of maps for entries where `aPartialMap` matches. If `useRegEx` is true all string entries
on `aPartialMap` will be interpreted as regular expressions. For number entries on the original map you can
have the prefixes `>`, `<`, `>=` and `<=` to limit the numeric values. The complete comparison must
contain a signed or unsigned number, optionally with decimals or an exponent (for example, `>=-1.5`).
Comparisons accept numbers and numeric strings; missing, null, boolean and nonnumeric values do not match.
Other string patterns remain regular expressions. Optionally you can provide also
`ignoreCase` = true to ignore case (will only affect if `useRegEx` is true). And optionally also `useParallel` to
provide the number of threads to use. Example:

```javascript
ow.obj.searchArray(io.listFiles("/usr/bin").files, { "isFile": true, "filename": "^cal.*", "size": ">=32000" }, true, true);

// you can use it, for example, in conjunction with jLinq
$from(ow.obj.searchArray(listFilesRecursive("/usr/lib"), { "filepath": "/usr/lib/ruby", "size": ">100000" }, true)).sort("size").select();

// to refer to a sub map value
ow.obj.searchArray(students, { "details.age": "<=25", "details.isMale": true }, true);
```

(available after `ow.loadObj()`)

### ow.obj.setFTPProxy

`ow.obj.setFTPProxy(aHost, aPort, anArrayNonProxyHosts)`

````text
Sets the current java FTP proxy to aHost, aPort and optional sets anArrayNonProxyHosts (see more in https://docs.oracle.com/javase/8/docs/technotes/guides/net/proxies.html). If no values are provided all ftp proxy settings, if any, are cleared out.
````

### ow.obj.setHTTPProxy

`ow.obj.setHTTPProxy(aHost, aPort, anArrayNonProxyHosts)`

````text
Sets the current java HTTP proxy to aHost, aPort and optional sets anArrayNonProxyHosts (see more in https://docs.oracle.com/javase/8/docs/technotes/guides/net/proxies.html). If no values are provided all http proxy settings, if any, are cleared out.
````

### ow.obj.setHTTPSProxy

`ow.obj.setHTTPSProxy(aHost, aPort, anArrayNonProxyHosts)`

````text
Sets the current java HTTPS proxy to aHost, aPort and optional sets anArrayNonProxyHosts (see more in https://docs.oracle.com/javase/8/docs/technotes/guides/net/proxies.html). If no values are provided all https proxy settings, if any, are cleared out.
````

### ow.obj.setPath

`ow.obj.setPath(aObject, aPath, aNewValue) : Object`

Given `aObject` it will try to parse the `aPath` a set the corresponding object under that path to `aNewValue`. Example:

```javascript
var a = { a : 1, b : { c: 2, d: [0, 1] } };

sprint(ow.obj.setPath(a, "b.c", 123)); // { a : 1, b : { c: 123, d: [0, 1] } }
```

### ow.obj.setSOCKSProxy

`ow.obj.setSOCKSProxy(aHost, aPort, aUser, aPass)`

````text
Sets the current java SOCKS proxy to aHost, aPort and optional sets aUser and aPass (see more in https://docs.oracle.com/javase/8/docs/technotes/guides/net/proxies.html). If no values are provided all scoks proxy settings, if any, are cleared out.
````

### ow.obj.sign

`ow.obj.sign(aKey, aMap, aHashName, aHashFunction) : Map`

````text
Given aMap and aKey will return a signed aMap using aHashFunction (defaults to sha512) with the hash algorithm indication aHashName (defaults to 'sha512'). The signed aMap can later be verified with ow.obj.signVerify.
````

### ow.obj.signVerify

`ow.obj.signVerify(aKey, aMap) : boolean`

````text
Verifies the signature of a signed aMap with ow.obj.sign function given aKey. Returns true if the signature is valid. Supported hash functions of ow.obj.sign: sha512, sha384 and sha256.
````

### ow.obj.socket.string2bytes

`ow.obj.socket.string2bytes(aHostAddress, aPort, aInputString) : Bytes`

````text
Tries to open a socket to aHostAddress on aPort sending aInputString. Will return the result, if any, as an array of bytes.
````

### ow.obj.socket.string2string

`ow.obj.socket.string2string(aHostAddress, aPort, aInputString) : String`

````text
Tries to open a socket to aHostAddress on aPort sending aInputString. Will return the result, if any, as a string.
````

### ow.obj.syncArray

`ow.obj.syncArray(anArray) : ow.obj.syncArray`

````text
Creates an instance of a thread-safe array/list. Optionally it can be initialized with anArray.
````

### ow.obj.syncArray.add

`ow.obj.syncArray.add(aObject, aPosition) : boolean`

````text
Adds aObject to the internal array/list. If aPosition is provided it will be added at that position, otherwise it will be added at the end.
````

### ow.obj.syncArray.addAll

`ow.obj.syncArray.addAll(anArray, aPosition)`

````text
Concatenates anArray with the internal array/list. If aPosition is provided it will be added at that position, otherwise it will be added at the end.
````

### ow.obj.syncArray.clear

`ow.obj.syncArray.clear()`

````text
Clears the internal array/list.
````

### ow.obj.syncArray.forEach

`ow.obj.syncArray.forEach(aFunction)`

````text
Executes aFunction for each element in the internal array/list. The function should have the signature function(value).
````

### ow.obj.syncArray.get

`ow.obj.syncArray.get(aIndex) : Object`

````text
Returns the object on the internal array/list on position aIndex.
````

### ow.obj.syncArray.getJavaObject

`ow.obj.syncArray.getJavaObject() : Object`

````text
Returns the internal java object.
````

### ow.obj.syncArray.getUnsafeJavaObject

`ow.obj.syncArray.getUnsafeJavaObject() : Object`

````text
Returns the internal java object without synchronization. Use with care! This is useful when you want to use the internal java object directly without the overhead of synchronization.
````

### ow.obj.syncArray.indexOf

`ow.obj.syncArray.indexOf(aObject) : Number`

````text
Returns the position of aObject in the internal array/list.
````

### ow.obj.syncArray.isEmpty

`ow.obj.syncArray.isEmpty() : boolean`

````text
Returns true if the internal array/list is empty.
````

### ow.obj.syncArray.length

`ow.obj.syncArray.length() : Number`

````text
Returns the current size of the internal array/list.
````

### ow.obj.syncArray.remove

`ow.obj.syncArray.remove(aIndex) : boolean`

````text
Removes the element at aIndex from the internal array/list.
````

### ow.obj.syncArray.set

`ow.obj.syncArray.set(aIndex, aObject) : Object`

````text
Sets aObject overwriting the previous value at aIndex on the internal array/list.
````

### ow.obj.syncArray.subList

`ow.obj.syncArray.subList(aStart, aEnd) : Array`

````text
Returns a sublist of the internal array/list from aStart to aEnd (exclusive). If aStart or aEnd are out of bounds it will throw an exception. The returned array will be a new array with the elements from aStart to aEnd.
````

### ow.obj.syncArray.toArray

`ow.obj.syncArray.toArray() : Array`

````text
Returns the internal array/list as a javascript array.
````

### ow.obj.syncArray.trimToSize

`ow.obj.syncArray.trimToSize()`

````text
Trims the internal array/list to its current size.
````

### ow.obj.syncMap

`ow.obj.syncMap(aMap) : ow.obj.syncMap`

````text
Creates an instance of a thread-safe map. Optionally it can be initialized with aMap.
````

### ow.obj.syncMap.clear

`ow.obj.syncMap.clear()`

````text
Clears the internal map.
````

### ow.obj.syncMap.containsKey

`ow.obj.syncMap.containsKey(aKey) : boolean`

````text
Returns true if the internal map contains aKey.
````

### ow.obj.syncMap.containsValue

`ow.obj.syncMap.containsValue(aValue) : boolean`

````text
Returns true if the internal map contains aValue.
````

### ow.obj.syncMap.forEach

`ow.obj.syncMap.forEach(aFunction)`

````text
Executes aFunction for each entry in the internal map. The function should have the signature function(key, value).
````

### ow.obj.syncMap.get

`ow.obj.syncMap.get(aKey) : Object`

````text
Returns the value of aKey in the internal map.
````

### ow.obj.syncMap.getJavaObject

`ow.obj.syncMap.getJavaObject() : Object`

````text
Returns the internal java object.
````

### ow.obj.syncMap.getKeys

`ow.obj.syncMap.getKeys() : Array`

````text
Returns an array with the entries of the internal map.
````

### ow.obj.syncMap.getValues

`ow.obj.syncMap.getValues() : Array`

````text
Returns an array with the values of the internal map.
````

### ow.obj.syncMap.isEmpty

`ow.obj.syncMap.isEmpty() : boolean`

````text
Returns true if the internal map is empty.
````

### ow.obj.syncMap.put

`ow.obj.syncMap.put(aKey, aValue) : ow.obj.syncMap`

````text
Puts aKey with aValue in the internal map.
````

### ow.obj.syncMap.putAll

`ow.obj.syncMap.putAll(aMap) : ow.obj.syncMap`

````text
Puts all the entries of aMap in the internal map.
````

### ow.obj.syncMap.remove

`ow.obj.syncMap.remove(aKey) : Object`

````text
Removes the entry identified by aKey from the internal map.
````

### ow.obj.syncMap.size

`ow.obj.syncMap.size() : Number`

````text
Returns the current size of the internal map.
````

### ow.obj.syncMap.toMap

`ow.obj.syncMap.toMap() : Map`

````text
Returns the internal map as a javascript map.
````
{% endraw %}
