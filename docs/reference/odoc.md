---
layout: default
title: odoc
parent: Reference
grand_parent: OpenAF docs
---

{% raw %}
## odoc

[Source: `06414cd9`](https://github.com/OpenAF/openaf/blob/06414cd9204e918daa1e2971ce904783299db333/js/odoc.js) · [Baseline](../source-snapshot.md)

### ODoc

`ODoc(aoDoc)`

````text
Object to hold an ODoc, the basic structure for OpenAF documentation. You can provide a ODoc structure to initialize this ODoc object.
````

### ODoc.add

`ODoc.add(aKey, aFullKey, aValue, aFormat)`

````text
Adds a ODoc entry given a key (a unique name), a full key (a function or object signature) and a corresponding text value. Optionally set aFormat to "markdown" or "md" to enable Markdown display.
````

### ODoc.addAll

`ODoc.addAll(aODoc)`

````text
Adds an ODoc Map structure imported from another ODoc object.
````

### ODoc.get

`ODoc.get(aKey) : Map`

````text
Returns the ODoc entry corresponding to the unique key provided.
````

### ODoc.getAll

`ODoc.getAll() : Map`

````text
Returns the ODoc entire Map structure to be exported somewhere else.
````

### ODoc.getKeys

`ODoc.getKeys() : Array`

````text
Returns an array with all keys from this ODoc.
````

### ODocs

`ODocs(aPath, aODocs, anArrayURLs, offline)`

````text
Object to hold ODocs objects, search them, load or save them (either offline or online). The parameter aPath can be a directory containing .odoc.db, a standalone database ZIP, or a JAR/ZIP containing .odoc.db. Saving requires a directory path. The parameter aODocs is optional but it can be used to link with ODocsGen contents (e.g (new ODocsGen(aMapOfFiles)).getODoc())). It's also possible to additionally specify anArrayURLs to load ODocs via web. Optional you can force it to only work offline (offline = true)
````

### ODocs.addAll

`ODocs.addAll(aODoc)`

````text
Add an external ODocs structure into these object.
````

### ODocs.get

`ODocs.get(aID, aKey) : Map`

````text
Returns the raw entry for a subject and key, loading missing subjects lazily and retaining cached entries. Returns undefined if the entry cannot be found. Offline mode prevents web fallback.
````

### ODocs.getODoc

`ODocs.getODoc(aID) : ODoc`

````text
Returns a currently loaded subject without loading it. Returns undefined if the subject is not cached.
````

### ODocs.load

`ODocs.load(aID, aFilename)`

````text
Loads a local documentation index and optionally one subject. Uses the remembered subject source or constructor path when aFilename is omitted. Accepts directories and standalone or nested ZIP archives.
````

### ODocs.loadFile

`ODocs.loadFile(aPath)`

````text
Loads a local documentation index. Defaults to the constructor path. Online fallback and background refresh are enabled only when offline is false and no explicit aPath was supplied.
````

### ODocs.loadWeb

`ODocs.loadWeb(aID) : Boolean`

````text
Loads web documentation from the configured URLs, trying the next URL on invalid responses. Without aID, loads only the index. Returns false when offline or loading fails.
````

### ODocs.save

`ODocs.save()`

````text
Saves the current ODocs into .odoc.db in the directory provided on the constructor in a way suitable for offline use.
````

### ODocs.saveWeb

`ODocs.saveWeb()`

````text
Saves the current ODocs into the path provided on the constructor with files suitable for loading from web.
````

### ODocs.search

`ODocs.search(aTerm, anArrayOfIds) : Array`

````text
Returns id/key candidates across the selected subjects. Prefers case-sensitive exact keys, then case-insensitive exact keys, then substrings. Ambiguous keys retain each matching subject.
````

### ODocsGen

`ODocsGen(aMapOfFiles) : ODocsGen`

````text
Object to generate ODocs structures. Given a map where the key is a ODoc subject and the value is the filesystem path to a javascript or Java source file (e.g. new ODocsGen({"sample": "/some/place/source.java"})). It finds text within odoc xml tags and adds it as odoc text. Inside the odoc xml tags you should have a key xml tag to specify a unique key within a ODoc subject (the key will be interpreted until the first '(', '{' or '[' occurs). Per standard practice you should specify the entire signature of a function when describing one.
````

### ODocsGen.genODoc

`ODocsGen.genODoc(aFileName) : ODoc`

````text
Generates a ODoc map where each key will be the identified odoc key and the value a map where k will represent the original key and t the associated text.
````

### ODocsGen.genODocs

`ODocsGen.genODocs()`

````text
The main execution function. Will generate odoc structures for all the files provided to this object
````

### ODocsGen.getODoc

`ODocsGen.getODoc() : Map`

````text
Gets the current odoc maps per id.
````

### ODocsGen.getODocKeys

`ODocsGen.getODocKeys() : Map`

````text
Gets the current odocs keys per id.
````
{% endraw %}
