---
layout: default
title: io
parent: Reference
grand_parent: OpenAF docs
---

### io.readFileJavaParameterMap

__io.readFileJavaParameterMap(aFilename, anEncoding, aNumLines) : JavaParameterMap__

````
Reads a given aFilename as a Java ParameterMap, optionally providing an encoding and aNumLines to skip.

````
### io.readFileJavaPMap

__io.readFileJavaPMap(aFilename, anEncoding, aNumLines) : JavaParameterMap__

````
Reads a given aFilename (in PMap format) as a Java ParameterMap, optionally providing an encoding and aNumLines to skip.

````
### io.readFileParameterMap

__io.readFileParameterMap(aFilename, anEncoding)__

````
Reads a given file as ParameterMap, optionally providing an encoding.
Note: aFilename can contain "a.zip::afile" to read from zip files.
````
### io.readFilePMap

__io.readFilePMap(aFilename, anEncoding)__

````
Reads a given file as PMap, optionally providing an encoding.
Note: aFilename can contain "a.zip::afile" to read from zip files.
````
### io.writeFileConfigPMap

__io.writeFileConfigPMap(aFilename, aJSONobject, anEncoding)__

````
Writes a JSON object into a config PMap file, optionally providing an encoding
````
### io.writeFileJavaParameterMap

__io.writeFileJavaParameterMap(aFilename, aPMIn, anEncoding)__

````
Writes a ParameterMap aFilename given aPMIn Java Parameter Map, optionally providing an encoding
````
### io.writeFileJavaPMap

__io.writeFileJavaPMap(aFilename, aPMIn, anEncoding)__

````
Writes a PMap aFilename given aPMIn Java Parameter Map, optionally providing an encoding
````
### io.writeFileParameterMap

__io.writeFileParameterMap(aFilename, aJSONobject, anEncoding)__

````
Writes a JSON object into a parameter map, optionally providing an encoding
````
### io.writeFilePMap

__io.writeFilePMap(aFilename, aJSONobject, anEncoding)__

````
Writes a JSON object into a PMap, optionally providing an encoding
````

### io.convertFileToEncoding

__io.convertFileToEncoding(aOriginalFile, aNewFile, anEncoding)__

````
Converts an original file into a new file using the provided enconding.
````
### io.convertFileToEncoding

__io.convertFileToEncoding(aOriginalFile, aNewFile, anEncoding)__

````
Converts an original file into a new file using the provided enconding.
````
### io.cp

__io.cp(aSourceFilePath, aTargetFilePath)__

````
Tries to copy aSourceFilePath to aTargetFilePath preserving file attributes.
````
### io.cp

__io.cp(aSourceFilePath, aTargetFilePath)__

````
Tries to copy aSourceFilePath to aTargetFilePath preserving file attributes.
````
### io.createTempFile

__io.createTempFile(aPrefix, aSuffix) : String__

````
Creates a temporary with the provided aPrefix and aSuffix that will be deleted upon execution exit. The absolute path for it is returned.
````
### io.createTempFile

__io.createTempFile(aPrefix, aSuffix) : String__

````
Creates a temporary with the provided aPrefix and aSuffix that will be deleted upon execution exit. The absolute path for it is returned.
````
### io.fileExists

__io.fileExists(aFilename) : boolean__

````
Returns true or false to determine if aFilename exists on the filesystem.
````
### io.fileExists

__io.fileExists(aFilename) : boolean__

````
Returns true or false to determine if aFilename exists on the filesystem.
````
### io.fileInfo

__io.fileInfo(aFilePath)__

````
Returns a file map with filename, filepath, lastModified, createTime, lastAccess,  size, permissions, isDirectory and isFile.
````
### io.fileInfo

__io.fileInfo(aFilePath)__

````
Returns a file map with filename, filepath, lastModified, createTime, lastAccess,  size, permissions, isDirectory and isFile.
````
### io.getCanonicalPath

__io.getCanonicalPath(aPath) : String__

````
Returns the canonical path for the provided aPath either if the file/folder exists or not.
````
### io.getCanonicalPath

__io.getCanonicalPath(aPath) : String__

````
Returns the canonical path for the provided aPath either if the file/folder exists or not.
````
### io.getDefaultEncoding

__io.getDefaultEncoding()__

````
Returns the current default encoding used.
````
### io.getDefaultEncoding

__io.getDefaultEncoding()__

````
Returns the current default encoding used.
````
### io.getFileEncoding

__io.getFileEncoding(aFile)__

````
Tries to determine the file encoding of a given file and returns the same.
````
### io.getFileEncoding

__io.getFileEncoding(aFile)__

````
Tries to determine the file encoding of a given file and returns the same.
````
### io.gunzip

__io.gunzip(anArrayOfBytes) : anObject__

````
Uncompresses a gziped array of bytes.
````
### io.gunzip

__io.gunzip(anArrayOfBytes) : anObject__

````
Uncompresses a gziped array of bytes.
````
### io.gzip

__io.gzip(anObject) : anArrayOfBytes__

````
Compresses an object into an array of bytes.
````
### io.gzip

