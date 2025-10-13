---
layout: default
title: Executing code asynchronously (promises)
parent: Advanced
grand_parent: Guides
---

# Executing code asynchronously (promises)

The execution of an OpenAF script is inherently sequential. Although it's easy to understand the execution flow (e.g. after a executes b) it might not have the best performance since it needs to wait for the end of the execution of the previous instruction to execute the next. Sometimes it makes sense because there is a dependency but in other cases it could be already executing something else asynchronously. OpenAF, through the Threads plugin, allows you access to the underneath great Java Threads functionality but the code may become hard to understand. An easy way to keep it simple but run asynchronously code is to use "promises". If you know how to use promises in other languages you will find it similar after checking the help information ("help $do"). For those that are not so familiar OpenAF tries to provide a easy and simple implementation.

You start be creating a promise for the code you want to run asynchronously:

````javascript
var promise = $do(() => { 
   // my code
});
````

The difference is that no matter what "my code" is OpenAF will return you immediately a promise object. "my code" will execute asynchronously a.s.a.p. and the promise object will be updated accordingly. But once "my code" executes you usually want to chain other actions. To chain more code you can use ".then":

````javascript
var promise = $do(() => { 
                 // my code
                 
                 return aResult;
              }).then((someResult) => {
                 // process the result

                 return processSuccess; 
              }).then((processStatus) => {
                 // etc... you get the point.
              });
````

What if any of these chained pieces of code throws an exception? At that point the promise won't be "fulfilled" but you can add ".catch" to handle it as you would do with a "try..catch":

````javascript
var promise = $do(() => { 
                 // my code
                 
                 return aResult;
              }).then((someResult) => {
                 // process the result

                 return processSuccess; 
              }).then((processStatus) => {
                 // etc... you get the point.
              }).catch((error) => {
                 // handle the error
              });
````

So, what can you do with a promise object?

  * You can wait for the end of the execution at any point blocking the current execution with $doWait(promise).
  * If you have an array of promise objects you can use $doFirst (waits for one of the promises to be "fulfilled") and $doAll (waits for all of the promises to be "fulfilled"). Both will return a single promise object that once "fulfilled" resumes the current execution.

How does that look like:

````javascript
var arrayOfPromises = [];
for (let idx in something) {
   arrayOfPromises.push($do( /* ... */ ));
}

// Yes, doFirst returns a promise, so you can chain more
arrayOfPromises.push($doFirst(arrayOfPromises)
                     .then(() => { 
                        print("One it's done!"); 
                     }));

var allPromises = $doAll(arrayOfPromises)
                  .then(() => {
                     print("Everything is done now!");
                  }));

/* do something else */

// Wait for all of them to finish
$doWait(allPromises);
````

Ok. But won't that just lunch a ton of threads "burning" down my machine? No. You don't need to worry about that. Underneath it will create a set of threads giving the number of identified compute cores and reuse them. So some promises will actually be waiting for others to finish and to have a thread available for them to execute.
In OpenAF there is also the function parallel4array and others to make it easy (and smarter) to asynchronously process an array since a promise for each might not actually give the best performance. But that will be the topic of another post.

## Virtual threads with `$doV`

OpenAF v20250721 introduces `$doV`, a drop-in replacement for `$do` that runs promise executors on Java virtual threads whenever they are available. Virtual threads are extremely lightweight and are ideal when you need to spawn hundreds or thousands of concurrent IO tasks without overwhelming the classic worker pools. Using `$doV` is as simple as swapping the function call:

````javascript
var promise = $doV(() => {
   var body = io.readUrl("https://example.org/service");
   return process(body);
}).then(saveResult)
  .catch($err);

$doWait(promise);
````

From an API perspective `$do` and `$doV` share the same chaining semantics, so you can pick the appropriate implementation per workload without refactoring your orchestration.

## Coordinating concurrent work with `$sync` and `$queue`

More helpers were added to simplify coordination between asynchronous tasks:

* `$sync()` creates a small wrapper that serialises access to a critical section. It is perfect to guard code that updates shared state from multiple promises.
* `$queue(initialItems)` yields a thread-safe queue that supports `add`, `poll`, `peek`, `has`, and other utility methods backed by `ConcurrentLinkedQueue`.

Combining both helpers allows you to build producer/consumer flows without leaving JavaScript:

````javascript
var work = $queue();
var syncStats = $sync();
var stats = [];

// Producer
$doV(() => {
   files.forEach(file => work.add(file));
});

// Consumers
var workers = [];
for (var i = 0; i < 4; i++) {
   workers.push($doV(() => {
      var next;
      while ((next = work.poll()) !== null) {
         var report = analyse(next);
         syncStats.run(() => stats.push(report));
      }
   }));
}

$doWait($doAll(workers));
````

In the previous snippet producers and consumers use virtual threads to keep latency low, while the `$sync` block ensures the shared `stats` collection stays consistent.
