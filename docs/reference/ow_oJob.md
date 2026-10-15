---
layout: default
title: ow.oJob
parent: Reference
grand_parent: OpenAF docs
---


## ow.oJob

### oJob.__addLog

__oJob.__addLog(aOperation, aJobName, aJobExecId, args, anErrorMessage, aId, aTypeArgs) : String__

````
Adds a new log entry to the channel oJob::log for the aJobName provided for the following operations:

- start (start of a job)
- success (successfully end of a job)
- error (erroneous end of a job)
- depsfail (job not started do to failed dependencies)

Optionally, for the operation error, you can provide also anErrorMessage.
Returns the current aJobExecId (or the created one for the operation start).
````
### oJob.add2Todo

__oJob.add2Todo(aTodo, aId) : oJob__

````
Add a new aTodo job name or a complete aTodo object with an optional aId.
````
### oJob.addTodos

__oJob.addTodos(aTodoList, aJobtTypeArgs, aId) : oJob__

````
Adds a new aTodoList array of job names. Optionally you can provide aId to segment these specific jobs.
````
### oJob.getID

__oJob.getID() : String__

````
Returns this oJob instance ID. Useful to lookup logging in the oJob::log channel.
````
### oJob.getJob

__oJob.getJob(aJobName) : Map__

````
Retrieves the aJobName definition map so it can be changed and overwritten with "oJob.setJob(aJobName, aJobMap)".
````
### oJob.load

__oJob.load(aJobsList, aTodoList, aoJobList, args, aId, init, help)__

````
Loads a set of aJobsList, corresponding aTodoList and a list of aoJobList. Optionally you can provide aId to segment these specific jobs.
````
### oJob.oJob

__oJob.oJob() : oJob__

````
Creates an instance of an oJob. O Uses the channel oJob::log for job logging, oJob::jobs for job register, oJob::todo as job todo register and oJob::oJob for oJob instances registry.
````
### oJob.removeJob

__oJob.removeJob(aJobName) : oJob__

````
Removes aJobName.
````
### oJob.setJob

__oJob.setJob(aJobName, aJob) : oJob__

````
Adds or overwrites an existing aJobName with the configuration aJob.
````
### oJob.start

__oJob.start(args, shouldStop, aId, isSubJob) : oJob__

````
Starts the todo list. Optionally you can provide arguments to be used by each job. Optionally you can provide aId to segment these specific jobs.
````
### oJob.stop

__oJob.stop()__

````
Stops all oJob processing.
````
### ow.oJob.addJob

__ow.oJob.addJob(aJobsCh, aName, jobDeps, jobType, aJobTypeArgs, jobArgs, jobFunc, jobFrom, jobTo, jobHelp, jobCatch, jobEach, jobLang, jobFile, jobCheck)__

````
Provided aJobsCh (a jobs channel) adds a new job with the provided aName, an array of jobDeps (job dependencies), a jobType (e.g. simple, periodic, shutdown), aJobTypeArgs (a map), jobArgs and a jobFunc (a job function).  Optionally you can inherit the job definition from a jobFrom and/or jobTo name ("from" will execute first, "to" will execute after). Also you can include jobHelp.
````
### ow.oJob.addTodo

__ow.oJob.addTodo(aOJobID, aJobsCh, aTodoCh, aJobName, aJobArgs, aJobType, aJobTypeArgs)__

````
Provided aOJobID (a oJob instance), aJobsCh (a jobs channel), aTodoCh (a todo channel), aJobArgs (job arguments). Optionally you can force the aJobType and aJobTypeArgs.
````
### ow.oJob.getJobsCh

__ow.oJob.getJobsCh() : Channel__

````
Gets the oJob::jobs channel
````
### ow.oJob.getLogCh

__ow.oJob.getLogCh() : Channel__

````
Gets the oJob::log channel
````
### ow.oJob.getMainCh

__ow.oJob.getMainCh() : Channel__