__io.gzip(anObject) : anArrayOfBytes__

````
Compresses an object into an array of bytes.
````
### io.listFilenames

__io.listFilenames(aFilePath, fullPath)__

````
Returns a files array with a map with filepath (if fullPath = true) or filename otherwise.
````
### io.listFilenames

__io.listFilenames(aFilePath, fullPath)__

````
Returns a files array with a map with filepath (if fullPath = true) or filename otherwise.
````
### io.listFiles

__io.listFiles(aFilePath, usePosix)__

````
Returns a files array with a map with filename, filepath, lastModified, createTime, lastAccess,  size, permissions, isDirectory and isFile for each entry on a file path. Alternatively you can specify to usePosix=true and it will add to the map the owner, group and full permissions of each file and folder.
````
### io.listFiles

__io.listFiles(aFilePath, usePosix)__

````
Returns a files array with a map with filename, filepath, lastModified, createTime, lastAccess,  size, permissions, isDirectory and isFile for each entry on a file path. Alternatively you can specify to usePosix=true and it will add to the map the owner, group and full permissions of each file and folder.
````
### io.mkdir

__io.mkdir(aNewDirectory) : boolean__

````
Tries to create aNewDirectory. Returns true if successfull, false otherwise.
````
### io.mkdir

__io.mkdir(aNewDirectory) : boolean__

````
Tries to create aNewDirectory. Returns true if successfull, false otherwise.
````
### io.mv

__io.mv(aSourceFilePath, aTargetFilePath)__

````
Tries to move aSourceFilePath to aTargetFilePath preserving file attributes.
````
### io.mv

__io.mv(aSourceFilePath, aTargetFilePath)__

````
Tries to move aSourceFilePath to aTargetFilePath preserving file attributes.
````
### io.randomAccessFile

__io.randomAccessFile(aFilename, aMode) : RandomAccessFile__

````
Creates a java RandomAccessFile to enable random access to files and returns the same.
````
### io.randomAccessFile

__io.randomAccessFile(aFilename, aMode) : RandomAccessFile__

````
Creates a java RandomAccessFile to enable random access to files and returns the same.
````
### io.readFile

__io.readFile(aFilename, anEncoding)__

````
Reads a file auto detecting between JSON, ParameterMap, PMap and configuration PMap, optionally providing an encoding.
Note: aFilename can contain "a.zip::afile" to read from zip files.
````
### io.readFile

__io.readFile(aFilename, anEncoding)__

````
Reads a file auto detecting between JSON, ParameterMap, PMap and configuration PMap, optionally providing an encoding.
Note: aFilename can contain "a.zip::afile" to read from zip files.
````
### io.readFileAsArray

__io.readFileAsArray(aFilename, anEncoding)__

````
Reads a file, optionally providing a specific encoding to use, and returns an array where each  line is an array element.
````
### io.readFileAsArray

__io.readFileAsArray(aFilename, anEncoding)__

````
Reads a file, optionally providing a specific encoding to use, and returns an array where each  line is an array element.
````
### io.readFileBytes

__io.readFileBytes(aFilename)__

````
Reads a file into an array of bytes.
Note: aFilename can contain "a.zip::afile" to read from zip files.
````
### io.readFileBytes

__io.readFileBytes(aFilename)__

````
Reads a file into an array of bytes.
Note: aFilename can contain "a.zip::afile" to read from zip files.
````
### io.readFileGzipStream

__io.readFileGzipStream(aFilename) : JavaStream__

````
Creates and returns a JavaStream to read from a gzip aFilename. For example:

var stream = io.readFileGzipStream("afile.txt.gz");
ioStreamRead(stream, function(buffer) { // you can also use ioStreamReadBytes 
   printnl(buffer);
});
stream.close();


````
### io.readFileGzipStream

__io.readFileGzipStream(aFilename) : JavaStream__

````
Creates and returns a JavaStream to read from a gzip aFilename. For example:

var stream = io.readFileGzipStream("afile.txt.gz");
ioStreamRead(stream, function(buffer) { // you can also use ioStreamReadBytes 
   printnl(buffer);
});
stream.close();


````
### io.readFileStream

__io.readFileStream(aFilename) : JavaStream__

````
Creates and returns a JavaStream to read aFilename. For example:

var stream = io.readFileStream("afile.txt");
ioStreamRead(stream, function(buffer) { // you can also use ioStreamReadBytes 
   printnl(buffer);
});
stream.close();


````
### io.readFileStream

__io.readFileStream(aFilename) : JavaStream__

````
Creates and returns a JavaStream to read aFilename. For example:

var stream = io.readFileStream("afile.txt");
ioStreamRead(stream, function(buffer) { // you can also use ioStreamReadBytes 
   printnl(buffer);
});
stream.close();


````
### io.readFileString

__io.readFileString(aFilename, anEncoding)__

````
Reads a file, optionally providing a specific encoding to use, and returns a string with the entire contents of the file.
Note: aFilename can contain "a.zip::afile" to read from zip files.
````
### io.readFileString

__io.readFileString(aFilename, anEncoding)__

