---
layout: default
title: JDBC drivers and connections
parent: oPacks
grand_parent: Guides
---

# JDBC drivers and connections

The [package catalog](catalog.md#jdbc-drivers) lists each JDBC driver oPack and its declared dependencies. Install only the driver needed for your database. A driver package supplies Java libraries and a JavaScript loader; credentials and database creation remain your responsibility.

## PostgreSQL

```sh
opack install jdbc-postgresql
```

```javascript
loadLib("jdbc-postgresql.js");
var db = DBpostgresql("jdbc:postgresql://localhost:5432/example", "example", "password");
try {
  print(db.q("select 1 as answer").results);
} finally {
  db.close();
}
```

`DBpostgresql(url, user, password, timeout)` selects `org.postgresql.Driver` explicitly. Retrieve real credentials from your configured secret store instead of committing them to a script. See the [loader source](https://github.com/OpenAF/openaf-opacks/blob/87b07e9774902bccee8bf16632201e319dcfca0d/jdbc-postgresql/jdbc-postgresql.js).

## SQLite

```sh
opack install jdbc-sqlite
```

```javascript
loadLib("jdbc-sqlite.js");
var db = DBsqlite("jdbc:sqlite:example.db", "", "");
try {
  print(db.q("select 1 as answer").results);
} finally {
  db.close();
}
```

The [SQLite loader](https://github.com/OpenAF/openaf-opacks/blob/87b07e9774902bccee8bf16632201e319dcfca0d/jdbc-sqlite/jdbc-sqlite.js) registers the `jdbc:sqlite:` prefix and exposes `DBsqlite`. File paths are relative to the process working directory.

## H2 and oafp

OpenAF includes H2. For an isolated in-memory query:

```javascript
var db = new DB("org.h2.Driver", "jdbc:h2:mem:example", "sa", "");
try {
  print(db.q("select 1 as answer").results);
} finally {
  db.close();
}
```

The optional `jdbc-h2` package also provides a `DBh2` wrapper. For processor commands, input connection options use the `indb` prefix and output options use `db`:

```sh
oafp in=db data='select 1 as answer' indbjdbc='jdbc:h2:mem:example' indbuser=sa indbpass='' out=json
```

See [oafp with databases](../oafp/with-db.md), the [DB API](../../reference/db.md), and [JDBC URL execution policy](../advanced/jdbc-url-policy.md). In particular, do not carry execution-enabling JDBC URL options from older examples into a connection without understanding the current policy. Driver-specific options and transaction semantics belong to the selected database.
