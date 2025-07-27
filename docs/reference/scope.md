---
layout: default
title: scope
parent: Reference
grand_parent: OpenAF docs
---


## scope

### $$from 

__$$from : Array__

````
Shortcut for the JLinq library for easy query and access to arrays/objects. To see all the available options please refer to http://hugoware.net/Projects/jlinq and the list of available functions by executing, in the openaf-console: "desc $$from([])".
````
### $a2m

__$a2m(aDef, aArray) : Array__

````
Tries to convert aArray into a map using the aDef array of keys for the map keys' value assignment in the output map. Example:

$a2m(['a', 'b', 'c'], [1, 2, 3])    // { a: 1, b: 2, c: 3 }


````
### $a4m

__$a4m(anArray, aKey, dontRemove) : Array__

````
Tries to create a map of maps from the provided anArrays. Optionally if aKey is provided it will be used to create the map keys (otherwise will fallback to "row[number]"). And can also optionally indicate by dontRemove = true that aKey shouldn't be removed from each map. 
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


````
### $atomic

__$atomic(aInitValue, aType) : Object__

````
Creates an atomic object of aType (defaults to long) to be get/set atomically on a multithreading script initialized with aInitValue. aType can be "int", "long" and "boolean". Each with different methods:

   int.dec          - Decrement an integer
   int.inc          - Increment an integer
   int.get          - Get the current integer
   int.getSet(n)    - Get and Set the current integer
   int.getAdd(n)    - Get and Add to the current integer
   int.setIf(t, n)  - Set the current integer to n if current value is t
   int.set          - Set the current integer

   long.dec         - Decrement an long
   long.inc         - Increment an long
   long.get         - Get the current long
   long.getSet(n)   - Get and Set the current long
   long.getAdd(n)   - Get and Add to the current long
   long.setIf(t, n) - Set the current long to n if current value is t
   long.set         - Set the current long

   boolean.get         - Get the current boolean
   boolean.set         - Set the current boolean
   boolean.getSet      - Get and Set the current boolean
   boolean.setIf(t, n) - Set the current boolean to n if current value is t


````
### $await

__$await(aName) : Object__

````
Wrapper around the Java wait/notify mechanism. For the provided name will returen an object with the following  functions wait (will block until a notify is invoked), notify (will notify and unblock one of the wait invocations),  notifyAll (will notify and unblock all wait invocations) and destroy existing references to aName.
````
### $bottleneck.destroy

__$bottleneck.destroy()__

````
Destroys any existing bottleneck definition.
````
### $bottleneck.exec

__$bottleneck.exec(args) : Object__

````
Creates a bottleneck aName to execute aFunction with the provided args. Returns what the function returns:

$bottleneck("myFunc", (a, b) => { ... return result; })
.maxExec(3)
.maxWait(5000)
.exec(2, 4);

$bottleneck("myFunc").exec(2, 2);


````
### $bottleneck.maxExec

__$bottleneck.maxExec(aMaxNumber) : Object__

````
Creates a bottleneck to a maximum concurrent execution number of aMaxNumber.
````
### $bottleneck.maxWait

__$bottleneck.maxWait(aMs) : Object__

````
Creates a bottleneck holding the function execution for a max period of aMs.
````
### $cache.byDefault

__$cache.byDefault(useDefault, aDefault) : Object__

````
Changes the behaviour of the cache to either use the default value (aDefault) if useDefault is true (launching the cache function in background) or try to use the previous value in the cache if useDefault  is false (if a previous value is not available the cache function will be called and the .get will wait for it).
````
### $cache.byPopularity

__$cache.byPopularity() : Object__

````
Changes the behaviour of the cache to use the most popular entries and prefer to discard the least popular ones  when the cache is full (maxSize is defined).
````
### $cache.ch

__$cache.ch(aChannelName) : Object__

````
Uses a pre-existing channel (e.g. aChannelName) as the cache channel.
````
### $cache.fn

__$cache.fn(aFunction) : Object__

````
Defines the aFunction use to get aKey. The returned object will be cached.
````
### $cache.get

__$cache.get(aKey) : Object__

````
Shortcut to use a cache channel. Returns an object that can be used like this:

$cache("numbers")
.ttl(30000)
.fn((aKey) => { ... return result; })
.create()

$cache("numbers").get(myKey);

$cache("numbers").destroy();


````
### $cache.inFile

__$cache.inFile(aFile) : Object__

````
Creates a mvs channel to hold the cache data in aFile. Note: don't use $cache.ch if you use this option.
````
### $cache.maxSize

__$cache.maxSize(aSize) : Object__

````
Establishes the max number of entries cached at any given point in time.
````
### $cache.ttl

__$cache.ttl(aTTL) : Object__

````
Defines the time-to-live (aTTL) to consider a cached result as valid.
````
### $ch

__$ch(aChannel)__

````
Please check more details with the help from ow.ch. The available methods are:

Channel basics:

- create(shouldCompress, aType, options)
- list()
- destroy()
- size()
- subscribe(aFunction, onlyFromNow, anId)
- unsubscribe(aId)
- forEach(aFunction)
- getAll()
- getKeys(fullInfo)
- getSortedKeys(fullInfo)
- set(aKey, aValue, aForcedTimestamp)
- setAll(keysArray, valuesArray, aForcedTimestamp)
- get(aKey)
- getSet(aMatch, aKey, aValue, aForcedTimestamp)
- unset(aKey, aForcedTimestamp)
- push(aKey, aValue)
- pop(aKey)
- shift(aKey)
- stopJobs()
- waitForJobs(aTimeout)
- getName()

Channel basic persistence:

- storeAdd(aFilename, anArrayOfKeys, shouldCompress)
- storeRestore(aFilename, anArrayOfKeys)

Inter-channel HTTP REST:

- expose(aLocalPortOrServer, aPath, aAuthFunc, aUnAuthFunc)
- peer(aLocalPortOrServer, aPath, aRemoteURL, aAuthFunc, aUnAuthFunc)
- unpeer(aRemoteURL)
- createRemote(aURL, aTimeout)
````
### $channels

__$channels(aChannel)__

````
Please check more details with the help from ow.ch. The available methods are:

Channel basics:

- create(shouldCompress, aType, options)
- list()
- destroy()
- size()
- subscribe(aFunction, onlyFromNow, anId)
- unsubscribe(aId)
- forEach(aFunction)
- getAll(fullInfo)
- getKeys(fullInfo)
- getSortedKeys(fullInfo)
- set(aKey, aValue, aForcedTimestamp)
- setAll(keysArray, valuesArray, aForcedTimestamp)
- unsetAll(keysArray, valuesArray, aForcedTimestamp)
- get(aKey)
- getSet(aMatch, aKey, aValue, aForcedTimestamp)
- unset(aKey, aForcedTimestamp)
- push(aKey, aValue)
- pop(aKey)
- shift(aKey)
- stopJobs()
- waitForJobs(aTimeout)
- getName()

Channel basic persistence:

- storeAdd(aFilename, anArrayOfKeys, shouldCompress, runSubscribersForAll)
- storeRestore(aFilename, anArrayOfKeys)

Inter-channel HTTP REST:

- expose(aLocalPortOrServer, aPath, aLogin, aPassword)
- peer(aLocalPortOrServer, aPath, aRemoteURL, aAuthFunc, aUnAuthFunc, aMaxTime, aMaxCount)
- unpeer(aRemoteURL)
- createRemote(aURL, aTimeout, aLogin, aPass)
````
### $csv

__$csv(aMap) : $csv__

````
Provides a shortcut to access CSV functionality. Optionally you can provide options through aMap.

Examples:
  $csv().fromInArray(anArray)
  $csv().fromInFile("test.csv").toOutArray()
  $csv().fromInFile("test.csv").toOutFn(m => print( af.toSLON(m) ))
  $csv().fromInString( $csv().fromInArray( io.listFiles(".").files ) ).toOutArray()
````
### $do

__$do(aFunction, aRejFunction) : oPromise__

````
Instantiates and returns a oPromise. If you provide aFunction, this aFunction will be executed async in a thread and oPromise object will be immediatelly returned. Optionally this aFunction can receive a resolve and reject functions for to you use inside aFunction to provide a result with resolve(aResult) or an exception with reject(aReason). If you don't call theses functions the returned value will be used for resolve or any exception thrown will be use for reject. You can use the "then" method to add more aFunction that will execute once the previous as executed successfully (in a stack fashion). The return/resolve value from the  previous function will be passed as the value for the second. You can use the "catch" method to add aFunction that will receive a string or exception for any exception thrown with the reject functions. You can also provide aRejFunction to work as a "catch" method as previously described before.
````
### $doA2B

__$doA2B(aAFunction, aBFunction, numberOfDoPromises, defaultTimeout, aErrorFunction, useVirtualThreads)__

````
Will call aAFunction with a function as argument that should be used to "send" values to aBFunction. aBFunction will be call asynchronously in individual $do up to the numberOfDoPromises limit. The defaultTimeout it 2500ms. If aErrorFunction is defined it will received any exceptions thrown from aBFunction with the corresponding arguments array. If useVirtualThreads is true it will use virtual threads to execute aBFunction. If useVirtualThreads is false (default) it will use the thread pool. Use virtual threads if you want to execute aBFunction without blocking the current thread (IO bound operations / high concurrency).
````
### $doAll

__$doAll(anArray) : oPromise__

````
Returns an oPromise that will be resolved when all oPromise part of the anArray are fullfiled. If any of the oPromises fails/rejects the returned oPromise will also be rejected/fail.
````
### $doFirst

__$doFirst(anArray) : oPromise__

````
Returns an oPromise that will be resolved when any oPromise part of the anArray is fullfiled. If any of the oPromises fails/rejects the returned oPromise will also be rejected/fail.
````
### $doV

__$doV(aFunction, aRejFunction) : oPromise__

````
Equivalent to $do but using virtual threads (if available) to execute the aFunction. This will allow the aFunction to be executed without blocking the current thread. If aFunction is not provided it will return a new oPromise that will be resolved when the first executor is added to it. If aRejFunction is provided it will be used as a "catch" method for the oPromise.
````
### $doWait

__$doWait(aPromise, aWaitTimeout) : oPromise__

````
Blocks until aPromise is fullfilled or rejected. Optionally you can specify aWaitTimeout between checks. Returns aPromise.
````
### $err

__$err(exception, rethrow, returnStr, code)__

````
Prints the exception stack trace and the code where it was thrown. If rethrow is true it will throw the exception again. If returnStr is true it will return the string instead of printing it.
````
### $f

__$f(aString, arg1, arg2, ...) : String__

````
Formats aString with arg1, arg2 and any other arguments provided using java.util.Formatter. The format is composed of "%[argument_index$][flags][width][.precision]conversion". Do note that javascript numbers are converted to java.lang.Float. If you need it to convert to Integer, Long, Double, Float and BigDecimal please use $ft. The javascript Date type will be converted to java Calendar. So possible values:

   argument_index: number
   flags         : '-' (left-justified); '#'; '+' (include sign); ' ' (leading space); '0' (zero-padded); ',' (separators); '(' (enclose negative values)
   conversion    : b/B (boolean), h/H (hash), s/S (string), "-" (left justify), c/C (character)

Examples:

   $f("Time %tT", new Date())
   $f("Date: %1$tm %1te, %1tY %1$tT", new Date())

   $f("%.2f", 1.9)
   $f("%10.2f", 1.9)


````
### $fetch

__$fetch(aURL, aOptions) : oPromise__

````
Tries to fetch aURL using the provided aOptions (a map with the following possible keys: method, body, headers, requestHeaders, downloadResume, connectionTimeout, uriQuery, urlEncode, login, pass, httpClient and retry). The method will return a promise that will resolve to a response object with the following methods: body, bodyUsed, headers, ok, status, json, bytes, blob and text. Example:

var response = $fetch("https://httpbin.org/post", { method: "POST", body: { a: 1, b: 2 }, headers: { "Content-Type": "application/json" } });
response.then(function(aResponse) { print(aResponse.status); });

The response object will have the following methods:

- body() : returns a Java InputStream with the response body
- bodyUsed : returns true if the body was already read
- headers : returns a map with the response headers
- ok : returns true if the response status is between 200 and 299
- status : returns the response status
- json() : returns the response body as a JSON object
- bytes() : returns the response body as a byte array
- blob() : returns the response body as a byte array
- text() : returns the response body as a string


````
### $flock.destroy

__$flock.destroy()__

````
Given aLockFile will destroy the provided lock entry.

   $flock(aLockFile).destroy()


````
### $flock.isLocalLocked

__$flock.isLocalLocked() : Boolean__

````
Given aLockFile will return true if locked in the current OpenAF instance otherwise false (see also isLocked).

   $flock(aLockFile).isLocalLocked()


````
### $flock.isLocked

__$flock.isLocked() : Boolean__

````
Given aLockFile will return true if locked in the current OpenAF instance or on the filesystem (by using $flock.tryLock) otherwise false (see also isLocalLocked).

   $flock(aLockFile).isLocked()


````
### $flock.lock

__$flock.lock()__

````
Given aLockFile will use the file to filesystem lock until unlock is called.

   $flock(aLockFile).lock()


````
### $flock.tryLock

__$flock.tryLock(aFunction) : Boolean__

````
Given aLockFile only execute aFunction if it's unlocked. If it executed aFunction it will return true otherwise false.

   $flock(aLockFile).tryLock(() => { ... })


````
### $flock.unlock

__$flock.unlock()__

````
Given aLockFile will unlock freeing any previous calls to lock.

   $flock(aLockFile).unlock()


````
### $fnDef4Help

__$fnDef4Help(aFnName) : Array__

````
Tries to retrieve an array of function argument names for the provided search string aFnName.
````
### $fnM

__$fnM(aFnName, aMap) : Object__

````
Calls aFnName function trying to determine the name of the arguments from OpenAF's help or accessible source code (throws an exception if it can't determine the arguments) and then builds the arguments used to call aFnName using the values of keys in aMap. Example:

plugin("HTTP"); var h = new HTTP();
$fnM("h.get", { aUrl: "https://openaf.io/release" });


````
### $fnM2A

__$fnM2A(aFn, aInstance, aDefinitionArray, aMap) : Object__

````
Tries to execute aFn, with aInstance if it's a function of an instance, using aMap of arguments that translate to aFn list of arguments. Returns whatever the function executed returns. Example:

plugin("HTTP");
var h = new HTTP();
$fnM2A(h.get, h, $fnDef4Help("HTTP.get"), { aUrl: "https://openaf.io/build", isBytes: false, returnStream: false });


````
### $from 

__$from : Array__

````
Shortcut for the nLinq library for easy query and access to arrays/objects. To see all the available options please refer to https://github.com/nmaguiar/nLinq/blob/main/Reference.md and the list of available functions by executing, in the openaf-console: "desc $from([])".
````
### $ft

__$ft(aString, arg1, arg2, ...) : String__

````
Equivalant to $f but number types are converted to Integer, Long, Double, Float and BigDecimal.
````
### $get

__$get(aKey) : Object__

````
Returns a value previously set with $set with aKey.
````
### $job

__$job(aJob, args, aId, isolate) : Object__

````
Shortcut to oJobRunJob and ow.oJob.runJob to execute aJob with args and returned the changed arguments. Optionally aId can be also provided. If isolate=true it will also clean the key 'res' and try to return the result of ow.oJob.output.
````
### $jsonrpc

__$jsonrpc(aOptions) : Map__

````
Creates a JSON-RPC client that can be used to communicate with a JSON-RPC server or a local process using stdio. The aOptions parameter is a map with the following possible keys: type (string, default "stdio" for local process or "remote" for remote server), url (string, required for remote server), timeout (number, default 60000 ms for remote server), cmd (string, required for local process), and options (map, optional additional options for remote server). The returned map has the following methods: type (to set the type), url (to set the URL for remote server), sh (to set the command for local process), exec (to execute a method with parameters), and destroy (to stop the client). The exec method returns a promise that resolves to the result of the method call or an error if the call fails. Example usage:

