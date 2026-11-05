---
layout: default
title: scope
parent: Reference
grand_parent: OpenAF docs
---

{% raw %}
## scope

[Source: `06414cd9`](https://github.com/OpenAF/openaf/blob/06414cd9204e918daa1e2971ce904783299db333/js/openaf.js) · [Baseline](../source-snapshot.md)

### $$from

`$$from : Array`

````text
Shortcut for the JLinq library for easy query and access to arrays/objects. To see all the available options please refer to http://hugoware.net/Projects/jlinq and the list of available functions by executing, in the openaf-console: "desc $$from([])".
````

### $a2m

`$a2m(aDef, aArray) : Array`

Tries to convert `aArray` into a map using the `aDef` array of keys for the map keys' value assignment in the output map. Example:

```javascript
$a2m(['a', 'b', 'c'], [1, 2, 3])    // { a: 1, b: 2, c: 3 }
```

### $a4m

`$a4m(anArray, aKey, dontRemove) : Array`

Tries to create a map of maps from the provided `anArrays`. Optionally if `aKey` is provided
it will be used to create the map keys (otherwise will fallback to "row[number]"). And can also
optionally indicate by `dontRemove` = true that `aKey` shouldn't be removed from each map.

```javascript
var a = [
  { "abc": "123", "xpt": "000", "key": "A1" },
  { "abc": "456", "xpt": "001", "key": "A2" },
  { "abc": "789", "xpt": "002", "key": "A3" }
]

$a4m(a, "key");
// {
//   "A1": { "abc": "123", "xpt": "000" },
//   "A2": { "abc": "456", "xpt": "001" },
//   "A3": { "abc": "789", "xpt": "002" }
// }
```

### $atomic

`$atomic(aInitValue, aType) : Object`

Creates an atomic object of `aType` (defaults to long) to be get/set atomically on a multithreading script initialized with `aInitValue`.
`aType` can be "int", "long" and "boolean". Each with different methods:

- `int.dec`: Decrement an integer
- `int.inc`: Increment an integer
- `int.get`: Get the current integer
- `int.getSet(n)`: Get and Set the current integer
- `int.getAdd(n)`: Get and Add to the current integer
- `int.setIf(t, n)`: Set the current integer to n if current value is t
- `int.set`: Set the current integer

- `long.dec`: Decrement an long
- `long.inc`: Increment an long
- `long.get`: Get the current long
- `long.getSet(n)`: Get and Set the current long
- `long.getAdd(n)`: Get and Add to the current long
- `long.setIf(t, n)`: Set the current long to n if current value is t
- `long.set`: Set the current long

- `boolean.get`: Get the current boolean
- `boolean.set`: Set the current boolean
- `boolean.getSet`: Get and Set the current boolean
- `boolean.setIf(t, n)`: Set the current boolean to n if current value is t

### $await

`$await(aName) : Object`

````text
Wrapper around the Java wait/notify mechanism. For the provided name will returen an object with the following  functions wait (will block until a notify is invoked), notify (will notify and unblock one of the wait invocations),  notifyAll (will notify and unblock all wait invocations) and destroy existing references to aName.
````

### $bottleneck.destroy

`$bottleneck.destroy()`

````text
Destroys any existing bottleneck definition.
````

### $bottleneck.exec

`$bottleneck.exec(args) : Object`

Creates a bottleneck `aName` to execute `aFunction` with the provided `args`. Returns what the function returns:

```javascript
$bottleneck("myFunc", (a, b) => { ... return result; })
.maxExec(3)
.maxWait(5000)
.exec(2, 4);

$bottleneck("myFunc").exec(2, 2);
```

### $bottleneck.maxExec

`$bottleneck.maxExec(aMaxNumber) : Object`

````text
Creates a bottleneck to a maximum concurrent execution number of aMaxNumber.
````

### $bottleneck.maxWait

`$bottleneck.maxWait(aMs) : Object`

````text
Creates a bottleneck holding the function execution for a max period of aMs.
````

### $cache.byDefault

`$cache.byDefault(useDefault, aDefault) : Object`

````text
Changes the behaviour of the cache to either use the default value (aDefault) if useDefault is true (launching the cache function in background) or try to use the previous value in the cache if useDefault  is false (if a previous value is not available the cache function will be called and the .get will wait for it).
````

### $cache.byPopularity

`$cache.byPopularity() : Object`

````text
Changes the behaviour of the cache to use the most popular entries and prefer to discard the least popular ones  when the cache is full (maxSize is defined).
````

### $cache.ch

`$cache.ch(aChannelName) : Object`

````text
Uses a pre-existing channel (e.g. aChannelName) as the cache channel.
````

### $cache.fn

`$cache.fn(aFunction) : Object`

````text
Defines the aFunction use to get aKey. The returned object will be cached.
````

### $cache.get

`$cache.get(aKey) : Object`

Shortcut to use a cache channel. Returns an object that can be used like this:

```javascript
$cache("numbers")
.ttl(30000)
.fn((aKey) => { ... return result; })
.create()

$cache("numbers").get(myKey);

$cache("numbers").destroy();
```

### $cache.inFile

`$cache.inFile(aFile) : Object`

````text
Creates a mvs channel to hold the cache data in aFile. Note: don't use $cache.ch if you use this option.
````

### $cache.maxSize

`$cache.maxSize(aSize) : Object`

````text
Establishes the max number of entries cached at any given point in time.
````

### $cache.ttl

`$cache.ttl(aTTL) : Object`

````text
Defines the time-to-live (aTTL) to consider a cached result as valid.
````

### $ch

`$ch(aChannel)`

Please check more details with the help from `ow.ch`. The available methods are:

Channel basics:

- `create(shouldCompress, aType, options)`
- `list()`
- `destroy()`
- `size()`
- `subscribe(aFunction, onlyFromNow, anId)`
- `unsubscribe(aId)`
- `forEach(aFunction)`
- `getAll()`
- `getKeys(fullInfo)`
- `getSortedKeys(fullInfo)`
- `set(aKey, aValue, aForcedTimestamp)`
- `setAll(keysArray, valuesArray, aForcedTimestamp)`
- `get(aKey)`
- `getSet(aMatch, aKey, aValue, aForcedTimestamp)`
- `unset(aKey, aForcedTimestamp)`
- `push(aKey, aValue)`
- `pop(aKey)`
- `shift(aKey)`
- `stopJobs()`
- `waitForJobs(aTimeout)`
- `getName()`

Channel basic persistence:

- `storeAdd(aFilename, anArrayOfKeys, shouldCompress)`
- `storeRestore(aFilename, anArrayOfKeys)`

Inter-channel HTTP REST:

- `expose(aLocalPortOrServer, aPath, aAuthFunc, aUnAuthFunc)`
- `peer(aLocalPortOrServer, aPath, aRemoteURL, aAuthFunc, aUnAuthFunc)`
- `unpeer(aRemoteURL)`
- `createRemote(aURL, aTimeout)`

### $channels

`$channels(aChannel)`

Please check more details with the help from `ow.ch`. The available methods are:

Channel basics:

- `create(shouldCompress, aType, options)`
- `list()`
- `destroy()`
- `size()`
- `subscribe(aFunction, onlyFromNow, anId)`
- `unsubscribe(aId)`
- `forEach(aFunction)`
- `getAll(fullInfo)`
- `getKeys(fullInfo)`
- `getSortedKeys(fullInfo)`
- `set(aKey, aValue, aForcedTimestamp)`
- `setAll(keysArray, valuesArray, aForcedTimestamp)`
- `unsetAll(keysArray, valuesArray, aForcedTimestamp)`
- `get(aKey)`
- `getSet(aMatch, aKey, aValue, aForcedTimestamp)`
- `unset(aKey, aForcedTimestamp)`
- `push(aKey, aValue)`
- `pop(aKey)`
- `shift(aKey)`
- `stopJobs()`
- `waitForJobs(aTimeout)`
- `getName()`

Channel basic persistence:

- `storeAdd(aFilename, anArrayOfKeys, shouldCompress, runSubscribersForAll)`
- `storeRestore(aFilename, anArrayOfKeys)`

Inter-channel HTTP REST:

- `expose(aLocalPortOrServer, aPath, aLogin, aPassword)`
- `peer(aLocalPortOrServer, aPath, aRemoteURL, aAuthFunc, aUnAuthFunc, aMaxTime, aMaxCount)`
- `unpeer(aRemoteURL)`
- `createRemote(aURL, aTimeout, aLogin, aPass)`

### $csv

`$csv(aMap) : $csv`

Provides a shortcut to access CSV functionality. Optionally you can provide options through `aMap`.

Examples:

```javascript
$csv().fromInArray(anArray)
$csv().fromInFile("test.csv").toOutArray()
$csv().fromInFile("test.csv").toOutFn(m => print( af.toSLON(m) ))
$csv().fromInString( $csv().fromInArray( io.listFiles(".").files ) ).toOutArray()
```

### $do

`$do(aFunction, aRejFunction) : oPromise`

````text
Instantiates and returns a oPromise. If you provide aFunction, this aFunction will be executed async in a thread and oPromise object will be immediatelly returned. Optionally this aFunction can receive a resolve and reject functions for to you use inside aFunction to provide a result with resolve(aResult) or an exception with reject(aReason). If you don't call theses functions the returned value will be used for resolve or any exception thrown will be use for reject. You can use the "then" method to add more aFunction that will execute once the previous as executed successfully (in a stack fashion). The return/resolve value from the previous function will be passed as the value for the second. You can use the "catch" method to add aFunction that will receive a string or exception for any exception thrown with the reject functions. You can also provide aRejFunction to work as a "catch" method as previously described before. The returned oPromise also exposes a cancel method to interrupt the corresponding running thread (similar to the Threads plugin capabilities) and reject the promise chain.
````

### $doA2B

`$doA2B(aAFunction, aBFunction, numberOfDoPromises, defaultTimeout, aErrorFunction, useVirtualThreads)`

````text
Will call aAFunction with a function as argument that should be used to "send" values to aBFunction. aBFunction will be call asynchronously in individual $do up to the numberOfDoPromises limit. The defaultTimeout it 2500ms. If aErrorFunction is defined it will received any exceptions thrown from aBFunction with the corresponding arguments array. If useVirtualThreads is true it will use virtual threads to execute aBFunction. If useVirtualThreads is false (default) it will use the thread pool. Use virtual threads if you want to execute aBFunction without blocking the current thread (IO bound operations / high concurrency).
````

### $doAll

`$doAll(anArray) : oPromise`

````text
Returns an oPromise that will be resolved when all oPromise part of the anArray are fullfiled. If any of the oPromises fails/rejects the returned oPromise will also be rejected/fail.
````

### $doFirst

`$doFirst(anArray) : oPromise`

````text
Returns an oPromise that will be resolved when any oPromise part of the anArray is fullfiled. If any of the oPromises fails/rejects the returned oPromise will also be rejected/fail.
````

### $doV

`$doV(aFunction, aRejFunction) : oPromise`

````text
Equivalent to $do but using virtual threads (if available) to execute the aFunction. This will allow the aFunction to be executed without blocking the current thread. If aFunction is not provided it will return a new oPromise that will be resolved when the first executor is added to it. If aRejFunction is provided it will be used as a "catch" method for the oPromise. The returned oPromise also exposes a cancel method to interrupt the corresponding running thread (similar to the Threads plugin capabilities) and reject the promise chain.
````

### $doWait

`$doWait(aPromise, aWaitTimeout) : oPromise`

````text
Blocks until aPromise is fullfilled or rejected. Optionally you can specify aWaitTimeout, in milliseconds, as an overall deadline for the wait: once it elapses $doWait returns even if aPromise hasn't settled yet (the caller is then responsible for checking aPromise's state and, if still pending, cancelling it to reclaim the thread pool slot). Returns aPromise.
````

### $err

`$err(exception, rethrow, returnStr, code)`

````text
Prints the exception stack trace and the code where it was thrown. If rethrow is true it will throw the exception again. If returnStr is true it will return the string instead of printing it.
````

### $f

`$f(aString, arg1, arg2, ...) : String`

Formats `aString` with `arg1`, `arg2` and any other arguments provided using java.util.Formatter. The format is composed
of "%[argument_index$][flags][width][.precision]conversion". Do note that javascript numbers are converted to java.lang.Float. If you
need it to convert to Integer, Long, Double, Float and BigDecimal please use `$ft`. The javascript Date type will be converted to java Calendar.
So possible values:

argument_index: number

- `flags`: '-' (left-justified); '#'; '+' (include sign); ' ' (leading space); '0' (zero-padded); ',' (separators); '(' (enclose negative values)
- `conversion`: b/B (boolean), h/H (hash), s/S (string), "-" (left justify), c/C (character)

Examples:

```javascript
$f("Time %tT", new Date())
$f("Date: %1$tm %1te, %1tY %1$tT", new Date())

$f("%.2f", 1.9)
$f("%10.2f", 1.9)
```

### $fetch

`$fetch(aURL, aOptions) : oPromise`

Tries to fetch `aURL` using the provided `aOptions` (a map with the following possible keys: method, body, headers, requestHeaders, downloadResume,
connectionTimeout, uriQuery, urlEncode, login, pass, httpClient and retry). The method will return a promise that will resolve to a response object
with the following methods: body, bodyUsed, headers, ok, status, json, bytes, blob and text. Example:

```javascript
var response = $fetch("https://httpbin.org/post", { method: "POST", body: { a: 1, b: 2 }, headers: { "Content-Type": "application/json" } });
response.then(function(aResponse) { print(aResponse.status); });
```

The response object will have the following methods:

- `body()`: returns a Java InputStream with the response body
- `bodyUsed`: returns true if the body was already read
- `headers`: returns a map with the response headers
- `ok`: returns true if the response status is between 200 and 299
- `status`: returns the response status
- `json()`: returns the response body as a JSON object
- `bytes()`: returns the response body as a byte array
- `blob()`: returns the response body as a byte array
- `text()`: returns the response body as a string

### $flock.destroy

`$flock.destroy()`

Given `aLockFile` will destroy the provided lock entry.

```javascript
$flock(aLockFile).destroy()
```

### $flock.isLocalLocked

`$flock.isLocalLocked() : Boolean`

Given `aLockFile` will return true if locked in the current OpenAF instance otherwise false (see also isLocked).

```javascript
$flock(aLockFile).isLocalLocked()
```

### $flock.isLocked

`$flock.isLocked() : Boolean`

Given `aLockFile` will return true if locked in the current OpenAF instance or on the filesystem (by using `$flock.tryLock`) otherwise false (see also isLocalLocked).

```javascript
$flock(aLockFile).isLocked()
```

### $flock.lock

`$flock.lock()`

Given `aLockFile` will use the file to filesystem lock until unlock is called.

```javascript
$flock(aLockFile).lock()
```

### $flock.tryLock

`$flock.tryLock(aFunction) : Boolean`

Given `aLockFile` only execute `aFunction` if it's unlocked. If it
executed `aFunction` it will return true otherwise false.

```javascript
$flock(aLockFile).tryLock(() => { ... })
```

### $flock.unlock

`$flock.unlock()`

Given `aLockFile` will unlock freeing any previous calls to lock.

```javascript
$flock(aLockFile).unlock()
```

### $fnDef4Help

`$fnDef4Help(aFnName) : Array`

````text
Tries to retrieve an array of function argument names for the provided search string aFnName.
````

### $fnM

`$fnM(aFnName, aMap) : Object`

Calls `aFnName` function trying to determine the name of the arguments from OpenAF's help or accessible source code (throws an exception
if it can't determine the arguments) and then builds the arguments used to call `aFnName` using the values of keys in `aMap`. Example:

```javascript
plugin("HTTP"); var h = new HTTP();
$fnM("h.get", { aUrl: "https://openaf.io/release" });
```

### $fnM2A

`$fnM2A(aFn, aInstance, aDefinitionArray, aMap) : Object`

Tries to execute `aFn`, with `aInstance` if it's a function of an instance, using `aMap` of arguments that translate to `aFn` list of
arguments. Returns whatever the function executed returns. Example:

```javascript
plugin("HTTP");
var h = new HTTP();
$fnM2A(h.get, h, $fnDef4Help("HTTP.get"), { aUrl: "https://openaf.io/build", isBytes: false, returnStream: false });
```

### $from

`$from : Array`

````text
Shortcut for the nLinq library for easy query and access to arrays/objects. To see all the available options please refer to https://github.com/nmaguiar/nLinq/blob/main/Reference.md and the list of available functions by executing, in the openaf-console: "desc $from([])".
````

### $ft

`$ft(aString, arg1, arg2, ...) : String`

````text
Equivalant to $f but number types are converted to Integer, Long, Double, Float and BigDecimal.
````

### $ftp.$ftp

`$ftp.$ftp(aMap) : $ftp`

````text
Builds an object to allow access through ftp/ftps. aMap should be a ftp/ftps string with the format: ftp://user:pass@host:port/?timeout=1234&passive=true&binary=true or ftps://user:pass@host:port/?timeout=1234&passive=true&binary=true&implicit=false&protocol=TLS or a map with the keys: host, port, login, pass, secure, implicit, protocol, passive, binary and timeout. See "help FTP.FTP" for more info.
````

### $ftp.binary

`$ftp.binary(isBinary) : $ftp`

````text
Sets the file transfer mode between binary and ascii.
````

### $ftp.cd

`$ftp.cd(aPath) : $ftp`

````text
Changes the current remote working directory.
````

### $ftp.close

`$ftp.close() : $ftp`

````text
Closes a remote host connection defined by aMap.
````

### $ftp.getFile

`$ftp.getFile(aSource, aTarget) : $ftp`

````text
Gets aSource filepath and stores it locally on aTarget from a remote host defined by aMap.
````

### $ftp.listFiles

`$ftp.listFiles(aRemotePath) : Array`

````text
Returns an array of maps with the listing of aRemotePath provided.
````

### $ftp.mkdir

`$ftp.mkdir(aDirectory) : $ftp`

````text
Creates aDirectory via FTP/FTPS on a remote host defined by aMap.
````

### $ftp.passive

`$ftp.passive(isPassive) : $ftp`

````text
Sets the passive mode for the ftp/ftps connection.
````

### $ftp.putFile

`$ftp.putFile(aSource, aTarget) : $ftp`

````text
Puts aSource local filepath or Java stream and stores it remotely in aTarget on a remote host defined by aMap.
````

### $ftp.pwd

`$ftp.pwd() : String`

````text
Returns the current remote working directory.
````

### $ftp.rename

`$ftp.rename(aSource, aTarget) : $ftp`

````text
Renames aSource filepath to aTarget filepath on a remote host defined by aMap.
````

### $ftp.rm

`$ftp.rm(aFilePath) : $ftp`

````text
Remove aFilePath from a remote host defined by aMap.
````

### $ftp.rmdir

`$ftp.rmdir(aFilePath) : $ftp`

````text
Removes a directory from a remote host defined by aMap.
````

### $ftp.timeout

`$ftp.timeout(aTimeout) : $ftp`

````text
Sets aTimeout in ms for the ftp/ftps connection to a remote host defined by aMap.
````

### $get

`$get(aKey) : Object`

````text
Returns a value previously set with $set with aKey.
````

### $job

`$job(aJob, args, aId, isolate) : Object`

````text
Shortcut to oJobRunJob and ow.oJob.runJob to execute aJob with args and returned the changed arguments. Optionally aId can be also provided. If isolate=true it will also clean the key 'res' and try to return the result of ow.oJob.output.
````

### $jq

`$jq(input, expression, options) : Object`

Evaluates jq syntax (jq 1.6 mode, jackson-jq 1.6.5) against one JSON value.
`expression` defaults to ".". Zero outputs return undefined, one returns the value,
and multiple outputs return an array. `options`.all=true always returns an array of outputs.
`options`.vars binds JSON values by variable name without the leading $. Examples:

```javascript
$jq({ a: 2 }, ".a"); // 2
$jq([1, 2], ".[]", { all: true }); // [1, 2]
$jq([1, 3], "map(select(. > $min))", { vars: { min: 2 } }); // [3]
```

Accepts plain objects, dense arrays, strings, finite numbers, booleans and null.
Rejects unsupported values and cycles with their location. Does not mutate inputs.
Results are detached JavaScript values; numbers have JavaScript precision.
`__flags.JQ_CACHE_SIZE` controls compiled query caching (256 entries; 0 clears/disables).
Filesystem imports, CLI `input` streams and OpenAF callbacks are unavailable.
See docs/jq.md for compatibility, value boundaries and error behavior.

### $jsonrpc

`$jsonrpc(aOptions) : Map`

Creates a JSON-RPC 2.0 client that can communicate with JSON-RPC servers over HTTP/HTTPS
or with local processes using stdio. The `aOptions` parameter is a map with the following
possible keys:

