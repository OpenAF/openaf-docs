---
layout: default
title: jmxserver
parent: Reference
grand_parent: OpenAF docs
---

{% raw %}
## jmxserver

[Source: `06414cd9`](https://github.com/OpenAF/openaf/blob/06414cd9204e918daa1e2971ce904783299db333/src/openaf/plugins/JMXServer.java) · [Baseline](../source-snapshot.md)

### JMXServer.JMXServer

`JMXServer.JMXServer(aJMXObjectName) : JMXServer`

````text
Creates a new JMX server instance for a given default JMX object name (defaults to 'com.openaf:type=Values'.
````

### JMXServer.addBean

`JMXServer.addBean(aAttrJSON, getFunction, setFunction, opsFunction) : number`

````text
Adds a JMX bean given a JSON map of the attributes, aAttrJSON, and corresponding types (e.g. '[writable] double',  '[writable] long', '[writable] string', 'operation'). Additionally you must provide a getFunction(aAttrName) that will receive  the name of the attribute and should return the value of the attribute and optionally a setFunction(aAttrName, aNewValue) that will receive the name and value of the attribute and should return the new value of the attribute. You can also provide a opsFunction(operation, arrayOfParams, arrayOfSignatures) (arrayOfParams and return should be strings). Returns the number of attributes or 0 if unsuccessful.
````

### JMXServer.addObjectBean

`JMXServer.addObjectBean(aObjectName, aAttrJSON, getFunction, setFunction, opsFunction) : number`

````text
Equivalent to JMXServer.addBean but enables you to add a JMX bean a different JMX object name (aObjectName) given  a JSON map of the attributes, aAttrJSON, and corresponding types (e.g. '[writable] double',  '[writable] long', '[writable] string'). Additionally you must provide a getFunction(aAttrName) that will receive  the name of the attribute and should return the value of the attribute and optionally a setFunction(aAttrName, aNewValue) that will receive the name and value of the attribute and should return the new value of the attribute. You can also provide a opsFunction(operation, arrayOfParams, arrayOfSignatures) (arrayOfParams and return should be strings). Returns the number of attributes or 0 if unsuccessful.
````

### JMXServer.start

`JMXServer.start(aPort, notLocal)`

````text
Starts the JMX server on the given aPort. You should use the addBean function after starting the server. You can optionally indicate that the server can be accessed from other hosts other than the local (NOT ADVISABLE).
````

### JMXServer.stop

`JMXServer.stop()`

````text
Stop the JMX server.
````
{% endraw %}
