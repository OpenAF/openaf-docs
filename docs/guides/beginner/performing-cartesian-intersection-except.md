---
layout: default
title: Performing cartesian product, intersection and except over two arrays
parent: Beginner
grand_parent: Guides
---

# Performing cartesian product, intersection and except over two arrays

The helper [_$from_](../../concepts/OpenAF-nLinq.md) simplifies the handling of an array of maps but it can also help performing functions with other arrays of maps namely for a cartesian product, intersection and except operations.

## Defining two sets of values

Let's start be defining two arrays of maps. A first set of values composed of maps with a _x_ value and a _y_ value:

````javascript
var a = [
    { x: 1, y: -1 },
    { x: 2, y: -1 }
]
````
And a second set of values where one entry is also present on the first set of values:

````javascript
var b = [
    { x: 1, y: 1 },
    { x: 2, y: 2 },
    { x: 2, y: -1 }
]
````

You can check the size of each (#2 for _a_ and #3 for _b_):

````javascript
{% raw %}
tprint("size of a = {{sizeA}} | size of b = {{sizeB}}", { sizeA: $from(a).count(), sizeB: $from(b).count() })
{% endraw %}
````

## Performing an intersection

To perform a intersection between _a_ and _b_ simply execute:

````javascript
var c = $from(a).intersect(b).select()
````

The result will be a new set _c_ with 1 element (x: 2 and y: -1):

````javascript
printTable(c)
````

## Performing an exception

To obtain the exception between _a_ and _b_ simple execute:

````javascript
var c = $from(a).except(b).select()
````

The result will be 1 element (excluding the common element between _a_ and _b_):

````javascript
printTable(c)
````

## Performing a cartersian product

A cartesian product between one set and another set will combine each element of the first set with all elements of other set. To better visualize let's create a third set _z_:

````javascript
var z = [
    { z: 1 },
    { z: -1 }
]
````

Now let's execute the cartesian product between _a_ and _z_:

````javascript
var c = $from(a).cartesian(z).select()
````

The result will be a new set _c_ with 4 elements:

| x | y | z |
|---|---|---|
| 1 | -1 | 1 |
| 1 | -1 | -1 |
| 2 | -1 | 1 |
| 2 | -1 | -1 |

````javascript
printTable(c)
````
