---
layout: default
title: ow.python
parent: Reference
grand_parent: OpenAF docs
---


## ow.python

### ow.python.exec

__ow.python.exec(aPythonCode, aInput, aOutputArray, shouldFork) : Map__

````
Tries to execute aPythonCode with the current interpreter providing the aInput map keys as python variables. It tries to return the values of the aOutputArray name variables. Example:

   var res = ow.python.exec("c = a + b", { a: 2, b: 1 }, [ "c" ]);
   print(res.c); // 3


````
### ow.python.execPM

__ow.python.execPM(aPythonCode, aInput) : Map__

````
Tries to execute aPythonCode with the current interpreter providing the aInput map as a python variable __pm. Any changes to this python variable will be returned.
````
### ow.python.execStandalone

__ow.python.execStandalone(aPythonCodeOrFile, aInput, throwExceptions)__

````
Executes aPythonCodeOrFile (a Python script path ending in ".py" or inline code) via the standalone bridge
started with ow.python.startServer(..., isAlone=true). The OpenAF bridge init code is prepended so that
the script can call back into OpenAF via _(). If throwExceptions is true, stderr output will raise an exception.
````
### ow.python.getVersion

__ow.python.getVersion() : String__

````
The majoy python version detected.
````
### ow.python.reset

__ow.python.reset(noException, tryOthers)__

````
Detects the Python version by running the configured interpreter. If noException is true, version detection
failures are silently recorded (version set to -1) rather than thrown. If tryOthers is true, a fallback
to "python3" is attempted when the primary interpreter fails.
````
### ow.python.setPython

__ow.python.setPython(aPythonPath)__

````
Sets the aPythonPath to the python interpreter process to use.
````
### ow.python.startServer

__ow.python.startServer(aPort, aSendPort, aFn, isAlone)__

````
Starts the bidirectional OpenAF-Python bridge. aPort is the port for the receive server (random if not specified),
aSendPort is the port for the Python-side server (random if not specified), aFn is an optional callback for
events ("connect", "exec", "error") and isAlone (boolean) starts only the receive half without launching a
Python subprocess (standalone mode).
````
### ow.python.stopServer

__ow.python.stopServer(aPort, force) : Boolean__

````
Stops the OpenAF-Python bridge listening on aPort. If force is true the server is stopped unconditionally;
otherwise it only stops when the internal reference counter reaches zero. Returns true if the server was
actually stopped.
````
