---
layout: default
title: oJob.io
parent: Concepts
grand_parent: OpenAF docs
---

# oJob.io

oJob.io is a service providing easy-to-access OpenAF [oJobs](/docs/concepts/oJob) for frequent routines across several domains. With OpenAF installed you simply execute
"ojob" to a specific address and the oJob will be downloaded and executed with the arguments provided. You can check the source code in [GitHub](https://github.com/OpenAF/oJob.io) 
and/or even build your own local [ojob.io service](https://github.com/OpenAF/openaf-opacks/tree/master/oJobIO). To start simply execute:

````bash
$ ojob ojob.io
````

and follow the instructions. You also have extra documentation for each ojob.io through the [website](https://ojob.io).

## Examples:

If you need a quick HTTP server to browse through the current folder from another machine's browser:
````bash
$ ojob ojob.io/httpServers/EasyHTTPd port=12345 path=.
````

If you need a quick HTTPs server to browse through the current folder and eventually upload files from a browse using a self-signed 
SSL certificate generated for a short period of time.
````bash
$ ojob ojob.io/httpServers/uploadHTTPSd cn=myserver.local port=12345
````

oJob.io can also be piped. Let's build an Excel with all the current environment variables:
````bash
$ ojob ojob.io/pipe 0=ojob.io/envs 1=ojob.io/formats/toXLS
````

Let's say you wanna retrieve the same environment variables but on HTML

````bash
$ ojob ojob.io/pipe 0=ojob.io/envs 1=ojob.io/html
````

## Using ojob.io from Docker directly

Depending on the ojob.io job you can run it directly in a docker command:

````bash
$ docker run --rm -ti openaf/oaf --ojob -e "ojob.io"
````

### Examples

Testing port latency:

````bash
docker run --rm -ti openaf/oaf --ojob -e "ojob.io/net/latency host=8.8.8.8 port=443 times=10"
````

Testing JDBC latency:

````bash
$ docker run --rm -ti openaf/oaf --ojob -e "ojob.io/net/jdbc jdbc=jdbc:postgresql://hh-pgsql-public.ebi.ac.uk:5432/pfmegrnargs user=reader pass=NWDMCE5xdipIjRrp"
````

Generating a template oJob yaml file:

````bash
$ docker run --rm -ti openaf/oaf --ojob -e "ojob.io/generate jobs=JobA,JobB author=myself"
````

## Some of the basic ojob.io

| ojob.io | Description | Example |
|---------|-------------|---------|
| check   | Check the syntax of an existing oJob for syntax errors | ````ojob ojob.io/check job=myjob.yaml```` |
| doc     | Generates a markdown output based on the oJob help     | ````ojob ojob.io/doc job=myjob.yaml output=myjob.md```` |
| echo    | Debug ojob to output all arguments provided            | ````ojob ojob.io/echo hello=world```` |
| envs    | Outputs the current environment variables              | ````ojob ojob.io/envs```` |
| generate | Generates a prebuild oJob                             | ````ojob ojob.io/generate > myNewOJob.yaml```` |
| get     | Retrieves the code of ojob.io                          | ````ojob ojob.io/get job=ojob.io/envs > envs.yaml```` |
| help    | Downloads and returns the corresponding oJob help      | ````ojob ojob.io/help job=ojob.io/generate```` |
| html    | Tries to open a browser with the map/array HTML representation | ````ojob ojob.io/pipe 0=ojob.io/help 0.job=ojob.io/generate 1=ojob.io/html```` |
| map     | Tries to open Excel with the list of environment variables | ````ojob ojob.io/pipe 0=ojob.io/envs 1=ojob.io/formats/toXLS```` |
| pipe    | Pipes oJobs passing their output maps or lists between them | ````ojob ojob.io/pipe 0=ojob.io/news/bbc 1=ojob.io/map 1.fields=title,link 2=ojob.io/html```` |

## Formatting the results

Most oJobs in ojob.io output results using the function *ow.oJob.output* or *$output* or *$o*. This allows to control how the results will be formatted. To select a different format just add the argument *__format**:

| Format | Argument | Category | Description |
|--------|----------|----------|-------------|
| CSV | __format=csv __csv="{}" | List/Array results | CSV like format |
| YAML | __format=yaml | List/Array/Map results | Output in YAML |
| JSON | __format=json | List/Array/Map results | Output in JSON |
| CJSON | __format=cjson | List/Array/Map results | Output in colored JSON |
| NDJSON | __format=ndjson | List/Array results | JSON newline-delimited output |
| SLON | __format=slon | List/Array/Map results | [SLON](https://github.com/nmaguiar/slon) output. |
| CSLON | __format=cslon | List/Array/Map results | Colored [SLON](https://github.com/nmaguiar/slon) output. |
| PRETTYJSON | __format=pretty | List/Array/Map results | JSON formatted in human-readable format. |
| MAP | __format=map | List/Array/Map results | List on a rectangular human-readable form. |
| TABLE | __format=table | List/Array results | Output on a table. |
| CTABLE | __format=ctable | List/Array results | Output in a table with row colors and word-wrap. |
| STABLE | __format=stable | List/Array results | Output in a table with row dividers and word-wrap. |
| TREE | __format=tree | List/Array/Map results | Output in tres ASCII format. |
| HTML | __format=html | List/Array/Map results | Output in HTML format. |
| PM | __format=pm | List/Array/Map results | Output into a global variable __pm._list. |
| RES | __format=res | List/Array/Map results | Output into the oJob $get("res") global data. |
| KEY | __format=key __key=specific-key | List/Array/Map results | Output into the oJob specific global data key. |
| ARGS | __format=args | List/Array/Map results | Output into args._list or args._map. |
| TEXT | __format=text | String results | Output in string text representation (if possible) | 
| MD | __format=md | String results | Output in markdown parsing (if possible) |
| HUMAN | __format=human | String results | Output in the raw human-readable representation |
| TOON | __format=toon | List/Array/Map/String results | Output using the [Toon](https://github.com/nmaguiar/toon) terminal rendering library (v2.1.0+) for rich terminal display |