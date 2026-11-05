---
layout: default
title: Format bytes abbreviation
parent: Beginner
grand_parent: Guides
---

# Format bytes abbreviation

Whenever dealing with bytes you might want to output an abbreviation for human reading like instead of saying 123456789 bytes saying it's around 118MB. You can do this in OpenAF using the ow.format.toBytesAbbreviation function like this:

````javascript
ow.loadFormat();

var folderPath = ".";
var sumBytes = ow.format.toBytesAbbreviation(
                 $from( io.listFiles(folderPath).files).sum("size")
               );

print(sumBytes);
````

In this example it will sum all the byte sizes of a given folder and print you the corresponding abbreviation in bytes.

Other examples:

````javascript
> ow.format.toBytesAbbreviation(10)
10 bytes
> ow.format.toBytesAbbreviation(10000)
9.77 KB
> ow.format.toBytesAbbreviation(10000000000000)
9.09 TB
````
