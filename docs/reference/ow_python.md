---
layout: default
title: ow.python
parent: Reference
grand_parent: OpenAF docs
---


## ow.python

### ow.python.exec

__ow.python.exec(aPythonCode, aInput, aOutputArray, throwExceptions, shouldFork) : Map__

````
Exchanges JSON values via named Python variables. Names must be ASCII identifiers and not keywords. A started embedded server preserves variables, imports and functions across serialized calls; otherwise a fresh process is used. shouldFork=true isolates a call. Errors print by default; throwExceptions=true throws on stderr, nonzero exits or bridge failures. Missing results return undefined.
````
### ow.python.execPM

__ow.python.execPM(aPythonCode, aInput, throwExceptions, shouldFork) : Map__

````
Exchanges a JSON map through __pm. Mutate __pm to return values. Uses the persistent server when started; shouldFork=true runs an isolated process. Errors print by default; throwExceptions=true throws on stderr, nonzero exits or bridge failures. Failed calls without a result return undefined.
````
### ow.python.execStandalone

__ow.python.execStandalone(aPythonCodeOrFile, aInput, throwExceptions, aArgv) : Map__

````
Executes a .py file or inline code in standalone mode with callbacks. Returns a process result with exitcode, inherits stdin and streams stdout/stderr (the returned output strings are empty). aInput is reserved. Explicit aArgv overrides OAF_PY_ARGC/OAF_PY_ARG_n. File execution preserves __file__, __name__, sys.argv[0], script import directory and future imports. throwExceptions defaults to false; true throws on stderr or a nonzero exit. Stop the bridge when done.
````
### ow.python.getVersion

__ow.python.getVersion() : Number__

````
Returns the Python major version (2 or 3), or -1 after failed detection.
````
### ow.python.reset

__ow.python.reset(noException, tryOthers)__

````
Detects the configured interpreter using --version. tryOthers enables python3 fallback. noException records failure as version=-1. The successful interpreter is retained. Stop the bridge before resetting.
````
### ow.python.setPython

__ow.python.setPython(aPythonPath)__

````
Selects and detects the interpreter executable. Stop the bridge first. Paths may contain spaces.
````
### ow.python.startServer

__ow.python.startServer(aPort, aSendPort, aFn, isAlone) : String__

````
Acquires a bridge reference, returning its token. Embedded mode owns a persistent, serialized Python namespace. isAlone=true starts only the callback listener for standalone scripts. Modes cannot be mixed until stopped. aFn receives connect, exec and error events. Startup has a bounded readiness check.
````
### ow.python.stopServer

__ow.python.stopServer(aPort, force) : Boolean__

````
Releases one explicit start reference. Stops owned resources at zero, or immediately with force=true. Returns true only when resources were stopped; repeated stops return false. aPort is retained for compatibility.
````
