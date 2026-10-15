---
layout: default
title: afbase
parent: Reference
grand_parent: OpenAF docs
---


## afbase

### af.compile

__af.compile(aScriptString, aSourceName) : Object__

````
Compiles the aScriptString executing it and returning the corresponding result.  Optionally you can provide aSourceName.
````
### af.compileToClasses

__af.compileToClasses(aClassfile, aScriptString, aPath)__

````
Given aClassfile name, aScriptString and, optionally, a filesystem aPath it will generate Java bytecode as result of compiling the aScriptString into a filesystem aClassfile (on the provided aPath). Example:

af.compileToClasses("SomeClass", "print('hello world!');", "/some/path")


````
### af.cp

__af.cp(aSourceFilePath, aTargetFilePath)__

````
Tries to copy aSourceFilePath to aTargetFilePath preserving file attributes.
````
### af.create2FACredentials

__af.create2FACredentials(anAccountName, anIssuer) : Map__

````
Given anAccountName and anIssuer will create a the 2FA/TOTP (Time-Based One-Time Password) returning a map with the scratchCodes, the verificationCode, the key, the openaf encryptedKey, the QR code URL  and the OTP URL.
````
### af.crypt

__af.crypt(aKey, aSalt) : String__

````
Tries to mimic crypt(3) password encryption using the org.apache.commons.codec.digest.Crypt.crypt function. Please check https://commons.apache.org/proper/commons-codec/apidocs/org/apache/commons/codec/digest/Crypt.html for more. Use af.randomCryptSalt() to generate a random salt if necessary.
````
### af.decrypt

__af.decrypt(aString, aKey) : String__

````
Decrypts the provided aString with the provided aKey.
````
### af.e

__af.e(aString)__

````
Outputs to stderr aString ending with a newline.
````
### af.encrypt

__af.encrypt(aString, aKey) : String__

````
Encrypts the provided aString as password for most of the OpenAF password functionality. If aKey is provided it will encrypt using it.
````
### af.enl

__af.enl(aString)__

````
Outputs to stderr aString without a newline on the end.
````
### af.eval

__af.eval(aScript) : Object__

````
Performs the equivalent version of the javascript eval function for the provided aScript. Returns  the corresponding result of the evaluation.
````
### af.externalAddClasspath

__af.externalAddClasspath(aURL)__

````
Tries to add aURL to the current classpath. Don't forget that directories must end with a '/', for  example: file:/my/own/dir/

Note: This might not work for some JVMs.
````
### af.externalClass

__af.externalClass(anArrayOfClasspathEntries, aClassName) : JavaClass__

````
Returns an external Java class with the aClassName, not included in the initial OpenAF's classpath, loaded from a list of jars/folders in anArrayOfClasspathEntries.
````
### af.externalClassLoader

__af.externalClassLoader(anArrayOfClasspathEntries) : ClassLoader__

````
Returns a ClassLoader suitable to be use with af.getClass to dynamically load Java classes that weren't included  on the initial OpenAF's classpath and are included in the jars/folders provided in anArrayOfClasspathEntries.
````
### af.externalPlugin

__af.externalPlugin(anArrayOfClasspathEntries, aPluginClass)__

````
Loads a OpenAF's plugin identified by the aPluginClass that isn't available in the initial OpenAF's classpath, loaded from a list of jars/folders in anArrayOfClasspathEntries.
````
### af.fromArray2Bytes

__af.fromArray2Bytes(anArray) : anArrayOfBytes__

````
Converts a javascript array of integers into a Java anArrayOfBytes.
````
### af.fromBase64

__af.fromBase64(aBase) : anArrayOfBytes__

````
Given aBase as a string or an array of bytes will convert it to anArrayOfBytes in Base 64.
````
### af.fromBytes2Array

__af.fromBytes2Array(anArrayOfBytes) : Array__

````
Converts a Java anArrayOfBytes into a javascript array of integers with the value representation of  each byte.
````
### af.fromBytes2InputStream

__af.fromBytes2InputStream(anArrayOfBytes) : Stream__

````
Converts anArrayOfBytes into a ByteArrayInputStream.
````
### af.fromBytes2OutputStream

__af.fromBytes2OutputStream(anArrayOfBytes) : Stream__

````
Converts anArrayOfBytes into a ByteArrayOutputStream. After using this stream you can, for example, use .toString and toByteArray methods from the resulting stream.
````
### af.fromBytes2String

__af.fromBytes2String(anArrayOfBytes, anEncoding) : aString__

````
Converts anArrayOfBytes into a string, optionally with the provided anEncoding.
````
### af.fromInputStream2Bytes

