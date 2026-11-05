---
layout: default
title: ow.test
parent: Reference
grand_parent: OpenAF docs
---

{% raw %}
## ow.test

[Source: `06414cd9`](https://github.com/OpenAF/openaf/blob/06414cd9204e918daa1e2971ce904783299db333/js/owrap.test.js) · [Baseline](../source-snapshot.md)

### ow.test.assert

`ow.test.assert(aResult, checkValue, errorMessage, notShowDiff)`

````text
Will throw an exception if aResult is different from checkValue. The exception will contain the errorMessage and the different values (if notShowDiff = true).
(available after ow.loadTest())
````

### ow.test.getAllProfileAvg

`ow.test.getAllProfileAvg() : Map`

````text
Returns a map of all profile keys to their respective average elapsed times in ms.
````

### ow.test.getAllProfileHits

`ow.test.getAllProfileHits() : Map`

````text
Returns a map of all profile keys to their respective hit counts.
````

### ow.test.getAllProfileLast

`ow.test.getAllProfileLast() : Map`

````text
Returns a map of all profile keys to their respective last recorded elapsed times in ms.
````

### ow.test.getChannel

`ow.test.getChannel() : Channel`

````text
Gets the current channel being used for test results.
````

### ow.test.getCountAssert

`ow.test.getCountAssert() : Number`

````text
Returns the current count of assertions executed.
````

### ow.test.getCountFail

`ow.test.getCountFail() : Number`

````text
Returns the current count of tests that failed.
````

### ow.test.getCountPass

`ow.test.getCountPass() : Number`

````text
Returns the current count of tests that passed.
````

### ow.test.getCountTest

`ow.test.getCountTest() : Number`

````text
Returns the current count of tests executed.
````

### ow.test.getExecHistory

`ow.test.getExecHistory() : Array`

````text
Gets the test results execution history.
````

### ow.test.getProfile

`ow.test.getProfile() : Map`

````text
Returns a map of all profile keys with their current hits, sum, last, start, max and min elapsed time values.
````

### ow.test.getProfileAvg

`ow.test.getProfileAvg(aProfileKey) : Number`

````text
Returns the average elapsed time in ms across all recorded executions for aProfileKey.
````

### ow.test.getProfileHits

`ow.test.getProfileHits(aProfileKey) : Number`

````text
Returns the number of times the timer for aProfileKey was stopped (completed executions).
````

### ow.test.getProfileLast

`ow.test.getProfileLast(aProfileKey) : Number`

````text
Returns the last recorded elapsed time in ms for aProfileKey.
````

### ow.test.getProfileMax

`ow.test.getProfileMax(aProfileKey) : Number`

````text
Returns the maximum recorded elapsed time in ms for aProfileKey.
````

### ow.test.getProfileMin

`ow.test.getProfileMin(aProfileKey) : Number`

````text
Returns the minimum recorded elapsed time in ms for aProfileKey.
````

### ow.test.profileReset

`ow.test.profileReset(aProfileKey)`

````text
Resets the profile counters (hits, sum, last and start) for aProfileKey.
````

### ow.test.reset

`ow.test.reset()`

````text
Resets the internal test counters (test, pass and fail).
(available after ow.loadTest())
````

### ow.test.setKeepStackTrace

`ow.test.setKeepStackTrace(aBooleanSetting)`

````text
Turns on (off by default) on keeping the java stack trace on java exceptions if aBooleanSetting = true.
````

### ow.test.setMemoryProfile

`ow.test.setMemoryProfile(aBooleanSetting)`

````text
Turns on (off by default) the gathering of memory differences if aBooleanSetting = true.
````

### ow.test.setOutput

`ow.test.setOutput(aBooleanSetting)`

````text
Turns off (on by default) the output of the result of each test.
````

### ow.test.setShowStackTrace

`ow.test.setShowStackTrace(aBooleanSetting)`

````text
Turns on (off by default) the display of java stack trace on java exceptions if aBooleanSetting = true.
````

### ow.test.start

`ow.test.start(aKey) : String`

````text
Starts a timer for the provided aKey to determined the elapsed time when ow.test.stop(aKey) is invoked. Returns the aKey provided.
````

### ow.test.stop

`ow.test.stop(aKey) : Number`

````text
Stops an existing timer for the provided aKey to determine the elapsed time since a ow.test.start(aKey) was invoked.
````

### ow.test.test

`ow.test.test(aTest, aFunction, aArgMap) : Object`

````text
Test aFunction for a test named aTest.  If aTest is divided with "::" the first part sill be consider to be a test suite name. Will return whatever the function returns. Optionally you can provide aArgMap with a map of arguments to be used by aFunction. The aFunction will receive two arguments: (1) a function that will output/log any map, array or string provided;  (2) the aArgMap if provided.
(available after ow.loadTest())
````

### ow.test.testExternally

`ow.test.testExternally(aTest, aCommand, aTimeout) : Object`

````text
Test executing aCommand for a give aTimeout (if provided) for a test named aTest. If aTest is divided with "::" the first part will be consider to be a test suite name. Will return whatever the command returns.
(available after ow.loadTest())
````

### ow.test.toJUnitXML

`ow.test.toJUnitXML(testSuitesId, testSuitesName) : String`

````text
Returns a JUnit results XML using testSuitesId and testSuitesName as identifiers.
````

### ow.test.toMarkdown

`ow.test.toMarkdown() : String`

````text
Returns a markdown-formatted string with a summary and per-test result table for all tests executed.
````
{% endraw %}
