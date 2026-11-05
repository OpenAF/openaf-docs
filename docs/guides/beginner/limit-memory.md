---
layout: default
title: Limit OpenAF memory
parent: Beginner
grand_parent: Guides
---

# Limit OpenAF memory

In Java if no memory limits are defined the JVM will request memory to the operating system for as long as it can. But this might not be the desired behaviour when sharing memory with other _"memory dynamic"_ applications.

## How to set memory limits

Steps to set memory limits to any OpenAF script:

### Step 1 - Changing startup scripts

With the right permissions, on the OpenAF folder, regenerate the OpenAF scripts (e.g. oaf, oafc, ojob, opack, etc...):

__Unix/Mac__:

````bash
cd /the/openaf/folder
java -jar openaf.jar --install -e 'args=$OAF_JARGS'
````

__Windows__:

````powershell
cd the\openaf\folder
java -jar openaf.jar --install -e 'args=%OAF_JARGS%'
````

This will rewrite all the exiting OpenAF scripts on "the/openaf/folder" to include an extra variable: OAF_JARGS.

### Step 2 - Testing changed scripts

To test the new environment variable execute:

__Unix/Mac__:

````bash
OAF_JARGS="-Xms64m -Xmx128m" ./oaf -c "sprint(ow.loadJava().getMemory(true), '')"

# {"max":"128 MB","total":"64.0 MB","used":"10.1 MB","free":"53.9 MB"}
````

__Windows__:

````powershell
set "OAF_JARGS=-Xms64m -Xmx128m"
oaf.bat -c "sprint(ow.loadJava().getMemory(true), '')"

# {"max":"128 MB","total":"64.0 MB","used":"10.1 MB","free":"53.9 MB"}
````

> The expected result is max = 128 MB and total = 64 MB according with the limits provided in the OAF_JARGS variable.

### Step 3 - Writing a specific startup script

Let's say you have an OpenAF script called _myScript.js_ which you want to limit the memory when it runs. Write a startup script similar to the following example:

__Unix/Mac__:

*myScript.sh*:
````bash
export OAF_JARGS="-Xms64m -Xmx128m"
cd /my/scripts
/the/openaf/folder/oaf -f myScripts.js
````

__Windows__:

*myScript.bat*:
````bat
set "OAF_JARGS=-Xms64m -Xmx128m"
cd my\scripts
the\openaf\folder\oaf -f myScripts.js
````

> For oJobs is similar. Just replace _"oaf"_ with _"ojob"_.
