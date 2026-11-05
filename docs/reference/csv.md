---
layout: default
title: csv
parent: Reference
grand_parent: OpenAF docs
---

{% raw %}
## csv

[Source: `06414cd9`](https://github.com/OpenAF/openaf/blob/06414cd9204e918daa1e2971ce904783299db333/src/openaf/core/CSV.java) · [Baseline](../source-snapshot.md)

### CSV.CSV

`CSV.CSV(aCsvString)`

````text
Creates a new instance of the CSV object. Optionally you can provide a string that contains a CSV.
````

### CSV.clear

`CSV.clear()`

````text
Clears all internal structures. This will clear all data stored previously in this instance.
````

### CSV.csv

`CSV.csv() : Array`

````text
Returns a javascript array of maps with the current internal CSV representation.
````

### CSV.fromCSV

`CSV.fromCSV(aCSVString)`

````text
Tries to convert aCSVString into an internal csv format.
````

### CSV.fromStream

`CSV.fromStream(aStream, aFunction)`

````text
Tries to read a CSV from aStream a calls aFunction with a map representing the fields of each line. The format is determined by CSV.setStreamFormat and each map entry will have either the number of the field or the corresponding name depending on the header options.
````

### CSV.readFile

`CSV.readFile(aFilename) : Number`

````text
Tries to read aFilename into the internal CSV representation. If successful the number of read lines will be returned. Otherwise an exception will be raised.
````

### CSV.setSeparator

`CSV.setSeparator(aSeparator)`

````text
Sets the default separator to use when building a CSV output (default is ;)
````

### CSV.setStreamFormat

`CSV.setStreamFormat(aMap)`

Set the options that will be used with CSV.fromStream. Available options are:

- `format` (String)
  You can choose between DEFAULT, EXCEL, INFORMIX_UNLOAD, INFORMIX_UNLOAD_CSV, MYSQL, RFC4180, ORACLE, POSTGRESQL_CSV, POSTGRESQL_TEXT and TDF (please check http://commons.apache.org/proper/commons-csv/user-guide.html)
- `withHeader` (Boolean)
  Tries to automatically use the available header
- `withHeaders` (Array)
  An array of header strings in the order that data lines will appear.
- `quoteMode` (String)
  You can choose between ALL, ALL_NON_NULL, MINIMAL, NON_NUMERIC and NONE.
- `withDelimiter` (String)
  A single character as a custom delimiter
- `withEscape` (String)
  A single character as a custom escape
- `withNullString` (String)

### CSV.setStringDelimiter

`CSV.setStringDelimiter(aDelimiter)`

````text
Sets the default string delimited to use when building a CSV output (default is ")
````

### CSV.toCsv

`CSV.toCsv(anArrayOfMaps, anArrayOfKeys)`

Tries to convert a javascript `anArrayOfMaps` into an internal csv format. The array should be composed of
maps whose elements must have the same keys (example: `[ { "F1": 1, "F2": abc}, { "F1": 2, "F2": xyz } ]`).
Optionally `anArrayOfKeys` can be provided to restrict the keys used and to force their order.

### CSV.toStream

`CSV.toStream(aStream, aFunction)`

````text
Tries to write a CSV to aStream calling aFunction and expecting it to return a map with the fields previously set with CSV.setStreamFormat and corresponding values for each line (each call will represent a line). The fields need to be specificed in withHeaders map property in CSV.setStreamFormat. The aFunction will be called continuosly until a different output from a map is returned. Note: aStream won't be closed.
````

### CSV.w

`CSV.w() : String`

````text
Returns the current CSV internal representation in the form of a string.
````

### CSV.writeFile

`CSV.writeFile(aFilename) : Number`

````text
Tries to write the internal CSV representation into aFilename. If successful it will return the number of lines written, otherwise an exception will be raised.
````
{% endraw %}
