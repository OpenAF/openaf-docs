---
layout: default
title: bsdiff
parent: Reference
grand_parent: OpenAF docs
---

{% raw %}
## bsdiff

[Source: `06414cd9`](https://github.com/OpenAF/openaf/blob/06414cd9204e918daa1e2971ce904783299db333/src/openaf/plugins/BSDiff.java) · [Baseline](../source-snapshot.md)

### BSDiff.BSDiff

`BSDiff.BSDiff()`

````text
Creates a new BSDiff instance to diff and patch binary files.
````

### BSDiff.diff

`BSDiff.diff(anOldFile, aNewFile, aPatchFile)`

````text
Given anOldFile and aNewFile binary file, the two will be compared and a new compressed aPatchFile will be generated. Check compression to be used with BSDiff.getCompression().
````

### BSDiff.diffBytes

`BSDiff.diffBytes(oldArrayOfBytes, newArrayOfBytes) : ArrayOfBytes`

````text
Given oldArrayOfBytes and newArrayOfBytes, the two will be compared and a new compressed ArrayOfBytes will be generated and returned. Check compression to be used with BSDiff.getCompression().
````

### BSDiff.getCompression

`BSDiff.getCompression() : String`

````text
Returns the current compression method in use.
````

### BSDiff.patchBytes

`BSDiff.patchBytes(oldFile, patchFile, newFile) : ArrayOfBytes`

````text
Given an oldFile will apply a patchFile (produced by diff/diffBytes) and write the result to newFile.
````

### BSDiff.setCompression

`BSDiff.setCompression(aCompression)`

````text
Sets a different compression method to be used (based on Apache Commons Compression available methods).
````
{% endraw %}
