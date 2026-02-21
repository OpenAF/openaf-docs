---
layout: default
title: OpenAF Channels
parent: Concepts
grand_parent: OpenAF docs
---
# OpenAF Channels

## What are channels?

By definition, channels should allow the flow of data between functionalities or processes. In a similar way, OpenAF channels allow data to flow between two points or functionalities. These two points can be in the same OpenAF script or in two different scripts (on the same machine or on different machines).

Let's consider a simple example: _Imagine that you have a script, called copyFiles.js, that copies files between a SFTP server and a local server. Additionally you have a preProcess.js script that will pre-process the copied files whenever they are copied. How do you make the name of the copied files “flow” to the preProcess.js script? You can build a channel between copyFiles.js and preProcess.js._

## How is data represented on a channel?

Data in OpenAF channels is represented by a set of key/value pairs. This set can be handled as a Map (where you can invoke get/set methods) or as a Queue (where you can invoke push/pop/shift methods), based on the order in which a key/value was added or modified.

The keys and values used can be simple Strings or JSON Maps.

Using the example: _For every copied file the copyFiles.js script can set a key/value pair like the following_: 

````javascript
Key = { "filename": "someData1234.dat" }
 
Value = { 
    "filename": "someData1234.dat",
    "filepath": "/some/input/folder/someData1234.dat",
    "dateReceived": "2016-12-02 12:34:56",
    "dateCopied": "2016-12-02 12:35:05"
}
````

Then preProcess.js can simply invoke the shift method on the same channel to obtain the first key/value pair added to the channel. 

## How to be notified of a change on a channel?

If a channel allows data to flow between two points, how does the target point know that the source point has added or changed data in the channel? The answer is channel subscription. For any given OpenAF channel, you can subscribe a function so it can be called whenever data is added or changed.

These subscriptions are non-blocking meaning that changing data on a channel won't be delayed by the subscriptions it holds at any given point. Each subscription will actually be executed on a separate thread in parallel.

At any time, you can unsubscribe a previous channel subscription.

Using the example: _copyFiles.js will add a key/value pair for each file it successfully copies in a "CopiedFiles" channel. preProcess.js just needs to subscribe to "CopiedFiles". Each time copyFiles.js adds a file, the provided preProcess.js function will be executed without delaying copyFiles.js functionality._

## Channels implementations

OpenAF channels can have different implementations on how the key/value set is stored and shared while maintaining the same interface methods. This means that, as a general rule, whatever implementation a channel uses the get/set/push/pop/etc… methods should be available.

Currently there are several different implementations built-in (on the included OpenWrap Channel library):

* Big (default until 20181210)
* DB
* Ignite
* Ops
* Remote
* Cache
* ElasticSearch
* MVS
* Simple (default from 20181210)
* File
* Buffer
* Proxy
* Etcd
* Prometheus
* All
* Dummy (for testing)

And some available through oPacks:

* Mongo (`mongo`, Mongo oPack)
* Etcd3 (`etcd3`, etcd3 oPack, via GRPC)
* Redis (`redis`, Redis oPack)
* RocksDB (`rocksdb`, rocksdb oPack)
* S3 (`s3`, S3 oPack)
* Chronicle Queue (`cq`, cq oPack)
* GIST (`gist`, GIST oPack)
* DynamoDB (`dynamo`, AWS oPack)
* AWS Secrets Manager (`awssecrets`, AWS oPack, primarily for `$sec`)
* Lucene Vector Search (`vectordb`, lucene oPack)
* Lucene Full-text Search (`searchdb`, lucene oPack)

You can find runnable examples for all oPack channel implementations in [OpenAF channel implementations through oPacks](../guides/medium/openaf-channel-implementations-through-opacks.md).

The default implementation, until version 20181210, Big uses the OpenWrap Big Objects functionality (from the OpenWrap Object library). You don't need to know how this functionality works internally. For the sake of simplicity let's assume it's like an internal JavaScript Array of a Map with a Key and Value.

