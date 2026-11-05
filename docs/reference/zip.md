---
layout: default
title: zip
parent: Reference
grand_parent: OpenAF docs
---

{% raw %}
## zip

[Source: `06414cd9`](https://github.com/OpenAF/openaf/blob/06414cd9204e918daa1e2971ce904783299db333/src/openaf/plugins/ZIP.java) · [Baseline](../source-snapshot.md)

### ZIP.ZIP

`ZIP.ZIP(anArrayOfBytes) : ZIP`

````text
Creates a ZIP object instance. If anArrayOfBytes is provided it will read it as a ZIP compressed contents into the ZIP object.
````

### ZIP.clean

`ZIP.clean()`

````text
Will clean all internal data regarding any previously ZIP contents handled by this object.
````

### ZIP.close

`ZIP.close()`

````text
Closes the loaded ZIP file and all outstanding entry streams associated with this object.
````

### ZIP.generate

`ZIP.generate(aMapOfOptions, dontReload) : anArrayOfBytes`

Will generate a ZIP `anArrayOfBytes` contents (that can then by saved into a file) given the provided options (a map
where you can specify the compressionLevel as a number). If `dontReload` = true then the internal ZIP object contents
won't be reloaded after generating. Example:

```javascript
plugin("ZIP");
var zip = new ZIP();
var text = new java.lang.String("Some example test to zip into a zip file");
var openaf = io.readFileBytes("c:\\apps\\OpenAF\\openaf.jar");
zip.putFile("text.txt", text.getBytes());
zip.putFile("openaf.jar", openaf);
var newZip = zip.generate({"compressionLevel": 9});
var zip = new ZIP(newZip);
print(beautifier(zip.list()));
```

### ZIP.generate2File

`ZIP.generate2File(aFile, aMapOfOptions, dontReload) : anArrayOfBytes`

````text
Will generate a ZIP into aFile given the provided options (a map where you can specify the compressionLevel as a number). If dontReload = true then the internal ZIP object contents won't be reloaded after generating.
````

### ZIP.getFile

`ZIP.getFile(aFilename) : anArrayOfBytes`

````text
Will uncompress the corresponding aFilename from the ZIP contents into an array of bytes. Returns null if the entry is absent.
````

### ZIP.gunzip

`ZIP.gunzip(anArrayOfBytes) : anObject`

````text
Will gunzip/uncompress the provided anArrayOfBytes into the original anObject compressed with ZIP.gzip.
````

### ZIP.gzip

`ZIP.gzip(anObject) : ArrayOfBytes`

````text
Will gzip/compress the contents of the anObject into an array of bytes. To uncompress use ZIP.gunzip.
````

### ZIP.list

`ZIP.list(aFilePath) : Map`

````text
Will list all files and folders of the loaded ZIP contents into a Map with name, size, compressedSize, comment, crc and time. Optionally you can provide a zip aFilePath instead of using the current in-memory zip.
````

### ZIP.load

`ZIP.load(anArrayOfBytes)`

````text
Loads anArrayOfBytes ZIP contents into the internal object structures.
````

### ZIP.loadFile

`ZIP.loadFile(aFilename)`

````text
Will load a ZIP file aFilename into the ZIP object internal structure.
````

### ZIP.putFile

`ZIP.putFile(aFilename, anArrayOfBytes)`

````text
Will add anArrayOfBytes to the ZIP contents as aFilename.
````

### ZIP.remove

`ZIP.remove(aFilename)`

````text
Will remove aFilename from the ZIP contents.
````

### ZIP.streamCreate

`ZIP.streamCreate(aFilePath)`

````text
Creates an empty ZIP file on aFilePath.
````

### ZIP.streamCreateFolder

`ZIP.streamCreateFolder(aFilePath, aFolder) : boolean`

````text
Creates aFolder on aFilePath ZIP file. Returns true if the folder was created or false if it already existed.
````

### ZIP.streamGetFile

`ZIP.streamGetFile(aFilePath, aName) : anArrayOfBytes`

````text
Retrieves aName file from aFilePath zip file without loading the zip file contents into memory returning the  file contents as an array of bytes, or null if the entry is absent. Uses an independent archive handle.
````

### ZIP.streamGetFileStream

`ZIP.streamGetFileStream(aFilePath, aName) : JavaInputStream`

````text
Retrieves aName file from aFilePath zip file without loading the zip file contents into memory returning a  Java InputStream, or null if the entry is absent. Each stream owns an independent archive handle. Close the stream after use to release that handle. ZIP.close() also closes outstanding streams.
````

### ZIP.streamPutFile

`ZIP.streamPutFile(aFilePath, aName, anArrayOfBytes)`

````text
Sets a aName file on the aFilePath ZIP provided with the anArrayOfBytes provided. All missing directories will be created.
````

### ZIP.streamPutFileStream

`ZIP.streamPutFileStream(aFilePath, aName, aJavaInputStream, useTempFile)`

````text
Sets a aName file on the aFilePath ZIP provided with the aJavaInputStream provided. All missing directories will be created. Optionally you can specify if a temp file should be used instead of memory (useTempFile = true).  Additionally, for performance, you can provide an array of maps (composed of "n" name of file and "s" javaInputStream) instead of  aJavaInputStream (aName will be ignored in this case).
````

### ZIP.streamRemoveFile

`ZIP.streamRemoveFile(aFilePath, aName)`

````text
Removes a file/directory aName from the aFilePath ZIP file provided.
````
{% endraw %}
