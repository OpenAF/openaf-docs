---
layout: default
title: ow.ch
parent: Reference
grand_parent: OpenAF docs
---

{% raw %}
## ow.ch

[Source: `06414cd9`](https://github.com/OpenAF/openaf/blob/06414cd9204e918daa1e2971ce904783299db333/js/owrap.ch.js) · [Baseline](../source-snapshot.md)

### ow.ch.comms.getSubscriberFunc

`ow.ch.comms.getSubscriberFunc(aURL, aUUID, aLogin, aPassword, aTimeout)`

````text
Returns a function to be used with ow.ch.subscribe for REST communication to the provided aURL intended to be used with ow.ch.server.*. Optionally aUUID can be provided to ignore subscriber request using it. Optionally you can provide aLogin, aPassword and/or a aTimeout (in ms).
````

### ow.ch.create

`ow.ch.create(aName, shouldCompress, type, options) : ow.ch`

Creates a channel of key/values with `aName`. Optionally you can specify if keys should also
be compressed in memory (`shouldCompress` = true), a channels implementation `type` and corresponding
`options` in a map.

Example:

```javascript
ow.ch.create("myChan", false, "db", { db: myDB, from: "TABLE" });
```

### ow.ch.destroy

`ow.ch.destroy(aName) : ow.ch`

````text
Deletes all data and removes references to the channel aName, including its locks. Stop producers and wait for pending channel operations/subscriber jobs before destroying a channel. Channel creation, destruction and listing are serialized; destruction does not drain active operations.
````

### ow.ch.forEach

`ow.ch.forEach(aName, aFunction) : ow.ch`

````text
Will execute the provided aFunction with each key and value for the channel identified by the aName provided.
````

### ow.ch.get

`ow.ch.get(aName, aKey) : ow.ch`

````text
Returns the value associated with the provided aKey on the channel identified by aName.
````

### ow.ch.getAll

`ow.ch.getAll(aName, fullInfo) : Array`

````text
Will return all values for the channel identified by the aName provided.
````

### ow.ch.getKeys

`ow.ch.getKeys(aName, full) : Array`

````text
Returns all keys in the form of an array for the channel identified by the aName provided. Optionally you can specify full = yes to obtain the detailed internal key index.
````

### ow.ch.getSet

`ow.ch.getSet(aName, aMatchMap, aKey, aValue, aTimestamp, aUUID)`

````text
Tries to update the channel identified by the provided aName with aKey and aValue only if it's possible to get the same aKey and  aMatchMap matches the current aValue. Optionally you can provide the internal aTimestamp (if the provided aTimestamp is smaller than getVersion the value will not be set)
````

### ow.ch.getSortedKeys

`ow.ch.getSortedKeys(aName, full) : Array`

````text
Returns all keys in the form of an array for the channel identified by the aName provided by order of the last modification. Optionally you can specify full = yes to obtain the detailed internal key index.
````

### ow.ch.getVersion

`ow.ch.getVersion(aName) : Number`

````text
Returns the current version (usually a timestamp) for the aName channel.
````

### ow.ch.list

`ow.ch.list() : Array`

````text
Returns a list the current channels available.
````

### ow.ch.persistence.create

`ow.ch.persistence.create(aChannel, aFilename, anArrayOfKeys, shouldCompress, forAll)`

````text
Adds a channel identified by the name aChannel, trying to restore data from aFilename given anArrayOfKeys (strings representing the key fields). Optionally indicating if keys should be compressed in memory with shouldCompress = true and/or existing subscribers should run for all elements (forAll = true)
````

### ow.ch.persistence.getSubscriberFunc

`ow.ch.persistence.getSubscriberFunc(aFilename)`

````text
Returns a function to be used with ow.ch.subscribe persisting any existing or new data into aFilename provided.
````

### ow.ch.persistence.restore

`ow.ch.persistence.restore(aChannel, aFilename, anArrayOfKeys) : Number`

````text
Tries to restore that previously persisted using ow.ch.getSubscribeFunc from the aFilename using  anArrayOfKeys (strings representing the string list of fields used as index). The values will be restored to the aChannel name provided. Returns -1 in case of error or the data loaded length otherwise.
````

### ow.ch.pop

`ow.ch.pop(aName) : Object`

````text
Mimics a LIFO queue behaviour by returning the last modified key/value entry for the channel aName. The entry will be removed from the channel.
````

### ow.ch.push

`ow.ch.push(aName, aKey, aValue) : ow.ch`

````text
Equivalent to ow.ch.set trying to set, for the channel aName, aKey and aValue trying to mimic a queue behaviour.
````

### ow.ch.server.expose

`ow.ch.server.expose(aName, aLocalPortORServer, aPath, aAuthFunc, aUnAuthFunc, noCheck) : String`

Given `aName` channel and `aLocalPortORServer` will use the provided server, or start a simple http server on the
provided port, to expose access to the `aName` channel on the URL `aPath`. It will return an unique identifier
to be use to identify incoming requests from this `aPath` and server on channel subscribe functions. Optionally
you can also provide `aAuthFunc(user, pass, aServer, aRequest)` and `aUnAuthFunc(aServer, aRequest)` functions using `ow.server.httpd.authBasic`.
The `aAuthFunc` can add `aRequest.channelPermission` to enforce read and/or write permissions on a channel (e.g. "r", "rw").
If needed you can ignore the checking if the `aName` channel exists with `noCheck`.

Example:

```javascript
// Exposing the a log dump channel on port 8090 for test proposes.
ow.ch.server.expose("__log", 8090, "/log");
```

### ow.ch.server.peer

`ow.ch.server.peer(aName, aLocalPortORServer, aPath, aRemoteURLArray, aAuthFunc, aUnAuthFunc, aMaxTime, aMaxCount)`

Exposes `aName` channel in the same way as `ow.ch.server.expose` but it also add a subscribe function to
the `aName` channel to remotely peer with other expose channel(s) given `aRemoteURLArray`. Optionally
`aRemoteURLArray` can also be a function returning a URL or an array of URLs. Optionally
you can also provide `aAuthFunc(user, pass)` and `aUnAuthFunc(aServer, aRequest)` functions using `ow.server.httpd.authBasic`.
The `aAuthFunc` can add `aRequest.channelPermission` to enforce read and/or write permissions on a channel (e.g. "r", "rw").
Optionally you can provide `aMaxTime` for expiration of commands to retry to communicate and `aMaxCount` of commands to retry to communicate.

Example:

```javascript
ow.ch.server.peer("__log", 8090, "/log", [ "http://server1.local:8090/log", "https://l:p@server2.local:8090/log" ]);
```

### ow.ch.server.routeProcessing

`ow.ch.server.routeProcessing(aURI, aRequest, aName) : HTTPServerReply`

Creates a server route processing for a `ow.ch.comms` client provided `aURI`, a HTTPServer `aRequest` and the
`aName` of a channel (please note that you should create the channel prior to using this function).
Depending on `aRequest.channelPermission` some operations may not execute:

- "r" - allows channel get/getAll operations
- "w" - allows channel set/setAll/getSet/unset/unsetAll operations

Example:

```javascript
var hs = ow.loadServer().httpd.start(17878);
ow.server.httpd.route(hs, { "/rest": function(r) { return ow.ch.server.routeProcessing("/rest", r, "my-channel") }});
```

for multiple channels:

```javascript
var hs = ow.loadServer().httpd.start(17878);
ow.server.httpd.route(hs, {
   "/chan1": function(r) { return ow.ch.server.routeProcessing("/chan1", r, "chan-1") },
   "/chan2": function(r) { return ow.ch.server.routeProcessing("/chan2", r, "chan-2") }
});
```

### ow.ch.server.setLog

`ow.ch.server.setLog(aLogFunction)`

Sets `aLogFunction` to act as audit for external communication to access a channel. The `aLogFunction`
will be called passing, as a single argument, a map with:

- `name` (the channel name)
- `op` (the operation can be AUTH_OK, AUTH_NOT_OK, GET, SET, REMOVE or CREATE)
- `request` (the HTTP request map)

The request, when available, will include an entry with the current user.

### ow.ch.server.unpeer

`ow.ch.server.unpeer(aName, aRemoteURL)`

````text
Remove all subscribers related with aRemoteURL from the aName channel effectively "unpeering" it from the aRemoteURL.
````

### ow.ch.set

`ow.ch.set(aName, aKey, aValue, aTimestamp)`

````text
Tries to insert/update the channel identified by the provided aName with aKey and aValue. Optionally you can provide the internal aTimestamp (if the provided aTimestamp is smaller than getVersion the value will not be set)
````

### ow.ch.setAll

`ow.ch.setAll(aName, anArrayOfKeys, anArrayOfMapData, aTimestamp)`

````text
Given anArrayOfKeys composed of strings identifying the key fields from the anArrayOfMapData provided will try to insert/update all values on the channel identified by aName. Optionally you can provide aTimestamp  (if the provided aTimestamp is smaller than getVersion the value will not be set)
````

### ow.ch.shift

`ow.ch.shift(aName) : Object`

````text
Mimics a FIFO queue behaviour by returning the first modified key/value entry for the channel aName. The entry will be removed from the channel.
````

### ow.ch.size

`ow.ch.size(aName) : Number`

````text
Returns the number of keys currently available for the channel aName.
````

### ow.ch.stopAllJobs

`ow.ch.stopAllJobs(aName) : ow.ch`

````text
Each channel subscription (using ow.ch.subscribe) will create internal jobs (threads). To stop all these immediately provide the channel aName.
````

### ow.ch.subscribe

`ow.ch.subscribe(aName, aFunction, onlyFromNowm, anId) : String`

Adds a callback function to the channel `aName`. The callback function will receive, as arguments:
the channel name, the operation, a key or an array of keys (for operation = setall/unsetall), a value or an array
of values (for operation = setall/unsetall) and the `ow.ch` object. Returns the subscriber id.
Optionally you can specify that existing
elements won't trigger operation = set callback calls and/or a custom subscriber `anId`.

Possible operations:

- `set`
- `setall`
- `unset`
- `unsetall`

### ow.ch.types.all

`ow.ch.types.all`

This channel type aggregates access to several channels. The creation options are:

- `chs` (Array) An array of names of channels to aggregate.
- `fn` (Function) A function that will receive an operation, a key and value (when applicable)) to return which channel name should be used (if no return or void all channels will be considered).
- `errFn` (Function) A function to call with: the name of this channel, the exception, the target channel, the operation and the arguments whenever a error occurs accessing a channel.
- `fnTrans` (Function) A function to translate the key (for example, to remove elements used only on fn).
- `fnKeys` (Function) Allows to filter an array of resulting keys, from different channels, for: getKeys, getSortedKeys
- `fnValues` (Function) Allows to filter an array of resulting values, from different channels, for: getAll, get, getSet, set and unset
- `treatAll` (Boolean) If true size, setAll and unsetAll will be executed individually and fn called for each (default is false and size will take the first result)

