---
layout: default
title: ow.oJob
parent: Reference
grand_parent: OpenAF docs
---

{% raw %}
## ow.oJob

[Source: `06414cd9`](https://github.com/OpenAF/openaf/blob/06414cd9204e918daa1e2971ce904783299db333/js/owrap.oJob.js) · [Baseline](../source-snapshot.md)

### oJob.__addLog

`oJob.__addLog(aOperation, aJobName, aJobExecId, args, anErrorMessage, aId, aTypeArgs) : String`

Adds a new log entry to the channel oJob::log for the `aJobName` provided for the following operations:

- `start` (start of a job)
- `success` (successfully end of a job)
- `error` (erroneous end of a job)
- `depsfail` (job not started do to failed dependencies)

Optionally, for the operation error, you can provide also `anErrorMessage`.
Returns the current `aJobExecId` (or the created one for the operation start).

### oJob.add2Todo

`oJob.add2Todo(aTodo, aId) : oJob`

````text
Add a new aTodo job name or a complete aTodo object with an optional aId.
````

### oJob.addTodos

`oJob.addTodos(aTodoList, aJobtTypeArgs, aId) : oJob`

````text
Adds a new aTodoList array of job names. Optionally you can provide aId to segment these specific jobs.
````

### oJob.getID

`oJob.getID() : String`

````text
Returns this oJob instance ID. Useful to lookup logging in the oJob::log channel.
````

### oJob.getJob

`oJob.getJob(aJobName) : Map`

````text
Retrieves the aJobName definition map so it can be changed and overwritten with "oJob.setJob(aJobName, aJobMap)".
````

### oJob.getLanguages

`oJob.getLanguages(probe) : Array`

````text
Lists registered languages, prerequisites and supported process options. With probe=true, performs local availability checks bounded to five seconds; never installs a runtime.
````

### oJob.load

`oJob.load(aJobsList, aTodoList, aoJobList, args, aId, init, help)`

````text
Loads a set of aJobsList, corresponding aTodoList and a list of aoJobList. Optionally you can provide aId to segment these specific jobs.
````

### oJob.oJob

`oJob.oJob() : oJob`

````text
Creates an instance of an oJob. O Uses the channel oJob::log for job logging, oJob::jobs for job register, oJob::todo as job todo register and oJob::oJob for oJob instances registry.
````

### oJob.registerLanguageCleanup

`oJob.registerLanguageCleanup(aName, aFunction)`

````text
Registers one cleanup per adapter, run after oJob workers stop. Replacing a name replaces its callback.
````

### oJob.removeJob

`oJob.removeJob(aJobName) : oJob`

````text
Removes aJobName.
````

### oJob.runLanguageProcess

`oJob.runLanguageProcess(aCommand, aOptions) : Map`

````text
Runs an argv array locally with concurrent UTF-8 output capture. Options: pwd, env, timeout (positive milliseconds). Returns stdout, stderr, exitcode, timedOut and descendantTracking. Does not install runtimes or parse output.
````

### oJob.setJob

`oJob.setJob(aJobName, aJob) : oJob`

````text
Adds or overwrites an existing aJobName with the configuration aJob.
````

### oJob.start

`oJob.start(args, shouldStop, aId, isSubJob) : oJob`

````text
Starts the todo list. Optionally you can provide arguments to be used by each job. Optionally you can provide aId to segment these specific jobs.
````

### oJob.stop

`oJob.stop()`

````text
Stops all oJob processing.
````

### ow.oJob.addJob

`ow.oJob.addJob(aJobsCh, aName, jobDeps, jobType, aJobTypeArgs, jobArgs, jobFunc, jobFrom, jobTo, jobHelp, jobCatch, jobEach, jobLang, jobFile, jobCheck)`

````text
Provided aJobsCh (a jobs channel) adds a new job with the provided aName, an array of jobDeps (job dependencies), a jobType (e.g. simple, periodic, shutdown), aJobTypeArgs (a map), jobArgs and a jobFunc (a job function).  Optionally you can inherit the job definition from a jobFrom and/or jobTo name ("from" will execute first, "to" will execute after). Also you can include jobHelp.
````

### ow.oJob.addTodo

`ow.oJob.addTodo(aOJobID, aJobsCh, aTodoCh, aJobName, aJobArgs, aJobType, aJobTypeArgs)`

````text
Provided aOJobID (a oJob instance), aJobsCh (a jobs channel), aTodoCh (a todo channel), aJobArgs (job arguments). Optionally you can force the aJobType and aJobTypeArgs.
````

### ow.oJob.askOnHelp

`ow.oJob.askOnHelp(aHelpMap, aUI) : Map`

````text
Collects job arguments interactively. Pass an askConsole-compatible UI to borrow its terminal, or true to open an independent terminal and close it on completion. Without aUI, retains the default process console and output.
````

### ow.oJob.getIncludes

`ow.oJob.getIncludes(aFile) : Map`

````text
Returns a map with include and jobsInclude arrays (if any).
````

### ow.oJob.getJobsCh

`ow.oJob.getJobsCh() : Channel`

````text
Gets the oJob::jobs channel
````

### ow.oJob.getLogCh

`ow.oJob.getLogCh() : Channel`

````text
Gets the oJob::log channel
````

### ow.oJob.getMainCh

`ow.oJob.getMainCh() : Channel`

````text
Gets the oJob::oJob channel
````

### ow.oJob.getMetric

`ow.oJob.getMetric(aMetricId)`

````text
Retrieves the current metric identified by aMetricId
````

### ow.oJob.getMetrics

`ow.oJob.getMetrics(aType) : Function`

````text
Returns a function to be used with ow.metrics.add to add functions by metric aType
````

### ow.oJob.getMetricsCh

`ow.oJob.getMetricsCh() : Channel`

````text
Gets the oJob::metrics channel
````

### ow.oJob.getRawIncludes

`ow.oJob.getRawIncludes(aFile) : Map`

````text
Returns a map with include and jobsInclude arrays from the raw file (no include resolution).
````

### ow.oJob.getState

`ow.oJob.getState() : String`

````text
Get current global state, if defined.
````

### ow.oJob.getTodoCh

`ow.oJob.getTodoCh() : Channel`

````text
Gets the oJob::todo channel
````

### ow.oJob.isEncryptedDefinition

`ow.oJob.isEncryptedDefinition(aFile) : boolean`

````text
Returns true if aFile ends with .yaml.enc or .json.enc (query/hash ignored).
````

### ow.oJob.loadFile

`ow.oJob.loadFile(aFile, args, aId)`

Loads the configuration from a YAML or JSON `aFile` and loads all configuration.
Optionally you can provide `aId` to segment these specific jobs.

Example of YAML:

```yaml
# Name your includes
#
include:
  - hello.js   # Some nice hello function

# Define the jobs
jobs:
   # Start processing
   - name        : Start processing
     exec        : >
        log("init");
        //sprint(ow.oJob.getJobsCh().getAll());

# Stop processing
   - name        : Stop processing
     type        : shutdown
     exec        : >
        log("done");
        sprint(ow.oJob.getLogCh().getAll());

# Hello world after start processing
   - name	      : Hello world
     deps          :
        - Start processing
     exec 	      : >
        sprint(args);
        hello("nuno");

# Bye world
   - name        : Bye
     deps        :
        - Hello world
        - Say the time
     exec        :
        print("bye, nice to meet you.");

# Say the time regularly
   - name        : Say the time
     type        : periodic
     typeArgs    :
        timeInterval   : 1000
        waitForFinish  : true
        cron           : "*\/5 * * * * *"
     exec        : >
        print(new Date());

# List what to do
todo:
   - Start processing
   - Say the time
   - Hello world
   - Bye
   - Stop processing

# This will be a daemon
ojob:
   daemon: false
   unique:
      pidFile     : helloworld.pid
      killPrevious: true
   channels:
      expose     : true
      port       : 17878
      permissions: r
      #list       :
      #  - oJob::log
      #auth       :
      #  - login: ojob
      #    pass : ojob
      #    permissions: r
```

### ow.oJob.loadJSON

`ow.oJob.loadJSON(aJSON, dontLoadTodos) : Object`

````text
Loads aJSON oJob configuration and returns the processed map (with all includes processed).
````

### ow.oJob.loadJobs

`ow.oJob.loadJobs(aFile, args, noReturn) : Array`

````text

````

### ow.oJob.previewFile

`ow.oJob.previewFile(aFile) : Map`

````text
Returns a map with a preview of the oJob configuration that would be executed with aFile.
````

### ow.oJob.run

`ow.oJob.run(providedArgs, aId)`

````text
Tries to run the current loaded configuration jobs (on the corresponding channels) with the provided arguments (providedArgs). Optionally you can provide aId to segment these specific jobs.
````

### ow.oJob.runAllShutdownJobs

`ow.oJob.runAllShutdownJobs()`

````text
Tries to run all the shutdown type jobs accumulated until now.
````

### ow.oJob.runFile

`ow.oJob.runFile(aFile, args, aId, isSubJob, aOptionsMap)`

````text
Loads aFile configuration and executes the oJob defined with the provided args. Optionally you can provide aId to segment these specific jobs.
````

### ow.oJob.runJob

`ow.oJob.runJob(aJob, provideArgs, aId)`

````text
With jobs defined try to execute/start aJob, with the provideArgs, directly passing any existing todo list.  Optionally you can provide aId to segment this specific jobs.
````

### ow.oJob.setMetric

`ow.oJob.setMetric(aId, aMetricObj)`

````text
Sets aMetricObj for the metric identified with aId
````

### ow.oJob.setState

`ow.oJob.setState(aState)`

````text
Sets the current global state to be used with todo.when
````

### ow.oJob.showHelp

`ow.oJob.showHelp(aHelpMap, args, showAnyway) : boolean`

````text
Given a job help map and the current arguments determines if there is a need to show help usage text and shows it on stdout. Returns true if help was output, false otherwise.
````
{% endraw %}
