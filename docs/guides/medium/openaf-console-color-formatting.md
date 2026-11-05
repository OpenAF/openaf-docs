---
layout: default
title: OpenAF-console color formatting
parent: Medium
grand_parent: Guides
---

# OpenAF-console color formatting

When using the OpenAF-console if the terminal is ANSI capable some of the output will be "colored" to improve readability:

![color-syntax-1](color-syntax-1.png)

But the same on dark mode might be harder to read:

![color-syntax-2](color-syntax-2.png)

The current colors used in the OpenAF are defined in the internal variable "__colorFormat":

````javascript
> __colorFormat
{
  "key": "BOLD,BLACK",
  "number": "GREEN",
  "string": "CYAN",
  "boolean": "RED",
  "default": "YELLOW"
}
````

You can check all the available attributes & colors executing "help ansiColor". You can change any color directly on the __colorFormat map. If you want to make your changes permanent you can add them to the ~/.openaf-console_profile file.

So let's change and see the diference:

````javascript
> __colorFormat.key = "BOLD,WHITE"
````

![color-syntax-3](color-syntax-3.png)

Much easier to read. Of course, it all depends on your personal preferences:

````json
{
  "key": "UNDERLINE,WHITE",
  "number": "BG_WHITE,GREEN",
  "string": "BG_WHITE,BLUE",
  "boolean": "BG_WHITE,RED",
  "default": "BG_WHITE,YELLOW"
}
````

![color-syntax-4](color-syntax-4.png)
