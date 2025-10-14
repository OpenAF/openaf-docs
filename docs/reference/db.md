---
layout: default
title: db
parent: Reference
grand_parent: OpenAF docs
---


## db

### DB.close

__DB.close()__

````
Closes the database connection for this DB object instance. In case of error an exception will be thrown.
````
### DB.closeAllStatements

__DB.closeAllStatements()__

````
Tries to close all prepared statements for this DB object instance. If an error occurs during this process an exception will be thrown.
````
### DB.closeStatement

__DB.closeStatement(aStatement)__

````
Closes the corresponding prepared statement. If an error occurs during this process an exception will be thrown.
````
### DB.commit

__DB.commit()__

````
Commits the current transaction associated with this DB object. An exception will be thrown if any database error occurs.

Example:

db.u("INSERT INTO A VALUES (1)");
db.commit();

````
### DB.convertDates

__DB.convertDates(aFlag)__

````
Sets to true or false (defaults to false) the conversion of Dates to javascript Date objects instead of strings.
````
### DB.db

__DB.db(aDriver, aURL, aLogin, aPassword, aTimeout)__

````
Creates a new instance of the object DB providing java class aDriver (e.g. oracle.jdbc.OracleDriver) that must be included on OpenAF's classpath, a JDBC aURL, aLogin and aPassword. If the aDriver is  null or undefined the Oracle driver will be used. Optionally you can provide aTimeout in ms.

Examples of JDBC URLs:

- Oracle Thin: jdbc:oracle:thin:@{{host}}:{{port}}:{{database}}
- PostgreSQL : jdbc:postgresql://{{host}}:{{port}}/{{database}}
- H2         : jdbc:h2:{{file}}
````
### DB.getAutoCommit

__DB.getAutoCommit() : boolean__

````
Retrieves the current database connection auto-commit flag state.
````
### DB.getConnect

__DB.getConnect() : JavaObject__

````
Returns a Java database connection.
````
### DB.getStatements

__DB.getStatements() : Array__

````
Returns the current list of database prepared statements that weren't closed it. Do close them, as soon as possible, using the DB.closeStatement or DB.closeAllStatements functions.
````
### DB.h2StartServer

__DB.h2StartServer(aPort, aListOfArguments) : String__

````
Starts a H2 server on aPort (if provided) with an array of arguments (supported options are:  -tcpPort, -tcpSSL, -tcpPassword, -tcpAllowOthers, -tcpDaemon, -trace, -ifExists, -baseDir, -key). After creating the access URL will be returned. In case of error an exception will be thrown.
````
### DB.h2StopServer

__DB.h2StopServer()__

````
Stops a H2 server started for this DB instance.
````
### DB.q

__DB.q(aQuery) : Map__

````
Executes the SQL query provided in aQuery on the current DB connection. It returns a Map with a results array where each element corresponds to one row. In case of error an exception will be thrown.
````
### DB.qLob

__DB.qLob(aSQL) : Object__

````
Executes aSQL on the current DB object returning only the first row and column. If that column is a CLOB a string is returned; if it is a BLOB a byte array is provided. Errors will raise an exception.
````
### DB.qs

__DB.qs(aQuery, arrayOfBindVariables, keepStatement) : Map__

````
Performs aQuery (SQL) on the current DB object instance using the bind variables from the arrayOfBindVariables. It returns a Map with a results array that will have an element per result set line. In case of error an  exception will be thrown. Optionally you can specify to keepStatement (e.g. boolean) to keep from closing the prepared statement used for reuse in another qs call. If you specify to use keepStatement do close this query, as soon as possible, using DB.closeStatement(aQuery) (where you provide an exactly equal statement to  aQuery) or DB.closeAllStatements.
````
### DB.qsRS

__DB.qsRS(aQuery, arrayOfBindVariables) : Map__

````
Performs aQuery (SQL) on the current DB object instance using the bind variables from the arrayOfBindVariables. It returns a java ResultSet object that should be closed after use. In case of error an  exception will be thrown. If you specify to use keepStatement do close this query, as soon as possible, using DB.closeStatement(aQuery) (where you provide an exactly equal statement to  aQuery) or DB.closeAllStatements.
````
### DB.rollback

__DB.rollback(dontIgnoreError)__

````
Rollbacks the current database session on the current DB object instance. In case of error an exception will be thrown if dontIgnoreError = true
````
### DB.setAutoCommit

__DB.setAutoCommit(aFlag)__

````
Sets to true or false (defaults to false) the current database connection auto-commit.
````
### DB.u

__DB.u(aSQL) : Number__

````
Executes a SQL statement on the current DB object instance. On success it will return the number of rows affected. In case of error an exception will be thrown.
````
### DB.uLob

__DB.uLob(aSQL, aLOB) : Number__

````
Executes a SQL statement on the current DB object instance to update a CLOB or BLOB provided in aLOB. On success it will return the number of rows affected. In case of error an exception will be thrown.
````
### DB.uLobs

__DB.uLobs(aSQL, anArray) : Number__

````
Executes a SQL statement on the current DB object instance that can have CLOB or BLOB bind variables that can be specified on anArray. On success it will return the number of rows affected. In case of error an exception will be thrown.
````
### DB.us

__DB.us(aSQL, anArray, keepStatement) : Number__

````
Executes a SQL statement on the current DB object instance that can have bind variables that  can be specified on anArray. On success it will return the number of rows affected. In case of error an exception will be thrown. Optionally you can specify to keepStatement (e.g. boolean) to keep from closing the prepared statement used for reuse in another us call. If you specify to use keepStatement do close this query, as soon as possible, using DB.closeStatement(aQuery) (where you provide an exactly equal statement to  aQuery) or DB.closeAllStatements.
````
### DB.usArray

__DB.usArray(aSQL, anArrayOfArrays, aBatchSize, keepStatement) : Number__

````
Executes, and commits, a batch of a SQL statement on the current DB object instance that can have bind variables that  can be specified on an array, for each record, as part of anArrayOfArrays. On success it will return the number of rows  affected. In case of error an exception will be thrown. Optionally you can specify to keepStatement (e.g. boolean) to keep from closing the prepared statement used for reuse in another usArray call. If you specify to use keepStatement do close this query, as soon as possible, using DB.closeStatement(aQuery) (where you provide an exactly equal statement to  aQuery) or DB.closeAllStatements. You can also specify aBatchSize (default is 1000) to indicate when a commit should be performed while executing aSQL for each array of bind variables in anArrayOfArrays.

Example:

var values = [ [1,2], [2,2], [3,3], [4,5]];
db.usArray("INSERT INTO A (c1, c2) VALUES (?, ?)", values, 2);


````
