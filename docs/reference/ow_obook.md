---
layout: default
title: ow.obook
parent: Reference
grand_parent: OpenAF docs
---

{% raw %}
## ow.obook

[Source: `06414cd9`](https://github.com/OpenAF/openaf/blob/06414cd9204e918daa1e2971ce904783299db333/js/owrap.oBook.js) · [Baseline](../source-snapshot.md)

### obook

`obook(aBook, exitOnEnd)`

````text
Convenience function to create and start an interactive oBook tutorial in the OpenAF console. aBook can be a file path to a markdown file or an inline markdown string. If exitOnEnd is true the process exits when the user reaches the end of the book. Sets up the watchLine/watchCommand hooks required for console integration.
````

### ow.oBook.book

`ow.oBook.book(aBook, exitOnEnd)`

`````text
Creates an interactive tutorial book from aBook, which can be a file path to a markdown file or a markdown string. The book alternates text sections with fenced ````javascript code blocks that the user can copy or execute interactively at the OpenAF console. If exitOnEnd is true the process exits when the last page is acknowledged.
`````

### ow.oBook.book.bookEnd

`ow.oBook.book.bookEnd()`

````text
Prints the oBook end banner and stops the watchLine/watchCommand loop. If exitOnEnd was set to true at construction time the process exits with code 0.
````

### ow.oBook.book.bookStart

`ow.oBook.book.bookStart()`

````text
Prints the oBook start banner. Called once before the first page is shown.
````

### ow.oBook.book.interaction

`ow.oBook.book.interaction()`

````text
Handles a single console interaction tick. On the first call the first page is shown. On subsequent calls it reads a key press: Enter/Space advances, Up/Down navigate, Ctrl+U exits to the console, 'q' or Escape quits. This method is called repeatedly via the watchLine mechanism when the book is running inside the OpenAF console.
````

### ow.oBook.book.parse

`ow.oBook.book.parse()`

`````````text
Parses the book string splitting it into alternating text/code sections using ````javascript and ```````` fenced block markers. Any *requires pkg >= version* directives at the top of the book are processed via includeOPack(). The resulting structure is stored in this.struct.
`````````

### ow.oBook.book.printPart

`ow.oBook.book.printPart(partId)`

````text
Renders the book section at index partId (0-based) including the progress indicator, the markdown text and any associated code block. When the code is multiline it is printed for copy-paste; when it is a single line it is written directly into the console input buffer.
````
{% endraw %}