- `type` (string) : Connection type, either "stdio" for local process, "remote"/"http" for HTTP server, "sse" for HTTP SSE responses (default: "stdio") or "dummy"
- `url` (string) : Required for remote servers - the endpoint URL
- `timeout` (number) : Timeout in milliseconds for operations (default: 60000)
- `cmd` (string|map|array) : Required for stdio type - the command to execute or the map/array accepted by `$sh`
- `pwd` (string) : For stdio type - the working directory to use when executing cmd (default: the JSONRPC.cmd.defaultDir flag, if set)
- `envs` (map) : For stdio type - a map of environment variables to use when executing cmd. Note: by default these are merged over the current process environment (so secrets in the parent environment are inherited); set envsOnly to true to use only this map
- `envsOnly` (boolean) : For stdio type - when true the child process environment will be exactly the envs map instead of merging it with the current environment (default: false)
- `options` (map) : Additional options passed to `$rest` for remote connections
- `sse` (boolean) : When true, remote/http requests expect Server-Sent Events responses with JSON-RPC payloads in `data:` events
- `debug` (boolean) : Enable debug output showing JSON-RPC messages (default: false)
- `shared` (boolean) : Share connections between identical configurations (default: false)

The returned client object provides these methods:

- `type(aType)`: Set the connection type
- `url(aURL)`: Set the URL and switch to remote type
- `sh(aCommand)`: Set the command and switch to stdio type
- `pwd(aPath)`: Set the working directory to use for stdio execution
- `envs(aMap)`: Set the environment variables map to use for stdio execution (merged with the current environment unless envsOnly is true)
- `exec(aMethod, aParams, aNotification)`: Execute a JSON-RPC method
- `destroy()`: Stop the client and cleanup resources

The exec method parameters:

- `aMethod` (string) : The JSON-RPC method name to call
- `aParams` (map) : Parameters object to send with the method call
- `aNotification` (boolean) : If true, sends a notification (no response expected)

For method calls (`aNotification`=false), exec returns the result directly.
For notifications (`aNotification`=true), exec returns undefined.

Examples:

```javascript
// Remote JSON-RPC server
var client = $jsonrpc({type: "remote", url: "http://api.example.com/rpc", debug: true});
var result = client.exec("getUserInfo", {userId: 123});
log("User info:", result);

// Send notification (no response)
client.exec("logEvent", {event: "user_login", userId: 123}, true);

// Local process via stdio
var localClient = $jsonrpc({cmd: "python3 my_rpc_server.py"});
var data = localClient.exec("processData", {input: [1, 2, 3]});
localClient.destroy();
```

### $llm

`$llm(aModel) : $llm`

````text
Shortcut for $gpt on the owrap.AI library.
````

### $lock.destroy

`$lock.destroy()`

Given `aLockName` will destroy the provided lock entry.

```javascript
$lock(aLockName).destroy()
```

### $lock.isLocked

`$lock.isLocked() : Boolean`

Given `aLockName` will return true if locked otherwise false.

```javascript
$lock(aLockName).isLocked()
```

### $lock.lock

`$lock.lock()`

Given `aLockName` will lock until unlock is called.

```javascript
$lock(aLockName).lock()
```

### $lock.tryLock

`$lock.tryLock(aFunction, aTimeoutMS) : Boolean`

Given `aLockName` only execute `aFunction` when it's able to lock or after `aTimeoutMS`. If it
executed `aFunction` it will return true otherwise false.

```javascript
$lock(aLockName).tryLock(() => { ... })
```

### $lock.unlock

`$lock.unlock()`

Given `aLockName` will unlock freeing any previous calls to lock.

```javascript
$lock(aLockName).unlock()
```

### $m2a

`$m2a(aDef, aMap) : Array`

Tries to convert `aMap` into an array using the `aDef` array of keys for the values order in the output array. Example:

```javascript
$m2a(['c', 'b', 'a'], { a: 1, b: 2, c: 3 })    // [ 3, 2, 1 ]
```

### $m4a

`$m4a(aMap, aKey) : Array`

Tries to create an array of maps from the provided `aMap` map of maps. Optionally if `aKey` is provided
it will be added to each array map with the map key. Example:

```javascript
var a = {
   "A1": { "abc": "123", "xpt": "000" },
   "A2": { "abc": "456", "xpt": "001" },
   "A3": { "abc": "789", "xpt": "002" }
}

$m4a(a, "key");
// [
//  { "key": "A1", "abc": "123", "xpt": "000" },
//  { "key": "A2", "abc": "456", "xpt": "001" },
//  { "key": "A3", "abc": "789", "xpt": "002" }
// ]
```

### $mcp

`$mcp(aOptions) : Map`

Creates a Model Context Protocol (MCP) client that can communicate with LLM MCP servers
using JSON-RPC over stdio, remote connections, dummy mode, or oJob-based servers. This client speaks the legacy,
initialize-handshake-based MCP protocol eras by default (protocolVersion "2024-11-05" or "2025-06-18", selectable
via `aOptions.protocolVersion`, default "2025-06-18") and provides access to tools, prompts, and other MCP
capabilities. It can optionally opt into the modern, stateless 2026-07-28+ protocol era by setting
`aOptions.protocolVersion` to "auto": this probes the server (server/discover on stdio, a modern request inspected
for a recognized error on HTTP) and negotiates the modern era when the server supports it, falling back to the
legacy initialize handshake otherwise -- existing callers that don't set "auto" are completely unaffected.

The `aOptions` parameter is a map with the following possible keys:

- `type` (string) : Connection type - "stdio" for local process, "remote"/"http" for HTTP server, "sse" for HTTP SSE responses, "dummy" for local testing, or "ojob" for oJob-based server (default: "stdio")
- `url` (string) : Required for remote servers - the MCP server endpoint URL
- `timeout` (number) : Timeout in milliseconds for operations (default: 60000)
- `cmd` (string|array) : Required for stdio type - the command to launch the MCP server (an array is executed directly, without going through a shell)
- `pwd` (string) : For stdio type - the working directory to use when launching the MCP server
- `envs` (map) : For stdio type - a map of environment variables to use when launching the MCP server. Note: by default these are merged over the current process environment (so secrets in the parent environment are inherited); set envsOnly to true to use only this map
- `envsOnly` (boolean) : For stdio type - when true the MCP server environment will be exactly the envs map instead of merging it with the current environment (default: false)
- `options` (map) : Additional options:
  - For remote/stdio: passed to underlying JSON-RPC client
- For dummy: { fns: map of function implementations, fnsMeta: map of function metadata }
  - For ojob: { job: path to oJob file, args: arguments map, init: init entry/entries to run, fns: map of additional functions, fnsMeta: map of additional function metadata }
- `debug` (boolean) : Enable debug output showing JSON-RPC messages (default: false)
- `shared` (boolean) : Enable shared JSON-RPC connections when possible (default: false)
- `sse` (boolean) : When true, remote/http MCP requests expect Server-Sent Events responses carrying JSON-RPC payloads
- `strict` (boolean) : Enable strict MCP protocol compliance (default: true)
- `clientInfo` (map) : Client information sent during initialization (default: {name: "OpenAF MCP Client", version: "1.0.0"})
- `blacklist` (array) : Optional array of MCP tool names to hide from listTools() and block in callTool()
- `preFn` (function) : Function called before each tool execution with (toolName, toolArguments)
- `posFn` (function) : Function called after each tool execution with (toolName, toolArguments, result)
- `auth` (map) : Optional authentication options for remote/http type:
  - `type` (string): "bearer" (static token) or "oauth2" (automatic token retrieval/refresh)
- `token` (string): Bearer token when type is "bearer"
  - `tokenType` (string): Authorization scheme prefix (default: "Bearer")
- For oauth2: tokenURL, clientId, clientSecret, scope, audience, resource, grantType (default: "client_credentials"), extraParams (map), refreshWindowMs (default: 30000), authURL/redirectURI for authorization_code flow
  - For oauth2: if tokenURL/authURL are omitted for remote/http MCP servers they can be discovered through OAuth 2.0 Protected Resource Metadata and Authorization Server Metadata (the metadata issuer must match and discovered endpoints must use HTTPS unless they are loopback addresses or allowHTTP is true)
- `interactive` (boolean): false prohibits browser login and code prompts; omitted preserves existing behavior
  - `callback` (boolean): opt-in loopback login through `ow.server.httpd.oauth2` at redirectURI, with state/PKCE validation; loginTimeoutMs defaults to 300000
- `tokenStore` (map): opt-in {type: "sec", profile: "default"}; optional repo (default mcp-oauth2), bucket, key, file, lockSecret, mainSecret, lockTimeoutMs (60000). Or a synchronous custom load/save/clear/withLock store.
  - `sendResource` (boolean): false omits the OAuth resource parameter; default true
- `disableOpenBrowser` (boolean): If true prevents opening a browser during OAuth2 authorization_code flow (default: false)
- authenticate() / getAuthStatus() / clearAuth(): authenticate, inspect non-secret status, or clear local tokens

Type-specific details:

"dummy" type: Creates a local testing MCP server without external processes.

- Use options.fns to define tool implementations as functions
- Use options.fnsMeta to define tool metadata (description, input schema)
- Useful for development and testing without running actual MCP servers

"ojob" type: Creates an MCP server based on oJob jobs as tools.

- `options.job` (required) : Path to the oJob file containing job definitions
- `options.args`: Arguments to pass to the oJob
- `options.init`: Init entry name(s) to execute on startup (string or array)
- Jobs with fnsMeta property become MCP tools automatically
- Job names become tool names (except "tools/list", "tools/call", "initialize", "notifications/initialized")
- Combines oJob's job execution with MCP protocol

The returned client object provides these methods:

- `type(aType)`: Set the connection type
- `url(aURL)`: Set the URL and switch to remote type
- `sh(aCommand)`: Set the command and switch to stdio type
- `initialize(clientInfo)`: Initialize the MCP connection and exchange capabilities
- `listTools()`: Get list of available tools from the MCP server
- `callTool(toolName, toolArguments, toolOptions)`: Execute a specific tool with given arguments and optional per-call options
- `listPrompts()`: Get list of available prompts from the MCP server
- `getPrompt(promptName, promptArguments)`: Get a specific prompt with given arguments
- `toGptTools(aGptInstance, aToolNames)`: Add MCP tools to a `$gpt` instance
- `exec(method, params)`: Low-level method to execute any MCP/JSON-RPC method
- `destroy()`: Stop the client and cleanup resources

Important: The initialize() method must be called before using listTools, callTool,
listPrompts, or getPrompt methods. All methods return results synchronously (not promises).

Examples:

```javascript
// Connect to local MCP server via stdio
var client = $mcp({cmd: "npx @modelcontextprotocol/server-filesystem /tmp"});
client.initialize();
var tools = client.listTools();
log("Available tools:", tools.tools.map(t => t.name));

var result = client.callTool("read_file", {path: "/tmp/example.txt"});
log("File content:", result.content);

// Connect to remote MCP server
var remoteClient = $mcp({
  type: "remote",
  url: "http://localhost:8080/mcp",
  clientInfo: {name: "MyApp", version: "2.0.0"}
});
remoteClient.initialize();
// Optional per-call HTTP options (only used for remote/http MCP clients)
var result2 = remoteClient.callTool("read_file", {path: "/tmp/example.txt"}, { requestHeaders: { Authorization: "Bearer ..." } });
var prompts = remoteClient.listPrompts();

// Remote MCP server with OAuth2 client credentials
var oauthClient = $mcp({
  type: "remote",
  url: "https://example.com/mcp",
  auth: {
    type: "oauth2",
    tokenURL: "https://example.com/oauth/token",
    clientId: "my-client",
    clientSecret: "my-secret",
    scope: "mcp:read mcp:write"
  }
});
oauthClient.initialize();

// OAuth2 authorization_code flow (opens browser by default)
var oauthCodeClient = $mcp({
  type: "remote",
  url: "https://example.com/mcp",
  auth: {
    type: "oauth2",
    grantType: "authorization_code",
    authURL: "https://example.com/oauth/authorize",
    tokenURL: "https://example.com/oauth/token",
    redirectURI: "http://localhost/callback",
    clientId: "my-client",
    clientSecret: "my-secret",
    disableOpenBrowser: false
  }
});

// Dummy mode for testing
var dummyClient = $mcp({
  type: "dummy",
  options: {
    fns: {
      "test_tool": (params) => ({ result: "test" })
    },
    fnsMeta: {
      "test_tool": {
        description: "A test tool",
        inputSchema: { type: "object", properties: {} }
      }
    }
  }
});
dummyClient.initialize();
dummyClient.callTool("test_tool", {});

// oJob-based MCP server
var ojobClient = $mcp({
  type: "ojob",
  options: {
    job: "mytools.yaml",
    args: { env: "prod" },
    init: "setup"
  }
});
ojobClient.initialize();
var jobTools = ojobClient.listTools();

client.destroy();
remoteClient.destroy();
dummyClient.destroy();
ojobClient.destroy();
```

### $mcp.getAgent

`$mcp.getAgent(agentId) : Map`

Retrieves metadata for a specific A2A agent by ID.
Returns the agent's metadata map (id, name, title, version, tags, capabilities).
Throws an error if the agent is not found.
Must call initialize() first.

Example:

```javascript
var client = $mcp({cmd: "ojob a2a-server.yaml"});
client.initialize();
var agent = client.getAgent("weather-agent");
print(agent);
```

### $mcp.listAgents

`$mcp.listAgents() : Map`

Lists all available A2A agents from the MCP server.
Returns a map with an 'agents' array containing agent metadata (id, name, title, version, tags, capabilities).
return _buildSyntheticInitializeResult(`aOptions.options`)

Example:

```javascript
var client = $mcp({cmd: "ojob a2a-server.yaml"});
client.initialize();
var agents = client.listAgents();
print(agents.agents);
```

### $mcp.sendToAgent

`$mcp.sendToAgent(agentId, message, options) : Map`

Sends a `message` to the specified A2A agent and returns the response.

- `agentId`: String identifier of the target agent
- `message`: String or Map containing the `message` content
- `options`: Optional map with request `options`

Returns MCP-style response: `{ content: [{type: "text", text: "..."}], isError: false }`

Supports preFn and posFn hooks if configured in the MCP client `options`.
Must call initialize() first.

Example:

```javascript
var client = $mcp({cmd: "ojob a2a-server.yaml"});
client.initialize();
var response = client.sendToAgent("echo-agent", "Hello World");
print(response.content[0].text);
```

### $mcp.toGptTools

`$mcp.toGptTools(aGptInstance, aToolNames) : $mcp`

Automatically adds this MCP client's tools to a `$gpt` instance using the `$gpt.withTool` method.
The `aGptInstance` should be an initialized `$gpt` object. If `aToolNames` is provided (array of strings),
only those specific tools will be added. Otherwise, all available tools are added.
Each MCP tool will be converted to a GPT-compatible tool using the MCP tool's JSON schema.

Example:

```javascript
var mcpClient = $mcp({cmd: "npx @modelcontextprotocol/server-filesystem /tmp"});
mcpClient.initialize();
var gpt = $gpt({type: "openai", options: {key: "your-key"}});
mcpClient.toGptTools(gpt); // Adds all MCP tools to GPT
// or mcpClient.toGptTools(gpt, ["read_file", "write_file"]); // Adds only specific tools

var response = gpt.prompt("Read the file /tmp/example.txt");
```

### $openaf

`$openaf(aScript, aPMIn, aOpenAF, extraJavaParamsArray) : Object`

````text
Tries to start an external process running openaf (if aOpenAF is provided, as a string or array, it will be used as the command to invoke openaf) to execute aScript setting the __pm variable to aPMIn. Upon execution end the __pm contents will be returned by the function.
````

### $output

`$output(aObj, args, aFunc, shouldReturn) : String`

Formats and prints `aObj` using the options in `args` (defaults to `{}`). Also available as `$o`.
Set `shouldReturn` to `true` to return formatted output instead of printing it.

##### Format selection

Use `args.__format` (or `args.__FORMAT`) to select a format. The lowercase option takes precedence.
Without an explicit format, `global.__format` is used when defined. Otherwise, maps and arrays use
`__colorFormat.table.format` when it is `table`, `stable`, `ctable`, `btable` or `bstable`;
all other cases default to `human`.

| Formats | Output |
| --- | --- |
| `json`, `prettyjson`, `cjson` | Compact, indented or colored JSON. |
| `gb64json` | Compact JSON encoded with gzip and Base64. |
| `slon`, `cslon` | SLON or colored SLON. |
| `ndjson` | One JSON value per array element. With `shouldReturn`, returns an array of strings. Use an array as input. |
| `xml`, `yaml`, `cyaml`, `toon` | XML, YAML, colored YAML or TOON. |
| `kyaml`, `ckyaml`, `lkyaml`, `clkyaml` | KYAML and its colored (`c`), single-line flow (`l`) variants. |
| `table`, `stable`, `ctable` | Table, wrapped table with row separators, or colored wrapped table. Maps become single-row arrays. |
| `btable`, `bstable` | Unicode borderless tables; `bstable` always separates records with light rules. |
| `tree`, `ctree`, `cntree`, `atree` | Tree output; colored (`c`), shortened keys (`n`), or colored without tables for arrays (`a`). |
| `mtree`, `mntree`, `btree`, `bntree` | Uncolored trees; monochrome (`m`) or plain (`b`), with shortened-key variants (`n`). |
| `map` | Map-style output using `printMap`. |
| `html`, `jsmap` | A complete HTML document from `ow.template.html.parseMap`. |
| `text` | JavaScript string conversion using `String`. |
| `md` | Render Markdown text for the terminal, or generate Markdown from maps and arrays (see below). |
| `csv` | CSV from an array of maps; a single map becomes a one-row array. |
| `human` | Call `aFunc` with the transformed value, or use the default tree/string output. |

##### Options

These options also accept uppercase names (for example, `__PATH`); lowercase takes precedence.
Transformations run before formatting, in the order `__path`, `__from`, `__sql`.

| Option | Purpose |
| --- | --- |
| `__path` | Select data with `$path(aObj, expression)`. |
| `__from` | Query data with `$from` using an nLinq expression parsed by `af.fromNLinq`. |
| `__sql` | Query data with `$sql`. |
| `__csv` | CSV configuration as a JSON or SLON string, passed to `$csv`. |
| `__pause` | Page printed text with `ow.format.string.pauseString`. Ignored when returning output. |
| `__width` | Positive integer wrapping width for `btable` and `bstable`; defaults to the available terminal width. |
| `__rowsep` | Enable light rules between records in `btable` (default `false`). `bstable` always enables them. |
| `__key` | Storage key for the `key` format (default `"res"`). |

##### Markdown output

For maps and arrays, `args.mdformat` accepts `structured` (default), `json` or `yaml`.
`structured` produces field/value tables for flat maps, column tables for arrays of flat maps,
lists for arrays of scalar values, and headings for nested data. Nested string sections use code fences.
`json` and `yaml` produce fenced code blocks. These map/array modes return or print Markdown source.
String input is rendered by `ow.format.withMD` for terminal display.

##### Storing results

The `res` format stores the transformed value with `$set("res", value)`; `key` uses `args.__key`.
A format named `set_NAME` stores it with `$set("NAME", value)`.
The `args` format writes to `args._list`, `args._map` or `args.result` according to the value type.
The `pm` format merges the same fields into `__pm`.

Storage formats do not return formatted data. With `shouldReturn` omitted or false, they print a blank line.
The return value depends on the format: usually a string, an array of strings for `ndjson`, or undefined.
`human` does not forward the return value from `aFunc`, including the default formatter.
A custom `aFunc` is responsible for its own printing.

##### Examples

```javascript
var rows = [{ name: "alpha", count: 2 }, { name: "beta", count: 5 }];
$output(rows, { __format: "btable", __width: 80, __rowsep: true });

// Capture formatted text without printing.
var json = $output(rows, { __format: "prettyjson" }, __, true);

// Select part of an object before formatting.
$output({ items: rows }, { __path: "items", __format: "yaml" });

// Generate Markdown source from structured data.
var markdown = $output(rows, { __format: "md" }, __, true);
var fenced = $output(rows, { __format: "md", mdformat: "json" }, __, true);

// Render Markdown text in the terminal.
$output("# Results\n\n**Complete**", { __format: "md" });
```

### $path

`$path(obj, path, customFunctions) : Object`

Shortcut for the JMESPath library for easy query and access to arrays/objects. To see all the available options
please refer to http://jmespath.org. Uses the Java engine by default; set `__flags.ALTERNATIVES.path`=false
to use the Javascript engine. `__flags.PATH_CACHE_SIZE` controls the Java syntax cache (256 entries by default; 0 disables).
Optional you can provide a map of `customFunctions`. Examples:

**Slicing:**

```javascript
$path(arr, "[0:5]"); $path(arr, "[5:10]"); $path(arr, "[:5]"); $path(arr, "[::2]"); $path(arr, "[::-1]");
```

**Projections:**

```javascript
$path(arr, "a[*].first"); $path(arr, "a.*.b"); $path(arr, "[]");
```

**Filters:**

```javascript
$path(arr, "a[?b=='xyz'].c"); $path(arr, "a[?b>`1`].x");
```

**MultiSelect:**

```javascript
$path(arr, "a[].[x, y]"); $path(arr, "a[].{ x: x, y: y }");
```

**Pipe:**

```javascript
$path(arr, "a[*].b | [0]");
```

**Functions:**

```text
abs(x), avg(x), contains(x, y), ceil(x), floor(x), join(x, arr), keys(obj), length(x), map(expr, arr), max(x), max_by(x, y), merge(a, b), min(a), min_by(a, b), not_null(a), reverse(arr), sort(arr), sort_by(a, y), starts_with(a, b), ends_with(a, b), sum(a), to_array(a), to_string(a), to_number(a), type(a), values(a)
$path(arr, "a[?contains(@, 'b') == `true`]")
```

