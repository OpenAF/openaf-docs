---
layout: default
title: ow.ch
parent: Reference
grand_parent: OpenAF docs
---


## ow.ch

### ow.ch.comms.getSubscriberFunc

__ow.ch.comms.getSubscriberFunc(aURL, aUUID, aLogin, aPassword, aTimeout)__

````
Returns a function to be used with ow.ch.subscribe for REST communication to the provided aURL intended to be used with ow.ch.server.*. Optionally aUUID can be provided to ignore subscriber request using it. Optionally you can provide aLogin, aPassword and/or a aTimeout (in ms).
````
### ow.ch.create

__ow.ch.create(aName, shouldCompress, type, options) : ow.ch__

````
Creates a channel of key/values with aName. Optionally you can specify if keys should also be compressed in memory (shouldCompress = true), a channels implementation type and corresponding options in a map.

Example:

ow.ch.create("myChan", false, "db", { db: myDB, from: "TABLE" });

````
### ow.ch.destroy

__ow.ch.destroy(aName) : ow.ch__

````
Deletes all data and removes references to the channel aName.
````
### ow.ch.forEach

__ow.ch.forEach(aName, aFunction) : ow.ch__

````
Will execute the provided aFunction with each key and value for the channel identified by the aName provided.
````
### ow.ch.get

__ow.ch.get(aName, aKey) : ow.ch__

````
Returns the value associated with the provided aKey on the channel identified by aName.
````
### ow.ch.getAll

__ow.ch.getAll(aName, fullInfo) : Array__

````
Will return all values for the channel identified by the aName provided.
````
### ow.ch.getKeys

__ow.ch.getKeys(aName, full) : Array__

````
Returns all keys in the form of an array for the channel identified by the aName provided. Optionally you can specify full = yes to obtain the detailed internal key index.
````
### ow.ch.getSet

__ow.ch.getSet(aName, aMatchMap, aKey, aValue, aTimestamp, aUUID)__

````
Tries to update the channel identified by the provided aName with aKey and aValue only if it's possible to get the same aKey and  aMatchMap matches the current aValue. Optionally you can provide the internal aTimestamp (if the provided aTimestamp is smaller than getVersion the value will not be set)
````
### ow.ch.getSortedKeys

__ow.ch.getSortedKeys(aName, full) : Array__

````
Returns all keys in the form of an array for the channel identified by the aName provided by order of the last modification. Optionally you can specify full = yes to obtain the detailed internal key index.
````
### ow.ch.getVersion

__ow.ch.getVersion(aName) : Number__

````
Returns the current version (usually a timestamp) for the aName channel.
````
### ow.ch.list

__ow.ch.list() : Array__

````
Returns a list the current channels available.
````
### ow.ch.persistence.create

__ow.ch.persistence.create(aChannel, aFilename, anArrayOfKeys, shouldCompress, forAll)__

````
Adds a channel identified by the name aChannel, trying to restore data from aFilename given anArrayOfKeys (strings representing the key fields). Optionally indicating if keys should be compressed in memory with shouldCompress = true and/or existing subscribers should run for all elements (forAll = true)
````
### ow.ch.persistence.getSubscriberFunc

__ow.ch.persistence.getSubscriberFunc(aFilename)__

````
Returns a function to be used with ow.ch.subscribe persisting any existing or new data into aFilename provided.
````
### ow.ch.persistence.restore

__ow.ch.persistence.restore(aChannel, aFilename, anArrayOfKeys) : Number__

````
Tries to restore that previously persisted using ow.ch.getSubscribeFunc from the aFilename using  anArrayOfKeys (strings representing the string list of fields used as index). The values will be restored to the aChannel name provided. Returns -1 in case of error or the data loaded length otherwise.
````
### ow.ch.pop

__ow.ch.pop(aName) : Object__

````
Mimics a LIFO queue behaviour by returning the last modified key/value entry for the channel aName. The entry will be removed from the channel.
````
### ow.ch.push

