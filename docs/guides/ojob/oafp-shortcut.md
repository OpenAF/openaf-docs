---
layout: default
title: Example of using the oafp oJob shortcut
parent: oJob
grand_parent: Guides
---

# Example of using the oafp oJob shortcut

Using the oJob's oafp shortcut it's possible to build oJobs that use oafp functionality to process input data into output data.

In this example a [SLON](https://github.com/nmaguiar/slon) string is parsed by oafp and set to the 'test' key. Then the data is retrieved from the 'test' key and each element is incremented setting the result back to the 'test' key. Then, finally, it outputs the 'test' key in a _ctree_ format:

```yaml
todo:
- Sample job

jobs:
# -----------------
- name : Sample job
  from :
  # Run OAFP given input data and setting the output on key test
  - (oafp    ):
      in   : slon
      data : "(a: 1, b: 2, c: 3)"
      out  : key
      __key: test
  # Output the result
  to   :
  - (output  ): test
    ((format)): ctree
  exec : |
    // Manipulate what is set on key 'test'

    var data = $get("test")
    Object.keys(data).forEach(key => data[key]++)
    $set("test", data)
```

Executing this oJob you should be able to see a similar result to:

```
╭ a: 2              
├ b: 3 
╰ c: 4 
```
