---
layout: default
title: threads
parent: Reference
grand_parent: OpenAF docs
---


## threads

### Threads.addCachedThread

__Threads.addCachedThread(aFunction) : String__

````
Adds to the cached thread pool aFunction to be executed. Returns an UUID associated with the thread. The aFunction will receive the corresponding UUID as the first parameter. Note: it calls initCachedThreadPool if it wasn't previously and it won't work if any of the other start* of init* methods has been used previously.
````
### Threads.addFixedThread

__Threads.addFixedThread(aFunction) : String__

````
Adds to the fixed thread pool aFunction to be executed. Returns an UUID associated with the thread. The aFunction will receive the corresponding UUID as the first parameter. Note: it calls initFixedThreadPool if it wasn't previously and it won't work if any of the other start* of init* methods has been used previously.
````
### Threads.addOpenAFShutdownHook

__Threads.addOpenAFShutdownHook(aFunction)__

````
Adds aFunction to try to execute whenever OpenAF is going to shutdown. The latest hook added will be the first to be executed until the first hook added.
````
### Threads.addScheduleThread

__Threads.addScheduleThread(aFunction, aDelay) : String__

````
Adds to the scheduled thread pool aFunction to be executed within aDelay in ms. Returns an UUID associated with the thread. The aFunction will receive the corresponding UUID as the first parameter. Note: it calls initScheduledThreadPool if it wasn't previously and it won't work if any of the other start* or init* methods has been used previously.
````
### Threads.addScheduleThreadAtFixedRate

__Threads.addScheduleThreadAtFixedRate(aFunction, aRate) : String__

````
Adds to the scheduled thread pool aFunction to be executed at a fixed aRate in ms. Returns an UUID associated with the thread. The aFunction will receive the corresponding UUID as the first parameter. Note: it calls initScheduledThreadPool if it wasn't previously and it won't work if any of the other start* or init* methods has been used previously.
````
### Threads.addScheduleThreadWithFixedDelay

__Threads.addScheduleThreadWithFixedDelay(aFunction, aDelay) : String__

````
Adds to the scheduled thread pool aFunction to be executed at a fixed aDelay in ms. Returns an UUID associated with the thread. The aFunction will receive the corresponding UUID as the first parameter. Note: it calls initScheduledThreadPool if it wasn't previously and it won't work if any of the other start* or init* methods has been used previously.
````
### Threads.addSingleThread

__Threads.addSingleThread(aFunction) : String__

````
Adds to the single thread pool aFunction to be executed. Returns an UUID associated with the thread. The aFunction will receive the corresponding UUID as the first parameter. Note: it calls initSingleThreadPool if it wasn't previously and it won't work if any of the other start* of init* methods has been used previously.
````
### Threads.addThread

__Threads.addThread(aFunction) : String__

````
Add a thread to call aFunction as callback. Returns an UUID associated with the thread. The aFunction will receive the corresponding UUID as the first parameter.
````
### Threads.addVirtualThread

__Threads.addVirtualThread(aFunction) : String__

````
Adds to the virtual thread executor aFunction to be executed. Returns an UUID associated with the thread.
````
### Threads.getNumberOfCores

__Threads.getNumberOfCores() : number__

````
Returns the number of cores identified by Java.
````
### Threads.initCachedThreadPool

__Threads.initCachedThreadPool()__

````
Uses a thread pool situable for cached threads. Note: it ignores any previous thread added using addThread; It won't work if any of the other start* or init* methods has been used.
````
### Threads.initFixedThreadPool

__Threads.initFixedThreadPool(numberOfThreads)__

````
Uses a thread pool situable for fixed threads where you can specify the numberOfThreads to use (by default the number of cores). Note: it ignores any previous thread added using addThread; It won't work if any of the other start* or init* methods has been used.
````
### Threads.initScheduledThreadPool

__Threads.initScheduledThreadPool(numberOfThreads)__

````
Uses a thread pool situable for scheduled threads where you can specify the numberOfThreads to use (by default the number of cores). Note: it ignores any previous thread added using addThread; It won't work if any of the other start* or init* methods has been used.
````
### Threads.initSingleThreadPool

__Threads.initSingleThreadPool(numberOfThreads)__

````
Uses a thread pool situable for single threads where you can specify the numberOfThreads to use (by default the number of cores). Note: it ignores any previous thread added using addThread; It won't work if any of the other start* or init* methods has been used.
````
### Threads.initVirtualThreadPerTaskExecutor