__ow.ch.push(aName, aKey, aValue) : ow.ch__

````
Equivalent to ow.ch.set trying to set, for the channel aName, aKey and aValue trying to mimic a queue behaviour.
````
### ow.ch.server.expose

__ow.ch.server.expose(aName, aLocalPortORServer, aPath, aAuthFunc, aUnAuthFunc, noCheck) : String__

````
Given aName channel and aLocalPortORServer will use the provided server, or start a simple http server on the  provided port, to expose access to the aName channel on the URL aPath. It will return an unique identifier to be use to identify incoming requests from this aPath and server on channel subscribe functions. Optionally you can also provide aAuthFunc(user, pass, aServer, aRequest) and aUnAuthFunc(aServer, aRequest) functions using ow.server.httpd.authBasic. The aAuthFunc can add aRequest.channelPermission to enforce read and/or write permissions on a channel (e.g. "r", "rw"). If needed you can ignore the checking if the aName channel exists with noCheck.

Example:

// Exposing the a log dump channel on port 8090 for test proposes.
ow.ch.server.expose("__log", 8090, "/log");


````
### ow.ch.server.peer

__ow.ch.server.peer(aName, aLocalPortORServer, aPath, aRemoteURLArray, aAuthFunc, aUnAuthFunc, aMaxTime, aMaxCount)__

````
Exposes aName channel in the same way as ow.ch.server.expose but it also add a subscribe function to  the aName channel to remotely peer with other expose channel(s) given aRemoteURLArray. Optionally you can also provide aAuthFunc(user, pass) and aUnAuthFunc(aServer, aRequest) functions using ow.server.httpd.authBasic. The aAuthFunc can add aRequest.channelPermission to enforce read and/or write permissions on a channel (e.g. "r", "rw"). Optionally you can provide aMaxTime for expiration of commands to retry to communicate and aMaxCount of commands to retry to communicate.

Example:

ow.ch.server.peer("__log", 8090, "/log", [ "http://server1.local:8090/log", "https://l:p@server2.local:8090/log" ]);


````
### ow.ch.server.routeProcessing

__ow.ch.server.routeProcessing(aURI, aRequest, aName) : HTTPServerReply__

````
Creates a server route processing for a ow.ch.comms client provided aURI, a HTTPServer aRequest and the  aName of a channel (please note that you should create the channel prior to using this function). Depending on aRequest.channelPermission some operations may not execute:

- "r" - allows channel get/getAll operations
- "w" - allows channel set/setAll/getSet/unset/unsetAll operations

Example:

var hs = ow.loadServer().httpd.start(17878);
ow.server.httpd.route(hs, { "/rest": function(r) { return ow.ch.server.routeProcessing("/rest", r, "my-channel") }});

