---
layout: default
title: Accessing MongoDB from OpenAF
parent: Medium
grand_parent: Guides
---

# Accessing MongoDB from OpenAF

OpenAF can access MongoDB through an oPack called "Mongo". This oPack uses the MongoDB Java client underneath and provides some utility functions for easier access/coding.

## Installing the oPack

````bash
$ opack install mongo
````

## Connecting using MongoUtil

First you need to determine the corresponding [MongoDB URL](https://docs.mongodb.com/manual/reference/connection-string) to access the intended MongoDB instance:

_mongodb://[username:password@]host1[:port1][,...hostN[:portN]][/[defaultauthdb][?options]]_

Some examples:

> mongodb://1.2.3.4:27017

> mongodb://root:example@1.2.3.4:27017

Then, on your code or in an OpenAF console just create an instance of the MongoUtil object:

````javascript
loadLib("mongo.js");

var mongo = new MongoUtil("mongodb://mongo:27017"); // or mongodb://root:example@mongo:27017 for root access
````

## Checking the available databases

A MongoDB is composed of one or more databases. To list them use the previously created MongoUtil object instance:

````javascript
mongo.getDatabaseNames()
// [0] admin
// [1] config
// [2] local
````

## Checking the available collections on a database

Each MongoDB database can have one or more collections of "documents". To list the available collections use the previously created MongoUtil object instance:

````javascript
mongo.getCollectionNames("config")
// [0] system.sessions

mongo.getCollectionNames("admin")
// [0] system.version
// [1] system.users

mongo.getCollectionNames("local")
// [0] startup_log
````

## Access data on a collection

To access data on a collection of a database use the previously created MongoUtil object instance to create an [OpenAF channel](../../concepts/OpenAF-Channels.md).

Example checking on the collection _system.users_ of the _admin_ database:

````javascript
mongo.getCh("admin", "system.users", "mongoUsers")

$ch("mongoUsers").size()
// 1

$ch("mongoUsers").getAll()
// [ { _id: "admin.root", ... , user: "root", db: "admin", ..., roles: [ { role: "root", db: "admin" }] }
````

Example checking the last log entry on the collection _startup\_log_ of the _local_ database:

````javascript
mongo.getCh("local", "startup_log", "mongoLog")

$ch("mongoLog").size()
// 4

var entries = $ch("mongoLog").getKeys()

$ch("mongoLog").get(entries[3])
// { ... hostname: "abcdef12345", ... , pid: 1, buildinfo: { version: "...", ... } }
````

## Create, modify or delete data

Following the previous examples we created a _test_ collection on the _local_ database in MongoDB. So let's start by creating an [OpenAF channel](../../concepts/OpenAF-Channels.md) for it:

````javascript
mongo.getCh("local", "test", "test")

$ch("test").size()
// 0
````

### Creating

All entries on a MongoDB collection have a special field _\_id_ which identifies uniquely each document. Lets create a document:

````javascript
// set(key, value)
// value must also have the _id field and value
$ch("test").set({ _id: 1 }, { _id: 1, text: "My first entry" });

$ch("test").size()
// 1

$ch("test").get({ _id: 1 })
// { _id: 1, text: "My first entry" });
````

### Modifying

To modify any MongoDB document you just need the corresponding _\_id_ field value:

````javascript
var document = $ch("test").get({ _id: 1 })

document.text  = "My modified entry";
document.other = 12345

// Modify the existing entry with the map of the document variable
$ch("test").set({ _id: 1 }, document)

$ch("test").get({ _id: 1 })
// { _id: 1, text: "My modified entry", other: 12345 }
````

_Note: You can use also the OpenAF channel setAll method if needed. Please refere to the generic [OpenAF channels](../../concepts/OpenAF-Channels.md) documentation._

### Deleting

To delete any MongoDB document you just need the corresponding _\_id_ field value:

````javascript
$ch("test").size()
// 1

$ch("test").unset({ _id: 1 })

$ch("test").size()
// 0
````

_Note: You can use also the OpenAF channel unsetAll method if needed. Please refere to the generic [OpenAF channels](../../concepts/OpenAF-Channels.md) documentation._

## Close the connection

To close the establihed connections do destroy each channel and also use MongoUtil.close:

````javascript
$ch("mongoUsers").destroy();
$ch("mongoLog").destroy();
$ch("test").destroy();

mongo.close()
````