__Threads.initVirtualThreadPerTaskExecutor()__

````
Uses a virtual thread per task executor (Java 21).
````
### Threads.start

__Threads.start()__

````
Start normally all threads added. Will wait for the end of execution of all threads. Note: it won't work if any of the other start* or init* methods has been used.
````
### Threads.startAtFixedRate

__Threads.startAtFixedRate(aTime)__

````
Start all threads and restarts them at a fixed rate determined by aTime (in ms) independently of the time when the thread execution ends. Execution will stop upon Threads.stop.  Note: it won't work if any of the other start* or init* methods has been used.
````
### Threads.startNoWait

__Threads.startNoWait()__

````
Start normally all threads added. Will not wait for the end of the execution of all threads. See Threads.waitForThreads for waiting for the execution of threads when needed or, in alternative, to Threads.start. Note: it won't work if any of the other start* or init* methods has been used.
````
### Threads.startWithFixedRate

__Threads.startWithFixedRate(aTime)__

````
Start all threads and restarts them at a fixed rate determined by aTime (in ms) starting on the time when the thread execution ends. Execution will stop upon Threads.stop. Note: it won't work if any of the other start* or init* methods has been used.
````
### Threads.stop

__Threads.stop(shouldForce)__

````
Stop all thread execution. If all threads need to be stopped immediately without waiting for the end of thread execution then used shouldForce = true.
````
### Threads.sync

__Threads.sync(aFunction)__

````
Try to execute the aFunction in a synchronized method. Useful in parallel processing to safely access variables/resources shared between threads.
````
### Threads.Threads

__Threads.Threads() : Threads__

````
Creates a new instance of a group of threads to manage.
````
### Threads.waitForThreads

__Threads.waitForThreads(aTimeout) : boolean__

````
Waits for all threads to finish during aTimeout period (in ms). Returns true if all threads stopped or false otherwise.
````

### Threads.runOpenAFShutdownHooksNow

__Threads.runOpenAFShutdownHooksNow()__

````
Synchronously runs, in the current thread, every shutdown hook/action registered so far via addOpenAFShutdownHook (and Java-side registrations such as io.createTempDir's cleanup) - in the reverse order they were added. Each one is guarded to run at most once, so it is safe to call this and still let the normal JVM shutdown sequence run afterwards (e.g. via System.exit): already-run hooks will be skipped there. Intended to be used right before Threads.nativeExit.
````

### Threads.nativeExit

__Threads.nativeExit(anExitCode)__

````
Terminates the current process immediately at the operating system level (the C library's _exit), bypassing the JVM's own shutdown sequence entirely - including JVM-registered shutdown hook threads and the safepoint HotSpot uses to wait for JIT compiler threads, which can otherwise delay process exit by several seconds (observed up to ~10s) when a compilation is still in flight. Because JVM-level cleanup is skipped, call Threads.runOpenAFShutdownHooksNow() first for any cleanup that must still happen (this is what exit(code, true) does). Falls back to Runtime.halt (not guaranteed to avoid the delay this method exists to avoid) if the native call is unavailable on this platform.
````

### Threads.armFastExitOnShutdown

__Threads.armFastExitOnShutdown(anExitCode)__

````
Arms an extra JVM shutdown hook that waits for every other OpenAF-registered shutdown hook/action (see addOpenAFShutdownHook and the Java-side registerShutdownAction) to finish, then calls Threads.nativeExit(anExitCode) itself - the same fast-exit trick exit(code, true) uses, but triggered automatically once JVM shutdown actually begins rather than requiring an explicit exit(code, true) call. This covers cases like a script simply finishing, Ctrl-C or SIGTERM, where the JVM's own trailing teardown (including the safepoint wait for JIT compiler threads that can delay exit by several seconds) would otherwise still run after the hooks are done. Calling this does nothing on its own: it only takes effect once real JVM shutdown starts, so normal execution and daemon/server processes that intentionally stay alive (non-daemon threads still running) are unaffected. As with exit(code, true), once armed, any shutdown hook or File.deleteOnExit() entry not registered through OpenAF will NOT run once shutdown starts. Idempotent: calling it again just updates the exit code that will be used.
````

### Threads.setRequestedExitCode

__Threads.setRequestedExitCode(anExitCode)__

````
Records anExitCode as the status the process is about to exit with (to be called right before System.exit) so that, if armFastExitOnShutdown is armed, the fast exit preserves it instead of using the armed exit code.
````