for multiple channels:
var hs = ow.loadServer().httpd.start(17878);
ow.server.httpd.route(hs, {
   "/chan1": function(r) { return ow.ch.server.routeProcessing("/chan1", r, "chan-1") },
   "/chan2": function(r) { return ow.ch.server.routeProcessing("/chan2", r, "chan-2") }
};


````
### ow.ch.server.setLog

__ow.ch.server.setLog(aLogFunction)__

````
Sets aLogFunction to act as audit for external communication to access a channel. The aLogFunction will be called passing, as a single argument, a map with:
   - name    (the channel name)
   - op      (the operation can be AUTH_OK, AUTH_NOT_OK, GET, SET, REMOVE or CREATE)
   - request (the HTTP request map)

The request, when available, will include an entry with the current user.


````
### ow.ch.server.unpeer

__ow.ch.server.unpeer(aName, aRemoteURL)__

````
Remove all subscribers related with aRemoteURL from the aName channel effectively "unpeering" it from the aRemoteURL.
````
### ow.ch.set

__ow.ch.set(aName, aKey, aValue, aTimestamp)__

````
Tries to insert/update the channel identified by the provided aName with aKey and aValue. Optionally you can provide the internal aTimestamp (if the provided aTimestamp is smaller than getVersion the value will not be set)
````
### ow.ch.setAll

__ow.ch.setAll(aName, anArrayOfKeys, anArrayOfMapData, aTimestamp)__

````
Given anArrayOfKeys composed of strings identifying the key fields from the anArrayOfMapData provided will try to insert/update all values on the channel identified by aName. Optionally you can provide aTimestamp  (if the provided aTimestamp is smaller than getVersion the value will not be set)
````
### ow.ch.shift

__ow.ch.shift(aName) : Object__

````
Mimics a FIFO queue behaviour by returning the first modified key/value entry for the channel aName. The entry will be removed from the channel.
````
### ow.ch.size

__ow.ch.size(aName) : Number__

````
Returns the number of keys currently available for the channel aName.
````
### ow.ch.stopAllJobs

__ow.ch.stopAllJobs(aName) : ow.ch__

````
Each channel subscription (using ow.ch.subscribe) will create internal jobs (threads). To stop all these immediately provide the channel aName.
````
### ow.ch.subscribe

__ow.ch.subscribe(aName, aFunction, onlyFromNowm, anId) : String__

````
Adds a callback function to the channel aName. The callback function will receive, as arguments: the channel name, the operation, a key or an array of keys (for operation = setall/unsetall), a value or an array  of values (for operation = setall/unsetall) and the ow.ch object. Returns the subscriber id. Optionally you can specify that existing elements won't trigger operation = set callback calls and/or a custom subscriber anId.

Possible operations:
   - set
   - setall
   - unset
   - unsetall


````
### ow.ch.types.all

__ow.ch.types.all__

````
This channel type aggregates access to several channels. The creation options are:

   - chs      (Array)    An array of names of channels to aggregate.
   - fn       (Function) A function that will receive an operation, a key and value (when applicable)) to return which channel name should be used (if no return or void all channels will be considered).
   - errFn    (Function) A function to call with: the name of this channel, the exception, the target channel, the operation and the arguments whenever a error occurs accessing a channel.
   - fnTrans  (Function) A function to translate the key (for example, to remove elements used only on fn).
   - fnKeys   (Function) Allows to filter an array of resulting keys, from different channels, for: getKeys, getSortedKeys
   - fnValues (Function) Allows to filter an array of resulting values, from different channels, for: getAll, get, getSet, set and unset
   - treatAll (Boolean)  If true size, setAll and unsetAll will be executed individually and fn called for each (default is false and size will take the first result)


````
### ow.ch.types.buffer

__ow.ch.types.buffer__

````
This OpenAF implementation establishes a buffer to another channel. The creation options are:

   - bufferCh       (String)   The channel that will receive data from the buffer channel.
   - bufferIdxs     (Array)    An array of keys to use for faster performance (defaults to []).
   - bufferByTime   (Number)   How much time before flushing contents from the buffer channel (default 2500ms).
   - bufferByNumber (Number)   How many entries before flushing contents from the buffer channel (default 100).
   - bufferTmpCh    (String)   The auxiliary temporary buffer storage channel to use (default creates [name]::__bufferStorage).
   - bufferFunc     (Function) Optional function that if returns true will trigger the buffer flush to bufferCh.


````
### ow.ch.types.db

__ow.ch.types.db__

