---
layout: default
title: OpenAF docs
has_children: true
---

# OpenAF

OpenAF (_pronounced open-a-f_) is a Java & Javascript based "swiss-army knife" scripting DevOps tool for different automation challenges with minimal requirements and footprint, extensible through packages ([oPacks](docs/concepts/oPack.md)) and with easy code orchestration ([oJob](docs/concepts/oJob.md) and [oJob.io](docs/concepts/oJobIO.md)).
## Topics

* __[Quick start](docs/guides/cheat-sheet/openaf-programming.md)__ - getting you quickly writing and executing OpenAF scripts
* __[Concepts](docs/concepts/index.md)__ - understand some of the basic concepts
* __[How to](docs/howto/index.md)__ - core functionality exemplified.
* __[Guides](docs/guides/index.md)__ - guides with example code from beginner to advanced topics.

## October 2026 source updates

Explore [what changed since July](docs/guides/advanced/october-2026.md): stateless LLM decisions, MCP OAuth, JSON query engines, instrumentation, and new script-to-oJob tutorials. This documentation covers the October source snapshot and the local `20261014 nightly` runtime; it does not announce a published stable release.

## Installing/Setup

### Docker

````bash
docker run --pull always --rm -ti openaf/oaf
# ./oafc
````

> For more options for the OpenAF container images check the [container images](docs/concepts/container-images.md) page.

## Single file download

Download the specific file for your OS and architecture (see below for Windows):

| OS | Architecture | Link |
|------------------|----|--------------|
| Linux | x86_64 (Intel) | [openaf.io/oaf-linux-x86_64](https://openaf.io/oaf-linux-x86_64) |
| Linux | aarch64 (Arm) | [openaf.io/oaf-linux-aarch64](https://openaf.io/oaf-linux-aarch64) |
| Alpine Linux | x86_64 (Intel) | [openaf.io/oaf-alpine-x86_64](https://openaf.io/oaf-alpine-x86_64) |
| Alpine Linux | aarch64 (Arm) | [openaf.io/oaf-alpine-aarch64](https://openaf.io/oaf-alpine-aarch64) |
| Mac | x64_64 (Intel) | [openaf.io/oaf-mac-x86_64](https://openaf.io/oaf-mac-x86_64) |
| Mac | aarch64 (Apple Silicon) | [openaf.io/oaf-mac-aarch64](https://openaf.io/oaf-mac-aarch64) |


After downloading the file, execute:

```bash
chmod u+x oaf-*
./oaf-*
# Please use the created symlinks: oaf, ojob, opack, oafc, oafp, oaf-sb or ojob-sb
# ./oafc
``` 

This will provide it with execution permissons and, afterwards, simply execute it.

For a more permanent or portable install follow the next instructions.

### Windows

````
C:\> mkdir oaf
C:\> cd oaf
C:\oaf> curl https://openaf.io/install.bat -o install.bat
C:\oaf> install.bat
C:\oaf> oafc
````

### Linux

````bash
# With sudo
curl https://openaf.io/install.sh | sh
# oafc

# Without sudo
curl https://openaf.io/setup.sh | sh && cd oaf
# ./oafc

# With an existing java JRE/JDK >= 21
curl https://ojob.io/get.sh | sh && cd oaf
# ./oafc
````

If you don't have _sudo_, _curl_ or _wget_ but you do have bash you can just execute the following command or [follow these instructions](docs/howto/Download-without-curl-or-wget.md):

```bash
# With just bash
/bin/bash -c "exec 3<>/dev/tcp/ojob.io/80 && echo -e \"GET /get.sh HTTP/1.1\nHost: ojob.io\nUser-Agent: curl\nConnection: close\n\n\" >&3 && cat <&3" | sed '1,/connection: close/d' | tail -n +2 | sh -s
```

### Mac OS

````bash
curl -o setup.sh https://openaf.io/setup.sh && sh setup.sh && rm setup.sh && mv oaf /Applications/OpenAF && sudo sh -c "echo "/Applications/OpenAF" > /etc/paths.d/OpenAF"
# oafc
````

## Move to a different folder

If you used "install.sh": After moving to the new folder execute the reinstall.sh (or reinstall.bat in Windows) created after the first installation.

If you used "setup.sh": Simple move the folder.

## Upgrade

After installing an update.sh (or update.bat in Windows) will be created. Simply execute it.

## Uninstall

### Linux

````bash
sudo ojob ojob.io/oaf/symlinks UNINSTALL=true && sudo rm -rf /opt/oaf
````

### Mac OS

````
rm -rf /Applications/OpenAF && sudo rm /etc/paths/OpenAF && rm ~/.openaf*
````

### Windows

Simply delete the created folder ([current folder]/oaf or c:\\oaf)

There might be also ".openaf*" files created on your home folder (c:\\users\\[your user]\\.openaf*)

## Specific installs

Follow the link for [specific architectures installations](installing.md).

### Nightly build

If you want to install the nightly build follow these [instructions](installing-nightly.md).

### Older versions

To install older versions please follow these [instructions](docs/howto/Download-older-versions.md).
You can also check the [GitHub releases list](https://github.com/OpenAF/openaf/releases)
