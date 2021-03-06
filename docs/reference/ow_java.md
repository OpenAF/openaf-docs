---
layout: default
title: ow.java
parent: Reference
grand_parent: OpenAF docs
---


## ow.java

### ow.java.cipher

__ow.java.cipher(anAlgorithm)__

````
Creates an ow.java.cipher to use anAlgorithm (defaults to RSA/ECB/OAEPWITHSHA-512ANDMGF1PADDING).
````
### ow.java.cipher

__ow.java.cipher(anAlgorithm)__

````
Creates an ow.java.cipher to use anAlgorithm (defaults to RSA/ECB/OAEPWITHSHA-512ANDMGF1PADDING).
````
### ow.java.cipher.aSymEncrypt

__ow.java.cipher.aSymEncrypt(aMessage, aPublicKey) : Map__

````
Given aMessage and previously generated aPublicKey will encrypt aMessage with a random symmetric key, encrypt that symmetric key with aPublicKey and return a map with eSymKey (encrypted symmetric key) and eMessage (encrypted message)
````
### ow.java.cipher.aSymEncrypt

__ow.java.cipher.aSymEncrypt(aMessage, aPublicKey) : Map__

````
Given aMessage and previously generated aPublicKey will encrypt aMessage with a random symmetric key, encrypt that symmetric key with aPublicKey and return a map with eSymKey (encrypted symmetric key) and eMessage (encrypted message)
````
### ow.java.cipher.decode2Key

__ow.java.cipher.decode2Key(aKey, isPrivate, anAlgorithm) : Key__

````
Given an encoded base 64 key (with ow.java.cipher.key2encode) returns the corresponding Key object. If the aKey is private isPrivate must be true, if public is must be false. Optionally a key anAlgorithm can be provided (defaults to RSA).
````
### ow.java.cipher.decode2Key

__ow.java.cipher.decode2Key(aKey, isPrivate, anAlgorithm) : Key__

````
Given an encoded base 64 key (with ow.java.cipher.key2encode) returns the corresponding Key object. If the aKey is private isPrivate must be true, if public is must be false. Optionally a key anAlgorithm can be provided (defaults to RSA).
````
### ow.java.cipher.decode2msg

__ow.java.cipher.decode2msg(aEncodedMessage) : String__

````
Given aEncodedMessage base 64 string returns the original message.
````
### ow.java.cipher.decode2msg

__ow.java.cipher.decode2msg(aEncodedMessage) : String__

````
Given aEncodedMessage base 64 string returns the original message.
````
### ow.java.cipher.decrypt

__ow.java.cipher.decrypt(aEncryptedMessage, aPrivateKey, anAlgorithm) : ArrayBytes__

````
Given a previously encrypted message will return the corresponding decrypted message using aPrivateKey. Optionally a key anAlgorithm can be provided (defaults to RSA).
````
### ow.java.cipher.decrypt

__ow.java.cipher.decrypt(aEncryptedMessage, aPrivateKey, anAlgorithm) : ArrayBytes__

````
Given a previously encrypted message will return the corresponding decrypted message using aPrivateKey. Optionally a key anAlgorithm can be provided (defaults to RSA).
````
### ow.java.cipher.decrypt4Text

__ow.java.cipher.decrypt4Text(aString, privateKey) : String__

````
Given aPrivateKey (from ow.java.cipher.readKey4File or genKeyPair) tries to RSA decrypt a base64 encrypted string returning the decrypted string.
````
### ow.java.cipher.decrypt4Text

__ow.java.cipher.decrypt4Text(aString, privateKey) : String__

````
Given aPrivateKey (from ow.java.cipher.readKey4File or genKeyPair) tries to RSA decrypt a base64 encrypted string returning the decrypted string.
````
### ow.java.cipher.decryptStream

__ow.java.cipher.decryptStream(aInputStream, aPrivateKey, anAlgorithm) : Stream__

