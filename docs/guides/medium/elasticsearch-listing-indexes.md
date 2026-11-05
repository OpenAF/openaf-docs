---
layout: default
title: Listing ElasticSearch/OpenSearch indexes
parent: Medium
grand_parent: Guides
---

# Listing ElasticSearch/OpenSearch indexes

This guide provides instructions on how to use OpenAF to produce a list of the current indexes on an ElasticSearch/OpenSearch cluster.

## 1. Installing the ElasticSearch oPack

The ElasticSearch oPack provides wrappers around commonly used ElasticSearch/OpenSearch functionality. To install it with OpenAF just execute:

````bash
./opack install ElasticSearch
````

## 2. Using the OpenAF console

The easiest way to have a quick glance at the list of ElasticSearch/OpenSearch indexes is to connect to the cluster given the provided URL and user & password (if no anonymous access is permitted):

````sh
$ ./oafc
> loadLib("elasticsearch.js")
````

### 2.1 Connecting

Then if you don't have any credentials:

````javascript
> var es = new ElasticSearch("https://[the cluster URL]")
````

If you do have credentials:

````javascript
> var es = new ElasticSearch("https://[the cluster URL]", "user", "password")
````

### 2.2 Listing

To list the available indices just execute:

````javascript
> table es.getIndices()
````

You can sort the table by different fields. By index:

````
> table $from(es.getIndices()).sort("index").select()
health│status│   index    │         uuid         │pri│rep│docs.count│docs.deleted│store.size│pri.store.size
──────┼──────┼────────────┼──────────────────────┼───┼───┼──────────┼────────────┼──────────┼──────────────
green │open  │data-2020-01│xm_jbvXZRl6e6nwDLhTH6w│1  │1  │132       │0           │80.3kb    │80.3kb
yellow│open  │data-2020-02│b5LYLrMnTKGkmPl7Y1Rj7A│2  │1  │2334      │2334        │111.8kb   │111.8kb
green │open  │data-2020-03│IJZSnbnaTOujaYxlpHm-HQ│1  │1  │62134     │0           │1.1mb     │1.1mb
green │open  │data-2020-04│ZOceFiU_RleQBZ6GV4jV1Q│1  │1  │10000     │0           │182.7kb   │182.7kb
green │open  │test        │37NeTq9bSpK8hiPZhMxP5Q│1  │1  │0         │0           │225b      │225b
[#5 rows]
````

By size:

````
> table $from(es.getIndices(true)).sort("primaryStoreSize").select()
health│status│   index    │         uuid         │primaryShards│replicas│docsCount│docsDeleted│storeSize│primaryStoreSize
──────┼──────┼────────────┼──────────────────────┼─────────────┼────────┼─────────┼───────────┼─────────┼────────────────
green │open  │test        │37NeTq9bSpK8hiPZhMxP5Q│1            │1       │0        │0          │225      │225
green │open  │data-2020-01│xm_jbvXZRl6e6nwDLhTH6w│1            │1       │132      │0          │82317    │82317
yellow│open  │data-2020-02│b5LYLrMnTKGkmPl7Y1Rj7A│2            │1       │2334     │2334       │114540   │114540
green │open  │data-2020-04│ZOceFiU_RleQBZ6GV4jV1Q│1            │1       │10000    │0          │187169   │187169
green │open  │data-2020-03│IJZSnbnaTOujaYxlpHm-HQ│1            │1       │62134    │0          │1249635  │1249635
````

> Passing the argument "true" on the getIndices function makes sure that the resulting size values are in bytes (for proper sorting) instead of human readable units

By documents:

````
> table $from(es.getIndices()).sort("docsCount").select()
health│status│   index    │         uuid         │pri│rep│docs.count│docs.deleted│store.size│pri.store.size
──────┼──────┼────────────┼──────────────────────┼───┼───┼──────────┼────────────┼──────────┼──────────────
green │open  │data-2020-01│xm_jbvXZRl6e6nwDLhTH6w│1  │1  │132       │0           │80.3kb    │80.3kb
green │open  │test        │37NeTq9bSpK8hiPZhMxP5Q│1  │1  │0         │0           │225b      │225b
green │open  │data-2020-03│IJZSnbnaTOujaYxlpHm-HQ│1  │1  │62134     │0           │1.1mb     │1.1mb
yellow│open  │data-2020-02│b5LYLrMnTKGkmPl7Y1Rj7A│2  │1  │2334      │2334        │111.8kb   │111.8kb
green │open  │data-2020-04│ZOceFiU_RleQBZ6GV4jV1Q│1  │1  │10000     │0           │182.7kb   │182.7kb
[#5 rows]
````

By index and reverse documents order:

````
> table $from(es.getIndices()).sort("index", "-docsCount").select()
health│status│   index    │         uuid         │pri│rep│docs.count│docs.deleted│store.size│pri.store.size
──────┼──────┼────────────┼──────────────────────┼───┼───┼──────────┼────────────┼──────────┼──────────────
green │open  │data-2020-01│xm_jbvXZRl6e6nwDLhTH6w│1  │1  │132       │0           │80.3kb    │80.3kb
yellow│open  │data-2020-02│b5LYLrMnTKGkmPl7Y1Rj7A│2  │1  │2334      │2334        │112.1kb   │112.1kb
green │open  │data-2020-03│IJZSnbnaTOujaYxlpHm-HQ│1  │1  │62134     │0           │1.1mb     │1.1mb
green │open  │data-2020-04│ZOceFiU_RleQBZ6GV4jV1Q│1  │1  │10000     │0           │182.7kb   │182.7kb
green │open  │test        │37NeTq9bSpK8hiPZhMxP5Q│1  │1  │0         │0           │225b      │225b
[#5 rows]
````

There are many ways to filter and sort these listings. You can see more in [OpenAF $from](../../concepts/OpenAF-nLinq.md).

### 2.3 Exporting the list to CSV

Any of the results you got previously you can export them to a CSV file:

````javascript
$csv().toOutFile("list.csv").fromInArray( es.getIndices(true) )
````

list.csv:
````csv
health,status,index,uuid,primaryShards,replicas,docsCount,docsDeleted,storeSize,primaryStoreSize
green,open,data-2020-01,xm_jbvXZRl6e6nwDLhTH6w,1.0,1.0,132.0,0.0,82317.0,82317.0
green,open,test,37NeTq9bSpK8hiPZhMxP5Q,1.0,1.0,0.0,0.0,225.0,225.0
green,open,data-2020-03,IJZSnbnaTOujaYxlpHm-HQ,1.0,1.0,62134.0,0.0,1249635.0,1249635.0
yellow,open,data-2020-02,b5LYLrMnTKGkmPl7Y1Rj7A,2.0,1.0,2334.0,2334.0,114870.0,114870.0
green,open,data-2020-04,ZOceFiU_RleQBZ6GV4jV1Q,1.0,1.0,10000.0,0.0,187169.0,187169.0
````

> You can use any of the previous commands within the function "fromInArray( ... )" to export to CSV the results you need.