var client = $jsonrpc({type: "remote", url: "http://example.com/api", timeout: 5000});
client.exec("methodName", {param1: "value1", param2: "value2"}).then(result => {
    log("Result:", result);
}).catch(error => {
    logErr("Error:", error);
});

var localClient = $jsonrpc({type: "stdio", cmd: "myLocalProcess"});
localClient.exec("localMethod", {param1: "value1"}).then(result => {
    log("Local Result:", result);
}).catch(error => {
    logErr("Local Error:", error);
});

````
### $llm

__$llm(aModel) : $llm__

````
Shortcut for $gpt on the owrap.AI library.
````
### $lock.destroy

__$lock.destroy()__

````
Given aLockName will destroy the provided lock entry.

   $lock(aLockName).destroy()


````
### $lock.isLocked

__$lock.isLocked() : Boolean__

````
Given aLockName will return true if locked otherwise false.

   $lock(aLockName).isLocked()


````
### $lock.lock

__$lock.lock()__

````
Given aLockName will lock until unlock is called.

   $lock(aLockName).lock()


````
### $lock.tryLock

__$lock.tryLock(aFunction, aTimeoutMS) : Boolean__

````
Given aLockName only execute aFunction when it's able to lock or after aTimeoutMS. If it executed aFunction it will return true otherwise false.

   $lock(aLockName).tryLock(() => { ... })


````
### $lock.unlock

__$lock.unlock()__

````
Given aLockName will unlock freeing any previous calls to lock.

   $lock(aLockName).unlock()


````
### $m2a

__$m2a(aDef, aMap) : Array__

````
Tries to convert aMap into an array using the aDef array of keys for the values order in the output array. Example:

$m2a(['c', 'b', 'a'], { a: 1, b: 2, c: 3 })    // [ 3, 2, 1 ]


````
### $m4a

__$m4a(aMap, aKey) : Array__

````
Tries to create an array of maps from the provided aMap map of maps. Optionally if aKey is provided it will be added to each array map with the map key. Example:

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


````
### $openaf

__$openaf(aScript, aPMIn, aOpenAF, extraJavaParamsArray) : Object__

````
Tries to start an external process running openaf (if aOpenAF is provided, as a string or array, it will be used as the command to invoke openaf) to execute aScript setting the __pm variable to aPMIn. Upon execution end the __pm contents will be returned by the function.
````
### $path

__$path(obj, path, customFunctions) : Object__

````
Shortcut for the JMESPath library for easy query and access to arrays/objects. To see all the available options please refer to http://jmespath.org. Optional you can provide a map of customFunctions. Examples:

[Slicing]: 
  $path(arr, "[0:5]"); $path(arr, "[5:10]"); $path(arr, "[:5]"); $path(arr, "[::2]"); $path(arr, "[::-1]");

[Projections]: 
  $path(arr, "a[*].first"); $path(arr, "a.*.b"); $path(arr, "[]");

[Filters]: 
  $path(arr, "a[?b=='xyz'].c"); $path(arr, "a[?b>`1`].x");

[MultiSelect]: 
  $path(arr, "a[].[x, y]"); $path(arr, "a[].{ x: x, y: y }");

[Pipe]: 
  $path(arr, "a[*].b | [0]"); 

[Functions]: 
  abs(x), avg(x), contains(x, y), ceil(x), floor(x), join(x, arr), keys(obj), length(x), map(expr, arr), max(x), max_by(x, y), merge(a, b), min(a), min_by(a, b), not_null(a), reverse(arr), sort(arr), sort_by(a, y), starts_with(a, b), ends_with(a, b), sum(a), to_array(a), to_string(a), to_number(a), type(a), values(a)
  $path(arr, "a[?contains(@, 'b') == `true`]")

[OpenAF custom functions]: 
  a2m(arrFields, arrValues), a4m(arr, 'key', dontRemove), m2a(arrFields, obj), m4a(obj, 'key'), count_by(arr, 'field'), format(x, 'format'), formatn(x, 'format'), group(arr, 'field'), group_by(arr, 'field1,field2'), unique(arr), to_map(arr, 'field'), to_date(x), to_datef(x, format) from_datef(x, format), to_isoDate(x), flat_map(x), search_keys(arr, 'text'), search_values(arr, 'text'), delete(map, 'field'), substring(a, ini, end),
 template(a, 'template'), t(a, 'template'), templateF(x, 'template'), tF(x, 'template'), to_bytesAbbr(x), to_numAbbr(x), from_bytesAbbr(x), from_siAbbr(x), from_timeAbbr(x), timeago(x), from_ms(x, 'format'), replace(x, 're', 'flags', 'replaceText'), split(x, 'sep'), trim(x), index_of(x, 'search'), last_index_of(x, 'search'), lower_case(x), upper_case(x), concat(x, y), match(x, 're', 'flags'), amerge(x, y), to_slon(x), from_slon(x), to_json(x), from_json(x, str), to_yaml(x, isMultiDoc), from_yaml(x), trim(x), nvl(x, v), to_toml(x), from_toml(x) add(x, y), sub(x, y), mul(x, y), div(x, y), mod(x, y)
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
ch(name, op, arg1, arg2), path(obj, jmespath), opath(jmespath)
to_ms(date), timeagoAbbr(x)
env(str), envs(regex)
oafp(json/slon)
if(cond, then, else)
assign(obj, path, value), assignp(objPathStr, path, value)
random(min, max), srandom(min, max)
at(arrayIndex)
to_numSpace(num, space), from_numSpace(num, space)
 Functions only active if flag PATH_SAFE is false:
  ojob(name, argsJSSLON)
  sh(command, stdin), sh_json(command, stdin), sh_jsslon(command, stdin), sh_yaml(command, stdin)

Custom functions:
  $path(2, "example(@)", { example: { _func: (a) => { return Number(a) + 10; }, _signature: [ { types: [ $path().number ] } ] } });


````
### $py

__$py(aPythonCodeOrFile, aInput, aOutputArray) : Map__

````
Executes aPythonCodeOrFile using a map aInput as variables in python and returns a map with python  variables in aOutputArray.
````
### $pyExec

__$pyExec(aPythonCodeOrFile, aInput)__

````
Executes aPythonCodeOrFile using a map aInput as variables in python. The python execution will be 'standalone', with access to OpenAF functionality, but no output will be returned.
````
### $pyStart

__$pyStart()__

````
Start python process on the background. Should be stopped with $pyStop.
````
### $pyStop

__$pyStop()__

````
Stops the background python process started by $pyStart.
````
### $queue

__$queue(anArray) : Object__

````
Returns an object with the following methods:
- add(aItem) : adds aItem to the queue and returns true if successful
- remove(aItem) : removes aItem from the queue and returns true if successful
- addAll(aItems) : adds all aItems to the queue and returns true if successful
- has(aItem) : returns true if aItem is in the queue
- isEmpty() : returns true if the queue is empty
- size() : returns the size of the queue
- toArray() : returns the queue as an array
- peek() : returns the first item in the queue without removing it
- poll() : returns the first item in the queue and removes it
 The queue is implemented using a java.util.concurrent.ConcurrentLinkedQueue, which is thread-safe and allows concurrent access.
If anArray is provided, it will be added to the queue using addAll.
````
### $rest.delete

__$rest.delete(aBaseURI, aIdxMap) : Map__

````
Shortcut for ow.obj.rest.jsonRemove (see help ow.obj.rest.jsonRemove) using aOptions ($rest(aOptions).): login (function or string),  pass (word), connectionTimeout (in ms), requestHeaders (map), urlEncode (boolean), uriQuery (boolean), httpClient (ow.obj.http object), default (map to return when there is an exception), throwExceptions (boolean defaulting to false controlling between throwing exceptions on different from 2xx http codes or connection issues or returning a map (merge with default if available)  and an error entry), collectAllStats (boolean with default false to store per uri or host:port statitics), preAction function that receives and returns a map with changes (aBaseURL, aIdxMap, aDataRowMap, login, pass, conTimeout, reqHeaders, urlEncode and httpClient), retry (number) and retryWait (time in ms).
````
### $rest.delete2File

__$rest.delete2File(aFilePath, aBaseURI, aIdxMap)__

````
Shortcut for ow.obj.rest.jsonRemove (see help ow.obj.rest.jsonRemove) using aOptions ($rest(aOptions).): login (function or string),  pass (word), connectionTimeout (in ms), requestHeaders (map), urlEncode (boolean), uriQuery (boolean), httpClient (ow.obj.http object), default (map to return when there is an exception), throwExceptions (boolean defaulting to false controlling between throwing exceptions on different from 2xx http codes or connection issues or returning a map (merge with default if available)  and an error entry), collectAllStats (boolean with default false to store per uri or host:port statitics), preAction function that receives and returns a map with changes (aBaseURL, aIdxMap, aDataRowMap, login, pass, conTimeout, reqHeaders, urlEncode and httpClient), retry (number) and retryWait (time in ms). The byte output will be saved into aFilePath. Optional $rest(aOptions.downloadResume = true) will resume download of a file if it exists.
````
### $rest.delete2Stream

__$rest.delete2Stream(aBaseURI, aIdxMap) : JavaStream__

````
Shortcut for ow.obj.rest.jsonRemove (see help ow.obj.rest.jsonRemove) using aOptions ($rest(aOptions).): login (function or string),  pass (word), connectionTimeout (in ms), requestHeaders (map), urlEncode (boolean), uriQuery (boolean), httpClient (ow.obj.http object), default (map to return when there is an exception), throwExceptions (boolean defaulting to false controlling between throwing exceptions on different from 2xx http codes or connection issues or returning a map (merge with default if available)  and an error entry), collectAllStats (boolean with default false to store per uri or host:port statitics), preAction function that receives and returns a map with changes (aBaseURL, aIdxMap, aDataRowMap, login, pass, conTimeout, reqHeaders, urlEncode and httpClient), retry (number) and retryWait (time in ms).
````
### $rest.get

__$rest.get(aBaseURI, aIdxMap) : Map__

````
Shortcut for ow.obj.rest.jsonGet (see help ow.obj.rest.jsonGet) using aOptions ($rest(aOptions).): login (function or string),  pass (word), connectionTimeout (in ms), requestHeaders (map), urlEncode (boolean), uriQuery (boolean), httpClient (ow.obj.http object), default (map to return when there is an exception), throwExceptions (boolean defaulting to false controlling between throwing exceptions on different from 2xx http codes or connection issues or returning a map (merge with default if available)  and an error entry), collectAllStats (boolean with default false to store per uri or host:port statitics), preAction function that receives and returns a map with changes (aBaseURL, aIdxMap, aDataRowMap, login, pass, conTimeout, reqHeaders, urlEncode and httpClient), retry (number) and retryWait (time in ms).
````
### $rest.get2File

__$rest.get2File(aFilePath, aBaseURI, aIdxMap)__

````
Shortcut for ow.obj.rest.jsonGet (see help ow.obj.rest.jsonGet) using aOptions ($rest(aOptions).): login (function or string),  pass (word), connectionTimeout (in ms), requestHeaders (map), urlEncode (boolean), uriQuery (boolean), httpClient (ow.obj.http object), default (map to return when there is an exception), throwExceptions (boolean defaulting to false controlling between throwing exceptions on different from 2xx http codes or connection issues or returning a map (merge with default if available)  and an error entry), collectAllStats (boolean with default false to store per uri or host:port statitics), preAction function that receives and returns a map with changes (aBaseURL, aIdxMap, aDataRowMap, login, pass, conTimeout, reqHeaders, urlEncode and httpClient), retry (number) and retryWait (time in ms). The byte output will be saved into aFilePath. Optional $rest(aOptions.downloadResume = true) will resume download of a file if it exists.
````
### $rest.get2Stream

__$rest.get2Stream(aBaseURI, aIdxMap) : JavaStream__

````
Shortcut for ow.obj.rest.jsonGet (see help ow.obj.rest.jsonGet) using aOptions ($rest(aOptions).): login (function or string),  pass (word), connectionTimeout (in ms), requestHeaders (map), urlEncode (boolean), uriQuery (boolean), httpClient (ow.obj.http object), default (map to return when there is an exception), throwExceptions (boolean defaulting to false controlling between throwing exceptions on different from 2xx http codes or connection issues or returning a map (merge with default if available)  and an error entry), collectAllStats (boolean with default false to store per uri or host:port statitics), preAction function that receives and returns a map with changes (aBaseURL, aIdxMap, aDataRowMap, login, pass, conTimeout, reqHeaders, urlEncode and httpClient), retry (number) and retryWait (time in ms).
````
### $rest.head

__$rest.head(aBaseURI, aIdxMap)__

````
Shortcut for ow.obj.rest.head (see help ow.obj.rest.head) using aOptions ($rest(aOptions).): login (function or string),  pass (word), connectionTimeout (in ms), requestHeaders (map), urlEncode (boolean), uriQuery (boolean), httpClient (ow.obj.http object), default (map to return when there is an exception), throwExceptions (boolean defaulting to false controlling between throwing exceptions on different from 2xx http codes or connection issues or returning a map (merge with default if available)  and an error entry), collectAllStats (boolean with default false to store per uri or host:port statitics), preAction function that receives and returns a map with changes (aBaseURL, aIdxMap, login, pass, conTimeout, reqHeaders, urlEncode and httpClient), retry (number) and retryWait (time in ms).
````
### $rest.index

__$rest.index(aMap) : String__

````
Shortcut for ow.obj.rest.writeIndexes (see help ow.obj.rest.writeIndexes).
````
### $rest.patch

__$rest.patch(aBaseURI, aDataRowMap, aIdxMap) : Map__

````
Shortcut for ow.obj.rest.jsonPatch (see help ow.obj.rest.jsonPatch) using aOptions ($rest(aOptions).): login (function or string),  pass (word), connectionTimeout (in ms), requestHeaders (map), urlEncode (boolean), uriQuery (boolean), httpClient (ow.obj.http object), default (map to return when there is an exception), throwExceptions (boolean defaulting to false controlling between throwing exceptions on different from 2xx http codes or connection issues or returning a map (merge with default if available)  and an error entry), collectAllStats (boolean with default false to store per uri or host:port statitics), preAction function that receives and returns a map with changes (aBaseURL, aIdxMap, aDataRowMap, login, pass, conTimeout, reqHeaders, urlEncode and httpClient), retry (number) and retryWait (time in ms).
````
### $rest.patch2File

__$rest.patch2File(aFilePath, aBaseURI, aDataRowMap, aIdxMap)__

````
Shortcut for ow.obj.rest.jsonPatch (see help ow.obj.rest.jsonPatch) using aOptions ($rest(aOptions).): login (function or string),  pass (word), connectionTimeout (in ms), requestHeaders (map), urlEncode (boolean), uriQuery (boolean), httpClient (ow.obj.http object), default (map to return when there is an exception), throwExceptions (boolean defaulting to false controlling between throwing exceptions on different from 2xx http codes or connection issues or returning a map (merge with default if available)  and an error entry), collectAllStats (boolean with default false to store per uri or host:port statitics), preAction function that receives and returns a map with changes (aBaseURL, aIdxMap, aDataRowMap, login, pass, conTimeout, reqHeaders, urlEncode and httpClient), retry (number) and retryWait (time in ms).  The byte output will be saved into aFilePath. Optional $rest(aOptions.downloadResume = true) will resume download of a file if it exists.
````
### $rest.patch2Stream

__$rest.patch2Stream(aBaseURI, aDataRowMap, aIdxMap) : JavaStream__

````
Shortcut for ow.obj.rest.jsonPatch (see help ow.obj.rest.jsonPatch) using aOptions ($rest(aOptions).): login (function or string),  pass (word), connectionTimeout (in ms), requestHeaders (map), urlEncode (boolean), uriQuery (boolean), httpClient (ow.obj.http object), default (map to return when there is an exception), throwExceptions (boolean defaulting to false controlling between throwing exceptions on different from 2xx http codes or connection issues or returning a map (merge with default if available)  and an error entry), collectAllStats (boolean with default false to store per uri or host:port statitics), preAction function that receives and returns a map with changes (aBaseURL, aIdxMap, aDataRowMap, login, pass, conTimeout, reqHeaders, urlEncode and httpClient), retry (number) and retryWait (time in ms).
````
### $rest.patchUpload

