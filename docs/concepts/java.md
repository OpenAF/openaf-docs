---
layout: default
title: Java support
parent: Concepts
grand_parent: OpenAF docs
---

# Java support

## Creating an object instance

Java is supported directly on the OpenAF javascript language. Simply:

````javascript
var str = new java.lang.String("hello world");
java.lang.System.out.println(str);
// hello world
````

In this example the _"hello world"_ string is actually a Javascript string which got converted to the _String_ parameter of the java.lang.String constructor. The newly created java instance was stored in the javascript variable _str_. Then, on the next line, _str_ was used as a parameter to the _println_ method of _java.lang.System.out_.

> Note: if the package if different from _java_ or _javax_ you can use ````Packages.my.package.MyClass```` as long as it's available on the classpath. To dynamically add classes to the classpath see [loadExternalJars](#loadexternaljars).

## Using an object instance

After creating an object instance you can call it's methods directly:

````javascript
var f = new java.io.File("test.txt");
f.exists()
// false
f.getName()
// test.txt
````

If you use _Object.keys_ over the object instance you will get an array of methods and properties:

````javascript
Object.keys(f)
// [
//   "getClass",
//   "parent",
//   "renameTo",
//   "getName",
// ...
````

> Note: You can even use it with ````for(i in f) { ... }```` for example.

### Choosing a specific method signature

In some cases a Java instance might have more than on method with the same name but different signature (e.g. different methods). In those cases it's possible to indicate one of them by calling the method like this:

```javascript
f['list(java.lang.String,com.some.options.Options$ListOption[])'](arg1, arg2)
```

## Implementing Java interfaces

It's also possible to provide a Java inteface implementation directly in Javascript:

````javascript
// Implementing the Runnable interface
var r = new java.lang.Runnable({
    run: function() {
        print("Hello World");
    }
});

// Providing the custom implementation to the Thread constructor
var t = new java.lang.Thread(r);
// Starting the thread
t.start()

// Hello World
````

## JavaImporter constructor

You can also build a javascript object that embeds access to other Java packages:

````javascript
var other = JavaImporter(java.lang.String, java.io.File);

with(other) {
    var s = new String("abc");
    var f = new File("text.txt");
}
````

## Java Exceptions

Java exceptions will be thrown as javascript exceptions and can be caught using the usual _try...catch_. To access the original Java exception object you can use the _javaException_ field:

````javascript
try {
    java.lang.Class.forName("NonExistingClass");
} catch(e) {
    if (e.javaException instanceof java.lang.ClassNotFoundException) {
       print("Class not found");
    }
}
````

It even support conditional catch:

````javascript
try {
    return java.lang.Class.forName(name);
} catch (e if e.javaException instanceof java.lang.ClassNotFoundException) {
    print("Class " + name + " not found");
} catch (e if e.javaException instanceof java.lang.NullPointerException) {
    print("Class name is null");
}
````

## OpenAF specific Java helpers

Overtime some Java helper functions were added to OpenAF.

### loadExternalJars

When OpenAF is executed with it's custom Java class loader (default on generated scripts) it's able to dynamically load classes and JAR files from the filesystem:

````javascript
loadExternalJars("libs/jars");
var o = new Packages.com.my.special.Object();
````

> Note: you can also use ````af.externalAddClasspath("file:/my/own/bin/dir")````

### newJavaArray

Creates a new Java Array object for the Java class type provided with a corresponding size:

````javascript
var ar1 = newJavaArray(java.lang.String, 5);        // non-native type
var ar2 = newJavaArray(java.lang.Integer.TYPE, 2);  // native type
````

### AF.fromJavaArray

Given a Java array object it will try to convert it into a true javascript array (where each array element might or not be a Java object):

````javascript
var ar = AF.fromJavaArray( java.lang.System.getProperties() );
````

### javaRegExp

Java regular expressions are actually more "complete" than JavaScript. So it makes sense to sometimes use them:

````javascript
// Verify that the last name is repeated.

javaRegExp("My name is Bond, James Bond").test("(\\w+), (\\w+) (\\1)", "g");
// true
````

You can also use the Java method equivalents of _match, matchAll, preCompile, removePreCompiled, replace, replaceAll, split_ and _test_.

### isJavaException

Test if a variable contains a Java exception:

````javascript
var e = new java.lang.Exception("hups!");
isJavaException(e);
// true
````

### isJavaObject

Test if a variable contains a Java object instance:

````javascript
var o = new java.lang.String("hups!");
isJavaObject(o);
// true
````

### getJavaStackTrace

Given a javascript exception if it derives from a Java exception it will convert it to a javascript array:

````javascript
try {
    java.lang.Integer.parseInt(22.2)
} catch(e) {
    sprint( getJavaStackTrace(e) )
}
// [
//   {
//     "moduleName": "java.base",
//     "moduleVersion": , "11.0.12",
//     "qclassLoaderName": null,
//     "className": "java.lang.Number.FormatException",
//     "methodName": "forInputString",
//  ...
````

## Compiling OpenAF javascript into Java classes

For performance reasons you can compile OpenAF javascript code into a Java class. This is actually performed automatically in OpenAF for commonly used pieces of javascript code (e.g. included libraries, opack based libraries, etc...)

````javascript
af.compileToClasses("HelloWorld", "print('hello world!');", ".");
// Generated HelloWorld.class

af.runFromExternalClass("HelloWorld", ".");
// hello world!

af.compileToClasses("MyCode", "var myCode = 'my code!!!';", ".");
af.runFromExternalClass("MyCode", ".");
print(myCode);
// my code!!!
````

## Other useful OpenAF functions

There are other useful OpenAF javascript functions like:

````javascript
ow.loadFormat();  // Load the format wrapper

ow.format.getJavaHome()
ow.format.getJavaVersion()

ow.loadJava(); // Load the java wrapper

ow.java.gc                 // Invoking the garbage collector
ow.java.getMemory          // Get the current runtime max, total, used and free heap memory
ow.java.getClassVersion    // Given a byte array of a Java class will return the minimum JVM version required to load the class.
ow.java.getJarVersion      // Given a JAR file will return an array with the JVM versions used in the java classes contained.
ow.java.IMAP.*             // Accessing IMAP functionality
````

### ow.java.cipher

A wrapper around creating, reading and using symetric and asymmetric keys in Java for encrypting, decrypting and signing (see more in [Encrypt/Decrypt with public and privated keys](https://docs.openaf.io/docs/guides/beginner/encrypt-decrypt-with-pubpriv-keys)).

### Ignoring SSL domain verification

It also includes disabling SSL domain verification. See more in [easily add SSL certificates](https://docs.openaf.io/docs/guides/advanced/easily-add-ssl-cert.html#ignoring-the-ssl-domain-validation).
