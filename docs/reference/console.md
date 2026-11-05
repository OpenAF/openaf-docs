---
layout: default
title: console
parent: Reference
grand_parent: OpenAF docs
---

{% raw %}
## console

[Source: `06414cd9`](https://github.com/OpenAF/openaf/blob/06414cd9204e918daa1e2971ce904783299db333/src/openaf/plugins/Console.java) · [Baseline](../source-snapshot.md)

### Console.console

`Console.console()`

````text
Creates a new instance of the object Console.
````

### Console.getConsoleReader

`Console.getConsoleReader() : ConsoleReader`

````text
Returns the internal ConsoleReader java object.
````

### Console.isAnsiSupported

`Console.isAnsiSupported() : boolean`

````text
Determines if the console is able to support ansi (returns true) or not (returns false).
````

### Console.readChar

`Console.readChar(allowed) : char`

````text
Read a character from the console. If allowed is provided only the characters on the string allowed will be considered.
````

### Console.readCharB

`Console.readCharB() : int`

````text
Low level character read from console with waiting. Will return -1 - EOF or -2 - No character available or the available character
````

### Console.readCharNB

`Console.readCharNB() : number`

````text
Low level character read from the console with no waiting. Will return -1 for EOF or -2 for No character available or the available character
````

### Console.readLine

`Console.readLine(aMaskchar) : String`

````text
Read a line from the console. Will provide a mask for introduction of passwords if aMaskchar is provided. Returns the line read. NOTE: Use Console.readLinePrompt if you are using a prompt.
````

### Console.readLinePrompt

`Console.readLinePrompt(aPrompt, aMaskchar) : String`

````text
Read a line from the console providing aPrompt. Will provide a mask for introduction of passwords if aMaskchar is provided. Returns the line read. NOTE: Use this method instead of Console.readLine if you are using a prompt
````
{% endraw %}
