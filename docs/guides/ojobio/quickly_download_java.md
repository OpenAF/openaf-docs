---
layout: default
title: Quickly download portable JDKs/JREs
parent: oJobIO
grand_parent: Guides
---

# Quickly download portable JVMs/JREs

The remote `ojob.io/java/download` job downloads and repackages Java distributions. It is maintained outside the four repositories in the [documentation baseline](../../source-snapshot.md). Consult its current help before use; available builds and default versions can change.

For the current OpenAF source baseline, request **Java 21 or later explicitly**:

```sh
ojob ojob.io/java/download version=21 os=linux arch=x64 type=jre
```

The job writes a runtime archive such as `jre.tgz` in the working directory. Extract it in a separate directory and check the executable:

```sh
tar xzf jre.tgz
jre/bin/java -version
```

## Download a JDK instead of a JRE

```sh
ojob ojob.io/java/download version=21 os=linux arch=x64 type=jdk
```

## Download a different version, a different architecture and/or a different operating system

For a Java 21 JDK on an Apple Silicon Mac:

```sh
ojob ojob.io/java/download type=jdk arch=aarch64 os=mac version=21
```

The target platform describes where the archive will run, which may differ from the machine downloading it.

## Listing available options

```sh
ojob ojob.io/java/download version=21 list=true
```

Use a combination returned by the current catalog. Archive sizes, release numbers and available combinations depend on the provider. See [updating OpenAF's JVM](../../howto/Update-JVM-version.md) to switch an existing installation.
