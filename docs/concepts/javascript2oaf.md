---
layout: default
title: Javascript to OpenAF
parent: Concepts
grand_parent: OpenAF docs
---

# Javascript to OpenAF

This article provides a description of the additions (e.g. functions, variables, libraries, etc...) to the standard JavaScript included with OpenAF.

## Basics

Starting with basics, OpenAF runs on Java interpreting/compiling javascript using [Mozilla Rhino](https://github.com/mozilla/rhino). Not the version that was included on the JVM a long time ago but current stable version on GitHub. That means it supports [ES5](https://www.w3schools.com/js/js_es5.asp) with some features of [ES6](https://www.w3schools.com/js/js_es6.asp) (see a [compatibility map from Mozilla Rhino](http://mozilla.github.io/rhino/compat/engines.html)).

You can always check documentation here or, using the openaf-console (oafc), executing the "help" command for more details:

````
> help [partial of full word match]
````

Additionally you can use the openaf-console (oafc) auto-complete, _desc_ and _scope_ commands to find out more.

## Basic

### Basic variables

| Variable | Type | Description |
|----------|------|-------------|
| \_\_ | | Shortcut for undefined |
| global   | | Represents all the global variables (e.g. _this_ on the main context). |

### Basic functions

| Function | Description |
|----------|-------------|
| compare | Compares two javascript objects (with deep map search). |
| clone | Clones the provided javascript object to a new instance. | 
| merge | Merges two javascript maps and/or arrays into a new object. |
| inherit | Given an parent and a child object it will copy the parent javascript prototype to the child prototype. |
| load | Given an OpenAF javascript file it will interpret and compile the corresponding code. Will search the current installed oPack paths if not found on the current path. |
| loadLib | Sames as _load_ but keeping track of previously loaded OpenAF javascript files to avoid re-execution. |
| plugin | Loads a Java-based OpenAF plugin that must be on the classpath. If found on current installed oPack paths it will try to dynamically added to the classpath (when using the custom class loader). | 
| require | Loads an OpenAF javascript with declared exports returning a map with the same. |
| exit | Immediatelly exits the current execution with the provided exit code. |
| arrayContains | Tries to determine if an array contains an object. |
| uniqArray | Returns an array with no duplicated entries (with deep map search). |
| splitArray | Returns the best effort of diving the provided array into a specific number of equal parts. |

## Checking types

### One-line type checking

The one-line type checking propose it's to be used for checking arguments of a function and providing default values or exceptions if a value is not provided.

The syntax of usage is:

````javascript
// For values that must be defined
_$([aVariable], [anOptionalDescription]).[combination of check functions].$_(anOptionalExceptionDescription)

// For values that have a default value
aVariable = _$([aVariable], [anOptionalDescription]).[combination of check functions].default(anOptionalExceptionDescription])
````

Examples:

````javascript
function useEvenNumber(aEvenNumber) {
    // Combining check functions
    _$(aEvenNumber, "aEvenNumber")
    .isNumber()
    .check(v => v % 2 == 0, "has to be even")
    .$_();

    [...]
}
````

````javascript
function modifyChild(aChildUUID, aParentUUID) {
    // Check mandatory
    _$(aChildUUID, "aChildUUID").isUUID().$_("a child uuid must be provided");
    
    // Check and assign defaults
    aParentUUID = _$(aParentUUID, "aParentUUID").isUUID().default("ed258253-a8e3-2df1-5d74-b106e8cd7e9a");

    [...]
}
````

For check functions any combination can be used (each function includes also a second argument to provide more text information about the failure of the check):

