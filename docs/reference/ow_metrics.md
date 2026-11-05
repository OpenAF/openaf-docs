---
layout: default
title: ow.metrics
parent: Reference
grand_parent: OpenAF docs
---

{% raw %}
## ow.metrics

[Source: `06414cd9`](https://github.com/OpenAF/openaf/blob/06414cd9204e918daa1e2971ce904783299db333/js/owrap.metrics.js) · [Baseline](../source-snapshot.md)

### ow.metrics.add

`ow.metrics.add(aName, aFunction)`

````text
Adds aName metric whose values are a map returned by aFunction.
````

### ow.metrics.collectMetrics

`ow.metrics.collectMetrics(aName, aFunction) : Object`

````text
Executes aFunction while collecting functions metrics under the name aName. Returns whatever the function returns or throws any exception.
````

### ow.metrics.collectMetrics4Fn

`ow.metrics.collectMetrics4Fn(aName, aFn)`

````text
Adds extra code to an existing aFn to collect functions metrics under the name aName. If the same aName and aFn has been already executed before it will throw an exception "Already collecting for the provided function."
````

### ow.metrics.exists

`ow.metrics.exists(aName) : Boolean`

````text
Determines if metric aName is currenly assigned.
````

### ow.metrics.fromObj2OpenMetrics

`ow.metrics.fromObj2OpenMetrics(aObj, aPrefix, aTimestamp, aHelpMap, aConvMap, aStrict) : String`

````text
Given aObj will return a string of open metric (prometheus) metric strings. Optionally you can provide a prefix (defaults to "metric")  and/or aTimestamp (a number in seconds or a label field, that will be used for all aObj values) and aConvMap composed of a key with a map of possible values and corresponding translation to numbers. Note: prefixes should not start with a digit. Set aStrict to true for OpenMetrics 1.0 text with grouped metadata and a final EOF marker. Strict mode supports unknown (default), gauge and counter scalar families, rejects name/series collisions and unsupported types, uses a prefix_id array label, and requires timestamps in epoch seconds (or a date label field).
````

### ow.metrics.fromOpenMetrics2Array

`ow.metrics.fromOpenMetrics2Array(aLines) : Array`

````text
Given an array or string newline delimited string following the OpenMetrics format  will try to return an array with each metric, value, labels, timestamp and perceived prefix.
````

### ow.metrics.getAll

`ow.metrics.getAll() : Map`

````text
Returns a map with all registered metrics.
````

### ow.metrics.getSome

`ow.metrics.getSome(anArrayOfNames) : Map`

````text
Returns just the metrics in the provided anArrayOfNames.
````

### ow.metrics.startCollecting

`ow.metrics.startCollecting(aChName, aPeriod, some, noDate)`

````text
Starts collecting metrics on aChName (defaults to '__metrics') every aPeriod ms (defaults to 1000ms) optionally just some (array) metrics.
````

### ow.metrics.stopCollecting

`ow.metrics.stopCollecting(aChName)`

````text
Stops collecting metrics on aChName (defaults to '__metrics')
````
{% endraw %}