**OpenAF custom functions:**

```text
  a2m(arrFields, arrValues), a4m(arr, 'key', dontRemove), m2a(arrFields, obj), m4a(obj, 'key'), count_by(arr, 'field'), format(x, 'format'), formatn(x, 'format'), group(arr, 'field'), group_by(arr, 'field1,field2'), unique(arr), to_map(arr, 'field'), to_date(x), to_datef(x, format) from_datef(x, format), to_isoDate(x), flat_map(x), search_keys(arr, 'text'), search_values(arr, 'text'), delete(map, 'field'), substring(a, ini, end),
 template(a, 'template'), t(a, 'template'), templateF(x, 'template'), tF(x, 'template'), to_bytesAbbr(x), to_numAbbr(x), from_bytesAbbr(x), from_siAbbr(x), from_timeAbbr(x), timeago(x), from_ms(x, 'format'), replace(x, 're', 'flags', 'replaceText'), split(x, 'sep'), trim(x), index_of(x, 'search'), last_index_of(x, 'search'), lower_case(x), upper_case(x), concat(x, y), match(x, 're', 'flags'), amerge(x, y), to_slon(x), from_slon(x), to_json(x), from_json(x, str), to_yaml(x, isMultiDoc), from_yaml(x), trim(x), nvl(x, v), to_toml(x), from_toml(x)
add(x, y), sub(x, y), mul(x, y), div(x, y), mod(x, y)
split(x, sep), split_re(x, sepRE), split_sep(x, sepRE, encls), date_diff(d, unit, nullValue)
insert(obj, 'field', value), now(negativeTimeDiff)
get(nameOrPath), set(obj, path), setp(obj, path, name)
range(count), ranges(count, start, step)
inc(name), dec(name), getc(name), unset(obj, name)
k2a(map, keyre, outkey, removeNulls), geta(nameOrPath, arrayIndex)
sql_format(sql, options), sort_semver(arrayVersions), sort_by_semver(arrayMaps, jmespathStringToVersionField)
semver(version, operation, argument)
progress(value, max, min, size, indicator, space),
to_csv(array, options), from_csv(str, options)
ch(name, op, arg1, arg2), chq(name, op, max, value), path(obj, jmespath), opath(jmespath)
sql(obj, query), from(obj, queryStringOrMap), jq(obj, query)
to_ms(date), timeagoAbbr(x)
env(str), envs(regex)
oafp(json/slon), oafpd(obj, json/slon)
if(cond, then, else)
assign(obj, path, value), assignp(objPathStr, path, value)
random(min, max), srandom(min, max)
at(arrayIndex)
to_numSpace(num, space), from_numSpace(num, space)
to_kyaml(obj), from_kyaml(str)
to_toon(obj), from_toon(str)
to_base64(str), from_base64(str)
to_xml(obj), from_xml(str)
```

Functions only active if flag PATH_SAFE is false:

```text
ojob(name, argsJSSLON)
sh(command, stdin), sh_json(command, stdin), sh_jsslon(command, stdin), sh_yaml(command, stdin)
```

Custom functions:

```javascript
$path(2, "example(@)", { example: { _func: (a) => { return Number(a) + 10; }, _signature: [ { types: [ $path().number ] } ] } });
```

Query helpers use `$sql` with its default method, `$from(...).query(...)` (parsing strings
with `af.fromNLinq`), and `$jq` with its default output behavior. Examples:

```javascript
$path(data, "sql(items, 'select name where price > 10')");
$path(data, "from(items, 'greater(price, 10)')");
$path(data, "jq(items, 'map(select(.price > 10))')");
```

### $py

`$py(aPythonCodeOrFile, aInput, aOutputArray, throwExceptions, shouldFork) : Map`

````text
Executes aPythonCodeOrFile using a map aInput as variables in python and returns a map with python  variables in aOutputArray. Starts an embedded session once if needed. throwExceptions defaults to false; true throws on stderr, nonzero exit or bridge failure. shouldFork=true isolates this call.
````

### $pyExec

`$pyExec(aPythonCodeOrFile, aInput, throwExceptions, aArgv) : Map`

````text
Runs a standalone script with callbacks and returns a process result including exitcode. aInput is reserved. aArgv overrides launcher environment arguments; throwExceptions defaults to false.
````

### $pyStart

`$pyStart()`

````text
Start python process on the background. Should be stopped with $pyStop.
````

### $pyStop

`$pyStop()`

````text
Stops the background python process started by $pyStart.
````

### $queue

`$queue(anArray) : Object`

Returns an object with the following methods:

- `add(aItem)`: adds `aItem` to the queue and returns true if successful
- `remove(aItem)`: removes `aItem` from the queue and returns true if successful
- `addAll(aItems)`: adds all `aItems` to the queue and returns true if successful
- `has(aItem)`: returns true if `aItem` is in the queue
- `isEmpty()`: returns true if the queue is empty
- `size()`: returns the size of the queue
- `toArray()`: returns the queue as an array
- `peek()`: returns the first item in the queue without removing it
- `poll()`: returns the first item in the queue and removes it

The queue is implemented using a java.util.concurrent.ConcurrentLinkedQueue, which is thread-safe and allows concurrent access.
If `anArray` is provided, it will be added to the queue using addAll.

### $rest.delete

`$rest.delete(aBaseURI, aIdxMap) : Map`

````text
Shortcut for ow.obj.rest.jsonRemove (see help ow.obj.rest.jsonRemove) using aOptions ($rest(aOptions).): login (function or string),  pass (word), connectionTimeout (in ms), requestHeaders (map), urlEncode (boolean), uriQuery (boolean), httpClient (ow.obj.http object), default (map to return when there is an exception), throwExceptions (boolean defaulting to false controlling between throwing exceptions on different from 2xx http codes or connection issues or returning a map (merge with default if available)  and an error entry), collectAllStats (boolean with default false to store per uri or host:port statitics), preAction function that receives and returns a map with changes (aBaseURL, aIdxMap, aDataRowMap, login, pass, conTimeout, reqHeaders, urlEncode and httpClient), retry (number) and retryWait (time in ms).
````

### $rest.delete2File

`$rest.delete2File(aFilePath, aBaseURI, aIdxMap)`

````text
Shortcut for ow.obj.rest.jsonRemove (see help ow.obj.rest.jsonRemove) using aOptions ($rest(aOptions).): login (function or string),  pass (word), connectionTimeout (in ms), requestHeaders (map), urlEncode (boolean), uriQuery (boolean), httpClient (ow.obj.http object), default (map to return when there is an exception), throwExceptions (boolean defaulting to false controlling between throwing exceptions on different from 2xx http codes or connection issues or returning a map (merge with default if available)  and an error entry), collectAllStats (boolean with default false to store per uri or host:port statitics), preAction function that receives and returns a map with changes (aBaseURL, aIdxMap, aDataRowMap, login, pass, conTimeout, reqHeaders, urlEncode and httpClient), retry (number) and retryWait (time in ms). The byte output will be saved into aFilePath. Optional $rest(aOptions.downloadResume = true) will resume download of a file if it exists.
````

### $rest.delete2Stream

`$rest.delete2Stream(aBaseURI, aIdxMap) : JavaStream`

````text
Shortcut for ow.obj.rest.jsonRemove (see help ow.obj.rest.jsonRemove) using aOptions ($rest(aOptions).): login (function or string),  pass (word), connectionTimeout (in ms), requestHeaders (map), urlEncode (boolean), uriQuery (boolean), httpClient (ow.obj.http object), default (map to return when there is an exception), throwExceptions (boolean defaulting to false controlling between throwing exceptions on different from 2xx http codes or connection issues or returning a map (merge with default if available)  and an error entry), collectAllStats (boolean with default false to store per uri or host:port statitics), preAction function that receives and returns a map with changes (aBaseURL, aIdxMap, aDataRowMap, login, pass, conTimeout, reqHeaders, urlEncode and httpClient), retry (number) and retryWait (time in ms).
````

### $rest.get

`$rest.get(aBaseURI, aIdxMap) : Map`

````text
Shortcut for ow.obj.rest.jsonGet (see help ow.obj.rest.jsonGet) using aOptions ($rest(aOptions).): login (function or string),  pass (word), connectionTimeout (in ms), requestHeaders (map), urlEncode (boolean), uriQuery (boolean), httpClient (ow.obj.http object), default (map to return when there is an exception), throwExceptions (boolean defaulting to false controlling between throwing exceptions on different from 2xx http codes or connection issues or returning a map (merge with default if available)  and an error entry), collectAllStats (boolean with default false to store per uri or host:port statitics), preAction function that receives and returns a map with changes (aBaseURL, aIdxMap, aDataRowMap, login, pass, conTimeout, reqHeaders, urlEncode and httpClient), retry (number) and retryWait (time in ms).
````

### $rest.get2File

`$rest.get2File(aFilePath, aBaseURI, aIdxMap)`

````text
Shortcut for ow.obj.rest.jsonGet (see help ow.obj.rest.jsonGet) using aOptions ($rest(aOptions).): login (function or string),  pass (word), connectionTimeout (in ms), requestHeaders (map), urlEncode (boolean), uriQuery (boolean), httpClient (ow.obj.http object), default (map to return when there is an exception), throwExceptions (boolean defaulting to false controlling between throwing exceptions on different from 2xx http codes or connection issues or returning a map (merge with default if available)  and an error entry), collectAllStats (boolean with default false to store per uri or host:port statitics), preAction function that receives and returns a map with changes (aBaseURL, aIdxMap, aDataRowMap, login, pass, conTimeout, reqHeaders, urlEncode and httpClient), retry (number) and retryWait (time in ms). The byte output will be saved into aFilePath. Optional $rest(aOptions.downloadResume = true) will resume download of a file if it exists.
````

### $rest.get2Stream

`$rest.get2Stream(aBaseURI, aIdxMap) : JavaStream`

````text
Shortcut for ow.obj.rest.jsonGet (see help ow.obj.rest.jsonGet) using aOptions ($rest(aOptions).): login (function or string),  pass (word), connectionTimeout (in ms), requestHeaders (map), urlEncode (boolean), uriQuery (boolean), httpClient (ow.obj.http object), default (map to return when there is an exception), throwExceptions (boolean defaulting to false controlling between throwing exceptions on different from 2xx http codes or connection issues or returning a map (merge with default if available)  and an error entry), collectAllStats (boolean with default false to store per uri or host:port statitics), preAction function that receives and returns a map with changes (aBaseURL, aIdxMap, aDataRowMap, login, pass, conTimeout, reqHeaders, urlEncode and httpClient), retry (number) and retryWait (time in ms).
````

### $rest.head

`$rest.head(aBaseURI, aIdxMap)`

````text
Shortcut for ow.obj.rest.head (see help ow.obj.rest.head) using aOptions ($rest(aOptions).): login (function or string),  pass (word), connectionTimeout (in ms), requestHeaders (map), urlEncode (boolean), uriQuery (boolean), httpClient (ow.obj.http object), default (map to return when there is an exception), throwExceptions (boolean defaulting to false controlling between throwing exceptions on different from 2xx http codes or connection issues or returning a map (merge with default if available)  and an error entry), collectAllStats (boolean with default false to store per uri or host:port statitics), preAction function that receives and returns a map with changes (aBaseURL, aIdxMap, login, pass, conTimeout, reqHeaders, urlEncode and httpClient), retry (number) and retryWait (time in ms).
````

### $rest.index

`$rest.index(aMap) : String`

````text
Shortcut for ow.obj.rest.writeIndexes (see help ow.obj.rest.writeIndexes).
````

### $rest.patch

`$rest.patch(aBaseURI, aDataRowMap, aIdxMap) : Map`

````text
Shortcut for ow.obj.rest.jsonPatch (see help ow.obj.rest.jsonPatch) using aOptions ($rest(aOptions).): login (function or string),  pass (word), connectionTimeout (in ms), requestHeaders (map), urlEncode (boolean), uriQuery (boolean), httpClient (ow.obj.http object), default (map to return when there is an exception), throwExceptions (boolean defaulting to false controlling between throwing exceptions on different from 2xx http codes or connection issues or returning a map (merge with default if available)  and an error entry), collectAllStats (boolean with default false to store per uri or host:port statitics), preAction function that receives and returns a map with changes (aBaseURL, aIdxMap, aDataRowMap, login, pass, conTimeout, reqHeaders, urlEncode and httpClient), retry (number) and retryWait (time in ms).
````

### $rest.patch2File

`$rest.patch2File(aFilePath, aBaseURI, aDataRowMap, aIdxMap)`

````text
Shortcut for ow.obj.rest.jsonPatch (see help ow.obj.rest.jsonPatch) using aOptions ($rest(aOptions).): login (function or string),  pass (word), connectionTimeout (in ms), requestHeaders (map), urlEncode (boolean), uriQuery (boolean), httpClient (ow.obj.http object), default (map to return when there is an exception), throwExceptions (boolean defaulting to false controlling between throwing exceptions on different from 2xx http codes or connection issues or returning a map (merge with default if available)  and an error entry), collectAllStats (boolean with default false to store per uri or host:port statitics), preAction function that receives and returns a map with changes (aBaseURL, aIdxMap, aDataRowMap, login, pass, conTimeout, reqHeaders, urlEncode and httpClient), retry (number) and retryWait (time in ms).  The byte output will be saved into aFilePath. Optional $rest(aOptions.downloadResume = true) will resume download of a file if it exists.
````

### $rest.patch2Stream

`$rest.patch2Stream(aBaseURI, aDataRowMap, aIdxMap) : JavaStream`

````text
Shortcut for ow.obj.rest.jsonPatch (see help ow.obj.rest.jsonPatch) using aOptions ($rest(aOptions).): login (function or string),  pass (word), connectionTimeout (in ms), requestHeaders (map), urlEncode (boolean), uriQuery (boolean), httpClient (ow.obj.http object), default (map to return when there is an exception), throwExceptions (boolean defaulting to false controlling between throwing exceptions on different from 2xx http codes or connection issues or returning a map (merge with default if available)  and an error entry), collectAllStats (boolean with default false to store per uri or host:port statitics), preAction function that receives and returns a map with changes (aBaseURL, aIdxMap, aDataRowMap, login, pass, conTimeout, reqHeaders, urlEncode and httpClient), retry (number) and retryWait (time in ms).
````

### $rest.patchUpload

`$rest.patchUpload(aBaseURI, aDataRowMap, aIdxMap) : Map`

````text
Shortcut for ow.obj.rest.upload (see help ow.obj.rest.upload with patch) using aOptions ($rest(aOptions).): login (function or string),  pass (word), connectionTimeout (in ms), requestHeaders (map), urlEncode (boolean), uriQuery (boolean), httpClient (ow.obj.http object), default (map to return when there is an exception), throwExceptions (boolean defaulting to false controlling between throwing exceptions on different from 2xx http codes or connection issues or returning a map (merge with default if available)  and an error entry), collectAllStats (boolean with default false to store per uri or host:port statitics), preAction function that receives and returns a map with changes (aBaseURL, aIdxMap, aDataRowMap, login, pass, conTimeout, reqHeaders, urlEncode and httpClient), retry (number) and retryWait (time in ms).
````

### $rest.patchUpload2Stream

`$rest.patchUpload2Stream(aBaseURI, aDataRowMap, aIdxMap) : JavaStream`

````text
Shortcut for ow.obj.rest.upload (see help ow.obj.rest.upload with patch) using aOptions ($rest(aOptions).): login (function or string),  pass (word), connectionTimeout (in ms), requestHeaders (map), urlEncode (boolean), uriQuery (boolean), httpClient (ow.obj.http object), default (map to return when there is an exception), throwExceptions (boolean defaulting to false controlling between throwing exceptions on different from 2xx http codes or connection issues or returning a map (merge with default if available)  and an error entry), collectAllStats (boolean with default false to store per uri or host:port statitics), preAction function that receives and returns a map with changes (aBaseURL, aIdxMap, aDataRowMap, login, pass, conTimeout, reqHeaders, urlEncode and httpClient), retry (number) and retryWait (time in ms).
````

### $rest.post

`$rest.post(aBaseURI, aDataRowMap, aIdxMap) : Map`

````text
Shortcut for ow.obj.rest.jsonCreate (see help ow.obj.rest.jsonCreate) using aOptions ($rest(aOptions).): login (function or string),  pass (word), connectionTimeout (in ms), requestHeaders (map), urlEncode (boolean), uriQuery (boolean), httpClient (ow.obj.http object), default (map to return when there is an exception), throwExceptions (boolean defaulting to false controlling between throwing exceptions on different from 2xx http codes or connection issues or returning a map (merge with default if available)  and an error entry), collectAllStats (boolean with default false to store per uri or host:port statitics), preAction function that receives and returns a map with changes (aBaseURL, aIdxMap, aDataRowMap, login, pass, conTimeout, reqHeaders, urlEncode and httpClient), retry (number) and retryWait (time in ms).
````

### $rest.post2File

`$rest.post2File(aFilePath, aBaseURI, aDataRowMap, aIdxMap)`

````text
Shortcut for ow.obj.rest.jsonCreate (see help ow.obj.rest.jsonCreate) using aOptions ($rest(aOptions).): login (function or string),  pass (word), connectionTimeout (in ms), requestHeaders (map), urlEncode (boolean), uriQuery (boolean), httpClient (ow.obj.http object), default (map to return when there is an exception), throwExceptions (boolean defaulting to false controlling between throwing exceptions on different from 2xx http codes or connection issues or returning a map (merge with default if available)  and an error entry), collectAllStats (boolean with default false to store per uri or host:port statitics), preAction function that receives and returns a map with changes (aBaseURL, aIdxMap, aDataRowMap, login, pass, conTimeout, reqHeaders, urlEncode and httpClient), retry (number) and retryWait (time in ms). The byte output will be saved into aFilePath. Optional $rest(aOptions.downloadResume = true) will resume download of a file if it exists.
````

### $rest.post2Stream

`$rest.post2Stream(aBaseURI, aDataRowMap, aIdxMap) : JavaStream`

````text
Shortcut for ow.obj.rest.jsonCreate (see help ow.obj.rest.jsonCreate) using aOptions ($rest(aOptions).): login (function or string),  pass (word), connectionTimeout (in ms), requestHeaders (map), urlEncode (boolean), uriQuery (boolean), httpClient (ow.obj.http object), default (map to return when there is an exception), throwExceptions (boolean defaulting to false controlling between throwing exceptions on different from 2xx http codes or connection issues or returning a map (merge with default if available)  and an error entry), collectAllStats (boolean with default false to store per uri or host:port statitics), preAction function that receives and returns a map with changes (aBaseURL, aIdxMap, aDataRowMap, login, pass, conTimeout, reqHeaders, urlEncode and httpClient), retry (number) and retryWait (time in ms).
````

### $rest.postUpload

`$rest.postUpload(aBaseURI, aDataRowMap, aIdxMap) : Map`

````text
Shortcut for ow.obj.rest.upload (see help ow.obj.rest.upload with post) using aOptions ($rest(aOptions).): login (function or string),  pass (word), connectionTimeout (in ms), requestHeaders (map), urlEncode (boolean), uriQuery (boolean), httpClient (ow.obj.http object), default (map to return when there is an exception), throwExceptions (boolean defaulting to false controlling between throwing exceptions on different from 2xx http codes or connection issues or returning a map (merge with default if available)  and an error entry), collectAllStats (boolean with default false to store per uri or host:port statitics), preAction function that receives and returns a map with changes (aBaseURL, aIdxMap, aDataRowMap, login, pass, conTimeout, reqHeaders, urlEncode and httpClient), retry (number) and retryWait (time in ms).
````

### $rest.postUpload2Stream

`$rest.postUpload2Stream(aBaseURI, aDataRowMap, aIdxMap) : JavaStream`

````text
Shortcut for ow.obj.rest.upload (see help ow.obj.rest.upload with post) using aOptions ($rest(aOptions).): login (function or string),  pass (word), connectionTimeout (in ms), requestHeaders (map), urlEncode (boolean), uriQuery (boolean), httpClient (ow.obj.http object), default (map to return when there is an exception), throwExceptions (boolean defaulting to false controlling between throwing exceptions on different from 2xx http codes or connection issues or returning a map (merge with default if available)  and an error entry), collectAllStats (boolean with default false to store per uri or host:port statitics), preAction function that receives and returns a map with changes (aBaseURL, aIdxMap, aDataRowMap, login, pass, conTimeout, reqHeaders, urlEncode and httpClient), retry (number) and retryWait (time in ms).
````

### $rest.put

`$rest.put(aBaseURI, aDataRowMap, aIdxMap) : Map`

````text
Shortcut for ow.obj.rest.jsonSet (see help ow.obj.rest.jsonSet) using aOptions ($rest(aOptions).): login (function or string),  pass (word), connectionTimeout (in ms), requestHeaders (map), urlEncode (boolean), uriQuery (boolean), httpClient (ow.obj.http object), default (map to return when there is an exception), throwExceptions (boolean defaulting to false controlling between throwing exceptions on different from 2xx http codes or connection issues or returning a map (merge with default if available)  and an error entry), collectAllStats (boolean with default false to store per uri or host:port statitics), preAction function that receives and returns a map with changes (aBaseURL, aIdxMap, aDataRowMap, login, pass, conTimeout, reqHeaders, urlEncode and httpClient), retry (number) and retryWait (time in ms).
````

