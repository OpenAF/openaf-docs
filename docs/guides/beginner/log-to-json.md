---
layout: default
title: Log to JSON
parent: Beginner
grand_parent: Guides
---

_applies to version >= 20211229_

# Log to JSON

The [OpenAF logging functionality](/docs/howto/Use-log) allows to change the template used to output stdout/stderr log messages including to JSON (see more in [logging to log files](/docs/guides/medium/logging-to-log-files)).

There is also built-in functionality to change the default template to a _logstash_ JSON compatible format which is useful which the OpenAF execution is performed on a container, for example.

## Logging to JSON in a script

To change the default stdout/stderr template output to a _logstash_ JSON compatible format on a simple OpenAF script you just need to execute the following code:

````javascript
setLog({ format: "json" })
````

Then whenever a _log_ function is executed the output will be in JSON:

````javascript
log("This is a test")
// {"@timestamp":"2022-01-01T01:02:03.010Z","level":"INFO","message":"This is a test"}
logErr("This is an error")
// {"@timestamp":"2022-01-01T01:02:03.110Z","level":"ERROR","message":"This is an error"}
````

## Logging to JSON in oJob

On oJob you can specify the same setting in the "ojob" section:

````yaml
todo:
- a log test

ojob:
 log         :
   format: json
 logToConsole: false  # For all JSON output

jobs:
- name: a log test
  exec: log('executing')
````

## Logging to JSON with the oJobRT

When launching an oJobRT container you just need to specify the OJOB_JSONLOG environment variable to "true":

````bash
docker run --rm -ti -v "$(pwd)":/test -e OJOB_CONFIG=/test/mytest.yaml -e OJOB_METHOD=local -e OJOB_JSONLOG=true openaf/ojobrt
````

Check the [openaf-dockers project](https://github.com/OpenAF/openaf-dockers/blob/master/oJobRT/README.md) for more details.
