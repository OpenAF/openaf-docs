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
