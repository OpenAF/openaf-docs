---
layout: default
title: Getting a DB table columns/fields
parent: Advanced
grand_parent: Guides
---

# Getting a DB table columns/fields

Ever wonder how the OpenAF-console can do commands like _"dsql"_ to list all the columns of a table (or a database object) and quickly? It's all on the JDBC metadata for any query over all columns. No need to go to the specific database column catalog.

## Getting the metadata

For each of the tables identified on the catalog of the corresponding database:

1. Performe a simple query to access the table's metadata BUT getting the JDBC ResultSet object:

````javascript
var db = new DB(jdbcURL, jdbcUsername, jdbcPassword);
var rs = db.qsRS("select * from \"" + schemaName + "\".\"" + tableName + "\"");
````

_Note: If you want to use a specific JDBC driver class just replace by "new DB(jdbcDriver, jdbcURL, jdbcUsername, jdbcPassword)"_

2. Get the number of columns from the JDBC ResultSet object:

````javascript
var numberOfColumns = rs.getMetaData().getColumnCount();
````

3. Get the columns' metadata:

````javascript
var columns = [];
for(let ci = 1; ci <= numberOfColumns; ci++) {
    columns.push({
        name : rs.getMetaData().getColumnName(ci),
        type:  rs.getMetaData().getColumnTypeName(ci).toUpperCase(),
        size : rs.getMetaData().getColumnDisplaySize(ci),
        scale: rs.getMetaData().getScale(ci)
    })
};
````

4. (please) Close the result set object and any possible transaction (e.g. because PostgreSQL):

````javascript
rs.close();
db.rollback();
````

And there you have it, a _columns_ array where each map entry has the necessary column information of the specific table:

````javascript
> table columns
     name      |  type   |size|scale
---------------+---------+----+-----
ID             |NUMERIC  |11  |0
SOME           |VARCHAR  |35  |0
TKEY           |VARCHAR  |512 |0
VALUE          |NUMERIC  |25  |6
CREATED_BY     |VARCHAR  |64  |0
CREATED_DATE   |TIMESTAMP|22  |0
MODIFIED_BY    |VARCHAR  |64  |0
MODIFIED_DATE  |TIMESTAMP|22  |0
[#8 rows]
````

## What about the list of tables?

Ok, for the list of tables you might really need to go the database's catalog. Here are some examples:

## Oracle

To get all tables in a specific Oracle schema:

````javascript
var tables = mapArray(db.qs("select owner || '.' || table_name from all_tables where owner = ?", ['mySchema'], true).results, [ "table_name" ]);
````

## PostgreSQL

To get all tables in a specific PostgreSQL schema:

````javascript
var tables = mapArray(db.qs("select table_schema || '.' || table_name from information_schema.tables where table_schema = ?", ['mySchema'], true).results, [ "table_name" ]);
````

## H2

To get all tables in a specific H2 schema:

````javascript
var tables = mapArray(db.qs("select table_schema || '.' || table_name from information_schema.tables where table_schema = ?", ['mySchema'], true).results, [ "table_name" ]);
````

_Note: Yes, it's equal to PostgreSQL_
