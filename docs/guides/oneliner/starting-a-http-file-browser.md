---
layout: default
title: Starting a HTTP file browser
parent: OneLiner
grand_parent: Guides
---

# Starting a HTTP file browser

On the article [Micro remote HTTP file browser](https://openafs.blogspot.com/2019/07/micro-remote-http-file-browser.html) we described a fast way to build a micro HTTP server serving files from the current folder. But some (myself included) need faster ways to do it instead of creating an oJob file and executing it.

So doing the same thing on one line that you can just copy+paste whenever you need can be very pratical. But you will be sacrifying readability by anyone else and you. Since oJobs can be used in YAML or JSON this enables you to build a YAML oJob file and then convert it to JSON string where initilization parameters can be easily change. Additionally you can convert back to YAML very easily.

## Example

Let's use the micro remote HTTP file browser example. Since YAML provides some features that JSON doesn't (like anchors) the original YAML needs some adaptation:

`httpd.yaml`
````yaml
init:
  port: 8080
  path: "."
  uri : "/"

ojob:
  daemon    : true
  sequential: true
  opacks    :
    - oJob-common

include:
  - oJobHTTPd.yaml

todo:
  - name: Init
  - name: HTTP Start Server
    args: "({ port: global.init.port, mapLibs: true })"
  - name: HTTP File Browse
    args: "({ port: global.init.port, path: global.init.path, uri: global.init.uri })"

jobs:
  # ----------
  - name: Init
    exec: "global.init = args.init;"
````

## Convert to a JSON one-liner

Then to convert this YAML file into a JSON string use openaf-console and execute:

````javascript
> print(stringify(io.readFileYAML("httpd.yaml"), void 0, ""))

{"init":{"port":8080,"path":".","uri":"/"},"ojob":{"daemon":true,"sequential":true,"opacks":["oJob-common"]},"include":["oJobHTTPd.yaml"],"todo":[{"name":"Init"},{"name":"HTTP Start Server","args":"({ port: global.init.port, mapLibs: true })"},{"name":"HTTP File Browse","args":"({ port: global.init.port, path: global.init.path, uri: global.init.uri })"}],"jobs":[{"name":"Init","exec":"global.init = args.init;"}]}
````

## Use the JSON one-liner

Then to use this JSON as an one-liner:

````javascript
> oJobRun( /* one-liner begin */  {"init":{"port":8080,"path":".","uri":"/"},"ojob":{"daemon":true,"sequential":true,"opacks":["oJob-common"]},"include":["oJobHTTPd.yaml"],"todo":[{"name":"Init"},{"name":"HTTP Start Server","args":"({ port: global.init.port, mapLibs: true })"},{"name":"HTTP File Browse","args":"({ port: global.init.port, path: global.init.path, uri: global.init.uri })"}],"jobs":[{"name":"Init","exec":"global.init = args.init;"}]}  /* one-liner end */ );
````

To stop just hit "Ctrl-C".

## Making changes

If you need to change the folder, port or uri used it's easy to just direclty change on the first init map:

````text
{"init":{"port":8080,"path":".","uri":"/"},
````

To convert it back to YAML:

````javascript
io.writeFileYAML("httpd.yaml", /* one-liner begin */  {"init":{"port":8080,"path":".","uri":"/"},"ojob":{"daemon":true,"sequential":true,"opacks":["oJob-common"]},"include":["oJobHTTPd.yaml"],"todo":[{"name":"Init"},{"name":"HTTP Start Server","args":"({ port: global.init.port, mapLibs: true })"},{"name":"HTTP File Browse","args":"({ port: global.init.port, path: global.init.path, uri: global.init.uri })"}],"jobs":[{"name":"Init","exec":"global.init = args.init;"}]}  /* one-line end */ );
````

_Note: since you lose comments we would recommed you to just use the original YAML file._