````
Given a previously encrypted aInputStream will return the corresponding decrypted stream using aPrivateKey. Optionally a key anAlgorithm can be provided (defaults to RSA).
````
### ow.java.cipher.decryptStream

__ow.java.cipher.decryptStream(aInputStream, aPrivateKey, anAlgorithm) : Stream__

````
Given a previously encrypted aInputStream will return the corresponding decrypted stream using aPrivateKey. Optionally a key anAlgorithm can be provided (defaults to RSA).
````
### ow.java.cipher.encrypt

__ow.java.cipher.encrypt(aString, aPublicKey) : ArrayBytes__

````
Given aPublicKey (from ow.java.cipher.readKey4File or genKeyPair) tries to RSA encrypt aString returning the encrypted ArrayBytes.
````
### ow.java.cipher.encrypt

__ow.java.cipher.encrypt(aString, aPublicKey) : ArrayBytes__

````
Given aPublicKey (from ow.java.cipher.readKey4File or genKeyPair) tries to RSA encrypt aString returning the encrypted ArrayBytes.
````
### ow.java.cipher.encrypt2Text

__ow.java.cipher.encrypt2Text(aString, aPublicKey) : String__

````
Given aPublicKey (from ow.java.cipher.readKey4File or genKeyPair) tries to RSA encrypt aString to a base64 string returning the encrypted string.
````
### ow.java.cipher.encrypt2Text

__ow.java.cipher.encrypt2Text(aString, aPublicKey) : String__

````
Given aPublicKey (from ow.java.cipher.readKey4File or genKeyPair) tries to RSA encrypt aString to a base64 string returning the encrypted string.
````
### ow.java.cipher.encryptStream

__ow.java.cipher.encryptStream(outputStream, aPublicKey) : Stream__

````
Given aPublicKey (from ow.java.cipher.readKey4File or genKeyPair) tries to RSA encrypt outputStream returning an encrypted stream.
````
### ow.java.cipher.encryptStream

__ow.java.cipher.encryptStream(outputStream, aPublicKey) : Stream__

````
Given aPublicKey (from ow.java.cipher.readKey4File or genKeyPair) tries to RSA encrypt outputStream returning an encrypted stream.
````
### ow.java.cipher.genCert

__ow.java.cipher.genCert(aDn, aPublicKey, aPrivateKey, aValidity, aSigAlgName, aKeyStore, aPassword, aKeyStoreType) : JavaSignature__

````
Generates a certificate with aDn (defaults to "cn=openaf"), using aPublicKey and aPrivateKey, for aValidity date (defaults to a date  one year from now). Optionally you can specify aSigAlgName (defaults to SHA256withRSA), a file based aKeyStore and the corresponding aPassword (defaults to "changeit").
````
### ow.java.cipher.genCert

__ow.java.cipher.genCert(aDn, aPublicKey, aPrivateKey, aValidity, aSigAlgName, aKeyStore, aPassword, aKeyStoreType) : JavaSignature__

````
Generates a certificate with aDn (defaults to "cn=openaf"), using aPublicKey and aPrivateKey, for aValidity date (defaults to a date  one year from now). Optionally you can specify aSigAlgName (defaults to SHA256withRSA), a file based aKeyStore and the corresponding aPassword (defaults to "changeit").
````
### ow.java.cipher.genKeyPair

__ow.java.cipher.genKeyPair(aKeySize, aAlg) : Map__

````
Given aKeySize (e.g. 2048, 3072, 4096, 7680 and 15360) will return a map with publicKey and privateKey. Optionally you can choose an anAlgorithm (defaults to RSA).
````
### ow.java.cipher.genKeyPair

__ow.java.cipher.genKeyPair(aKeySize, aAlg) : Map__

````
Given aKeySize (e.g. 2048, 3072, 4096, 7680 and 15360) will return a map with publicKey and privateKey. Optionally you can choose an anAlgorithm (defaults to RSA).
````
### ow.java.cipher.key2encode

__ow.java.cipher.key2encode(aKey) : String__