| Function | Checking propose |
|----------|------------------|
| anyOf    | Determine if the array provided only has values from a pre-provided array of values. |
| between | Determines if a number is between a minimum and maximum values exclusively. | 
| betweenEquals | Determines if a number is between a minimum and maximum values inclusively. |
| check   | Uses the provided javascript function to check. |
| contains | Determines if a string value contains a sub-string. |
| empty    | Determines if the provided value is empty. |
| ends     | Determines if the provided string ends with the provided sub-string. |
| equals   | Determines if the provided string is equals to the provided string. |
| greater  | Determines if the provided value is bigger than the provided value. |
| greaterEquals | Determines if the provided value if bigger or equal than the provided value. | 
| isArray  | Determines if a variable is an array.  |
| isBoolean | Determines if a variable is a boolean. |
| isDate | Determines if a variable is a date.|
| isFunction | Determines if a variable is a function. | 
| isInstanceOf | Determines if the provided Java object is an instance of a given Java class. |
| isJavaObject | Determines if a variable is a Java object. |
| isMap | Determines if a variable is a map. | 
| isNotNull | Determines if a variable is not null. | 
| isNumber | Determines if a variable is a number. | 
| isObject | Determines if a variable is a object (e.g. map, array) | 
| isRegExp | Determines if a variable is a javascript regular expression. |
| isSchema | Determines if a provided map is according with the provided JSON schema. |
| isString | Determines if a variable is a string. |
| isTNumber | Determines if the type of a number provided, independently of it's conversion from number, is a Number. |
| isUUID | Determines if a variable is an UUID |
| javaRegexp | Determines if a Java object provided is a Java regular expression. |
| less | Determines if a provided number is less than a number. | 
| lessEquals | Determines if a provided number is less or equal than a number. |
| notContains | Determines if a provided string doesn't contain a sub-string. |
| notEmpty | Determines if a variable isn't empty. | 
| notEnds | Determines if a string doesn't end with a sub-string. |
| notEquals | Determines if the provided string is not equal to a specific string. | 
| notStarts | Determines if a string doesn't start with a sub-string |
| oneOf | Determines if the value is one of the array of values provided. |
| regexp | Given a regular expression tests if the value matches it. |
| starts | Determines if a string starts with a sub-string. |  

### Function type checking

For function-based type checking there are a set of functions prefixed with "is". They provide not only javascript type checking but also java object type checking in specific cases:

| Function      | Description |
|---------------|-------------|
| isArray       | Determines if an variable is an array. |
| isBinaryArray | Determines if the variable is a Java binary (integers) array. |
| isBoolean     | Determines if an variable is a boolean. |
| isByteArray   | Determines if the variable is a Java byte array. |
| isDate        | Determines if an variable is a date. |
| isDecimal     | Determines if a javascript number variable has a decimal component or not. |
| isDef         | Determines if the provided variable is defined. |
| isFunction    | Determins if the provided variable is a function. |
| isInteger     | Determines if a javascript number variable doesn't have a decimal component. |
| isJavaException | Determines if the provided variable is a Java exception object instance. |
| isJavaObject  | Determines if the provided variable is a Java object instance. |
| isMap         | Determines if the provided variable is a map. |
| isNull        | Determines if the provided variable is a null. |
| isNumber      | Determines if the provided variable is a number. |
| isObject      | Determines if the provided variable is a generic javascript object (e.g. map, array) |
| isString      | Determines if the provided variable is a string. |
| isTNumber     | Determines if the provided variable, independently of the possible conversion to number, is of javascript type Number |
| isUUID        | Determines if the provided variable string is a UUID. |
| isUnDef       | Determines if the provided variable is not defined. |  

## Printing

| Function | Description |
|----------|-------------|
| print      | Outputs a string to stdout with a new-line |
| printnl    | Outputs a string to stdout without a new-line |
| printErr   | Outputs a string to stderr with a new-line |
| printErrnl | Outputs a string to stderr without a new-line |
| sprint     | Outputs a stringify of an object to stdout with a new-line |
| sprintnl   | Outputs a stringify of an object to stdout without a new-line |
| sprintErr  | Outputs a stringify of an object to stderr with a new-line |
| sprintErrnl| Outputs a stringify of an object to stderr without a new-line |
| tprint     | Outputs a string based on a provided template using data from an object to stdout with a new-line |
| tprintnl   | Outputs a string based on a provided template using data from an object to stdout without a new-line |
| tprintErr  | Outputs a string based on a provided template using data from an object to stderr with a new-line |
| tprintErrnl| Outputs a string based on a provided template using data from an object to stderr without a new-line |

## Logging