````
Reads a file, optionally providing a specific encoding to use, and returns a string with the entire contents of the file.
Note: aFilename can contain "a.zip::afile" to read from zip files.
````
### io.readFileXML

__io.readFileXML(aFilename, numOfLinesToSkip, anEncoding)__

````
Reads a file, optionally providing a specific encoding to use and/or the number of lines to skip (e.g. 1 to exclude the xml main header) and returns the contents in a XML object.
Note: aFilename can contain "a.zip::afile" to read from zip files.
````
### io.readFileXML

__io.readFileXML(aFilename, numOfLinesToSkip, anEncoding)__

````
Reads a file, optionally providing a specific encoding to use and/or the number of lines to skip (e.g. 1 to exclude the xml main header) and returns the contents in a XML object.
Note: aFilename can contain "a.zip::afile" to read from zip files.
````
### io.rename

__io.rename(aSourceFilePath, aTargetFilePath)__

````
Tries to rename aSourceFilePath to aTargetFilePath.
````
### io.rename

__io.rename(aSourceFilePath, aTargetFilePath)__

````
Tries to rename aSourceFilePath to aTargetFilePath.
````
### io.rm

__io.rm(aFilePath)__

````
Tries to delete a file or a directory on the provided aFilePath. In case it's a directory it will try to  recursively delete all directory contents.
````
### io.rm

__io.rm(aFilePath)__

````
Tries to delete a file or a directory on the provided aFilePath. In case it's a directory it will try to  recursively delete all directory contents.
````
### io.writeFile

__io.writeFile(aFilename, aJSONobject, anEncoding, shouldAppend)__

````
Writes a JSON object into the given filename, optionally with the provided encoding and/or determine if it shouldAppend to an existing file.
````
### io.writeFile

__io.writeFile(aFilename, aJSONobject, anEncoding, shouldAppend)__

````
Writes a JSON object into the given filename, optionally with the provided encoding and/or determine if it shouldAppend to an existing file.
````
### io.writeFileAsArray

__io.writeFileAsArray(aFilename, anArrayOfLines, anEncoding)__

````
Writes an array of string lines into a file, optionally with the provided encoding
````
### io.writeFileAsArray

__io.writeFileAsArray(aFilename, anArrayOfLines, anEncoding)__

````
Writes an array of string lines into a file, optionally with the provided encoding
````
### io.writeFileBytes

__io.writeFileBytes(aFilename, anArrayOfBytes)__

````
Writes an array of bytes into the given filename.
````
### io.writeFileBytes

__io.writeFileBytes(aFilename, anArrayOfBytes)__

````
Writes an array of bytes into the given filename.
````
### io.writeFileGzipStream

__io.writeFileGzipStream(aFilename) : JavaStream__

````
Creates and returns a JavaStream to write to a gzip aFilename. For example:

var stream = io.writeFileGzipStream("afile.txt.gz");
ioStreamWrite(stream, "Hello "); // you can also use ioStreamWriteBytes 
ioStreamWrite(stream, "World!");
stream.close();


````
### io.writeFileGzipStream

__io.writeFileGzipStream(aFilename) : JavaStream__

````
Creates and returns a JavaStream to write to a gzip aFilename. For example:

var stream = io.writeFileGzipStream("afile.txt.gz");
ioStreamWrite(stream, "Hello "); // you can also use ioStreamWriteBytes 
ioStreamWrite(stream, "World!");
stream.close();


````
### io.writeFileStream

__io.writeFileStream(aFilename, shouldAppend) : JavaStream__

````
Creates and returns a JavaStream to write to aFilename. If shouldAppend = true the stream will  append to the existing file. For example:

var stream = io.writeFileStream("afile.txt");
ioStreamWrite(stream, "Hello "); // you can also use ioStreamWriteBytes 
ioStreamWrite(stream, "World!");
stream.close();


````
### io.writeFileStream

__io.writeFileStream(aFilename, shouldAppend) : JavaStream__

````
Creates and returns a JavaStream to write to aFilename. If shouldAppend = true the stream will  append to the existing file. For example:

var stream = io.writeFileStream("afile.txt");
ioStreamWrite(stream, "Hello "); // you can also use ioStreamWriteBytes 
ioStreamWrite(stream, "World!");
stream.close();


````
### io.writeFileString

__io.writeFileString(aFilename, aString, anEncoding, shouldAppend)__

````
Writes a string into the given filename, optionally with the provided encoding and/or determine if it shouldAppend to an existing file.
````
### io.writeFileString

__io.writeFileString(aFilename, aString, anEncoding, shouldAppend)__

````
Writes a string into the given filename, optionally with the provided encoding and/or determine if it shouldAppend to an existing file.
````
### io.writeFileXML

__io.writeFileXML(aFilename, aXMLobject, anEncoding, shouldAppend)__

````
Writes a XML object into the given filename, optionally with the provided encoding and/or determine if it shouldAppend to an existing file.
````
### io.writeFileXML

__io.writeFileXML(aFilename, aXMLobject, anEncoding, shouldAppend)__

````
Writes a XML object into the given filename, optionally with the provided encoding and/or determine if it shouldAppend to an existing file.
````
