---
layout: default
title: jmx
parent: Reference
grand_parent: OpenAF docs
---

{% raw %}
## jmx

[Source: `06414cd9`](https://github.com/OpenAF/openaf/blob/06414cd9204e918daa1e2971ce904783299db333/src/openaf/plugins/JMX.java) · [Baseline](../source-snapshot.md)

### JMX.JMX

`JMX.JMX(aURL, aLogin, aPassword, aProvider) : JMX`

Creates an instance to connect to `aURL` (e.g. service:jmx:rmi:///jndi/rmi://127.0.0.1:12345/jmxrmi). If needed `aLogin`
and `aPassword` can be provided. `aProvider` can also be specified to access custom MX bean classes (e.g. WebLogic application servers).
Example:

```javascript
var jmx = new JMX("service:jmx:rmi:///jndi/rmi://127.0.0.1:12345/jmxrmi");
```

### JMX.attach2Local

`JMX.attach2Local(aId) : Object`

````text
Establishes a connection with a local Java process given the aId provided by JMX.getLocals() returning an URL to establish a JMX connection, a list of System environment variables and a Agent describing the Java Management Agent activated on the local Java process.
````

### JMX.getLocals

`JMX.getLocals() : Object`

````text
Returns a Locals map with an id and name of each Java process detected locally. To be used with JMX.attach2Local().
````

### JMX.getObject

`JMX.getObject(aObjName) : Object`

Obtains a bean `aObject` (e.g. `aObjName` = "com.openaf:type=Values").
Example:

```javascript
jmx.getObject("com.openaf:type=Values");
```
{% endraw %}
