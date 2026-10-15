---
layout: default
title: zip
parent: Reference
grand_parent: OpenAF docs
---


## zip

### ZIP.clean

__ZIP.clean()__

````
Will clean all internal data regarding any previously ZIP contents handled by this object.
````
### ZIP.close

__ZIP.close()__

````
Closes the loaded ZIP file and all outstanding entry streams associated with this object.
````
### ZIP.generate

__ZIP.generate(aMapOfOptions, dontReload) : anArrayOfBytes__

````
Will generate a ZIP anArrayOfBytes contents (that can then by saved into a file) given the provided options (a map where you can specify the compressionLevel as a number). If dontReload = true then the internal ZIP object contents won't be reloaded after generating. Example:

plugin("ZIP");
var zip = new ZIP();
var text = new java.lang.String("Some example test to zip into a zip file");
var openaf = io.readFileBytes("c:\\apps\\OpenAF\\openaf.jar");
zip.putFile("text.txt", text.getBytes());
zip.putFile("openaf.jar", openaf);
var newZip = zip.generate({"compressionLevel": 9});
var zip = new ZIP(newZip);
print(beautifier(zip.list()));


````
### ZIP.generate2File

__ZIP.generate2File(aFile, aMapOfOptions, dontReload) : anArrayOfBytes__

````
Will generate a ZIP into aFile given the provided options (a map where you can specify the compressionLevel as a number). If dontReload = true then the internal ZIP object contents won't be reloaded after generating.
````
### ZIP.getFile

__ZIP.getFile(aFilename) : anArrayOfBytes__

````
Will uncompress the corresponding aFilename from the ZIP contents into an array of bytes. Returns null if the entry is absent.
````
### ZIP.gunzip

__ZIP.gunzip(anArrayOfBytes) : anObject__

````
Will gunzip/uncompress the provided anArrayOfBytes into the original anObject compressed with ZIP.gzip.
````
### ZIP.gzip

__ZIP.gzip(anObject) : ArrayOfBytes__

````
Will gzip/compress the contents of the anObject into an array of bytes. To uncompress use ZIP.gunzip.
````
### ZIP.list

__ZIP.list(aFilePath) : Map__

````
Will list all files and folders of the loaded ZIP contents into a Map with name, size, compressedSize, comment, crc and time. Optionally you can provide a zip aFilePath instead of using the current in-memory zip.
````
### ZIP.load

__ZIP.load(anArrayOfBytes)__

````
Loads anArrayOfBytes ZIP contents into the internal object structures.
````
### ZIP.loadFile

__ZIP.loadFile(aFilename)__

````
Will load a ZIP file aFilename into the ZIP object internal structure.
````
### ZIP.putFile

__ZIP.putFile(aFilename, anArrayOfBytes)__

````
Will add anArrayOfBytes to the ZIP contents as aFilename.
````
### ZIP.remove

__ZIP.remove(aFilename)__

````
Will remove aFilename from the ZIP contents.
````
### ZIP.streamCreate

__ZIP.streamCreate(aFilePath)__

````
Creates an empty ZIP file on aFilePath.
````
### ZIP.streamCreateFolder

__ZIP.streamCreateFolder(aFilePath, aFolder) : boolean__

````
Creates aFolder on aFilePath ZIP file. Returns true if the folder was created or false if it already existed.
````
### ZIP.streamGetFile

__ZIP.streamGetFile(aFilePath, aName) : anArrayOfBytes__

````
Retrieves aName file from aFilePath zip file without loading the zip file contents into memory returning the  file contents as an array of bytes, or null if the entry is absent. Uses an independent archive handle.
````
### ZIP.streamGetFileStream

__ZIP.streamGetFileStream(aFilePath, aName) : JavaInputStream__

````
Retrieves aName file from aFilePath zip file without loading the zip file contents into memory returning a  Java InputStream, or null if the entry is absent. Each stream owns an independent archive handle. Close the stream after use to release that handle. ZIP.close() also closes outstanding streams.
````
### ZIP.streamPutFile

__ZIP.streamPutFile(aFilePath, aName, anArrayOfBytes)__

````
Sets a aName file on the aFilePath ZIP provided with the anArrayOfBytes provided. All missing directories will be created.
````
### ZIP.streamPutFileStream

__ZIP.streamPutFileStream(aFilePath, aName, aJavaInputStream, useTempFile)__

````
Sets a aName file on the aFilePath ZIP provided with the aJavaInputStream provided. All missing directories will be created. Optionally you can specify if a temp file should be used instead of memory (useTempFile = true).  Additionally, for performance, you can provide an array of maps (composed of "n" name of file and "s" javaInputStream) instead of  aJavaInputStream (aName will be ignored in this case).
````
### ZIP.streamRemoveFile

__ZIP.streamRemoveFile(aFilePath, aName)__

````
Removes a file/directory aName from the aFilePath ZIP file provided.
````
### ZIP.ZIP

__ZIP.ZIP(anArrayOfBytes) : ZIP__

````
Creates a ZIP object instance. If anArrayOfBytes is provided it will read it as a ZIP compressed contents into the ZIP object.
````
