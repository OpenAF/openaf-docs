---
layout: default
title: How To - Update the JVM version
parent: How To
grand_parent: OpenAF docs
---

# How to - Update the JVM version

OpenAF launchers (`oaf`, `oafc`, `ojob`, `opack`) run a Java executable with `openaf.jar`. The current source baseline requires **Java 21 or later**. Choose a Java build for the host operating system and architecture; old Java 8 paths in historical examples are not suitable for this baseline.

Inspect the Java runtime actually used by OpenAF:

```sh
oaf -c 'print(java.lang.System.getProperty("java.version")); print(java.lang.System.getProperty("java.home"));'
```

## When Java is on an operating system folder

Install the new Java runtime first, then regenerate launchers from the OpenAF installation directory using that runtime explicitly:

```sh
cd /path/to/openaf
/path/to/jdk-21/bin/java -jar openaf.jar --install
```

`--install` rewrites the launcher scripts to use the selected Java installation. Run the inspection command again to confirm the path and version. Restart long-running OpenAF processes separately; changing a launcher does not switch an already-running JVM.

## When there is a "jre" sub-folder

Stop processes that use the bundled runtime, keep a backup of the existing `jre` directory, and extract the replacement so that `jre/bin/java` exists. Verify its executable permissions and version, then regenerate launchers if the path has changed:

```sh
cd /path/to/openaf
./jre/bin/java -version
./jre/bin/java -jar openaf.jar --install
```

Preserve any deliberately configured truststore or JVM settings when migrating. See [portable Java downloads](../guides/ojobio/quickly_download_java.md) and [certificate installation](../guides/advanced/easily-add-ssl-cert.md).

## In container images

Select or rebuild an image containing the required Java version and recreate containers from it. Inspect the runtime inside the new container; a tag alone does not establish the Java version or update running containers.
