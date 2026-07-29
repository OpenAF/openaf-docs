---
layout: default
title: ftp
parent: Reference
grand_parent: OpenAF docs
---


## ftp

### FTP.FTP

__FTP.FTP(aHost, aPort, aLogin, aPass, isFTPS, isImplicit, aProtocol, isPassive, isBinary, aTimeout) : FTP__

````
Creates an instance of a FTP/FTPS client (and connects) given a host, port, login username and password.
Alternatively you can provide a FTP/FTPS url where aHost = ftp://user:pass@host:port/?timeout=1234&passive=true&binary=true
or ftps://user:pass@host:port/?timeout=1234&passive=true&binary=true&implicit=false&protocol=TLS.

See also the $ftp shortcut in the [scope reference](scope.md) for a more convenient chainable JavaScript API.
````
### FTP.cd

__FTP.cd(aPath)__

````
Changes the remote directory to the corresponding path.
````
### FTP.close

__FTP.close()__

````
Closes the FTP/FTPS connection.
````
### FTP.get

__FTP.get(aRemoteFilePath, aLocalFilePath) : String__

````
Retrieves a file, using the FTP/FTPS connection, from aRemoteFilePath to aLocalFilePath.
Use FTP.getBytes in case you are reading a binary file into memory.
````
### FTP.getBytes

__FTP.getBytes(aRemoteFile) : anArrayOfBytes__

````
Returns an array of bytes with the contents of aRemoteFilePath, using the FTP/FTPS connection.
````
### FTP.getFTPClient

__FTP.getFTPClient() : Object__

````
Obtains the internal FTP/FTPS client.
````
### FTP.ftpGet

__FTP.ftpGet(aRemoteFile, aLocalFile) : JavaStream__

````
Retrieves a remote file over the FTP/FTPS connection to be stored on the local path provided. If aLocalFile is
not provided the remote file contents will be returned as a Java Stream.
````
### FTP.ftpPut

__FTP.ftpPut(aSource, aRemoteFile)__

````
Sends aSource file (if string) or a Java stream to a remote file path over a FTP/FTPS connection.
````
### FTP.listFiles

__FTP.listFiles(aPath) : Map__

````
Returns a files array where each entry has filename, longname, filepath, size, permissions, lastModified,
createTime, isDirectory and isFile.
````
### FTP.mkdir

__FTP.mkdir(aPath)__

````
Tries to create a remote directory for the provided aPath.
````
### FTP.put

__FTP.put(aSourceFilePath, aRemoteFilePath)__

````
Copies aSourceFilePath to aRemoteFilePath, using the FTP/FTPS connection.
````
### FTP.putBytes

__FTP.putBytes(aRemoteFilePath, bytes)__

````
Writes an array of bytes on aRemoteFilePath, using the FTP/FTPS connection.
````
### FTP.pwd

__FTP.pwd() : String__

````
Returns the current remote path.
````
### FTP.rename

__FTP.rename(aOriginalName, aNewName)__

````
Renames a remote original filename to a newname.
````
### FTP.rm

__FTP.rm(aFilePath)__

````
Removes a remote filename at the provided aFilePath.
````
### FTP.rmdir

__FTP.rmdir(aPath)__

````
Removes a remote directory at the provided aPath.
````
### FTP.setBinaryMode

__FTP.setBinaryMode(isBinary)__

````
Switches between binary and ascii file transfer mode.
````
### FTP.setPassiveMode

__FTP.setPassiveMode(isPassive)__

````
Switches between passive and active mode.
````
### FTP.setTimeout

__FTP.setTimeout(aTimeout)__

````
Sets aTimeout in ms for the FTP/FTPS connection.
````