### $rest.put2File

`$rest.put2File(aFilePath, aBaseURI, aDataRowMap, aIdxMap)`

````text
Shortcut for ow.obj.rest.jsonSet (see help ow.obj.rest.jsonSet) using aOptions ($rest(aOptions).): login (function or string),  pass (word), connectionTimeout (in ms), requestHeaders (map), urlEncode (boolean), uriQuery (boolean), httpClient (ow.obj.http object), default (map to return when there is an exception), throwExceptions (boolean defaulting to false controlling between throwing exceptions on different from 2xx http codes or connection issues or returning a map (merge with default if available)  and an error entry), collectAllStats (boolean with default false to store per uri or host:port statitics), preAction function that receives and returns a map with changes (aBaseURL, aIdxMap, aDataRowMap, login, pass, conTimeout, reqHeaders, urlEncode and httpClient), retry (number) and retryWait (time in ms). The byte output will be saved into aFilePath. Optional $rest(aOptions.downloadResume = true) will resume download of a file if it exists.
````

### $rest.put2Stream

`$rest.put2Stream(aBaseURI, aDataRowMap, aIdxMap) : JavaStream`

````text
Shortcut for ow.obj.rest.jsonSet (see help ow.obj.rest.jsonSet) using aOptions ($rest(aOptions).): login (function or string),  pass (word), connectionTimeout (in ms), requestHeaders (map), urlEncode (boolean), uriQuery (boolean), httpClient (ow.obj.http object), default (map to return when there is an exception), throwExceptions (boolean defaulting to false controlling between throwing exceptions on different from 2xx http codes or connection issues or returning a map (merge with default if available)  and an error entry), collectAllStats (boolean with default false to store per uri or host:port statitics), preAction function that receives and returns a map with changes (aBaseURL, aIdxMap, aDataRowMap, login, pass, conTimeout, reqHeaders, urlEncode and httpClient), retry (number) and retryWait (time in ms).
````

### $rest.putUpload

`$rest.putUpload(aBaseURI, aDataRowMap, aIdxMap) : Map`

````text
Shortcut for ow.obj.rest.upload (see help ow.obj.rest.upload with put) using aOptions ($rest(aOptions).): login (function or string),  pass (word), connectionTimeout (in ms), requestHeaders (map), urlEncode (boolean), uriQuery (boolean), httpClient (ow.obj.http object), default (map to return when there is an exception), throwExceptions (boolean defaulting to false controlling between throwing exceptions on different from 2xx http codes or connection issues or returning a map (merge with default if available)  and an error entry), collectAllStats (boolean with default false to store per uri or host:port statitics), preAction function that receives and returns a map with changes (aBaseURL, aIdxMap, aDataRowMap, login, pass, conTimeout, reqHeaders, urlEncode and httpClient), retry (number) and retryWait (time in ms).
````

### $rest.putUpload2Stream

`$rest.putUpload2Stream(aBaseURI, aDataRowMap, aIdxMap) : JavaStream`

````text
Shortcut for ow.obj.rest.upload (see help ow.obj.rest.upload with post) using aOptions ($rest(aOptions).): login (function or string),  pass (word), connectionTimeout (in ms), requestHeaders (map), urlEncode (boolean), uriQuery (boolean), httpClient (ow.obj.http object), default (map to return when there is an exception), throwExceptions (boolean defaulting to false controlling between throwing exceptions on different from 2xx http codes or connection issues or returning a map (merge with default if available)  and an error entry), collectAllStats (boolean with default false to store per uri or host:port statitics), preAction function that receives and returns a map with changes (aBaseURL, aIdxMap, aDataRowMap, login, pass, conTimeout, reqHeaders, urlEncode and httpClient), retry (number) and retryWait (time in ms).
````

### $rest.query

`$rest.query(aMap) : String`

````text
Shortcut for ow.obj.rest.writeQuery (see help ow.obj.rest.writeQuery).
````

### $retry

`$retry(aFunction, aNumOfTriesOrFunction) : Object`

````text
Tries to execute aFunction and return the corresponding returned result. If aNumOfTriesOrFunction is a number (defaults to 1) and aFunction throws an exception it will repeat aFunction until it doesn't throw an exception or for the number of aNumOfTriesOrFunc. If aNumOfTriesOrFunction is a function it will be called whenever aFunction throws an exception with the corresponding exception as argument and it will retry until aNumOfTriesOrFunction returns false.
````

### $set

`$set(aKey, aValue)`

````text
Sets aValue with aKey so it can be retrieved with $get later.
````

### $sh.cb

`$sh.cb(aCallbackFunc) : $sh`

````text
When executing aCmd (with .get) use aCallbackFunc function.
````

### $sh.cp

`$sh.cp(aSource, aTarget) : $sh`

````text
Immediately copies aSource to aTarget before executing aCmd (with .exec).
````

### $sh.dontWait

`$sh.dontWait(aBooleanValue) : $sh`

````text
If aBooleanValue = true the execution won't wait for output (default: false).
````

### $sh.envs

`$sh.envs(aMap, includeExisting) : $sh`

````text
Uses aMap of strings as the environment variables map. If includeExisting = true it will include the current environment variables also.
````

### $sh.exec

`$sh.exec(aIdx) : Object`

````text
Immediately copies the result of executing aCmd string or array (and any other commands in queue added using sh). If aIdx is provided it will return the map entry for the corresponding command on the array otherwise it will return the array.
````

### $sh.exit

`$sh.exit(aFunc) : $sh`

````text
Sets aFunc function to execute after the execution of aCmd (with .exec).
````

### $sh.exitcb

`$sh.exitcb(aFunction) : $sh`

````text
When executing aCmd if aFunction is provided it will be called to determine if the execution should continue or not. If aFunction returns "destroy" the execution will try to be destroyed. If aFunction returns "force" the execution will be forced to stop.
````

### $sh.get

`$sh.get(aIdx) : Object`

````text
Immediately copies the result of executing aCmd string or array (and any other commands in queue added using sh). If aIdx is provided it will return the map entry for the corresponding command on the array otherwise it will return the array.
````

### $sh.getJsSlon

`$sh.getJsSlon(aIdx) : Object`

````text
Immediately copies the result of executing aCmd string or array (and any other commands in queue added using sh) trying to parse it as json or slon. If aIdx is provided it will return the map entry for the corresponding command on the array otherwise it will return the array.
````

### $sh.getJson

`$sh.getJson(aIdx) : Object`

````text
Immediately copies the result of executing aCmd string or array (and any other commands in queue added using sh) trying to parse it as json (will ingore non json content). If aIdx is provided it will return the map entry for the corresponding command on the array otherwise it will return the array.
````

### $sh.getYaml

`$sh.getYaml(aIdx) : Object`

````text
Immediately copies the result of executing aCmd string or array (and any other commands in queue added using sh) trying to parse it as yaml. If aIdx is provided it will return the map entry for the corresponding command on the array otherwise it will return the array.
````

### $sh.mkdir

`$sh.mkdir(aDir) : $sh`

````text
Immediately creates aDir before executing aCmd (with .exec).
````

### $sh.mv

`$sh.mv(aSource, aTarget) : $sh`

````text
Immediately moves aSource to aTarget before executing aCmd (with .exec).
````

### $sh.prefix

`$sh.prefix(aPrefix, aTemplate) : $sh`

````text
When executing aCmd (with .get) it will use ow.format.streamSHPrefix with aPrefix and optionally aTemplate.
````

### $sh.pwd

`$sh.pwd(aPwd) : $sh`

````text
When executing aCmd (with .exec) use aPwd as the current working directory.
````

### $sh.rename

`$sh.rename(aSource, aTarget) : $sh`

````text
Immediately renames aSource to aTarget before executing aCmd (with .exec).
````

### $sh.rm

`$sh.rm(aFilePath) : $sh`

````text
Immediately removes aFilePath before executing aCmd (with .exec).
````

### $sh.sh

`$sh.sh(aCmd, aIn) : $sh`

````text
When executing aCmd (with .exec) sets additional aCmds (with the optional corresponding aIn) to use.
````

### $sh.timeout

`$sh.timeout(aTimeout) : $sh`

````text
When executing aCmd (with .exec) uses aTimeout.
````

### $sh.useEncoding

`$sh.useEncoding(aEncoding) : $sh`

````text
Forces the aEncoding to be used.
````

### $sql

`$sql(aObject, aSQL, aMethod) : Array`

Given an `aObject` (map or array) will try to execute `aSQL` (SQL expression) and return the corresponding results.
Optionally you can provide `aMethod` to be used (e.g. "auto" (default) or "nlinq" or "h2"). "nlinq" it's the fastest but doesn't
support aggregations or multi-field combinations; "h2" is the more complete but will require a lot more resources, it's slower.

NOTE: In "h2" you can use the table _TMP for your queries.

### $ssh.$ssh

`$ssh.$ssh(aMap) : $ssh`

````text
Builds an object to allow access through ssh. aMap should be a ssh string with the format: ssh://user:pass@host:port/identificationKey?timeout=1234&compression=true or a map with the keys: host, port, login, pass, id (file key) / key (string representation), compress and timeout. See "help SSH.SSH" for more info.
````

### $ssh.cb

`$ssh.cb(aCallback) : $ssh`

````text
Sets aCallback function to execute during the execution of commands on a remote host defined by aMap (host, port, login, pass, id, compress and timeout).
````

### $ssh.close

`$ssh.close() : $ssh`

````text
Closes a remote host connection defined by aMap (host, port, login, pass, id, compress and timeout).
````

### $ssh.delTunnelLocal

`$ssh.delTunnelLocal(aLocalInterface, aLocalPort) : $ssh`

````text
Deletes a local tunnel mapping aLocalInterface:aLocalPort
````

### $ssh.delTunnelRemote

`$ssh.delTunnelRemote(aRemoteInterface, aRemotePort) : $ssh`

````text
Deletes a remote tunnel mapping aRemoteInterface:aRemotePort
````

### $ssh.exec

`$ssh.exec(aIdx) : Array`

````text
Executes a list of commands previously set on a remote host connection defined by aMap (host, port, login, pass, id, compress and timeout). IO is inherit. If aIdx is provided it will return the map entry for the corresponding command on the array otherwise it will return the array.
````

### $ssh.exit

`$ssh.exit(aFunc) : $ssh`

````text
Sets a callback aFunc to execute upon a command execution s a remote host connection defined by aMap (host, port, login, pass, id, compress and timeout).
````

### $ssh.get

`$ssh.get(aIdx) : Object`

````text
Executes a list of commands previously set on a remote host connection defined by aMap (host, port, login, pass, id, compress and timeout). IO is not inherit. If aIdx is provided it will return the map entry for the corresponding command on the array otherwise it will return the array.
````

### $ssh.getFile

`$ssh.getFile(aSource, aTarget) : $ssh`

````text
Gets aSource filepath and stores it locally on aTarget from a remote host defined by aMap (host, port, login, pass, id, compress and timeout).
````

### $ssh.getJson

`$ssh.getJson(aIdx) : Object`

````text
Executes a list of commands previously set on a remote host connection defined by aMap (host, port, login, pass, id, compress and timeout). IO is not inherit. If aIdx is provided it will return the map entry for the corresponding command on the array otherwise it will return the array. The stdout and stderr will be pre-parsed from json to objects.
````

### $ssh.listFiles

`$ssh.listFiles(aRemotePath) : Array`

````text
Returns an array of maps with the listing of aRemotePath provided.
````

### $ssh.mkdir

`$ssh.mkdir(aDirectory) : $ssh`

````text
Creates aDirectory via SFTP on a remote host defined by aMap (host, port, login, pass, id, compress and timeout).
````

### $ssh.prefix

`$ssh.prefix(aPrefix, aTemplate) : $ssh`

````text
When executing aCmd (with .get) it will use ow.format.streamSHPrefix with aPrefix and optionally aTemplate.
````

### $ssh.pty

`$ssh.pty(aFlag) : $ssh`

````text
Sets the flag to use or not a pty term allocation on the ssh connection to a remote host defined by aMap (host, port, login, pass, id, key, compress and timeout).
````

### $ssh.putFile

`$ssh.putFile(aSource, aTarget) : $ssh`

````text
Puts aSource local filepath and stores it remotely in aTarget on a remote host defined by aMap (host, port, login, pass, id, compress and timeout).
````

### $ssh.pwd

`$ssh.pwd(aPwd) : $ssh`

````text
Sets aPwd directory for getting and sending files to a remote host defined by aMap (host, port, login, pass, id, compress and timeout).
````

### $ssh.rename

`$ssh.rename(aSource, aTarget) : $ssh`

````text
Renames aSource filepath to aTarget filepath on a remote host defined by aMap (host, port, login, pass, id, compress and timeout).
````

### $ssh.rm

`$ssh.rm(aFilePath) : $ssh`

````text
Remove aFilePath from a remote host defined by aMap (host, port, login, pass, id, compress and timeout).
````

### $ssh.rmdir

`$ssh.rmdir(aFilePath) : $ssh`

````text
Removes a directory from a remote host defined by aMap (host, port, login, pass, id, compress and timeout).
````

### $ssh.sh

`$ssh.sh(aCmd, aIn) : $ssh`

````text
Sets aCmd to be executed with an optional aIn (stdin) on the remote host defined by aMap (host, port, login, pass, id, compress and timeout).
````

### $ssh.timeout

`$ssh.timeout(aTimeout) : $ssh`

````text
Sets aTimeout in ms for the ssh/sftp connection to a remote host defined by aMap (host, port, login, pass, id, compress and timeout).
````

### $ssh.tunnelLocal

`$ssh.tunnelLocal(aLocalPort, aRemoteHost, aRemotePort) : $ssh`

````text
Creates a local tunnel mapping aLocalPort to aRemoteHost:aRemotePort using the ssh connection defined by aMap (host, port, login, pass, id, compress and timeout).
````

### $ssh.tunnelLocalBind

`$ssh.tunnelLocalBind(aLocalInterface, aLocalPort, aRemoteHost, aRemotePort) : $ssh`

````text
Creates a local tunnel mapping aLocalInterface:aLocalPort to aRemoteHost:aRemotePort using the ssh connection defined by aMap (host, port, login, pass, id, compress and timeout).
````

### $ssh.tunnelRemote

`$ssh.tunnelRemote(aRemotePort, aLocalAddress aLocalPort) : $ssh`

````text
Creates a remote tunnel mapping aRemotePort to aLocalAddress:aLocalPort using the ssh connection defined by aMap (host, port, login, pass, id, compress and timeout).
````

### $ssh.tunnelRemoteBind

`$ssh.tunnelRemoteBind(aRemoteInterface, aRemotePort, aLocalAddress aLocalPort) : $ssh`

````text
Creates a remote tunnel mapping aRemoteInterface:aRemotePort to aLocalAddress:aLocalPort using the ssh connection defined by aMap (host, port, login, pass, id, compress and timeout).
````

### $stream

`$stream`

````text
Shortcut for the streamjs library for easy query and access to streams of data. To see all the available options please refer to https://github.com/winterbe/streamjs/blob/master/APIDOC.md.
````

### $sync

`$sync() : Object`

Returns an object with a 'run(`aFn`)' function that will execute the provided `aFn` in a synchronized way.
The run function will lock the execution until the `aFn` is finished. This is useful to
ensure that only one thread is executing the `aFn` at a time.

Example:

```javascript
var s = $sync()
s.run(() => {
    // Your code here, only one thread will execute this at a time
})
```

### $tb

`$tb(aFunction) : Result`

Shortcut for a "thread-box" to execute `aFunction`. The "thread" will timeout with the provided execution timeout (in ms)
or stop whenever the stopWhen function returns true (called continuously or after each timeout). Examples:

```javascript
$tb().timeout(5000).exec(aFunc);  // Executes aFunc to a maximum of 5 seconds. Afterwards the aFunc is stopped.
$tb(aFunc).timeout(5000).exec();  // Sames as previous, aFunc can be provided before or on exec.
$tb().timeout(500).stopWhen(aStopFunc).exec(); // Stops when aStopFunc is true.
```

### $throwIfUnDef

`$throwIfUnDef(aFunc) : Function`

````text
Returns a function that tries to execute aFunc and throws and exception if the result if undefined otherwise returns the result. Usefull with $retry when waiting for a "defined" result.
````

### $unset

`$unset(aKey)`

````text
Unset a previously set value with aKey.
````

### AF.encryptText

`AF.encryptText()`

````text
Interactevly asks to enter a text and then uses af.encrypt to print to stdout the result.
````

### AF.endOpenAFAndStart

`AF.endOpenAFAndStart(aCommandLineArray, noStop, redirectOutput)`

````text
Calls endOpenAFAndStart to start a detached process and then end the current OpenAF execution. noStop=true can be used to avoid exiting the current OpenAF process. If redirectOutput is true (default), output is redirected to /dev/null on Unix (on Windows output is always visible). Set redirectOutput to false to keep the output visible.
````

### AF.endOpenAFAndStartOpenAF

`AF.endOpenAFAndStartOpenAF(aCommandLineArray, preCommandLineArray, noStop, redirectOutput)`

````text
Calls endOpenAFAndStartOpenAF to detach and start another OpenAF with current arguments plus extras. If redirectOutput is true (default), output is redirected to /dev/null on Unix (on Windows output is always visible). Set redirectOutput to false to keep the output visible.
````

### AF.fromJSSLON

`AF.fromJSSLON(aString) : Object`

````text
Tries to convert the provided aString into an object. The string might be JSON or SLON.
````

### AF.fromJavaArray

`AF.fromJavaArray(aJavaArray) : Array`

````text
Tries to convert aJavaArray into a native an array.
````

### AF.fromNLinq

`AF.fromNLinq(aString) : Map`

````text
Converts a nLinq chained command line string representation into a suitable map to be used with $from.query.
````

### AF.fromSLON

`AF.fromSLON(aString) : Map`

````text
Converts a SLON (https://github.com/nmaguiar/slon) string representation into the original map.
````

### AF.fromSQL

`AF.fromSQL(aString) : Map`

````text
Converts a SQL expression into an ASP map.
````

### AF.fromSQL2NLinq

`AF.fromSQL2NLinq(aSQL) : Map`

````text
Converts a SQL expression into a suitable map to be used with $from.query.
````

### AF.fromTOON

`AF.fromTOON(aTOONStr, alternative) : Object`

````text
Tries to parse aTOONStr into a javascript object. If alternative = true (or, if unset, defaults to __flags.ALTERNATIVES.fromTOON) a native Java TOON engine will be used instead of the bundled Javascript one (faster and lower memory footprint on bigger payloads).
````

### AF.fromYAML

`AF.fromYAML(aYaml) : Object`

````text
Tries to parse aYaml into a javascript map.
````

### AF.getEncoding

`AF.getEncoding(anArrayOfBytesORString) : String`

````text
Given anArrayOfBytesORString will try to detect which encode is used and returns a string with the identified charset encoding.
````

### AF.printStackTrace

`AF.printStackTrace(aFunction) : Object`

````text
Executes aFunction but if it throws an exception and the exception is a Java exception it will print the exception's stack trace.
````

### AF.protectSystemExit

`AF.protectSystemExit(shouldProtect, aMessage)`

````text
Protects the current execution against a exit instruction if shouldProtect = true (otherwise it will unprotect). If protected a security exception with aMessage (string) followed by the exit status will be thrown or the result of calling function aMessage with the exit status as a parameter.
````

### AF.setInteractiveTerminal

`AF.setInteractiveTerminal()`

````text
Sets the current terminal to be interactive (no echo, no buffering).
````

### AF.swap

`AF.swap(anArray, anIndex1, anIndex2) : Array`

````text
Swaps the elements at anIndex1 and anIndex2 in anArray. Returns the new array with the elements swapped.
````

### AF.toCSLON

`AF.toCSLON(aObject, aTheme) : String`

````text
Converts aObject map/array into SLON representation with ansi colors (see more in help for ow.format.toCSLON)
````

### AF.toKYAML

`AF.toKYAML(aJson, multiDoc, sanitize, shouldColor, perEntryNewLine) : String`

Converts `aJson` to a Kubernetes-style YAML (flow) string using these rules:

- Double-quoted string values.
- Unquoted keys unless ambiguous.
- Flow style `{}` for maps and `[]` for arrays.
- If `perEntryNewLine` (or `__flags.YAML.perEntryNewLine`) is true, each entry or element appears on its own line, similar to JSON pretty-print.

If `multiDoc` is true and `aJson` is an array, multiple documents are emitted separated by `---`.
If `sanitize` is true, Java objects are stringified. Toggle color with `shouldColor`.

### AF.toSLON

`AF.toSLON(aObject, aTheme) : String`

````text
Converts aObject map/array into SLON representation (see more in help for ow.format.toSLON)
````

### AF.toTOON

`AF.toTOON(aObj, alternative) : String`

````text
Tries to convert aObj into a TOON string. If alternative = true (or, if unset, defaults to __flags.ALTERNATIVES.toTOON) a native Java TOON engine will be used instead of the bundled Javascript one (faster and lower memory footprint on bigger payloads).
````

### AF.toYAML

`AF.toYAML(aJson, multiDoc, sanitize, shouldColor) : String`

````text
Tries to dump aJson into a YAML string. If multiDoc = true and aJson is an array the output will be multi-document. If sanitize = true all Java objects will be converted to avoid parsing errors.
````

### AF.unsetInteractiveTerminal

`AF.unsetInteractiveTerminal()`

````text
Unsets the current terminal to be interactive (no echo, no buffering).
````

### __colorFormat

`__colorFormat`

Global map with the ANSI color/style settings used when printing colored output (colorify, cprint*, printTable/printTree,
ask/askChoose/askChooseMultiple prompts and markdown rendering). Each color value is a comma-separated list of ansiColor
attributes (e.g. "BOLD,CYAN", "FG(12)", "RESET"). Entries can be changed at runtime to customize the theme:

- key, number, string, boolean, date, default: colors used by colorify and tree/table values per data type.
- askPre, askQuestion, askChoose, askChooseFilter, askPos: colors used by ask, askChoose and askChooseMultiple.
- `askChooseChars`: characters used in choose prompts (chooseMultipleSelected, chooseMultipleUnselected, chooseUp, chooseDown, chooseLine).
- `table`: { lines, value, title, bandRow, format } colors for table output; the optional "format" (table, stable, ctable, btable or bstable)
  selects the default table renderer for `$output` when no global or explicit format is set.
- `tree`: { lines } color for tree connecting lines (other tree options are merged with `__flags.TREE`).
- `md`: colors used by `ow.format.withMD`: codeBlock {line, text, theme}, codeInline {text, surround}, heads {h1..h4}, line, link {text, url},
  bullets, list, strike and note {line, text, theme}. Missing md entries are filled with defaults on first use.

Example:

```javascript
__colorFormat.string = "GREEN"; __colorFormat.table.title = "BOLD,UNDERLINE"; __colorFormat.md.heads.h1 = "CYAN,BOLD"
```

### _i$

`_i$(aValue, aPrefixMessage) : Object`

````text
Same as _$ but if aValue is not defined and aPrefixMessage if defined it will use ask() or askEncrypt() to  interactively ask the user for the value with the prompt "[aPrefixMessage]: ". Should only be used if user interaction is expected but to force not be interactiv you can set __i$interactive to false). Note: askEncrypt will be used if aPrefixMessage has any reference to "secret" or "pass".
````