````
Given aKey (from ow.java.cipher.readKey4File or genKeyPair) returns the base 64 corresponding encoded string.
````
### ow.java.cipher.key2encode

__ow.java.cipher.key2encode(aKey) : String__

````
Given aKey (from ow.java.cipher.readKey4File or genKeyPair) returns the base 64 corresponding encoded string.
````
### ow.java.cipher.msg2encode

__ow.java.cipher.msg2encode(anEncryptedMessage) : String__

````
Given anEncryptedMessage returns the base 64 encoded string.
````
### ow.java.cipher.msg2encode

__ow.java.cipher.msg2encode(anEncryptedMessage) : String__

````
Given anEncryptedMessage returns the base 64 encoded string.
````
### ow.java.cipher.prototype.aSymDecrypt

__ow.java.cipher.prototype.aSymDecrypt(eMessage, eSymKey, privateKey) : ArrayBytes__

````
Given a previously encrypted eMessage with an encrypted symmetric key, will use the provided privateKey to decrypt eSymKey and use it to decrypt eMessage returning the corresponding decrypted contents.
````
### ow.java.cipher.prototype.aSymDecrypt

__ow.java.cipher.prototype.aSymDecrypt(eMessage, eSymKey, privateKey) : ArrayBytes__

````
Given a previously encrypted eMessage with an encrypted symmetric key, will use the provided privateKey to decrypt eSymKey and use it to decrypt eMessage returning the corresponding decrypted contents.
````
### ow.java.cipher.readKey4File

__ow.java.cipher.readKey4File(aFilename, isPrivate, anAlgorithm) : Key__

````
Given a key file previously saved with ow.java.cipher.saveKey2File returns the Key object to use with other functions. If the aKey is private isPrivate must be true, if public is must be false. Optionally a key anAlgorithm can be provided (defaults to RSA).
````
### ow.java.cipher.readKey4File

__ow.java.cipher.readKey4File(aFilename, isPrivate, anAlgorithm) : Key__

````
Given a key file previously saved with ow.java.cipher.saveKey2File returns the Key object to use with other functions. If the aKey is private isPrivate must be true, if public is must be false. Optionally a key anAlgorithm can be provided (defaults to RSA).
````
### ow.java.cipher.saveKey2File

__ow.java.cipher.saveKey2File(aFilename, aKey, isPrivate, anAlgorithm)__

````
Given a public or private aKey (from ow.java.cipher.readKey4File or genKeyPair) tries to save it to aFilename. If the aKey is private isPrivate must be true, if public is must be false. Optionally a key anAlgorithm can be provided (defaults to RSA).
````
### ow.java.cipher.saveKey2File

__ow.java.cipher.saveKey2File(aFilename, aKey, isPrivate, anAlgorithm)__

````
Given a public or private aKey (from ow.java.cipher.readKey4File or genKeyPair) tries to save it to aFilename. If the aKey is private isPrivate must be true, if public is must be false. Optionally a key anAlgorithm can be provided (defaults to RSA).
````
### ow.java.cipher.sign

__ow.java.cipher.sign(aPrivateKey, aInputStream, inBytes) : Object__

````
Tries to sign the contents from aInputStream using aPrivateKey. Return the signature in an array of bytes or, if inBytes = true, has a base 64 encoded string.
````
### ow.java.cipher.sign

__ow.java.cipher.sign(aPrivateKey, aInputStream, inBytes) : Object__

````
Tries to sign the contents from aInputStream using aPrivateKey. Return the signature in an array of bytes or, if inBytes = true, has a base 64 encoded string.
````
### ow.java.cipher.symDecrypt

__ow.java.cipher.symDecrypt(anEncryptedMessage, aKey) : ArrayBytes__

````
Returns the decrypted anEncryptedMessage using aKey (used to encrypt with symEncrypt)
````
### ow.java.cipher.symDecrypt

__ow.java.cipher.symDecrypt(anEncryptedMessage, aKey) : ArrayBytes__