__$rest.patchUpload(aBaseURI, aDataRowMap, aIdxMap) : Map__

````
Shortcut for ow.obj.rest.upload (see help ow.obj.rest.upload with patch) using aOptions ($rest(aOptions).): login (function or string),  pass (word), connectionTimeout (in ms), requestHeaders (map), urlEncode (boolean), uriQuery (boolean), httpClient (ow.obj.http object), default (map to return when there is an exception), throwExceptions (boolean defaulting to false controlling between throwing exceptions on different from 2xx http codes or connection issues or returning a map (merge with default if available)  and an error entry), collectAllStats (boolean with default false to store per uri or host:port statitics), preAction function that receives and returns a map with changes (aBaseURL, aIdxMap, aDataRowMap, login, pass, conTimeout, reqHeaders, urlEncode and httpClient), retry (number) and retryWait (time in ms).
````
### $rest.patchUpload2Stream

__$rest.patchUpload2Stream(aBaseURI, aDataRowMap, aIdxMap) : JavaStream__

````
Shortcut for ow.obj.rest.upload (see help ow.obj.rest.upload with patch) using aOptions ($rest(aOptions).): login (function or string),  pass (word), connectionTimeout (in ms), requestHeaders (map), urlEncode (boolean), uriQuery (boolean), httpClient (ow.obj.http object), default (map to return when there is an exception), throwExceptions (boolean defaulting to false controlling between throwing exceptions on different from 2xx http codes or connection issues or returning a map (merge with default if available)  and an error entry), collectAllStats (boolean with default false to store per uri or host:port statitics), preAction function that receives and returns a map with changes (aBaseURL, aIdxMap, aDataRowMap, login, pass, conTimeout, reqHeaders, urlEncode and httpClient), retry (number) and retryWait (time in ms).
````
### $rest.post

__$rest.post(aBaseURI, aDataRowMap, aIdxMap) : Map__

````
Shortcut for ow.obj.rest.jsonCreate (see help ow.obj.rest.jsonCreate) using aOptions ($rest(aOptions).): login (function or string),  pass (word), connectionTimeout (in ms), requestHeaders (map), urlEncode (boolean), uriQuery (boolean), httpClient (ow.obj.http object), default (map to return when there is an exception), throwExceptions (boolean defaulting to false controlling between throwing exceptions on different from 2xx http codes or connection issues or returning a map (merge with default if available)  and an error entry), collectAllStats (boolean with default false to store per uri or host:port statitics), preAction function that receives and returns a map with changes (aBaseURL, aIdxMap, aDataRowMap, login, pass, conTimeout, reqHeaders, urlEncode and httpClient), retry (number) and retryWait (time in ms).
````
### $rest.post2File

__$rest.post2File(aFilePath, aBaseURI, aDataRowMap, aIdxMap)__

````
Shortcut for ow.obj.rest.jsonCreate (see help ow.obj.rest.jsonCreate) using aOptions ($rest(aOptions).): login (function or string),  pass (word), connectionTimeout (in ms), requestHeaders (map), urlEncode (boolean), uriQuery (boolean), httpClient (ow.obj.http object), default (map to return when there is an exception), throwExceptions (boolean defaulting to false controlling between throwing exceptions on different from 2xx http codes or connection issues or returning a map (merge with default if available)  and an error entry), collectAllStats (boolean with default false to store per uri or host:port statitics), preAction function that receives and returns a map with changes (aBaseURL, aIdxMap, aDataRowMap, login, pass, conTimeout, reqHeaders, urlEncode and httpClient), retry (number) and retryWait (time in ms). The byte output will be saved into aFilePath. Optional $rest(aOptions.downloadResume = true) will resume download of a file if it exists.
````
### $rest.post2Stream

__$rest.post2Stream(aBaseURI, aDataRowMap, aIdxMap) : JavaStream__

````
Shortcut for ow.obj.rest.jsonCreate (see help ow.obj.rest.jsonCreate) using aOptions ($rest(aOptions).): login (function or string),  pass (word), connectionTimeout (in ms), requestHeaders (map), urlEncode (boolean), uriQuery (boolean), httpClient (ow.obj.http object), default (map to return when there is an exception), throwExceptions (boolean defaulting to false controlling between throwing exceptions on different from 2xx http codes or connection issues or returning a map (merge with default if available)  and an error entry), collectAllStats (boolean with default false to store per uri or host:port statitics), preAction function that receives and returns a map with changes (aBaseURL, aIdxMap, aDataRowMap, login, pass, conTimeout, reqHeaders, urlEncode and httpClient), retry (number) and retryWait (time in ms).
````
### $rest.postUpload

__$rest.postUpload(aBaseURI, aDataRowMap, aIdxMap) : Map__

````
Shortcut for ow.obj.rest.upload (see help ow.obj.rest.upload with post) using aOptions ($rest(aOptions).): login (function or string),  pass (word), connectionTimeout (in ms), requestHeaders (map), urlEncode (boolean), uriQuery (boolean), httpClient (ow.obj.http object), default (map to return when there is an exception), throwExceptions (boolean defaulting to false controlling between throwing exceptions on different from 2xx http codes or connection issues or returning a map (merge with default if available)  and an error entry), collectAllStats (boolean with default false to store per uri or host:port statitics), preAction function that receives and returns a map with changes (aBaseURL, aIdxMap, aDataRowMap, login, pass, conTimeout, reqHeaders, urlEncode and httpClient), retry (number) and retryWait (time in ms).
````
### $rest.postUpload2Stream

__$rest.postUpload2Stream(aBaseURI, aDataRowMap, aIdxMap) : JavaStream__

````
Shortcut for ow.obj.rest.upload (see help ow.obj.rest.upload with post) using aOptions ($rest(aOptions).): login (function or string),  pass (word), connectionTimeout (in ms), requestHeaders (map), urlEncode (boolean), uriQuery (boolean), httpClient (ow.obj.http object), default (map to return when there is an exception), throwExceptions (boolean defaulting to false controlling between throwing exceptions on different from 2xx http codes or connection issues or returning a map (merge with default if available)  and an error entry), collectAllStats (boolean with default false to store per uri or host:port statitics), preAction function that receives and returns a map with changes (aBaseURL, aIdxMap, aDataRowMap, login, pass, conTimeout, reqHeaders, urlEncode and httpClient), retry (number) and retryWait (time in ms).
````
### $rest.put

__$rest.put(aBaseURI, aDataRowMap, aIdxMap) : Map__

````
Shortcut for ow.obj.rest.jsonSet (see help ow.obj.rest.jsonSet) using aOptions ($rest(aOptions).): login (function or string),  pass (word), connectionTimeout (in ms), requestHeaders (map), urlEncode (boolean), uriQuery (boolean), httpClient (ow.obj.http object), default (map to return when there is an exception), throwExceptions (boolean defaulting to false controlling between throwing exceptions on different from 2xx http codes or connection issues or returning a map (merge with default if available)  and an error entry), collectAllStats (boolean with default false to store per uri or host:port statitics), preAction function that receives and returns a map with changes (aBaseURL, aIdxMap, aDataRowMap, login, pass, conTimeout, reqHeaders, urlEncode and httpClient), retry (number) and retryWait (time in ms).
````
### $rest.put2File

__$rest.put2File(aFilePath, aBaseURI, aDataRowMap, aIdxMap)__

````
Shortcut for ow.obj.rest.jsonSet (see help ow.obj.rest.jsonSet) using aOptions ($rest(aOptions).): login (function or string),  pass (word), connectionTimeout (in ms), requestHeaders (map), urlEncode (boolean), uriQuery (boolean), httpClient (ow.obj.http object), default (map to return when there is an exception), throwExceptions (boolean defaulting to false controlling between throwing exceptions on different from 2xx http codes or connection issues or returning a map (merge with default if available)  and an error entry), collectAllStats (boolean with default false to store per uri or host:port statitics), preAction function that receives and returns a map with changes (aBaseURL, aIdxMap, aDataRowMap, login, pass, conTimeout, reqHeaders, urlEncode and httpClient), retry (number) and retryWait (time in ms). The byte output will be saved into aFilePath. Optional $rest(aOptions.downloadResume = true) will resume download of a file if it exists.
````
### $rest.put2Stream

__$rest.put2Stream(aBaseURI, aDataRowMap, aIdxMap) : JavaStream__

````
Shortcut for ow.obj.rest.jsonSet (see help ow.obj.rest.jsonSet) using aOptions ($rest(aOptions).): login (function or string),  pass (word), connectionTimeout (in ms), requestHeaders (map), urlEncode (boolean), uriQuery (boolean), httpClient (ow.obj.http object), default (map to return when there is an exception), throwExceptions (boolean defaulting to false controlling between throwing exceptions on different from 2xx http codes or connection issues or returning a map (merge with default if available)  and an error entry), collectAllStats (boolean with default false to store per uri or host:port statitics), preAction function that receives and returns a map with changes (aBaseURL, aIdxMap, aDataRowMap, login, pass, conTimeout, reqHeaders, urlEncode and httpClient), retry (number) and retryWait (time in ms).
````
### $rest.putUpload

__$rest.putUpload(aBaseURI, aDataRowMap, aIdxMap) : Map__

````
Shortcut for ow.obj.rest.upload (see help ow.obj.rest.upload with put) using aOptions ($rest(aOptions).): login (function or string),  pass (word), connectionTimeout (in ms), requestHeaders (map), urlEncode (boolean), uriQuery (boolean), httpClient (ow.obj.http object), default (map to return when there is an exception), throwExceptions (boolean defaulting to false controlling between throwing exceptions on different from 2xx http codes or connection issues or returning a map (merge with default if available)  and an error entry), collectAllStats (boolean with default false to store per uri or host:port statitics), preAction function that receives and returns a map with changes (aBaseURL, aIdxMap, aDataRowMap, login, pass, conTimeout, reqHeaders, urlEncode and httpClient), retry (number) and retryWait (time in ms).
````
### $rest.putUpload2Stream

__$rest.putUpload2Stream(aBaseURI, aDataRowMap, aIdxMap) : JavaStream__

````
Shortcut for ow.obj.rest.upload (see help ow.obj.rest.upload with post) using aOptions ($rest(aOptions).): login (function or string),  pass (word), connectionTimeout (in ms), requestHeaders (map), urlEncode (boolean), uriQuery (boolean), httpClient (ow.obj.http object), default (map to return when there is an exception), throwExceptions (boolean defaulting to false controlling between throwing exceptions on different from 2xx http codes or connection issues or returning a map (merge with default if available)  and an error entry), collectAllStats (boolean with default false to store per uri or host:port statitics), preAction function that receives and returns a map with changes (aBaseURL, aIdxMap, aDataRowMap, login, pass, conTimeout, reqHeaders, urlEncode and httpClient), retry (number) and retryWait (time in ms).
````
### $rest.query

__$rest.query(aMap) : String__

````
Shortcut for ow.obj.rest.writeQuery (see help ow.obj.rest.writeQuery).
````
### $retry

__$retry(aFunction, aNumOfTriesOrFunction) : Object__

````
Tries to execute aFunction and return the corresponding returned result. If aNumOfTriesOrFunction is a number (defaults to 1) and aFunction throws an exception it will repeat aFunction until it doesn't throw an exception or for the number of aNumOfTriesOrFunc. If aNumOfTriesOrFunction is a function it will be called whenever aFunction throws an exception with the corresponding exception as argument and it will retry until aNumOfTriesOrFunction returns false.
````
### $set

__$set(aKey, aValue)__

````
Sets aValue with aKey so it can be retrieved with $get later.
````
### $sh.cb

__$sh.cb(aCallbackFunc) : $sh__

````
When executing aCmd (with .get) use aCallbackFunc function.
````
### $sh.cp

__$sh.cp(aSource, aTarget) : $sh__

````
Immediately copies aSource to aTarget before executing aCmd (with .exec).
````
### $sh.dontWait

__$sh.dontWait(aBooleanValue) : $sh__

````
If aBooleanValue = true the execution won't wait for output (default: false).
````
### $sh.envs

__$sh.envs(aMap, includeExisting) : $sh__

````
Uses aMap of strings as the environment variables map. If includeExisting = true it will include the current environment variables also.
````
### $sh.exec

__$sh.exec(aIdx) : Object__

````
Immediately copies the result of executing aCmd string or array (and any other commands in queue added using sh). If aIdx is provided it will return the map entry for the corresponding command on the array otherwise it will return the array.
````
### $sh.exit

__$sh.exit(aFunc) : $sh__

````
Sets aFunc function to execute after the execution of aCmd (with .exec).
````
### $sh.get

__$sh.get(aIdx) : Object__

````
Immediately copies the result of executing aCmd string or array (and any other commands in queue added using sh). If aIdx is provided it will return the map entry for the corresponding command on the array otherwise it will return the array.
````
### $sh.getJson

__$sh.getJson(aIdx) : Object__

````
Immediately copies the result of executing aCmd string or array (and any other commands in queue added using sh) trying to parse it as json (will ingore non json content). If aIdx is provided it will return the map entry for the corresponding command on the array otherwise it will return the array.
````
### $sh.getJsSlon

__$sh.getJsSlon(aIdx) : Object__

````
Immediately copies the result of executing aCmd string or array (and any other commands in queue added using sh) trying to parse it as json or slon. If aIdx is provided it will return the map entry for the corresponding command on the array otherwise it will return the array.
````
### $sh.getYaml

__$sh.getYaml(aIdx) : Object__

````
Immediately copies the result of executing aCmd string or array (and any other commands in queue added using sh) trying to parse it as yaml. If aIdx is provided it will return the map entry for the corresponding command on the array otherwise it will return the array.
````
### $sh.mkdir

__$sh.mkdir(aDir) : $sh__

````
Immediately creates aDir before executing aCmd (with .exec).
````
### $sh.mv

__$sh.mv(aSource, aTarget) : $sh__

````
Immediately moves aSource to aTarget before executing aCmd (with .exec).
````
### $sh.prefix

__$sh.prefix(aPrefix, aTemplate) : $sh__

````
When executing aCmd (with .get) it will use ow.format.streamSHPrefix with aPrefix and optionally aTemplate.
````
### $sh.pwd

__$sh.pwd(aPwd) : $sh__

````
When executing aCmd (with .exec) use aPwd as the current working directory.
````
### $sh.rename

__$sh.rename(aSource, aTarget) : $sh__

````
Immediately renames aSource to aTarget before executing aCmd (with .exec).
````
### $sh.rm

__$sh.rm(aFilePath) : $sh__

````
Immediately removes aFilePath before executing aCmd (with .exec).
````
### $sh.sh

__$sh.sh(aCmd, aIn) : $sh__

````
When executing aCmd (with .exec) sets additional aCmds (with the optional corresponding aIn) to use.
````
### $sh.timeout

__$sh.timeout(aTimeout) : $sh__

````
When executing aCmd (with .exec) uses aTimeout.
````
### $sh.useEncoding

__$sh.useEncoding(aEncoding) : $sh__

````
Forces the aEncoding to be used.
````
### $sql

__$sql(aObject, aSQL, aMethod) : Array__

````
Given an aObject (map or array) will try to execute aSQL (SQL expression) and return the corresponding results. Optionally you can provide aMethod to be used (e.g. "auto" (default) or "nlinq" or "h2"). "nlinq" it's the fastest but doesn't support aggregations or multi-field combinations; "h2" is the more complete but will require a lot more resources, it's slower.

NOTE: In "h2" you can use the table _TMP for your queries.
````
### $ssh.$ssh

__$ssh.$ssh(aMap) : $ssh__

````
Builds an object to allow access through ssh. aMap should be a ssh string with the format: ssh://user:pass@host:port/identificationKey?timeout=1234&compression=true or a map with the keys: host, port, login, pass, id (file key) / key (string representation), compress and timeout. See "help SSH.SSH" for more info.
````
### $ssh.cb

