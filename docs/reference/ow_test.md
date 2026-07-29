---
layout: default
title: ow.test
parent: Reference
grand_parent: OpenAF docs
---


## ow.test

### ow.test.assert

__ow.test.assert(aResult, checkValue, errorMessage, notShowDiff)__

````
Will throw an exception if aResult is different from checkValue. The exception will contain the errorMessage and the different values (if notShowDiff = true).
(available after ow.loadTest())
````
### ow.test.getAllProfileAvg

__ow.test.getAllProfileAvg() : Map__

````
Returns a map of all profile keys to their respective average elapsed times in ms.
````
### ow.test.getAllProfileHits

__ow.test.getAllProfileHits() : Map__

````
Returns a map of all profile keys to their respective hit counts.
````
### ow.test.getAllProfileLast

__ow.test.getAllProfileLast() : Map__

````
Returns a map of all profile keys to their respective last recorded elapsed times in ms.
````
### ow.test.getChannel

__ow.test.getChannel() : Channel__

````
Gets the current channel being used for test results.
````
### ow.test.getCountAssert

__ow.test.getCountAssert() : Number__

````
Returns the current count of assertions executed.
````
### ow.test.getCountFail

__ow.test.getCountFail() : Number__

````
Returns the current count of tests that failed.
````
### ow.test.getCountPass

__ow.test.getCountPass() : Number__

````
Returns the current count of tests that passed.
````
### ow.test.getCountTest

__ow.test.getCountTest() : Number__

````
Returns the current count of tests executed.
````
### ow.test.getExecHistory

__ow.test.getExecHistory() : Array__

````
Gets the test results execution history.
````
### ow.test.getProfile

__ow.test.getProfile() : Map__

````
Returns a map of all profile keys with their current hits, sum, last, start, max and min elapsed time values.
````
### ow.test.getProfileAvg

__ow.test.getProfileAvg(aProfileKey) : Number__

````
Returns the average elapsed time in ms across all recorded executions for aProfileKey.
````
### ow.test.getProfileHits

__ow.test.getProfileHits(aProfileKey) : Number__

````
Returns the number of times the timer for aProfileKey was stopped (completed executions).
````
### ow.test.getProfileLast

__ow.test.getProfileLast(aProfileKey) : Number__

````
Returns the last recorded elapsed time in ms for aProfileKey.
````
### ow.test.getProfileMax

__ow.test.getProfileMax(aProfileKey) : Number__

````
Returns the maximum recorded elapsed time in ms for aProfileKey.
````
### ow.test.getProfileMin

__ow.test.getProfileMin(aProfileKey) : Number__

````
Returns the minimum recorded elapsed time in ms for aProfileKey.
````
### ow.test.profileReset

__ow.test.profileReset(aProfileKey)__

````
Resets the profile counters (hits, sum, last and start) for aProfileKey.
````
### ow.test.reset

__ow.test.reset()__

````
Resets the internal test counters (test, pass and fail).
(available after ow.loadTest())
````
### ow.test.setKeepStackTrace

__ow.test.setKeepStackTrace(aBooleanSetting)__

````
Turns on (off by default) on keeping the java stack trace on java exceptions if aBooleanSetting = true.
````
### ow.test.setMemoryProfile

__ow.test.setMemoryProfile(aBooleanSetting)__

````
Turns on (off by default) the gathering of memory differences if aBooleanSetting = true.
````
### ow.test.setOutput

__ow.test.setOutput(aBooleanSetting)__

````
Turns off (on by default) the output of the result of each test.
````
### ow.test.setShowStackTrace

__ow.test.setShowStackTrace(aBooleanSetting)__

````
Turns on (off by default) the display of java stack trace on java exceptions if aBooleanSetting = true.
````
### ow.test.start

__ow.test.start(aKey) : String__

````
Starts a timer for the provided aKey to determined the elapsed time when ow.test.stop(aKey) is invoked. Returns the aKey provided.
````
### ow.test.stop

__ow.test.stop(aKey) : Number__

````
Stops an existing timer for the provided aKey to determine the elapsed time since a ow.test.start(aKey) was invoked.
````
### ow.test.test

__ow.test.test(aTest, aFunction, aArgMap) : Object__

````
Test aFunction for a test named aTest.  If aTest is divided with "::" the first part sill be consider to be a test suite name. Will return whatever the function returns. Optionally you can provide aArgMap with a map of arguments to be used by aFunction. The aFunction will receive two arguments: (1) a function that will output/log any map, array or string provided;  (2) the aArgMap if provided.
(available after ow.loadTest())
````
### ow.test.testExternally

__ow.test.testExternally(aTest, aCommand, aTimeout) : Object__

````
Test executing aCommand for a give aTimeout (if provided) for a test named aTest. If aTest is divided with "::" the first part will be consider to be a test suite name. Will return whatever the command returns.
(available after ow.loadTest())
````
### ow.test.toJUnitXML

__ow.test.toJUnitXML(testSuitesId, testSuitesName) : String__

````
Returns a JUnit results XML using testSuitesId and testSuitesName as identifiers.
````
### ow.test.toMarkdown

__ow.test.toMarkdown() : String__

````
Returns a markdown-formatted string with a summary and per-test result table for all tests executed.
````