````
Returns the decrypted anEncryptedMessage using aKey (used to encrypt with symEncrypt)
````
### ow.java.cipher.symEncrypt

__ow.java.cipher.symEncrypt(aMessage, aKey) : ArrayBytes__

````
Returns a symmetric encrypted aMessage using a previously generated aKey (using ow.java.cipher.symGenKey).
````
### ow.java.cipher.symEncrypt

__ow.java.cipher.symEncrypt(aMessage, aKey) : ArrayBytes__

````
Returns a symmetric encrypted aMessage using a previously generated aKey (using ow.java.cipher.symGenKey).
````
### ow.java.cipher.symGenKey

__ow.java.cipher.symGenKey(aSize) : ArrayBytes__

````
Returns a generated symmetric key with aSize (defaults to aSize)
````
### ow.java.cipher.symGenKey

__ow.java.cipher.symGenKey(aSize) : ArrayBytes__

````
Returns a generated symmetric key with aSize (defaults to aSize)
````
### ow.java.cipher.verify

__ow.java.cipher.verify(signatureToVerify, aPublicKey, aInputStream, isBytes) : boolean__

````
Given aInputStream and aPublicKey will verify if the signatureToVerify is valid. Optionally isBytes = true  the signatureToVerify is an array of bytes instead of base 64 encoded.
````
### ow.java.cipher.verify

__ow.java.cipher.verify(signatureToVerify, aPublicKey, aInputStream, isBytes) : boolean__

````
Given aInputStream and aPublicKey will verify if the signatureToVerify is valid. Optionally isBytes = true  the signatureToVerify is an array of bytes instead of base 64 encoded.
````
### ow.java.gc

__ow.java.gc()__

````
Executes the Java runtime gargabe collector.
````
### ow.java.gc

__ow.java.gc()__

````
Executes the Java runtime gargabe collector.
````
### ow.java.getAddressType

__ow.java.getAddressType(aAddress) : Map__

````
Given aAddress tries to return a map with the following flags: isValidAddress, hostname, ipv4, ipv6 and privateAddress
````
### ow.java.getAddressType

__ow.java.getAddressType(aAddress) : Map__

````
Given aAddress tries to return a map with the following flags: isValidAddress, hostname, ipv4, ipv6 and privateAddress
````
### ow.java.getClassVersion

__ow.java.getClassVersion(aClassBytes) : String__

````
Given the class array of bytes (aClassBytes), or a string from which the corresponding bytes will be read, tries to determine the minimum JVM version required to load the class.
````
### ow.java.getClassVersion

__ow.java.getClassVersion(aClassBytes) : String__

````
Given the class array of bytes (aClassBytes), or a string from which the corresponding bytes will be read, tries to determine the minimum JVM version required to load the class.
````
### ow.java.getHost2IP

__ow.java.getHost2IP(aHost) : String__

````
Tries to resolve aHost to an IP address using the default DNS.
````
### ow.java.getHost2IP

__ow.java.getHost2IP(aHost) : String__

````
Tries to resolve aHost to an IP address using the default DNS.
````
### ow.java.getIP2Host

__ow.java.getIP2Host(aIP) : String__

````
Tries to reverse DNS aIP to a host address using the default DNS.
````
### ow.java.getIP2Host

__ow.java.getIP2Host(aIP) : String__

````
Tries to reverse DNS aIP to a host address using the default DNS.
````
### ow.java.getJarVersion

__ow.java.getJarVersion(aJarFile) : Array__

````
Given aJarFile will return an array of JVM versions used in java classes contained.
````
### ow.java.getJarVersion

__ow.java.getJarVersion(aJarFile) : Array__

````
Given aJarFile will return an array of JVM versions used in java classes contained.
````
### ow.java.getMemory

__ow.java.getMemory(shouldFormat) : Map__

````
Returns a map with the current java runtime max, total, used and free heap memory. If shouldFormat = true ow.format.toBytesAbbreviation will be used.
````
### ow.java.getMemory

