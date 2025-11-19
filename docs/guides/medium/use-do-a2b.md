---
layout: default
title: Using $doA2B
parent: Medium
grand_parent: Guides
---

# Using $doA2B

Most of the times when you need to run a current processing you will have a function (**A**) that computes a work set that needs to be processed by a second function (**B**).

OpenAF provides a helper function, $doA2B, so that during the execution of function **A** each work set item can start being processed by function **B** in concurrently.

The first function **A** receives, as a parameter, a function callback to send a map to each execution of function **B**. Let's take an example of a function **A** that lists the files in a folder and, for each, executes a function **B** that calculates the number of lines in a file.

````javascript
// A map to hold results
var files = {}

$doA2B(each => {
    // FUNCTION A

    // For each file the "each" function will be called with the corresponding "filemap"
    io.listFiles(".").files.forEach(filemap => each(filemap))
}, filemap => {
    // FUNCTION B

    // Ensures the entry received is actually a file and then counts the number of lines
    // and stores in the "files" map.
    if (filemap.isFile) {
       tprint("{% raw %}Counting lines {{filename}}...{% endraw %}", filemap)
       files[filemap.filename] = io.readFileAsArray(filemap.filename).length
    }
}, __, __, error => sprintErr(error))

// Sorts the "files" map and prints the output
cprint(sortMapKeys(files))
````

> Besides the function A and B it's possible to customize the number of concurrent requests to submit at a time, the default timeout to submit more data to be processed concurrently and the error function to handle errors while executing function B.

## In oJob

It's also possible to perform the same with oJob's jobs using the "each" key on a **A** job (in this case "Count lines in files").

````yaml
todo:
- Count lines in files
- Show results

ojob:
  channels:
    create:
    - name: files

jobs:
# ---------------------------
- name : Count lines in files
  check:
    in:
      folder: isString
  each : File count lines
  exec : |
    io.listFiles(args.folder).files.forEach(filemap => each(filemap))

# -----------------------
- name : File count lines
  catch: sprintErr(exception)
  exec : |
    if (args.isFile) {
       tprint("{% raw %}Counting lines {{filepath}}{% endraw %}", args)
       $ch("files").set({
         file : args.filepath
       }, {
         file : args.filepath,
         lines: io.readFileAsArray(args.filepath).length
       })
    }

# ------------------
- name: Show results
  exec: |
    ow.oJob.output($from($ch("files").getAll()).sort("file").select(), args)
````

### Multiple B functions

In oJob it's also possible to have a list of jobs to make up the **B** function make it easy to add or remove specific functionality:

````yaml
# ---------------------------
- name : Count lines in files
  check:
    in:
      folder: isString
  each : 
  - File count lines
  - File count empty lines
  - File count words
  exec : |
    io.listFiles(args.folder).files.forEach(filemap => each(filemap))
````