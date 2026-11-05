---
layout: default
title: ow.java
parent: Reference
grand_parent: OpenAF docs
---

{% raw %}
## ow.java

[Source: `06414cd9`](https://github.com/OpenAF/openaf/blob/06414cd9204e918daa1e2971ce904783299db333/js/owrap.java.js) · [Baseline](../source-snapshot.md)

### ow.java.IMAP

`ow.java.IMAP(aServer, aUser, aPassword, isSSL, aPort, isReadOnly)`

````text
Creates an instance to access aServer, using aUser and aPassword through a optional aPort and optionally using isSSL = true to use SSL. If isReadOnly = true the folders will be open only as read-only.
````

### ow.java.IMAP.close

`ow.java.IMAP.close(aFolder)`

````text
Tries to a close a previously aFolder (defaults to "Inbox") automatically open in other operations.
````

### ow.java.IMAP.getMessage

`ow.java.IMAP.getMessage(aFolder, aNum) : Map`

````text
Tries to retrieve a message metadata map based on aNum from aFolder.
````

### ow.java.IMAP.getMessageBodyPart

`ow.java.IMAP.getMessageBodyPart(aFolder, aNum, aBodyPartId) : String`

````text
Retrieves the body part identified as aBodyPartId (starts in 0) from the message aNum on aFolder.
````

### ow.java.IMAP.getMessageCount

`ow.java.IMAP.getMessageCount(aFolder) : Number`

````text
Retrieves the current message count for aFolder.
````

### ow.java.IMAP.getMessages

`ow.java.IMAP.getMessages(aFolder, aNumber) : Array`

````text
Tries to retrieve an array of maps of message metadata from aFolder (defaults to Inbox) up to aNumber (defaults to 5) of messages.
````

### ow.java.IMAP.getNewMessageCount

`ow.java.IMAP.getNewMessageCount(aFolder) : Number`

````text
Retrieves the current new message count for aFolder.
````

### ow.java.IMAP.getSortedMessages

`ow.java.IMAP.getSortedMessages(aFolder, aType, aTerm, aNumber) : Array`

````text
For IMAP servers supporting the SORT operation will retrieve an array of maps of message metadata from aFolder (defaults to "Inbox") up to aNumber (defaults to 5) of messages. The list will be filtered by aTerm for aType (e.g. FROM (default), ARRIVAL, CC, DATE, REVERSE, SIZE, SUBJECT, TO).
````

### ow.java.IMAP.getUnreadMessageCount

`ow.java.IMAP.getUnreadMessageCount(aFolder) : Boolean`

````text
Tries to determine if there are new unread messages in aFolder (defailt to Inbox)
````

### ow.java.IMAP.hasNewMessages

`ow.java.IMAP.hasNewMessages(aFolder) : Boolean`

````text
Tries to determine how many new messagse there are in aFolder (defailt to Inbox)
````

### ow.java.JMX

`ow.java.JMX(aURL, aUser, aPass, aProvider) : JMX`

````text
Creates a JMX connection to the provided URL (similar to service:jmx:rmi:///jndi/rmi://1.2.3.4:1234/jmxrmi or a map with a host and a port). Optionally, if necessary, aUser and aPass. To customize the JMX provider use aProvider.
````

### ow.java.JMX.getAll

`ow.java.JMX.getAll() : Map`

````text
Will query the JMX target for all registered domains, query the registered objects for each domain and returns a combined map of the corresponding values.
````

### ow.java.JMX.getDomains

`ow.java.JMX.getDomains() : Array`

````text
Will query the JMX target for existing domains to be used with ow.java.JMX.queryNames a return the corresponding list.
````

### ow.java.JMX.getJavaStd

`ow.java.JMX.getJavaStd() : Map`

````text
Will query the JMX target for the "java.lang.*" objects and return the corresponding map.
````

### ow.java.JMX.getObject

`ow.java.JMX.getObject(anObject) : Map`

````text
Given a JMX anObject will find all the corresponding attributes, retrieve their corresponding values and returning in a map. If any errors occurred a map entry "_errors" with an array of errors will be included in the returned map.
````

### ow.java.JMX.getObjects

`ow.java.JMX.getObjects(aObjectName) : Map`

````text
Given a JMX domain + name + type or JMX aQuery (similar to the provided to ow.java.JMX.queryNames) will retrieve all objects from each domain, name and type. The returned map will be organized by a map "name" entry with sub-map for each "type".
````

### ow.java.JMX.queryNames

`ow.java.JMX.queryNames(aQuery) : Array`

````text
Given aQuery (similar to 'java.lang:*') given a JMX domain it will query the JMX target and return a list of registered domain + name + type ready to be used with ow.java.JMX.getObject.
````

### ow.java.checkDigest

`ow.java.checkDigest(aDigestString, aMessage) : boolean`

````text
Given aDigestString (e.g. [algorithm]:[digest]) and aMessage will verify the digest verifies returning true or false
````

### ow.java.cipher

`ow.java.cipher(anAlgorithm)`

````text
Creates an ow.java.cipher to use anAlgorithm (defaults to RSA/ECB/OAEPWITHSHA-512ANDMGF1PADDING).
````

### ow.java.cipher.aSymEncrypt

`ow.java.cipher.aSymEncrypt(aMessage, aPublicKey) : Map`

````text
Given aMessage and previously generated aPublicKey will encrypt aMessage with a random symmetric key, encrypt that symmetric key with aPublicKey and return a map with eSymKey (encrypted symmetric key) and eMessage (encrypted message)
````

### ow.java.cipher.decode2Key

`ow.java.cipher.decode2Key(aKey, isPrivate, anAlgorithm) : Key`

````text
Given an encoded base 64 key (with ow.java.cipher.key2encode) returns the corresponding Key object. If the aKey is private isPrivate must be true, if public is must be false. Optionally a key anAlgorithm can be provided (defaults to RSA).
````

### ow.java.cipher.decode2msg

`ow.java.cipher.decode2msg(aEncodedMessage) : String`

````text
Given aEncodedMessage base 64 string returns the original message.
````

### ow.java.cipher.decodeKey

`ow.java.cipher.decodeKey(aString, isPrivate, anAlgorithm) : JavaObject`

````text
Decode aString base64 key representation (from encodeKey) into a public or private (isPrivate = true) key optionally specifying anAlgorithm (defaults to RSA)
````

### ow.java.cipher.decrypt

`ow.java.cipher.decrypt(aEncryptedMessage, aPrivateKey, anAlgorithm) : ArrayBytes`

````text
Given a previously encrypted message will return the corresponding decrypted message using aPrivateKey. Optionally a key anAlgorithm can be provided (defaults to RSA).
````

### ow.java.cipher.decrypt4Text

`ow.java.cipher.decrypt4Text(aString, privateKey) : String`

````text
Given aPrivateKey (from ow.java.cipher.readKey4File or genKeyPair) tries to RSA decrypt a base64 encrypted string returning the decrypted string.
````

### ow.java.cipher.decryptStream

`ow.java.cipher.decryptStream(aInputStream, aPrivateKey, anAlgorithm) : Stream`

````text
Given a previously encrypted aInputStream will return the corresponding decrypted stream using aPrivateKey. Optionally a key anAlgorithm can be provided (defaults to RSA).
````

### ow.java.cipher.encodeCert

`ow.java.cipher.encodeCert(aCert) : String`

````text
Encodes aCert(ificate) into a base64 PEM representation.
````

### ow.java.cipher.encodeKey

`ow.java.cipher.encodeKey(aKey, isPrivate) : String`

````text
Encodes private (isPrivate = true) or public key into a base64 key representation.
````

### ow.java.cipher.encrypt

`ow.java.cipher.encrypt(aString, aPublicKey) : ArrayBytes`

````text
Given aPublicKey (from ow.java.cipher.readKey4File or genKeyPair) tries to RSA encrypt aString returning the encrypted ArrayBytes.
````

### ow.java.cipher.encrypt2Text

`ow.java.cipher.encrypt2Text(aString, aPublicKey) : String`

````text
Given aPublicKey (from ow.java.cipher.readKey4File or genKeyPair) tries to RSA encrypt aString to a base64 string returning the encrypted string.
````

### ow.java.cipher.encryptStream

`ow.java.cipher.encryptStream(outputStream, aPublicKey) : Stream`

````text
Given aPublicKey (from ow.java.cipher.readKey4File or genKeyPair) tries to RSA encrypt outputStream returning an encrypted stream.
````

### ow.java.cipher.genCert

`ow.java.cipher.genCert(aDn, aPublicKey, aPrivateKey, aValidity, aSigAlgName, aKeyStore, aPassword, aKeyStoreType) : JavaSignature`

````text
Generates a certificate with aDn (defaults to "cn=openaf"), using aPublicKey and aPrivateKey, for aValidity date (defaults to a date  one year from now). Optionally you can specify aSigAlgName (defaults to SHA256withRSA), a file based aKeyStore and the corresponding aPassword (defaults to "changeit").
````

### ow.java.cipher.genKeyPair

`ow.java.cipher.genKeyPair(aKeySize, aAlg) : Map`

````text
Given aKeySize (e.g. 2048, 3072, 4096, 7680 and 15360) will return a map with publicKey and privateKey. Optionally you can choose an anAlgorithm (defaults to RSA).
````

### ow.java.cipher.getCert4File

`ow.java.cipher.getCert4File(aFile) : Java`

````text
Given a X509 certificate aFile will return the corresponding Java certificate object.
````

### ow.java.cipher.getCert4String

`ow.java.cipher.getCert4String(aString) : Java`

````text
Given a X509 certificate string will return the corresponding Java certificate object.
````

### ow.java.cipher.key2encode

`ow.java.cipher.key2encode(aKey) : String`

````text
Given aKey (from ow.java.cipher.readKey4File or genKeyPair) returns the base 64 corresponding encoded string.
````

### ow.java.cipher.msg2encode

`ow.java.cipher.msg2encode(anEncryptedMessage) : String`

````text
Given anEncryptedMessage returns the base 64 encoded string.
````

### ow.java.cipher.prototype.aSymDecrypt

`ow.java.cipher.prototype.aSymDecrypt(eMessage, eSymKey, privateKey) : ArrayBytes`

````text
Given a previously encrypted eMessage with an encrypted symmetric key, will use the provided privateKey to decrypt eSymKey and use it to decrypt eMessage returning the corresponding decrypted contents.
````

### ow.java.cipher.readKey4File

`ow.java.cipher.readKey4File(aFilename, isPrivate, anAlgorithm) : Key`

````text
Given a key file previously saved with ow.java.cipher.saveKey2File returns the Key object to use with other functions. If the aKey is private isPrivate must be true, if public is must be false. Optionally a key anAlgorithm can be provided (defaults to RSA).
````

### ow.java.cipher.readKey4Stream

`ow.java.cipher.readKey4Stream(aInputStream, isPrivate, anAlgorithm) : Key`

````text
Given a key on aInputStream previously saved with ow.java.cipher.saveKey2Stream returns the Key object to use with other functions. If the aKey is private isPrivate must be true, if public is must be false. Optionally a key anAlgorithm can be provided (defaults to RSA).
````

### ow.java.cipher.readKey4String

`ow.java.cipher.readKey4String(aString, isPrivate, anAlgorithm) : Key`

````text
Given a key on aString previously saved with ow.java.cipher.saveKey2String returns the Key object to use with other functions. If the aKey is private isPrivate must be true, if public is must be false. Optionally a key anAlgorithm can be provided (defaults to RSA).
````

### ow.java.cipher.saveKey2File

`ow.java.cipher.saveKey2File(aFilename, aKey, isPrivate, anAlgorithm)`

````text
Given a public or private aKey (from ow.java.cipher.readKey4File or genKeyPair) tries to save it to aFilename. If the aKey is private isPrivate must be true, if public is must be false. Optionally a key anAlgorithm can be provided (defaults to RSA).
````

### ow.java.cipher.saveKey2Stream

`ow.java.cipher.saveKey2Stream(aOutputStream, isPrivate, anAlgorithm) : String`

````text
Given a public or private aKey (from ow.java.cipher.readKey4File or genKeyPair) tries to return output to aOutputStream. If the aKey is private isPrivate must be true, if public is must be false. Optionally a key anAlgorithm can be provided (defaults to RSA).
````

### ow.java.cipher.saveKey2String

`ow.java.cipher.saveKey2String(aKey, isPrivate, anAlgorithm) : String`

````text
Given a public or private aKey (from ow.java.cipher.readKey4File or genKeyPair) tries to return a string representation. If the aKey is private isPrivate must be true, if public is must be false. Optionally a key anAlgorithm can be provided (defaults to RSA).
````

### ow.java.cipher.sign

`ow.java.cipher.sign(aPrivateKey, aInputStream, inBytes) : Object`

````text
Tries to sign the contents from aInputStream using aPrivateKey. Return the signature in an array of bytes or, if inBytes = true, has a base 64 encoded string.
````

### ow.java.cipher.symDecrypt

`ow.java.cipher.symDecrypt(anEncryptedMessage, aKey) : ArrayBytes`

````text
Returns the decrypted anEncryptedMessage using aKey (used to encrypt with symEncrypt)
````

### ow.java.cipher.symEncrypt

`ow.java.cipher.symEncrypt(aMessage, aKey) : ArrayBytes`

````text
Returns a symmetric encrypted aMessage using a previously generated aKey (using ow.java.cipher.symGenKey).
````

### ow.java.cipher.symGenKey

`ow.java.cipher.symGenKey(aSize) : ArrayBytes`

````text
Returns a generated symmetric key with aSize (defaults to aSize)
````

### ow.java.cipher.verify

`ow.java.cipher.verify(signatureToVerify, aPublicKey, aInputStream, isBytes) : boolean`

````text
Given aInputStream and aPublicKey will verify if the signatureToVerify is valid. Optionally isBytes = true  the signatureToVerify is an array of bytes instead of base 64 encoded.
````

### ow.java.digestAsHex

`ow.java.digestAsHex(aAlg, aMessage) : String`

````text
Given an avaiable JVM aAlg(orithm) (check with ow.java.getDigestAlgs) will return the corresponding aMessage  (which can be a string, byte array, ByteBuffer, File or InputStream) digest in hexadecimal format.
````

### ow.java.gc

`ow.java.gc()`

````text
Executes the Java runtime gargabe collector.
````

### ow.java.getAddressType

`ow.java.getAddressType(aAddress) : Map`

````text
Given aAddress tries to return a map with the following flags: isValidAddress, hostname, ipv4, ipv6 and privateAddress
````

### ow.java.getCCPU

`ow.java.getCCPU(aReadFileFn) : Map`

````text
Returns a map with the current cgroup cpu stats. Optionally you can provide a aReadFileFn that should expect the full path on a linux cgroup root filesystem and return a string with the corresponding contents.
````

### ow.java.getCMemory

`ow.java.getCMemory(shouldFormat, aReadFileFn, aFileExistsFn) : Map`

````text
Returns a map with the current cgroup runtime max, total, used and free memory. If shouldFormat = true ow.format.toBytesAbbreviation will be used. Optionally you can provide a aReadFileFn that should expect the full path on a linux cgroup root filesystem and return a string with the corresponding contents.
````

### ow.java.getClassPath

`ow.java.getClassPath() : String`

````text
Retrieves the initial java classpath.
````

### ow.java.getClassVersion

`ow.java.getClassVersion(aClassBytes) : String`

````text
Given the class array of bytes (aClassBytes), or a string from which the corresponding bytes will be read, tries to determine the minimum JVM version required to load the class.
````

### ow.java.getDigestAlgs

`ow.java.getDigestAlgs() : Array`

````text
Retrieves the current JVM list of digest algorithms (and provider) to be used with ow.java.digestAsHex.
````

### ow.java.getHost2IP

`ow.java.getHost2IP(aHost) : String`

````text
Tries to resolve aHost to an IP address using the default DNS.
````

### ow.java.getIP2Host

`ow.java.getIP2Host(aIP) : String`

````text
Tries to reverse DNS aIP to a host address using the default DNS.
````

### ow.java.getInputArguments

`ow.java.getInputArguments() : Array`

````text
List of Java virtual machine input arguments
````

### ow.java.getJarVersion

`ow.java.getJarVersion(aJarFile) : Array`

````text
Given aJarFile will return an array of JVM versions used in java classes contained.
````

### ow.java.getLibraryPath

`ow.java.getLibraryPath() : String`

````text
Retrieves the initial OS library path.
````

### ow.java.getLinuxCPUInfo

`ow.java.getLinuxCPUInfo(aReadFileFn) : Array`

````text
Parses a Linux CPU info. Optionally you can provide a aReadFileFn that should expect the full path on a linux /proc root filesystem and return a string with the corresponding contents.
````

### ow.java.getLinuxUptime

`ow.java.getLinuxUptime(aReadFileFn) : Array`

````text
Parses a Linux uptme info. Optionally you can provide a aReadFileFn that should expect the full path on a linux /proc root filesystem and return a string with the corresponding contents.
````

### ow.java.getLocalJavaPIDs

`ow.java.getLocalJavaPIDs(aUserID, aTmpDir) : Array`

````text
Will return an array with the pid and the path for hsperf (to use with ow.java.parseHSPerf) that are currently running (hotspot jvms only) in the current system.  If aUserID is not provided the current user name will be used. Optionally you can provide aTmpDir to use a different temporary directory.
````

### ow.java.getMemory

`ow.java.getMemory(shouldFormat) : Map`

````text
Returns a map with the current java runtime max, total, used and free heap memory. If shouldFormat = true ow.format.toBytesAbbreviation will be used.
````

### ow.java.getSystemProperties

`ow.java.getSystemProperties() : Map`

````text
Retrieves the current list of system properties.
````

### ow.java.getWhoIs

`ow.java.getWhoIs(aQuery, aInitServer) : Map`

````text
Tries to perform a whois aQuery for a domain or an ip address. Optionally you can provide aInitServer (defaults to whois.iana.org)
````

### ow.java.ini

`ow.java.ini() : Object`

Returns an object to handle Windows INI / Java properties kind of files. Available methods are:

- `load(content)`: Given a INI/properties file content converts to an internal format
- `loadFile(aFile)`: Loads a file with load()
- `get()`: Returns a map of the internal format representation
- `put(aMap)`: Read `aMap` into the internal format representation (arrays not fully supported)
- `save()`: Returns a INI/properties string
- `saveFile(aFile)`: Saves a file using save()

Examples:

```javascript
ow.java.ini().loadFile("/etc/os-release").get()
ow.java.ini().put(myMap).save()
```

### ow.java.jcmd

`ow.java.jcmd(aPid, aJCmd) : String`

````text
Tries to attach to local JVM with aPid and execute aJCmd returning the output.
````

### ow.java.maven.getFile

`ow.java.maven.getFile(artifactId, aFilenameTemplate, aOutputDir)`

Given the `artifactId` (prefixed with the group id using ".") will try to download the latest version of the `aFilenameTemplate` (where
version will translate to the latest version) on the provided `aOutputDir`.

Example:

```javascript
getFile("com.google.code.gson.gson", "gson-{{version}}.jar", ".")
```

### ow.java.maven.getFileVersion

`ow.java.maven.getFileVersion(artifactId, aFilenameTemplate, aVersion, aOutputDir)`

Given the `artifactId` (prefixed with the group id using ".") will try to download the specific version of the `aFilenameTemplate` (where
version will translate to the latest version) on the provided `aOutputDir`.

Example:

```javascript
getFile("com.google.code.gson.gson", "gson-{{version}}.jar", "1.2.3", ".")
```

### ow.java.maven.getLatestStableVersion

`ow.java.maven.getLatestStableVersion(aURI) : String`

````text
Get the highest stable version (excluding alpha, beta, milestones, release candidates, snapshots, etc...) from the provided aURI for a Maven 2 repository. Returns undefined if no stable version is found.
````

### ow.java.maven.getLatestVersion

`ow.java.maven.getLatestVersion(aURI) : String`

````text
Get the latest version from the provide aURI for a Maven 2 repository.
````

### ow.java.maven.getLatestVersionGA

`ow.java.maven.getLatestVersionGA(aGroupId, aArtifactId, onlyStable) : String`

````text
Same as getLatestVersionString but with separate aGroupId and aArtifactId (needed when the artifactId itself contains dots, e.g. jakarta.xml.bind:jakarta.xml.bind-api). If onlyStable = true pre-release versions are ignored.
````

### ow.java.maven.getLatestVersionString

`ow.java.maven.getLatestVersionString(artifactId, onlyStable) : String`

````text
Given the artifactId (prefixed with the group id using ".") will try to determine the latest version and return the corresponding string. If onlyStable = true pre-release versions (alpha, beta, rc, milestones, snapshots, etc...) are ignored.
````

### ow.java.maven.getLicenseByVersion

`ow.java.maven.getLicenseByVersion(artifactId, aFilenameTemplate, aVersion, aOutputDir)`

Given the `artifactId` (prefixed with the group id using ".") will try to update a LICENSES.txt on the provided `aOutputDir` based
on `aFilenameTemplate` (where version will translate to the latest version).

Example:

```javascript
getLicenseByVersion("com.google.code.gson.gson", "gson-{{version}}.jar", "1.2.3", ".")
```

### ow.java.maven.getVersions

`ow.java.maven.getVersions(aURI) : Array`

````text
Returns the array of all versions listed in the maven-metadata.xml of the provided aURI for a Maven 2 repository.
````

### ow.java.maven.isStableVersion

`ow.java.maven.isStableVersion(aVersion) : boolean`

````text
Returns false if aVersion looks like a pre-release (e.g. alpha, beta, milestone, rc, cr, preview, ea, snapshot, dev, nightly...) and true otherwise (e.g. 1.2.3, 1.2.3.Final, 1.2.3-jre, 5.0.0.RELEASE, 1.0-GA).
````

### ow.java.maven.processMavenFile

`ow.java.maven.processMavenFile(aFolder, shouldDeleteOld, aLogFunc)`

````text
Processes a ".maven.yaml" or ".maven.json" on aFolder. Optionally you can specify that is should not delete old versions and/or provide a specific log function (defaults to log). The ".maven.yaml/json" file is expected to contain an artifacts map with an array of maps each with: group (maven artifact group), id (maven id), version (optionally if not the latest), output (optionally specify a different output folder than aFolder), testFunc (optionally a test function to determine which files should be deleted).
````

### ow.java.maven.removeOldVersions

`ow.java.maven.removeOldVersions(artifactId, aFilenameTemplate, aOutputDir, aFunction)`

````text
Given the artifactId (prefixed with the group id using ".") will try to delete from aOutputDir all versions that aren't the latest version  of the aFilenameTemplate (where version will translate to the latest version). Optionally you can provide aFunction that receives the canonical filename of each potential version and will only delete it if the function returns true.
````

### ow.java.maven.search

`ow.java.maven.search(aTerm) : Array`

````text
Tries to search aTerm in maven.org and then fallsback to archetype-catalog.xml returning an array with groupId and artifactId.
````

### ow.java.parseHSPerf

`ow.java.parseHSPerf(aByteArrayOrFile, retFlat, options) : Map`

````text
Given aByteArray or a file path for a java (hotspot jvm) hsperf file (using ow.java.getLocalJavaPIDs or similar) will return the java performance information parsed into a map. If retFlat = true the returned map will be a flat map with each java performance metric and correspondent exact string value. Nested output includes available derived calculations with the prefix "__". Supports HotSpot perfdata 2.0 (Java 8+), with long scalars and UTF-8 strings. options.metadata=true returns {values, header, entries}; entries use original counter names. options.strict=true throws descriptive parse errors, including unsupported counter types/shapes; otherwise unsupported counters are skipped and invalid or inaccessible buffers return 4. File and argument errors throw. Header overflow reports counters that could not be stored. Derived timer values use the reported frequency; application time is an estimate.
````

### ow.java.parseJFR

`ow.java.parseJFR(aFile, aFnRec, includeDesc) : Array`

````text
Given aFile (a Java Flight Recorder file) will parse it and call aFnRec for each event found, if defined. Optionally you can provide aFnRec to receive each event as a map with the following fields: startTime, endTime, duration, name, thread and fields. If includeDesc is true it will include a field (__desc_) for each field added with the description of the field.
````

### ow.java.pidCheckJFR

`ow.java.pidCheckJFR(aPid) : String`

````text
Tries to attach to local JVM with aPid and check the current Java Flight Recorder recording status.
````

### ow.java.pidDumpJFR

`ow.java.pidDumpJFR(aPid, aName, aFile) : String`

````text
Tries to attach to local JVM with aPid and dump a Java Flight Recorder returning the output.
````

### ow.java.pidStartJFR

`ow.java.pidStartJFR(aPid, aDuration, aName, aMaxSize) : String`

````text
Tries to attach to local JVM with aPid and start a Java Flight Recorder returning the output.
````

### ow.java.pidStopJFR

`ow.java.pidStopJFR(aPid, aName) : String`

````text
Tries to attach to local JVM with aPid and stop a Java Flight Recorder returning the output.
````

### ow.java.pidSystemProperties

`ow.java.pidSystemProperties(aPid) : Map`

````text
Tries to attach to local JVM with aPid and retrieve the system properties.
````

### ow.java.pidThreadDump

`ow.java.pidThreadDump(aPid) : String`

````text
Tries to attach to local JVM with aPid and execute a thread dump returning the output.
````

### ow.java.setIgnoreSSLDomains

`ow.java.setIgnoreSSLDomains(aList, aPassword)`

````text
Replaces the current Java SSL socket factory with a version with a custom trust manager that will "ignore" verification of SSL certificates whose domains are part of aList (if no aList is provided defaults DANGEROUSLY to all). Optionally  aPassword for the key store can be forced.
WARNING: this should only be used in advanced setups where you know what are doing since it DISABLES IMPORTANT SECURITY FEATURES.
````
{% endraw %}