### addOPackRemoteDB

`addOPackRemoteDB(aURL)`

````text
Adds a path to an opack.db file to the current search path.
````

### addOnOpenAFShutdown

`addOnOpenAFShutdown(aFunction) : Boolean`

````text
Adds aFunction to try to execute whenever OpenAF is going to shutdown. The latest hook added will be the first to be executed until the first hook added (actually a shortcut for Threads.addOpenAFShutdownHook).
````

### af.fromJava2JS

`af.fromJava2JS(aJavaObj) : Object`

````text
Tries to convert the provided Java object to a native javascript object
````

### af.fromObj2XML

`af.fromObj2XML(aMap, sanitize, aAttrKey) : String`

````text
Tries to convert aMap into a similiar XML strucuture returned as string. Note that no validation of XML strucuture is performed.  If aAttrKey string is defined it will be used to prefix attributes (from af.fromXML2Obj). Tips: ensure each map is under a map key.
````

### af.fromTOML

`af.fromTOML(aTOML) : Object`

````text
Tries to parse aTOML into a javascript object
````

### af.fromXML2Obj

`af.fromXML2Obj(xml, ignored, aPrefix, reverseIgnored) : Object`

````text
Tries to convert a XML object into a javascript object. Tag attributes will be ignored unless the corresponding tag name is included on the ignored array and attributes will be added to the corresponding map with a prefix "_" (or aPrefix). Optionally if reverseIgnored = true the ignored array will be used to not include the tag name in the ignored array.
````

### af.nvl

`af.nvl(aValue, aDefault) : Object`

````text
Returns aValue if it is defined or aDefault otherwise.
````

### af.runFromExternalClass

`af.runFromExternalClass(aClassName, aPath)`

Tries to "execute" `aClassName` from a previously compiled OpenAF script, with `af.compileToClasses`, on `aPath`.

Example:

```javascript
af.compileToClasses("MyClass", "var myOpen = 'AF Class'", ".");
af.runFromExternalClass("MyClass", ".");
myOpen; // AF Class
```

### af.toTOML

`af.toTOML(aObj) : String`

````text
Tries to convert aObj into a TOML string.
````

### ansiColor

`ansiColor(aAnsi, aString, force, noCache, noReset) : String`

Returns the ANSI codes together with `aString`, if determined that the current terminal can handle ANSI codes (overridden
by `force` = true), with the attributes defined in `aAnsi`. Please use with ansiStart() and ansiStop().
The optional `noReset` boolean flag will remove ansi reset as part of the string returned.
The attributes separated by commas can be:

- `BLACK`, `RED`, `GREEN`, `YELLOW`, `BLUE`, `MAGENTA`, `CYAN`, `WHITE`
- `FG_BLACK`, `FG_RED`, `FG_GREEN`, `FG_YELLOW`, `FG_BLUE`, `FG_MAGENTA`, `FG_CYAN`, `FG_WHITE`
- `BG_BLACK`, `BG_RED`, `BG_GREEN`, `BG_YELLOW`, `BG_BLUE`, `BG_MAGENTA`, `BG_CYAN`, `BG_WHITE`
- `BOLD`, `FAINT`, `INTENSITY_BOLD`, `INTENSITY_FAINT`, `ITALIC`, `UNDERLINE`, `BLINK_SLOW`, `BLINK_FAST`, `BLINK_OFF`, `NEGATIVE_ON`, `NEGATIVE_OFF`, `CONCEAL_ON`, `CONCEAL_OFF`, `UNDERLINE_DOUBLE`, `UNDERLINE_OFF`

### ansiLength

`ansiLength(aString) : Number`

````text
Tries to return the aString length without any ansi control sequences.
````

### ansiStart

`ansiStart(force)`

````text
Prepares to output ansi codes if the current terminal is capable off (unless force = true). Use with ansiColor() and ansiStop().
````

### ansiStop

`ansiStop(force)`

````text
Disables the output of ansi codes if the current terminal is capable off (unless force = true). Use with ansiColor() and ansiStart().
````

### ansiWinTermCap

`ansiWinTermCap() : boolean`

````text
Determines in Windows if the current terminal has support for newer capabilities or not (e.g. cmd.exe)
````

### armFastExitOnShutdown

`armFastExitOnShutdown(anExitCode)`

````text
Arms the same fast-exit trick exit(anExitCode, true) uses (see exit) so it also happens automatically once the JVM actually starts shutting down (a script simply finishing, Ctrl-C, SIGTERM, etc.), not just when exit(code, true) is called explicitly. Once every OpenAF-registered shutdown hook has run, the process terminates immediately with anExitCode - skipping the JVM's own trailing teardown that can otherwise delay exit by several seconds when a JIT compilation is still in flight. Only takes effect once shutdown actually begins, so it doesn't affect normal execution or daemon/server processes that intentionally stay alive. Shortcut for Threads.armFastExitOnShutdown.
````

### arrayContains

`arrayContains(anArray, aObj, aPreFilter) : Number`

````text
Tries to find aObj in anArray returning the position where it's first found or -1 if not found. Optionally aPreFilter function can prepare each object for comparing.
````

### ask

`ask(aPrompt, aMask, aConsole, noAnsi, aWrite) : String`

````text
Stops for user interaction prompting aPrompt waiting for an entire line of characters and, optionally, masking the user input with aMask (e.g. "*"). Returns the user input.
````

### ask1

`ask1(aPrompt, allowed, aConsole, aWrite) : String`

````text
Stops for user interaction prompting aPrompt waiting for a single character within the allowed string (a set of characters). Returns the user input.
````

### askChoose

`askChoose(aPrompt, anArray, aMaxDisplay, aHelpText, aUI) : Number`

````text
Stops for user interaction prompting aPrompt waiting for a single character to choose from the provided anArray of options. Optionally you can provide aMaxDisplay to limit the number of options displayed at a time. Returns the index of the chosen option.
Optional aUI is the console/write/ansi map returned by askConsole (or a compatible injected UI).
````

### askChooseMultiple

`askChooseMultiple(aPrompt, anArray, aMaxDisplay, aHelpText, aUI) : Array`

````text
Stops for user interaction prompting aPrompt waiting for a single character to choose multiple from the provided anArray of options. Optionally you can provide aMaxDisplay to limit the number of options displayed at a time. Returns an array with the chosen options.
````

### askConsole

`askConsole() : Map`

````text
Opens an independent controlling terminal (including with piped stdin/redirected stdout). Returns console/write/ansi/close for injection into askChoose and ask. Close in finally. Throws if no controlling terminal is available. Does not replace process input or output.
````

### askDef

`askDef(aInit, aQuestion, isSecret, isVoidable, aUI) : String`

````text
If aInit is not defined will ask aQuestion (if isSecret = true it will askEncrypt) and return the value. If isVoidable = true and no answer is provided it will return undefined.
````

### askEncrypt

`askEncrypt(aPrompt, aConsole, noAnsi, aWrite) : String`

````text
Similar to ask but the return user input will be encrypted. If an empty string is entered by the user the function will return undefined.
````

### askKey

`askKey(aUI, aTimeoutMs, aOptions) : String|Map`

````text
Reads a single key from aUI (a map returned by askConsole or compatible, providing read(aTimeoutMs) that returns a character code, -2 on timeout and -1 on end of input) and returns a normalized name: "up", "down", "left", "right", "home", "end", "pgup", "pgdn", "delete", "insert", "enter", "tab", "shift-tab", "backspace", "esc", "eof", "ctrl-<letter>", "alt-<char>" or the printable character itself. With aOptions.mouse true, also returns { type: "mouse", button, x, y, release } for SGR mouse reports (1-based cells). Mouse reports are otherwise consumed without returning a key. Returns undefined if aTimeoutMs expires without input. A lone ESC is told apart from escape sequences with a short timeout.
````

### askN

`askN(aPromptFn, aStopFn, aConsole) : String`

````text
Stops for a multi-line user interaction prompting, for each line, the result of calling aPromptFn that receives the current user input  (if a string is provided it will default to a function that returns that string). The interaction will stop when aStopFn function, that receives the current user input as an argument, returns true (if the function is not provided it will default to 3 new lines).
````

### askStruct

`askStruct(anArrayOfQuestions, aUI) : Array`

Given `anArrayOfQuestions` with a structure like:

```javascript
[
 { name: "question1", prompt: "Question 1", type: "question" },
 { name: "question2", prompt: "Question 2", type: "secret" },
 { name: "question3", prompt: "Question 3", type: "char", options: "YN" },
 { name: "question4", prompt: "Question 4", type: "choose", options: ["Option 1", "Option 2", "Option 3"], output: "index" },
 { name: "question5", prompt: "Question 5", type: "multiple", options: ["Option 1", "Option 2", "Option 3"], max: 2 }
]
```

Will prompt the user for each question and return an array with the answers.

The type can be:

- "question" (default)
- "secret"
- "char" (requires options)
- "choose" (requires options)
- "multiple" (requires options)

### bcrypt

`bcrypt(aText, aVerifyHash, hashingRounds) : String/boolean`

````text
If aText is provided it will return the resulting string of applying the bcrypt hash to aText. Optionally the bcrypt hashingRounds (between 4 and  31, default 10) can be provided (note: the more rounds, the more slower and secure). If aVerifyHash is provided it will return a boolean determining if the provided aVerifyHash (result of a previous bcrypt) matches the aText provided (hashingRounds will be ignored since the hash string already provides the rounds used).
````

### beautifier

`beautifier(anObject) : String`

````text
Shortcut for the af.js2s function providing a human readable representation of the javascript object provided.
````

### beep

`beep()`

````text
Tries to produce a beep sound.
````

### bprint

`bprint(aStr)`

"Beautifies" and prints the `aStr` to the stdout (with a new line on the end) (example: `bprint("hello world!")`)

### bprintErr

`bprintErr(aStr)`

"Beautifies" and prints the `aStr` to the stderr (with a new line on the end) (example: `bprintErr("Hupps!! A problem!")`)

### bprintErrnl

`bprintErrnl(aStr)`

"Beautifies" and prints the `aStr` to the stderr (without adding a new line on the end) (example: `bprintErrnl("Hupps!! A problem!")`)

### bprintnl

`bprintnl(aStr)`

"Beautifies" and prints the `aStr` to the stdout (without adding a new line on the end) (example: `bprintnl("hello world!")`)

### checkLatestVersion

`checkLatestVersion() : String`

````text
Tries to determine what is the latest available version for OpenAF. Compare it with getVersion() to determine if you need an update.
````

### clearInterval

`clearInterval(uuid)`

````text
Clears the interval with the provided uuid returned by setInterval.
````

### clone

`clone(anObject) : aClonedObject`

````text
Creates a new copy of a JavaScript object.
````

### cls

`cls()`

````text
Tries to clear the screen. The commands to try to clean the screen are given in ANSI.
````

### colorify

`colorify(aObject) : String`

````text
Tries to ANSI colorify a json aObject for use with cprint, cprintErr, cprintErrnl and cprintnl. Colors are defined in __colorFormat.
````

### compare

`compare(X, Y) : Boolean`

````text
Compares a X object to a Y object at the content level. If they are equal the function will return true otherwise it will return false.
````

### compress

`compress(anObject) : ArrayOfBytes`

````text
Compresses a JSON object into an array of bytes suitable to be uncompressed using the uncompress function.
````

### conReset

`conReset() : boolean`

````text
Tries to reset the console to its original state. Returns true if successful.
````

### cprint

`cprint(aStr)`

"Stringifies" in ANSI color and prints the `aStr` to the stdout (with a new line on the end) (example: `cprint("hello world!")`)

### cprintErr

`cprintErr(aStr)`

"Stringifies" in ANSI color and prints the `aStr` to the stderr (with a new line on the end) (example: `cprintErr("Hupps!! A problem!")`)

### cprintErrnl

`cprintErrnl(aStr)`

"Stringifies" in ANSI color and prints the `aStr` to the stderr (with a new line on the end) (example: `cprintErrnl("Hupps!! A problem!")`)

### cprintnl

`cprintnl(aStr)`

"Stringifies" in ANSI color and prints the `aStr` to the stdout (with a new line on the end) (example: `cprintnl("hello world!")`)

### createDB

`createDB(aFile, aLogin, aPass) : DB`

````text
Creates a DB object instantiated with a file based H2 database for the aFile provided. Optionally you can use aLogin and aPass(word).
````

### createDBInMem

`createDBInMem(aName, dontClose, aLogin, aPass, inMemFileSystem, inMemCompressed, useNIO) : DB`

````text
Creates a DB object instantiated with an in-memory database for the given name. Optionally you can  specify that you don't want it to close on db.close (but all data will be lost on exiting OpenAF). Optionally you can also specify aLogin and aPass. This is a H2 database so do check more documentation on http://www.h2database.com/.  Also optionally you can specify if you want the in-memory database to be file based (inMemFileSystem) which  is slower than normal; to be compressed (inMemCompressed) which is slower than normal and inMemFileSystem; to store data outside the VM's heap (useNIO). Do note that if inMemFileSystem and inMemCompressed are selected only inMemCompressed will be used. And useNIO will only affect inMemFileSystem or inMemCompressed options.
````

### createDBServer

`createDBServer(aFile, aPort, aLogin, aPass) : DB`

````text
Creates a DB object instantiated with a server based H2 database, on the provided aPort (defaults to 9090), for the aFile provided. Optionally you can use aLogin and aPass(word).
````

### csv.fromArray2File

`csv.fromArray2File(anArray, aFile, withHeadersOrStreamFormat) : Number`

````text
Tries to wirte anArray to aFile. If withHeadersOrStreamFormat is provided, if an array it will  be interpreted as the files of headers otherwise as the new streamFormat object to use.
````

### csv.fromFile2Array

`csv.fromFile2Array(aFile, withHeadersOrStreamFormat) : Array`

````text
Tries to read a CSV file and convert it into an array. If withHeadersOrStreamFormat is provided, if an array it will  be interpreted as the files of headers otherwise as the new streamFormat object to use.
````

### deleteFromArray

`deleteFromArray(anArray, anIndex) : Array`

````text
Deletes the array element at anIndex from the provided anArray. Returns the new array with the element removed.
````

### descType

`descType(aObject) : String`

````text
Given aObject will try to return the apparent type withing: undefined, null, bytearray, javaclass, java, boolean, array, number, string, function, date, map and object.
````

### dumpLog

`dumpLog() : Array`

````text
Returns an array with collected log messages. Each entry has: d - timestamp; t - type; m - message.
````

### endOpenAFAndStart

`endOpenAFAndStart(aCommandLineArray, noStop, redirectOutput)`

````text
Terminates the current OpenAF execution while trying to execute the commands on the aCommandLineArray in detached mode. On Unix systems it uses nohup (and setsid if available). On Windows it uses cmd start. If redirectOutput is true (default), output is redirected to /dev/null on Unix (on Windows output is always visible). Set redirectOutput to false to keep the output visible.
````

### endOpenAFAndStartOpenAF

`endOpenAFAndStartOpenAF(aCommandLineArray, preCommandLineArray, noStop, redirectOutput)`

````text
Terminates the current OpenAF execution and tries to start a detached OpenAF process with the current OpenAF command line plus an extra aCommandLineArray. preCommandLineArray can be used to provide java arguments. If redirectOutput is true (default), output is redirected to /dev/null on Unix (on Windows output is always visible). Set redirectOutput to false to keep the output visible.
````

### exit

`exit(anExitCode, force)`

````text
Immediately exits execution with the provided exit code. Optionally force=true can be provided to run any registered OpenAF shutdown hooks (see addOnOpenAFShutdown/Threads.addOpenAFShutdownHook) synchronously and then terminate the process at the operating system level, bypassing the JVM's own shutdown sequence. Regular JVM shutdown hooks not registered through OpenAF, and File.deleteOnExit() entries, will NOT run in this case. Use this when a still-running JIT compilation would otherwise stall a plain exit() for several seconds waiting for the JVM's safepoint teardown to complete. To get the same behavior on shutdown paths that don't call exit() explicitly (a script simply finishing, Ctrl-C, SIGTERM), see armFastExitOnShutdown.
````

### extend

`extend([deep], target [, object1][, objectN]) : Object`

````text
Merges the contents of two or more objects together into the first object (target). If deep is specified the copy will be recursive. This function is equivalent to JQuery's extend function. See more in  https://api.jquery.com/jquery.extend/
````

### findRandomOpenPort

`findRandomOpenPort() : number`

````text
Tries to find a random open port on all network interfaces. Useful to start network servers on an available port.
````

### flatten

`flatten(aObject, noKeyValSeparation) : Array`

````text
Given aObject it will traverse it and create an array where each element will have a key and a val(ue). The key will  begin with a "." whenever it's a children key on aObject. This function is useful when trying to find specific keys or values across a Map. Optionally you can specify that you don't want each array element with the key and the value as separate elements but rather a directly as key and value.
````

### forkOpenAF

`forkOpenAF(aCommandLineArray, preCommandLineArray) : Promise`

````text
Starts another OpenAF with the same command line, if aCommandLineArray is not provided.  If aCommandLineArray is provided each array element will be use sequentially to build the command line to start a new OpenAF instance. preCommandLineArray can be used to  provide java arguments if defined.
````

### genUUID

`genUUID(useSecureRandom) : String`

````text
Generates and returns an UUID using a javascript algorithm (if needed you can refer to the  AF operation AF.KeyGenerator.GenerateUUID).
````

### getCPULoad

`getCPULoad(useAlternative) : Number`

````text
Tries to obtain the current system load average (equivalent to top). If not available a negative value will be returned. Optionally you can specify to use the current system load if useAlternative = true. If the current system doesn't provide a load average it will fallback to the current system load.
````

### getChLog

`getChLog() : Channel`

````text
Returns the current log dump channel.
````

### getDistribution

`getDistribution() : String`

````text
Returns the current distribution channel for this version of OpenAF.
````

### getEnv

`getEnv(anEnvironmentVariable) : String`

````text
Returns the current value of the operating system anEnvironmentVariable.
````

### getEnvs

`getEnvs() : Map`

````text
Returns a map of key and values with the operating system environment variables.
````

### getEnvsDef

`getEnvsDef(aEnv, aVar, aDefault, isJson) : Object`

````text
Given an environment variable aEnv name will check if a value is provided and return it if so. Otherwise it will check the value of aVar and return it if defined. If aVar is also not defined it will return aDefault. Optionally if isJson=true the value of the provided aEnv will be parsed from JSON or SLON.
````

### getFromZip

`getFromZip(aZipFile, aResource, inBytes, anEncoding, notInMemory) : anArrayOfBytes`

````text
Retrieves aResource, as anArrayOfBytes, from aZipFile. This resource can be inBytes = true or not and anEncoding can be provided. If the resource to retrieve is big you can use notInMemory = true for a slower but less memory retrieval.
````

### getJavaStackTrace

`getJavaStackTrace(anException) : Array`

````text
Given a javascript anException, if it's a wrapped or directly a java exception it will try to obtain the corresponding stack trace information in the form of an array.
````

### getNumberOfCores

`getNumberOfCores(realValue) : Number`

````text
Try to identify the current number of cores on the system where the script is being executed.
````