__$ssh.cb(aCallback) : $ssh__

````
Sets aCallback function to execute during the execution of commands on a remote host defined by aMap (host, port, login, pass, id, compress and timeout).
````
### $ssh.close

__$ssh.close() : $ssh__

````
Closes a remote host connection defined by aMap (host, port, login, pass, id, compress and timeout).
````
### $ssh.exec

__$ssh.exec(aIdx) : Array__

````
Executes a list of commands previously set on a remote host connection defined by aMap (host, port, login, pass, id, compress and timeout). IO is inherit. If aIdx is provided it will return the map entry for the corresponding command on the array otherwise it will return the array.
````
### $ssh.exit

__$ssh.exit(aFunc) : $ssh__

````
Sets a callback aFunc to execute upon a command execution s a remote host connection defined by aMap (host, port, login, pass, id, compress and timeout).
````
### $ssh.get

__$ssh.get(aIdx) : Object__

````
Executes a list of commands previously set on a remote host connection defined by aMap (host, port, login, pass, id, compress and timeout). IO is not inherit. If aIdx is provided it will return the map entry for the corresponding command on the array otherwise it will return the array.
````
### $ssh.getFile

__$ssh.getFile(aSource, aTarget) : $ssh__

````
Gets aSource filepath and stores it locally on aTarget from a remote host defined by aMap (host, port, login, pass, id, compress and timeout).
````
### $ssh.getJson

__$ssh.getJson(aIdx) : Object__

````
Executes a list of commands previously set on a remote host connection defined by aMap (host, port, login, pass, id, compress and timeout). IO is not inherit. If aIdx is provided it will return the map entry for the corresponding command on the array otherwise it will return the array. The stdout and stderr will be pre-parsed from json to objects.
````
### $ssh.listFiles

__$ssh.listFiles(aRemotePath) : Array__

````
Returns an array of maps with the listing of aRemotePath provided.
````
### $ssh.mkdir

__$ssh.mkdir(aDirectory) : $ssh__

````
Creates aDirectory via SFTP on a remote host defined by aMap (host, port, login, pass, id, compress and timeout).
````
### $ssh.prefix

__$ssh.prefix(aPrefix, aTemplate) : $ssh__

````
When executing aCmd (with .get) it will use ow.format.streamSHPrefix with aPrefix and optionally aTemplate.
````
### $ssh.pty

__$ssh.pty(aFlag) : $ssh__

````
Sets the flag to use or not a pty term allocation on the ssh connection to a remote host defined by aMap (host, port, login, pass, id, key, compress and timeout).
````
### $ssh.putFile

__$ssh.putFile(aSource, aTarget) : $ssh__

````
Puts aSource local filepath and stores it remotely in aTarget on a remote host defined by aMap (host, port, login, pass, id, compress and timeout).
````
### $ssh.pwd

__$ssh.pwd(aPwd) : $ssh__

````
Sets aPwd directory for getting and sending files to a remote host defined by aMap (host, port, login, pass, id, compress and timeout).
````
### $ssh.rename

__$ssh.rename(aSource, aTarget) : $ssh__

````
Renames aSource filepath to aTarget filepath on a remote host defined by aMap (host, port, login, pass, id, compress and timeout).
````
### $ssh.rm

__$ssh.rm(aFilePath) : $ssh__

````
Remove aFilePath from a remote host defined by aMap (host, port, login, pass, id, compress and timeout).
````
### $ssh.rmdir

__$ssh.rmdir(aFilePath) : $ssh__

````
Removes a directory from a remote host defined by aMap (host, port, login, pass, id, compress and timeout).
````
### $ssh.sh

__$ssh.sh(aCmd, aIn) : $ssh__

````
Sets aCmd to be executed with an optional aIn (stdin) on the remote host defined by aMap (host, port, login, pass, id, compress and timeout).
````
### $ssh.timeout

__$ssh.timeout(aTimeout) : $ssh__

````
Sets aTimeout in ms for the ssh/sftp connection to a remote host defined by aMap (host, port, login, pass, id, compress and timeout).
````
### $ssh.tunnelLocal

__$ssh.tunnelLocal(aLocalPort, aRemoteHost, aRemotePort) : $ssh__

````
Creates a local tunnel mapping aLocalPort to aRemoteHost:aRemotePort using the ssh connection defined by aMap (host, port, login, pass, id, compress and timeout).
````
### $ssh.tunnelLocalBind

__$ssh.tunnelLocalBind(aLocalInterface, aLocalPort, aRemoteHost, aRemotePort) : $ssh__

````
Creates a local tunnel mapping aLocalInterface:aLocalPort to aRemoteHost:aRemotePort using the ssh connection defined by aMap (host, port, login, pass, id, compress and timeout).
````
### $ssh.tunnelRemote

__$ssh.tunnelRemote(aRemotePort, aLocalAddress aLocalPort) : $ssh__

````
Creates a remote tunnel mapping aRemotePort to aLocalAddress:aLocalPort using the ssh connection defined by aMap (host, port, login, pass, id, compress and timeout).
````
### $ssh.tunnelRemoteBind

__$ssh.tunnelRemoteBind(aRemoteInterface, aRemotePort, aLocalAddress aLocalPort) : $ssh__

````
Creates a remote tunnel mapping aRemoteInterface:aRemotePort to aLocalAddress:aLocalPort using the ssh connection defined by aMap (host, port, login, pass, id, compress and timeout).
````
### $stream

__$stream__

````
Shortcut for the streamjs library for easy query and access to streams of data. To see all the available options please refer to https://github.com/winterbe/streamjs/blob/master/APIDOC.md.
````
### $sync

__$sync() : Object__

````
Returns an object with a 'run(aFn)' function that will execute the provided aFn in a synchronized way. The run function will lock the execution until the aFn is finished. This is useful to ensure that only one thread is executing the aFn at a time.

Example:

var s = $sync()
s.run(() => {
    // Your code here, only one thread will execute this at a time
})
````
### $tb

__$tb(aFunction) : Result__

````
Shorcut for a "thread-box" to execute aFunction. The "thread" will timeout with the provided execution timeout (in ms) or stop whenever the stopWhen function returns true (called continuously or after each timeout). Examples:

   $tb().timeout(5000).exec(aFunc);  // Executes aFunc to a maximum of 5 seconds. Afterwards the aFunc is stopped.
   $tb(aFunc).timeout(5000).exec();  // Sames as previous, aFunc can be provided before or on exec.
   $tb().timeout(500).stopWhen(aStopFunc).exec(); // Stops when aStopFunc is true.

````
### $throwIfUnDef

__$throwIfUnDef(aFunc) : Function__

````
Returns a function that tries to execute aFunc and throws and exception if the result if undefined otherwise returns the result. Usefull with $retry when waiting for a "defined" result.
````
### $unset

__$unset(aKey)__

````
Unset a previously set value with aKey.
````
### _i$

___i$(aValue, aPrefixMessage) : Object__

````
Same as _$ but if aValue is not defined and aPrefixMessage if defined it will use ask() or askEncrypt() to  interactively ask the user for the value with the prompt "[aPrefixMessage]: ". Should only be used if user interaction is expected but to force not be interactiv you can set __i$interactive to false). Note: askEncrypt will be used if aPrefixMessage has any reference to "secret" or "pass".
````
### addOnOpenAFShutdown

__addOnOpenAFShutdown(aFunction) : Boolean__

````
Adds aFunction to try to execute whenever OpenAF is going to shutdown. The latest hook added will be the first to be executed until the first hook added (actually a shortcut for Threads.addOpenAFShutdownHook).
````
### addOPackRemoteDB

__addOPackRemoteDB(aURL)__

````
Adds a path to an opack.db file to the current search path.
````
### AF.encryptText

__AF.encryptText()__

````
Interactevly asks to enter a text and then uses af.encrypt to print to stdout the result.
````
### AF.fromJavaArray

__AF.fromJavaArray(aJavaArray) : Array__

````
Tries to convert aJavaArray into a native an array.
````
### AF.fromJSSLON

__AF.fromJSSLON(aString) : Object__

````
Tries to convert the provided aString into an object. The string might be JSON or SLON.
````
### AF.fromNLinq

__AF.fromNLinq(aString) : Map__

````
Converts a nLinq chained command line string representation into a suitable map to be used with $from.query.
````
### af.fromObj2XML

__af.fromObj2XML(aMap, sanitize, aAttrKey) : String__

````
Tries to convert aMap into a similiar XML strucuture returned as string. Note that no validation of XML strucuture is performed.  If aAttrKey string is defined it will be used to prefix attributes (from af.fromXML2Obj). Tips: ensure each map is under a map key.
````
### AF.fromSLON

__AF.fromSLON(aString) : Map__