__ow.java.getMemory(shouldFormat) : Map__

````
Returns a map with the current java runtime max, total, used and free heap memory. If shouldFormat = true ow.format.toBytesAbbreviation will be used.
````
### ow.java.getWhoIs

__ow.java.getWhoIs(aQuery, aInitServer) : Map__

````
Tries to perform a whois aQuery for a domain or an ip address. Optionally you can provide aInitServer (defaults to whois.iana.org)
````
### ow.java.getWhoIs

__ow.java.getWhoIs(aQuery, aInitServer) : Map__

````
Tries to perform a whois aQuery for a domain or an ip address. Optionally you can provide aInitServer (defaults to whois.iana.org)
````
### ow.java.IMAP

__ow.java.IMAP(aServer, aUser, aPassword, isSSL, aPort, isReadOnly)__

````
Creates an instance to access aServer, using aUser and aPassword through a optional aPort and optionally using isSSL = true to use SSL. If isReadOnly = true the folders will be open only as read-only.
````
### ow.java.IMAP

__ow.java.IMAP(aServer, aUser, aPassword, isSSL, aPort, isReadOnly)__

````
Creates an instance to access aServer, using aUser and aPassword through a optional aPort and optionally using isSSL = true to use SSL. If isReadOnly = true the folders will be open only as read-only.
````
### ow.java.IMAP.close

__ow.java.IMAP.close(aFolder)__

````
Tries to a close a previously aFolder (defaults to "Inbox") automatically open in other operations.
````
### ow.java.IMAP.close

__ow.java.IMAP.close(aFolder)__

````
Tries to a close a previously aFolder (defaults to "Inbox") automatically open in other operations.
````
### ow.java.IMAP.getMessage

__ow.java.IMAP.getMessage(aFolder, aNum) : Map__

````
Tries to retrieve a message metadata map based on aNum from aFolder.
````
### ow.java.IMAP.getMessage

__ow.java.IMAP.getMessage(aFolder, aNum) : Map__

````
Tries to retrieve a message metadata map based on aNum from aFolder.
````
### ow.java.IMAP.getMessageBodyPart

__ow.java.IMAP.getMessageBodyPart(aFolder, aNum, aBodyPartId) : String__

````
Retrieves the body part identified as aBodyPartId (starts in 0) from the message aNum on aFolder.
````
### ow.java.IMAP.getMessageBodyPart

__ow.java.IMAP.getMessageBodyPart(aFolder, aNum, aBodyPartId) : String__

````
Retrieves the body part identified as aBodyPartId (starts in 0) from the message aNum on aFolder.
````
### ow.java.IMAP.getMessageCount

__ow.java.IMAP.getMessageCount(aFolder) : Number__

````
Retrieves the current message count for aFolder.
````
### ow.java.IMAP.getMessageCount

__ow.java.IMAP.getMessageCount(aFolder) : Number__

````
Retrieves the current message count for aFolder.
````
### ow.java.IMAP.getMessages

__ow.java.IMAP.getMessages(aFolder, aNumber) : Array__

````
Tries to retrieve an array of maps of message metadata from aFolder (defaults to Inbox) up to aNumber (defaults to 5) of messages.
````
### ow.java.IMAP.getMessages

__ow.java.IMAP.getMessages(aFolder, aNumber) : Array__

````
Tries to retrieve an array of maps of message metadata from aFolder (defaults to Inbox) up to aNumber (defaults to 5) of messages.
````
### ow.java.IMAP.getNewMessageCount

__ow.java.IMAP.getNewMessageCount(aFolder) : Number__

````
Retrieves the current new message count for aFolder.
````
### ow.java.IMAP.getNewMessageCount

__ow.java.IMAP.getNewMessageCount(aFolder) : Number__

````
Retrieves the current new message count for aFolder.
````
### ow.java.IMAP.getSortedMessages

__ow.java.IMAP.getSortedMessages(aFolder, aType, aTerm, aNumber) : Array__

