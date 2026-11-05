---
layout: default
title: Easily add a SSL certificate to access an URL
parent: Advanced
grand_parent: Guides
---

# Easily add a SSL certificate to access an URL

When accessing an URL that hosts a self-signed SSL certificate you might need to add the certificate to your's Java runtime environment trusted certificates. If you search around the internet you will find several articles explaining how to do this using Java's keytool utility (adding the certificate to the Java's keystore).

You might find a very old piece of code, posted on Sun's blog, which would connect to a host on a specific port, examine the certificate and added it to the Java's keystore. That code was packed in an OpenAF's oPack for ease of use.

## Install it

To install it just execute:

````bash
$ opack install InstallCert
````

## To use it

To use it change the current directory to the JRE/JDK's security path. This is usually on $JAVA_HOME/lib/security. To use it:

````bash
$ cd $JAVA_HOME/lib/security
$ opack exec InstallCert some.host:443
````

_Note: you can use a different port (instead of 443) if needed._

During the execution you will be prompted to add the certificate to the trusted keystore by answering the number of the certificate. If needed execute more than one time to add all certificates or ensure that the certificate is now trusted (e.g. won't ask if you want to add it).

## If the keystore has a different password

The code will generate a file called _jssecacerts_. If you already have a similar file with a different password from the default you may enter it like this:

````bash
$ cd $JAVA_HOME/lib/security
$ opack exec InstallCert some.host:443 myNewPassword
````

## Ignoring the SSL domain validation

In some cases, for testing, you might want to ignore the SSL domain validation. This can be done by adding the following code in OpenAF:

````javascript
ow.loadJava();
ow.java.setIgnoreSSLDomains(["some.host"]); // or ow.java.setIgnoreSSLDomains(["some.host"], "myNewPassword")
````

You can set this on your [user home holder]/.openaf-console_profile file so that it applies to all OpenAF based execution.

Please do keep in mind that this **DISABLES IMPORTANT SECURITY FEATURES** and should only be used in advanced setups where this is intended or testing.