````
Gets the oJob::oJob channel
````
### ow.oJob.getMetric

__ow.oJob.getMetric(aMetricId)__

````
Retrieves the current metric identified by aMetricId
````
### ow.oJob.getMetrics

__ow.oJob.getMetrics(aType) : Function__

````
Returns a function to be used with ow.metrics.add to add functions by metric aType
````
### ow.oJob.getMetricsCh

__ow.oJob.getMetricsCh() : Channel__

````
Gets the oJob::metrics channel
````
### ow.oJob.getState

__ow.oJob.getState() : String__

````
Get current global state, if defined.
````
### ow.oJob.getTodoCh

__ow.oJob.getTodoCh() : Channel__

````
Gets the oJob::todo channel
````
### ow.oJob.loadFile

__ow.oJob.loadFile(aFile, args, aId)__

````
Loads the configuration from a YAML or JSON aFile and loads all configuration.
Optionally you can provide aId to segment these specific jobs.

Example of YAML:
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


````
### ow.oJob.loadJobs

__ow.oJob.loadJobs(aFile, args, noReturn) : Array__

````

````
### ow.oJob.loadJSON

__ow.oJob.loadJSON(aJSON, dontLoadTodos) : Object__

````
Loads aJSON oJob configuration and returns the processed map (with all includes processed).
````
### ow.oJob.previewFile

__ow.oJob.previewFile(aFile) : Map__

````
Returns a map with a preview of the oJob configuration that would be executed with aFile.
````
### ow.oJob.run

__ow.oJob.run(providedArgs, aId)__

````
Tries to run the current loaded configuration jobs (on the corresponding channels) with the provided arguments (providedArgs). Optionally you can provide aId to segment these specific jobs.
````
### ow.oJob.runAllShutdownJobs

__ow.oJob.runAllShutdownJobs()__

````
Tries to run all the shutdown type jobs accumulated until now.
````
### ow.oJob.runFile

__ow.oJob.runFile(aFile, args, aId, isSubJob, aOptionsMap)__

````
Loads aFile configuration and executes the oJob defined with the provided args. Optionally you can provide aId to segment these specific jobs.
````
### ow.oJob.runJob

__ow.oJob.runJob(aJob, provideArgs, aId)__

````
With jobs defined try to execute/start aJob, with the provideArgs, directly passing any existing todo list.  Optionally you can provide aId to segment this specific jobs.
````
### ow.oJob.setMetric

__ow.oJob.setMetric(aId, aMetricObj)__

````
Sets aMetricObj for the metric identified with aId
````
### ow.oJob.setState

__ow.oJob.setState(aState)__

````
Sets the current global state to be used with todo.when
````
### ow.oJob.showHelp

__ow.oJob.showHelp(aHelpMap, args, showAnyway) : boolean__

````
Given a job help map and the current arguments determines if there is a need to show help usage text and shows it on stdout. Returns true if help was output, false otherwise.
````

### ow.oJob.askOnHelp

__ow.oJob.askOnHelp(aHelpMap, aUI) : Map__

````
Collects job arguments interactively. Pass an askConsole-compatible UI to borrow its terminal, or true to open an independent terminal and close it on completion. Without aUI, retains the default process console and output.
````

### oJob.runLanguageProcess

__oJob.runLanguageProcess(aCommand, aOptions) : Map__

````
Runs an argv array locally with concurrent UTF-8 output capture. Options: pwd, env, timeout (positive milliseconds). Returns stdout, stderr, exitcode, timedOut and descendantTracking. Does not install runtimes or parse output.
````

### oJob.getLanguages

__oJob.getLanguages(probe) : Array__

````
Lists registered languages, prerequisites and supported process options. With probe=true, performs local availability checks bounded to five seconds; never installs a runtime.
````

### oJob.registerLanguageCleanup

__oJob.registerLanguageCleanup(aName, aFunction)__

````
Registers one cleanup per adapter, run after oJob workers stop. Replacing a name replaces its callback.
````