````
Converts a SLON (https://github.com/nmaguiar/slon) string representation into the original map.
````
### AF.fromSQL

__AF.fromSQL(aString) : Map__

````
Converts a SQL expression into an ASP map.
````
### AF.fromSQL2NLinq

__AF.fromSQL2NLinq(aSQL) : Map__

````
Converts a SQL expression into a suitable map to be used with $from.query.
````
### af.fromTOML

__af.fromTOML(aTOML) : Object__

````
Tries to parse aTOML into a javascript object
````
### af.fromXML2Obj

__af.fromXML2Obj(xml, ignored, aPrefix, reverseIgnored) : Object__

````
Tries to convert a XML object into a javascript object. Tag attributes will be ignored unless the corresponding tag name is included on the ignored array and attributes will be added to the corresponding map with a prefix "_" (or aPrefix). Optionally if reverseIgnored = true the ignored array will be used to not include the tag name in the ignored array.
````
### AF.fromYAML

__AF.fromYAML(aYaml) : Object__

````
Tries to parse aYaml into a javascript map.
````
### AF.getEncoding

__AF.getEncoding(anArrayOfBytesORString) : String__

````
Given anArrayOfBytesORString will try to detect which encode is used and returns a string with the identified charset encoding.
````
### af.nvl

__af.nvl(aValue, aDefault) : Object__

````
Returns aValue if it is defined or aDefault otherwise.
````
### AF.printStackTrace

__AF.printStackTrace(aFunction) : Object__

````
Executes aFunction but if it throws an exception and the exception is a Java exception it will print the exception's stack trace.
````
### AF.protectSystemExit

__AF.protectSystemExit(shouldProtect, aMessage)__

````
Protects the current execution against a exit instruction if shouldProtect = true (otherwise it will unprotect). If protected a security exception with aMessage (string) followed by the exit status will be thrown or the result of calling function aMessage with the exit status as a parameter.
````
### af.runFromExternalClass

__af.runFromExternalClass(aClassName, aPath)__

````
Tries to "execute" aClassName from a previously compiled OpenAF script, with af.compileToClasses, on aPath.

Example:
   af.compileToClasses("MyClass", "var myOpen = 'AF Class'", ".");
   af.runFromExternalClass("MyClass", ".");
   myOpen; // AF Class


````
### AF.setInteractiveTerminal

__AF.setInteractiveTerminal()__

````
Sets the current terminal to be interactive (no echo, no buffering).
````
### AF.swap

__AF.swap(anArray, anIndex1, anIndex2) : Array__

````
Swaps the elements at anIndex1 and anIndex2 in anArray. Returns the new array with the elements swapped.
````
### AF.toCSLON

__AF.toCSLON(aObject, aTheme) : String__

````
Converts aObject map/array into SLON representation with ansi colors (see more in help for ow.format.toCSLON)
````
### AF.toSLON

__AF.toSLON(aObject, aTheme) : String__

````
Converts aObject map/array into SLON representation (see more in help for ow.format.toSLON)
````
### af.toTOML

__af.toTOML(aObj) : String__

````
Tries to convert aObj into a TOML string.
````
### AF.toYAML

__AF.toYAML(aJson, multiDoc, sanitize, shouldColor) : String__

````
Tries to dump aJson into a YAML string. If multiDoc = true and aJson is an array the output will be multi-document. If sanitize = true all Java objects will be converted to avoid parsing errors.
````
### AF.unsetInteractiveTerminal

__AF.unsetInteractiveTerminal()__

````
Unsets the current terminal to be interactive (no echo, no buffering).
````
### ansiColor

__ansiColor(aAnsi, aString, force, noCache, noReset) : String__

````
Returns the ANSI codes together with aString, if determined that the current terminal can handle ANSI codes (overridden by force = true), with the attributes defined in aAnsi. Please use with ansiStart() and ansiStop(). The optional noReset boolean flag will remove ansi reset as part of the string returned. The attributes separated by commas can be:

BLACK; RED; GREEN; YELLOW; BLUE; MAGENTA; CYAN; WHITE;
FG_BLACK; FG_RED; FG_GREEN; FG_YELLOW; FG_BLUE; FG_MAGENTA; FG_CYAN; FG_WHITE;
BG_BLACK; BG_RED; BG_GREEN; BG_YELLOW; BG_BLUE; BG_MAGENTA; BG_CYAN; BG_WHITE;
BOLD; FAINT; INTENSITY_BOLD; INTENSITY_FAINT; ITALIC; UNDERLINE; BLINK_SLOW; BLINK_FAST; BLINK_OFF; NEGATIVE_ON; NEGATIVE_OFF; CONCEAL_ON; CONCEAL_OFF; UNDERLINE_DOUBLE; UNDERLINE_OFF;


````
### ansiLength

__ansiLength(aString) : Number__

````
Tries to return the aString length without any ansi control sequences.
````
### ansiStart

__ansiStart(force)__

````
Prepares to output ansi codes if the current terminal is capable off (unless force = true). Use with ansiColor() and ansiStop().
````
### ansiStop

__ansiStop(force)__

````
Disables the output of ansi codes if the current terminal is capable off (unless force = true). Use with ansiColor() and ansiStart().
````
### ansiWinTermCap

__ansiWinTermCap() : boolean__

````
Determines in Windows if the current terminal has support for newer capabilities or not (e.g. cmd.exe)
````
### arrayContains

__arrayContains(anArray, aObj, aPreFilter) : Number__

````
Tries to find aObj in anArray returning the position where it's first found or -1 if not found. Optionally aPreFilter function can prepare each object for comparing.
````
### ask

__ask(aPrompt, aMask) : String__

````
Stops for user interaction prompting aPrompt waiting for an entire line of characters and, optionally, masking the user input with aMask (e.g. "*"). Returns the user input.
````
### ask1

__ask1(aPrompt, allowed) : String__

````
Stops for user interaction prompting aPrompt waiting for a single character within the allowed string (a set of characters). Returns the user input.
````
### askChoose

__askChoose(aPrompt, anArray, aMaxDisplay, aHelpText) : Number__

````
Stops for user interaction prompting aPrompt waiting for a single character to choose from the provided anArray of options. Optionally you can provide aMaxDisplay to limit the number of options displayed at a time. Returns the index of the chosen option.
````
### askChooseMultiple

__askChooseMultiple(aPrompt, anArray, aMaxDisplay, aHelpText) : Array__

````
Stops for user interaction prompting aPrompt waiting for a single character to choose multiple from the provided anArray of options. Optionally you can provide aMaxDisplay to limit the number of options displayed at a time. Returns an array with the chosen options.
````
### askDef

__askDef(aInit, aQuestion, isSecret, isVoidable) : String__

````
If aInit is not defined will ask aQuestion (if isSecret = true it will askEncrypt) and return the value. If isVoidable = true and no answer is provided it will return undefined.
````
### askEncrypt

__askEncrypt(aPrompt) : String__

````
Similar to ask but the return user input will be encrypted. If an empty string is entered by the user the function will return undefined.
````
### askN

__askN(aPromptFn, aStopFn) : String__

````
Stops for a multi-line user interaction prompting, for each line, the result of calling aPromptFn that receives the current user input  (if a string is provided it will default to a function that returns that string). The interaction will stop when aStopFn function, that receives the current user input as an argument, returns true (if the function is not provided it will default to 3 new lines).
````
### askStruct

__askStruct(anArrayOfQuestions) : Array__

````
Given anArrayOfQuestions with a structure like:

[
 { name: "question1", prompt: "Question 1", type: "question" },
 { name: "question2", prompt: "Question 2", type: "secret" },
 { name: "question3", prompt: "Question 3", type: "char", options: "YN" },
 { name: "question4", prompt: "Question 4", type: "choose", options: ["Option 1", "Option 2", "Option 3"], output: "index" },
 { name: "question5", prompt: "Question 5", type: "multiple", options: ["Option 1", "Option 2", "Option 3"], max: 2 }
]

Will prompt the user for each question and return an array with the answers.

The type can be:

- "question" (default)
- "secret"
- "char" (requires options)
- "choose" (requires options)
- "multiple" (requires options)
````
### bcrypt

__bcrypt(aText, aVerifyHash, hashingRounds) : String/boolean__

````
If aText is provided it will return the resulting string of applying the bcrypt hash to aText. Optionally the bcrypt hashingRounds (between 4 and  31, default 10) can be provided (note: the more rounds, the more slower and secure). If aVerifyHash is provided it will return a boolean determining if the provided aVerifyHash (result of a previous bcrypt) matches the aText provided (hashingRounds will be ignored since the hash string already provides the rounds used).
````
### beautifier

__beautifier(anObject) : String__

````
Shortcut for the af.js2s function providing a human readable representation of the javascript object provided.
````
### beep

__beep()__

````
Tries to produce a beep sound.
````
### bprint

__bprint(aStr)__

````
"Beautifies" and prints the aStr to the stdout (with a new line on the end) (example: bprint("hello world!"))
````
### bprintErr

__bprintErr(aStr)__

````
"Beautifies" and prints the aStr to the stderr (with a new line on the end) (example: bprintErr("Hupps!! A problem!"))
````
### bprintErrnl

__bprintErrnl(aStr)__

````
"Beautifies" and prints the aStr to the stderr (without adding a new line on the end) (example: bprintErrnl("Hupps!! A problem!"))
````
### bprintnl

__bprintnl(aStr)__

````
"Beautifies" and prints the aStr to the stdout (without adding a new line on the end) (example: bprintnl("hello world!"))
````
### checkLatestVersion

__checkLatestVersion() : String__

````
Tries to determine what is the latest available version for OpenAF. Compare it with getVersion() to determine if you need an update.
````
### clone

__clone(anObject) : aClonedObject__

````
Creates a new copy of a JavaScript object.
````
### cls

__cls()__

````
Tries to clear the screen. The commands to try to clean the screen are given in ANSI.
````
### colorify

__colorify(aObject) : String__

````
Tries to ANSI colorify a json aObject for use with cprint, cprintErr, cprintErrnl and cprintnl
````
### compare

__compare(X, Y) : Boolean__

````
Compares a X object to a Y object at the content level. If they are equal the function will return true otherwise it will return false.
````
### compress

__compress(anObject) : ArrayOfBytes__

````
Compresses a JSON object into an array of bytes suitable to be uncompressed using the uncompress function.
````
### conReset

__conReset() : boolean__

````
Tries to reset the console to its original state. Returns true if successful.
````
### cprint

__cprint(aStr)__

````
"Stringifies" in ANSI color and prints the aStr to the stdout (with a new line on the end) (example: cprint("hello world!"))
````
### cprintErr

__cprintErr(aStr)__

````
"Stringifies" in ANSI color and prints the aStr to the stderr (with a new line on the end) (example: cprintErr("Hupps!! A problem!"))
````
### cprintErrnl

__cprintErrnl(aStr)__

````
"Stringifies" in ANSI color and prints the aStr to the stderr (with a new line on the end) (example: cprintErrnl("Hupps!! A problem!"))
````
### cprintnl

__cprintnl(aStr)__

````
"Stringifies" in ANSI color and prints the aStr to the stdout (with a new line on the end) (example: cprintnl("hello world!"))
````
### createDB

__createDB(aFile, aLogin, aPass) : DB__

````
Creates a DB object instantiated with a file based H2 database for the aFile provided. Optionally you can use aLogin and aPass(word).
````
### createDBInMem

__createDBInMem(aName, dontClose, aLogin, aPass, inMemFileSystem, inMemCompressed, useNIO) : DB__

````
Creates a DB object instantiated with an in-memory database for the given name. Optionally you can  specify that you don't want it to close on db.close (but all data will be lost on exiting OpenAF). Optionally you can also specify aLogin and aPass. This is a H2 database so do check more documentation on http://www.h2database.com/.  Also optionally you can specify if you want the in-memory database to be file based (inMemFileSystem) which  is slower than normal; to be compressed (inMemCompressed) which is slower than normal and inMemFileSystem; to store data outside the VM's heap (useNIO). Do note that if inMemFileSystem and inMemCompressed are selected only inMemCompressed will be used. And useNIO will only affect inMemFileSystem or inMemCompressed options.
````
### createDBServer

__createDBServer(aFile, aPort, aLogin, aPass) : DB__

````
Creates a DB object instantiated with a server based H2 database, on the provided aPort (defaults to 9090), for the aFile provided. Optionally you can use aLogin and aPass(word).
````
### csv.fromArray2File

__csv.fromArray2File(anArray, aFile, withHeadersOrStreamFormat) : Number__

````
Tries to wirte anArray to aFile. If withHeadersOrStreamFormat is provided, if an array it will  be interpreted as the files of headers otherwise as the new streamFormat object to use.
````
### csv.fromFile2Array

__csv.fromFile2Array(aFile, withHeadersOrStreamFormat) : Array__

````
Tries to read a CSV file and convert it into an array. If withHeadersOrStreamFormat is provided, if an array it will  be interpreted as the files of headers otherwise as the new streamFormat object to use.
````
### deleteFromArray

__deleteFromArray(anArray, anIndex) : Array__

````
Deletes the array element at anIndex from the provided anArray. Returns the new array with the element removed.
````
### descType

__descType(aObject) : String__

````
Given aObject will try to return the apparent type withing: undefined, null, bytearray, javaclass, java, boolean, array, number, string, function, date, map and object.
````
### dumpLog

__dumpLog() : Array__

````
Returns an array with collected log messages. Each entry has: d - timestamp; t - type; m - message.
````
### exit

__exit(anExitCode, force)__

````
Immediately exits execution with the provided exit code.  Optionally force=true can be provided but no shutdown triggers will be executed (use only as a last option)
````
### extend

__extend([deep], target [, object1][, objectN]) : Object__

````
Merges the contents of two or more objects together into the first object (target). If deep is specified the copy will be recursive. This function is equivalent to JQuery's extend function. See more in  https://api.jquery.com/jquery.extend/
````
### findRandomOpenPort

__findRandomOpenPort() : number__

````
Tries to find a random open port on all network interfaces. Useful to start network servers on an available port.
````
### flatten

__flatten(aObject, noKeyValSeparation) : Array__

````
Given aObject it will traverse it and create an array where each element will have a key and a val(ue). The key will  begin with a "." whenever it's a children key on aObject. This function is useful when trying to find specific keys or values across a Map. Optionally you can specify that you don't want each array element with the key and the value as separate elements but rather a directly as key and value.
````
### forkOpenAF

__forkOpenAF(aCommandLineArray, preCommandLineArray) : Promise__

````
Starts another OpenAF with the same command line, if aCommandLineArray is not provided.  If aCommandLineArray is provided each array element will be use sequentially to build the command line to start a new OpenAF instance. preCommandLineArray can be used to  provide java arguments if defined.
````
### genUUID

__genUUID(useSecureRandom) : String__

````
Generates and returns an UUID using a javascript algorithm (if needed you can refer to the  AF operation AF.KeyGenerator.GenerateUUID).
````
### getChLog

__getChLog() : Channel__

````
Returns the current log dump channel.
````
### getCPULoad

__getCPULoad(useAlternative) : Number__

````
Tries to obtain the current system load average (equivalent to top). If not available a negative value will be returned. Optionally you can specify to use the current system load if useAlternative = true. If the current system doesn't provide a load average it will fallback to the current system load.
````
### getDistribution

__getDistribution() : String__

````
Returns the current distribution channel for this version of OpenAF.
````
### getEnv

__getEnv(anEnvironmentVariable) : String__

````
Returns the current value of the operating system anEnvironmentVariable.
````
### getEnvs

__getEnvs() : Map__

````
Returns a map of key and values with the operating system environment variables.
````
### getEnvsDef

__getEnvsDef(aEnv, aVar, aDefault, isJson) : Object__

````
Given an environment variable aEnv name will check if a value is provided and return it if so. Otherwise it will check the value of aVar and return it if defined. If aVar is also not defined it will return aDefault. Optionally if isJson=true the value of the provided aEnv will be parsed from JSON or SLON.
````
### getFromZip

__getFromZip(aZipFile, aResource, inBytes, anEncoding, notInMemory) : anArrayOfBytes__

````
Retrieves aResource, as anArrayOfBytes, from aZipFile. This resource can be inBytes = true or not and anEncoding can be provided. If the resource to retrieve is big you can use notInMemory = true for a slower but less memory retrieval.
````
### getJavaStackTrace

__getJavaStackTrace(anException) : Array__

````
Given a javascript anException, if it's a wrapped or directly a java exception it will try to obtain the corresponding stack trace information in the form of an array.
````
### getNumberOfCores

__getNumberOfCores(realValue) : Number__

````
Try to identify the current number of cores on the system where the script is being executed.
````
### getOPackLocalDB

__getOPackLocalDB() : Array__

````
Returns an Array of maps. Each map element is an opack package description of the currently  locally, and per user, installed opack packages.
````
### getOPackPath

__getOPackPath(aPackage) : String__

````
Given aPackage name (a opack name) will search the opack and if installed will return the filesystem path where the opack is installed.
````
### getOPackPaths

__getOPackPaths() : Array__

````
Returns an array of strings with the paths for each of the installed opacks.
````
### getOPackRemoteDB

__getOPackRemoteDB() : Array__

````
Returns an Array of maps. Each map element is an opack package description registered in the OpenAF central repository.
````
### getOpenAFJar

__getOpenAFJar() : String__

````
Returns the complete filepath and name for the OpenAF jar file. (Shortcut for af.getOpenAFJar()). If __forcedOpenAFJar is defined the corresponding value will be used (useful when detection of the OpenAF jar doesn't work as expected or when OpenAF is embedded.
````
### getOpenAFPath

__getOpenAFPath() : String__

````
Returns the filesystem path to the openaf.jar currently being used for the script execution.
````
### getPid

__getPid() : String__

````
Tries to retrieve the current script execution operating system PID and returns it.
````
### getVersion

__getVersion() : String__

````
Shortcut for the af.getVersion (see more af.getVersion) function. Will return the current version of OpenAF being used.
````
### hmacSHA1

__hmacSHA1(data, key, toHex) : ArrayOfBytes__

````
Given data and a key will calculate the hash-based message authentication code (HMAC) using the SHA1 hash function. Optionally if toHex = true the output will be converted to hexadecimal lower case.
````
### hmacSHA256

__hmacSHA256(data, key, toHex) : ArrayOfBytes__

````
Given data and a key will calculate the hash-based message authentication code (HMAC) using the SHA256 hash function. Optionally if toHex = true the output will be converted to hexadecimal lower case.
````
### hmacSHA384

__hmacSHA384(data, key, toHex) : ArrayOfBytes__

````
Given data and a key will calculate the hash-based message authentication code (HMAC) using the SHA384 hash function. Optionally if toHex = true the output will be converted to hexadecimal lower case.
````
### hmacSHA512

__hmacSHA512(data, key, toHex) : ArrayOfBytes__

````
Given data and a key will calculate the hash-based message authentication code (HMAC) using the SHA512 hash function. Optionally if toHex = true the output will be converted to hexadecimal lower case.
````
### includeOPack

__includeOPack(aOPackName, aMinVersion)__

````
Ensures that aOPackName is installed. Optionally you can provide a minimal opack version. If the opack is not installed, can't be installed or cannot be updated to a version bigger or equal to aMinVersion an exception will be thrown.
````
### inherit

__inherit(Child, Parent)__

````
Associates a Child object to a Parent simulating a inheritance relationship. This is done by copying the Parent prototype to the Child prototype. This is similar to "Parent.call(this, arg1, arg2)"
````
### io.isBinaryFile

__io.isBinaryFile(aFile, confirmLimit) : boolean__

````
Tries to determine if the provided aFile is a binary or text file by checking the first 1024 chars (limit can be changed using confirmLimit). Returns true if file is believed to be binary. Based on the function isBinaryArray.
````
### io.listFilesTAR

__io.listFilesTAR(aTARfile, isGzip) : Array__

````
Given aTARfile (or output stream (with isGzip = true/false)) will return an array with the TAR file entries. Each entry will have: isDirectory (boolean), isFile (boolean), canonicalPath (string), filepath (string), filename (string), size (number), lastModified (date), groupId (string), group (string), userId (string) and user (string).
````
### io.lz4

__io.lz4(anInput) : bytes__

````
Compresses anInput using LZ4 compression and returns the compressed bytes.
````
### io.onDirEvent

__io.onDirEvent(aPath, aFn, aFnErr) : Promise__

````
Given aPath of a directory will return a promise ($do) that, for every create, modify or delete event that happens on aPath it will call aFn with two parameters: kind and filename.  The 'kind' string can be one of four events: ENTRY_CREATE, ENTRY_DELETE, ENTRY_MODIFY, OVERFLOW (meaning events were lost or discarded). The 'filename' represents the filename affected. Optionally aFnErr function can be provided to handle any errors and, in case aPath no longer exists, aFnErr will be called with the string "ENTRY_NA". Example:

var p = io.onDirEvent("myDir", (kind, filename) => {
   log("Event '" + kind + "' on '" + filename + "'");
}, e => {
   if (isString(e) && e == "ENTRY_NA") logWarn("myDir no longer exists."); else logErr(e);
});

$doWait(p);


````
### io.pipeCh

__io.pipeCh(aFunc)__

````
Starts a wait on stdin calling aFunc everytime a character is sent to stdin. The wait cycle breaks when aFunc returns true.
````
### io.pipeLn

__io.pipeLn(aFunc)__

````
Starts a wait on stdin calling aFunc everytime a line is sent to stdin. The wait cycle breaks when aFunc returns true.
````
### io.readFileBytesRO

__io.readFileBytesRO(aFile) : ByteArray__

````
Tries to read aFile in read-only mode (even if being used by another process) and returns the corresponding byte array.
````
### io.readFileJSON

__io.readFileJSON(aJSONFile) : Object__

````
Tries to read aJSONFile into a javascript object.
````
### io.readFileLZ4Stream

__io.readFileLZ4Stream(aFile) : InputStream__

````
Reads aFile as a LZ4 compressed stream and returns the InputStream to read from. This is useful to read large files that are compressed with LZ4 without decompressing them into memory.
````
### io.readFileTAR2Stream

__io.readFileTAR2Stream(aTARfile, isGzip, aFunc)__

````
Given aTARFile (or stream) will call aFunc(tion) with the corresponding Java TAR input stream. If aTARFile is a stream you should specify with isGzip = true/false if it has been "gzipped". Note: for direct usage use io.readFileTARStream
````
### io.readFileTARBytes

__io.readFileTARBytes(aTARFile, aFilePath, isGzip) : ByteArray__

````
Given aTARFile (or stream) will try to retrieve aFilePath and return the corresponding byte array. If aTARFile is a stream you should specify with isGzip = true/false if it has been "gzipped".
````
### io.readFileTARStream

__io.readFileTARStream(aTARFile, aFilePath, isGzip, aFunc)__

````
Given aTARFile (or stream) will try to retrieve aFilePath and call aFunc(tion) with the corresponding Java input stream. If aTARFile is a stream you should specify with isGzip = true/false if it has been "gzipped".
````
### io.readFileTOML

__io.readFileTOML(aFile) : Object__

````
Tries to read aFile and parse it as TOML into a javascript object.
````
### io.readFileYAML

__io.readFileYAML(aYAMLFile) : Object__

````
Tries to read aYAMLFile into a javascript object.
````
### io.readLinesNDJSON

__io.readLinesNDJSON(aNDJSONFile, aFuncCallback, aErrorCallback, anEncoding)__

````
Opens aNDJSONFile (a newline delimited JSON) (a filename or an input stream) as a stream call aFuncCallback with each parse JSON. If aFuncCallback returns true the cycle will be interrupted. For any parse error it calls the aErrorCallback  with each exception.
````
### io.readStreamJSON

__io.readStreamJSON(aJSONFile, aValFunc) : Map__

````
Reads a JSON file (aJSONFile) without loading all structures to memory (usefull to handling large JSON files). The aValFunc receives a single string argument with the current JSON path being processed (for example $.log.entries[123].request), where "$" is the root of the JSON document. When aValFunc returns true the current JSON structure is recorded in memory. If aValFunc is not defined it will return true for all paths. Returns the JSON structure recorded in memory.

Example:

   var amap = io.readStreamJSON("someFile.har",
                                path => (/^\$\.log\.entries\[\d+\]\.request/).test(path))


````
### io.unlz4

__io.unlz4(anInput) : Map/String__

````
Decompresses anInput using LZ4 compression and returns the decompressed map or string.
````
### io.unzip

__io.unzip(zipFile, targetDir, logFn, logErrFn)__

````
Tries to unzip a zipFile into targetDir. Optionally you can provide a logFn and logErrFn to log the progress. The logFn will receive the following object:

  { type: "file" | "dir", source: [zip entry], target: [targetPath] }


````
### io.writeFileJSON

__io.writeFileJSON(aJSONFile, aObj, aSpace)__

````
Tries to write a javascript aObj into a aJSONFile with an optional aSpace.
````
### io.writeFileTAR4Stream

__io.writeFileTAR4Stream(aTARfile, isGzip, aFunc)__

````
Given aTARfile (or output stream (with isGzip = true/false)) will call aFunc with the Java TAR output stream. Note: for direct usage use io.writeFileTARStream
````
### io.writeFileTARBytes

__io.writeFileTARBytes(aTARfile, aFilePath, isGzip, aArrayBytes)__

````
Given aTARfile (or output stream (with isGzip = true/false)) will write aArrayBytes into aFilePath in the TAR file/stream. Note: for multiple files use io.writeFileTARStream
````
### io.writeFileTARStream

__io.writeFileTARStream(aTARfile, isGzip, aFunc, aDefaultMap)__

````
Given aTARfile (or output stream (with isGzip = true/false)) will call aFunc(tion) providing, as argument, a writer function with three arguments: aFilePath, a Java input stream for the contents and the modification date for the target file.  Optionally aDefaultDate can be provided to be used whenever a date is not provided or for folders.
````
### io.writeFileTOML

__io.writeFileTOML(aFile, aObj)__

````
Tries to write aObj into aFile as TOML.
````
### io.writeFileYAML

__io.writeFileYAML(aYAMLFile, aObj, multidoc)__

````
Tries to write a javascript aObj into a aYAMLFile. If multiDoc = true and aJson is an array the output will be multi-document.
````
### io.writeLineNDJSON

__io.writeLineNDJSON(aNDJSONFile, aObj, aEncode)__

````
Writes aObj into a single line on aNDJSONFile (newline delimited JSON) (or an output stream). Optionally you can provide an encoding (only is a string filename is provided)
````
### io.zip

__io.zip(targetDir, zipFile, logFn, logErrFn)__

````
Tries to zip a targetDir into a zipFile. Optionally you can provide a logFn and logErrFn to log the progress. The logFn will receive the following object:

  { type: "file" | "dir", source: [io.listFile entry], target: [targetPath] }


````
### ioSetNIO

__ioSetNIO(aFlag)__

````
Sets the default use of NIO in ioStream* functions. It's overridden if the ioStream* function defines a value for the useNIO function argument.
````
### ioStreamCopy

__ioStreamCopy(aOutputStream, aInputStream)__

````
Copies the contents of a Java aInputStream to a Java aOutputStream. The two streams will  be closed in the end.
````
### ioStreamRead

__ioStreamRead(aStream, aFunction, aBufferSize, useNIO, encoding)__

````
Given a Java input or output stream helps to read strings by using aFunction with a string argument for each buffer size  (default 1024 characters). Optionally you can provide a different aBufferSize (default: 1024) and/or also specify that  Java NIO functionality should be used. If aFunction returns true the read operation stops.
````
### ioStreamReadBytes

__ioStreamReadBytes(aStream, aFunction, aBufferSize, useNIO)__

````
Given a Java input or output stream helps to read an array of bytes by using aFunction with anArrayOfBytes argument for  each buffer size (default 1024 characters). Optionally you can provide a different aBufferSize (default: 1024) and/or  also specify that Java NIO functionality should be used. If aFunction returns true the read operation stops.
````
### ioStreamReadLines

__ioStreamReadLines(aStream, aFunctionPerLine, aSeparator, useNIO, anEncoding)__

````
Given aStream will read the entire buffer and call aFunctionPerLine(withALine) per each \n found. Aditionally you can specify a different aSeparator for each line other than "\n".  If aFunctionPerLine returns true the read operation stops. Optionally you can also provide anEncoding.
````
### ioStreamWrite

__ioStreamWrite(aStream, aString, aBufferSize, useNIO)__

````
Given a Java input or output stream helps to write aString into the same. Optionally you can provide a different aBufferSize (default: 1024) and/or also specify that Java NIO functionality should be used.
````
### ioStreamWriteBytes

__ioStreamWriteBytes(aStream, aArrayBytes, aBufferSize, useNIO)__

````
Given a Java input or output stream helps to write aArrayBytes into the same. Optionally you can provide a different aBufferSize (default: 1024) and/or also specify that Java NIO functionality should be used.
````
### isArray

__isArray(aObj) : boolean__

````
Returns true if aObj is an array, false otherwise.
````
### isBinaryArray

__isBinaryArray(anArrayOfChars, confirmLimit, previousResult) : boolean__

````
Tries to determine if the provided anArrayOfChars is binary or text. The detection is performed with the first 1024 chars ( that can be changed if confirmLimit is provided). Additionally is possible to link multiple calls providing the last result on previousResult for multiple subsequences of a main array of chars sequence. Should work for utf8, iso-8859-1, iso-8859-7,  windows-1252 and windows-1253. Returns true if file is believed to be binary.
````
### isBoolean

__isBoolean(aObj) : boolean__

````
Returns true if aObj is boolean, false otherwise
````
### isByteArray

__isByteArray(aObj) : boolean__

````
Returns true if aObj is a byte array object, false otherwise.
````
### isDate

__isDate(aObj) : boolean__

````
Returns true if aObj is a date, false otherwise
````
### isDecimal

__isDecimal(aObj) : boolean__

````
Returns true if aObj has a decimal component.
````
### isDef

__isDef(aObject) : boolean__

````
Returns true if the provided aObject is defined as a javascript variable. It will return false otherwise. (see also isUnDef). Shortcut for the isDefined function.
````
### isDefined

__isDefined(aObject) : boolean__

````
Returns true if the provided aObject is defined as a javascript variable. It will return false otherwise. (see also isUndefined)
````
### isFunction

__isFunction(aObj) : boolean__

````
Returns true if aObj is a function, false otherwise;
````
### isInteger

__isInteger(aObj) : boolean__

````
Returns true if aObj doesn't have a decimal component.
````
### isJavaArray

__isJavaArray(aObj) : boolean__

````
Returns true if aObj is a Java array, false otherwise
````
### isJavaClass

__isJavaClass(aObj) : boolean__

````
Return true if aObj is a Java class, false otherwise
````
### isJavaException

__isJavaException(aObject) : boolean__

````
Determines if aObject is a java exception object or a javascript exception with an embeeded java exception.
````
### isJavaObject

__isJavaObject(aObj) : boolean__

````
Returns true if aObj is a Java object, false otherwise
````
### isMap

__isMap(aObj) : boolean__

````
Returns true if aObj is a map, false otherwise.
````
### isNull

__isNull(aObj) : boolean__

````
Returns true if aObj is null, false otherwise
````
### isNumber

__isNumber(aObj) : boolean__

````
Returns true if aObj can be a number, false otherwise
````
### isObject

__isObject(aObj) : boolean__

````
Returns true if aObj is an object, false otherwise;
````
### isString

__isString(aObj) : boolean__

````
Returns true if aObj is a string, false otherwise
````
### isTNumber

__isTNumber(aObj) : boolean__

````
Returns true if aObj is of type number, false otherwise
````
### isUnDef

__isUnDef(aObject) : boolean__

````
Returns true if the provided aObject is undefined as a javascript variable. It will return false otherwise. (see also isDef). Shortcut for the isUndefined function.
````
### isUndefined

__isUndefined(aObject) : boolean__

````
Returns true if the provided aObject is undefined as a javascript variable. It will return false otherwise. (see also isDefined)
````
### isUUID

__isUUID(aObj) : boolean__

````
Returns true if aObj is an UUID.
````
### javaRegExp

__javaRegExp(text).test(regExp, mods) : boolean__

````
Mimics, using Java, the javascript RegExp test function. Supported mods are "g", "m" and "i" or the java integer composed  mods. Returns the corresponding boolean value.
````
### jsonParse

__jsonParse(aString, alternative, unsafe, ignoreNonJson) : Map__

````
Shorcut for the native JSON.parse that returns an empty map if aString is not defined, empty or unparsable.
````
### listFilesRecursive

__listFilesRecursive(aPath, usePosix, aFnErr) : Map__

````
Performs the io.listFiles function recursively given aPath. The returned map will be equivalent to the io.listFiles function (see more in io.listFiles). Alternatively you can specify to usePosix=true and it will add to the map the owner, group and full permissions of each file and folder. When __flags.ALTERNATIVES.listFilesRecursive=true the processing will be done in parallel and aFnErr will be called in case of an error.
````
### load

__load(aScript)__

````
Provides a shortcut for the af.load function (see more af.load). If the provided aScript is not found this function will try to search the script on the openaf.jar::js folder and on the installed opacks. If it doesn't find the provided aScript it will throw an exception "Couldn't find aScript".
````
### loadCompiled

__loadCompiled(aScript, dontCompile, dontLoad) : boolean__

````
Tries to load an OpenAF script as a compiled class. If a compiled class file doesn't exist in the same path  it will try to compile and load from the compiled code. If a compiled class file exists in the same path it will recompile it if the modified date of the original aScript is newer than the class.  If the class was already loaded or can't be loaded it will return false. Returns true otherwise. Optionally you can force to not compile dontCompile=true or just to compile with dontLoad=true
````
### loadCompiledLib

__loadCompiledLib(aLibClass, forceReload, aFunction, withSync) : boolean__

````
Loads the corresponding compiled javascript library class and keeps track if it was already loaded or not (in __loadedLibs). Optionally you can force reload and provide aFunction to execute after the successful loading. Returns true if successfull, false otherwise.
````
### loadDBInMem

__loadDBInMem(aDB, aFilename)__

````
Tries to load to a in-memory database, aDB object, previously created by the function createDBInMem from a SQL aFilename probably created by the function persistDBInMem.
````
### loadDiff

__loadDiff()__

````
Loads the JsDiff javascript library into scope (check https://github.com/kpdecker/jsdiff).
````
### loadExternalJars

__loadExternalJars(aPath, dontCheck)__

````
Given a path will try to add to the current classpath (using af.externalAddClasspath) all files with the extension '.jar'. Optionally you can override the dontCheck if it was loaded with this command previously.
````
### loadFuse

__loadFuse()__

````
Loads the FuseJS javascript library into scope.

See more in: http://fusejs.io/
````
### loadHandlebars

__loadHandlebars()__

````
Loads the Handlebars javascript library into scope. Example:

loadHandlebards();
var source = "<m>{{#each lines}}\t<s name=\"{{key}}\">{{value}}</s>\n{{/each}}\n</m>";
var data = { "lines": [ { "name": "n1", "value": "v1" }, { "name": "n2", "value": "v2" } ] };
var template = Handlebars.compile(source);
print(template(data));
data.lines.push({"name": "n3", "value": "v3"});
print(template(data));

See more documentation in: http://handlebarsjs.com/


````
### loadHelp

__loadHelp()__

````
Loads into scope the ODoc objects for documentation support.
````
### loadJSYAML

__loadJSYAML()__

````
Loads the JS-YAML library.
````
### loadLib

__loadLib(aLib, forceReload, aFunction) : boolean__

````
Loads the corresponding javascript library and keeps track if it was already loaded or not (in __loadedLibs). Optionally you can force reload and provide aFunction to execute after the successful loading. Returns true if successfull, false otherwise.
````
### loadLodash

__loadLodash()__

````
Loads the loadash javascript library.

See more in https://lodash.com/docs
````
### loadOAFP

__loadOAFP()__

````
Loads the OpenAF processor that can be used with the function oafp. Example:

# Thread unsafe example
oafp({ data: "(abc: 123, xyz: 456)", out: "pm" })
sprint(__pm._map)

# Thread safe example
oafp({ data: "(abc: 123, xyz: 456)", out: "key", __key: "myresult" })
sprint($get("myresult"))


````
### loadPy

__loadPy(aPyScript, aInput, aOutputArray, dontStop) : Map__

````
Provides a shortcut for the $py function (see more in $py). If the provided aPyScript is not found this function will try to search the python script on the installed opacks. If it doesn't find the provided aScript it will throw an exception "Couldn't find aPyScript". If aInput map is defined each entry will be converted into python variables. If aOutputArray is defined the python variables string names in the array will be returned as a map.
````
### loadUnderscore

__loadUnderscore()__

````
Loads the Underscore javascript library into scope (using the loadash alternative).

See more in: http://underscorejs.org and https://lodash.com/docs
````
### log

__log(msg, formatOptions)__

````
Outputs to the current stdout a line composed of the current date, indication of INFO and the provided msg. Optionally you can provide a formatOptions map for overriding the defaults from setLog. Note: you can use startLog, stopLog and dumpLog to keep an internal record of theses messages.
````
### logErr

__logErr(msg, formatOptions)__

````
Outputs to the current stderr a line composed of the current date, indication of ERROR and the provided msg. Optionally you can provide a formatOptions map for overriding the defaults from setLog. Note: you can use startLog, stopLog and dumpLog to keep an internal record of theses messages.
````
### logFlush

__logFlush(aTimeout)__

````
Will wait for the current log promise to finish. Optionally you can provide aTimeout in milliseconds.
````
### lognl

__lognl(msg, formatOptions)__

````
Outputs to the current stdout, without a new line, a sentence composed of the current date, indication of INFO and the provided msg. Optionally you can provide a formatOptions map for overriding the defaults from setLog. Note: you can use startLog, stopLog and dumpLog to keep an internal record of theses messages.
````
### logWarn

__logWarn(msg, formatOptions)__

````
Outputs to the current warning in a line composed of the current date, indication of WARN and the provided msg. Optionally you can provide a formatOptions map for overriding the defaults from setLog. Note: you can use startLog, stopLog and dumpLog to keep an internal record of theses messages.
````
### lprint

__lprint(aStr, withColor)__

````
"SLONs" and prints the aStr to the stdout (with a new line on the end)
````
### lprintErr

__lprintErr(aStr, withColor)__

````
"SLONs" and prints the aStr to the stderr (with a new line on the end)
````
### lprintErrnl

__lprintErrnl(aStr, withColor)__

````
"SLONs" and prints the aStr to the stderr (without adding a new line on the end)
````
### lprintnl

__lprintnl(aStr, withColor)__

````
"SLONs" and prints the aStr to the stdout (without adding a new line on the end)
````
### mapArray

__mapArray(anArray, selectors, limit) : Array__

````
Helper functions to map selectors (inputs for ow.obj.getPath) from anArray returning the filtered array. IF selectors is a string or just one array entry the result will be an array with just the value results. Optionally you can also limit the number of results to the first "limit" (number).
````
### md2

__md2(anObject) : String__

````
Will return of the MD2 in hexadecimal format for a given anObject.
For files you can provide a file stream: var s = io.readFileStream(getOpenAFJar()); md2(s); s.close()
````
### md5

__md5(anObject) : String__

````
Will return of the MD5 in hexadecimal format for a given anObject.
For files you can provide a file stream: var s = io.readFileStream(getOpenAFJar()); md5(s); s.close()
````
### merge

__merge(anObjectA, anObjectB) : aMergedObject__

````
Merges a JavaScript object A with a JavaScript object B a returns the result as a new object.
````
### newFn

__newFn() : Function__

````
Builds a new Function handling any debug needs if necessary.
````
### newJavaArray

__newJavaArray(aJavaClass, aSize) : JavaArrayClass__

````
Creates a new Java Array object for the aJavaClass type for a provided aSize.

Examples:

newJavaArray(java.lang.String, 5);
newJavaArray(java.lang.Integer.TYPE, 2);


````
### now

__now() : Number__

````
Will return the current system time in milliseconds.
````
### nowE

__nowE() : Number__

````
Returns the current epoch time in seconds.
````
### nowNano

__nowNano() : Number__

````
Will return the current system time in nanoseconds.
````
### nowNanoE

__nowNanoE() : Number__

````
Returns the current epoch time in nanoseconds.
````
### nowTZ

__nowTZ() : Number__

````
Returns the same as now() but adjusted with the local timezone offset.
````
### nowUTC

__nowUTC() : Number__

````
Will return the current system time in milliseconds.
````
### objOrStr

__objOrStr(aObj, aStr) : String__

````
Given aObj (a map or an array) will try to assess if aStr is an aObj key (using $$.get). If yes, it will return the corresponding aObj value otherwise it will return aStr.
````
### oJob

__oJob(aFile, args, aId, aOptionsMap, shouldReturn)__

````
Shortcut for oJobRunFile return the result on the variable __pm. Keep in mind that it doesn't support concurrency. If shouldReturn is true it will return the result (from ow.oJob.output if used) of the job instead of the __pm variable.
````
### oJobRun

__oJobRun(aJson, args, aId)__

````
Runs a oJob from aJson definition with the provided args (arguments). Optionally you can provide aId to segment these specific jobs.
````
### oJobRunFile

__oJobRunFile(aFile, args, aId, aOptionsMap, isSubJob)__

````
Runs a oJob aFile with the provided args (arguments). Optionally you can provide aId to segment these specific jobs.
````
### oJobRunFileAsync

__oJobRunFileAsync(aFile, args, aId, aOptionsMap, isSubJob) : oPromise__

````
Runs a oJob aFile async with the provided args (arguments). Optionally you can provide aId to segment these specific jobs. Returns the corresponding promise.
````
### oJobRunJob

__oJobRunJob(aJob, args, aId, waitForFinish) : boolean__

````
Shortcut for ow.oJob.runJob. Please see help for ow.oJob.runJob. Optionally you can provide aId to segment this specific job. If aJob is a string it will try to retrieve the job from the jobs channel. Returns true if the job executed or false otherwise (e.g. failed deps).
````
### oJobRunJobAsync

__oJobRunJobAsync(aJob, args, aId) : oPromise__

````
Creates an oPromise to run the same arguments for oJobRunJob thus executing the job async. Returns the generate oPromise.
````
### oPack

__oPack(aParameters)__

````
Tries to execute oPack with aParameters string. These string is equivalent to the opack command-line commands. aParameters = "help" will, for example, print all the help information.
````
### opackExec

__opackExec(aPackageName)__

````
Tries to execute the provided opack aPackageName.
````
### openInBrowser

__openInBrowser(anURL) : Boolean__

````
Tries to open anURL on the current OS desktop browser. Returns false if it's unable to open the OS desktop browser for some reason.
````
### oPromise

__oPromise(aFunction, aRejFunction, useVirtualThreads) : oPromise__

````
Custom Promise-like implementation. If you provide aFunction, this aFunction will be executed async in a thread and oPromise object will be immediatelly returned. Optionally this aFunction can receive a resolve and reject functions for to you use inside aFunction to provide a result with resolve(aResult) or an exception with reject(aReason). If you don't call theses functions the returned value will be used for resolve or any exception thrown will be use for reject. You can use the "then" method to add more aFunction that will execute once the previous as executed successfully (in a stack fashion). The return/resolve value from the  previous function will be passed as the value for the second. You can use the "catch" method to add aFunction that will receive a string or exception for any exception thrown with the reject functions. You can also provide a aRejFunction that works like a "catch" method as previously described.  Optionally if useVirtualThreads is true, the aFunction will be executed in a virtual thread, otherwise it will be executed in a normal thread.
````
### oPromise.all

__oPromise.all(anArray) : oPromise__

````
Returns an oPromise that will be resolved when all oPromise part of the anArray are fullfiled. If any of the oPromises fails/rejects the returned oPromise will also be rejected/fail.
````
### oPromise.catch

__oPromise.catch(onReject) : oPromise__

````
Adds onRejected to the current oPromise stack to execute if the previous function was rejected and receives the reason as parameter.
````
### oPromise.race

__oPromise.race(anArray) : oPromise__

````
Returns an oPromise that will be resolved when any oPromise part of the anArray is fullfiled. If any of the oPromises fails/rejects the returned oPromise will also be rejected/fail.
````
### oPromise.then

__oPromise.then(onFulfilled, onRejected) : oPromise__

````
Adds onFulfilled to the current oPromise stack to execute if the previous function was resolved successfully and receives the resolve/return value as parameter. Also adds onRejected to the current oPromise stack to execute if the previous function was rejected and receives the reason as parameter.
````
### ow.loadAI

__ow.loadAI()__

````
Loads OpenWrap AI functionality.
````
### ow.loadCh

__ow.loadCh()__

````
Loads OpenWrap channels functionality.
````
### ow.loadDebug

__ow.loadDebug()__

````
Loads OpenWrap debug functionality.
````
### ow.loadDev

__ow.loadDev()__

````
Loads OpenWrap dev functionality. Basically functions being tested.
````
### ow.loadFormat

__ow.loadFormat()__

````
Loads OpenWrap format functionality. Basically functions to help with the formatting of strings, numbers, dates, etc...
````
### ow.loadJava

__ow.loadJava()__

````
Loads OpenWrap Java functionality.
````
### ow.loadMetrics

__ow.loadMetrics()__

````
Loads OpenWrap Metrics functionality. Basically functions to wrap access to server functionality.
````
### ow.loadNet

__ow.loadNet()__

````
Loads OpenWrap net functionality. Basically functions for net.
````
### ow.loadObj

__ow.loadObj()__

````
Loads OpenWrap object functionality.
````
### ow.loadOBook

__ow.loadOBook()__

````
Loads OpenWrap oBook functionality.
````
### ow.loadOJob

__ow.loadOJob()__

````
Loads OpenWrap oJob functionality.
````
### ow.loadPython

__ow.loadPython()__

````
Loads OpenWrap Python functionality.
````
### ow.loadSec

__ow.loadSec()__

````
Loads OpenWrap sec functionality. Basically functions for sec.
````
### ow.loadServer

__ow.loadServer()__

````
Loads OpenWrap Server functionality. Basically functions to wrap access to server functionality.
````
### ow.loadTemplate

__ow.loadTemplate()__

````
Loads OpenWrap template functionality. Basically functions to wrap access to Handlebars functionality.
````
### ow.loadTest

__ow.loadTest()__

````
Loads OpenWrap test functionality. Basically functions to unit test other functionality.
````
### parallel

__parallel(aFunction, numThreads, aAggFunction, aControlMap) : Object__

````
Executes a function in a specific number of threads (each function will receive a corresponding uuid).  The returned result of each function execution is kept in an array. If no aAggFunction is provided this array will be returned, otherwise the array will be passed to the aAggFunction for processing and the corresponding result of aAggFunction will be returned. If no numThreads is provided, the number of threads will be automatically determined. Optionally you can provide a empty map as aControlMap that it will be filled with aControlMap.__threads with the  threads object, the aControlMap.__numThreads for the number of threads in use and a thread __uuid list.
````
### parallel4Array

__parallel4Array(anArray, aFunction, numThreads, aControlMap) : Object__

````
Given anArray, divides it in subsets for processing in a specific number of threads. In each thread aFunction(aValue) will be executed for each value in sequence. An array with all the aFunction results will be returned. If no numThreads is  provided, the number of threads will be automatically determined. Optionally you can provide a empty map as aControlMap that it will be filled with aControlMap.__threads with the threads object, the aControlMap.__numThreads for the number of threads in use and a thread __uuid list. Example:

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

````
### parallelArray

__parallelArray(anArray, aReduceFunction, initValue, aAggFunction, numThreads, aControlMap) : Object__

````
Given anArray, divides it in subsets for processing in a specific number of threads. In each thread aReduceFunction(pr, cv, i, arr), where pr = previous result, cv = current value, i = index and arr = array subset, will be executed for each value in sequence. The pr value for the first execution on each thread will have the value initValue if provided. The returned result, in each thread, will be placed into an array. If aAggFunction is defined, the resulting array will be passed to the aAggFunction for processing and the corresponding result of aAggFunction will be returned. If no numThreads is provided, the number of threads will be  automatically determined. Optionally you can provide a empty map as aControlMap that it will be filled with aControlMap.__threads with the threads object, the aControlMap.__numThreads for the number of threads in use and a thread __uuid list.
````
### persistDBInMem

__persistDBInMem(aDB, aFilename) : Array__

````
Tries to persist a in-memory database, aDB object, previously created by the function createDBInMem into a SQL aFilename. This can later be used to load again using the loadDBInMem function.
````
### pForEach

__pForEach(anArray, aFn, aErrFn, aUseSeq) : Array__

````
Given anArray, divides it in subsets for processing in a specific number of threads. In each thread aFn(aValue, index) will be executed for each value in sequence. The results of each aFn will be returned in the same order as the original array. If an error occurs during the execution of aFn, aErrFn will be called with the error. If aUseSeq is true the sequential execution will be forced.

Example:

var res = pForEach(thingsToProcess,
  function(aValue, index) {
    return processValue(aValue)
  },
  function(e) {
    printErr(e)
  } )

````
### pidCheck

__pidCheck(aPid) : Boolean__

````
Verifies if aPid is running (returning true) or not (returning false).
````
### pidCheckIn

__pidCheckIn(aFilename) : boolean__

````
Uses the contents of aFilename to determine if there is an existing process running with the pid  recorded on the file. If it's running it will return false, if not it will return true and record the current pid on the aFilename. The function pidCheckOut will be added as a hook to run on the  end of the current process.
````
### pidCheckOut

__pidCheckOut(aFilename) : boolean__

````
Removes the pid information from aFilename and deletes the file if possible.  If successful returns true, if not returns false.
````
### pidKill

__pidKill(aPidNumber, isForce) : boolean__

````
Tries to terminate a process with aPidNumber. If successful it will return true otherwise it will return false. If necessary, a boolean true value on isForce, will force the termination of the process.
````
### plugin

__plugin(aPlugin, aClass)__

````
Provides a shortcut for the af.plugin function. It also provides a shortcut for plugins with the java package "openaf.plugins" (e.g. af.plugin("openaf.plugins.HTTP") is the same as plugin("HTTP")). In alternative you can provide plugin aClass if it's different from aPlugin.
````
### pods.declare

__pods.declare(aId, exports)__

````
Declares a new module, aId, as the provided exports literal.
````
### pods.define

__pods.define(aId, aDepsArray, aFactoryFunction)__

````
Defines a new module given aId, aDepsArray with depend id modules and a factory function.
````
### pods.require

__pods.require(aIds, aCallbackFunction)__

````
Requires a module or a list of modules and all of its dependencies. Optionally you can provide aCallbackFunction to inject the required modules into.
````
### print

__print(aStr)__

````
Prints the aStr to the stdout (with a new line on the end) (example: print("hello world!"))
````
### printBars

__printBars(aFormatString, hSize, aMax, aMin, aIndicatorChar, aSpaceChar) : String__

````
Produces horizontal bars given aFormatString, a hSize (horizontal max size), aMax (the axis max value) and aMin  (the axis min value). The aFormatString should be composed of "<units> [<function[:color][:legend]> ...]":

   The units can be: int, dec1, dec2, dec3, dec, bytes and si;
   Each function should return the corresponding current value (optionally it can be a number directly);
   Optionally each color should use any combinations similar to ansiColor (check 'help ansiColor');
   Optionally each legend, if used, will be included in a bottom legend;


````
### printChart

__printChart(aFormatString, hSize, vSize, aMax, aMin, dColor) : String__

````
Produces a line chart given aFormatString, a hSize (horizontal max size), a vSize (vertical max size), aMax (the axis max value) and aMin  (the axis min value). The aFormatString should be composed of "<dataset> <units> [<function[:color][:legend]> ...]":

   The dataset should be an unique name (data can be cleaned with ow.format.string.dataClean);
   The units can be: int, dec1, dec2, dec3, dec4, dec, bytes and si;
   Each function should return the corresponding current value (optionally it can be a number directly);
   Optionally each color should use any combinations similar to ansiColor (check 'help ansiColor');
   Optionally each legend, if used, will be included in a bottom legend;

   If function "-min" it will overwrite the aMin
   If function "-max" it will overwrite the aMax
   If function "-hsize" it will overwrite the hSize
   If function "-vsize" it will overwrite the vSize


````
### printErr

__printErr(aStr)__

````
Prints the aStr to the stderr (with a new line on the end) (example: printErr("Hupps!! A problem!"))
````
### printErrnl

__printErrnl(aStr)__

````
Prints the aStr to the stderr (without adding a new line on the end) (example: printErrnl("Hupps!! A problem!"))
````
### printMap

__printMap(aMap, aWidth, aTheme, useAnsi) : String__

````
Returns a ASCII map representation of aMap optionally with a give aWidth, aTheme and/or useAnsi boolean. aTheme can be "utf" or "plain" depending on the terminal capabilities.
````
### printnl

__printnl(aStr)__

````
Prints the aStr to the stdout (without adding a new line on the end) (example: printnl("hello world!"))
````
### printTable

__printTable(anArrayOfEntries, aWidthLimit, displayCount, useAnsi, aTheme, aBgColor, wordWrap, useRowSep, bandRows) : String__

````
Returns a ASCII table representation of anArrayOfEntries where each entry is a Map with the same keys. Optionally you can specify aWidthLimit, useAnsi, bandRows and/or aBgColor. If you want to include a count of rows just use displayCount = true. If useAnsi = true you can provide a theme (e.g. "utf" or "plain")
````
### printTree

__printTree(aObj, aWidth, aOptions) : String__

````
Given aObj(ect) will return a tree with the object elements. Optionaly you can specificy aWidth and/or aOptions: noansi (boolean) no ansi character sequences, curved (boolean) for UTF curved characters, wordWrap (boolean) to wrap long string values, compact (boolean) to compact tree lines, fullKeySize (boolean) to pad the each entry key, fullValSize (boolean) to pad the entire key and value and withValues (boolean) to include or not each key values
````
### printTreeOrS

__printTreeOrS(aObj, aWidth, aOptions) : String__

````
Tries to use printTree with the provided arguments. In case printTree throws an exception (like insufficient width) if will fallback to colorify or stringify (if the noansi option is true).
````
### processExpr

__processExpr(aSeparator, ignoreCase, aSource) : Map__

````
Will access the current contents of the OpenAF -e argument (if a different aSource is not defined) looking for pairs of key values in the form "a=5;b=1;c=xpto\\;" and will produce a Map with { "a": 5, "b": 1, "c": "xpto;" }. If no aSeparator is provided ';' will be assumed. __pmIn values will be also included. If ignoreCase = true all keys will be lower cased.
````
### quickSort

__quickSort(items, aCompareFunction) : Array__

````
Performs a quick sort algorithm on the items array provided. Optionally aCompareFunction can be provided. The sorted array will be returned.
````
### range

__range(aCount, aStart, aStep) : Array__

````
Generates an array with aCount of numbers starting at 1. Optionally you can provide a different aStart number and/or aStep increment.
````
### repeat

__repeat(nTimes, aStr) : String__

````
Will build a string composed of aStr repeated nTimes.
````
### require

__require(aScript) : Object__

````
Will try to load aScript from the directories specified in the loadRequire function (by default all opack directories plus the current working directory). Returns the exports object manipulated in aScript (note: results are cached)
````
### requireCompiled

__requireCompiled(aScript, dontCompile, dontLoad) : Object__

````
Loads aScript, through require, previously compile or it will be compiled if (dontCompile is not true). IF dontLoad = true the module exports won't be returned.
````
### restartOpenAF

__restartOpenAF(aCommandLineArray, preCommandLineArray)__

````
Terminates the current OpenAF execution and tries to start a new with the same command line, if aCommandLineArray is not provided. If aCommandLineArray is provided each array element will be use sequentially to build the command line to start a new OpenAF instance.  preCommandLineArray can be used to provide java arguments if defined.
````
### saveHelp

__saveHelp(aPath, aMapOfFiles)__

````
Given aMapOfFiles, or basically an array of JavaScript or Java source filenames, each file will  be processed for ODoc XML tags and the corresponding ODoc database will be generated on the  provided aPath suitable for offline use.
````
### saveHelpWeb

__saveHelpWeb(aPath, aMapOfFiles)__

````
Given aMapOfFiles, or basically an array of JavaScript or Java source filenames, each file will  be processed for ODoc XML tags and the corresponding ODoc database will be generated on the  provided aPath suitable for online use.
````
### searchArray

__searchArray(anArray, aPartialMap, useRegEx, ignoreCase, useParallel) : Array__

````
Shortcut to ow.obj.searchArray.
````
### searchHelp

__searchHelp(aTerm, aPath, anArrayOfIds) : Map__

````
Searches the OpenAF ODoc help system for a specific term. Optionally you can provide a path of where to  search for ODoc help files. If an exact match is found the function will return an array with a single a map with the corresponding ODoc id, key, fullkey and text. If no exact match is found the function will return an array of alternative matches or an empty array if no alternatives are found. Optionally you can also restrict by anArrayOfIds.
````
### searchKeys

__searchKeys(aObject, aSearchKey, useCase, actFunc) : Map__

````
Traverses aObject looking for key matches, ignoring case if useCase is true, of the regular expression aSearchKey. Each element found is added to the returned Map. The element key will represent the path from aObject to it. Tip: The actFunc  can use ow.obj.setPath to replace a value: "(key, value, path) => { ow.obj.setPath(aObject, path + '.' + key, replaceValue); }"
````
### searchValues

__searchValues(aObject, aSearchValue, useCase, actFunc) : Map__

````
Traverse aObject looking for value matches, ignoring case if useCase is true, of the regular expression aSearchKey.  Each value found is added to the returned Map linked to the path representation of where it was found. Optionally you can provide an actFunc that receives the key, value and path. Tip: The actFunc can use ow.obj.setPath to  replace a value: "(key, value, path) => { ow.obj.setPath(aObject, path + '.' + key, replaceValue); }"
````
### setLog

__setLog(aMap)__

````
Sets the current log output settings:

- off        (boolean) Turns off output to stdout/stderr
- offInfo    (boolean) Turns off output of INFO
- offError   (boolean) Turns off output of ERROR
- offWarn    (boolean) Turns off output of WARN
- dateFormat (string)  ow.format.fromDate format for date
- dateTZ     (string)  Time zone to use with ow.format.fromDate
- separator  (string)  String to use as separator
- async      (boolean) Run in async mode
- profile    (boolean) Gathers memory and system load stats
- format     (string)  Sets the format to output logs (e.g. json, slon, human)


````
### setOfflineHelp

__setOfflineHelp(aBoolean)__

````
Forces help (odoc) to be retrieved locally (if aBoolean is true) or reestablishes the normal behaviour of retrieving from online first (if aBoolean is false)
````
### sh

__sh(commandArguments, aStdIn, aTimeout, shouldInheritIO, aDirectory, returnMap, callbackFunc, anEncoding, dontWait, envsMap) : String__

````
Tries to execute commandArguments (either a String or an array of strings) in the operating system as a shortcut for  AF.sh except that it will run them through the OS shell. Optionally aStdIn can be provided, aTimeout can be defined  for the execution and if shouldInheritIO is true the stdout, stderr and stdin will be inherit from OpenAF. If  shouldInheritIO is not defined or false it will return the stdout of the command execution. It's possible also to  provide a different working aDirectory. If envsMap (a map of strings) is defined the environment variables will be replaced by envsMap. The variables __exitcode and __stderr can be checked for the command exit code and the stderr output correspondingly. In alternative if returnMap = true a map will be returned with stdout, stderr and exitcode. A callbackFunc can be provided, if shouldInheritIO is undefined or false, that will receive, as parameters, an output  stream, a error stream and an input stream (see help af.sh for an example). If defined the stdout and stderr won't be available for the returnMap if true.
````
### sha1

__sha1(anObject) : String__

````
Will return of the SHA-1 in hexadecimal format for a given anObject.
For files you can provide a file stream: var s = io.readFileStream(getOpenAFJar()); sha1(s); s.close()
````
### sha256

__sha256(anObject) : String__

````
Will return of the SHA-256 in hexadecimal format for a given anObject.
For files you can provide a file stream: var s = io.readFileStream(getOpenAFJar()); sha256(s); s.close()
````
### sha384

__sha384(anObject) : String__

````
Will return of the SHA-384 in hexadecimal format for a given anObject.
For files you can provide a file stream: var s = io.readFileStream(getOpenAFJar()); sha384(s); s.close()
````
### sha512

__sha512(anObject) : String__

````
Will return of the SHA-512 in hexadecimal format for a given anObject.
For files you can provide a file stream: var s = io.readFileStream(getOpenAFJar()); sha512(s); s.close()
````
### showH2Console

__showH2Console() : Console__

````
Instantiates and returns a H2 Console object openning a browser (if possible) to interact with the H2 Console. With  the returned object you can later invoke .shutdown() or unload it from the console. Invoking a second time will result in a port bind error since it the first instance wasn't shutdown.
````
### sleep

__sleep(millis, shouldCheck)__

````
Shortcut for af.sleep function. Will pause execution for a given period of time expressed in milliseconds. If shouldCheck is true it will enforce checking if the time has really passed or not.
````
### sortMapKeys

__sortMapKeys(aMap, moreLevels) : Map__

````
Tries to sort the first level map keys returning the rewritten map.  If moreLevels=true it will try to recursively map sub maps.
````
### splitArray

__splitArray(anArray, numberOfParts) : Array__

````
Returns the result of the split of anArray into equals numberOfParts (when possible). If numberOfParts is not provided the current result of getNumberOfCores() will be used.
````
### splitBySeparator

__splitBySeparator(aString, aSeparator) : Array__

````
Will split aString using the provided aSeparator. If the aSeparator is escaped (for example if ';' is the aSeparator and  aString 'abc\\;def;123" only the second ';' will be considered.
````
### splitBySepWithEnc

__splitBySepWithEnc(text, separator, enclosures, includeEnclosures) : array__

````
Given a text, a separator, a list of enclosures and a flag includeEnclosures, this function will split the text by the separator while ignoring the separator inside the enclosures. If includeEnclosures is true, the enclosures will be included in the result. If includeEnclosures is false, the enclosures will be removed from the result.
````
### splitKVBySeparator

__splitKVBySeparator(aString, aOptions) : Map__

````
Given aString with multiple key/value entries will return a map with the same. Optionally you can provide aOptions:

   sep  - the key/value entries separator (defaults to " ")
   ksep - the key separator from a value (defaults to "=")
   esc  - the escape character (defaults to "\\")
   qto  - the quote character (defaults to "\"")
   nul  - the null representation (defaults to null)


````
### sprint

__sprint(aStr)__

````
"Stringifies" and prints the aStr to the stdout (with a new line on the end) (example: sprint("hello world!"))
````
### sprintErr

__sprintErr(aStr)__

````
"Stringifies" and prints the aStr to the stderr (with a new line on the end) (example: sprintErr("Hupps!! A problem!"))
````
### sprintErrnl

__sprintErrnl(aStr)__

````
"Stringifies" and prints the aStr to the stderr (without adding a new line on the end) (example: sprintErrnl("Hupps!! A problem!"))
````
### sprintnl

__sprintnl(aStr)__

````
"Stringifies" and prints the aStr to the stdout (without adding a new line on the end) (example: sprintnl("hello world!"))
````
### startLog

__startLog(externalLogging, hkItems)__

````
Starts collecting log messages logged with log* functions. See stopLog() and dumpLog(). You can also specify externalLogging, a custom channel subscribe function and a different number of hkItems (housekeeping items) from the default 100 (if -1 it won't delete items).
````
### stopLog

__stopLog()__

````
Will stop collecting log messages and will reset everything. User dumpLog() before stopping if you intend to keep the recorded log messages.
````
### stopOpenAFAndRun

__stopOpenAFAndRun(aCommandLineArray, addCommand)__

````
Terminates the current OpenAF execution while trying to execute the commands on the aCommandLineArray. Optionally you can use addCommand boolean flag (true) to allow for shell like commands on the current operating system. To restart OpenAF please use the restartOpenAF function.
````
### stringify

__stringify(anObject, replacer, space) : String__

````
Converts anObject into a string representation of the same. This is equivalent to the JSON.stringify function. If space isn't defined a "  " (2 spaces) is assumed as the default value. Reverts to the beautifier function if it isn't possible to apply stringify to the current object.  To see more info on the remaining parameters please check https://developer.mozilla.org/en/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify
````
### sync

__sync(aFunction, anObject)__

````
Will ensure that aFunction is synchronized, in multi-threaded scripts. Optionally you can provide anObject to synchronized upon.
````
### syncFn

__syncFn(aFunction, anObject) : Object__

````
Will ensure that aFunction is synchronized, in multi-threaded scripts (alternative to sync). Optionally you can provide anObject to synchronized upon. Returns the result of aFunction.
````
### templify

__templify(aTemplateString, someData) : String__

````
Using Handlebars and the functionality provided in ow.template, will use the aTemplateString as a Handlebars template and return the parsed output. Optionally you can provide someData as data for the Handlebars template  otherwise the current scope will be used.

Example:

var someText = "Hello World!";
var retText = templify("Hi, {{someText}}"); // Hi, Hello World!
````
### threadBox

__threadBox(aExecFunction, aTimeout, aStopFunction)__

````
Tries to execute aExecFunction inside a thread. If aTimeout is defined the thread will be terminated if it's still executing after aTimeout. If aStopFunction is defined  it will receive, as argument, a boolean indicating if the thread has stopped (true). If this function returns true the thread execution will be terminated, if false will continue.
Note: see threadBoxCtrlC as aStopFunction to stop executing on Ctrl-C
````
### threadBoxCtrlC

__threadBoxCtrlC() : Boolean__

````
Meant to be use as a stopFunction for threadBox will return true if Ctrl-C is detected and false otherwise. If the current terminal can't support ANSI if will default to false.
````
### tlog

__tlog(msg, someData, formatOptions)__

````
Outputs to the current stdout a line composed of the current date, indication of INFO and the provided msg using the templify function. Optionally you can provide also someData and you can provide a formatOptions map for overriding the defaults from setLog. Note: you can use startLog, stopLog and dumpLog to keep an internal record of theses messages.
````
### tlogErr

__tlogErr(msg, someData, formatOptions)__

````
Outputs to the current stderr a line composed of the current date, indication of ERROR and the provided msg using the templify function. Optionally you can provide a formatOptions map for overriding the defaults from setLog.  Optinionally you can provide also someData.
````
### tlognl

__tlognl(msg, someData, formatOptions)__

````
Outputs to the current stdout, without a new line, a sentence composed of the current date, indication of INFO and the provided msg using the templify function. Optionally you can provide a formatOptions map for overriding the defaults from setLog. Optinionally you can provide also someData.
````
### tlogWarn

__tlogWarn(msg, someData, formatOptions)__

````
Outputs to the current warning in a line composed of the current date, indication of WARN and the provided msg using the templify function. Optionally you can provide a formatOptions map for overriding the defaults from setLog.  Optinionally you can provide also someData.
````
### toBoolean

__toBoolean(aObj) : Boolean__

````
Tries to convert aObj (String, Number or Boolean) into a boolean value
````
### toCSV

__toCSV(anArray) : CSV__

````
Converts a given javascript anArray into a CSV object instance.
````
### toEncoding

__toEncoding(aString, anEncoding) : String__

````
Converts the provided aString to a different anEncoding (by default UTF-8).
````
### tprint

__tprint(aTemplateString, someData)__

````
Using Handlebars and the functionality provided in ow.template, will use the aTemplateString as a Handlebars template and print the parsed output. Optionally you can provide someData as data for the Handlebars template  otherwise the current scope will be used.

Example:

var someText = "Hello World!";
tprint("Hi, {{someText}}"); // Hi, Hello World!
````
### tprintErr

__tprintErr(aTemplateString, someData)__

````
Using Handlebars and the functionality provided in ow.template, will use the aTemplateString as a Handlebars template and print, to the stderr, the parsed output. Optionally you can provide someData as data for the Handlebars template  otherwise the current scope will be used.

Example:

var someText = "Hello World!";
tprintErr("Hi, {{someText}}"); // Hi, Hello World!
````
### tprintErrnl

__tprintErrnl(aTemplateString, someData)__

````
Using Handlebars and the functionality provided in ow.template, will use the aTemplateString as a Handlebars template and print, to the stderr without new line, the parsed output. Optionally you can provide someData as data for the Handlebars template  otherwise the current scope will be used.

Example:

var someText = "Hello World!";
tprintErrnl("Hi, {{someText}}"); // Hi, Hello World!
````
### tprintln

__tprintln(aTemplateString, someData)__

````
Using Handlebars and the functionality provided in ow.template, will use the aTemplateString as a Handlebars template and print, withouth a new line, the parsed output. Optionally you can provide someData as data for the Handlebars template  otherwise the current scope will be used.

Example:

var someText = "Hello World!";
tprintln("Hi, {{someText}}"); // Hi, Hello World!
````
### traverse

__traverse(aObject, aFunction) : Map__

````
Traverses aObject executing aFunction for every single element. The aFunction will receive the arguments: aKey, aValue, aPath, aObject.
````
### uncompress

__uncompress(aResultOfTheCompressFunction) : Object__

````
Uncompresses a JSON object, compressed by using the compress function, into a JSON object.
````
### uniqArray

__uniqArray(anArray) : Array__

````
Returns anArray with no duplicates entries (including duplicate maps).
````
### utf8

__utf8(aString) : String__

````
Converts the provided aString into UTF-8 encoding.
````
### visibleLength

__visibleLength(aString) : Number__

````
More complete af.visibleLength function
````
### watch

__watch(waitFor, aCommand, beautifyFlag, noPrint)__

````
Executes javascript aCommand provided every waitFor periods of time (expressed in ms). The screen will be cleared and the execution will repeat indefinitely until the 'q' key is pressed.  Optionally a beautifyFlag can be provided to execute the beautifier function on the aCommand result.
````
### wedoDate

__wedoDate(year, month, day, hour, minute, second, ms) : Map__

````
Builds and returns a wedoDate JSON object given either a year, a month, a day, a hour, a minute, a second and ms or a Date object.
````
### yprint

__yprint(aObj, multidoc, sanitize, shouldColor)__

````
Prints aObj in YAML. If multiDoc = true and aJson is an array the output will be multi-document. If sanitize = true all Java objects will be converted to avoid parsing errors.
````
### yprintErr

__yprintErr(aObj, multidoc)__

````
Prints aObj in YAML to stderr. If multiDoc = true and aJson is an array the output will be multi-document.
````