````
For IMAP servers supporting the SORT operation will retrieve an array of maps of message metadata from aFolder (defaults to "Inbox") up to aNumber (defaults to 5) of messages. The list will be filtered by aTerm for aType (e.g. FROM (default), ARRIVAL, CC, DATE, REVERSE, SIZE, SUBJECT, TO).
````
### ow.java.IMAP.getSortedMessages

__ow.java.IMAP.getSortedMessages(aFolder, aType, aTerm, aNumber) : Array__

````
For IMAP servers supporting the SORT operation will retrieve an array of maps of message metadata from aFolder (defaults to "Inbox") up to aNumber (defaults to 5) of messages. The list will be filtered by aTerm for aType (e.g. FROM (default), ARRIVAL, CC, DATE, REVERSE, SIZE, SUBJECT, TO).
````
### ow.java.IMAP.getUnreadMessageCount

__ow.java.IMAP.getUnreadMessageCount(aFolder) : Boolean__

````
Tries to determine if there are new unread messages in aFolder (defailt to Inbox)
````
### ow.java.IMAP.getUnreadMessageCount

__ow.java.IMAP.getUnreadMessageCount(aFolder) : Boolean__

````
Tries to determine if there are new unread messages in aFolder (defailt to Inbox)
````
### ow.java.IMAP.hasNewMessages

__ow.java.IMAP.hasNewMessages(aFolder) : Boolean__

````
Tries to determine how many new messagse there are in aFolder (defailt to Inbox)
````
### ow.java.IMAP.hasNewMessages

__ow.java.IMAP.hasNewMessages(aFolder) : Boolean__

````
Tries to determine how many new messagse there are in aFolder (defailt to Inbox)
````
### ow.java.maven.getFile

__ow.java.maven.getFile(artifactId, aFilenameTemplate, aOutputDir)__

````
Given the artifactId (prefixed with the group id using ".") will try to download the latest version of the aFilenameTemplate (where version will translate to the latest version) on the provided aOutputDir.

Example:
   getFile("com.google.code.gson.gson", "gson-{{version}}.jar", ".")


````
### ow.java.maven.getFile

__ow.java.maven.getFile(artifactId, aFilenameTemplate, aOutputDir)__

````
Given the artifactId (prefixed with the group id using ".") will try to download the latest version of the aFilenameTemplate (where version will translate to the latest version) on the provided aOutputDir.

Example:
   getFile("com.google.code.gson.gson", "gson-{{version}}.jar", ".")


````
### ow.java.maven.getFileVersion

__ow.java.maven.getFileVersion(artifactId, aFilenameTemplate, aVersion, aOutputDir)__

````
Given the artifactId (prefixed with the group id using ".") will try to download the specific version of the aFilenameTemplate (where version will translate to the latest version) on the provided aOutputDir.

Example:
   getFile("com.google.code.gson.gson", "gson-{{version}}.jar", "1.2.3", ".")


````
### ow.java.maven.getFileVersion

__ow.java.maven.getFileVersion(artifactId, aFilenameTemplate, aVersion, aOutputDir)__

````
Given the artifactId (prefixed with the group id using ".") will try to download the specific version of the aFilenameTemplate (where version will translate to the latest version) on the provided aOutputDir.

Example:
   getFile("com.google.code.gson.gson", "gson-{{version}}.jar", "1.2.3", ".")


````
### ow.java.maven.getLatestVersion

__ow.java.maven.getLatestVersion(aURI) : String__

````
Get the latest version from the provide aURI for a Maven 2 repository.
````
### ow.java.maven.getLatestVersion

__ow.java.maven.getLatestVersion(aURI) : String__

````
Get the latest version from the provide aURI for a Maven 2 repository.
````
### ow.java.maven.getLicenseByVersion

__ow.java.maven.getLicenseByVersion(artifactId, aFilenameTemplate, aVersion, aOutputDir)__

````
Given the artifactId (prefixed with the group id using ".") will try to update a LICENSES.txt on the provided aOutputDir based on aFilenameTemplate (where version will translate to the latest version).