| Function | Description |
|----------|-------------|
| log      | Prints a string with a timestamp and a log level of 'INFO' to stdout with a new-line |
| lognl    | Prints a string with a timestamp and a log level of 'INFO' to stdout without a new-line |
| logErr   | Prints a string with a timestamp and a log level of 'ERROR' to stderr with a new-line |
| logWarn  | Prints a string with a timestamp and a log level of 'WARN' to stdout with a new-line |
| tlog     | Outputs a string based on a provided template using data from an object together with a timestamp and a log level of 'INFO' to stdout with a new-line |
| tlognl   | Outputs a string based on a provided template using data from an object together with a timestamp and a log level of 'INFO' to stdout without a new-line |
| tlogErr  | Outputs a string based on a provided template using data from an object together with a timestamp and a log level of 'ERROR' to stderr with a new-line |
| tlogWarn | Outputs a string based on a provided template using data from an object together with a timestamp and a log level of 'WARN' to stdout with a new-line |
| setLog | Sets several flags for how the log functions behave including setting which log levels get output or not, how the timestamp is formated, if they should async or sync calls and if process memory and load should be captured in each execution. |
| startLog | Starts logging to a default or specified [OpenAF channel](OpenAF-Channels.md) with automatic housekeeping |
| stopLog | Stops logging to a default of specified [OpenAF channel](OpenAF-Channels.md) after a startLog function has been previously executed. |

## Error handling helpers

OpenAF provides utility helpers to improve diagnostics and recoverability when exceptions are raised. The most notable helper added for the v20250721 release is `$err(exception, rethrow, returnStr, code)`. It formats JavaScript and Java exceptions consistently, prints the stack trace (respecting the `OAF_ERRSTACK` flag) and, when source information is available, highlights the code lines around the failure so troubleshooting is easier. By default `$err` writes the formatted message to the console, but you can set `returnStr=true` to obtain the formatted text programmatically or `rethrow=true` to propagate the original exception after logging it.

## Navigating arrays and maps

There are a set of libraries includes to help to "navigate" through javascript arrays and maps:

