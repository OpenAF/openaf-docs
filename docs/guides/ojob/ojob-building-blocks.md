---
layout: default
title: oJob building blocks
parent: oJob
grand_parent: Guides
---

# oJob building blocks

To enrich the oJob building blocks there is a set of jobs to help minimize coding (low-code). OpenAF provides these built-in jobs through __ojob.yaml__ (`includeOJob: true`). The separate [oJob-common package](ojob-common-modules.md) supplies reusable modules such as `oJobBasics.yaml` and `oJobHTTPd.yaml`.

## What's provided

| Area | Job | Description |
|------|-----|-------------|
| Control | [ojob if](#ojob-if) | If the provided "condition" is evaluated as true it will execute the "then" jobs otherwise it will execute the "else" jobs. |
| Control | [ojob repeat](#ojob-repeat) | Repeats sequentially, for a specific number of "times", the provided list of "jobs" (one or more). |
| Control | [ojob repeat with each](#ojob-repeat-with-each) | Repeats the configured "jobs" (one or more jobs) sequentially for each element of the provided "key" list. |
| Debug | [ojob debug](#ojob-debug) | Outputs the current args and res values to help debug an ojob flow. |
| Debug | [ojob job debug](#ojob-job-debug) | Provides an alternative to print based debug. |
| Channel | [ojob channel](#channel) | Provides a set of operations over an OpenAF channel. |
| Function | [ojob function](#ojob-function) | Executes the provided function mapping any args to the function arguments using the odoc help available for the provided function. |
| Input | [ojob get](#ojob-get) | Retrieves a specific map key (or path) using $get. |
| Input | [ojob file get](#ojob-file-get) | Retrieves a specific map key (or path) from an YAML or JSON file provided. |
| Input | [ojob split to items](#ojob-split-to-items) | Splits an args source into an array of maps. |
| Query | [ojob query](#ojob-query) | Performs a query (using ow.obj.filter) to the existing args. |
| Options | [ojob job](#ojob-job) | Provides a way to organize idempotent jobs. |
| Options | [ojob job report](#ojob-job-report) | Outputs a job jobs report (e.g. job name, action and plan). |
| Options | [ojob job final report](#ojob-job-final-report) | Outputs a job jobs report (e.g. job name, action and plan) upon ojob termination. |
| Options | [ojob options](#ojob-options) | Adds new "todo" entries depending on the value of a provided args variable. |
| Options | [ojob todo](#ojob-todo) | Adds new "todo" entries. |
| Output | [ojob set](#ojob-set) | Sets a "key" with the current value on a "path" using $set. |
| Output | [ojob set envs](#ojob-set-envs) | Sets job args based on environment variables. |
| Output | [ojob print](#ojob-print) | Prints a message line given an OpenAF template. |
| Output | [ojob log](#ojob-log) | Logs a message line given an OpenAF template. |
| Output | [ojob find/replace](#ojob-findreplace) | Performs an in-memory find/replace on a provided string or file and outputs to args.output or, optionally, to a file. |
| Output | [ojob output](#ojob-output) | Prints the current arguments to the console. |
| Template | [ojob template](#ojob-template) | Applies the OpenAF template over the provided data producing an output. |
| Template | [ojob template folder](#ojob-template-folder) | Given a templateFolder it will execute 'ojob template' for each (recursively), with the provided data, to output to outputFolder. |
| Report | [ojob report](#ojob-report) | Outputs a jobs report (e.g. job name, status, number of executions, total time, avg time and last execution). |
| Report | [ojob final report](#ojob-final-report) | Outputs a jobs report (e.g. job name, status, number of executions, total time, avg time and last execution) upon ojob termination. |
| Security | [ojob sec get](#ojob-sec-get) | This job will get a SBucket secret and map it to oJob's args. |
| State | [ojob state](#ojob-state) | Changes the current state depending on the value of a provided args variable. |
| State | [ojob get state](#ojob-get-state) | Gets the current state into args.state. |
| State | [ojob set state](#ojob-set-state) | Changes the current state. |
| AI    | [ojob llm](llm-shortcut) | Enable interaction with LLM (Large Language Models) AI models. |

## How to start using it

You can include it in different ways depending on the OpenAF version you are using.

For OpenAF version >= 20230103:

````yaml
ojob:
  includeOJob: true
````

For older OpenAF versions

````yaml
ojob:
  opacks:
    oJob-common: 20230103

include:
- ojob.yaml
````

or (requiring internet access)

````yaml
include:
- ojob.io/common/ojob
````

## Control

### ojob if

If the provided "condition" is evaluated as true it will execute the "then" jobs otherwise it will execute the "else" jobs

__Expects:__

| name | required? | description |
|------|-----------|-------------|
|__condition|no|An OpenAF code condition with templating functionality|
|__then|no|One job or a list of jobs to execute if the "condition" is true|
|__else|no|One job or a list of jobs to execute if the "condition" is false|
|__debug|no|Boolean to indicate if should log the original condition and the parsed condition for debug proposes|


### ojob repeat

Repeats sequentially, for a specific number of "times", the provided list of "jobs" (one or more)

__Expects:__

| name | required? | description |
|------|-----------|-------------|
|__times|no|The number of times to repeat the provided list of jobs|
|__jobs|no|One job or a list of jobs to execute each time|

### ojob repeat with each

Repeats the configured "jobs" (one or more jobs) sequentially for each element of the provided "key" list.

__Expects:__

| name | required? | description |
|------|-----------|-------------|
|__key|no|The key or path for an existing list in args|
|__jobs|no|One job or a list of jobs to execute each time|

## Debug

### ojob debug

Outputs the current args and res values to help debug an ojob flow.

### ojob job debug

Provides an alternative to print based debug.

Example:

````yaml
  # ----------------
  - name: Sample job
    exec: |
      //@ Declaring array
      var ar = [ 0, 1, 2, 3, 4, 5 ]

      //@ Start cycle
      var ii = 0;
      while(ii < ar.length) {
        print("II = " + ii)
        ii++
        //# ii == 3
      }
      //@ End cycle
      //? ii

      //?s args
      //?y args
````

__Expects:__

| name | required? | description |
|------|-----------|-------------|
|job|no|The job to change to include debug|
|jobs|no|The jobs array to change to include debug|
|lineColor|no|The line color around the debug info|
|textColor|no|The text color around the debug info|
|theme|no|The withSideLineThemes theme to use|
|emoticons|no|If emoticons should be used or not|
|signs|no|A custom map of emoticons (keys: checkpoint, assert and print)|
|includeTime|no|A boolean value to indicate if a time indication should be included|

## Channel

Provides a set of operations over an OpenAF channel.

__Expects:__

| name | required? | description |
|------|-----------|-------------|
| __name | yes | The name of the OpenAF channel to use |
| __op   | yes | The operation to perform (e.g. setall, set, get, unset, unsetall, getkeys, getall and size) |
| __key  | no  | The key from where to retrieve the operation arguments (args to retrive from arguments) |
| __kpath | no | If defined, the path over the values retrieved from __key where the key or keys of the operation are defined |
| key | no | If defined, the key to use with the operations set, get and unset |
| keys | no | If defined, the set of fields to use with the operations setall and unsetall |
| value | no | If defined, the value to use with the operations set, get and unset |
| values | no | If defined, an array of values to use with the operations setall and unsetall |
| __vpath | no | If defined, the path over the values retrieved from __key where the value or values of the operation are defined |
| extra | no | If defined, will provide an extra argument (usually a map), depending on channel type, for the getall and getkeys operations. |

__Returns:__

| name | description |
|------|-------------|
| _list | If __key == 'args' will return the results of getall and getkeys |
| _map | If __key == 'args' will return the results of get |
| size | If __key == 'args' will return the size of the channel |

## Function

### ojob function

Executes the provided function mapping any args to the function arguments using the odoc help available for the provided function.
Note: accessing odoc might be slow on a first execution.

__Expects:__

| name | required? | description |
|------|-----------|-------------|
|__key|yes|The key string to retrieve previous results (defaults to 'res')|
|__fn|no|The function to execute|
|__path|no|If defined the args path for the function arguments to consider|
|__fnPath|no|If defined the args path where to set the function result|

## Input

### ojob get

Retrieves a specific map key (or path) using $get

__Expects:__

| name | required? | description |
|------|-----------|-------------|
|__key|no|Map key or path (key is also checked for compatibility)|

### ojob file get

Retrieves a specific map key (or path) from an YAML or JSON file provided.

__Expects:__

| name | required? | description |
|------|-----------|-------------|
|__file|yes|The file path to an YAML or JSON file|
|__key|no|Map key or path on the file contents|
|__cache|no|Boolean value that if false it won't cache the file contents (default: true)|
|__ttl|no|If cache is enabled lets you define a numeric ttl|
|__out|no|The path on args to set the map key/path contents|

### ojob split to items

Splits an args source into an array of maps (_list).

Example:

````
  a source string with the value "abc, xyz, 1"
  + separator = ','
  transforms into:

  - item: abc
  - item: xyz
  - item: 1
````

__Expects:__

| name | required? | description |
|------|-----------|-------------|
|source|no|A object path to the string source to split|
|separator|no|The separator for the source string (defaults to \n)|

## Query

### ojob query

Performs a query (using ow.obj.filter) to the existing args.

__Expects:__

| name | required? | description |
|------|-----------|-------------|
|__query|no|The query map for ow.obj.filter|
|__from|no|The path to the args key to perform the query|
|__to|no|The path to where the results should be stores|
|__key|no|If __from and __to not provided defaults to $get/$set on the provided key|

## Options

### ojob job

Provides a way to organize idempotent jobs. One or more "checks" jobs will be called to determine an args._action.
Initially the args._action is set to "none". If the "checks" jobs determine an action it will call the corresponding
jobs on "actions" jobs. If "_go=true" is not provided, instead of running, it will only return a plan of actions.
For example:

````yaml
  - name: Write Hello World
    to  : ojob job
    args:
      _checks : Check Hello World
      _actions:
        create   : Create Hello World
        overwrite: Overwrite Hello World
        delete   : Delete Hello World
````

__Expects:__

| name | required? | description |
|------|-----------|-------------|
|_checks|no|A list of one or more jobs to be called to perform checks to determine an args._action|
|_actions|no|A map of possible values of args._action whose values are one or more jobs to execute|
|_go|no|A boolean value (defaults to false) that controls if the _actions jobs are called (when true) or not|

### ojob job report

Outputs a job jobs report (e.g. job name, action and plan)

__Expects:__

| name | required? | description |
|------|-----------|-------------|
|__format|no|Can be json, yaml, table (default) or any other ow.oJob.output format|

### ojob job final report

Outputs a job jobs report (e.g. job name, action and plan) upon ojob termination

__Expects:__

| name | required? | description |
|------|-----------|-------------|
|__format|no|Can be json, yaml, table (default) or any other ow.oJob.output format|

### ojob options

Adds new "todo" entries depending on the value of a provided args variable.

Example:

````yaml
  __optionOn : mode
  __lowerCase: true
  __todos    :
    mode1:
    - Job 1
    - Job 2
    mode2:
    - Job 2
    - Job 3
  __default:
  - Job 2
````

__Expects:__

| name | required? | description |
|------|-----------|-------------|
|__optionOn|yes|The variable in args that will define which set of "todo"s will be added (trimmed)|
|__lowerCase|no|Boolean value to determine if should compare the optionOn in lower case (defaults to false)|
|__upperCase|no|Boolean value to determine if should compare the optionOn in upper case (defaults to false)|
|__todos|yes|Map where each option value should have a list/array of "todo"s|
|__default|no|Default array of "todo"s|
|__async|no|Boolean value that if true, run the todos in async mode|

### ojob todo

Executes an ojob sub-todo.

_NOTE: doesn't perform any checks for recursive behaviour!_

| name | required? | description |
|------|-----------|-------------|
| todo | no | A string or array of todo' maps |
| todo[].name | no | Name of the job to execute |
| todo[].args | no | Arguments to merge (if isolateArgs is not true) with the main job arguments |
| todo[].isolateArgs | no | Boolean to indicate, for a specific todo, that args should be isolated from all others |
| todo[].isolateJob | no | Boolean to indicate, for a specific todo, that the job should run in a different scope (e.g. deps will not work) |
| todo[].templateArgs | no | Boolean to indicate, for a specific todo, to apply template to each string of the provided args (use only if typeArgs.noTemplateArgs = false OR job.templateArgs = true) |
| isolateArgs | no | Boolean, false by default, to indicate that args should be isolated from all others |
| isolateJob | no | Boolean, false by default, to indicate that the job should run in a different scope (e.g. deps will not work) |
| templateArgs | no | Boolean, true by default, to indicate to apply template to each string of the provided args (use only if typeArgs.noTemplateArgs = false OR job.templateArgs = true) |
| shareArgs | no | Boolean, false by default, to indicate that args should be shared between all todo's jobs sequentially. |
| __debug | no | Boolean to indicate that each job execution parameters should be printed before executing |

## Output

### ojob set

Sets a "key" with the current value on a "path" using $set

__Expects:__

| name | required? | description |
|------|-----------|-------------|
|__key|no|Map key|
|__path|no|A key or path to a value from the current args|

### ojob set envs

Sets job args based on environment variables.

__Expects:__

| name | required? | description |
|------|-----------|-------------|
|envs|no|A map where each key corresponds to an environment variable and the value to the args path where it should be placed|

### ojob print

Prints a message line given an OpenAF template

__Expects:__

| name | required? | description |
|------|-----------|-------------|
|__key|no|Map key to retrieve ('args' for arguments)|
|__path|no|The path to consider from the __key|
|msg|yes|The message template to use|
|level|no|The level of the message (info (default) or error)|

### ojob log

Logs a message line given an OpenAF template

__Expects:__

| name | required? | description |
|------|-----------|-------------|
|__key|no|Map key to retrieve ('args' for arguments)|
|__path|no|The path to consider from the __key|
|msg|yes|The message template to use|
|level|no|The level of the message (info (default), warn or error)|
|options|no|Extra options to provide to the tlog* functions. See more in the help of tlog, tlogErr and tlogWarn.|

### ojob output

Prints the current arguments to the console.

__Expects:__

| name | required? | description |
|------|-----------|-------------|
|__key|no|The key string to retrieve previous results (defaults to 'res')|
|__path|no|A path string to a map/array over the results set on key.|
|__format|no|The output format (e.g. see ow.oJob.output help)|
|__title|no|Encapsulates the output map/array with a title key.|
|__internal|no|Boolean value that if true it will display the internal oJob entries on the arguments (default false)|

### ojob find/replace

Performs an in-memory find/replace on a provided string or file and outputs to args.output or, optionally, to a file.

__Expects:__

| name | required? | description |
|------|-----------|-------------|
| __key | no | The key that holds template and/or data (default to 'res'). If 'args' it will use the current arguments. |
| __path | no | The path in __key where a map of replacements ([text/regexp]:[replace text]) can be found. |
| inputKey | no | If defined, indicates the key that holds the string of data to replace. |
| inputPath | no | If defined with inputKey, indicates the path to use to select the string of data to replace. |
| inputFile | no | If defined the contents to be replaced will be read from the inputFile. |
| outputFile | no | If defined will output of the content replacement to the defined file. |
| useRegExp | no | Boolean value to determine if the map of replacements will be interpreted as a regexp or text. |
| logJob | no | Optionally provide a logging job with the current args and __op with 'read' or 'write' |

__Returns:__

| name | description |
|------|-------------|
| output | If outputFile is not defined the output will contain the content replacement |

## Report

### ojob report

Outputs a jobs report (e.g. job name, status, number of executions, total time, avg time and last execution)

__Expects:__

| name | required? | description |
|------|-----------|-------------|
|__format|no|Can be json, yaml, table (default) or any other ow.oJob.output format|

### ojob final report

Outputs a jobs report (e.g. job name, status, number of executions, total time, avg time and last execution) upon ojob termination

__Expects:__

| name | required? | description |
|------|-----------|-------------|
|__format|no|Can be json, yaml, table (default) or any other ow.oJob.output format|

## Template

### ojob template

Applies the OpenAF template over the provided data producing an output.

__Expects:__

| name | required? | description |
|------|-----------|-------------|
|__key|no|The key that holds template and/or data (default to 'res'). If 'args' it will use the current arguments.|
|__tpath|no|The path in __key where a string with the template can be found.|
|__dpath|no|The path in __key where a map/array data to use can be found.|
|__out|no|The output will be stored into the provided key (defaults to 'res')|
|template|no|If defined, will be used as template|
|templateFile|no|If defined, it will use the provided template file.|
|data|no|If defined, will be used as data|
|dataFile|no|If defined, it will use the provided data file (either yaml or json).|
|outputFile|no|If defined, the output will be written to the provided file path.|

__Returns:__

| name | required? | description |
|------|-----------|-------------|
|output|no|If no outputFile is provided this will hold the output of applying the template with the provided data|

### ojob template folder

Given a templateFolder it will execute 'ojob template' for each (recursively), with the provided data, to output to outputFolder. Optionally metaTemplate can be use where each json/yaml file in templateFolder all or part of the arguments for 'ojob template'.


__Expects:__

| name | required? | description |
|------|-----------|-------------|
|templateFolder|yes|The original folder where the templates are located.|
|__templatePath|no|If defined, will apply a $path string over the recursive list of files in templateFolder.|
|outputFolder|yes|The path where the output should be stored.|
|data|no|If defined, will be used as data|
|dataFile|no|If defined, it will use the provided data file (either yaml or json).|
|__key|no|The key that holds template and/or data (default to 'res'). If 'args' it will use the current arguments.|
|__dpath|no|The path in __key where a map/array data to use can be found.|
|logJob|no|A ojob job to log the 'ojob template' activity (receives the same arguments as 'ojob template')|
|metaTemplate|no|Boolean that if 'true' will interpret any json/yaml file, in the templateFolder, as a map/array of arguments to use when calling 'ojob template' overriden the defaults.|

## Security

### ojob sec get

This job will get a SBucket secret and map it to oJob's args

__Expects:__

| name | required? | description |
|------|-----------|-------------|
|secIn|no|The args path where all the remaining sec arguments should be read from (defaults to no path)|
|[secIn].secOut|no|The args path to be mapped with the secret (defaults to secIn)|
|[secIn].secKey|no|The SBucket key|
|[secIn].secRepo|no|The SBucket repository|
|[secIn].secBucket|no|The SBucket name|
|[secIn].secPass|no|The SBucket password|
|[secIn].secMainPass|no|The SBucket repository password|
|[secIn].secFile|no|Optional provide a specific sbucket file|
|[secIn].secDontAsk|no|Determine if passwords should be asked from the user (default=false)|
|[secIn].secIgnore|no|If true will ignore errors of sec parameters not being provided (default=false)|

__Returns:__

| name | required? | description |
|------|-----------|-------------|
|[secIn].[secOut]|no|The args path to be mapped with the secret (defaults to secIn)|

## State

### ojob state

Changes the current state depending on the value of a provided args variable.

Example:

````yaml
    stateOn  : mode
    lowerCase: true
    default  : Help
````

__Expects:__

| name | required? | description |
|------|-----------|-------------|
|stateOn|no|The variable in args that will define the current global set (to execute todo.when)|
|lowerCase|no|A boolean value to determine if should compare the stateOn in lower case (defaults to false)|
|upperCase|no|A boolean value to determine if should compare the stateOn in upper case (defaults to false)|
|validStates|no|An array of valid states to change to. If not included the default will be choosen (or none).|
|default|no|Default value of state|

### ojob get state

Gets the current state into args.state.

__Returns:__

| name | required? | description |
|------|-----------|-------------|
|state|no|The current state|

### ojob set state

Changes the current state.

__Expects:__

| name | required? | description |
|------|-----------|-------------|
|__state|no|The state to change to (to execute todo.when)|
