---
layout: default
title: How to connect directly to a local JVM via JMX
parent: Advanced
grand_parent: Guides
---

# How to connect directly to a local JVM via JMX

OpenAF's JMX client enables the creation of JMX "client" scripts. To connect the "client" to the target JVM you need an JMX URL.

But if the JVMs are local to the same host you can request a "special" URL that will connect to them without the need to open any remote JMX ports and change the target Java startup arguments.

To do this first list the "recognized" running JVMs on your host:

````javascript
> plugin("JMX");
> var jmx = new JMX();
> af.fromJavaMap(jmx.getLocals());
+---------+-----+-------+-----------------------------------+
| Locals: | [0] | name: | /openaf/openaf.jar --console      |
|         |     |   id: | 24720                             |
+---------+-----+-------+-----------------------------------+
|         | [1] | name: | /myApp/myapp.jar                  |
|         |     |   id: | 15004                             |
+---------+-----+-------+-----------------------------------+
````

Using the _id_ number, for the local Java JVM you want to target, now call _attach2Local_ like this, creating a new JMX object instance:

````javascript
> var localJMX = new JMX(String(jmx.attach2Local(15004).get("URL")));
````

If successfull you will now be able to use the _localJMX_ JMX client object:

````javascript
> var obj = localJMX.getObject("java.lang:type=Runtime");
> String(obj.get("ClassPath"));
"/myApp/myapp.jar"
````
