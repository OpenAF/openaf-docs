---
layout: default
title: oPack
parent: Concepts
grand_parent: OpenAF docs
---
# oPack

OpenAF comes with a minimalist and simple package manager. The idea is to enable OpenAF to extend it’s functionalities in a modular way.

The basic unit is an oPack (*o-pack*). A simple ZIP file containing the package contents and a special file with the package definition: *.package.yaml* (or *.package.json*)

These oPack files can be hosted in oPack servers to which OpenAF will connect for:

   * Installing a new oPack
   * Updating an existing oPack
   * Searching for provided oPacks

oPack servers can be public or private. OpenAF comes with a pre-defined oPack server but it’s possible to add other public and private oPack servers.

## Using the oPack command

After installing OpenAF an oPack script will be available to access the oPack functionality.

By default, all oPacks are installed under the same directory from where OpenAF is installed.

*tbc*

### List of all oPack commands

The following lists all the available oPack commands *verbs* that can be used:

| Command | Description | Example |
|--------:|:-----------|:--------|
| install | Will try to install an oPack from a local file, a local folder or from a configured remote central repository. | ````opack install apis````<br/>````opack install /my/dir````<br/>````opack install myPack.opack```` |
| update | Will try to update an oPack from a local file, a local folder or from a configured remote central repository. | ````opack update apis````<br/>````opack update /my/dir````<br/>````opack update myPack.opack```` | 
| erase | Will erase an oPack from the current installation. | ````opack erase myPack```` |
| remove | Removes an oPack entry from the local OpenPack database. Supports an **interactive mode** that prompts for confirmation before removal. | ````opack remove myPack```` |
| search | Will search an oPack by keywords on the configured remote central repositories. | ````opack search docker```` |

## How to create an oPack

## How to setup an oPack Server