### ow.ch.types.big

`ow.ch.types.big`

This OpenAF channel implementation stores key/values in a compressed in-memory structure (`ow.obj.big`) optimized
for large datasets. It accepts no creation options beyond the inherited shouldCompress parameter.

Example:

```javascript
ow.ch.create("myBig", true, "big");
```

Note: the underlying `ow.obj.big` storage uses a sorted index so getSortedKeys reflects insertion/modification order.

### ow.ch.types.buffer

`ow.ch.types.buffer`

This OpenAF implementation establishes a buffer to another channel. The creation options are:

- `bufferCh` (String) The channel that will receive data from the buffer channel.
- `bufferIdxs` (Array) An array of keys to use for faster performance (defaults to []).
- `bufferByTime` (Number) How much time before flushing contents from the buffer channel (default 2500ms).
- `bufferByNumber` (Number) How many entries before flushing contents from the buffer channel (default 100).
- `bufferTmpCh` (String) The auxiliary temporary buffer storage channel to use (default creates [name]::`__bufferStorage`).
- `bufferFunc` (Function) Optional function that if returns true will trigger the buffer flush to bufferCh.

### ow.ch.types.cache

`ow.ch.types.cache`

This OpenAF channel implementation provides a caching layer around a function or another channel. The creation options are:

