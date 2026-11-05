---
layout: default
title: afbase
parent: Reference
grand_parent: OpenAF docs
---

{% raw %}
## afbase

[Source: `06414cd9`](https://github.com/OpenAF/openaf/blob/06414cd9204e918daa1e2971ce904783299db333/src/openaf/AFBase.java) · [Baseline](../source-snapshot.md)

### af.compile

`af.compile(aScriptString, aSourceName) : Object`

````text
Compiles the aScriptString executing it and returning the corresponding result.  Optionally you can provide aSourceName.
````

### af.compileToClasses

`af.compileToClasses(aClassfile, aScriptString, aPath)`

Given `aClassfile` name, `aScriptString` and, optionally, a filesystem `aPath` it will generate Java bytecode
as result of compiling the `aScriptString` into a filesystem `aClassfile` (on the provided `aPath`). Example:

```javascript
af.compileToClasses("SomeClass", "print('hello world!');", "/some/path")
```

### af.compileToJar

`af.compileToJar(aClassfile, aScriptString, aJarFile)`

Given `aClassfile` name and `aScriptString` it will generate Java bytecode as a result of compiling
`aScriptString`, writing every generated class as a single entry into `aJarFile` instead of one loose
.class file per class (see `af.compileToClasses`). `aJarFile` is written to a temporary file next to
it and then moved into place, so a failed compile never leaves a partial/corrupt jar behind; the
class can then be loaded with `af.externalClass`/`af.runFromExternalClass` pointed at `aJarFile`
directly (a URLClassLoader treats a jar file URL the same as a directory URL). Example:

```javascript
af.compileToJar("SomeClass", "print('hello world!');", "/some/path/SomeClass.jar")
```

### af.cp

`af.cp(aSourceFilePath, aTargetFilePath)`

````text
Tries to copy aSourceFilePath to aTargetFilePath preserving file attributes.
````

### af.create2FACredentials

`af.create2FACredentials(anAccountName, anIssuer) : Map`

````text
Given anAccountName and anIssuer will create a the 2FA/TOTP (Time-Based One-Time Password) returning a map with the scratchCodes, the verificationCode, the key, the openaf encryptedKey, the QR code URL  and the OTP URL.
````

### af.crypt

`af.crypt(aKey, aSalt) : String`

````text
Tries to mimic crypt(3) password encryption using the org.apache.commons.codec.digest.Crypt.crypt function. Please check https://commons.apache.org/proper/commons-codec/apidocs/org/apache/commons/codec/digest/Crypt.html for more. Use af.randomCryptSalt() to generate a random salt if necessary.
````

### af.decrypt

`af.decrypt(aString, aKey) : String`

````text
Decrypts the provided aString with the provided aKey.
````

### af.decryptBytes

`af.decryptBytes(anArrayOfBytes, aKey) : anArrayOfBytes`

````text
Decrypts the provided anArrayOfBytes (with the IV in the last 16 bytes) using AES/CBC/PKCS5PADDING. If aKey is provided it will decrypt using it.
````

### af.decryptBytes2String

`af.decryptBytes2String(anArrayOfBytes, aKey) : String`

````text
Decrypts the provided anArrayOfBytes (with the IV in the last 16 bytes) using AES/CBC/PKCS5PADDING and returns the result as a String. If aKey is provided it will decrypt using it.
````

### af.decryptBytesIfPossible

`af.decryptBytesIfPossible(anArrayOfBytes, aKey) : anArrayOfBytes`

````text
Tries to decrypt anArrayOfBytes using the provided aKey (or the default key if not provided). If decryption fails, returns the original bytes unchanged.
````

### af.e

`af.e(aString)`

````text
Outputs to stderr aString ending with a newline.
````

### af.encrypt

`af.encrypt(aString, aKey) : String`

````text
Encrypts the provided aString as password for most of the OpenAF password functionality. If aKey is provided it will encrypt using it.
````

### af.encryptBytes

`af.encryptBytes(anArrayOfBytes, aKey) : anArrayOfBytes`

````text
Encrypts the provided anArrayOfBytes using AES/CBC/PKCS5PADDING. If aKey is provided it will encrypt using it. Returns the encrypted bytes with the IV appended at the end (last 16 bytes).
````

### af.encryptString2Bytes

`af.encryptString2Bytes(aString, aKey) : anArrayOfBytes`

````text
Encrypts the provided aString using AES/CBC/PKCS5PADDING and returns the encrypted bytes with the IV appended at the end (last 16 bytes). If aKey is provided it will encrypt using it.
````

### af.enl

`af.enl(aString)`

````text
Outputs to stderr aString without a newline on the end.
````

### af.eval

`af.eval(aScript) : Object`

````text
Performs the equivalent version of the javascript eval function for the provided aScript. Returns  the corresponding result of the evaluation.
````

### af.externalAddClasspath

`af.externalAddClasspath(aURL)`

Tries to add `aURL` to the current classpath. Don't forget that directories must end with a '/', for
example: `file:/my/own/dir/`

Note: This might not work for some JVMs.

### af.externalClass

`af.externalClass(anArrayOfClasspathEntries, aClassName) : JavaClass`

````text
Returns an external Java class with the aClassName, not included in the initial OpenAF's classpath, loaded from a list of jars/folders in anArrayOfClasspathEntries.
````

### af.externalClassLoader

`af.externalClassLoader(anArrayOfClasspathEntries) : ClassLoader`

````text
Returns a ClassLoader suitable to be use with af.getClass to dynamically load Java classes that weren't included  on the initial OpenAF's classpath and are included in the jars/folders provided in anArrayOfClasspathEntries.
````

### af.externalPlugin

`af.externalPlugin(anArrayOfClasspathEntries, aPluginClass)`

````text
Loads a OpenAF's plugin identified by the aPluginClass that isn't available in the initial OpenAF's classpath, loaded from a list of jars/folders in anArrayOfClasspathEntries.
````

### af.fromArray2Bytes

`af.fromArray2Bytes(anArray) : anArrayOfBytes`

````text
Converts a javascript array of integers into a Java anArrayOfBytes.
````

### af.fromBase64

`af.fromBase64(aBase) : anArrayOfBytes`

````text
Decodes aBase, a Base64 string or array of bytes, into the original array of bytes.
````

### af.fromBase64Stream

`af.fromBase64Stream(aInputStream, aOutputStream, shouldNotClose)`

Decodes Base64 using the same lenient decoding as af.fromBase64, copying Java streams with bounded memory.
Both streams close on success or processing failure unless `shouldNotClose` is true
(default false). Successful conversion finalizes and flushes output even when left open.
Invalid arguments are rejected before reading or closing streams. Errors propagate and
may leave partial output; cleanup errors are suppressed behind the original error.
Returns undefined. For example:

```javascript
af.fromBase64Stream(io.readFileStream("B.b64"), io.writeFileStream("A.decoded"));
```

### af.fromBytes2Array

`af.fromBytes2Array(anArrayOfBytes) : Array`

````text
Converts a Java anArrayOfBytes into a javascript array of integers with the value representation of  each byte.
````

### af.fromBytes2InputStream

`af.fromBytes2InputStream(anArrayOfBytes) : Stream`

````text
Converts anArrayOfBytes into a ByteArrayInputStream.
````

### af.fromBytes2OutputStream

`af.fromBytes2OutputStream(anArrayOfBytes) : Stream`

Converts `anArrayOfBytes` into a ByteArrayOutputStream. After using this stream you can, for example, use
`toString` and `toByteArray` methods from the resulting stream.

### af.fromBytes2String

`af.fromBytes2String(anArrayOfBytes, anEncoding) : aString`

````text
Converts anArrayOfBytes into a string, optionally with the provided anEncoding.
````

### af.fromInputStream2Bytes

`af.fromInputStream2Bytes(aStream) : anArrayOfBytes`

````text

````

### af.fromInputStream2String

`af.fromInputStream2String(aStream, anEncoding) : String`

````text
Tries to convert an input aStream into a String.
````

### af.fromJavaMap

`af.fromJavaMap(JavaMap) : Map`

````text
Converts a Java Map to a JavaScript Object.
````

### af.fromString2Bytes

`af.fromString2Bytes(aString, anEncoding) : anArrayOfBytes`

````text
Converts aString into anArrayOfBytes, optionally with the provided anEncoding.
````

### af.fromString2InputStream

`af.fromString2InputStream(aString, anEncoding) : Stream`

````text
Converts aString into a ByteArrayInputStream.
````

### af.fromString2OutputStream

`af.fromString2OutputStream(aString, encoding) : Stream`

Converts `aString` into a ByteArrayOutputStream. After using this stream you can, for example, use
`toString` and `toByteArray` methods from the resulting stream.

### af.fromTOONJava

`af.fromTOONJava(aTOONStr) : Object`

````text
Tries to parse aTOONStr into a javascript object using the native Java TOON engine (json-io) instead of the bundled Javascript one. See __flags.ALTERNATIVES.fromTOON.
````

### af.fromXML

`af.fromXML(aXMLObject) : aString`

````text
Converts aXMLObject (E4X) into a String. Warning: beware that E4X is an obsolete object.
````

### af.get2FAToken

`af.get2FAToken(aKey, aSpecificTime) : String`

````text
Given 2FA aKey it will return the current token. Note: it will use the current date/time of the system so it must be in sync with the authenticator. Optionally you can provide aSpecificTime.
````

### af.getClass

`af.getClass(aName, aLoader) : JavaClass`

````text
Returns the JavaClass object the Java class identified by aName. Optionally you can provide a Java classloader ( this can be the result of using af.externalClassLoader).
````

### af.getDistribution

`af.getDistribution() : String`

````text
Returns the current OpenAF's distribution channel.
````

### af.getOpenAFJar

`af.getOpenAFJar() : String`

````text
Retrives the fullpath for the OpenAF jar.
````

### af.getScopeIds

`af.getScopeIds() : Array`

````text
Returns an array of the current scope IDs.
````

### af.getVersion

`af.getVersion() : String`

````text
Returns the current OpenAF's build version.
````

### af.jqJava

`af.jqJava(input, expression, options) : Object`

````text
Evaluates jq 1.6 against JSON values. Prefer $jq for the documented public interface.
````

### af.js2s

`af.js2s(aObject) : String`

````text
Tries to convert an object into a beautified string representation.
````

### af.load

`af.load(aFilename)`

Loads an OpenAF script/file `aFilename`. The variable `__loadedfrom` will always be set to the `aFilename` value
after each execution. The `aFilename` can be composed not only by a filename but also with a zip/opack
file where it resides (for example: `"aZipFile.zip::aScriptInsideTheZip.js"`). The variable `__loadedfromzip` would hold,
in this case, the zip file from which the script was executed.

### af.loadRequire

`af.loadRequire(arrayOfPaths, isSandboxed)`

````text
Will redefine the require function on the current scope to use the arrayOfPaths provided.  Optionally you can the require function can provide a sandbox enviroment if isSandboxed = true.
````

### af.mkdir

`af.mkdir(aNewDirectory) : boolean`

````text
Tries to create aNewDirectory. Returns true if successfull, false otherwise.
````

### af.mv

`af.mv(aSourceFilePath, aTargetFilePath)`

````text
Tries to move aSourceFilePath to aTargetFilePath preserving file attributes.
````

### af.newOutputStream

`af.newOutputStream() : Stream`

Creates a new ByteArrayOutputStream. After using this stream you can, for example, use
`toString` and `toByteArray` methods from the resulting stream.

### af.newScriptInstance

`af.newScriptInstance(aClassOrName) : Script`

````text
Instantiates a compiled script class, handling Rhino descriptor-based constructors when needed.
````

### af.p

`af.p(aString)`

````text
Outputs to stdout aString ending with a newline.
````

### af.parse

`af.parse(aScriptString, aSourceName) : Array`

````text
Parses aScriptString, with aSourceName, returning the corresponding parsed statments.
````

### af.pathJava

`af.pathJava(obj, expression, customFunctions) : Object`

````text
Evaluates a JMESPath expression directly against Rhino values using the Java engine. Uses __flags.PATH_CACHE_SIZE (default 256, 0 disables caching). Prefer $path for OpenAF extensions.
````

### af.plugin

`af.plugin(aPluginClass)`

````text
Loads a OpenAF's plugin class (aPluginClass).
````

### af.pnl

`af.pnl(aString)`

````text
Outputs to stdout aString without a newline on the end.
````

### af.randomCryptSalt

`af.randomCryptSalt() : String`

````text
Generates a random valid, 2 char long, crypt salt to be used with af.crypt.
````

### af.rename

`af.rename(aSourceFilePath, aTargetFilePath)`

````text
Tries to rename aSourceFilePath to aTargetFilePath.
````

### af.restartOpenAF

`af.restartOpenAF(aCommandLineArray)`

````text
Terminates the current OpenAF execution and tries to start a new with the same command line, if aCommandLineArray is not provided. If aCommandLineArray is provided each array element will be use sequentially to build the command line to start a new OpenAF instance.
````

### af.rm

`af.rm(aFilePath)`

````text
Tries to delete a file or a directory on the provided aFilePath. In case it's a directory it will try to  recursively delete all directory contents.
````

### af.runFromClass

`af.runFromClass(aCompiledJavascriptClass) : Object`

Runs `aCompiledJavascriptClass` returning it's output. Example:

```javascript
af.compileToClasses("SomeClass", "print('hello world!');", "/some/path");
var aScriptClass = af.externalClass(["file://some/path/"], "SomeClass");
af.runFromClass(aScriptClass.newInstance());
```

### af.secureRandom

`af.secureRandom() : Double`

````text
Returns a java security SecureRandom double value.
````

### af.setK

`af.setK(aK)`

````text
Sets the current 16 bytes encrypt/decrypt key.
````

### af.sh

`af.sh(commandArguments, aStdIn, aTimeout, shouldInheritIO, aDirectory, returnMap, callbackFunc, encoding, dontWait, envsMap, exitCallback) : String/Map`

Tries to execute `commandArguments` (either a String or an array of strings) in the operating system. Optionally
`aStdIn` can be provided, `aTimeout` can be defined for the execution and if `shouldInheritIO` is true the stdout, stderr and stdin
will be inherit from OpenAF. If `shouldInheritIO` is not defined or false it will return the stdout of the command execution.
It's possible also to provide a different working `aDirectory`.
If `envsMap` (a map of strings) is defined the environment variables will be replaced by `envsMap`.
The variables `__exitcode` and `__stderr` can be checked for the command exit code and the stderr output correspondingly. In alternative
if `returnMap` = true a map will be returned with stdout, stderr and exitcode.
A `callbackFunc` can be provided, if `shouldInheritIO` is undefined or false, that will receive, as parameters, an output stream, a error stream and an input stream.
An `exitCallback` can also be provided that will receive the process as parameter and should return "force" to forcefully terminate the process or "destroy" to gracefully terminate it.
If defined the stdout and stderr won't be available for the `returnMap` if true. Example:

```javascript
sh("someCommand", void 0, void 0, false, void 0, false, function(o, e, i) { ioStreamReadLines(o, (f) => { print("TEST | " + String(f)) }, void 0, false) });
```

### af.sleep

`af.sleep(aTime)`

Suspends the current script execution (if using Threads only the thread executing this function) for a
period of `aTime` in ms. For example `aTime = 1000` would result in suspending the execution for 1 second.

### af.sync

`af.sync(aFunction, aObject)`

````text
When running in multithreaded scripts will ensure that aFunction is synchronized. Optionally aObject for synchronization can be provided.
````

### af.toBase64Bytes

`af.toBase64Bytes(arrayOfBytes) : anArrayOfBytes`

````text
Encodes arrayOfBytes, a string or array of bytes, as Base64 bytes without line breaks.
````

### af.toBase64Stream

`af.toBase64Stream(aInputStream, aOutputStream, shouldNotClose)`

Encodes raw bytes as standard padded Base64 without line breaks, copying Java streams with bounded memory.
Both streams close on success or processing failure unless `shouldNotClose` is true
(default false). Successful conversion finalizes and flushes output even when left open.
Invalid arguments are rejected before reading or closing streams. Errors propagate and
may leave partial output; cleanup errors are suppressed behind the original error.
Returns undefined. For example:

```javascript
af.toBase64Stream(io.readFileStream("A"), io.writeFileStream("B.b64"));
```

### af.toEncoding

`af.toEncoding(aString, aTargetEncoding, aSourceEncoding) : String`

````text
Converts aString to aTargetEncoding optionally providing aSourceEncoding. If aTargetEncoding is not provided it will default to the current java encoding.
````

### af.toTOONJava

`af.toTOONJava(aObj) : String`

````text
Tries to convert aObj into a TOON string using the native Java TOON engine (json-io) instead of the bundled Javascript one. See __flags.ALTERNATIVES.toTOON.
````

### af.validate2FA

`af.validate2FA(aKey, aToken) : boolean`

````text
Given aToken and a 2FA aKey returns true if it's valid. Note: it will use the current date/time of the system so it must be in sync with the authenticator app; scratchCodes are not handled.
````

### af.visibleLength

`af.visibleLength(aString, aWideEmojiPresentation) : int`

````text
Given aString returns its visible terminal width in columns, removing ANSI sequences and collapsing combined characters and emoji grapheme sequences. By default (aWideEmojiPresentation = true) bare "Emoji_Presentation=Yes" symbols (e.g. ✅ ⏳ ⚽ without a trailing U+FE0F) count as double-width, matching how modern GUI terminals (macOS Terminal, iTerm2, VS Code) render them. Pass false to match plain wcwidth-style terminals that only widen those symbols with an explicit U+FE0F.
````
{% endraw %}
