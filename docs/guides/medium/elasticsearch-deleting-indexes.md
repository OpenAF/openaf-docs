---
layout: default
title: Deleting ElasticSearch/OpenSearch indexes
parent: Medium
grand_parent: Guides
---

# Deleting ElasticSearch/OpenSearch indexes

This guide provides instructions on how to use OpenAF to delete specificing indexes on an ElasticSearch/OpenSearch cluster.

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

### 2.2 List the specific indexes that you want to remove

First you can get a glimpse of all the indexes:

````
> table $from(es.getIndices()).sort("index").select()
health│status│   index    │         uuid         │pri│rep│docs.count│docs.deleted│store.size│pri.store.size
──────┼──────┼────────────┼──────────────────────┼───┼───┼──────────┼────────────┼──────────┼──────────────
green │open  │data-2020-01│xm_jbvXZRl6e6nwDLhTH6w│1  │1  │132       │0           │80.3kb    │80.3kb
yellow│open  │data-2020-02│b5LYLrMnTKGkmPl7Y1Rj7A│2  │1  │2334      │2334        │112.1kb   │112.1kb
green │open  │data-2020-03│IJZSnbnaTOujaYxlpHm-HQ│1  │1  │62134     │0           │1.1mb     │1.1mb
green │open  │data-2020-04│ZOceFiU_RleQBZ6GV4jV1Q│1  │1  │10000     │0           │182.7kb   │182.7kb
green │open  │test        │37NeTq9bSpK8hiPZhMxP5Q│1  │1  │0         │0           │225b      │225b
[#5 rows]
````

Then focus on the ones you want:

````
> table $from(es.getIndices()).starts("index", "data-2020").select()
health│status│   index    │         uuid         │pri│rep│docs.count│docs.deleted│store.size│pri.store.size
──────┼──────┼────────────┼──────────────────────┼───┼───┼──────────┼────────────┼──────────┼──────────────
green │open  │data-2020-01│xm_jbvXZRl6e6nwDLhTH6w│1  │1  │132       │0           │80.3kb    │80.3kb
yellow│open  │data-2020-02│b5LYLrMnTKGkmPl7Y1Rj7A│2  │1  │2334      │2334        │111.8kb   │111.8kb
green │open  │data-2020-03│IJZSnbnaTOujaYxlpHm-HQ│1  │1  │62134     │0           │1.1mb     │1.1mb
green │open  │data-2020-04│ZOceFiU_RleQBZ6GV4jV1Q│1  │1  │10000     │0           │182.7kb   │182.7kb
green │open  │test        │37NeTq9bSpK8hiPZhMxP5Q│1  │1  │0         │0           │225b      │225b
[#5 rows]
````

You can filter by "starts", "ends", "contains" and "match" (which allows you to use a regular expression). You can check out other options in ([OpenAF $from](../../concepts/OpenAF-nLinq.md)))

### 2.3 Deleting indices

After you filtered the indexes you want, on the previous list, you can now execute the __deleteIndex__ function for each by introducing a new argument to the previous _select_ function:

````javascript
> $from(es.getIndices()).starts("index", "data-2020").select(r => es.deleteIndex(r.index))
─ acknowledged: true
─ acknowledged: true
─ acknowledged: true
─ acknowledged: true
````

> You will get an "acknowledged" result per each index you tried to delete.

You can now repeat the listing commands, from 2.2, to check the new listing.

---

If you want to try out deleting some dummy indexes before performing the real operation you can create them by executing:

````javascript
> es.createIndex("mytest-2020-01", 1, 1)
> es.createIndex("mytest-2020-02", 1, 1)
> es.createIndex("mytest-2020-03", 1, 1)
````

> The arguments of createIndex are: name of index to create; number of primary shards; number of replica shards