Example:
   getLicenseByVersion("com.google.code.gson.gson", "gson-{{version}}.jar", "1.2.3", ".")


````
### ow.java.maven.getLicenseByVersion

__ow.java.maven.getLicenseByVersion(artifactId, aFilenameTemplate, aVersion, aOutputDir)__

````
Given the artifactId (prefixed with the group id using ".") will try to update a LICENSES.txt on the provided aOutputDir based on aFilenameTemplate (where version will translate to the latest version).

Example:
   getLicenseByVersion("com.google.code.gson.gson", "gson-{{version}}.jar", "1.2.3", ".")


````
### ow.java.maven.processMavenFile

__ow.java.maven.processMavenFile(aFolder, shouldDeleteOld, aLogFunc)__

````
Processes a ".maven.yaml" or ".maven.json" on aFolder. Optionally you can specify that is should not delete old versions and/or provide a specific log function (defaults to log). The ".maven.yaml/json" file is expected to contain an artifacts map with an array of maps each with: group (maven artifact group), id (maven id), version (optionally if not the latest), output (optionally specify a different output folder than aFolder), testFunc (optionally a test function to determine which files should be deleted).
````
### ow.java.maven.processMavenFile

__ow.java.maven.processMavenFile(aFolder, shouldDeleteOld, aLogFunc)__

````
Processes a ".maven.yaml" or ".maven.json" on aFolder. Optionally you can specify that is should not delete old versions and/or provide a specific log function (defaults to log). The ".maven.yaml/json" file is expected to contain an artifacts map with an array of maps each with: group (maven artifact group), id (maven id), version (optionally if not the latest), output (optionally specify a different output folder than aFolder), testFunc (optionally a test function to determine which files should be deleted).
````
### ow.java.maven.removeOldVersions

__ow.java.maven.removeOldVersions(artifactId, aFilenameTemplate, aOutputDir, aFunction)__

````
Given the artifactId (prefixed with the group id using ".") will try to delete from aOutputDir all versions that aren't the latest version  of the aFilenameTemplate (where version will translate to the latest version). Optionally you can provide aFunction that receives the canonical filename of each potential version and will only delete it if the function returns true.
````
### ow.java.maven.removeOldVersions

__ow.java.maven.removeOldVersions(artifactId, aFilenameTemplate, aOutputDir, aFunction)__

````
Given the artifactId (prefixed with the group id using ".") will try to delete from aOutputDir all versions that aren't the latest version  of the aFilenameTemplate (where version will translate to the latest version). Optionally you can provide aFunction that receives the canonical filename of each potential version and will only delete it if the function returns true.
````
### ow.java.maven.search

__ow.java.maven.search(aTerm) : Array__

````
Tries to search aTerm in maven.org and then fallsback to archetype-catalog.xml returning an array with groupId and artifactId.
````
### ow.java.maven.search

__ow.java.maven.search(aTerm) : Array__

````
Tries to search aTerm in maven.org and then fallsback to archetype-catalog.xml returning an array with groupId and artifactId.
````
### ow.java.setIgnoreSSLDomains

__ow.java.setIgnoreSSLDomains(aList, aPassword)__

````
Replaces the current Java SSL socket factory with a version with a custom trust manager that will "ignore" verification of SSL certificates whose domains are part of aList. Optionally aPassword for the key store can be forced. WARNING: this should only be used in advanced setups where you know what are doing since it DISABLES IMPORTANT SECURITY FEATURES.
````
### ow.java.setIgnoreSSLDomains

__ow.java.setIgnoreSSLDomains(aList, aPassword)__

````
Replaces the current Java SSL socket factory with a version with a custom trust manager that will "ignore" verification of SSL certificates whose domains are part of aList. Optionally aPassword for the key store can be forced. WARNING: this should only be used in advanced setups where you know what are doing since it DISABLES IMPORTANT SECURITY FEATURES.
````
