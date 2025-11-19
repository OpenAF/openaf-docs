---
layout: default
title: Applying Templates
parent: oJobIO
grand_parent: Guides
---

# Applying Templates

OpenAF comes bundle with a small template engine that makes it easy to quickly have a text template and apply a source of data. For example:

Let's consider a small data file in YAML (data.yaml):

````yaml
data:
  names:
  - Anne
  - John
  - Scott
````

A template file (using [HandleBars](https://handlebarsjs.com/guide/)) to produce a shell script (script.hbs):

````handlebars
{% raw %}{{#each names}}{% endraw %}
echo {% raw %}{{this}}{% endraw %}
{% raw %}{{/each}}{% endraw %}
````

Execute the [ojob.io/template/apply](https://ojob.io/template/apply.md):

````bash
$ ojob ojob.io/template/apply data=data.yaml template=script.hbs file=script.sh
````

And you get the result in script.sh:

````bash
echo Anne
echo John
echo Scott 
````

## Putting everything on the same file

You can provide the template and the output file on the initial YAML data file (data.yaml):

{% raw %}
````yaml
template: &TEMPLATE |
  {{#each names}}
  echo {{this}}
  {{/each}}

data:
  _template: *TEMPLATE
  _file    : script.sh
  names    :
  - Anne
  - John
  - Scott
````

And it's even simpler to execute:

````sh
$ ojob ojob.io/template/apply data=data.yaml
````

> On the _template entry you can still use external files if needed. Instead of a template just replace the entry with the name of an existing file: "_template: myTemplate.hbs"

## Generating multiple files

Let's take our previous example and generate a Windows and an Unix script (data.yaml):

{% raw %}````yaml
template: &TEMPLATE |
  {{#if windows}}
  @echo off
  {{else}}
  #!/bin/sh
  {{/if}}
  {{#each names}}
  echo {{this}}
  {{/each}}


data:
- _template: *TEMPLATE
  _file    : script.sh
  windows  : false
  names    : &DATA
  - Anne
  - John
  - Scott

- _template: *TEMPLATE
  _file    : script.bat
  windows  : true
  names    : *DATA
````{% endraw %}

Execute again and you will get the two different scripts:

````sh
$ ojob ojob.io/template/apply data=data.yaml
$ cat script.bat
@echo off
echo Anne
echo John
echo Scott
$ cat script.sh
#!/bin/sh
echo Anne
echo John
echo Scott
````

> If the "data" entry on the data.yaml file is an array it will that each entry will produce a different file. You can add an entire path that OpenAF will try to create the necessary folders.

## Using multiple templates

In your previous example you tried to just use one template and using HandleBars produce two scripts using the same template. But, if needed, you can actually use different templates (data.yaml):

{% raw %}````yaml
templateWin: &TEMPLATE_WIN |
  @echo off
  {{#each names}}
  echo {{this}}
  {{/each}}

templateUnix: &TEMPLATE_UNIX |
  #!/bin/sh
  {{#each names}}
  echo {{this}}
  {{/each}}

data:
- _template: *TEMPLATE_WIN
  _file    : script.bat
  names    : &DATA
  - Anne
  - John
  - Scott

- _template: *TEMPLATE_UNIX
  _file    : script.sh
  names    : *DATA
````{% endraw %}

And executing in the same way as the previous example it will generate the same exact scripts.

## Generating other templates

When it gets really interesting is when you generate other data files using a master data & template file. Let's say you need to generate some install scripts for your Java application in different architectures with different JREs. Your stepA.yaml could look like this:

````yaml
template: &TEMPLATE |
  _template: |
    \{{#if win}}
    @echo off
    wget -O jre.zip https://my.site/jres/\{{arch}}/jre-\{{jvm}}.zip
    unzip jre.zip
    del jre.zip
    \{{else}}
    #!/bin/sh
    wget -O jre.tgz https://my.site/jres/\{{arch}}/jre-\{{jvm}}.tgz
    rm jre.tgz
    \{{/if}}
    wget -O myapp.jar https://my.site/\{{dist}}/myapp.jar
    jre/bin/java -jar myapp.jar --install

  data:
  {{#each arch}}
   {{#each ../jvmVersion}}
    {{#each ../../appDistribution}}
  - _file: scripts/{{this}}/{{../../this}}/{{../this}}/install.{{#is ../../this 'win64'}}bat{{else}}sh{{/is}}
    win : {{#is ../../this 'win64'}}true{{else}}false{{/is}}
    dist: {{this}}
    jvm : {{../this}}
    arch: {{../../this}}
    {{/each}}
   {{/each}}
  {{/each}}

data:
  _file          : stepB.yaml
  _template      : *TEMPLATE
  arch           :
  - amd64
  - x86
  - arm64
  - m1
  - win64
  jvmVersion     :
  - 8
  - 11
  - 15
  appDistribution:
  - stable
  - canary
  - nightly
````

Executing ojob.io/template/apply on stepA.yaml generates a new stepB.yaml with 45 data entries:

````sh
$ ojob ojob.io/template/apply data=stepA.yaml
````

stepB.yaml:

````yaml
_template: &TEMPLATE
# ...
data: 
- _file    : scripts/stable/amd64/8/install.sh
  _template: *TEMPLATE
  win      : false
  dist     : stable
  jvm      : 8
  arch     : amd64
- _file    : scripts/stable/amd64/8/install.sh
  _template: *TEMPLATE
  win      : false
  dist     : stable
  jvm      : 8
  arch     : amd64
# ...
````
{% endraw %}

Executing stepB.yaml:

````sh
$ ojob ojob.io/template/apply data=stepB.yaml
$ find scripts | grep install | wc -l
45
````

You get 45 install scripts. Now if there is any change you need you just need to change the original template and execute stepA.yaml and then stepB.yaml and the change will be propagated to 45 files. 

Of couse, adding new architecures, JVM versions and application distributions is as easy as just changing the stepA.yaml file.

> On stepA.yaml some handlebar entries are escaped with '\'. This is how you escape a handlebar entry to keep if for being evaluated directly on stepA.yaml.