| Function | Description | 
|----------|-------------|
| $from | See more in [$from](OpenAF-nLinq) |
| $path | Uses the [JMESPath library](http://jmespath.org) |
| $stream | Uses the old [streamjs library](https://github.com/winterbe/streamjs/blob/master/APIDOC.md) |

## Utility

The `af` namespace continues to aggregate convenience helpers for day-to-day scripting. Two recent additions are:

| Function | Description |
|----------|-------------|
| `af.nvl(value, default)` | Returns `value` when it is defined and non-null, or `default` otherwise. It is a concise alternative to common null/undefined coalescing patterns when working with optional data sources. |
| `af.swap(array, index1, index2)` | Returns a new array where the elements at `index1` and `index2` have been exchanged. The original array is validated and left untouched, making it safer to reorganise data that is being shared between functions or promises. |

## Parallel execution

Asynchronous utilities received multiple improvements that embrace Java virtual threads while keeping the familiar OpenAF APIs:

* `$do(fn)` continues to run `fn` on the managed worker pool and immediately returns an `oPromise` chain.
* `$doV(fn)` mirrors `$do`, but executes the promise callbacks on Java virtual threads when they are available. This is ideal for IO-bound workloads that benefit from lightweight concurrency without exhausting classic thread pools.
* `$sync()` returns an object exposing `run(fn)` which serialises access to the provided function by using a `ReentrantLock`. It is a simple way to protect shared resources that are updated from multiple promises or channel callbacks without manually instantiating locks.
* `$queue(initialItems)` creates a thread-safe FIFO queue backed by `ConcurrentLinkedQueue`, exposing helpers such as `add`, `poll`, `peek`, `has`, and `size`. Passing an initial array enqueues it immediately, offering an easy coordination primitive for producer/consumer flows.

These utilities can be combined: for example, producers can push work with `$queue().add(...)`, consumers can fetch it with `$doV` to process in virtual threads, and any critical sections can be guarded with `$sync().run(...)`.

## OPack specific

_tbc_

## OpenAF help functionality

_tbc_
## OpenAF runtime specific

### Global runtime variables

| Variable | Type | Description |
|----------|------|-------------|
| noHomeComms | Boolean | When set to _true_ the OpenAF runtime will avoid any call to "openaf.io" (to get help indexes, latest version, etc...) |
| __separator | String | The operating-system dependent line separator (e.g. '\n' or '\r\n') |

_tbc_

### Global runtime functions

| Function | Description |
|----------|-------------|
| getOpenAFJar | Returns the complete filepath and name for the OpenAF jar file. |
| processExpr | Processes command-line argument data provided with the option _"-e"_ |
| getVersion | Returns the current OpenAF runtime version. |
| getDistribution | Returns the current OpenAF runtime distribution name. |
| getOpenAFPath | Returns the filepath to where OpenAF seems to be installed. |
| loadExternalJars | If using OpenAF's custom class loader it will dynamicall load external classes from JARs on the filpath provided. |
| loadCompiled | Loads a pre-compiled OpenAF javascript library (if not pre-compiled it will attempt to compile it). |
| loadLibCompiled | Same as _loadCompiled_ but ensuring that the pre-compiled OpenAF javascript library code is only executed once. |
| requireCompiled | Returns an object with all the javascript exports on a javascript pre-compiled library. |
| restartOpenAF | Terminates the current OpenAF execution and tries to restart the java process again. |
| forkOpenAF | Starts another OpenAF process with the same command-line. |
| stopOpenAFAndRun | Terminates the current OpenAF execution in parallel with starting the execution of a new command-line provided. |
| addOnOpenAFShutdown | Adds a function to be executed upon OpenAF execution end. |
| getNumberOfCores | Returns the current reported number of cores. |
| getCPULoad | Returns the current reports CPU load from the Java instrumentation API. |
| getPid | Returns the current process OS identifier. |
| pidCheck | Verifies if the provided pid is currently running or not. |
| pidCheckIn | Provides check-in pid functionality over a .pid file to ensure that only one OpenAF execution is invoked. |
| pidKill | Tries to terminate a OS process by pid. |
| pidCheckOut | Provided check-out pid functionality over a .pid file to ensure that only one OpenAF execution is invoked. |

_tbc_

## Python integration

_tbc_

## oWrap and other included libraries

The following is a list of the OpenAF and external libraries included. Most of the libraries are automatically loaded by OpenAF when required but _ow.load*_ and _load*_ functions can be used to ensure they are loaded. These load functions can be used repeatedly as OpenAF ensures that they are only loaded on the first call. 

Most of the none basic OpenAF functionality is kept in included "ow" (OpenWrap) _wrapper_ libraries:

| Library | Description | To load |
|---------|-------------|---------|
| Format | One of the main libraries with all formatting functionality (might include some old format unrelated functions) | ````ow.loadFormat();```` |
| Obj | One of the main libraries with object manipulation functionality | ````ow.loadObj();```` |
| Server | One of the main libraries with server related functionality when OpenAF code is run as a daemon | ````ow.loadServer();```` |
| Ch | One of the main libraries with [OpenAF channel](OpenAF-Channels.md) functionality | ````ow.loadCh();```` |
| Template | One of the main libraries providing templating functionality (HandleBards based) | ````ow.loadTemplate();```` | 
| Sec | Includes all the [OpenAF 'secure buckets'](sBuckets.md) functionality | ````ow.loadSec();```` |
| Net | Includes network related functionality | ````ow.loadNet();```` |
| Metrics | Includes self monitoring and telemetry functionality | ````ow.loadMetrics();```` |
| Test | Includes unitary test helper functionality | ````ow.loadTest();```` | 
| Java | Java integration functionality | ````ow.loadJava();```` |
| Python | Python integration functionality | ````ow.loadPython();```` |
| AI | Includes some basic AI functionality | ````ow.loadAI();```` |
| Dev | Includes functionality that it's still being tested. | ````ow.loadDev();```` |

External javascript based libraries are also included:

| Library | To load | 
|---------|---------|
| Underscore (Lodash) | ````loadUnderscore()```` |
| FuseJS | ````loadFuse()```` |
| JsDiff | ````loadDiff()```` |
| Ajv | ````loadAjv()```` |
| Lodash (Underscore) | ````loadLodash()```` |
| OpenAF oDoc (help functionality) | ````loadHelp()```` |

## Java support

To check on how to interact between Javascript and Java in OpenAF (including some OpenAF helper functions built-in) see [Java support](/docs/concepts/java)
