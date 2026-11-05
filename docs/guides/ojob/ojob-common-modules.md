---
layout: default
title: oJob-common modules
parent: oJob
grand_parent: Guides
---

{% raw %}
# oJob-common module index

OpenAF provides built-in lowercase `ojob …` jobs through `ojob.yaml` / `includeOJob: true`. The **oJob-common** oPack supplies the modules below, normally containing `oJob …` jobs. Include only the modules your workflow needs. See the [job reference](ojob-common-reference.md) for arguments and examples.

```yaml
ojob:
  opacks:
    oJob-common: ">=20261030"
include:
- oJobBasics.yaml
todo:
- name: oJob Print args
  args:
    message: Hello
```

## oJobBasics

[Source definition](https://github.com/OpenAF/oJob-common/blob/130addf46fb52ca733da6a66bf7b990430006caf/oJobBasics.yaml).

| Job | Description from source help |
| --- | --- |
| `oJob Start` | See source definition and its argument checks. |
| `oJob Shutdown` | See source definition and its argument checks. |
| `oJob Stop` | See source definition and its argument checks. |
| `oJob Exit` | See source definition and its argument checks. |
| `oJob Sleep 5s` | See source definition and its argument checks. |
| `oJob Sleep 1s` | See source definition and its argument checks. |
| `oJob Stringify` | This job prints to the console the provided javascript expression. Expects: |
| `oJob Set` | Assigns a value to a variable. Expects: |
| `oJob Path Set` | Assigns a value to a variable on a specific path. Expects: |
| `oJob YAML` | This job prints to the console the provided javascript expression as YAML. Expects: |
| `oJob Sort Array` | This job sorts a variable 'srcName' to 'name'. Expects: |
| `oJob Map Array` | This job sets a variable 'name' from a srcName array of maps remapped with the provided selectors. Expects: |
| `oJob Map` | This job sets a variable 'name' mapped using $path/JMESPath, defined by path, from the variable/expression 'srcName'. Expects: |
| `oJob From global` | This job will reset or merge a global variable map. Expects: |
| `oJob Args from JSON` | This job will load the args map from a JSON file. Expects: |
| `oJob Args from YAML` | This job will load the args map from a YAML file. Expects: |
| `oJob Split into items` | Splits a string in args into an array of maps stored in args._list. Expects: |
| `oJob Print list` | Prints the current args._list as YAML. |
| `oJob Print args` | Prints args (or a sub-path) as YAML. Optionally expects: |
| `oJob Get kept result` | Retrieves a previously kept result saved with oJob Keep result. Optionally expects: |
| `oJob Keep result` | Keeps the current args result to be retrieved later with oJob Get kept result or oafGetResult(aName). Optionally expects: |
| `oJob Switch` | Adds new todo entries depending on the value of a provided args variable. Expects: |
| `oJob Sec Get` | Retrieves a SBucket secret and maps it into args: |
| `oJob sh` | This job runs a local shell command and accepts the following args: |
| `oJob Process Launch` | Launches a process in background. |
| `oJob Process Wait` | Waits for the background launched processes. |
| `oJob Show Log` | See source definition and its argument checks. |
| `oJob Jobs Report` | Outputs a jobs report (e.g. job name, status, number of executions, total time, avg time and last execution) |
| `oJob Jobs Final Report` | See source definition and its argument checks. |
| `oJob A2B` | Will execute A code providing a function (fn) to send data, in batches, to B code which receives it async as values. Expects: |
| `oJob Get settings` | Will retrieve the yaml settings stored on the user home folder |
| `oJob Set settings` | Will set yaml settings stored on the user home folder |

## oJobBrowse

[Source definition](https://github.com/OpenAF/oJob-common/blob/130addf46fb52ca733da6a66bf7b990430006caf/oJobBrowse.yaml). Includes: `oJobHTTPd.yaml`.

| Job | Description from source help |
| --- | --- |
| `HTTP Browser` | Provides a HTTP browser service based on an existing type. |
| `HTTP Browse generic` | Provides a HTTP browse definition. |
| `HTTP Browse API` | Provides a HTTP API to access getList/getObj for any HTTP Browse generic implementation. |

## oJobCh

[Source definition](https://github.com/OpenAF/oJob-common/blob/130addf46fb52ca733da6a66bf7b990430006caf/oJobCh.yaml).

| Job | Description from source help |
| --- | --- |
| `oJob Ch Start Buffering` | Creates a buffering channel between a source and a target channel. Expects: |
| `oJob Ch Stop Buffering` | Stops buffering between a source and a target channel previously set up by oJob Ch Start Buffering. Expects: |
| `oJob Ch Wait For Jobs` | Waits for the jobs associated with a channel. Expects: |

## oJobDebug

[Source definition](https://github.com/OpenAF/oJob-common/blob/130addf46fb52ca733da6a66bf7b990430006caf/oJobDebug.yaml).

| Job | Description from source help |
| --- | --- |
| `oJob Debug Args` | See source definition and its argument checks. |

## oJobDirector

[Source definition](https://github.com/OpenAF/oJob-common/blob/130addf46fb52ca733da6a66bf7b990430006caf/oJobDirector.yaml).

| Job | Description from source help |
| --- | --- |
| `oJob Director init` | Initializes an oJob Director expecting: |
| `oJob Director checkin` | Checks in a specific job with a jobUUID execution (to be used with "from"). Will not execute further job code if the job name and uuid have already been executed. |
| `oJob Director checkout` | Checks out a specific job with a jobUUID execution (to be used with "to"): |
| `oJob Director check` | Checks if a specific job with a jobUUID execution has executed or not. If yes, it will warn and return from the current job (to be used with "from"): |
| `oJob Director wait` | Waits for a specific job with a jobUUID execution (to be used with "from"). If it timesout waiting it will throw an exception. |

## oJobES

[Source definition](https://github.com/OpenAF/oJob-common/blob/130addf46fb52ca733da6a66bf7b990430006caf/oJobES.yaml).

| Job | Description from source help |
| --- | --- |
| `Start Log to ES` | Starts logging to ElasticSearch. Expects: |
| `Stop ES logging` | Stops logging to ElasticSearch. |

## oJobEmail

[Source definition](https://github.com/OpenAF/oJob-common/blob/130addf46fb52ca733da6a66bf7b990430006caf/oJobEmail.yaml).

| Job | Description from source help |
| --- | --- |
| `oJob Send email` | This job tries to send an email. |

## oJobGIT

[Source definition](https://github.com/OpenAF/oJob-common/blob/130addf46fb52ca733da6a66bf7b990430006caf/oJobGIT.yaml).

| Job | Description from source help |
| --- | --- |
| `GIT Copy Repository` | Will copy a GIT repository files. Expects: |

## oJobHBS

[Source definition](https://github.com/OpenAF/oJob-common/blob/130addf46fb52ca733da6a66bf7b990430006caf/oJobHBS.yaml).

| Job | Description from source help |
| --- | --- |
| `oJob HBS Add helpers` | See source definition and its argument checks. |
| `oJob HBS file` | This job will apply an args.template hbs file using args.data to produce a new file (args.target). |
| `oJob HBS` | This job will apply an args.template hbs file using args.data to produce contents to args.output. |

## oJobHTTPd

[Source definition](https://github.com/OpenAF/oJob-common/blob/130addf46fb52ca733da6a66bf7b990430006caf/oJobHTTPd.yaml).

| Job | Description from source help |
| --- | --- |
| `HTTP Start Server` | Provides and starts a HTTP server. |
| `HTTP Apply Service` | See source definition and its argument checks. |
| `HTTP Stop Server` | Sets a shutdown job for the server. If using sequential do ensure that the job 'HTTP Start Server' gets executed first. |
| `HTTP Default Auth` | Provides a default authentication function for all routes on a given port. |
| `HTTP Service` | Provides a HTTP service definition. If using sequential jobs do ensure that the job 'HTTP Start Server' gets executed first. |
| `HTTP Default` | Provides a HTTP default handler. |
| `HTTP Redirect` | Provides a HTTP default handler. |
| `HTTP Upload` | Provides a HTTP upload handler. |
| `HTTP Healthz` | Adds a healthz URI |
| `HTTP Metrics` | Adds a metrics URI with a OpenMetrics/Prometheus output |
| `HTTP Add Metric` | Add a metric to the current daemon execution |
| `HTTP markdown` | Adds a markdown URI |
| `HTTP Classical File Browse` | Provides a classical HTTP file browse definition. |
| `HTTP File Browse` | Provides a HTTP file browse definition. |
| `HTTP SSE Service` | Provides a Server-Sent Events (SSE) streaming endpoint. If using sequential jobs do ensure that the job 'HTTP Start Server' gets executed first. |

## oJobIO

[Source definition](https://github.com/OpenAF/oJob-common/blob/130addf46fb52ca733da6a66bf7b990430006caf/oJobIO.yaml).

| Job | Description from source help |
| --- | --- |
| `IO Append File` | Appends a line to a file. Expects: |
| `IO Find &amp; Replace` | Finds and replaces text on a target. Expects: |
| `IO MV File` | Moves a source to a target. Expects: |
| `IO RM File` | Removes a file or directory recursively. Expects: |
| `IO CP File` | Copies a source to a target. Expects: |
| `IO List files` | List files from a local filepath to args.files array. Expects: |
| `IO List filenames` | List filenames from a local filepath to args.files array. Expects: |
| `IO Modify text file` | Given a file tries to find the first string 'find' and replace with 'replace'. If the file doesn't exist it will create it. It differs from the "IO Find &amp; Replace" job as it doesn't use regular expressions and just looks for exact matches which is usually more pratical for text configuration files. Expects: |

## oJobMCP

[Source definition](https://github.com/OpenAF/oJob-common/blob/130addf46fb52ca733da6a66bf7b990430006caf/oJobMCP.yaml). Includes: `oJobHTTPd.yaml`.

| Job | Description from source help |
| --- | --- |
| `HTTP MCP Server` | Starts a MCP server to handle requests with execution of jobs. |
| `STDIO MCP Server` | Starts a MCP stdio to handle requests with execution of jobs. |

## oJobManager

[Source definition](https://github.com/OpenAF/oJob-common/blob/130addf46fb52ca733da6a66bf7b990430006caf/oJobManager.yaml).

| Job | Description from source help |
| --- | --- |
| `oJobManager Init` | Initializes oJobManager creating the oJobManager-jobs and oJobManager-locks channels. It also provides the function global.oJobManagerLaunchJob(aJobName, aArgs) that enables the launching of containers (include the docker opack to launch in docker). Optionally expects: |
| `oJobManager Error` | Provides the error handling functionality. Should be used directly on a catch property when executing oJobManager Start and oJobManager End. |
| `oJobManager Job Start` | Check and registers a container job to start. Expects: |
| `oJobManager Job End` | Unregisters a container job after ending. Expects: |

## oJobNet

[Source definition](https://github.com/OpenAF/oJob-common/blob/130addf46fb52ca733da6a66bf7b990430006caf/oJobNet.yaml).

| Job | Description from source help |
| --- | --- |
| `NET Port test` | Tests access to TCP port (the result will be available as a boolean in args.__netPortTest[host][port]: |

## oJobOPack

[Source definition](https://github.com/OpenAF/oJob-common/blob/130addf46fb52ca733da6a66bf7b990430006caf/oJobOPack.yaml).

| Job | Description from source help |
| --- | --- |
| `oPack Pack external` | Packs an external opack given an url or opack name: |

## oJobQueue

[Source definition](https://github.com/OpenAF/oJob-common/blob/130addf46fb52ca733da6a66bf7b990430006caf/oJobQueue.yaml).

| Job | Description from source help |
| --- | --- |
| `oJob Queue Add` | See source definition and its argument checks. |
| `oJob Queue Delete` | See source definition and its argument checks. |
| `oJob Queue Rules` | See source definition and its argument checks. |
| `oJob Queue Manager` | See source definition and its argument checks. |

## oJobRAID

[Source definition](https://github.com/OpenAF/oJob-common/blob/130addf46fb52ca733da6a66bf7b990430006caf/oJobRAID.yaml).

| Job | Description from source help |
| --- | --- |
| `RAID AF` | Executes a RAID AF operation. Expects: |

## oJobRest

[Source definition](https://github.com/OpenAF/oJob-common/blob/130addf46fb52ca733da6a66bf7b990430006caf/oJobRest.yaml).

| Job | Description from source help |
| --- | --- |
| `REST Start Server` | Provides a REST server. The expected arguments are: |
| `REST Apply Service` | See source definition and its argument checks. |
| `REST Stop Server` | See source definition and its argument checks. |
| `REST List Services` | Provides a REST endpoint list for a endpoint prefix (aURI). The expected arguments: |
| `REST Doc Service` | Provides a REST documentation service defintion to display the markdown documentation of an URI. The expected arguments are: |
| `REST Service` | Provides a REST service definition. The expected arguments are: |
| `REST Healthz` | Adds a healthz URI |
| `REST Metrics` | Adds a metrics URI with a OpenMetrics/Prometheus output |
| `REST Add Metric` | Add a metric to the current daemon execution |

## oJobSQL

[Source definition](https://github.com/OpenAF/oJob-common/blob/130addf46fb52ca733da6a66bf7b990430006caf/oJobSQL.yaml).

| Job | Description from source help |
| --- | --- |
| `SQL Result` | Use internally by oJobSQL |
| `SQL` | Executes a DB SQL query. |
| `SQL Batch` | Executes a series of DB SQLs. |
| `SQL RAID` | Executes a RAID SQL query. |

## oJobSSH

[Source definition](https://github.com/OpenAF/oJob-common/blob/130addf46fb52ca733da6a66bf7b990430006caf/oJobSSH.yaml).

| Job | Description from source help |
| --- | --- |
| `SSH Load hosts` | Loads a list of hosts (in YAML) to a channel. The expected arguments are: |
| `SSH Exec` | Executes commands on a SSH connection. The expected arguments are: |
| `SSH Send file` | Sends a file over a SSH connection. The expected arguments are: |
| `SSH Get file` | Gets a file over a SSH connection. The expected arguments are: |

## oJobSVN

[Source definition](https://github.com/OpenAF/oJob-common/blob/130addf46fb52ca733da6a66bf7b990430006caf/oJobSVN.yaml).

| Job | Description from source help |
| --- | --- |
| `SVN checkout` | Will checkout a SVN repository. Expects: |
| `SVN update` | Will update a SVN repository. Expects: |
| `SVN commit` | Will add and commit to SVN repository. Expects: |

## oJobTest

[Source definition](https://github.com/OpenAF/oJob-common/blob/130addf46fb52ca733da6a66bf7b990430006caf/oJobTest.yaml).

| Job | Description from source help |
| --- | --- |
| `oJob Assert` | This job will assert that args.a and args.b provided are equal. Otherwise it will display the args.msg message. |
| `oJob Test` | This job will test an args.func (function) or an args.job provided. The test will use the current oJob job name. Optionally you can specify args.count (defaults to 1) to test more than one time. |
| `oJob Test sh` | This job will test a args.cmd (shell command) provided. The test will use the current oJob job name. |
| `oJob Test Results` | Prints or outputs (if args.quiet = true) a args.results with: count of tests, tests passed, tests failed and all profile information. |
| `oJob Test Todo results` | Prints or outputs (if args.quiet = true) a args.results with: count of tests, tests passed and tests failed. |
| `oJob Generate Markdown` | This job will generate a Markdown with the current test results and optionally logs. |
| `oJob Generate JSON results` | This job will generate a JSON with the current test results and optionally logs. |
| `oJob Test CI summary` | Prints a CI-friendly PASS/FAIL summary and exits with a non-zero code if there are failed tests. |
| `oJob Generate JUnit XML` | This job will generate a JUnit XML with the current test results. |

## oJobWatchDog

[Source definition](https://github.com/OpenAF/oJob-common/blob/130addf46fb52ca733da6a66bf7b990430006caf/oJobWatchDog.yaml).

| Job | Description from source help |
| --- | --- |
| `oJob WatchDog` | Verifies that a process (OpenAF/oJob/etc...) is running. Expects: |

## oJobXLS

[Source definition](https://github.com/OpenAF/oJob-common/blob/130addf46fb52ca733da6a66bf7b990430006caf/oJobXLS.yaml).

| Job | Description from source help |
| --- | --- |
| `oJob XLS Open File` | Opens a XLSx file to use with other oJob XLS jobs. Expects: |
| `oJob XLS Table` | Adds an array of objects as a table on a XLS file sheet. Expects: |
| `oJob XLS Close File` | Closes a XLSx file writing it to the filesystem. Expects: |

## oJobs

[Source definition](https://github.com/OpenAF/oJob-common/blob/130addf46fb52ca733da6a66bf7b990430006caf/oJobs.yaml). Includes: `oJobBasics.yaml`, `oJobCh.yaml`, `oJobDebug.yaml`, `oJobEmail.yaml`, `oJobES.yaml`, `oJobGIT.yaml`, `oJobHBS.yaml`, `oJobHTTPd.yaml`, `oJobIO.yaml`, `oJobNet.yaml`, `oJobOPack.yaml`, `oJobRAID.yaml`, `oJobRest.yaml`, `oJobSQL.yaml`, `oJobSSH.yaml`, `oJobSVN.yaml`, `oJobTest.yaml`, `oJobWatchDog.yaml`, `oJobXLS.yaml`.
{% endraw %}
