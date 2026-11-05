---
layout: default
title: iocore
parent: Reference
grand_parent: OpenAF docs
---

{% raw %}
## iocore

[Source: `06414cd9`](https://github.com/OpenAF/openaf/blob/06414cd9204e918daa1e2971ce904783299db333/src/openaf/core/IO.java) · [Baseline](../source-snapshot.md)

### io.convertFileToEncoding

`io.convertFileToEncoding(aOriginalFile, aNewFile, anEncoding)`

````text
Converts an original file into a new file using the provided enconding.
````

### io.cp

`io.cp(aSourceFilePath, aTargetFilePath)`

````text
Tries to copy aSourceFilePath to aTargetFilePath preserving file attributes.
````

### io.createTempDir

`io.createTempDir(aPrefix, aPath) : String`

````text
Creates a temporary directory with the provided aPrefix that will be deleted completly (all files and folders inside) upon execution exit. The absolute path for it is returned. Optionally, if aPath is defined, the temporary directory will be created in aPath.
````

### io.createTempFile

`io.createTempFile(aPrefix, aSuffix, aPath) : String`

````text
Creates a temporary file with the provided aPrefix and aSuffix that will be deleted upon execution exit. The absolute path for it is returned. Optionally, if aPath is defined, the temporary file will be created in aPath.
````

### io.fileExists

`io.fileExists(aFilename) : boolean`

````text
Returns true or false to determine if aFilename exists on the filesystem.
````

### io.fileInfo

`io.fileInfo(aFilePath, usePosix)`

````text
Returns a file map with filename, filepath, lastModified, createTime, lastAccess,  size, permissions, isDirectory and isFile. Alternatively you can specify to usePosix=true and it will add to the map the owner, group and full permissions of each file and folder.
````

### io.getCanonicalPath

`io.getCanonicalPath(aPath) : String`

````text
Returns the canonical path for the provided aPath either if the file/folder exists or not.
````

### io.getDefaultEncoding

`io.getDefaultEncoding()`

````text
Returns the current default encoding used.
````

### io.getFileEncoding

`io.getFileEncoding(aFile)`

````text
Tries to determine the file encoding of a given file and returns the same.
````

### io.gunzip

`io.gunzip(anArrayOfBytes) : anObject`

````text
Uncompresses a gziped array of bytes.
````

### io.gunzipStream

`io.gunzipStream(aInputStream, aOutputStream, shouldNotClose)`

Decompresses GZIP into raw bytes, copying Java streams with bounded memory and no object serialization.
Both streams close on success or processing failure unless `shouldNotClose` is true
(default false). Successful conversion finalizes and flushes output even when left open.
Invalid arguments are rejected before reading or closing streams. Errors propagate and
may leave partial output; cleanup errors are suppressed behind the original error.
Returns undefined. For example:

```javascript
io.gunzipStream(io.readFileStream("A.gz"), io.writeFileStream("A.decoded"));
```

### io.gzip

`io.gzip(anObject) : anArrayOfBytes`

````text
Compresses an object into an array of bytes.
````

### io.gzipStream

`io.gzipStream(aInputStream, aOutputStream, shouldNotClose)`

Compresses raw bytes into GZIP, copying Java streams with bounded memory and no object serialization.
Both streams close on success or processing failure unless `shouldNotClose` is true
(default false). Successful conversion finalizes and flushes output even when left open.
Invalid arguments are rejected before reading or closing streams. Errors propagate and
may leave partial output; cleanup errors are suppressed behind the original error.
Returns undefined. For example:

```javascript
io.gzipStream(io.readFileStream("A"), io.writeFileStream("A.gz"));
```

### io.listFilenames

`io.listFilenames(aFilePath, fullPath)`

````text
Returns a files array with a map with filepath (if fullPath = true) or filename otherwise.
````

### io.listFiles

`io.listFiles(aFilePath, usePosix)`

````text
Returns a files array with a map with filename, filepath, lastModified, createTime, lastAccess,  size, permissions, isDirectory and isFile for each entry on a file path. Alternatively you can specify to usePosix=true and it will add to the map the owner, group and full permissions of each file and folder.
````

### io.mkdir

`io.mkdir(aNewDirectory) : boolean`

````text
Tries to create aNewDirectory. Returns true if successfull, false otherwise.
````

### io.mv

`io.mv(aSourceFilePath, aTargetFilePath)`

````text
Tries to move aSourceFilePath to aTargetFilePath preserving file attributes.
````

### io.randomAccessFile

`io.randomAccessFile(aFilename, aMode) : RandomAccessFile`

````text
Creates a java RandomAccessFile to enable random access to files and returns the same.
````

### io.readFile

`io.readFile(aFilename, anEncoding)`

````text
Reads a file auto detecting between JSON, ParameterMap, PMap and configuration PMap, optionally providing an encoding.
Note: aFilename can contain "a.zip::afile" to read from zip files.
````

### io.readFileAsArray

`io.readFileAsArray(aFilename, anEncoding)`

````text
Reads a file, optionally providing a specific encoding to use, and returns an array where each  line is an array element.
````

### io.readFileBytes

`io.readFileBytes(aFilename)`

````text
Reads a file into an array of bytes.
Note: aFilename can contain "a.zip::afile" to read from zip files.
````

### io.readFileGzipStream

`io.readFileGzipStream(aFilename) : JavaStream`

Creates and returns a JavaStream to read from a gzip `aFilename`. For example:

```javascript
var stream = io.readFileGzipStream("afile.txt.gz");
ioStreamRead(stream, function(buffer) { // you can also use ioStreamReadBytes
   printnl(buffer);
});
stream.close();
```

### io.readFileStream

`io.readFileStream(aFilename) : JavaStream`

Creates and returns a JavaStream to read `aFilename`. For example:

```javascript
var stream = io.readFileStream("afile.txt");
ioStreamRead(stream, function(buffer) { // you can also use ioStreamReadBytes
   printnl(buffer);
});
stream.close();
```

### io.readFileString

`io.readFileString(aFilename, anEncoding)`

````text
Reads a file, optionally providing a specific encoding to use, and returns a string with the entire contents of the file.
Note: aFilename can contain "a.zip::afile" to read from zip files.
````

### io.readFileXML

`io.readFileXML(aFilename, numOfLinesToSkip, anEncoding)`

````text
Reads a file, optionally providing a specific encoding to use and/or the number of lines to skip (e.g. 1 to exclude the xml main header) and returns the contents in a XML object.
Note: aFilename can contain "a.zip::afile" to read from zip files.
````

### io.rename

`io.rename(aSourceFilePath, aTargetFilePath)`

````text
Tries to rename aSourceFilePath to aTargetFilePath.
````

### io.rm

`io.rm(aFilePath)`

````text
Tries to delete a file or a directory on the provided aFilePath. In case it's a directory it will try to  recursively delete all directory contents.
````

### io.writeFile

`io.writeFile(aFilename, aJSONobject, anEncoding, shouldAppend)`

````text
Writes a JSON object into the given filename, optionally with the provided encoding and/or determine if it shouldAppend to an existing file.
````

### io.writeFileAsArray

`io.writeFileAsArray(aFilename, anArrayOfLines, anEncoding)`

````text
Writes an array of string lines into a file, optionally with the provided encoding
````

### io.writeFileBytes

`io.writeFileBytes(aFilename, anArrayOfBytes)`

````text
Writes an array of bytes into the given filename.
````

### io.writeFileGzipStream

`io.writeFileGzipStream(aFilename, shouldAppend) : JavaStream`

Creates and returns a JavaStream to write to a gzip `aFilename`. Optionally if `shouldAppend`=true
it will append to an existing file. For example:

```javascript
var stream = io.writeFileGzipStream("afile.txt.gz");
ioStreamWrite(stream, "Hello "); // you can also use ioStreamWriteBytes
ioStreamWrite(stream, "World!");
stream.close();
```

### io.writeFileStream

`io.writeFileStream(aFilename, shouldAppend) : JavaStream`

Creates and returns a JavaStream to write to `aFilename`. If `shouldAppend` = true the stream will
append to the existing file. For example:

```javascript
var stream = io.writeFileStream("afile.txt");
ioStreamWrite(stream, "Hello "); // you can also use ioStreamWriteBytes
ioStreamWrite(stream, "World!");
stream.close();
```

### io.writeFileString

`io.writeFileString(aFilename, aString, anEncoding, shouldAppend)`

````text
Writes a string into the given filename, optionally with the provided encoding and/or determine if it shouldAppend to an existing file.
````

### io.writeFileXML

`io.writeFileXML(aFilename, aXMLobject, anEncoding, shouldAppend)`

````text
Writes a XML object into the given filename, optionally with the provided encoding and/or determine if it shouldAppend to an existing file.
````
{% endraw %}
