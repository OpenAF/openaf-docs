---
layout: default
title: How to copy a remote oJob
parent: oJobIO
grand_parent: Guides
---

# How to copy a remote oJob

If you want to run locally an YAML/JSON from a remote site, like [oJob.io](../../concepts/oJobIO.md), you can execute:

````
ojob ojob.io/get job=ojob.io/es/export > exportFromES.yaml
````

This will create a local exportFromES.yaml file that, when you run it, will be the [exact functionality as ojob.io/es/export](elasticsearch-import-export.md).

But if you are in an internet-less network and you might not have the necessary ElasticSearch [oPack](../../concepts/oPack.md)?
You have two options: manually download the oPack from https://openaf.io/opacks/ElasticSearch.opack OR user the 'airgap=true' option.

## AirGap option

The airgap option will try to download all the necessary files for you to run the oJob mentioned in the option _"job="_ in an Internet-less/offline environment. You should start by creating an empty folder:

````
mkdir export
````

````
ojob ojob.io/get job=ojob.io/es/export airgap=true
````

This will create, in the current folder (e.g. export), a copy of ojob.io/es/export as "ojob.io_es_export.yaml" and a subfolder with the ElasticSearch oPack.

Everytime you use the _"airgap=true"_ option the ojob.io/get will try to determine **all oPacks** that you might need, download them and write in the current folder.

In the end you just have to pack the current folder (e.g. zip it, create a tgz, etc...) a transport the contents to your target system.