- `func` (Function) Function called with the key map when a cache miss occurs; its return value is stored and returned.
- `ttl` (Number) Time-to-live in ms before cached entries expire (defaults to 5000ms).
- `size` (Number) Maximum number of entries to keep in cache; -1 means unlimited (defaults to -1).
- `method` (String) Eviction method: "t" (time-based TTL, default) or "p" (count-based, evicts oldest when size is exceeded).
- `default` (Object) Optional default value to store and return on a cache miss if func is not defined.
- `useDefault` (Boolean) If true the default value is returned instead of calling func on a miss.
- `ch` (String/Channel) Optional backing storage channel (defaults to an auto-created [name]::`__cache` simple channel).

Example:

```javascript
ow.ch.create("myCache", false, "cache", { func: k => $rest().get("http://api/data/" + k.id), ttl: 60000 });
```

### ow.ch.types.db

`ow.ch.types.db`

This OpenAF channel implementation wraps access to a db table. The creation options are:

- `db` (Database) The database object to access the database table (or a JSON/SLON string with 'url', 'user', 'pass', 'timeout', 'driver').
- `from` (String) The name of the database table or object (don't use double quotes).
- `keys` (Array) An array of fields keys to use (don't use double quotes).
- `cs` (Boolean) Determines if the database is case sensitive for table and field names (defaults to false).

### ow.ch.types.dummy

`ow.ch.types.dummy`

This OpenAF channel implementation is a no-op sink: all write operations (set, setAll, unset, unsetAll) are silently
discarded, all read operations (get, getAll, getKeys, size, forEach) return empty results. Useful for disabling a
channel without changing calling code. Accepts no creation options.

Example:

```javascript
ow.ch.create("blackhole", false, "dummy");
```

### ow.ch.types.elasticsearch

`ow.ch.types.elasticsearch`

This OpenAF implementation connects to an ElasticSearch (ES) server/cluster. The creation options are:

- `index` (String/Function) The ES index to use or a function to return the name (see also `ow.ch.utils.getElasticIndex`).
- `format` (String) If index is a string will use format with `ow.ch.utils.getElasticIndex`.
- `idKey` (String) The ES key id field. Defaults to 'id'.
- `url` (String) The HTTP(S) URL to access the ES server/cluster.
- `user` (String) Optionally provide a user name to access the ES server/cluster.
- `pass` (String) Optionally provide a password to access the ES server/cluster (encrypted or not).
- `fnId` (String/Function) Optionally called on every operation to calculate the idKey with the key provided as argument. If string will the corresponding hash function (md5/sha1/etc...) with sortMapKeys + stringify.
- `size` (Number) Optionally getAll/getKeys to return more than 10 records (up to 10000).
- `stamp` (Map) Optionally merge with stamp map.
- `timeout` (Number) Optional request timeout in ms.
- `preAction` (Function) Optional function to be called before every request.

The getAll/getKeys functions accept an extra argument to provide a ES query map to restrict the results.

### ow.ch.types.etcd

`ow.ch.types.etcd`

This OpenAF channel implementation connects to an etcd v2 key/value store. The creation options are:

- `url` (String) The HTTP(S) URL of the etcd daemon (e.g. http://etcd-host:2379). Mandatory.
- `folder` (String) Optional key prefix/folder path to scope all channel operations (defaults to root).
- `throwExceptions` (Boolean) If true (default) HTTP errors from etcd will be thrown as exceptions.
- `default` (Object) Optional default value to return when a request fails instead of throwing.
- `preAction` (Function) Optional function called before every HTTP request (receives the `$rest` options map).

Note: this implementation targets the etcd v2 HTTP API (/v2/keys). For etcd v3 consider an alternative approach.

Example:

```javascript
ow.ch.create("myEtcd", false, "etcd", { url: "http://etcd:2379", folder: "/myapp" });
```

### ow.ch.types.file

`ow.ch.types.file`

This OpenAF implementation implements a simple channel on a single JSON, YAML or TOON file. The creation options are:

- `file` (String) The filepath to the JSON or YAML file to use (if multifile is false)
- `path` (String) The path to use to store JSON, YAML or TOON objects to use (if multifile is true)
- `yaml` (Boolean) Use YAML instead of JSON (defaults to false)
- `toon` (Boolean) Use TOON instead of JSON (defaults to false)
- `compact` (Boolean) If JSON and compact = true the JSON format will be compacted (defaults to false or shouldCompress option)
- `multifile` (Boolean) If true instead of keeping values in one file it will be kept in multiple files (*)
- `multipart` (Boolean) If YAML and multipart = true the YAML file will be multipart
- `key` (String) If a key contains "key" it will be replaced by the "key" value
- `multipath` (Boolean) Supports string keys with paths (e.g. `ow.obj.setPath`) (defaults to false)
- `lock` (String) If defined the filepath to a dummy file for filesystem lock while accessing the file
- `gzip` (Boolean) If true the output file will be gzip (defaults to false)
- `lz4` (Boolean) If true the output file will be lz4 (defaults to false)
- `tmp` (Boolean) If true "file" will be temporary and destroyed upon execution/process end

(*) - Be aware that although there is a very small probability of collision between the unique id (sha-512) for filenames it still exists

### ow.ch.types.graph

`ow.ch.types.graph`

Channel over a knowledge graph stored in a single JSON file, using the Mini-A wiki graph format:
`{ version, nodes: { id: { id, type, props } }, edges: [ { from, to, type, provenance, props } ], ... }`.

Creation options:

| Option | Type | Default | Description |
| --- | --- | --- | --- |
| `file` | String | _required_ | Path to the graph JSON file |
| `readOnly` | Boolean | `false` | Reject changes and never write the file |
| `create` | Boolean | `true` | If `false` the file must already exist; otherwise an empty graph is started |
| `autosave` | String | `"always"` | `"always"`, `"debounced"` or `"off"`; pending changes are always flushed on destroy |
| `saveDebounceMs` | Number | `5000` | Minimum ms between saves when `autosave` is `"debounced"` |
| `lock` | String | | Path to a dummy file used as a filesystem lock while loading/saving |
| `store` | Map | | `{ type, options, compress, bulk }`: keep nodes, edges and other sections in channels of that type (e.g. `mvs`) instead of memory; can't be combined with `file` |

Keys and values:

- **Node**: key `{ id }` (e.g. `{ id: "doc:readme.md" }`), value `{ id, type, props }`.
- **Edge**: key `{ from, to, type, provenance, page, section }`, value `{ from, to, type, provenance, props }`.
  `provenance` is `EXTRACTED`, `INFERRED` or `AMBIGUOUS` (default); `page` and `section` map to `props.page` and `props.section`.
- Setting an edge requires both nodes to exist; unsetting a node also removes its edges.
- File sections not handled by the channel (e.g. `communities`, `summaries`) are preserved on save.

Example:

```javascript
$ch("g").create(true, "graph", { file: "graph.json" });
$ch("g").set({ id: "doc:a.md" }, { type: "document", props: { title: "A" } });
$ch("g").set({ id: "doc:b.md" }, { type: "document", props: { title: "B" } });
$ch("g").set({ from: "doc:a.md", to: "doc:b.md", type: "LINKS_TO" }, {});
ow.ch.utils.graph.path("g", "a.md", "b.md"); // [ "doc:a.md", "doc:b.md" ]
```

Use `ow.ch.utils.graph` to navigate the graph. The whole file is rewritten on save, so avoid several writers over the same file.

### ow.ch.types.ignite

`ow.ch.types.ignite`

This channel type uses plugin-Ignite 3.1 tables with JSON keys and values. The creation options are:

- `ignite` (Ignite) Use a previously instantiated Ignite plugin (defaults to a new instance).
- `gridName` (String) Use a specific Ignite node/client name.
- `client` (Boolean) Connect a thin client instead of starting an embedded node.
- `configuration` (Map) Ignite.configure options, including addresses or configFile/workDir.
- `persist` (String) Persistent Ignite 3 work directory (alias for configuration.workDir).
- `cacheName` (String) Shared backing table name (defaults to the channel name).
- `keepOnDestroy` (Boolean) Keep the backing table when destroying the channel (default false).

### ow.ch.types.mvs

`ow.ch.types.mvs`

The channel type mvs uses H2 MVStore to keep key/value structures either in memory or in files.
The creation options are:

- `file` (String) If not defined it will default to the in-memory implementation otherwise a file.
- `shouldCompress` (Boolean) Specifies if it should compress the entire structure or not.
- `compact` (Boolean) Upon channel create/destroy it will try to run a compact operation over the file to save space.
- `map` (String/Function) The map name (defaults to 'default'). If defined as a function it will receive the key as argument if possible (only for get/set/unset/setall)
for sharding purposes.

- `multifile` (Boolean) If true keys will be spread (by key hash) across several MVStore files on "path" (defaults to false) (*)
- `path` (String) The folder where to keep the MVStore files (required if multifile is true)
- `files` (Number) The number of MVStore files to use if multifile is true (defaults to 4 or to the number already in use on "path")

The map will be created if it doesn't exist. Operations getKeys/getAll can be paginated with the extra map argument containing start and end

(*) - With multifile the files are named mvs-NN.db and a mvs-multifile.json manifest records the number of files (to change it use `ow.ch.utils.mvs.reshard`).
All other options apply to each file. getKeys/getAll (including start/end pagination) and pop/shift go through the files in order (no global key ordering).
Each file can be handled individually with `ow.ch.utils.mvs`.

### ow.ch.types.ops

`ow.ch.types.ops`

This OpenAF channel implementation encapsulates access based on functions. The creation options are a map of
keys where each value is a function.

Example:

```javascript
ow.ch.create("logic", false, "ops", { hello: name => "hi " + name });
```

### ow.ch.types.prometheus

`ow.ch.types.prometheus`

This OpenAF implementation connects to a prometheus server. The creation options are:

- `urlQuery` (String) The URL of a prometheus server (e.g. http://prometheus:9090)
- `urlPushGW` (String) The URL of a prometheus push gateway server (e.g. http://prometheus:9091).
- `prefix` (String) If defined the prefix for all openmetrics.
- `gwGroup` (Map) A map of grouping labels for data ingestion by the push gw (job label must be defined).
- `helpMap` (Map) The helpMap for the openmetrics (see more in `ow.metrics.fromObj2OpenMetrics`).

The forEach/getSet/pop/shift/unsetAll functions are not supported.
The size function retrieves the total number of labels.
The get/getAll function enables instant query (with the extra map key query), query range query (with the extra map keys query, start and end) and label values query (with the extra map key label).
The set/setAll functions only consider the value(s) argument, the key(s) is ignored.

Note: query by specific series are not currently supported.

### ow.ch.types.proxy

`ow.ch.types.proxy`

This OpenAF implementation establishes a proxy to another channel. The creation options are:

- `chTarget` (String) The channel that will receive all operations (if proxyFunc doesn't return).
- `proxyFunc` (Function) Function that receives a map (by reference that can be changed) with: op (operation),
name (target channel), function (where applicable), full (where applicable), match (the match of getSet), k (the key(s)),
v (the value(s)) and timestamp. If this function returns something no operation will be executed on the chTarget and the
value returned by the function will be the value returned by this channel.

### ow.ch.types.remote

`ow.ch.types.remote`

This OpenAF channel implementation connects to a remote channel exposed via `ow.ch.server.expose` or `ow.ch.server.peer`. The creation options are:

- `url` (String) The HTTP(S) URL of the remote exposed channel (e.g. http://server:8090/channel).
- `login` (String) Optional username for HTTP basic authentication.
- `password` (String) Optional password for HTTP basic authentication (encrypted or not).
- `timeout` (Number) Optional connection and request timeout in ms.
- `default` (Object) Optional default value to return when the request fails instead of throwing.
- `stopWhen` (Function) Optional function that, if it returns true, stops the underlying HTTP request retry.
- `throwExceptions` (Boolean) If true (default) exceptions from the remote server will be thrown locally.
- `preAction` (Function) Optional function called before every HTTP request (receives the `$rest` options map).

Example:

```javascript
ow.ch.create("myRemote", false, "remote", { url: "http://server:8090/myChannel" });
$ch("myRemote").set({ id: 1 }, { id: 1, name: "test" });
```

Note: the remote channel relies on `ow.ch.server.expose`/peer on the server side and uses the OpenAF REST channel
protocol over HTTP(S). For two-way synchronization between nodes consider using `ow.ch.server.peer` instead.

### ow.ch.types.simple

`ow.ch.types.simple`

This OpenAF channel implementation is the default in-memory key/value store (used when no type is specified in `ow.ch.create`).
It stores entries in a JavaScript Map keyed by a deterministic JSON serialization of the key map, preserving
modification-time order for getSortedKeys. Accepts no creation options.

Example:

```javascript
ow.ch.create("myChannel");                    // uses "simple" by default
ow.ch.create("myChannel", false, "simple");   // explicit
```

### ow.ch.types.simpleold

`ow.ch.types.simpleold`

````text
This OpenAF channel implementation is the legacy in-memory key/value store backed by a plain JavaScript object. It is kept for backward compatibility; prefer the "simple" type for new channels. Accepts no creation options.
````

### ow.ch.types.timeseries

`ow.ch.types.timeseries`

Channel over labelled numeric time series (metric + labels + timestamp), kept in memory with an optional append-only NDJSON file,
or delegated to other channels (e.g. `mvs`) with `store`. Supports retention (age and/or count) and stored rollups (RRD-like).

Creation options:

| Option | Type | Default | Description |
| --- | --- | --- | --- |
| `file` | String | | Path to an NDJSON log file. Without `file` (and `store`) the channel only lives in memory |
| `readOnly` | Boolean | `false` | Reject changes and never write the file |
| `create` | Boolean | `true` | If `false` the file (or store) must already exist |
| `autosave` | String | `"always"` | `"always"` appends on every change, `"debounced"` appends at most every `saveDebounceMs`, `"off"` only on `save`/destroy |
| `saveDebounceMs` | Number | `5000` | Minimum ms between appends when `autosave` is `"debounced"` |
| `lock` | String | | Path to a dummy file used as a filesystem lock while loading and writing |
| `compactRatio` | Number | `0.5` | The file is rewritten (compacted) when more than this ratio of its lines is dead (overwritten, deleted or expired) |
| `store` | Map | | `{ type, options, compress, bulk }`: keep the data in chunks stored on channels of that type (e.g. `mvs`); can't be combined with `file` |
| `chunk` | String/Number | `"1h"` | Time span of each stored chunk (only used with `store`) |
| `retention` | String/Number | | How long to keep raw points (e.g. `"7d"`), relative to the newest point of each series (see `retentionRef`). Same as `raw.keep` |
| `maxPoints` | Number | | Maximum raw points per series. Same as `raw.maxPoints` |
| `raw` | Map | | `{ keep, maxPoints }` for the raw points |
| `rollups` | Array | | `[ { step: "1m", keep: "1d" }, { step: "1h", keep: "30d" } ]`: aggregated buckets kept per series (`count`, `sum`, `min`, `max`, `first`, `last`) |
| `retentionRef` | String | `"series"` | `"series"` measures `keep` back from the newest point of the series, `"now"` from the current time |
| `housekeepEveryMs` | Number | `0` | Minimum ms between retention runs triggered by writes (`0` = on every write) |

Keys and values:

- **Key**: `{ metric, labels, ts }`. `labels` is a map (values are stored as strings); `ts` is epoch ms, a Date or an ISO string (defaults to now on `set`).
- **Value**: `{ v }` where `v` is a number.
- `get` without `ts` returns the latest point; the value returned is always `{ metric, labels, ts, v }`.
- `unset` with `ts` removes a point; without `ts` it drops the whole series (points and rollups).
- `getKeys`/`getAll` accept a selector map `{ metric, labels, from, to }`; `pop`/`shift` return the key of the newest/oldest point.

Example:

```javascript
$ch("m").create(true, "timeseries", { file: "cpu.ndjson", retention: "7d" });
$ch("m").set({ metric: "cpu", labels: { host: "a" }, ts: 1000 }, { v: 0.4 });
$ch("m").set({ metric: "cpu", labels: { host: "a" }, ts: 2000 }, { v: 0.6 });
ow.ch.utils.timeseries.range("m", { metric: "cpu" }, { step: "1s", fn: "avg" });
```

Retention deletes made by the channel itself do not notify channel subscribers. Use `ow.ch.utils.timeseries` to query.

### ow.ch.unset

`ow.ch.unset(aName, aKey, aTimestamp) : ow.obj.channel`

````text
Tries to remove all associations to the provided aKey on the channel identified by aName. Optionally aTimestamp can be provided.
````

### ow.ch.unsetAll

`ow.ch.unsetAll(aName, anArrayOfKeys, anArrayOfMapData, aTimestamp)`

````text
Given anArrayOfKeys composed of strings identifying the key fields from the anArrayOfMapData provided will try to delete all values on the channel identified by aName. Optionally you can provide aTimestamp  (if the provided aTimestamp is smaller than getVersion the value will not be set)
````

### ow.ch.unsubscribe

`ow.ch.unsubscribe(aName, aId) : ow.ch`

````text
Tries to unsubscribe aId callback from the channel identified by the aName provided.
````

### ow.ch.unsubscribeAll

`ow.ch.unsubscribeAll(aName) : ow.ch`

````text
Tries to unsubscribe all callback functions from the channel identified by the aName provided.
````

### ow.ch.utils.closeBuffer

`ow.ch.utils.closeBuffer(aName)`

````text
Tries to close and flush a channel buffer with aName (if not provided assumes all buffer type channels).
````

### ow.ch.utils.flushBuffer

`ow.ch.utils.flushBuffer(aName)`

````text
Tries to flush a channel buffer with aName (if not provided assumes all buffer type channels).
````

### ow.ch.utils.getBufferSubscriber

`ow.ch.utils.getBufferSubscriber(aSourceCh, indexes, byNumber, byTimeInMs, aBufferCh, aTmpBufferCh, aFilterFunc, aBufferFunc) : Function`

Returns a channel subscriber function that will buffer set, setall, unsetall and unset operations from `aSourceCh` channel to `aBufferCh` (by
default a dummy channel to be subscribed, if not defined the name will be `aSourceCh` + "::buffer"). As a temporary buffer channel
`aTmpBufferCh` will be used (if not defined the name will be `aSourceCh` + "::`__bufferStorage`"). The `aBufferCh` will be configured with
the provided `indexes`, `byNumber` (number of times to trigger the buffer) and `byTimeInMs` (amount of time in ms to trigger the buffer).
Additionally you can specify `aFilterFunc` (with arguments channel, operation, key(s) and value(s)) that will only buffer if returns false
and `aBufferFunc` that will trigger the buffer flush if it returns true.

NOTE: do call `ow.ch.utils.closeBuffer(aSourceCh)` when it's no longer needed.

### ow.ch.utils.getElasticIndex

`ow.ch.utils.getElasticIndex(aPrefix, aFormat) : Function`

````text
Returns a function to be used for generating ElasticSearch indexes with aPrefix-aDate (in the format of YYYY.MM.DD). This helps to generate a specific index per day. If a specific format is needed you can provided it as aFormat (see ow.format.fromDate)).
````

### ow.ch.utils.getElasticQuery

`ow.ch.utils.getElasticQuery(aQueryString) : Map`

````text
Returns a query map using aQueryString (using lucene query string (like in Kibana)) to be used on getAll, for example.
````

### ow.ch.utils.getFileHousekeepSubscriber

`ow.ch.utils.getFileHousekeepSubscriber(aFolder, aRegExPattern, howLongAgoInMinutes, dontCompress, aBackupFolder) : Function`

````text
Returns a channel subscriber function to perform file housekeep (specially useful with ow.ch.utils.getLogFilePerDate) given the main aFolder where just the newest file whose filename matches aRegExPattern (e.g. "log\\d{4}-\\d{2}-\\d{2}\\.log") will be kept uncompressed. All other files will be gziped (if dontCompress = false) and moved to aBackupFolder (if defined, defaults to aFolder). If howLongAgoInMinutes is defined all  files older than now - howLongAgoInMinutes will be deleted from the aBackupFolder.
````

### ow.ch.utils.getHousekeepSubscriber

`ow.ch.utils.getHousekeepSubscriber(aTargetCh, maxNumberOfKeys) : Function`

````text
Returns a channel subscriber function that will keep the channel size to the maximum of maxNumberOfKeys (defaults to 100). If the number of keys is bigger than maxNumberOfKeys than it will perform a channel unset operation (that will, depending on the type of channel, remove the oldest element).
````

### ow.ch.utils.getK8sRemoteURLArrayFunc

`ow.ch.utils.getK8sRemoteURLArrayFunc(aOptions) : Function`

Returns a function to be used as `aRemoteURLArray` in `ow.ch.server.peer`. It will resolve
all IP addresses from a Kubernetes DNS name (typically a headless service for deployments)
using `ow.net.getDNS` and return an array of remote channel URLs.

`aOptions` map entries:

- `dnsName` (String, mandatory) Kubernetes DNS name to resolve
- `recordType` (String, optional) DNS record type (defaults to "a")
- `dnsServer` (String, optional) DNS server to use
- `protocol` (String, optional) URL protocol (defaults to "http")
- `port` (Number, optional) Port to use (defaults to local peer port when numeric)
- `path` (String, optional) URL path (defaults to peer path argument)
- `excludeCurrentIP` (Boolean, optional) Excludes current instance IP from result (defaults to false)
- `currentIP` (String, optional) Explicit current instance IP (otherwise uses POD_IP env var or `ow.net.getHostAddress()`)
- `urlFn` (Function, optional) Custom URL builder fn(ip, ctx)

Example:

```javascript
var peersFn = ow.ch.utils.getK8sRemoteURLArrayFunc({
  dnsName: "openaf-peers.default.svc.cluster.local",
  protocol: "http",
  port: 8090,
  path: "/log"
});
ow.ch.server.peer("__log", 8090, "/log", peersFn);
```

### ow.ch.utils.getLogFilePerDate

`ow.ch.utils.getLogFilePerDate(aLogFolder, aTemplate, aFileDateFormat, aLineTemplate, aLineDateFormat) : Function`

````text
Returns a function to be used to generate a log file in aLogFolder path. If the log file already exists it will append to it. You can customize the log filename format using a aTemplate (e.g. "log-{{timedate}}.log" by default). The "timedate" is defined on the aFileDateFormat (e.g. "yyyy-MM-dd" by day, "yyyy-MM-dd-HH" by hour (check ow.format.fromDate for more options)). Each line that will be append to the file can be defined by aLineTemplate (e.g. "{{timedate}} | {{type}} | {{message}}"  by default) where "type" is the of logging (INFO, WARN, ERROR), "message" the logged message and "timedate" is defined on the aLineDateFormat (e.g. "yyyy-MM-dd HH:mm:ss.SSS" by default (check ow.format.fromDate for more options)).
````

### ow.ch.utils.getLogStashSubscriber

`ow.ch.utils.getLogStashSubscriber(aTargetCh, aType, aHost, aErrorFunc, shouldHK, stampMap) : Function`

````text
Returns a channel subscriber function that will transform changes to a log channel (see startLog and the __log channel) and will replicate them in aTargetCh (this means expecting the value to have a 'd': date; 'm': message and 't' as the level/type). The value set on aTargetCh will follow the LogStash format setting type to aType and host to aHost. The id and key will be set  to a sha1 hash of the stringify version of the value being set. In case of error aErrorFunc will be invoked providing the exception as an argument. You can also indicate if you want to house keep the original channel to save the script's memory and a stampMap to force entries on all maps sent.
````

### ow.ch.utils.getMirrorSubscriber

`ow.ch.utils.getMirrorSubscriber(aTargetCh, aFunc) : Function`

````text
Returns a channel subscriber function that will mirror any changes to aTargetCh if aFunc(key, op) returns true when invoked with the key being changed and the corresponding operation.
````

### ow.ch.utils.getStatsProxyFunction

`ow.ch.utils.getStatsProxyFunction(aStatsCh) : Function`

````text
Returns a proxy function to be use with a proxy channel. The aStatsCh where to store the channel access statistics.
````

### ow.ch.utils.graph

`ow.ch.utils.graph`

Helpers to navigate and query a channel of type `graph` (see `ow.ch.types.graph`). Node ids without a `:` are treated as `doc:` ids.

| Function | Returns | Description |
| --- | --- | --- |
| `neighbors(aName, anId, aOptions)` | Array | Edges connected to a node. Options: `direction` (`"out"`, `"in"` or `"both"`), `type`, `provenance` (String or Array) |
| `degree(aName, anId, aOptions)` | Number | Number of edges connected to a node (same options as `neighbors`) |
| `path(aName, aFromId, aToId, aOptions)` | Array | Shortest path (BFS, ignoring direction) as node ids, `[]` if none. Options: `maxDepth`, `type` |
| `traverse(aName, anId, aOptions)` | Map | `{ nodes, edges }` sub-graph reachable from a node. Options: `depth` (default 1), `direction`, `type`, `provenance` |
| `find(aName, aOptions)` | Array | Nodes matching `type` and/or `text` (case insensitive match on id and props) |
| `stats(aName)` | Map | Node and edge counts plus counts by node type, edge type and provenance |
| `save(aName)` | Boolean | Flushes pending changes to the file (`false` if read-only) |

Example:

```javascript
ow.ch.utils.graph.neighbors("g", "a.md", { direction: "out", type: "LINKS_TO" });
ow.ch.utils.graph.traverse("g", "a.md", { depth: 2 }); // { nodes: [...], edges: [...] }
```

### ow.ch.utils.keepHistory

`ow.ch.utils.keepHistory(timeRepeatExpression, aName, aFunction, withKeys, historySize) : Object`

````text
For a given aName channel (preferably a temporary one) will execute aFunction periodically given a timeRepeatExpression (if a Number the ms interval, if a String a cron expression). That aFunction should return aMap for which the withKeys array will be used to determine the keys entries to set it on the provided aName channel (if withKeys is not provided, id will be assumed and filled with nowNano()). The channel aName will be filled with entries with the result of executing aFunction periodically thus keeping an history of results (by default 10 if a historySize is not provided). An object with a stop function will be returned so the keepHistory periodical behaviour of runnning aFunction and keeping the results in the channel aName.
````

### ow.ch.utils.mvs.list

`ow.ch.utils.mvs.list(aMVSFile) : Array`

````text
Returns a list of names of maps in the corresponding aMVSFile.
````

### ow.ch.utils.mvs.remove

`ow.ch.utils.mvs.remove(aMVSFile, aMapToRemove)`

````text
Removes aMapToRemove on the provided aMVSFile.
````

### ow.ch.utils.mvs.rename

`ow.ch.utils.mvs.rename(aMVSFile, anOriginalMap, aDestinationMap)`

````text
Renames anOriginalMap by aDestinationMap on the provided aMVSFile.
````

### ow.ch.utils.mvs.reshard

`ow.ch.utils.mvs.reshard(aPath, aNewFiles, shouldCompress) : Number`

````text
Changes the number of files of an "mvs" channel created with multifile = true on aPath to aNewFiles, redistributing all the entries of all the maps. Returns the number of entries moved. The channel(s) using aPath need to be destroyed first. The new files are built on a temporary folder inside aPath and only replace the current ones (and the mvs-multifile.json manifest) after all the entries are copied and counted. Use shouldCompress = true if the channel was created with it.
````

### ow.ch.utils.poolChanges

`ow.ch.utils.poolChanges(aCh, idKeys, aChM)`

````text
When executed pools to find all changes in aCh, using an idKeys array of key map fields, and executing a setAll on aCh for the changed entries. To compare it stores the last version in a 'aCh + "::chMemory"' channel that can be created with aChM map options ($ch type and options entries). Usefull to trigger channel subscribed functions when the aCh type doesn't detect automatically changes. Should be used with small sized channels as datasets are compared in memory.
````

### ow.ch.utils.setLogToFile

`ow.ch.utils.setLogToFile(aConfigMap)`

Shortcut to set OpenAF's logging into a rotating per date set of log files. You can set any of these options:

- `logFolder` (string) Where the current log file should be written (defaults to '.')
- `filenameTemplate` (string) `ow.template` for the log filename (defaults to 'log-{{timedate}}.log')
- `fileDateFormat` (string) File date format to be used in filenameTemplate (defaults to 'yyyy-MM-dd')
- `lineTemplate` (string) `ow.template` for each log line (defaults to '{{timedate}} | {{type}} | {{message}}\n')
- `lineDateFormat` (string) Date format to be used in lineTemplate (defaults to 'yyyy-MM-dd HH:mm:ss.SSS')
- `HKRegExPattern` (string) Housekeeping regular expression pattern to find log files (defaults to 'log-\\d{4}-\\d{2}-\\d{2}\\.log')
- `HKhowLongAgoInMinutes` (number) How many minutes of logs should be kept (if not defined won't delete files)
- `dontCompress` (boolean) Defines if older files should not be gzip (default to false)
- `backupFolder` (string) If defined older log files will be moved to this folder (if not defined they won't be moved)
- `numberOfEntriesToKeep` (number) Number of OpenAF log channel entries to keep in memory (defaults to 100)
- `setLogOff` (boolean) Turns off console logging (defaults to false)

### ow.ch.utils.syncCh

`ow.ch.utils.syncCh(aIdxsArray, aSource, aTarget, aSyncFn, aLogFn)`

Tries to sync all values from `aSource` with `aTarget` channel using the `aIdxsArray` (list of value indexes field).
Optionally `aSyncFn` can be provided to decide how to sync the values between source and target (defaults to return always true). A `aLogFn`
can be provided so all sync actions can be logged.

Table of sync actions given the return values of a custom syncFn(source, target) : boolean

| source | target | return true | return false |
|--------|--------|-------------|--------------|
| __     | def    | del target  | add source   |
| def    | __     | add target  | del source   |
| def    | def    | set target  | set source   |

### ow.ch.utils.timeseries

`ow.ch.utils.timeseries`

Helpers to query and feed channels of type `timeseries`. Every function takes the channel name first. A `selector` is a map
`{ metric, labels }` where `metric` and each label value can be a String, an Array (any of), a RegExp or a Function.

| Function | Returns | Description |
| --- | --- | --- |
| `series(aName, aSelector)` | Array | `{ metric, labels }` of the matching series |
| `labels(aName, aMetric)` | Map | Label names with their sorted values for a metric (or all metrics) |
| `latest(aName, aSelector)` | Array | Newest point of each matching series as flat rows |
| `range(aName, aSelector, aOptions)` | Array | Flat rows `{ ts, metric, ...labels, v }`. Options: `from`, `to`, `step` (ms or "1m"), `fn` (`avg`, `min`, `max`, `sum`, `count`, `first`, `last`, `rate`, `increase`; default `avg`), `fill` (`none`, `null`, `zero`, `prev`), `tier` (`raw` or a rollup step to force one) |
| `drop(aName, aSelector)` | Number | Removes the matching series, returns how many |
| `stats(aName)` | Map | Series and point counts, per metric and per tier |
| `housekeep(aName, aOptions)` | Number | Applies retention now (`{ now }` to measure from a given time); returns the removed entries |
| `rebuildRollups(aName)` | | Recomputes every rollup from the raw points |
| `compact(aName)` | Boolean | Rewrites the NDJSON file with the live data only |
| `save(aName)` | Boolean | Flushes pending changes now |
| `collect(aEvery, aName, aSource, aOptions)` | Map | Periodically records metrics (default `ow.metrics.getAll()`); returns `{ once, stop }` |
| `getTimeSeriesSubscriber(aTargetCh, aOptions)` | Function | Channel subscriber that records changes of another channel as points |
| `toOpenMetrics(aName, aSelector, aOptions)` | String | OpenMetrics text of the latest points (or all points with `from`/`to`) |
| `fromOpenMetrics(aName, aText, aOptions)` | Number | Records OpenMetrics text as points; returns how many |
| `pushPrometheus(aName, aPushGwUrl, aJob, aSelector, aOptions)` | Number | Pushes the latest point of each series to a Prometheus push gateway (one request per `groupBy` value); returns how many series were pushed |

With `step`, points are grouped in buckets aligned to the epoch and the row `ts` is the start of the bucket. When rollups exist, the finest
tier that reaches back to `from` and divides `step` is used. `rate` and `increase` treat a decrease in value as a counter reset (on rollup tiers they are approximate).

Example:

```javascript
ow.ch.utils.timeseries.range("m", { metric: "cpu", labels: { host: /^web/ } }, { from: "2026-01-01", step: "5m", fn: "max" });
```

### ow.ch.waitForJobs

`ow.ch.waitForJobs(aName, aTimeout) : ow.ch`

````text
Each channel subscription (using ow.ch.subscribe) will create internal jobs (threads). To wait for  this jobs to finish provide the channel aName and, optionally, aTimeout.
````
{% endraw %}
