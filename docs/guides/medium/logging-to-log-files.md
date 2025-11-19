---
layout: default
title: Logging to log files
parent: Medium
grand_parent: Guides
---

# Logging to log files

There are several benefits of using the OpenAF's _log*_ functions. One of them is to quickly have a logs folder with automated housekeeping with just a couple of lines of code.

Let's start with a simple script with _log_ functions:

````javascript
log("Init");

try {
    log("Writing file...");
    io.writeFileString("test.txt", "test");
    log("File test.txt written.");
} catch(e) {
    logErr("Couldn't write file test.txt. Error: " + String(e));
}

log("Done");
````

Executing you will get the expected standard output:

````bash
2019-12-08 09:19:00.540 | INFO | Init
2019-12-08 09:19:00.750 | INFO | Writing file...
2019-12-08 09:19:00.780 | INFO | File test.txt written.
2019-12-08 09:19:00.785 | INFO | Done
````

## Log to a folder

Let's log to a folder:

````javascript
ow.loadCh();
// Setting default logging to the logs folder
ow.ch.utils.setLogToFile({ logFolder: "logs" });
// Ensuring logs are written synchronously
setLog({ async: true });

log("Init");

try {
    log("Writing file...");
    io.writeFileString("test.txt", "test");
    log("File test.txt written.");
} catch(e) {
    logErr("Couldn't write file test.txt. Error: " + String(e));
}

log("Done");
````

Executing again the result seems similar but a new "logs" folder was created with a daily log file containing all the log messages. When creating a new daily log file it will automatically gzip all old daily log files.

But that's the standard behaviour that can, of course, be customizable. Let's add housekeeping to delete files older than one week:

````javascript
ow.loadCh();
ow.ch.utils.setLogToFile({ 
    logFolder: "logs",
    HKhowLongAgoInMinutes: 7200
});
//...
````

_p.s.: you can specify a different folder to hold the previous compressed log files using _backupFolder_. You can also control if old log files should be compressed or not with _dontCompress_._

## Logging to files by hour

The default is logging to daily files but you can customize to any date time grouping. To group files by hour can simply add a specific _fileDateFormat_. Additionally let's change the log filenames generated using _filenameTemplate_ (that uses handlebars notation).

Since we are changing the log filenames for the housekeeping process to be able to identify the new log filenames you need to provide a _HKRegExPattern_ regular expression pattern also.

{% raw %}````javascript
ow.loadCh();
ow.ch.utils.setLogToFile({
    logFolder: "logs",
    filenameTemplate: "hourly-logs-{{timedate}}.log",
    fileDateFormat: "yyyy-MM-dd-HH",
    HKhowLongAgoInMinutes: 7200,
    HKRegExPattern: "hourly-log-\\d{4}-\\d{2}-\\d{2}-\\d{2]\\.log"
});
//...
````{% endraw %}

## Logging as CSV files

To log into CSV files you just need to change the _filenameTemplate_ and the _lineTemplate_:

{% raw %}````javascript
ow.loadCh();
ow.ch.utils.setLogToFile({
    logFolder: "logs",
    filenameTemplate: "log-{{timedate}}.csv",
    lineTemplate: "\"{{timedate}}\";\"{{type}}\";\"{{{message}}}\"\n",
    HKhowLongAgoInMinutes: 7200
});
//...
````{% endraw %}

## Logging as NDJSON files

To log as NDJSON:

{% raw %}````javascript
ow.loadCh();
ow.ch.utils.setLogToFile({
    logFolder: "logs",
    filenameTemplate: "log-{{timedate}}.csv",
    lineTemplate: "{d:\"{{timedate}}\",t:\"{{type}}\",m:\"{{{message}}}\"}\n",
    HKhowLongAgoInMinutes: 7200
});
````{% endraw %}

## Keeping log entries only on files

You can also specify that log entries should only be recorded in the log files and not shown on the standard output console:

````javascript
ow.loadCh();
ow.ch.utils.setLogToFile({
    logFolder: "logs",
    setLogOff: true
});
````

## And more&#46;&#46;&#46;

You can check all the available options by executing:

````javascript
> help ow.ch.utils.setLogToFile
````

on an openaf-console prompt.