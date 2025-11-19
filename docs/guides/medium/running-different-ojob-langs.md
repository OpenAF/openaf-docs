---
layout: default
title: Running different oJob languages
parent: Medium
grand_parent: Guides
---

# Running different oJob languages

When running an oJob, by default, the language of the _exec_ section of a job definition is javascript:

````yaml
jobs:
- name: My job
  exec: |
    var ABC = 123;
    print(ABC);
````

But it's also possible to define other available "languages". For example you could add shell scripts by just defining the "lang" entry on any job definition:

````yaml
jobs:
- name: My job
  lang: shell
  exec: |
    ABC=123
    echo $ABC
````

There are multiple languages available by default (if the corresponding languages is available in your system):

| Lang | Description | 
|------|-------------|
| shell | In unix based OS it will default to "/bin/sh" and in Windows to "cmd". In the _exec_ contents you can add script code as you would do on a _.sh_ file or _.bat_ file. |
| powershell | In Windows you can use PowerShell scripting. |
| ssh | Takes, as arguments, the arguments of $ssh (check the help for $ssh) and executes the code remotely. |
| winssh | Similar to "ssh" but will use powershell |
| go | Will execute any go-lang code in the _exec_ contents with "go run" |
| ruby | Will execute any ruby code in the _exec_ contents |
| perl | Will execute any perl code in the _exec_ contents |
| python | Executes any Python 2 or 3 code depending on the version available on your Unix or Windows system. |

> NOTE: Python has a special integration where the _args_ variable is available and can be modified directly. Other special Python functions are also defined like \_('[openaf code]') and \_d(python variable).

## Interaction between jobs

### Output 

In oJob the interaction between different jobs, in the same execution chain, is achieved from the variable _args_. With the exception of Pyhton and OpenAF, this variable is not available in all languages. 
So the script language execution output is parsed for JSON:

````yaml
jobs:
# --------------
- name: Do stuff
  to  :
  - Shell job
  - OpenAF job

# ---------------
- name: Shell job
  lang: shell
  exec: |
    ABC=123
    echo { \"result\": \"$ABC\" }
    
# ----------------
- name: OpenAF job
  exec: |
    print(args.result);
````

### Input

For input the _exec_ contents are basically a template (HandleBars) where you can use any of the _args_ variables:

{% raw %}````yaml
jobs:
# --------------
- name: Do stuff
  to  :
  - Define name
  - Say hello

# -----------------
- name: Define name
  lang: shell
  exec: |
    echo { \"name\": \"`hostname`\" }

# ---------------
- name: Say hello
  lang: shell
  exec: |
    echo Hello {{name}}!
````{% endraw %}

## What's possible

Pretty much all job related functionality is avaiable. Examples:

{% raw %}````yaml
jobs:
- name: My external file
  lang: perl
  file: myjob.pl

- name: My parallel execution
  lang: shell
  args:
  - name: Anne
  - name: Mary
  - name: John
  exec: |
    echo Hello {{name}}!

- name: Using handlebars
  lang: shell
  args:
    names:
    - name  : Anne
      type  : scientist
      isMale: false
    - name  : Mary
      type  : programmer
      isMale: false
    - name  : John
      type  : mechanic
      isMale: true
  exec: |
    {{#each names}}
    echo We need {{name}}, {{#if isMale}}he{{else}}she{{/if}} is a {{type}}.
    {{/each}}
````{% endraw %}

You can even mix languages and use dependencies if needed:

````yaml
ojob:
  async: true

jobs:
# -----------
- name: Begin
  lang: shell
  exec: |
    echo Lets begin...

- name: Middle
  lang: python
  deps:
  - Begin
  exec: |
    print("I'm on the middle.")

# ---------
- name: End
  deps:
  - Begin
  - Middle
  exec: |
    print("That's all folks!")

todo:
- Begin
- Middle
- End
````

## What's not possible

Anything that is directly related with OpenAF. Examples:
* using the _"each"_ function to execute a sub-job in parallel for every call on a main job is only possible with the default OpenAF language.
* using ````ojob ojob.io/check job=myjob.yaml```` will only check OpenAF syntax for the regular OpenAF code

## Custom languages

### Stdin based

It's also possible to extend it to other languages or needs. For example, if you want to execute Swift:

````yaml
ojob:
  langs:
  - lang : swift
    shell: /usr/bin/swift -
    
jobs:
# -------------------
- name: My swift code
  lang: swift
  exec: |
    import Foundation;

    if let value = ProcessInfo.processInfo.environment["NAME"] {
       print("{ \"msg\": \"Hello " + value + "!\" }");
    } else {
       print("{ \"msg\": \"Hello stranger!\" }");
    }

````

### Code based

If the language "execution" command doesn't support scripting from the _stdin_ it's possible to define the code in an OpenAF function:

````yaml
ojob:
  langs:
  - lang  : prolog
    langFn: |
      // Handle prolog knowledge
      // Convert args to prolog knowledge with prefix kl_
      
jobs:
# ------------------------------------------------
- name: Infer all german car brands from knowledge
  lang: prolog
  args:
  
    knowledge:
    - brand     : BMW
      isCarMaker: true
      isGerman  : true
    - brand     : Mercedes
      isCarMaker: true
      isGerman  : true
    - brand     : Tesla
      isCarMaker: true
      isGerman  : false
  
    knowledgeKey: brand
    
  exec: kl_isCarMaker(Brand, 'true'), kl_isGerman(Brand, 'true').
````

> NOTE: If you are curious about Prolog you can see more in the OpenAF's [Prolog oPack](https://github.com/OpenAF/openaf-opacks/tree/master/prolog)
