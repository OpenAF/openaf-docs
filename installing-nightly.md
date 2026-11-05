---
layout: default
title: Installing the nightly build
parent: How To
grand_parent: OpenAF docs
---

The current source baseline requires **Java 21 or later**. Bundled installers select a runtime; when supplying your own Java, verify its version and architecture. Stable and nightly downloads have separate release histories; see the [documentation baseline](docs/source-snapshot.md).

## Installing the nightly build

### Unix (x86 based)

````bash
$ mkdir oaf && cd oaf
$ wget -O - https://openaf.io/unix64/nightly/install.sh | sh
$ ./oafc
````

### Windows (64-bit)

````
C:\> mkdir oaf
C:\> cd oaf
C:\oaf> curl https://openaf.io/win64/nightly/install.bat -o install.bat
C:\oaf> install.bat
C:\oaf> oafc
````

### Mac OS (Intel based)

````bash
$ mkdir oaf && cd oaf
$ curl -o install.sh https://openaf.io/mac64/nightly/install.sh
$ sh install.sh
$ oafc
````

### Mac OS (Apple silicon based)

````bash
$ mkdir oaf && cd oaf
$ curl -o install.sh https://openaf.io/macarm/nightly/install.sh | sh
$ ./oafc
````

### Docker

````bash
$ docker run --rm -ti openaf/openaf:nightly
/openaf # oafc
````

### Unix (ARM 64)

````bash
$ mkdir oaf && cd oaf
$ wget -O - https://openaf.io/arm64/nightly/install.sh | sh
$ oafc
````

### Unix (ARM 32)

````bash
$ mkdir oaf && cd oaf
$ wget -O - https://openaf.io/arm32/nightly/install.sh | sh
$ oafc
````

## Upgrade

After installing an update.sh (or update.bat in Windows) will be created. Simply execute it.

## Move to a different folder

After moving to the new folder execute the reinstall.sh (or reinstall.bat in Windows) created after the first installation.

## Uninstall

Simply delete the created folder.

There might be also ".openaf*" files created on your home folder.

## Unix generic install/uninstall

### Install (with Java)

````bash
$ wget -O - https://openaf.io/nightly/install.sh | sh
````

### Install (without Java)

````bash
$ wget -O - https://openaf.io/nightly/download.sh | sh
````

### Uninstall

````bash
$ ojob ojob.io/oaf/symlinks UNINSTALL=true && rm -rf /opt/oaf
````
