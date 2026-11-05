---
layout: default
title: Get a javascript array from an Excel
parent: Beginner
grand_parent: Guides
---

# Get a javascript array from an Excel

In the same way you can [write a javascript array to an Excel](adding-an-array-to-an-excel-spreadsheet.md) it's equally easy to retrieve a javascript array from an existing Excel. Let's take this excel sheet as an example (from test.xlsx):

![get-a-javascript-array-from-an-excel](get-a-javascript-array-from-an-excel.png)

To convert it to a javascript array just create the following OpenAF script (test.js):

````javascript
plugin("XLS");
var xls = new XLS("test.xlsx");
var sheet = xls.getSheet("Sheet1");
// The second boolean parameter determines if formulas should be evaluated
var myArray = xls.getTable(sheet, true, "B", 3).table;

sprint(myArray);
````

And execute it:

````bash
openaf -f test.js
````

The result will be:

````javscript
[
  {
    "ID": 1,
    "Description": "Test 1",
    "Value": 123
  },
  {
    "ID": 2,
    "Description": "Test 2",
    "Value": 321
  },
  {
    "ID": 3,
    "Description": "Test 3",
    "Value": 456
  },
  {
    "ID": 4,
    "Description": "Test 4",
    "Value": 654
  }
]
````
