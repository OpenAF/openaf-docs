---
layout: default
title: Using ElasticSearch
parent: Advanced
grand_parent: Guides
---

# Using ElasticSearch

OpenAF comes with builtin support for ElasticSearch. So, among other things, it can log directly to ElasticSearch whenever you use the _log*_ functions. Nevertheless there is an oPack to make it all a little easier. Let's start by installing it:

````sh
$ opack install elasticsearch
````

The ElasticSearch oPack is basically a wrapper around some ElasticSearch functionality aiming to make easier daily ElasticSearch operations (e.g. creating/deleting indexes, export/import data, reindex indexes, etc&#46;&#46;&#46;). We are going to describe some basic functionality. To start you need to instantiate an object poiting to your ElasticSearch cluster:

````javascript
load("elasticsearch.js");
var es = new ElasticSearch("http://my.elastic.cluster:9200", "myUser", "myPassword");
````

_Note: the user and password are optional and only needed if your ElasticSearch cluster is protected with user/password._

## Creating an index

To create an index you just need to:

````javascript
> es.createIndex("test", 1, 1);
````

This will create a new index "test" with 1 primary shard and 1 replica. This operation isn't usually necessary as ElasticSearch will just create any index you try to use.

You can check that it was created by executing:

````javascript
> es.getIndices()
````

And checking the resulting array.

## Adding/Changing data

To interact with ElasticSearch at the data level the easiest way in OpenAF is to use an OpenAF channel. To easily create an OpenAF channel to connect to the "test" index just execute:

````javascript
es.createCh("test", ["canonicalPath"], "testCh");
````

This creates an OpenAF channel "testCh" that allows you to access the test index. You also need to provide a list of keys that can be used to retrieve an unique record (in this case "canonicalPath").

_Note: You can also define a pattern of indexes instead of the exact name but you will be limited just to .get* functions. It's also possible instead of a string to provide a function that returns the name of the ElasticSearch index to use (e.g. for example, appending the current date)._

To add new data just use the newly created channel:

````javascript
$ch("testCh").set({
    canonicalPath: "/",
}, {
    isDirectory: true,
    isFile: false,
    filename: "noname",
    filepath: "/",
    canonicalPath: "/",
    lastModified: 0,
    createTime: 0,
    size: 0
});
````

## Retriving data

If you know how to use OpenAF channels now it becomes easier. To get a map value you just need:

````javascript
var fileMap = $ch("test").get({ canonicalPath: "/" });
````

## Batch get/set data

To batch insert/change data into ElasticSearch you need to divide all the requests in smaller chuncks of data. Then you just use the _.setAll_ function:

````javascript
$ch("test").setAll(["canonicalPath"], io.listFiles("/some/path").files);
````

To obtain a list of keys or values you can use _getAll_ or _getKeys_:

````javascript
var q = (m, s) => { return { size: s, query: { query_string: { query: m }}}; };
var listOfSmallFiles = $ch("test").getAll(q("size:<1 AND ", 1000));
````

Unlike the usual _getAll_ and _getKeys_ behaviour the elasticsearch OpenAF channel type will only retrieves a specific amount of records (default to 10). In this example we created a small function to allow you to query using Lucene query syntax and specifying the limit number of records you wish to retrieve (within the search API limits). Check the [ElasticSearch search API](https://www.elastic.co/guide/en/elasticsearch/reference/current/search-search.html) for more.

## Delete data

To delete data simply use the unset/unsetAll functions:

````javascript
$ch("test").unset({ canonicalPath: "/" });
````