The remote implementation allows for the creation of a channel whose implementation is held on a different OpenAF script that can be accessed for a REST API. We will get into the details of how this is done and setup later but this implementation is important to access channels with local script storage (like the default implementation is). 

### Channel basics

To access the channel functionality you can use functions in the ow.ch (OpenWrap Channel) library or the common shortcuts: $channel or $ch. We will use the $ch to show the channels basics.

`$ch` is a JavaScript function that takes the unique name of a channel as its parameter. This name only needs to be unique within a single OpenAF script.

#### Channel maintenance

Before using a channel you always need to create it. 

````javascript
> $ch("mychannel").create() // default
> $ch("mychannel").create(true, "myimpl", {"option1": "value1"}) // to create a channel with a myimpl implementation
````

You can list the current created channels by: 

````javascript
> $ch().list()
````

When you no longer need a channel and corresponding data you can destroy it by: 

````javascript
> $ch("mychannel").destroy()
````

#### Channel value get/set/unset

You can add/set a key/value on a channel by: 
````javascript
> $ch("mychannel1").set(1, "hello")
> $ch("mychannel1").set(2, "hello")
````

The keys and values can be string, numbers or maps:

````javascript
> $ch("mychannel").set({date: "20100601", person: "me"}, {data: ... })
````

You can add an array of map entries just indicating which map entries should be considered for keys

````javascript
> $ch("mychannel").setAll(["date", "person"], anArrayOfData)
````

In a similar way to *setAll* you can also remove entries:

````javascript
> $ch("mychannel").unsetAll(["date", "person"], anArrayOfData)
````

To retrieve data you simply use the full key:

````javascript
> $ch("mychannel1").get(1)
> $ch("mychannel").get({date: "20100601", person: "me"})
````

To delete any entry just use the full key again:

````javascript
> $ch("mychannel").unset(1)
> $ch("mychannel").unset({date: "20100601", person: "me"})
````

To get a list of all the keys of a channel:

````javascript
> $ch("mychannel").getKeys()
> $ch("mychannel").getSortedKeys() // by the last changes
````

You can use the list of keys of a channel to also delete all entries:

````javascript
> $ch("mychannel").unsetAll(["date", "person"], $ch("mychannel").getKeys())
````

To get all elements of a channel:

````javascript
> $ch("mychannel").getAll()
````

To get the number of elements in a channel:

````javascript
> $ch("mychannel").size()
````

If you need to check and set an entry in one single “transaction” you just need to provide the value map element that needs to be checked and if true set the entry with the new value (usually to ensure that just one thread will actually change an entry):

````javascript
> $ch("mychannel").getSet({status: "toExecute"}, {jobId: 123}, { jobId: 123, runCommand: "processStuff.sh", status: "executing"})
````

Note: Usually it's a good practice to have the key elements as part of the value also thus setAll keeps the key elements also on the value map for each array element. 

#### Using a channel as a queue

Ordering in channels is, by default, over the last modify time stamps. To retrieve the first element removing it from the channel: 

````javascript
> var myvalue = $ch("mychannel").shift()
````

To remove the last:

````javascript
> var myvalue = $ch("mychannel").pop()
````

You can even add new elements using push:

````javascript
> $ch("mychannel").push(myvalue)
````

#### Channel forEach

To execute a function over all elements:

````javascript
> $ch("mychannel").forEach(function(key, value) {
    // do stuff with key and value
})
````

#### Channel subscription

One of the most important functions of a channel is the ability to subscribe it for any change: 

````javascript
> $ch("mychannel").subscribe(function(aChannelName, aOperation, aKeyOrKeys , aValueOrValues) { ... }, onlyFromNowOn)
````

The subscribe function will receive: 
* aChannelName identifying the channel (only useful when you want to use a generic subscribing function);
* aOperation which will have a value of “set”, “setall” or “unset”;
* aKeyOrKeys representing the key or keys for the setall operation;
* aValueOrValues representing the value or values for the setall operation.

Once a function is provided subscribing a channel, it will be executed with a “set” operation for all existing elements (thus syncing all existing channel elements). You can override this behavior by setting onlyFromNowOn to true.

