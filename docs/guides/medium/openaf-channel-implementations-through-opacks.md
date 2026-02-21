---
layout: default
title: OpenAF channel implementations through oPacks
parent: Medium
grand_parent: Guides
---

# OpenAF channel implementations through oPacks

This guide provides quick usage examples for OpenAF channel types implemented by oPacks.

## Mongo (`mongo`)

```javascript
// opack install Mongo
loadLib("mongo.js")

$ch("users").create("mongo", {
  url: "mongodb://127.0.0.1:27017",
  database: "app",
  collection: "users"
})

$ch("users").set({ _id: "u1" }, { _id: "u1", name: "Alice" })
print($ch("users").get({ _id: "u1" }).name)
```

## Etcd v3 (`etcd3`)

```javascript
// opack install etcd3
loadLib("etcd3.js")

$ch("cfg").create("etcd3", {
  host: "127.0.0.1",
  port: 2379,
  namespace: "openaf/"
})

$ch("cfg").set({ key: "featureA" }, { enabled: true })
print($ch("cfg").get({ key: "featureA" }).enabled)
```

## Redis (`redis`)

```javascript
// opack install Redis
loadLib("redis.js")

$ch("cache").create("redis", {
  host: "127.0.0.1",
  port: 6379
})

$ch("cache").set({ key: "greeting" }, { value: "hello" })
print($ch("cache").get({ key: "greeting" }).value)
```

## RocksDB (`rocksdb`)

```javascript
// opack install rocksdb
loadLib("rocksdb.js")

$ch("state").create("rocksdb", { path: "./db/state" })
$ch("state").set({ id: "job-1" }, { id: "job-1", status: "running" })
print($ch("state").get({ id: "job-1" }).status)
```

## S3 (`s3`)

```javascript
// opack install S3
loadLib("s3.js")

$ch("bucketData").create("s3", {
  s3url: "https://play.min.io:9000",
  s3accessKey: "minioadmin",
  s3secretKey: "minioadmin",
  s3bucket: "test",
  s3prefix: "openaf/ch",
  multifile: true
})

$ch("bucketData").set({ id: "1" }, { id: "1", value: "hello s3" })
print($ch("bucketData").get({ id: "1" }).value)
```

## Chronicle Queue (`cq`)

```javascript
// opack install cq
loadLib("cq.js")

$ch("events").create("cq", {
  path: "./queue-data/events",
  cycle: "DAILY"
})

$ch("events").set({ id: "evt-1" }, { id: "evt-1", type: "created" })
print($ch("events").size())
```

## GIST (`gist`)

```javascript
// opack install GIST
loadLib("gist.js")

$ch("snippets").create("gist", {
  user: "your-github-user",
  token: "ghp_xxx"
})

var r = $ch("snippets").set({ file: "sample.json", description: "OpenAF sample" }, { ok: true })
print(r.id)
```

## DynamoDB (`dynamo`)

```javascript
// opack install AWS
loadLib("aws_dynamo.js")

$ch("orders").create("dynamo", {
  region: "us-east-1",
  tableName: "orders"
})

$ch("orders").set({ pk: "order#1", sk: "v1" }, { pk: "order#1", sk: "v1", total: 42 })
print($ch("orders").get({ pk: "order#1", sk: "v1" }).total)
```

## AWS Secrets Manager (`awssecrets`)

This channel type is mainly used by `$sec`.

```javascript
// opack install AWS
// requires AWS credentials + AWS_REGION in the environment
loadLib("aws_secrets_sec.js")

$ch("___openaf_sbuckets-awssecrets").create("awssecrets", {})
var secret = $sec("awssecrets", "arn:aws:secretsmanager:us-east-1:123456789012:secret:my-secret").get("SecretString")
print(secret.username)
```

## Lucene Vector Search (`vectordb`)

```javascript
// opack install lucene
loadLib("lucene.js")

$ch("embeddings").create("vectordb", {
  path: "./data/embeddings",
  dimension: 3
})

$ch("embeddings").set({ id: "doc-1" }, { vector: [0.1, 0.2, 0.3], payload: { text: "hello" } })
var hits = $ch("embeddings").getAll({ vector: [0.1, 0.2, 0.29], k: 3 })
print(hits.length)
```

## Lucene Full-text Search (`searchdb`)

```javascript
// opack install lucene
loadLib("lucene.js")

$ch("docs").create("searchdb", {
  path: "./data/search",
  idField: "id",
  contentField: "content"
})

$ch("docs").set({ id: "doc-1" }, { content: "OpenAF channels with Lucene", payload: { source: "example" } })
var res = $ch("docs").getAll({ query: "channels", limit: 5 })
print(res.length)
```

## Notes

* Channel type names are case-sensitive (`mongo`, `etcd3`, `redis`, etc.).
* Most of these channel types require `loadLib(...)` from the corresponding installed oPack.
* For cloud-backed channels (`dynamo`, `awssecrets`, `s3`) ensure credentials and network access are configured.
