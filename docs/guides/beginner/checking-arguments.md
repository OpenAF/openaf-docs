---
layout: default
title: Checking arguments
parent: Beginner
grand_parent: Guides
---

# Checking arguments

In OpenAF whenever you built a simple function, or you have a piece of code on a oJob that expects arguments or any code block you will eventually need to ensure the type of the input variables/arguments and enforce mandatory arguments.

Let's say that you build a function to add two values and return a verbose result. It receives arguments a and b that must be numbers, but if b is not provided it assumes 0. Argument c should be a string and if not provided a default value is provided. All this in plain javascript is:

````javascript
function sum(a, b, c) {
    if (typeof a != "number") throw "a needs to be a number";
    if (typeof b == "undefined") b = 0;
    if (typeof b != "number") throw "b needs to be a number";
    if (typeof c == "undefined") c = "the result is ";
    if (typeof c != "string") throw "c needs to be a string";

    return c + String(a + b);
}
````

If you inspect it carefully you need to have the "if" statements in the right order to achieve the intended result. The more arguments you have the harder to read.

OpenAF as a shortcut to help with readability. It's not intended to be like TypeScript but just a small helper for OpenAF scripting. So the previous function would look like this with these OpenAF shortcuts:

````javascript
function sum(a, b, c) {
    _$(a, "a").isNumber().$_();

    b = _$(b, "b").isNumber().default(0);
    c = _$(c, "c").isString().default("the result is ");

    return c + String(a + b);
}
````

Each declaration starts always with _\_$(variable, stringName)_. The _stringName_ is actually optional if you want to become "more verbose" (you will see how in a second).

The declaration is then followed by conditions like _isNumber_ and _isString_. You can provide an argument to each of these "conditions" to have more verbose exceptions than _"a needs to be a number."_.

The declaration ends with _default(aValue)_ or _$\_(stringName)_. If no value is provided _default_ will ensure that the variable will always default to some value while _$\__ doesn't return any value but will throw an exception indicating that the variable value wasn't provided.

So a more verbose type checking could be:

````javascript
function sum(a, b, c) {
    _$(a).isNumber("The argument 'a' needs to be a number.").$_("The argument 'a' is mandatory for the sum function.");

    b = _$(b).isNumber("The argument 'b', if defined, must be a number.").default(0);
    c = _$(c).isString("The argument 'c', if defined, must be a string.").default("the result is ");

    return c + String(a + b);
}
````

You can see the list of all available conditions by executing _desc \_$()_ on an openaf-console.