The subscribing function will always run in a separate thread so that the channel basic set, setall and unset operations performance is not directly affected by the number or performance of the subscribing functions. This is currently by design option.

For each subscribe instruction a corresponding UUID will be returned. You can use this UUID to unsubscribe the function from the channel if needed: 

````javascript
> $ch("mychannel").unsubscribe(anUUID)
````

In advanced implementations you can also stop all subscribing functions running (called jobs) by executing:

````javascript
> $ch("mychannel").stopJobs()
````

This is usually only helpful when you want to stop a channel and all subscribing functions quickly. Otherwise if you just want to know when all current jobs finish you can use:

````javascript
> $ch("mychannel").waitForJobs(aLimitTimeout)
````

#### Persisting Channel values

A simple subscribe function is to keep an update filesystem copy of the channel values. There is a simple basic implementation built in. To add the built in subscribe function to a channel just execute:

````javascript
> $ch("mychannel").storeAdd("mychannel.channel", ["date", "person"])
````

This will also check if the file already exists and restore values from it so you need to provide the list of values to use as key. The contents are compressed by default and it's just a simple JSON file meaning you could use this function to read and maintain JSON file based data, for example. You can even create channels with different keys over the same data.

To just restore the values just use:

````javascript
> $ch("mychannel").storeRestore("mychannel.channel", ["date", "person"]) 
````

Do be aware that there is no locking mechanism preventing access to the file and that current implementation (e.g. memory, database, remote, etc…) contents will always override the filesystem values except, of course, on the initial data restore. So changing the file while a channel is “live” won't change it and on the next set/unset/setall all data on the file will be overwritten. For these reasons it's suitable to be used for small/medium size channels depending on the values size and keeping channel data always preserved. If you are looking for a solution to store large sized channels you can either use getAll or forEach to save them when needed or build a more sophisticated subscribe function (for example: keeping each value as a separate file on a folder structured indexed by keys).

#### Details specific to each implementation

### DB

The DB implementation wraps a database table/object and maps channel operations to SQL statements.

Use channel type `db`.

Creation options:

| Option | Mandatory? | Type | Description |
|--------|------------|------|-------------|
| `db` | Yes | `DB` object, map or JSSLON string | Database connection. If you pass a map/string (`url`, `user`, `pass`, `timeout`, optional `driver`) the channel creates the `DB` object internally and closes it on `destroy()`. |
| `from` | Yes | String | Table name (or SQL object). |
| `keys` | No | Array | Key fields used to build `WHERE` clauses for `get`/`set` (update)/`unset`. |
| `cs` | No | Boolean | Case-sensitive table/field handling (defaults to `false`). |

Behavior notes:

* `set(key, value)` performs an upsert pattern:
  * updates when a matching row exists;
  * inserts otherwise (using fields from `value`).
* If `keys` is defined, only those key fields are used for matching/deleting.
* `getKeys(full)` accepts an optional SQL `WHERE` string.
* `getAll(full)` accepts an optional map for equality filters.
* `destroy()` only releases channel resources; it does not remove table data.

Current limitations/nuances in this implementation:

* `getSet(...)` is not implemented for `db`.
* `getSortedKeys()` currently behaves like `getKeys()` (no extra sorting logic).
* `pop()`/`shift()` depend on the order returned by `getKeys()` from the database.

Example:

````javascript
var db = new DB("jdbc:h2:./data", "sa", "sa");
$ch("employees").create(1, "db", {
  db: db,
  from: "employees",
  keys: ["id"],
  cs: false
});

$ch("employees").set({ id: 1 }, {
  id: 1,
  first_name: "John",
  last_name: "Doe"
});

var row = $ch("employees").get({ id: 1 });
$ch("employees").unset({ id: 1 });
````

### Ignite

The Ignite implementation encapsulates access to an Ignite data grid using functionality from the Ignite plugin. Upon creation the shouldCompress is ignored and the options available are not mandatory:

* *gridName* - The Ignite grid name to access
* *ignite* - An Ignite object from the Ignite plugin that you previously instantiated.
* *persist* - Optional filesystem path to enable Ignite persistence and WAL storage.
* *client* - Optional client mode flag used when connecting to a specific gridName.

The name of the channel is actually the name of Ignite data grid cache that will be used. All functionality is available.

### Ops

The ops (operations) implementation is a special channel that does not store values. Instead, it executes a specific function for each key and returns the corresponding value (for example, useful for exposing functionality). That function receives the value map as an argument. On creation, `shouldCompress` is ignored, and the options are the map of functions, as shown in the next example:

````javascript
$ch("myops").create(1, "ops", {
    "help": () => { return { "add": "Add an argument a with b" } },
    "add" : (v) => { return { result: v.a + v.b }; }
});
````

Then to use it:

````javascript
> $ch("myops").get("help");
{
    "add": "Add an argument a with b"
}
> $ch("myops").set("add", { a: 2, b: 3 });
{
    "result": 5
}
````

Due to the nature of this implementation setAll, pop, shift and unset are not implemented and will just execute returning undefined.

### Cache

The cache implementation lets you define a channel that uses a provided function to retrieve and return the value for a given key. The value is kept in another OpenAF channel acting as a cache, where it is reused for a specific TTL (time-to-live) in ms. After the TTL expires, the function runs again and the new result is cached. This is useful when you expect many `get` operations, but retrieving each value is slow.

To create, the shouldCompress option is ignored and the following options can be used:

| Option | Mandatory | Type | Description |
|--------|-----------|------|-------------|
| func | Yes | Function | The function that receives a key and returns the corresponding value to be returned and cached for a TTL. |
| ttl | No | Number | The cache time-to-live in ms (defaults to 5 seconds) |
| ch | No | String/Channel | The name (or channel object) of the secondary OpenAF channel to store cached values. Defaults to current name suffixed with "::__cache". Note: Upon "destroy" of the cache channel this channel will be also destroyed. |
| size | No | Number | Maximum number of cached entries (`-1` means unlimited). |
| method | No | String | Cache policy: `"t"` (TTL-based, default) or `"p"` (promote/reorder on access). |
| default | No | Any | Default value to return when `useDefault` is enabled and a refresh is in progress. |
| useDefault | No | Boolean | If true, cache refresh can happen asynchronously while returning `default` (or previous value depending on path). |

The `set`/`setAll` functions ignore the provided value and call the function with the provided key, updating the cached value and resetting the current TTL.

### ElasticSearch

The ElasticSearch implementation encapsulates the access to an ElasticSearch server/cluster. Pretty much all OpenAF channel functionality is available and there are some extensions to enable the use of ElasticSearch functionality. On creation, the shouldCompress is ignored but the options map should contain:

| Option | Mandatory | Type | Description |
|--------|-----------|------|-------------|
| index | Yes | String/Function | The ES index string or a function that returns the name (see also ow.ch.utils.getElasticIndex) |
| format | No | String | If `index` is a string, optional format pattern used by `ow.ch.utils.getElasticIndex`. |
| idKey | No | String | If the ES index uses an id field you can specify it (defaults to `'id'`). |
| url | Yes | String | The URL string to access the ES cluster/server using HTTP/HTTPs |
| user | No | String | If the ES cluster/server requires authentication credentials, you can specify the username. |
| pass | No | String | If the ES cluster/server requires authentication credentials, you can specify the password (encrypted or not). |
| fnId | No | String/Function | Optional id generator for document ids. If string, uses hash function name (e.g. md5/sha1/sha256/sha512). |
| size | No | Number | Optional limit used by getAll/getKeys when no explicit query map is provided. |
| stamp | No | Map | Optional map merged into keys/values on set operations and used to scope default search filters. |
| seeAll | No | Boolean | If `stamp` is set, controls whether getAll/getKeys should ignore (`true`) or apply (`false`) stamp filter. |
| timeout | No | Number | Request timeout in ms. |
| preAction | No | Function | Function called before each HTTP request. |
| throwExceptions | No | Boolean | If true, REST errors throw exceptions (defaults to false). |

