---
layout: default
title: Specific installation instructions
parent: How To
grand_parent: OpenAF docs
---

# Specific installation instructions

The current source baseline requires **Java 21 or later**. Bundled installers select a runtime; when supplying your own Java, verify its version and architecture. Stable and nightly downloads have separate release histories; see the [documentation baseline](docs/source-snapshot.md).

## Unix (x86 based)

````bash
$ mkdir oaf && cd oaf
$ wget -O - https://openaf.io/unix64/install.sh | sh
$ ./oafc
````

## Windows (64-bit)

````
C:\> mkdir oaf
C:\> cd oaf
C:\oaf> curl https://openaf.io/win64/install.bat -o install.bat
C:\oaf> install.bat
C:\oaf> oafc
````

## Mac OS (Intel based)

````bash
$ mkdir oaf && cd oaf
$ curl -o install.sh https://openaf.io/mac64/install.sh
$ sh install.sh
$ ./oafc
````

## Mac OS (Apple silicon based)

````bash
$ mkdir oaf && cd oaf
$ curl -o install.sh https://openaf.io/macarm/install.sh
$ sh install.sh
$ ./oafc
````

## Docker

````bash
$ docker run --rm -ti openaf/openaf
/openaf # oafc
````

## Unix (ARM 64)

````bash
$ mkdir oaf && cd oaf
$ wget -O - https://openaf.io/arm64/install.sh | sh
$ oafc
````

## Unix (ARM 32)

````bash
$ mkdir oaf && cd oaf
$ wget -O - https://openaf.io/arm32/install.sh | sh
$ oafc
````