````
This OpenAF channel implementation wraps access to a db table. The creation options are:

   - db   (Database) The database object to access the database table (or a JSON/SLON string with 'url', 'user', 'pass', 'timeout', 'driver').
   - from (String)   The name of the database table or object (don't use double quotes).
   - keys (Array)    An array of fields keys to use (don't use double quotes).
   - cs   (Boolean)  Determines if the database is case sensitive for table and field names (defaults to false).


````
### ow.ch.types.elasticsearch

__ow.ch.types.elasticsearch__

````
This OpenAF implementation connects to an ElasticSearch (ES) server/cluster. The creation options are:

   - index       (String/Function) The ES index to use or a function to return the name (see also ow.ch.utils.getElasticIndex).
   - format      (String)          If index is a string will use format with ow.ch.utils.getElasticIndex.
   - idKey       (String)          The ES key id field. Defaults to 'id'.
   - url         (String)          The HTTP(S) URL to access the ES server/cluster.
   - user        (String)          Optionally provide a user name to access the ES server/cluster.
   - pass        (String)          Optionally provide a password to access the ES server/cluster (encrypted or not).
   - fnId        (String/Function) Optionally called on every operation to calculate the idKey with the key provided as argument. If string will the corresponding hash function (md5/sha1/etc...) with sortMapKeys + stringify.
   - size        (Number)          Optionally getAll/getKeys to return more than 10 records (up to 10000).
   - stamp       (Map)             Optionally merge with stamp map.
   - timeout     (Number)          Optional request timeout in ms.
   - preAction   (Function)        Optional function to be called before every request.

The getAll/getKeys functions accept an extra argument to provide a ES query map to restrict the results.
````
### ow.ch.types.file

__ow.ch.types.file__

````
This OpenAF implementation implements a simple channel on a single JSON or YAML file. The creation options are:

   - file      (String)  The filepath to the JSON or YAML file to use (if multifile is false)
   - path      (String)  The path to use to store JSON or YAML objects to use (if multifile is true)
   - yaml      (Boolean) Use YAML instead of JSON (defaults to false)
   - compact   (Boolean) If JSON and compact = true the JSON format will be compacted (defaults to false or shouldCompress option)
   - multifile (Boolean) If true instead of keeping values in one file it will be kept in multiple files (*)
   - multipart (Boolean) If YAML and multipart = true the YAML file will be multipart
   - key       (String)  If a key contains "key" it will be replaced by the "key" value
   - multipath (Boolean) Supports string keys with paths (e.g. ow.obj.setPath) (defaults to false)
   - lock      (String)  If defined the filepath to a dummy file for filesystem lock while accessing the file
   - gzip      (Boolean) If true the output file will be gzip (defaults to false)
   - lz4       (Boolean) If true the output file will be lz4 (defaults to false)
   - tmp       (Boolean) If true "file" will be temporary and destroyed upon execution/process end

(*) - Be aware that althought there is a very small probability of collision between the unique id (sha-512) for filenames it still exists


````
### ow.ch.types.ignite

__ow.ch.types.ignite__

````
This channel type will use an Ignite Data Grid. The creation options are:

   - ignite (Ignite) Use a previously instantiated Ignite plugin (defaults to a new instance).
   - gridName (String) Use a specific Ignite grid name.


````
### ow.ch.types.mvs

__ow.ch.types.mvs__

````
The channel type mvs uses H2 MVStore to keep key/value structures either in memory or in files. The creation options are:

   - file (String) If not defined it will default to the in-memory implementation otherwise a file.
   - shouldCompress (Boolean) Specifies if it should compress the entire structure or not.
   - compact (Boolean) Upon channel create/destroy it will try to run a compact operation over the file to save space.
   - map (String/Function) The map name (defaults to 'default'). If defined as a function it will receive the key as argument if possible (only for get/set/unset/setall) for sharding proposes.

The map will be created if it doesn't exist. Operations getKeys/getAll can be paginated with the extra map argument containing start and end

````
### ow.ch.types.ops

__ow.ch.types.ops__

````
This OpenAF channel implementation encapsulates access based on functions. The creation options are a map of keys where each value is a function.

Example:

ow.ch.create("logic", false, "ops", { hello: name => "hi " + name });

````
### ow.ch.types.prometheus

__ow.ch.types.prometheus__

````
This OpenAF implementation connects to a prometheus server. The creation options are:

   - urlQuery  (String) The URL of a prometheus server (e.g. http://prometheus:9090) 
   - urlPushGW (String) The URL of a prometheus push gateway server (e.g. http://prometheus:9091).
   - prefix    (String) If defined the prefix for all openmetrics.
   - gwGroup   (Map)    A map of grouping labels for data ingestion by the push gw (job label must be defined).
   - helpMap   (Map)    The helpMap for the openmetrics (see more in ow.metrics.fromObj2OpenMetrics).

The forEach/getSet/pop/shift/unsetAll functions are not supported.
The size function retrieves the total number of labels.
The get/getAll function enables instant query (with the extra map key query), query range query (with the extra map keys query, start and end) and label values query (with the extra map key label).
The set/setAll functions only consider the value(s) argument, the key(s) is ignored.

Note: query by specific series are not currently supported.

````
### ow.ch.types.proxy

__ow.ch.types.proxy__

````
This OpenAF implementation establishes a proxy to another channel. The creation options are:

   - chTarget  (String)   The channel that will receive all operations (if proxyFunc doesn't return).
   - proxyFunc (Function) Function that receives a map (by reference that can be changed) with: op (operation), name (target channel), function (where applicable), full (where applicable), match (the match of getSet), k (the key(s)), v (the value(s)) and timestamp. If this function returns something no operation will be executed on the chTarget and the value returned by the function will be the value returned by this channel.


````
### ow.ch.unset

__ow.ch.unset(aName, aKey, aTimestamp) : ow.obj.channel__

````
Tries to remove all associations to the provided aKey on the channel identified by aName. Optionally aTimestamp can be provided.
````
### ow.ch.unsetAll

__ow.ch.unsetAll(aName, anArrayOfKeys, anArrayOfMapData, aTimestamp)__

````
Given anArrayOfKeys composed of strings identifying the key fields from the anArrayOfMapData provided will try to delete all values on the channel identified by aName. Optionally you can provide aTimestamp  (if the provided aTimestamp is smaller than getVersion the value will not be set)
````
### ow.ch.unsubscribe

__ow.ch.unsubscribe(aName, aId) : ow.ch__

````
Tries to unsubscribe aId callback from the channel identified by the aName provided.
````
### ow.ch.unsubscribeAll

__ow.ch.unsubscribeAll(aName) : ow.ch__

````
Tries to unsubscribe all callback functions from the channel identified by the aName provided.
````
### ow.ch.utils.closeBuffer

__ow.ch.utils.closeBuffer(aName)__

````
Tries to close and flush a channel buffer with aName (if not provided assumes all buffer type channels).
````
### ow.ch.utils.flushBuffer

__ow.ch.utils.flushBuffer(aName)__

````
Tries to flush a channel buffer with aName (if not provided assumes all buffer type channels).
````
### ow.ch.utils.getBufferSubscriber

__ow.ch.utils.getBufferSubscriber(aSourceCh, indexes, byNumber, byTimeInMs, aBufferCh, aTmpBufferCh, aFilterFunc, aBufferFunc) : Function__

````
Returns a channel subscriber function that will buffer set, setall, unsetall and unset operations from aSourceCh channel to aBufferCh (by default a dummy channel to be subscribed, if not defined the name will be aSourceCh + "::buffer"). As a temporary buffer channel aTmpBufferCh will be used (if not defined the name will be aSourceCh + "::__bufferStorage"). The aBufferCh will be configured with the provided indexes, byNumber (number of times to trigger the buffer) and byTimeInMs (amount of time in ms to trigger the buffer). Additionally you can specify aFilterFunc (with arguments channel, operation, key(s) and value(s)) that will only buffer if returns false and aBufferFunc that will trigger the buffer flush if it returns true.

NOTE: do call ow.ch.utils.closeBuffer(aSourceCh) when it's no longer needed.


````
### ow.ch.utils.getElasticIndex

__ow.ch.utils.getElasticIndex(aPrefix, aFormat) : Function__

````
Returns a function to be used for generating ElasticSearch indexes with aPrefix-aDate (in the format of YYYY.MM.DD). This helps to generate a specific index per day. If a specific format is needed you can provided it as aFormat (see ow.format.fromDate)).
````
### ow.ch.utils.getElasticQuery

__ow.ch.utils.getElasticQuery(aQueryString) : Map__

````
Returns a query map using aQueryString (using lucene query string (like in Kibana)) to be used on getAll, for example.
````
### ow.ch.utils.getFileHousekeepSubscriber

__ow.ch.utils.getFileHousekeepSubscriber(aFolder, aRegExPattern, howLongAgoInMinutes, dontCompress, aBackupFolder) : Function__

````
Returns a channel subscriber function to perform file housekeep (specially useful with ow.ch.utils.getLogFilePerDate) given the main aFolder where just the newest file whose filename matches aRegExPattern (e.g. "log\\d{4}-\\d{2}-\\d{2}\\.log") will be kept uncompressed. All other files will be gziped (if dontCompress = false) and moved to aBackupFolder (if defined, defaults to aFolder). If howLongAgoInMinutes is defined all  files older than now - howLongAgoInMinutes will be deleted from the aBackupFolder.
````
### ow.ch.utils.getHousekeepSubscriber

__ow.ch.utils.getHousekeepSubscriber(aTargetCh, maxNumberOfKeys) : Function__

````
Returns a channel subscriber function that will keep the channel size to the maximum of maxNumberOfKeys (defaults to 100). If the number of keys is bigger than maxNumberOfKeys than it will perform a channel unset operation (that will, depending on the type of channel, remove the oldest element).
````
### ow.ch.utils.getLogFilePerDate

__ow.ch.utils.getLogFilePerDate(aLogFolder, aTemplate, aFileDateFormat, aLineTemplate, aLineDateFormat) : Function__

````
Returns a function to be used to generate a log file in aLogFolder path. If the log file already exists it will append to it. You can customize the log filename format using a aTemplate (e.g. "log-{{timedate}}.log" by default). The "timedate" is defined on the aFileDateFormat (e.g. "yyyy-MM-dd" by day, "yyyy-MM-dd-HH" by hour (check ow.format.fromDate for more options)). Each line that will be append to the file can be defined by aLineTemplate (e.g. "{{timedate}} | {{type}} | {{message}}"  by default) where "type" is the of logging (INFO, WARN, ERROR), "message" the logged message and "timedate" is defined on the aLineDateFormat (e.g. "yyyy-MM-dd HH:mm:ss.SSS" by default (check ow.format.fromDate for more options)).
````
### ow.ch.utils.getLogStashSubscriber

__ow.ch.utils.getLogStashSubscriber(aTargetCh, aType, aHost, aErrorFunc, shouldHK, stampMap) : Function__

````
Returns a channel subscriber function that will transform changes to a log channel (see startLog and the __log channel) and will replicate them in aTargetCh (this means expecting the value to have a 'd': date; 'm': message and 't' as the level/type). The value set on aTargetCh will follow the LogStash format setting type to aType and host to aHost. The id and key will be set  to a sha1 hash of the stringify version of the value being set. In case of error aErrorFunc will be invoked providing the exception as an argument. You can also indicate if you want to house keep the original channel to save the script's memory and a stampMap to force entries on all maps sent.
````
### ow.ch.utils.getMirrorSubscriber

__ow.ch.utils.getMirrorSubscriber(aTargetCh, aFunc) : Function__

````
Returns a channel subscriber function that will mirror any changes to aTargetCh if aFunc(key, op) returns true when invoked with the key being changed and the corresponding operation.
````
### ow.ch.utils.getStatsProxyFunction

__ow.ch.utils.getStatsProxyFunction(aStatsCh) : Function__

````
Returns a proxy function to be use with a proxy channel. The aStatsCh where to store the channel access statistics.
````
### ow.ch.utils.keepHistory

__ow.ch.utils.keepHistory(timeRepeatExpression, aName, aFunction, withKeys, historySize) : Object__

````
For a given aName channel (preferably a temporary one) will execute aFunction periodically given a timeRepeatExpression (if a Number the ms interval, if a String a cron expression). That aFunction should return aMap for which the withKeys array will be used to determine the keys entries to set it on the provided aName channel (if withKeys is not provided, id will be assumed and filled with nowNano()). The channel aName will be filled with entries with the result of executing aFunction periodically thus keeping an history of results (by default 10 if a historySize is not provided). An object with a stop function will be returned so the keepHistory periodical behaviour of runnning aFunction and keeping the results in the channel aName.
````
### ow.ch.utils.mvs.list

__ow.ch.utils.mvs.list(aMVSFile) : Array__

````
Returns a list of names of maps in the corresponding aMVSFile.
````
### ow.ch.utils.mvs.remove

__ow.ch.utils.mvs.remove(aMVSFile, aMapToRemove)__

````
Removes aMapToRemove on the provided aMVSFile.
````
### ow.ch.utils.mvs.rename

__ow.ch.utils.mvs.rename(aMVSFile, anOriginalMap, aDestinationMap)__

````
Renames anOriginalMap by aDestinationMap on the provided aMVSFile.
````
### ow.ch.utils.poolChanges

__ow.ch.utils.poolChanges(aCh, idKeys, aChM)__

````
When executed pools to find all changes in aCh, using an idKeys array of key map fields, and executing a setAll on aCh for the changed entries. To compare it stores the last version in a 'aCh + "::chMemory"' channel that can be created with aChM map options ($ch type and options entries). Usefull to trigger channel subscribed functions when the aCh type doesn't detect automatically changes. Should be used with small sized channels as datasets are compared in memory.
````
### ow.ch.utils.setLogToFile

__ow.ch.utils.setLogToFile(aConfigMap)__

````
Shortcut to set OpenAF's logging into a rotating per date set of log files. You can set any of these options:

logFolder             (string)  Where the current log file should be written (defaults to '.')
filenameTemplate      (string)  ow.template for the log filename (defaults to 'log-{{timedate}}.log')
fileDateFormat        (string)  File date format to be used in filenameTemplate (defaults to 'yyyy-MM-dd')
lineTemplate          (string)  ow.template for each log line (defaults to '{{timedate}} | {{type}} | {{message}}\n')
lineDateFormat        (string)  Date format to be used in lineTemplate (defaults to 'yyyy-MM-dd HH:mm:ss.SSS')
HKRegExPattern        (string)  Housekeeping regular expression pattern to find log files (defaults to 'log-\\d{4}-\\d{2}-\\d{2}\\.log')
HKhowLongAgoInMinutes (number)  How many minutes of logs should be kept (if not defined won't delete files)
dontCompress          (boolean) Defines if older files should not be gzip (default to false)
backupFolder          (string)  If defined older log files will be moved to this folder (if not defined they won't be moved)
numberOfEntriesToKeep (number)  Number of OpenAF log channel entries to keep in memory (defaults to 100)
setLogOff             (boolean) Turns off console logging (defaults to false)


````
### ow.ch.utils.syncCh

__ow.ch.utils.syncCh(aIdxsArray, aSource, aTarget, aSyncFn, aLogFn)__

````
Tries to sync all values from aSource with aTarget channel using the aIdxsArray (list of value indexes field). Optionally aSyncFn can be provided to decide how to sync the values between source and target (defaults to return always true). A aLogFn can be provided so all sync actions can be logged.

Table of sync actions given the return values of a custom syncFn(source, target) : boolean

  | source | target | return true | return false |
  |--------|--------|-------------|--------------|
  | __     | def    | del target  | add source   |
  | def    | __     | add target  | del source   |
  | def    | def    | set target  | set source   |


````
### ow.ch.waitForJobs

__ow.ch.waitForJobs(aName, aTimeout) : ow.ch__

````
Each channel subscription (using ow.ch.subscribe) will create internal jobs (threads). To wait for  this jobs to finish provide the channel aName and, optionally, aTimeout.
````
