---
layout: default
title: oJob
parent: Concepts
grand_parent: OpenAF docs
---
# oJob

oJob is an automated OpenAF job executor. It basically tries to modularize and organize script processing hiding most of the complexity of handling execution dependencies, parallel processing, running scripts as daemons, remote coordinated job execution, reusable modules for multiple targets, etc.

A oJob is mainly defined by a YAML file (although it can also be defined in JSON) that looks like a shopping list:

````yaml
jobs:
   - name: Get eggs
   - name: Get sugar
   - name: Get flour
   
   - name: Make cake
     deps:
       - Get eggs
       - Get sugar
       - Get flour

todo:
   - Get eggs
   - Get sugar
   - Get flour
   - Make cake
````

From this yaml file oJob already understands that we need to somehow get eggs, sugar and floor (even in parallel if possible) in order to be ready to prepare a cake.

So basically you have a jobs section that defines each job (for the sake of simplicity of the example we didn't define how to execute each job) and if they have dependencies to start. Then you have a to do section that defines, by order, what needs to happen.

To run it you would just execute:
````bash
ojob myrecipe.yaml
````

## Embeeded documentation for an oJob

Starting with OpenAF v20250721 the `ojob` CLI can render the oJob documentation directly. Two new options are available:

* `ojob -reference` renders a human-friendly overview of jobs, arguments and dependencies using the standard console output (with colours when supported).
* `ojob -mdreference` emits the same reference in Markdown.


In the next chapters will go through how you can add arguments to each job (e.g. how many eggs, how much sugar, …), how you can have jobs chains (e.g. job “Get ingredients” → “Make cake” → “Serve cake” for just a to do “Make cake”), how you can make a production line of cakes with array arguments and more.

# Jobs

A job is simple module unit in oJob, identified by an unique name that can be plug in different ways to reach the end goal. As input they accept arguments, as output they execute the actions you define:

````yaml
jobs:
   - name: Say hello
     exec: >
       print("Hello " + args.who);
       
todo:
   - name: Say hello
     args: 
       who: world
````

As you can see on the example above, the todo list can also contain arguments for a job. And inside a job you have the “args” map available with the args provide in the todo.

Each job definition has the following possible entries:

| Entry | Type | Mandatory? | Description |
|-------|------|------------|-------------|
| name  | _string_ | _yes_ | _The **unique name** of the job._ |
| args  | _map/array_ | _no_ | _A map of arguments to be used by the job. It will be available on openaf code as a "args" map. If instead of a map is defined as an array it will execute the job for each array entry that will represent each job execution map of arguments._ |
| exec  | _string_ | _no_ | _OpenAF code that gets executed for this job. If it throws an exception the job will fail otherwise it will be considered successful._ |
| deps  | _array_ | _no_ | _An array of job dependencies where you refer other jobs by their unique name or a map with the following entries: name, onSuccess, onFail. The onSuccess and onFail can be used to define OpenAF code to execute on the success or failure of the job dependency executions. If the code returns true it will be consider as a satisfied dependency allowing the current job definition to execute, if false it will be consider that the current job definition can't be executed. Additionally theses functions can access the current "args", "job" map and run "id"._ |
| type  | _string_ | _no_ | _The oJob type. By default they are of type "single". But you can specify other types of jobs like shutdown, periodic and "jobs". See more on the job types sub-chapter._ |
| typeArgs | _map_ | _no_ | _A map of arguments to be provided for each job type. Common to all is the typeArg 'single' which tries to force the job to run in a single thread if args is an array. See more on the job types sub-chapter._ |
| from  | _string/array_ | _no_ | _The name of a job (or ordered list) whose execution will be prefixed (like a document header) with the current job execution (e.g. if you want all job executions to execute another job initially)._ |
| to    | _string/array_ | _no_ | _The name of a job (or ordered list) whose execution will be suffixed (like a document footer) with the current job execution (e.g. if you want all job executions to execute another job when they end)._ | 
| help  | _string_ | _no_ | _A help text to be presented whenever you execute "ojob -jobhelp 'My job'"_ |
| lang  | _string_ | _no_ | _The executing language for the "exec" entry. By default languages 'js' (default), 'python' and 'shell' can be used but custom languages can be added using the ojob.langs entry or the typeArgs.langs entry. For 'js' and 'python' job arguments will be available in the "args" variable for other shell based languages job arguments will be converted to environment variables._ |
| catch | _string_ | _no_ | _Code for a try/catch function that will get executed if the main job execution code throws an exception. Receives, as parameters: "args", "job", "id", "deps" and the "exception"._ |
| help | _map_ | _no_ | _Provides a help message to be used with the help option, as a string, or the oJob help (on a job named "Help" with a "text" string field, an array "expects" field where each entry should be a "name" string, a "desc" string and an "example" string._ |
| each | _string_ | _no_ | _Can be a string or an array representing other jobs names that will be called whenever the function "each" is used inside the main execution code providing a map (each function will receive the map as args). See the help for $doA2B for more._ |
| lang | _string_ | _no_ | _Convinient string or map shortcut to job's generic typeArgs langs_ |

## Job types

The most used type of job is "simple". All job types, including "simple" have the following typeArgs:

| typeArgs entry | Type | Mandatory? | Description |
|----------------|------|------------|-------------|
| timeout | _number_ | _no_ | _The time interval, in milliseconds, for the entire job execution or between stopWhen function executions. If no stopWhen function is provided and the timeout time is exceeded the job will fail indicating that it exceed the timeout. _ |
| stopWhen | _string_ | _no_ | _Function string that will be evaluated continuously or every timeout time interval. If the function returns true the current job execution will be terminated._ |
| langs | _map_ | _no_ | _String with language or Map with lang (language name) and shell (language shell command) to be used as the executing language for the "exec" entry. Job arguments will be available as environment variables. Optionally using "langFn" the execution code to handle will be provided as the variable "code"._ |
| execJs | _String_ | _no_ | _Reads the OpenAF javascript execution code from an external filepath._ |
| execRequire | _String_ | _no_ | _Loads an external filepath OpenAF javascript execution code file where the function with the job name will be executed with the current args._ |
| execPy | _String_ | _no_ | _Reads a Python execution code from an external filepath._ |
| file | _String_ | _no_ | _Reads the execution code from an external filepath._ |
| lock | _String_ | _no_ | _Specifies a lock name to ensure a job execution is not concurrent._ |
| lockCh | _String_| _no_ | _Specifies the lock channel to use (defaults to simple "oJob::locks")_ |

Then for other types there are specific typeArgs available:

### periodic

This job when included on a todo list will execute on a separate thread the job periodically until the ojob ends or it's stopped (if ojob.daemon is set to true). You can optionally provide a cron like expression time. To set this you can provide as typeArgs:

| typeArgs entry | Type | Mandatory? | Description |
|----------------|------|------------|-------------|
| timeInterval | _number_ | _no_ |  _The time interval in milliseconds between each job execution periodic execution._ |
| cron | _string_ | _no_ | _If defined, a minutes-based (e.g. * * * * *) or seconds-based (e.g. * * * * * *) cron-like expression to indicate if the job should run between. This cron expression will be checked for on the start of each timeInterval if defined otherwise a single thread will wait for the next scheduled cron event._ |
| cronCheck | _map_ | _no_ | _If defined, creates a channel based tracking to eventually persist if this job definition has executed or not within the provided cron expression (for example: if it was supposed to run every hour but once restart didn't run for 2 hours it will automatically try to execute the job). The map should be composed of: active (boolean); ch (string), indicating the channel to be used (defaults to oJob::cron); retries (number), the number of retries if the job execution fails; cron (string), a different cron expression to determin if an execution is missing or not._ |
| waitForFinish | _boolean_ | _no_ | _If defined and set to true the timeInterval is considered from the end of execution (even if bigger than the defined timeInterval). Thus preventing more than one concurrent execution to occur. If not defined or set to false the timeInterval is considered from the beginning of execution. So even if the first execution didn't end and second will start if the timeInterval has reach it's end._ |

Example:

````yaml
ojob:
   daemon: true

jobs:
   # Say the time regularly
   - name         : Say the time
     type         : periodic
     typeArgs     :
        waitForFinish: false
        cron         : "*/5 * * * * *"
     exec         : >
        print(new Date());

todo:
   - Say the time
````

### subscribe

This job type will execute whenever a set/setAll/unSet operation occurs in a channel (OpenAF channel subscriber). The job execution will have access to the operation, key(s) and value(s) affected.

Example:

````yaml
jobs:
   - name    : Print stuff
     type    : subscribe
     typeArgs:
        chSubscribe: myChannel
     exec    : |
        sprint(args);
        // args.ch - channel name
        // args.op - operation (set/unset/setall)
        // args.k - the key (set/unset) or key fields to use (setall)
        // args.v - the value (set/unset) or array of values (setall)

todo: 
   - Print stuff
````

| typeArgs entry | Type | Mandatory? | Description |
|----------------|------|------------|-------------|
| chSubscribe | String | Yes | The channel name to subscribe for changes. |

### shutdown

This is equivalent to single but it will only be triggered on the end of the oJob script or if a shutdown signal is received. It's ideal use is closing open connections, saving data before a crash, etc... It has no typeArgs available.

Example:

````yaml
jobs:
   - name: Do stuff
     exec: >
       print("I'm doing stuff...");
       // connectionStart()
   
   - name: Close
     type: shutdown
     exec: >
       print("I'm going to die now... bye!");
       // connectionClose()
       
todo:
   
   - Close
   - Do stuff
````

_Why isn't there a “startup” type? That's because you control what runs first in the todo list and with job dependencies or you can use the sequence mode (see oJob settings)._

### jobs

"The mother of all jobs" in the sense that will execute any other provided ojob yaml file with it's jobs and todo. The arguments received by this job will be passed through as arguments all jobs in the ojob yaml file. It has one typeArgs: file. This argument is the file path to the other ojob yaml file.

````yaml
jobs:
   - name    : Do stuff for a date
     type    : jobs
     typeArgs:
        file: lotsOfStuff.yaml
     args    :
        dateToProcess: 20170101
   
   - name    : Done
     deps    :
        - Do stuff for a date
     exec    : >
       print("Finally... everything is done.");
       
todo:
   - Do stuff for a date
   - Done
````

# Todo

This is where you define the list of what needs to be done (e.g. to do). Let's consider the example: 

````yaml
jobs:
   - name: Get eggs
   - name: Get sugar
   - name: Get floor
   
   - name: Make cake
     deps:
       - Get eggs
       - Get sugar
       - Get floor

todo:
   - Get eggs
   - Get sugar
   - Get floor
   - Make cake
````

oJob will try to "Get eggs", "Get sugar", "Get floor" and "Make cake" in parallel. Since "Make cake" depends on the success of "Get eggs", "Get sugar", "Get floor" it won't start until all of them end successfully. This behavior can be changed by the ojob.sequential = true where oJob will honor the order of the todo list and execute subsequent job only when the previous and ended it's execution (but this doesn't disable the job dependencies check).

But each job execution might require different arguments. In this case, different quantities. So on "todo" you can specify arguments to execute each job:

````yaml
todo:
   - name: Get eggs
     args:
        howMany: 2
        size   : L

   - name: Get sugar
     args:
        cups: 1.5

   - Get floor
   - Make cake
```` 

If you instead of a map you provide a list/array then the job will be execute with each list of arguments provided on the list:

````yaml
todo:
   - name: Get eggs
     args:
        howMany: 8
        size   : L

   - name: Get sugar
     args:
        cups: 5

   - Get floor

   - name: Make cake
     args:
        - name           : Chocolate cake
          typeOfChocolate: milk
        - name           : Dark chocolate cake
          typeOfChocolate: dark
````

# Include

This is where you can include other ojob files with more job definitions. This allows for having modular ojob files with different type of jobs. It's basically an array/list of file paths. The files will be searched on the current path and on the installed oPacks. So if you install [oJob-common](https://github.com/OpenAF/oJob-common), for example, you can include existing job definitions in other ojob files:

````yaml
include:
   - oJobSSH.yaml

jobs:
   - name: print remote cpuinfo
     to  : SSH Exec
     args:
       host : some.host
       login: mylogin
       pass : mypassword
       cmd  : >
          cat /proc/cpuinfo

todo:
  - print remote cpuinfo
````

# oJob

This is where you set specific settings on how the ojob should run. Here is a set of list of possible entries per category:

## Logging

Funcitonality to control OpenAF and oJob logging:

| Entry | Type | Description |
|-------|------|-------------|
| logToFile | _map_ | _Map with the same options as ow.ch.utils.setLogToFile_ |
| log | _map_ | _Map with the same options as setLog_ |
| recordLog | _boolean_ | _Determines if it should use startLog to log into the \_\_log channel._ |
| logArgs | _boolean_ | _If true the arguments provided to each job execution will be logged (defaults to false)._ |
| logToConsole | _boolean_ | _If false ojob logging won't be output to the console (defaults to true)._ |
| logLimit | _number_ | _The number of internal execution logs per job that should be kept (default to 100)._ |
| logJobs | _boolean_ | _If false no job start, end or error will be logged. (default to true)._ |
| metrics | _map_ | _Can be a boolean to indicate that metrics should be collected or a map with the metrics channel "chName" and "period" for collecting (see more in ow.metrics.startCollecting). Optionally custom metric functions can be added with a "add" map where each represents the metric name and the value the corresponding function code (see more in ow.metrics.add help)_ |

## Execution control

Functionality to control oJob's job execution:

| Entry | Type | Description |
|-------|------|-------------|
| unique | _map_ | _Map to ensure that only one instance of ojob runs. The map can define a pidFile (defaults to ojob.pid and will be evaluated as code) and killPrevious (defaults to false)._ |
| sequential | _boolean_ | _If true each todo entry will be executed only when the previous has ended it's execution. Otherwise it will try to execute in parallel._ |
| daemon | _boolean_ | _If true the ojob will behave like a daemon. It will only exit if the process is killed or if executed with the arguments stop, forcestop or restart._ | 
| numThreads | _number_ | _Force the maximum number of threads to use. If not defined it will try to automatically assess an ideal number of threads to use._ |
| async | _boolean_ | _Runs all jobs asynchronously (defaults to false)_ | 
| depsTimeout | _number_ | _If defined establishes a maximum time interval, in ms, that each job will wait for the corresponding job dependencies to be fullfilled. If the time is exceeded the corresponding job will fail._ |
| checkStall | _map_ | _Checks if job execution is stalled "everySeconds" (defaults to every 60 seconds) by executing "checkFunc" (stops oJob if returns true) or "killAfterSeconds" seconds have pass since startup._ |
| tags | _array_ | _An array of string tags to easily identify this oJob among others._ |

**Note**: Use _sequential = true_ and _numThreads = 1_ for a total sequential execution. Keep in mind that if _numThreads_ is not defined or greater than 1 multiple job executions can still occur despite _sequential = true_ (for example when the job args is an array). The sequential parameter will just ensure that jobs listed in the todo list are executed in the order of the todo list instead of being launched all in parallel.

## Languages support

Functionality related with language support:

| Entry | Type | Description |
|-------|------|-------------|
| langs | _array_ | _List of maps with two entries: lang (a name) and shell (the command to execute). If the job has the "lang" entry it will invoke the "shell" command to execute the "exec" entry. Job arguments will be passed as environment variables. Optionally using "langFn" the execution code to handle will be provided as the variable "code"._ |

## OpenAF functionality

Functionality related with OpenAF:

| Entry  | Type | Description |
|--------|------|-------------|
| opacks | _array_ | _Array of oPacks needed for the oJob execution (if possible, it will try to install the corresponding oPack if not available). If the array entry is a map it's possible to provide a version rule string value (e.g. &gt;= 20200101)_ |
| loadLibs | _array_ | _Array of OpenAF javascript libs to preload (equivalent to "loadLib")_ |
| loads | _array_ | _Array of OpenAF javascript to preload (equivalent to "load")_ |
| argsFromEnvs | _boolean_ | _If true all the current environment variables will be converted into entries in the args map._ |

## Channels

This is actually a map to define the channel use in the ojob:

| Entry | Type | Description |
|-------|------|-------------|
| expose | _boolean_ | _Determines if channels should be exposed externally._ | 
| port | _number_ | _If expose = true then defines the host port to use to expose channels._ |
| host | _string_ | _If expose = true then defines the network interface on which to expose channels._ |
| keyStorePath | _string_ | _If expose = true then defines where SSL keys are stored to use HTTPS._ |
| keyPassword | _string_ | _If expose = true and a keyStorePath was defined, defines the password to use to open the corresponding key store._ | 
| permissions | _string_ | _General permissions for anonymous access (r = read, w = write). Defaults to "r"._ |
| list | _array_ | _If expose = true specifies which channels should be exposed (default is all)._ |
| auth | _array_ | _Array of maps to provide http authentication when accessing channels. Each map should have a login, a pass and permissions._ |
| create | _array_ | _An array of maps containing the channel "type", the "compress" create option and the given necessary "options"._ |
| peers | _array_ | _Establishes peer relationships for all the "list" channels (requires port to be defined) with the provided url array list (the uri expected should included the channel name)._ |
| clusters | _map_ | _Setups an OpenAF cluster with the provided name, checkPeriod, host, port, nodeTimeoutm numberOfTries, tryTimeout and discovery map entries._ |

## Advanced preprocessing 

| Entry | Type | Description |
|-------|------|-------------|
| conAnsi | _boolean_ | _Advanced option to turn off ansi characters use._ |
| conWidth | _number_ | _Advanced option to override screen size detection._ |

# init

For organization proposes if a init entry is used all mapped values will be available during oJob execution in _args.init_ map entry.

# oJob command-line

To execute a ojob you can simple execute:

````bash
ojob myrecipe.yaml
````

You can add arguments that will be available to all jobs in the file as arguments:

````bash
ojob myrecipe.yaml typeOfChocolate=dark nameOfCake=My\ dark\ cake
````

You can also use the following extra options:

| Option | Description |
|--------|-------------|
| -compile | Processes all includes and the current file to produce a single YAML output. |
| -tojson | Processes all includes and the current file to produce a single JSON output. Useful to debug any YAML parsing issues. |
| -jobs | List all the jobs available including the ones defined in includes. |
| -todo | List the final todo list after processing all includes and the current file. | 
| -deps | Tries to provide a human readable representation of the dependencies between all jobs in includes and on the current file. |
| -jobhelp | Display any available help information for a job. Can include extra help of jobs defined in "from" an "to". Example: "ojob example.yaml -jobhelp oJob sh" |
| -nocolor | Removes all processing to determine screen size and use ansi colors. |
