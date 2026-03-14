---
layout: default
title: How To - Use ask functions
parent: How To
grand_parent: OpenAF docs
---
# How to - Use ask functions

_applies to version >= 20201111_

When running OpenAF scripts it's possible to "ask" for user input. This can be achieve using one of four functions:

| Function | Description |
|----------|-------------|
| ask | Asks for an entire input line optionally masking with a char (e.g. masking with '*' all characters). |
| ask1 | Asks for just a single key of input from a list of possible key values. | 
| askChoose | Displays a scrollable list of choices for the user to choose one (since version >= 20231222) |
| askEncrypt | Asks for user input to produce an encrypted string. |
| askN | Asks for multi-line input providing a function to decide each lien prompt and a stop function to decide when the input is finished. |  

## Using 'ask'

Asking a question to the user:

````javascript
> var result = ask("What's your name? ");
What's your name? Scott Tiger
> print(result)
Scott Tiger
````

Asking for a question with a secret answer:

````javascript
> var result = ask("What's your password? ", "*");
What's your password? **********
> print(result)
MyPassword
````

## Using 'ask1'

Asking for a confirmation from the user:

````javascript
> var result = ask1("Do you want to continue (y/n)?", "ynYN"); print(result);
Do you want to continue? (y/n)> n
> result = String(result).toLowerCase();
> if (result.toLowerCase() == "n") { 
|    print("stopping....)    
| }
````

## Using 'askEncrypt'

This is the same as the function 'ask' but avoiding to echo any input and returning the encrypted format.

````javascript
> var result = askEncrypt("Password: ");
Password:
> print(result);
74D685B4A77E691819C3194BC55B0AA240EF2C918D386027EE1CB645D67AF9B8
````

## Using 'askN'

Asking for a multi-line input:

````javascript
> var result = askN(() => "| ", v => v.endsWith("\n\n"));
| first line
| second line
|
> print(result)
first line
second line


>
````

## Using 'askChoose'

> Available on versions >= 20231222

Asking a choice within a list of possible choices:

```javascript
var result = askChoose("Do you want to proceed?", [ 'Yes', 'No' ])
? Do you want to proceed?
> Yes
  No
[...]
✓ Do you want to proceed?[Yes]
> print(result)
0
```

With more choices but just showing 3:

```javascript
> var result = askChoose("Which configuration you want to use?", [ 'Config 1', 'Config 2', 'Config 3', 'Config 4', 'Config 5' ], 3)
? Which configuration you want to use?
> Config 1
  Config 2
v Config 3
[...]
? Which configuration you want to use?
^ Config 2
  Config 3
> Config 4
[...]
✓ Which configuration you want to use?[Config 4]
> print(result)
3
```

### Cancellation support

`askChoose` and `askChooseMultiple` support **cancellation** via Ctrl+C. When the user presses Ctrl+C, the function returns `undefined` instead of throwing an exception, allowing scripts to handle the cancellation gracefully:

```javascript
var result = askChoose("Pick an option:", ["Option A", "Option B", "Option C"])
if (!isDef(result)) {
  print("Selection cancelled by user.")
} else {
  print("Selected index: " + result)
}
```

Navigation within the list was also improved to support circular scrolling (wrapping from last to first entry and vice versa).