Examples:

````javascript
> $ch("myvalues").create(1, "elasticsearch", { url: "http://es.local", index: "myvalues" });
> $ch("values").create(1, "elasticsearch", { url: "http://es.local", index: ow.ch.utils.getElasticIndex("value", ow.ch.utils.getElasticIndex("values", "yyyy.w"))});
````

The getAll/getKeys functions accept an extra argument to provide an ES query map to restrict the results.

Nevertheless please use the ElasticSearch oPack that encapsulates more functionality not available through the OpenAF channel implementation and enables the easy creation of ElasticSearch channels.

### MVS

MVS (MVStore) is a "persistent, log structured key-value store" and the storage subsystem used by H2. It is fast, small, and a good alternative to keeping channel data only in memory, although it can also run in-memory. The `shouldCompress` option specifies whether the entire data structure should be compressed by MVS. Most channel functionality is available. You can also specify the following options:

| Option | Mandatory | Type | Description |
|--------|-----------|------|-------------|
| file   | No | String | Specifies the file where MVS will store data to. If not defined it stores data in-memory. |
| compact | No | Boolean | If yes upon channel creation/destruction it will run the MVS compact operation over the file trying to save storage space. |
| map | No | String/Function | If not defined, defaults to `"default"`. Each file can contain several collections (maps) of values. If defined as a function, it receives the key in use as an argument and should return the map name to use (for example, useful for sharding) and a default map name when a key is not provided. |
| closeOnShutdown | No | Boolean | If true (default), closes/destroys the channel automatically on OpenAF shutdown. |
| internalTrim | No | String | Optional stringify indentation/trim behavior for stored keys/values (advanced usage). |

Examples:

````javascript
> $ch("test").create(1, "mvs"); // Creates an in-memory mvs channel for map 'default'
> $ch("mymap").create(1, "mvs", { map: "mymap" }); // Creates an in-memory mvs channel for map 'mymap'
````

````javascript
// Creates a mvs file 'myfile.db' with a map 'mymap'
$ch("myfile").create(1, "mvs", { file: "myfile.db", map: "mymap" });

// Creates a mvs file 'myfile.db' with distributing values using the field date from the key to map names like "logs-yyyy.MM.dd"
var func = (key) => { 
    key = _$(key).isMap().default({}); 
    var d = _$(key.date).isDate().default(new Date); 
    
    return "logs-" + ow.format.fromDate(d, "yyyy.MM.dd"); 
};
$ch("myfile").create(1, "mvs", { file: "myfile.db", map: func });
````

**Note:** function based map channels should only be used for adding/modifying values. For accessing you should create specific channels for the specific map name. Keep in mind that MVS supports concurrent read and write.

There are utility functions for MVS files in `ow.ch.utils.mvs.*`, namely:

* *list(aFile)* - returning an array with all maps contained on a MVS file.
* *remove(aFile, aMapToRemove)* - deleting any map contained on a MVS file.
* *rename(aFile, oldMapName, newMapName)* - to rename an existing map contained on a MVS file.

### Simple

The simple implementation, default since version 20181210, uses plain JavaScript objects (for example, arrays and maps) instead of OpenWrap Big Objects. It improves add/modify performance, but can use more memory overall for large or variable-size values. All functionality is available, and behavior should be similar to the default implementation, although `shouldCompress` is ignored.

To create one just:

````javascript
> $ch("test").create(1, "simple")
````

### File

The file implementation keeps channel data in JSON or YAML files, either in one file or split across multiple files.

Creation options:

| Option | Mandatory | Type | Description |
|--------|-----------|------|-------------|
| file | No | String | File path to store channel data (single-file mode). |
| path | No | String | Base path used for generated files (especially in multifile mode). |
| yaml | No | Boolean | Use YAML instead of JSON (default `false`). |
| compact | No | Boolean | JSON compact output (defaults to `shouldCompress`). |
| multifile | No | Boolean | Store each value in an individual file plus an index file. |
| multipart | No | Boolean | For YAML output, write/read multi-document YAML. |
| key | No | String | If key map contains this property, it is used as effective channel key. |
| multipath | No | Boolean | Treat string keys containing dots as object paths. |
| lock | No | String | Lock file path used for filesystem locking while accessing data. |
| gzip | No | Boolean | Enable gzip compression for persisted file(s). |
| lz4 | No | Boolean | Enable lz4 compression for persisted file(s). |
| tmp | No | Boolean | Use temporary backing file and remove it on destroy/process end. |

### Buffer

The buffer implementation acts as a "proxy" to another channel. It can buffer values for a specific time and/or number of values before sending it to a target channel.

To create one just:

````javascript
> $ch("buffer").create(1, "buffer", {
    bufferCh      : "targetCh",
    bufferIdxs    : [ "key1", "key2" ],
    bufferByTime  : 2500,
    bufferByNumber: 100,
    bufferTmpCh   : "buffer::__buffer"
});
````

The options used are:

| Option | Mandatory | Type | Description |
|--------|-----------|------|-------------|
| bufferCh | Yes | String | Target channel to receive flushed entries. |
| bufferIdxs | No | Array | Index fields used to flush through `setAll` (default `[]`). |
| bufferByTime | No | Number | Flush interval in ms (default `2500`). |
| bufferByNumber | No | Number | Flush threshold by number of buffered entries (default `100`). |
| bufferTmpCh | No | String | Temporary buffer storage channel name (default `<name>::__bufferStorage`). |
| bufferFunc | No | Function | Optional function that can force a flush when returning true. |
| timeout | No | Number | Timeout in ms used by flush/close helpers (default `1500`). |
| errorFn | No | Function | Optional error callback when forwarding buffered entries fails. |

### Proxy

This implementation allows to intersect channel request to another target channel. It can be useful to collect channel usage statistics using *ow.ch.utils.getStatsProxyFunction*.

To create a proxy just:

````javascript
> $ch("proxy").create(1, "proxy", {
    chTarget  : "targetCh".
    proxyFunc : function(aMap) { 
        // Function that receives a map (by reference that can be changed)
        // with: op (operation), name (target channel), function (where 
        // applicable), full (where applicable), match (the match of getSet),
        // k (the key(s)), v (the value(s)) and timestamp. If this function 
        // returns something no operation will be executed on the chTarget 
        // and the value returned by the function will be the value returned 
        // by this channel.
    }
});
````

### Etcd