__af.fromInputStream2Bytes(aStream) : anArrayOfBytes__

````

````
### af.fromInputStream2String

__af.fromInputStream2String(aStream, anEncoding) : String__

````
Tries to convert an input aStream into a String.
````
### af.fromString2Bytes

__af.fromString2Bytes(aString, anEncoding) : anArrayOfBytes__

````
Converts aString into anArrayOfBytes, optionally with the provided anEncoding.
````
### af.fromString2InputStream

__af.fromString2InputStream(aString, anEncoding) : Stream__

````
Converts aString into a ByteArrayInputStream.
````
### af.fromString2OutputStream

__af.fromString2OutputStream(aString, encoding) : Stream__

````
Converts aString into a ByteArrayOutputStream. After using this stream you can, for example, use .toString and toByteArray methods from the resulting stream.
````
### af.fromXML

__af.fromXML(aXMLObject) : aString__

````
Converts aXMLObject (E4X) into a String. Warning: beware that E4X is an obsolete object.
````
### af.get2FAToken

__af.get2FAToken(aKey, aSpecificTime) : String__

````
Given 2FA aKey it will return the current token. Note: it will use the current date/time of the system so it must be in sync with the authenticator. Optionally you can provide aSpecificTime.
````
### af.getClass

__af.getClass(aName, aLoader) : JavaClass__

````
Returns the JavaClass object the Java class identified by aName. Optionally you can provide a Java classloader ( this can be the result of using af.externalClassLoader).
````
### af.getDistribution

__af.getDistribution() : String__

````
Returns the current OpenAF's distribution channel.
````
### af.getOpenAFJar

__af.getOpenAFJar() : String__

````
Retrives the fullpath for the OpenAF jar.
````
### af.getScopeIds

__af.getScopeIds() : Array__

````
Returns an array of the current scope IDs.
````
### af.getVersion

__af.getVersion() : String__

````
Returns the current OpenAF's build version.
````
### af.js2s

__af.js2s(aObject) : String__

````
Tries to convert an object into a beautified string representation.
````
### af.load

__af.load(aFilename)__

````
Loads an OpenAF script/file aFilename. The variable __loadedfrom will always be set to the aFilename value a after each execution. The aFilename can be composed not only by a filename but also with a zip/opack file where it resides (for example: "aZipFile.zip::aScriptInsideTheZip.js"). The variable __loadedfromzip would hold,  in this case, the zip file from which the script was executed.
````
### af.loadRequire

__af.loadRequire(arrayOfPaths, isSandboxed)__

````
Will redefine the require function on the current scope to use the arrayOfPaths provided.  Optionally you can the require function can provide a sandbox enviroment if isSandboxed = true.
````
### af.mkdir

__af.mkdir(aNewDirectory) : boolean__

````
Tries to create aNewDirectory. Returns true if successfull, false otherwise.
````
### af.mv

__af.mv(aSourceFilePath, aTargetFilePath)__

````
Tries to move aSourceFilePath to aTargetFilePath preserving file attributes.
````
### af.newOutputStream

__af.newOutputStream() : Stream__

````
Creates a new ByteArrayOutputStream. After using this stream you can, for example, use .toString and toByteArray methods from the resulting stream.
````
### af.p

__af.p(aString)__

````
Outputs to stdout aString ending with a newline.
````
### af.parse

__af.parse(aScriptString, aSourceName) : Array__

````
Parses aScriptString, with aSourceName, returning the corresponding parsed statments.
````
### af.plugin

__af.plugin(aPluginClass)__

````
Loads a OpenAF's plugin class (aPluginClass).
````
### af.pnl

__af.pnl(aString)__

````
Outputs to stdout aString without a newline on the end.
````
### af.randomCryptSalt

__af.randomCryptSalt() : String__

````
Generates a random valid, 2 char long, crypt salt to be used with af.crypt.
````
### af.rename

__af.rename(aSourceFilePath, aTargetFilePath)__

````
Tries to rename aSourceFilePath to aTargetFilePath.
````
### af.restartOpenAF

__af.restartOpenAF(aCommandLineArray)__

````
Terminates the current OpenAF execution and tries to start a new with the same command line, if aCommandLineArray is not provided. If aCommandLineArray is provided each array element will be use sequentially to build the command line to start a new OpenAF instance.
````
### af.rm

__af.rm(aFilePath)__

````
Tries to delete a file or a directory on the provided aFilePath. In case it's a directory it will try to  recursively delete all directory contents.
````
### af.runFromClass

__af.runFromClass(aCompiledJavascriptClass) : Object__

````
Runs aCompiledJavascriptClass returning it's output. Example:

af.compileToClasses("SomeClass", "print('hello world!');", "/some/path");
var aScriptClass = af.externalClass(["file://some/path/"], "SomeClass");
af.runFromClass(aScriptClass.newInstance());


````
### af.secureRandom

__af.secureRandom() : Double__

````
Returns a java security SecureRandom double value.
````
### af.setK

__af.setK(aK)__

````
Sets the current 16 bytes encrypt/decrypt key.
````
### af.sh

__af.sh(commandArguments, aStdIn, aTimeout, shouldInheritIO, aDirectory, returnMap, callbackFunc, encoding, dontWait, envsMap) : String/Map__

````
Tries to execute commandArguments (either a String or an array of strings) in the operating system. Optionally aStdIn can be provided, aTimeout can be defined for the execution and if shouldInheritIO is true the stdout, stderr and stdin will be inherit from OpenAF. If shouldInheritIO is not defined or false it will return the stdout of the command execution. It's possible also to provide a different working aDirectory. If envsMap (a map of strings) is defined the environment variables will be replaced by envsMap. The variables __exitcode and __stderr can be checked for the command exit code and the stderr output correspondingly. In alternative  if returnMap = true a map will be returned with stdout, stderr and exitcode. A callbackFunc can be provided, if shouldInheritIO is undefined or false, that will receive, as parameters, an output stream, a error stream and an input stream. If defined the stdout and stderr won't be available for the returnMap if true. Example:

sh("someCommand", void 0, void 0, false, void 0, false, function(o, e, i) { ioStreamReadLines(o, (f) => { print("TEST | " + String(f)) }, void 0, false) });


````
### af.sleep

__af.sleep(aTime)__

````
Suspends the current script execution (if using Threads only the thread executing this function) for a  period of aTime in ms. For example aTime = 1000 would result in suspending the execution for 1 second.
````
### af.sync

__af.sync(aFunction, aObject)__

````
When running in multithreaded scripts will ensure that aFunction is synchronized. Optionally aObject for synchronization can be provided.
````
### af.toBase64Bytes

__af.toBase64Bytes(arrayOfBytes) : anArrayOfBytes__

````
Given arrayOfBytes as a string or an array of bytes in Base 64 will convert it back to an array of bytes.
````
### af.toEncoding

__af.toEncoding(aString, aTargetEncoding, aSourceEncoding) : String__

````
Converts aString to aTargetEncoding optionally providing aSourceEncoding. If aTargetEncoding is not provided it will default to the current java encoding.
````
### af.validate2FA

__af.validate2FA(aKey, aToken) : boolean__

````
Given aToken and a 2FA aKey returns true if it's valid. Note: it will use the current date/time of the system so it must be in sync with the authenticator app; scratchCodes are not handled.
````
### af.visibleLength

__af.visibleLength(aString, aWideEmojiPresentation) : int__

````
Given aString returns its visible terminal width in columns, removing ANSI sequences and collapsing combined characters and emoji grapheme sequences. By default (aWideEmojiPresentation = true) bare "Emoji_Presentation=Yes" symbols (e.g. ✅ ⏳ ⚽ without a trailing U+FE0F) count as double-width, matching how modern GUI terminals (macOS Terminal, iTerm2, VS Code) render them. Pass false to match plain wcwidth-style terminals that only widen those symbols with an explicit U+FE0F.
````

### af.jqJava

__af.jqJava(input, expression, options) : Object__

````
Evaluates jq 1.6 against JSON values. Prefer $jq for the documented public interface.
````

### af.pathJava

__af.pathJava(obj, expression, customFunctions) : Object__

````
Evaluates a JMESPath expression directly against Rhino values using the Java engine. Uses __flags.PATH_CACHE_SIZE (default 256, 0 disables caching). Prefer $path for OpenAF extensions.
````

### af.compileToJar

__af.compileToJar(aClassfile, aScriptString, aJarFile)__

````
Given aClassfile name and aScriptString it will generate Java bytecode as a result of compiling aScriptString, writing every generated class as a single entry into aJarFile instead of one loose .class file per class (see af.compileToClasses). aJarFile is written to a temporary file next to it and then moved into place, so a failed compile never leaves a partial/corrupt jar behind; the class can then be loaded with af.externalClass/af.runFromExternalClass pointed at aJarFile directly (a URLClassLoader treats a jar file URL the same as a directory URL). Example:

af.compileToJar("SomeClass", "print('hello world!');", "/some/path/SomeClass.jar")
````

### af.newScriptInstance

__af.newScriptInstance(aClassOrName) : Script__

````
Instantiates a compiled script class, handling Rhino descriptor-based constructors when needed.
````
