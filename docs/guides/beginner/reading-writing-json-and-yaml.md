---
layout: default
title: Reading and writing from/to JSON and YAML files
parent: Beginner
grand_parent: Guides
---

# Reading and writing from/to JSON and YAML files

One of the most basic funcionality in OpenAF is to read and write Javascript maps or arrays to [JSON](https://en.wikipedia.org/wiki/JSON) or [YAML](https://en.wikipedia.org/wiki/YAML) files.

## Writing

Given any Javascript map or array you can write it to a JSON or YAML file. Do note that only numbers, strings, booleans, other maps and other arrays will be stored given the limitations (technical and for security reasons) of the JSON and the YAML formats.

Let's starts creating a simple Javascript map:

````javascript
var example = {
    name: "point",
    coordinates: { x: -1, y: 1 },
    labels: [ "point", "dot" ]
}
````

To write it to a JSON file simply execute:

````javascript
io.writeFileJSON("example.json", example)
````

> In more advanced contexts you might want to remove all spaces in the JSON representation to save space. To do this simple add a third argument: ````io.writeFileJSON("example.json", example, "")````

To write it to an YAML file simply execute:

````javascript
io.writeFileYAML("example.yaml", example)
````

> In more advanced contexts you might want to write multi-document YAMLs. To do it simple alter the command to: ````io.writeFileYAML("examples.yaml", [ example1, example2, example3 ], true)````

## Reading

To read a JSON or YAML file and create a javascript map/array with the previously stored contents you can simply execute:

__JSON:__

````javascript
var example = io.readFileJSON("example.json")
````

__YAML:__

````javascript
var example = io.readFileYAML("example.yaml")
````

> If the YAML is a multi-document YAML the result will be an array where each entry is a document.