### getOPackLocalDB

`getOPackLocalDB() : Array`

````text
Returns an Array of maps. Each map element is an opack package description of the currently  locally, and per user, installed opack packages.
````

### getOPackPath

`getOPackPath(aPackage) : String`

````text
Given aPackage name (a opack name) will search the opack and if installed will return the filesystem path where the opack is installed.
````

### getOPackPaths

`getOPackPaths() : Array`

````text
Returns an array of strings with the paths for each of the installed opacks.
````

### getOPackRemoteDB

`getOPackRemoteDB() : Array`

````text
Returns an Array of maps. Each map element is an opack package description registered in the OpenAF central repository. Results are cached using $cache for __flags.OPACK_REMOTE_DB_CACHE_TTL milliseconds (default: 60000).
````

### getOpenAFJar

`getOpenAFJar() : String`

````text
Returns the complete filepath and name for the OpenAF jar file. (Shortcut for af.getOpenAFJar()). If __forcedOpenAFJar is defined the corresponding value will be used (useful when detection of the OpenAF jar doesn't work as expected or when OpenAF is embedded.
````

### getOpenAFPath

`getOpenAFPath() : String`

````text
Returns the filesystem path to the openaf.jar currently being used for the script execution.
````

### getPid

`getPid() : String`

````text
Tries to retrieve the current script execution operating system PID and returns it.
````

### getVersion

`getVersion() : String`

````text
Shortcut for the af.getVersion (see more af.getVersion) function. Will return the current version of OpenAF being used.
````

### hmacSHA1

`hmacSHA1(data, key, toHex) : ArrayOfBytes`

````text
Given data and a key will calculate the hash-based message authentication code (HMAC) using the SHA1 hash function. Optionally if toHex = true the output will be converted to hexadecimal lower case.
````

### hmacSHA256

`hmacSHA256(data, key, toHex) : ArrayOfBytes`

````text
Given data and a key will calculate the hash-based message authentication code (HMAC) using the SHA256 hash function. Optionally if toHex = true the output will be converted to hexadecimal lower case.
````

### hmacSHA384

`hmacSHA384(data, key, toHex) : ArrayOfBytes`

````text
Given data and a key will calculate the hash-based message authentication code (HMAC) using the SHA384 hash function. Optionally if toHex = true the output will be converted to hexadecimal lower case.
````

### hmacSHA512

`hmacSHA512(data, key, toHex) : ArrayOfBytes`

````text
Given data and a key will calculate the hash-based message authentication code (HMAC) using the SHA512 hash function. Optionally if toHex = true the output will be converted to hexadecimal lower case.
````

### includeOPack

`includeOPack(aOPackName, aMinVersion)`

````text
Ensures that aOPackName is installed. Optionally you can provide a minimal opack version. If the opack is not installed, can't be installed or cannot be updated to a version bigger or equal to aMinVersion an exception will be thrown.
````

### inherit

`inherit(Child, Parent)`

````text
Associates a Child object to a Parent simulating a inheritance relationship. This is done by copying the Parent prototype to the Child prototype. This is similar to "Parent.call(this, arg1, arg2)"
````

### io.copyJSONRange

`io.copyJSONRange(aFile, aStart, anEnd, anOutputStream, aOptions)`

````text
Copies an exclusive byte range discovered by io.scanJSON using bounded buffers. The output is borrowed and remains open. Input is always closed. Optional cancel/progress functions work as in io.scanJSON.
````

### io.extractJSON

`io.extractJSON(aFile, aPath, anOutputStream, aOptions) : boolean`

````text
Copies the JSON value at a literal key/index path to a borrowed output stream. An empty path selects the root. Returns false without writing when absent. Uses bounded buffers and preserves original JSON bytes. The source must remain unchanged during extraction. Options cancel/progress/maxNodes apply to scanning; copy progress restarts at zero. Early selection does not validate the unread suffix.
````

### io.isBinaryFile

`io.isBinaryFile(aFile, confirmLimit) : boolean`

````text
Tries to determine if the provided aFile is a binary or text file by checking the first 1024 chars (limit can be changed using confirmLimit). Returns true if file is believed to be binary. Based on the function isBinaryArray.
````

### io.listFilesTAR

`io.listFilesTAR(aTARfile, isGzip) : Array`

````text
Given aTARfile (or output stream (with isGzip = true/false)) will return an array with the TAR file entries. Each entry will have: isDirectory (boolean), isFile (boolean), canonicalPath (string), filepath (string), filename (string), size (number), lastModified (date), groupId (string), group (string), userId (string) and user (string).
````

### io.lz4

`io.lz4(anInput) : bytes`

````text
Compresses anInput using LZ4 compression and returns the compressed bytes.
````

### io.onDirEvent

`io.onDirEvent(aPath, aFn, aFnErr) : Promise`

Given `aPath` of a directory will return a promise (`$do`) that, for every create, modify or delete event that happens on `aPath` it will call `aFn` with two parameters: kind and filename.
The 'kind' string can be one of four events: ENTRY_CREATE, ENTRY_DELETE, ENTRY_MODIFY, OVERFLOW (meaning events were lost or discarded). The 'filename' represents the filename affected.
Optionally `aFnErr` function can be provided to handle any errors and, in case `aPath` no longer exists, `aFnErr` will be called with the string "ENTRY_NA". Example:

```javascript
var p = io.onDirEvent("myDir", (kind, filename) => {
   log("Event '" + kind + "' on '" + filename + "'");
}, e => {
   if (isString(e) && e == "ENTRY_NA") logWarn("myDir no longer exists."); else logErr(e);
});

$doWait(p);
```

### io.pipeCh

`io.pipeCh(aFunc)`

````text
Starts a wait on stdin calling aFunc everytime a character is sent to stdin. The wait cycle breaks when aFunc returns true.
````

### io.pipeLn

`io.pipeLn(aFunc)`

````text
Starts a wait on stdin calling aFunc everytime a line is sent to stdin. The wait cycle breaks when aFunc returns true.
````

### io.readFileBytesRO

`io.readFileBytesRO(aFile) : ByteArray`

````text
Tries to read aFile in read-only mode (even if being used by another process) and returns the corresponding byte array.
````

### io.readFileJSON

`io.readFileJSON(aJSONFile) : Object`

````text
Tries to read aJSONFile into a javascript object.
````

### io.readFileLZ4Stream

`io.readFileLZ4Stream(aFile) : InputStream`

````text
Reads aFile as a LZ4 compressed stream and returns the InputStream to read from. This is useful to read large files that are compressed with LZ4 without decompressing them into memory.
````

### io.readFileTAR2Stream

`io.readFileTAR2Stream(aTARfile, isGzip, aFunc)`

````text
Given aTARFile (or stream) will call aFunc(tion) with the corresponding Java TAR input stream. If aTARFile is a stream you should specify with isGzip = true/false if it has been "gzipped". Note: for direct usage use io.readFileTARStream
````

### io.readFileTARBytes

`io.readFileTARBytes(aTARFile, aFilePath, isGzip) : ByteArray`

````text
Given aTARFile (or stream) will try to retrieve aFilePath and return the corresponding byte array. If aTARFile is a stream you should specify with isGzip = true/false if it has been "gzipped".
````

### io.readFileTARStream

`io.readFileTARStream(aTARFile, aFilePath, isGzip, aFunc)`

````text
Given aTARFile (or stream) will try to retrieve aFilePath and call aFunc(tion) with the corresponding Java input stream. If aTARFile is a stream you should specify with isGzip = true/false if it has been "gzipped".
````

### io.readFileTOML

`io.readFileTOML(aFile) : Object`

````text
Tries to read aFile and parse it as TOML into a javascript object.
````

### io.readFileYAML

`io.readFileYAML(aYAMLFile) : Object`

````text
Tries to read aYAMLFile into a javascript object.
````

### io.readJSONArray

`io.readJSONArray(source, callback, encoding, raw) : Number`

````text
Reads a top-level JSON array from a filename or a Java input stream, retaining only one element at a time. Calls callback(value, zeroBasedIndex) for each element. Return true to stop early. Encoding defaults to UTF-8. With raw=true the callback receives each element as JSON text instead. Returns the number of delivered elements. Non-array roots, malformed JSON and trailing content throw. Filename streams are closed even on errors; caller-provided streams remain owned by the caller.
````

### io.readLinesNDJSON

`io.readLinesNDJSON(aNDJSONFile, aFuncCallback, aErrorCallback, anEncoding)`

````text
Opens aNDJSONFile (a newline delimited JSON) (a filename or an input stream) as a stream call aFuncCallback with each parse JSON. If aFuncCallback returns true the cycle will be interrupted. For any parse error it calls the aErrorCallback  with each exception.
````

### io.readStreamJSON

`io.readStreamJSON(aJSONFile, aValFunc) : Map`

Reads a JSON file (`aJSONFile`) without loading all structures to memory (useful to handling large JSON files).
The `aValFunc` receives a single string argument with the current JSON path being processed (for example $.log.entries[123].request),
where "$" is the root of the JSON document. When `aValFunc` returns true the current JSON structure is recorded in memory.
If `aValFunc` is not defined it will return true for all paths. Returns the JSON structure recorded in memory.

Example:

```javascript
var amap = io.readStreamJSON("someFile.har",
                             path => (/^\$\.log\.entries\[\d+\]\.request/).test(path))
```

### io.scanJSON

`io.scanJSON(aFile, aVisitor, aOptions) : Map`

````text
Visits UTF-8 JSON without materializing values. Events have phase (value/end), path (an array of literal keys/indices), type, start and, on end, end (exclusive byte offsets) and size for traversed containers. Return "skip" on a value to skip its children, or "stop" to stop. Options: cancel (function), progress (function receiving byte offset), maxNodes. A stopped scan does not validate the unread suffix. The file and parser are always closed.
````

### io.unlz4

`io.unlz4(anInput) : Map/String`

````text
Decompresses anInput using LZ4 compression and returns the decompressed map or string.
````

### io.unzip

`io.unzip(zipFile, targetDir, logFn, logErrFn)`

> Example formatting/syntax corrected against the implementation; the signature is unchanged.

Tries to unzip a `zipFile` into `targetDir`. Optionally you can provide a `logFn` and `logErrFn` to log the progress.
The `logFn` will receive the following object:

```text
{ type: "file" | "dir", source: [zip entry], target: [targetPath] }
```

### io.writeFileJSON

`io.writeFileJSON(aJSONFile, aObj, aSpace)`

````text
Tries to write a javascript aObj into a aJSONFile with an optional aSpace.
````

### io.writeFileLZ4Stream

`io.writeFileLZ4Stream(aFile) : InputStream`

````text
Reads aFile as a LZ4 compressed file and returns the InputStream to read from. This is useful to read large files that are compressed with LZ4 without decompressing them into memory.
````

### io.writeFileTAR4Stream

`io.writeFileTAR4Stream(aTARfile, isGzip, aFunc)`

````text
Given aTARfile (or output stream (with isGzip = true/false)) will call aFunc with the Java TAR output stream. Note: for direct usage use io.writeFileTARStream
````

### io.writeFileTARBytes

`io.writeFileTARBytes(aTARfile, aFilePath, isGzip, aArrayBytes)`

````text
Given aTARfile (or output stream (with isGzip = true/false)) will write aArrayBytes into aFilePath in the TAR file/stream. Note: for multiple files use io.writeFileTARStream
````

### io.writeFileTARStream

`io.writeFileTARStream(aTARfile, isGzip, aFunc, aDefaultMap)`

````text
Given aTARfile (or output stream (with isGzip = true/false)) will call aFunc(tion) providing, as argument, a writer function with three arguments: aFilePath, a Java input stream for the contents and the modification date for the target file.  Optionally aDefaultDate can be provided to be used whenever a date is not provided or for folders.
````

### io.writeFileTOML

`io.writeFileTOML(aFile, aObj)`

````text
Tries to write aObj into aFile as TOML.
````

### io.writeFileYAML

`io.writeFileYAML(aYAMLFile, aObj, multidoc)`

````text
Tries to write a javascript aObj into a aYAMLFile. If multiDoc = true and aJson is an array the output will be multi-document.
````

### io.writeLineNDJSON

`io.writeLineNDJSON(aNDJSONFile, aObj, aEncode)`

````text
Writes aObj into a single line on aNDJSONFile (newline delimited JSON) (or an output stream). Optionally you can provide an encoding (only is a string filename is provided)
````

### io.zip

`io.zip(targetDir, zipFile, logFn, logErrFn)`

> Example formatting/syntax corrected against the implementation; the signature is unchanged.

Tries to zip a `targetDir` into a `zipFile`. Optionally you can provide a `logFn` and `logErrFn` to log the progress.
The `logFn` will receive the following object:

```text
{ type: "file" | "dir", source: [io.listFile entry], target: [targetPath] }
```

### ioSetNIO

`ioSetNIO(aFlag)`

````text
Sets the default use of NIO in ioStream* functions. It's overridden if the ioStream* function defines a value for the useNIO function argument.
````

### ioStreamCopy

`ioStreamCopy(aOutputStream, aInputStream)`

````text
Copies the contents of a Java aInputStream to a Java aOutputStream. The two streams will  be closed in the end.
````

### ioStreamRead

`ioStreamRead(aStream, aFunction, aBufferSize, useNIO, encoding)`

````text
Given a Java input or output stream helps to read strings by using aFunction with a string argument for each buffer size  (default 1024 characters). Optionally you can provide a different aBufferSize (default: 1024) and/or also specify that  Java NIO functionality should be used. If aFunction returns true the read operation stops.
````

### ioStreamReadBytes

`ioStreamReadBytes(aStream, aFunction, aBufferSize, useNIO)`

````text
Given a Java input or output stream helps to read an array of bytes by using aFunction with anArrayOfBytes argument for  each buffer size (default 1024 characters). Optionally you can provide a different aBufferSize (default: 1024) and/or  also specify that Java NIO functionality should be used. If aFunction returns true the read operation stops.
````

### ioStreamReadLines

`ioStreamReadLines(aStream, aFunctionPerLine, aSeparator, useNIO, anEncoding)`

````text
Given aStream will read the entire buffer and call aFunctionPerLine(withALine) per each \n found. Aditionally you can specify a different aSeparator for each line other than "\n".  If aFunctionPerLine returns true the read operation stops. Optionally you can also provide anEncoding.
````

### ioStreamWrite

`ioStreamWrite(aStream, aString, aBufferSize, useNIO)`

````text
Given a Java input or output stream helps to write aString into the same. Optionally you can provide a different aBufferSize (default: 1024) and/or also specify that Java NIO functionality should be used.
````

### ioStreamWriteBytes

`ioStreamWriteBytes(aStream, aArrayBytes, aBufferSize, useNIO)`

````text
Given a Java input or output stream helps to write aArrayBytes into the same. Optionally you can provide a different aBufferSize (default: 1024) and/or also specify that Java NIO functionality should be used.
````

### isArray

`isArray(aObj) : boolean`

````text
Returns true if aObj is an array, false otherwise.
````

### isBinaryArray

`isBinaryArray(anArrayOfChars, confirmLimit, previousResult) : boolean`

````text
Tries to determine if the provided anArrayOfChars is binary or text. The detection is performed with the first 1024 chars ( that can be changed if confirmLimit is provided). Additionally is possible to link multiple calls providing the last result on previousResult for multiple subsequences of a main array of chars sequence. Should work for utf8, iso-8859-1, iso-8859-7,  windows-1252 and windows-1253. Returns true if file is believed to be binary.
````

### isBoolean

`isBoolean(aObj) : boolean`

````text
Returns true if aObj is boolean, false otherwise
````

### isByteArray

`isByteArray(aObj) : boolean`

````text
Returns true if aObj is a byte array object, false otherwise.
````

### isDate

`isDate(aObj) : boolean`

````text
Returns true if aObj is a date, false otherwise
````

### isDecimal

`isDecimal(aObj) : boolean`

````text
Returns true if aObj has a decimal component.
````

### isDef

`isDef(aObject) : boolean`

````text
Returns true if the provided aObject is defined as a javascript variable. It will return false otherwise. (see also isUnDef). Shortcut for the isDefined function.
````

### isDefined

`isDefined(aObject) : boolean`

````text
Returns true if the provided aObject is defined as a javascript variable. It will return false otherwise. (see also isUndefined)
````

### isFunction

`isFunction(aObj) : boolean`

````text
Returns true if aObj is a function, false otherwise;
````

### isInteger

`isInteger(aObj) : boolean`

````text
Returns true if aObj doesn't have a decimal component.
````

### isJavaArray

`isJavaArray(aObj) : boolean`

````text
Returns true if aObj is a Java array, false otherwise
````

### isJavaClass

`isJavaClass(aObj) : boolean`

````text
Return true if aObj is a Java class, false otherwise
````

### isJavaException

`isJavaException(aObject) : boolean`

````text
Determines if aObject is a java exception object or a javascript exception with an embeeded java exception.
````

### isJavaObject

`isJavaObject(aObj) : boolean`

````text
Returns true if aObj is a Java object, false otherwise
````

### isMap

`isMap(aObj) : boolean`

````text
Returns true if aObj is a map, false otherwise.
````

### isNull

`isNull(aObj) : boolean`

````text
Returns true if aObj is null, false otherwise
````

### isNumber

`isNumber(aObj) : boolean`

````text
Returns true if aObj can be a number, false otherwise
````

### isObject

`isObject(aObj) : boolean`

````text
Returns true if aObj is an object, false otherwise;
````

### isString

`isString(aObj) : boolean`

````text
Returns true if aObj is a string, false otherwise
````

### isTNumber

`isTNumber(aObj) : boolean`

````text
Returns true if aObj is of type number, false otherwise
````

### isUUID

`isUUID(aObj) : boolean`

````text
Returns true if aObj is an UUID.
````

### isUnDef

`isUnDef(aObject) : boolean`

````text
Returns true if the provided aObject is undefined as a javascript variable. It will return false otherwise. (see also isDef). Shortcut for the isUndefined function.
````

### isUndefined

`isUndefined(aObject) : boolean`

````text
Returns true if the provided aObject is undefined as a javascript variable. It will return false otherwise. (see also isDefined)
````

### javaRegExp

`javaRegExp(text).test(regExp, mods) : boolean`

````text
Mimics, using Java, the javascript RegExp test function. Supported mods are "g", "m" and "i" or the java integer composed  mods. Returns the corresponding boolean value.
````

### joniRegExp

`joniRegExp(pattern, options) : Object`

````text
Compiles an Oniguruma (Ruby syntax) pattern once. Options are ignoreCase, dotAll and extended (booleans, default false). Methods: test(input), match(input), matchAll(input), replace(input, replacement), replaceAll(input, replacement), split(input, limit). Matches contain text, index, end (UTF-16 offsets), captures and groups. Replacement strings use JavaScript dollar tokens; callbacks receive match, captures, offset, input and named groups. Inputs must be strings without unpaired surrogates. See docs/joni.md for details.
````

### jsonParse

`jsonParse(aString, alternative, unsafe, ignoreNonJson) : Map`

````text
Shorcut for the native JSON.parse that returns an empty map if aString is not defined, empty or unparsable.
````

### listFilesRecursive

`listFilesRecursive(aPath, usePosix, aFnErr) : Map`

````text
Performs the io.listFiles function recursively given aPath. The returned map will be equivalent to the io.listFiles function (see more in io.listFiles). Alternatively you can specify to usePosix=true and it will add to the map the owner, group and full permissions of each file and folder. When __flags.ALTERNATIVES.listFilesRecursive=true the processing will be done in parallel and aFnErr will be called in case of an error.
````

### load

`load(aScript)`

````text
Provides a shortcut for the af.load function (see more af.load). If the provided aScript is not found this function will try to search the script on the openaf.jar::js folder and on the installed opacks. If it doesn't find the provided aScript it will throw an exception "Couldn't find aScript".
````

### loadAjv

`loadAjv()`

````text
Loads the bundled Ajv v8 JSON Schema validator as global Ajv. OpenAF schema helpers automatically load it and configure formats, draft routing and compatibility options. See ow.obj.schemaInit and docs/json-schema.md.
````

### loadCompiled

`loadCompiled(aScript, dontCompile, dontLoad) : boolean`

````text
Tries to load an OpenAF script as a compiled class. If a compiled class file doesn't exist in the same path it will try to compile and load from the compiled code. If a compiled class file exists in the same path it will recompile it if the modified date of the original aScript is newer than the class. If the class was already loaded or can't be loaded it will return false. Returns true otherwise. Optionally you can force to not compile dontCompile=true or just to compile with dontLoad=true
````

### loadCompiledLib

`loadCompiledLib(aLibClass, forceReload, aFunction, withSync) : boolean`

````text
Loads the corresponding compiled javascript library class and keeps track if it was already loaded or not (in __loadedLibs). Optionally you can force reload and provide aFunction to execute after the successful loading. Returns true if successfull, false otherwise.
````

### loadDBInMem

`loadDBInMem(aDB, aFilename)`

````text
Tries to load to a in-memory database, aDB object, previously created by the function createDBInMem from a SQL aFilename probably created by the function persistDBInMem.
````

### loadDiff

`loadDiff()`

````text
Loads the JsDiff javascript library into scope (check https://github.com/kpdecker/jsdiff).
````

### loadExternalJars

`loadExternalJars(aPath, dontCheck)`

````text
Given a path will try to add to the current classpath (using af.externalAddClasspath) all files with the extension '.jar'. Optionally you can override the dontCheck if it was loaded with this command previously.
````

### loadFuse

`loadFuse()`

Loads the FuseJS javascript library into scope.

See more in: http://fusejs.io/

### loadHandlebars

`loadHandlebars()`

Loads the Handlebars javascript library into scope. Example:

```javascript
loadHandlebars();
var source = "<m>{{#each lines}}\t<s name=\"{{key}}\">{{value}}</s>\n{{/each}}\n</m>";
var data = { "lines": [ { "name": "n1", "value": "v1" }, { "name": "n2", "value": "v2" } ] };
var template = Handlebars.compile(source);
print(template(data));
data.lines.push({"name": "n3", "value": "v3"});
print(template(data));
```

See more documentation in: http://handlebarsjs.com/

### loadHelp

`loadHelp()`

````text
Loads into scope the ODoc objects for documentation support.
````

### loadJSYAML

`loadJSYAML()`

````text
Loads the JS-YAML library.
````

### loadLib

`loadLib(aLib, forceReload, aFunction) : boolean`

````text
Loads the corresponding javascript library and keeps track if it was already loaded or not (in __loadedLibs). Optionally you can force reload and provide aFunction to execute after the successful loading. Returns true if successfull, false otherwise.
````

### loadLodash

`loadLodash()`

Loads the Lodash javascript library.

See more in https://lodash.com/docs

### loadOAFP

`loadOAFP()`

Loads the OpenAF processor that can be used with the function oafp. Example:

```javascript
// Thread unsafe example
oafp({ data: "(abc: 123, xyz: 456)", out: "pm" })
sprint(__pm._map)

// Thread safe example
oafp({ data: "(abc: 123, xyz: 456)", out: "key", __key: "myresult" })
sprint($get("myresult"))
```

### loadPy

`loadPy(aPyScript, aInput, aOutputArray, dontStop) : Map`

````text
Provides a shortcut for the $py function (see more in $py). If the provided aPyScript is not found this function will try to search the python script on the installed opacks. If it doesn't find the provided aScript it will throw an exception "Couldn't find aPyScript". If aInput map is defined each entry will be converted into python variables. If aOutputArray is defined the python variables string names in the array will be returned as a map.
````

### loadTOON

`loadTOON()`

````text
Loads the TOON image encoding/decoding library.
````

### loadUnderscore

`loadUnderscore()`

Loads the Underscore javascript library into scope (using the Lodash alternative).

See more in: http://underscorejs.org and https://lodash.com/docs

### log

`log(msg, formatOptions)`

````text
Outputs to the current stdout a line composed of the current date, indication of INFO and the provided msg. Optionally you can provide a formatOptions map for overriding the defaults from setLog. Note: you can use startLog, stopLog and dumpLog to keep an internal record of theses messages.
````

### logErr

`logErr(msg, formatOptions)`

````text
Outputs to the current stderr a line composed of the current date, indication of ERROR and the provided msg. Optionally you can provide a formatOptions map for overriding the defaults from setLog. Note: you can use startLog, stopLog and dumpLog to keep an internal record of theses messages.
````

### logFlush

`logFlush(aTimeout)`

````text
Will wait for the current log promise to finish. Optionally you can provide aTimeout in milliseconds.
````

### logWarn

`logWarn(msg, formatOptions)`

````text
Outputs to the current warning in a line composed of the current date, indication of WARN and the provided msg. Optionally you can provide a formatOptions map for overriding the defaults from setLog. Note: you can use startLog, stopLog and dumpLog to keep an internal record of theses messages.
````

### lognl

`lognl(msg, formatOptions)`

````text
Outputs to the current stdout, without a new line, a sentence composed of the current date, indication of INFO and the provided msg. Optionally you can provide a formatOptions map for overriding the defaults from setLog. Note: you can use startLog, stopLog and dumpLog to keep an internal record of theses messages.
````

### lprint

`lprint(aStr, withColor)`

````text
"SLONs" and prints the aStr to the stdout (with a new line on the end)
````

### lprintErr

`lprintErr(aStr, withColor)`

````text
"SLONs" and prints the aStr to the stderr (with a new line on the end)
````

### lprintErrnl

`lprintErrnl(aStr, withColor)`

````text
"SLONs" and prints the aStr to the stderr (without adding a new line on the end)
````

### lprintnl

`lprintnl(aStr, withColor)`

````text
"SLONs" and prints the aStr to the stdout (without adding a new line on the end)
````

### mapArray

`mapArray(anArray, selectors, limit) : Array`

````text
Helper functions to map selectors (inputs for ow.obj.getPath) from anArray returning the filtered array. IF selectors is a string or just one array entry the result will be an array with just the value results. Optionally you can also limit the number of results to the first "limit" (number).
````

### md2

`md2(anObject) : String`

````text
Will return of the MD2 in hexadecimal format for a given anObject.
For files you can provide a file stream: var s = io.readFileStream(getOpenAFJar()); md2(s); s.close()
````

### md5

`md5(anObject) : String`

````text
Will return of the MD5 in hexadecimal format for a given anObject.
For files you can provide a file stream: var s = io.readFileStream(getOpenAFJar()); md5(s); s.close()
````

### merge

`merge(anObjectA, anObjectB) : aMergedObject`

````text
Merges a JavaScript object A with a JavaScript object B a returns the result as a new object.
````

### newFn

`newFn() : Function`

````text
Builds a new Function handling any debug needs if necessary.
````

### newJavaArray

`newJavaArray(aJavaClass, aSize) : JavaArrayClass`

Creates a new Java Array object for the `aJavaClass` type for a provided `aSize`.

Examples:

```javascript
newJavaArray(java.lang.String, 5);
newJavaArray(java.lang.Integer.TYPE, 2);
```

### now

`now() : Number`

````text
Will return the current system time in milliseconds.
````

### nowE

`nowE() : Number`

````text
Returns the current epoch time in seconds.
````

### nowNano

`nowNano() : Number`

````text
Will return the current system time in nanoseconds.
````

### nowNanoE

`nowNanoE() : Number`

````text
Returns the current epoch time in nanoseconds.
````

### nowTZ

`nowTZ() : Number`

````text
Returns the same as now() but adjusted with the local timezone offset.
````

### nowUTC

`nowUTC() : Number`

````text
Will return the current system time in milliseconds.
````

### oJob

`oJob(aFile, args, aId, aOptionsMap, shouldReturn)`

````text
Shortcut for oJobRunFile return the result on the variable __pm. Keep in mind that it doesn't support concurrency. If shouldReturn is true it will return the result (from ow.oJob.output if used) of the job instead of the __pm variable.
````

### oJobRun

`oJobRun(aJson, args, aId)`

````text
Runs a oJob from aJson definition with the provided args (arguments). Optionally you can provide aId to segment these specific jobs.
````

### oJobRunFile

`oJobRunFile(aFile, args, aId, aOptionsMap, isSubJob)`

````text
Runs a oJob aFile with the provided args (arguments). Optionally you can provide aId to segment these specific jobs.
````

### oJobRunFileAsync

`oJobRunFileAsync(aFile, args, aId, aOptionsMap, isSubJob) : oPromise`

````text
Runs a oJob aFile async with the provided args (arguments). Optionally you can provide aId to segment these specific jobs. Returns the corresponding promise.
````

### oJobRunJob

`oJobRunJob(aJob, args, aId, waitForFinish) : boolean`

````text
Shortcut for ow.oJob.runJob. Please see help for ow.oJob.runJob. Optionally you can provide aId to segment this specific job. If aJob is a string it will try to retrieve the job from the jobs channel. Returns true if the job executed or false otherwise (e.g. failed deps).
````

### oJobRunJobAsync

`oJobRunJobAsync(aJob, args, aId) : oPromise`

````text
Creates an oPromise to run the same arguments for oJobRunJob thus executing the job async. Returns the generate oPromise.
````

### oPack

`oPack(aParameters)`

Tries to execute oPack with `aParameters` string. These string is equivalent to the opack command-line commands.
`aParameters` = "help" will, for example, print all the help information.

### oPromise

`oPromise(aFunction, aRejFunction, useVirtualThreads) : oPromise`

````text
Custom Promise-like implementation. If you provide aFunction, this aFunction will be executed async in a thread and oPromise object will be immediatelly returned. Optionally this aFunction can receive a resolve and reject functions for to you use inside aFunction to provide a result with resolve(aResult) or an exception with reject(aReason). If you don't call theses functions the returned value will be used for resolve or any exception thrown will be use for reject. You can use the "then" method to add more aFunction that will execute once the previous as executed successfully (in a stack fashion). The return/resolve value from the  previous function will be passed as the value for the second. You can use the "catch" method to add aFunction that will receive a string or exception for any exception thrown with the reject functions. You can also provide a aRejFunction that works like a "catch" method as previously described.  Optionally if useVirtualThreads is true, the aFunction will be executed in a virtual thread, otherwise it will be executed in a normal thread.
````

### oPromise.all

`oPromise.all(anArray) : oPromise`

````text
Returns an oPromise that will be resolved when all oPromise part of the anArray are fullfiled. If any of the oPromises fails/rejects the returned oPromise will also be rejected/fail.
````

### oPromise.catch

`oPromise.catch(onReject) : oPromise`

````text
Adds onRejected to the current oPromise stack to execute if the previous function was rejected and receives the reason as parameter.
````

### oPromise.race

`oPromise.race(anArray) : oPromise`

````text
Returns an oPromise that will be resolved when any oPromise part of the anArray is fullfiled. If any of the oPromises fails/rejects the returned oPromise will also be rejected/fail.
````

### oPromise.then

`oPromise.then(onFulfilled, onRejected) : oPromise`

````text
Adds onFulfilled to the current oPromise stack to execute if the previous function was resolved successfully and receives the resolve/return value as parameter. Also adds onRejected to the current oPromise stack to execute if the previous function was rejected and receives the reason as parameter.
````

### objOrStr

`objOrStr(aObj, aStr) : String`

````text
Given aObj (a map or an array) will try to assess if aStr is an aObj key (using $$.get). If yes, it will return the corresponding aObj value otherwise it will return aStr.
````

### opackExec

`opackExec(aPackageName)`

````text
Tries to execute the provided opack aPackageName.
````

### openInBrowser

`openInBrowser(anURL) : Boolean`

````text
Tries to open anURL on the current OS desktop browser. Returns false if it's unable to open the OS desktop browser for some reason.
````

### ow.loadAI

`ow.loadAI()`

````text
Loads OpenWrap AI functionality.
````

### ow.loadCh

`ow.loadCh()`

````text
Loads OpenWrap channels functionality.
````

### ow.loadDebug

`ow.loadDebug()`

````text
Loads OpenWrap debug functionality.
````

### ow.loadDesktop

`ow.loadDesktop(aOptions) : ow.desktop`

````text
Loads the optional provider-independent HTML desktop facade. JavaFX support is supplied by the plugin-DesktopJavaFX oPack. Toolkit initialization is deferred until the first operation.
````

### ow.loadDev

`ow.loadDev()`

````text
Loads OpenWrap dev functionality. Basically functions being tested.
````

### ow.loadFormat

`ow.loadFormat()`

````text
Loads OpenWrap format functionality. Basically functions to help with the formatting of strings, numbers, dates, etc...
````

### ow.loadInstrumentation

`ow.loadInstrumentation()`

````text
Loads the opt-in generic instrumentation module. Loading does not enable capture.
````

### ow.loadJava

`ow.loadJava()`

````text
Loads OpenWrap Java functionality.
````

### ow.loadMetrics

`ow.loadMetrics()`

````text
Loads OpenWrap Metrics functionality. Basically functions to wrap access to server functionality.
````

### ow.loadNet

`ow.loadNet()`

````text
Loads OpenWrap net functionality. Basically functions for net.
````

### ow.loadOBook

`ow.loadOBook()`

````text
Loads OpenWrap oBook functionality.
````

### ow.loadOJob

`ow.loadOJob()`

````text
Loads OpenWrap oJob functionality.
````

### ow.loadObj

`ow.loadObj()`

````text
Loads OpenWrap object functionality.
````

### ow.loadPython

`ow.loadPython()`

````text
Loads OpenWrap Python functionality.
````

### ow.loadScreen

`ow.loadScreen(aOptions) : ow.screen`

````text
Loads the OpenWrap Screen TUI and terminal styling/layout library. Provides full UTF-8/Unicode measurement, 16/256/truecolor ANSI and hex/RGB styling, bold/italic/underline/faint/strikethrough/reverse attributes, left/center/right alignment, spacing, box-drawing panels, and interactive terminal views (integrating with ow.desktop TUI).
````

### ow.loadSec

`ow.loadSec()`

````text
Loads OpenWrap sec functionality. Basically functions for sec.
````

### ow.loadServer

`ow.loadServer()`

````text
Loads OpenWrap Server functionality. Basically functions to wrap access to server functionality.
````

### ow.loadTemplate

`ow.loadTemplate()`

````text
Loads OpenWrap template functionality. Basically functions to wrap access to Handlebars functionality.
````

### ow.loadTest

`ow.loadTest()`

````text
Loads OpenWrap test functionality. Basically functions to unit test other functionality.
````

### pForEach

`pForEach(anArray, aFn, aErrFn, aUseSeq, aTimeoutMs, options) : Array`

Given `anArray`, divides it in subsets for processing in a specific number of threads. In each thread `aFn(aValue, index)`
will be executed for each value in sequence. The results of each `aFn` will be returned in the same order as the original
array. If an error occurs during the execution of `aFn`, `aErrFn` will be called with the error. If `aUseSeq` is true the
sequential execution will be forced. `aTimeoutMs`, if provided, overrides `__flags.PFOREACH.wait_timeout_ms` as the overall
deadline, in milliseconds, from parallel dispatch through queue-pressure and completion waits. If neither is a positive
number (the default) pForEach waits for all partitions to complete.
Sequential callbacks remain synchronous and are not interrupted by this deadline. On timeout the still-pending partitions
(and their pool worker threads) are cancelled, `aErrFn` is called with a "pForEach: N of M partitions timed out"
diagnostic and whatever results were collected so far are returned (missing entries come back as arrays of __, so the
returned array keeps the same length and order as `anArray`).

Example:

```javascript
var res = pForEach(thingsToProcess,
  function(aValue, index) {
    return processValue(aValue)
  },
  function(e) {
    printErr(e)
  }
)
```

### parallel

`parallel(aFunction, numThreads, aAggFunction, aControlMap) : Object`

````text
Executes a function in a specific number of threads (each function will receive a corresponding uuid).  The returned result of each function execution is kept in an array. If no aAggFunction is provided this array will be returned, otherwise the array will be passed to the aAggFunction for processing and the corresponding result of aAggFunction will be returned. If no numThreads is provided, the number of threads will be automatically determined. Optionally you can provide a empty map as aControlMap that it will be filled with aControlMap.__threads with the  threads object, the aControlMap.__numThreads for the number of threads in use and a thread __uuid list.
````

### parallel4Array

`parallel4Array(anArray, aFunction, numThreads, aControlMap, options) : Object`

Given `anArray`, divides it in subsets for processing in a specific number of threads. In each thread `aFunction(aValue)`
will be executed for each value in sequence. An array with all the `aFunction` results will be returned. If no `numThreads` is
provided, the number of threads will be automatically determined. Optionally you can provide a empty map as `aControlMap`
that it will be filled with `aControlMap.__threads` with the threads object, the `aControlMap.__numThreads` for the number of
threads in use and a thread `__uuid` list. Example:

```javascript
var count = 0;
var ctrl = {};
var res = parallel4Array(thingsToProcess,
   function(aValue) {
      ctrl.__threads.sync(function() { count++; }) // Sync access to a shared variable
      return processValue(aValue);
   },
   undefined,
   ctrl
);
```

### parallelArray

`parallelArray(anArray, aReduceFunction, initValue, aAggFunction, numThreads, aControlMap) : Object`

````text
An installed GPU opack may handle calls without an explicit thread count/control map. Set OAF_PFOREACH_GPU=false, __flags.PFOREACH.useGPU=false or options.useGPU=false to bypass it. Given anArray, divides it in subsets for processing in a specific number of threads. In each thread aReduceFunction(pr, cv, i, arr), where pr = previous result, cv = current value, i = index and arr = array subset, will be executed for each value in sequence. The pr value for the first execution on each thread will have the value initValue if provided. The returned result, in each thread, will be placed into an array. If aAggFunction is defined, the resulting array will be passed to the aAggFunction for processing and the corresponding result of aAggFunction will be returned. If no numThreads is provided, the number of threads will be  automatically determined. Optionally you can provide a empty map as aControlMap that it will be filled with aControlMap.__threads with the threads object, the aControlMap.__numThreads for the number of threads in use and a thread __uuid list.
````

### persistDBInMem

`persistDBInMem(aDB, aFilename) : Array`

````text
Tries to persist a in-memory database, aDB object, previously created by the function createDBInMem into a SQL aFilename. This can later be used to load again using the loadDBInMem function.
````

### pidCheck

`pidCheck(aPid) : Boolean`

````text
Verifies if aPid is running (returning true) or not (returning false).
````

### pidCheckIn

`pidCheckIn(aFilename) : boolean`

````text
Uses the contents of aFilename to determine if there is an existing process running with the pid  recorded on the file. If it's running it will return false, if not it will return true and record the current pid on the aFilename. The function pidCheckOut will be added as a hook to run on the  end of the current process.
````

### pidCheckOut

`pidCheckOut(aFilename) : boolean`

````text
Removes the pid information from aFilename and deletes the file if possible.  If successful returns true, if not returns false.
````

### pidKill

`pidKill(aPidNumber, isForce) : boolean`

````text
Tries to terminate a process with aPidNumber. If successful it will return true otherwise it will return false. If necessary, a boolean true value on isForce, will force the termination of the process. When isForce is true, it will also attempt to kill any child processes of the target process.
````

### plugin

`plugin(aPlugin, aClass)`

````text
Provides a shortcut for the af.plugin function. It also provides a shortcut for plugins with the java package "openaf.plugins" (e.g. af.plugin("openaf.plugins.HTTP") is the same as plugin("HTTP")). In alternative you can provide plugin aClass if it's different from aPlugin.
````

### pods.declare

`pods.declare(aId, exports)`

````text
Declares a new module, aId, as the provided exports literal.
````

### pods.define

`pods.define(aId, aDepsArray, aFactoryFunction)`

````text
Defines a new module given aId, aDepsArray with depend id modules and a factory function.
````

### pods.require

`pods.require(aIds, aCallbackFunction)`

````text
Requires a module or a list of modules and all of its dependencies. Optionally you can provide aCallbackFunction to inject the required modules into.
````

### print

`print(aStr)`

Prints the `aStr` to the stdout (with a new line on the end) (example: `print("hello world!")`)

### printBars

`printBars(aFormatString, hSize, aMax, aMin, aIndicatorChar, aSpaceChar) : String`

Produces horizontal bars given `aFormatString`, a `hSize` (horizontal max size), `aMax` (the axis max value) and `aMin`
(the axis min value). The `aFormatString` should be composed of `<units> [<function[:color][:legend]> ...]`:

- The units can be: int, dec1, dec2, dec3, dec, bytes and si;
- Each function should return the corresponding current value (optionally it can be a number directly);
- Optionally each color should use any combinations similar to ansiColor (check 'help ansiColor');
- Optionally each legend, if used, will be included in a bottom legend;

### printChart

`printChart(aFormatString, hSize, vSize, aMax, aMin, dColor) : String`

Produces a line chart given `aFormatString`, a `hSize` (horizontal max size), a `vSize` (vertical max size), `aMax` (the axis max value) and `aMin`
(the axis min value). The `aFormatString` should be composed of `<dataset> <units> [<function[:color][:legend]> ...]`:

- The dataset should be an unique name (data can be cleaned with `ow.format.string.dataClean`);
- The units can be: int, dec1, dec2, dec3, dec4, dec, bytes and si;
- Each function should return the corresponding current value (optionally it can be a number directly);
- Optionally each color should use any combinations similar to ansiColor (check 'help ansiColor');
- Optionally each legend, if used, will be included in a bottom legend;

- If function "-min" it will overwrite the `aMin`
- If function "-max" it will overwrite the `aMax`
- If function "-hsize" it will overwrite the `hSize`
- If function "-vsize" it will overwrite the `vSize`

### printChartArray

`printChartArray(anArray, aType, hSize, vSize, aMax, aMin, options) : String`

Produces and returns a one-shot terminal line chart directly from `anArray`, without calling functions or keeping a named
dataset between calls. Use an array of numbers for one series or an array of arrays of numbers for multiple series. Series
can have different lengths. `aType` controls the y-axis label format and can be: int, dec1, dec2, dec3, dec4, dec, bytes or si.
`hSize` and `vSize` set the chart width and height; when omitted in a console they default to the terminal width and terminal
height minus 5 respectively. `aMax` and `aMin` optionally fix the y-axis bounds; omitted bounds are calculated from the values.

`options` is passed to `ow.format.string.lineChart` and can include:

- `colors` (array) ANSI color specification for each series. Colors are assigned by series order and repeat if fewer colors are provided;
- `label` (boolean) Include y-axis labels (default true);
- `dColor` (string) ANSI color specification for the labels, axes and other default chart elements;
- `offset` (number) Horizontal offset reserved for the y-axis (default 2);
- `padding` (string) String prepended to each chart line (default "");
- `symbols` (array) Ten characters replacing the default line drawing symbols;

Each color accepts the same values and comma-separated combinations as ansiColor (check 'help ansiColor'), including
named foreground/background colors (for example GREEN, FG_CYAN or BG_BLUE), attributes (for example BOLD,GREEN),
256-color forms such as FG(208) or BG(236), and true-color forms such as RGB(80,160,255), FG_RGB(80,160,255) or
BG_RGB(20,20,20). ANSI colors are shown when terminal color support is enabled.

Examples:

```javascript
print(printChartArray([1, 4, 2, 5, 3], "int", 40, 10, 5, 0, { colors: ["GREEN"] }));
print(printChartArray([[1, 2, 3], [3, 2, 1]], "dec1", 40, 10, __, __, { colors: ["BOLD,CYAN", "FG(208)"] }));
```

### printErr

`printErr(aStr)`

Prints the `aStr` to the stderr (with a new line on the end) (example: `printErr("Hupps!! A problem!")`)

### printErrnl

`printErrnl(aStr)`

Prints the `aStr` to the stderr (without adding a new line on the end) (example: `printErrnl("Hupps!! A problem!")`)

### printMap

`printMap(aMap, aWidth, aTheme, useAnsi) : String`

````text
Returns a ASCII map representation of aMap optionally with a give aWidth, aTheme and/or useAnsi boolean. aTheme can be "utf" or "plain" depending on the terminal capabilities.
````

### printTable

`printTable(anArrayOfEntries, aWidthLimit, displayCount, useAnsi, aTheme, aBgColor, wordWrap, useRowSep, bandRows) : String`

````text
Returns a ASCII table representation of anArrayOfEntries where each entry is a Map with the same keys. Optionally you can specify aWidthLimit, useAnsi, bandRows and/or aBgColor. If you want to include a count of rows just use displayCount = true. If useAnsi = true you can provide a theme (e.g. "utf", "plain" or "borderless"). The "borderless" theme uses two-space column gaps, heavy Unicode header rules and optional light rules between records (useRowSep), including wrapped records
````

### printTree

`printTree(aObj, aWidth, aOptions) : String`

````text
Given aObj(ect) will return a tree with the object elements. Optionaly you can specificy aWidth and/or aOptions: noansi (boolean) no ansi character sequences, curved (boolean) for UTF curved characters, wordWrap (boolean) to wrap long string values, compact (boolean) to compact tree lines, fullKeySize (boolean) to pad the each entry key, fullValSize (boolean) to pad the entire key and value and withValues (boolean) to include or not each key values, tableArrays (boolean) to render arrays composed only of non-map/array values (or maps whose fields are all non-map/array values) as a printTable instead of nested tree branches
````

### printTreeOrS

`printTreeOrS(aObj, aWidth, aOptions) : String`

````text
Tries to use printTree with the provided arguments. In case printTree throws an exception (like insufficient width) if will fallback to colorify or stringify (if the noansi option is true).
````

### printnl

`printnl(aStr)`

Prints the `aStr` to the stdout (without adding a new line on the end) (example: `printnl("hello world!")`)

### processExpr

`processExpr(aSeparator, ignoreCase, aSource) : Map`

````text
Will access the current contents of the OpenAF -e argument (if a different aSource is not defined) looking for pairs of key values in the form "a=5;b=1;c=xpto\\;" and will produce a Map with { "a": 5, "b": 1, "c": "xpto;" }. If no aSeparator is provided ';' will be assumed. __pmIn values will be also included. If ignoreCase = true all keys will be lower cased.
````

### quickSort

`quickSort(items, aCompareFunction) : Array`

````text
Performs a quick sort algorithm on the items array provided. Optionally aCompareFunction can be provided. The sorted array will be returned.
````

### range

`range(aCount, aStart, aStep) : Array`

````text
Generates an array with aCount of numbers starting at 1. Optionally you can provide a different aStart number and/or aStep increment.
````

### repeat

`repeat(nTimes, aStr) : String`

````text
Will build a string composed of aStr repeated nTimes.
````

### require

`require(aScript) : Object`

````text
Will try to load aScript from the directories specified in the loadRequire function (by default all opack directories plus the current working directory). Returns the exports object manipulated in aScript (note: results are cached)
````

### requireCompiled

`requireCompiled(aScript, dontCompile, dontLoad) : Object`

````text
Loads aScript, through require, previously compile or it will be compiled if (dontCompile is not true). IF dontLoad = true the module exports won't be returned.
````

### restartOpenAF

`restartOpenAF(aCommandLineArray, preCommandLineArray)`

````text
Terminates the current OpenAF execution and tries to start a new with the same command line, if aCommandLineArray is not provided. If aCommandLineArray is provided each array element will be use sequentially to build the command line to start a new OpenAF instance.  preCommandLineArray can be used to provide java arguments if defined.
````

### saveHelp

`saveHelp(aPath, aMapOfFiles)`

````text
Given aMapOfFiles mapping subject ids to JavaScript or Java source filenames, each file will be processed for ODoc XML tags and the corresponding ODoc database will be generated on the  provided aPath suitable for offline use.
````

### saveHelpWeb

`saveHelpWeb(aPath, aMapOfFiles)`

````text
Given aMapOfFiles mapping subject ids to JavaScript or Java source filenames, each file will be processed for ODoc XML tags and the corresponding ODoc database will be generated on the  provided aPath suitable for online use.
````

### searchArray

`searchArray(anArray, aPartialMap, useRegEx, ignoreCase, useParallel) : Array`

````text
Shortcut to ow.obj.searchArray.
````

### searchHelp

`searchHelp(aTerm, aPath, anArrayOfIds) : Array`

````text
Searches the OpenAF ODoc help system for a specific term. Optionally you can provide a path of where to  search for ODoc help files. A unique result returns an array with one map containing id, key, fullkey and raw text, plus format for explicitly marked entries. Ambiguous results contain id and key only. Matches prefer case-sensitive exact keys, then case-insensitive exact keys, then substrings. Returns an empty array when nothing is found. Optionally restrict by anArrayOfIds.
````

### searchKeys

`searchKeys(aObject, aSearchKey, useCase, actFunc) : Map`

````text
Traverses aObject looking for key matches, ignoring case if useCase is true, of the regular expression aSearchKey. Each element found is added to the returned Map. The element key will represent the path from aObject to it. Tip: The actFunc  can use ow.obj.setPath to replace a value: "(key, value, path) => { ow.obj.setPath(aObject, path + '.' + key, replaceValue); }"
````

### searchValues

`searchValues(aObject, aSearchValue, useCase, actFunc) : Map`

````text
Traverse aObject looking for value matches, ignoring case if useCase is true, of the regular expression aSearchKey.  Each value found is added to the returned Map linked to the path representation of where it was found. Optionally you can provide an actFunc that receives the key, value and path. Tip: The actFunc can use ow.obj.setPath to  replace a value: "(key, value, path) => { ow.obj.setPath(aObject, path + '.' + key, replaceValue); }"
````

### setInterval

`setInterval(aFunction, aPeriod) : String`

````text
Tries to execute aFunction every aPeriod milliseconds. Returns an id that can be used to clear the interval with clearInterval. Note: this function uses Threads plugin, so it will execute aFunction in a different thread and it won't block the main thread. Also, do note that the aFunction execution time is not included in the aPeriod, so if aFunction takes 2 seconds to execute and aPeriod is 5 seconds, the next execution will be 5 seconds after aFunction finishes, so it will be 7 seconds after the previous execution start.
````

### setLog

`setLog(aMap)`

Sets the current log output settings:

- `off` (boolean) Turns off output to stdout/stderr
- `offInfo` (boolean) Turns off output of INFO
- `offError` (boolean) Turns off output of ERROR
- `offWarn` (boolean) Turns off output of WARN
- `dateFormat` (string) `ow.format.fromDate` format for date
- `dateTZ` (string) Time zone to use with `ow.format.fromDate`
- `separator` (string) String to use as separator
- `async` (boolean) Run in async mode
- `profile` (boolean) Gathers memory and system load stats
- `format` (string) Sets the format to output logs (e.g. json, slon, human)

### setOfflineHelp

`setOfflineHelp(aBoolean)`

````text
Forces help (odoc) to be retrieved locally (if aBoolean is true) or reestablishes the normal behaviour of loading local documentation with online fallback and background refresh (if aBoolean is false)
````

### setTimeout

`setTimeout(aFunction, aPeriod)`

Tries to execute `aFunction` after `aPeriod` milliseconds. Note: this function will block the
main thread, so use it with caution. If you need to execute `aFunction` in a different thread and avoid blocking the main thread, please use setInterval with a clearInterval after the first execution.

Example:

```javascript
setTimeout(() => { print("Hello after 2 seconds"); }, 2000);

// or using setInterval to avoid blocking the main thread
var id = setInterval(() => { print("Hello after 2 seconds"); clearInterval(id); }, 2000);
```

### sh

`sh(commandArguments, aStdIn, aTimeout, shouldInheritIO, aDirectory, returnMap, callbackFunc, anEncoding, dontWait, envsMap, exitCallback) : String`

Executes `commandArguments` (a string or an array of strings) through the operating system shell as a shortcut for `AF.sh`.

- `aStdIn`: optional standard input.
- `aTimeout`: optional execution timeout.
- `shouldInheritIO`: when true, inherits stdout, stderr and stdin from OpenAF. When false or undefined, returns the command's stdout.
- `aDirectory`: optional working directory.
- `envsMap`: a map of strings that replaces the environment variables.
- `returnMap`: when true, returns a map with `stdout`, `stderr` and `exitcode`.

Check `__exitcode` and `__stderr` for the command exit code and stderr output.

When `shouldInheritIO` is false or undefined, `callbackFunc` can receive an output stream, an error stream and an input stream (see `af.sh` for an example). With a callback, stdout and stderr are unavailable in the returned map.

An optional `exitCallback` receives the exit code.

### sha1

`sha1(anObject) : String`

````text
Will return of the SHA-1 in hexadecimal format for a given anObject.
For files you can provide a file stream: var s = io.readFileStream(getOpenAFJar()); sha1(s); s.close()
````

### sha256

`sha256(anObject) : String`

````text
Will return of the SHA-256 in hexadecimal format for a given anObject.
For files you can provide a file stream: var s = io.readFileStream(getOpenAFJar()); sha256(s); s.close()
````

### sha384

`sha384(anObject) : String`

````text
Will return of the SHA-384 in hexadecimal format for a given anObject.
For files you can provide a file stream: var s = io.readFileStream(getOpenAFJar()); sha384(s); s.close()
````

### sha512

`sha512(anObject) : String`

````text
Will return of the SHA-512 in hexadecimal format for a given anObject.
For files you can provide a file stream: var s = io.readFileStream(getOpenAFJar()); sha512(s); s.close()
````

### showH2Console

`showH2Console() : Console`

````text
Instantiates and returns a H2 Console object openning a browser (if possible) to interact with the H2 Console. With  the returned object you can later invoke .shutdown() or unload it from the console. Invoking a second time will result in a port bind error since it the first instance wasn't shutdown.
````

### sleep

`sleep(millis, shouldCheck)`

````text
Shortcut for af.sleep function. Will pause execution for a given period of time expressed in milliseconds. If shouldCheck is true it will enforce checking if the time has really passed or not.
````

### sortMapKeys

`sortMapKeys(aMap, moreLevels) : Map`

````text
Tries to sort the first level map keys returning the rewritten map.  If moreLevels=true it will try to recursively map sub maps.
````

### splitArray

`splitArray(anArray, numberOfParts) : Array`

````text
Returns the result of the split of anArray into equals numberOfParts (when possible). If numberOfParts is not provided the current result of getNumberOfCores() will be used.
````

### splitBySepWithEnc

`splitBySepWithEnc(text, separator, enclosures, includeEnclosures) : array`

````text
Given a text, a separator, a list of enclosures and a flag includeEnclosures, this function will split the text by the separator while ignoring the separator inside the enclosures. If includeEnclosures is true, the enclosures will be included in the result. If includeEnclosures is false, the enclosures will be removed from the result.
````

### splitBySeparator

`splitBySeparator(aString, aSeparator) : Array`

Splits `aString` using `aSeparator`. Escaped separators are ignored. For example, if `aSeparator` is `;` and
`aString` is `abc\\;def;123`, only the second `;` is treated as a separator.

### splitKVBySeparator

`splitKVBySeparator(aString, aOptions) : Map`

Given `aString` with multiple key/value entries will return a map with the same. Optionally you can provide `aOptions`:

- `sep`: the key/value entries separator (defaults to " ")
- `ksep`: the key separator from a value (defaults to "=")
- `esc`: the escape character (defaults to `"\\"`)
- `qto`: the quote character (defaults to `"\""`)
- `nul`: the null representation (defaults to null)

### sprint

`sprint(aStr)`

"Stringifies" and prints the `aStr` to the stdout (with a new line on the end) (example: `sprint("hello world!")`)

### sprintErr

`sprintErr(aStr)`

"Stringifies" and prints the `aStr` to the stderr (with a new line on the end) (example: `sprintErr("Hupps!! A problem!")`)

### sprintErrnl

`sprintErrnl(aStr)`

"Stringifies" and prints the `aStr` to the stderr (without adding a new line on the end) (example: `sprintErrnl("Hupps!! A problem!")`)

### sprintnl

`sprintnl(aStr)`

"Stringifies" and prints the `aStr` to the stdout (without adding a new line on the end) (example: `sprintnl("hello world!")`)

### startLog

`startLog(externalLogging, hkItems)`

````text
Starts collecting log messages logged with log* functions. See stopLog() and dumpLog(). You can also specify externalLogging, a custom channel subscribe function and a different number of hkItems (housekeeping items) from the default 100 (if -1 it won't delete items).
````

### stopLog

`stopLog()`

````text
Will stop collecting log messages and will reset everything. User dumpLog() before stopping if you intend to keep the recorded log messages.
````

### stopOpenAFAndRun

`stopOpenAFAndRun(aCommandLineArray, addCommand, redirectOutput, noStop)`

````text
Terminates the current OpenAF execution while trying to execute the commands on the aCommandLineArray. Optionally you can use addCommand boolean flag (true) to allow for shell like commands on the current operating system. If redirectOutput is false (default), output is inherited from the parent process. Set redirectOutput to true to redirect output to /dev/null (or NUL on Windows). If noStop is true the current OpenAF execution will not be terminated. To restart OpenAF please use the restartOpenAF function.
````

### stringify

`stringify(anObject, replacer, space) : String`

````text
Converts anObject into a string representation of the same. This is equivalent to the JSON.stringify function. If space isn't defined a "  " (2 spaces) is assumed as the default value. Reverts to the beautifier function if it isn't possible to apply stringify to the current object.  To see more info on the remaining parameters please check https://developer.mozilla.org/en/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify
````

### sync

`sync(aFunction, anObject)`

````text
Will ensure that aFunction is synchronized, in multi-threaded scripts. Optionally you can provide anObject to synchronized upon.
````

### syncFn

`syncFn(aFunction, anObject) : Object`

````text
Will ensure that aFunction is synchronized, in multi-threaded scripts (alternative to sync). Optionally you can provide anObject to synchronized upon. Returns the result of aFunction.
````

### templify

`templify(aTemplateString, someData) : String`

Using Handlebars and the functionality provided in `ow.template`, will use the `aTemplateString` as a Handlebars template
and return the parsed output. Optionally you can provide `someData` as data for the Handlebars template
otherwise the current scope will be used.

Example:

```javascript
var someText = "Hello World!";
var retText = templify("Hi, {{someText}}"); // Hi, Hello World!
```

### threadBox

`threadBox(aExecFunction, aTimeout, aStopFunction)`

````text
Tries to execute aExecFunction inside a thread. If aTimeout is defined the thread will be terminated if it's still executing after aTimeout. If aStopFunction is defined  it will receive, as argument, a boolean indicating if the thread has stopped (true). If this function returns true the thread execution will be terminated, if false will continue.
Note: see threadBoxCtrlC as aStopFunction to stop executing on Ctrl-C
````

### threadBoxCtrlC

`threadBoxCtrlC() : Boolean`

````text
Meant to be use as a stopFunction for threadBox will return true if Ctrl-C is detected and false otherwise. If the current terminal can't support ANSI if will default to false.
````

### tlog

`tlog(msg, someData, formatOptions)`

````text
Outputs to the current stdout a line composed of the current date, indication of INFO and the provided msg using the templify function. Optionally you can provide also someData and you can provide a formatOptions map for overriding the defaults from setLog. Note: you can use startLog, stopLog and dumpLog to keep an internal record of theses messages.
````

### tlogErr

`tlogErr(msg, someData, formatOptions)`

````text
Outputs to the current stderr a line composed of the current date, indication of ERROR and the provided msg using the templify function. Optionally you can provide a formatOptions map for overriding the defaults from setLog.  Optinionally you can provide also someData.
````

### tlogWarn

`tlogWarn(msg, someData, formatOptions)`

````text
Outputs to the current warning in a line composed of the current date, indication of WARN and the provided msg using the templify function. Optionally you can provide a formatOptions map for overriding the defaults from setLog.  Optinionally you can provide also someData.
````

### tlognl

`tlognl(msg, someData, formatOptions)`

````text
Outputs to the current stdout, without a new line, a sentence composed of the current date, indication of INFO and the provided msg using the templify function. Optionally you can provide a formatOptions map for overriding the defaults from setLog. Optinionally you can provide also someData.
````

### toBoolean

`toBoolean(aObj) : Boolean`

````text
Tries to convert aObj (String, Number or Boolean) into a boolean value
````

### toCSV

`toCSV(anArray) : CSV`

````text
Converts a given javascript anArray into a CSV object instance.
````

### toEncoding

`toEncoding(aString, anEncoding) : String`

````text
Converts the provided aString to a different anEncoding (by default UTF-8).
````

### tprint

`tprint(aTemplateString, someData)`

Using Handlebars and the functionality provided in `ow.template`, will use the `aTemplateString` as a Handlebars template
and print the parsed output. Optionally you can provide `someData` as data for the Handlebars template
otherwise the current scope will be used.

Example:

```javascript
var someText = "Hello World!";
tprint("Hi, {{someText}}"); // Hi, Hello World!
```

### tprintErr

`tprintErr(aTemplateString, someData)`

Using Handlebars and the functionality provided in `ow.template`, will use the `aTemplateString` as a Handlebars template
and print, to the stderr, the parsed output. Optionally you can provide `someData` as data for the Handlebars template
otherwise the current scope will be used.

Example:

```javascript
var someText = "Hello World!";
tprintErr("Hi, {{someText}}"); // Hi, Hello World!
```

### tprintErrnl

`tprintErrnl(aTemplateString, someData)`

Using Handlebars and the functionality provided in `ow.template`, will use the `aTemplateString` as a Handlebars template
and print, to the stderr without new line, the parsed output. Optionally you can provide `someData` as data for the Handlebars template
otherwise the current scope will be used.

Example:

```javascript
var someText = "Hello World!";
tprintErrnl("Hi, {{someText}}"); // Hi, Hello World!
```

### tprintln

`tprintln(aTemplateString, someData)`

Using Handlebars and the functionality provided in `ow.template`, will use the `aTemplateString` as a Handlebars template
and print, without a new line, the parsed output. Optionally you can provide `someData` as data for the Handlebars template
otherwise the current scope will be used.

Example:

```javascript
var someText = "Hello World!";
tprintln("Hi, {{someText}}"); // Hi, Hello World!
```

### traverse

`traverse(aObject, aFunction) : Map`

````text
Traverses aObject executing aFunction for every single element. The aFunction will receive the arguments: aKey, aValue, aPath, aObject.
````

### uncompress

`uncompress(aResultOfTheCompressFunction) : Object`

````text
Uncompresses a JSON object, compressed by using the compress function, into a JSON object.
````

### uniqArray

`uniqArray(anArray) : Array`

````text
Returns anArray with no duplicates entries (including duplicate maps).
````

### utf8

`utf8(aString) : String`

````text
Converts the provided aString into UTF-8 encoding.
````

### visibleLength

`visibleLength(aString) : Number`

````text
More complete af.visibleLength function
````

### watch

`watch(waitFor, aCommand, beautifyFlag, noPrint)`

````text
Executes javascript aCommand provided every waitFor periods of time (expressed in ms). The screen will be cleared and the execution will repeat indefinitely until the 'q' key is pressed.  Optionally a beautifyFlag can be provided to execute the beautifier function on the aCommand result.
````

### wedoDate

`wedoDate(year, month, day, hour, minute, second, ms) : Map`

````text
Builds and returns a wedoDate JSON object given either a year, a month, a day, a hour, a minute, a second and ms or a Date object.
````

### yprint

`yprint(aObj, multidoc, sanitize, shouldColor)`

````text
Prints aObj in YAML. If multiDoc = true and aJson is an array the output will be multi-document. If sanitize = true all Java objects will be converted to avoid parsing errors.
````

### yprintErr

`yprintErr(aObj, multidoc)`

````text
Prints aObj in YAML to stderr. If multiDoc = true and aJson is an array the output will be multi-document.
````
{% endraw %}