This OpenAF channel implementation interacts with a [Etcd](https://etcd.io) cluster through HTTP/HTTPs. You can use the Etcd3 oPack to interact via GRPC.

To create an etcd channel just:

````javascript
> $ch("etcd").create(1, "etcd", {
    url: "http://my.etcd.cluster:2379",
    folder: "myFolder",
    throwExceptions: false,
    default: { result: 0 }
});
````

The options used are:

| Option | Mandatory | Type | Description |
|--------|-----------|------|-------------|
| url | Yes | String | The URL to connect to the Etcd cluster |
| folder | No | String | The key prefix to use. |
| throwExceptions | No | Boolean | If true, whenever there is an error (e.g. communication error, etc...) an exception will be thrown. |
| default | No | Map | If throwExceptions is false what should be returned on a get function in case of error. |
| preAction | No | Function | Function called before each HTTP request. |

### Prometheus

This implementation connects channels to Prometheus query APIs and/or Pushgateway ingestion.

Creation options:

| Option | Mandatory | Type | Description |
|--------|-----------|------|-------------|
| urlQuery | No* | String | Prometheus server URL used for read/query operations. |
| urlPushGW | No* | String | Prometheus Pushgateway URL used for write/delete operations. |
| prefix | No | String | Optional metrics prefix for openmetrics payload generation. |
| gwGroup | No | Map | Grouping labels for Pushgateway endpoints (must include `job` when `urlPushGW` is used). |
| helpMap | No | Map | Optional help metadata map forwarded to `ow.metrics.fromObj2OpenMetrics`. |

\* At least one of `urlQuery` or `urlPushGW` must be defined.

Behavior notes:

* `forEach`, `getSet`, `pop`, `shift`, `unsetAll` are not supported.
* `set`/`setAll` use the value payload and ignore the key argument.
* `getAll` supports:
  * instant query (`{ query }`);
  * range query (`{ query, start, end }`);
  * label values (`{ label }`).

### All

This implementation aggregates multiple target channels behind a single channel.

Creation options:

| Option | Mandatory | Type | Description |
|--------|-----------|------|-------------|
| chs | No | Array | Array of channel names to aggregate. |
| fn | No | Function | Routing function receiving operation/key/value; can return one or more target channels. |
| errFn | No | Function | Error callback `(name, error, targetCh, operation, args)`. |
| fnTrans | No | Function | Key translation function before forwarding to target channels. |
| fnKeys | No | Function | Post-processing function for aggregated `getKeys`/`getSortedKeys`. |
| fnValues | No | Function | Post-processing function for aggregated values (`getAll`, `get`, `set`, etc.). |
| treatAll | No | Boolean | If true, executes size/setAll/unsetAll per-entry/per-channel behavior (default `false`). |

### Dummy

In this implementation, all operations simply return without executing anything. It is mainly used for testing purposes.

### Mongo (through the Mongo oPack)

Use channel type `mongo` (Mongo oPack).

Examples:
* [Accessing MongoDB](../guides/medium/accessing-mongodb.md)
* [OpenAF channel implementations through oPacks](../guides/medium/openaf-channel-implementations-through-opacks.md)

### Etcd3 (through the Etcd3 oPack)

This implementation differs from the "etcd" implementation since it will communicate via GRPC instead of HTTP.

Use channel type `etcd3` (etcd3 oPack).

Examples:
* [OpenAF channel implementations through oPacks](../guides/medium/openaf-channel-implementations-through-opacks.md)
* [oafp with OpenAF channels](../guides/oafp/with-oaf-ch.md)

### Dynamo (through the AWS oPack)

This implementation uses the AWS API directly to interact with AWS's Dynamo DB.

Use channel type `dynamo` (AWS oPack).

Examples:
* [OpenAF channel implementations through oPacks](../guides/medium/openaf-channel-implementations-through-opacks.md)

### Redis (through the Redis oPack)

Use channel type `redis` (Redis oPack).

Examples:
* [OpenAF channel implementations through oPacks](../guides/medium/openaf-channel-implementations-through-opacks.md)

### RocksDB (through the rocksdb oPack)

Use channel type `rocksdb` (rocksdb oPack).

Examples:
* [OpenAF channel implementations through oPacks](../guides/medium/openaf-channel-implementations-through-opacks.md)

### S3 (through the S3 oPack)

Use channel type `s3` (S3 oPack).

Examples:
* [OpenAF channel implementations through oPacks](../guides/medium/openaf-channel-implementations-through-opacks.md)

### Chronicle Queue (through the cq oPack)

Use channel type `cq` (cq oPack).

Examples:
* [OpenAF channel implementations through oPacks](../guides/medium/openaf-channel-implementations-through-opacks.md)

### GIST (through the GIST oPack)

Use channel type `gist` (GIST oPack).

Examples:
* [OpenAF channel implementations through oPacks](../guides/medium/openaf-channel-implementations-through-opacks.md)

### AWS Secrets Manager (through the AWS oPack)

Use channel type `awssecrets` (AWS oPack), typically through `$sec("awssecrets", ...)`.

Examples:
* [OpenAF channel implementations through oPacks](../guides/medium/openaf-channel-implementations-through-opacks.md)

### Lucene Vector Search (through the lucene oPack)

Use channel type `vectordb` (lucene oPack).

Examples:
* [OpenAF channel implementations through oPacks](../guides/medium/openaf-channel-implementations-through-opacks.md)

### Lucene Full-text Search (through the lucene oPack)

Use channel type `searchdb` (lucene oPack).

Examples:
* [OpenAF channel implementations through oPacks](../guides/medium/openaf-channel-implementations-through-opacks.md)

### Exposing channels externally

#### Remote channels

For whatever channel you have created you can expose it externally through a REST protocol. You can achieve this easily by executing for an existing channel:

````javascript
> $ch("mychannel").expose(1234, "/mychannel")
````

This creates a HTTP server on the port 1234 that will respond to REST queries on the URI “/mychannel”. You can create a remote channel on another openaf script or session to communicate with it by executing:

````javascript
> $ch("remoteChannel").createRemote("http://the.other.guy:1234/mychannel")
````

The channel “remoteChannel” can now be used normally. All operations will be relayed back to the original channel. But if you subscribe the “remoteChannel” you won't receive any set/setall/unset operations from “mychannel”.

You can also create a remote channel directly with the `remote` type and options:

````javascript
> $ch("remoteChannel").create(1, "remote", {
    url: "http://the.other.guy:1234/mychannel",
    login: "user",
    password: "pass",
    timeout: 1500,
    throwExceptions: true
});
````

Remote options:

| Option | Mandatory | Type | Description |
|--------|-----------|------|-------------|
| url | Yes | String | Base URL of the exposed remote channel endpoint. |
| login | No | String | Optional username for HTTP authentication. |
| password | No | String | Optional password for HTTP authentication. |
| timeout | No | Number | Request timeout/connection timeout in ms. |
| default | No | Any | Default value returned by REST helper when requests fail and exceptions are disabled. |
| stopWhen | No | Function | Optional stop predicate used by REST helper retries/flow. |
| throwExceptions | No | Boolean | Throw on REST errors (defaults to `true` for `remote`). |
| preAction | No | Function | Function called before each HTTP request. |

### Peering channels

Peering is an advanced mode for remote channels. Instead of one-way communication from a source channel to a target channel, it uses bidirectional communication to keep both channels up to date.

On side A you simply execute (similar to *expose*):

````javascript
> $ch("mychannelOnA").peer(8010, "/mychannel", [ "http://the.other.guy:8011/mychannel" ]);
````

and on the other side B:

````javascript
> $ch("mychannelOnB").peer(8011, "/mychannel", [ "http://the.original.guy:8010/mychannel" ]);
````

If you look carefully, you will notice the peer is provided as an array because you can define a list of peers (which should include all peers for each side). Let's add side C:

On side A:

````javascript
> $ch("mychannelOnA").peer(8010, "/mychannel", [ "http://the.other.guy:8011/mychannel", "http://the.extra.guy:8012/mychannel" ]);
````

on side B:

````javascript
> $ch("mychannelOnB").peer(8011, "/mychannel", [ "http://the.original.guy:8010/mychannel", "http://the.extra.guy:8012/mychannel" ]);
````

and on side C:

````javascript
> $ch("mychannelOnC").peer(8012, "/mychannel", [ "http://the.original.guy:8010/mychannel", "http://the.other.guy:8011/mychannel" ]);
````

The peering functionality is a little similar to the Ignite type with the following differences:

* Subscribers will get triggered in each side upon data change
* Each side should mirror all data
* Static list of peers

### Channels REST API

The next table describes the REST API in more detail to communicate with an exposed/peered channel:

| Channel operation | HTTP Method | URI |
|:------------------|:------------|:----|
| getAll | GET | [base uri]/o/a |
| getKeys | GET | [base uri]/o/k |
| getSortedKeys | GET | [base uri]/o/s |
| getSet | PUT | [base uri]/o/es/m/[match]/k/[key]/t/[timestamp] |
| set | PUT | [base uri]/o/e/k/[key]/t/[timestamp] |
| setAll | PUT | [base uri]/o/a/k/[key]/t/[timestamp] |
| get | GET | [base uri]/o/e/k/[key] |
| unset | DELETE | [base uri]/o/e/k/[key]/t/[timestamp] | 
