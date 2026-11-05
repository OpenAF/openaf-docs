---
layout: default
title: ssh
parent: Reference
grand_parent: OpenAF docs
---

{% raw %}
## ssh

[Source: `06414cd9`](https://github.com/OpenAF/openaf/blob/06414cd9204e918daa1e2971ce904783299db333/src/openaf/plugins/SSH.java) · [Baseline](../source-snapshot.md)

### SSH.SSH

`SSH.SSH(aHost, aPort, aLogin, aPass, anIdentificationKey, withCompression, aTimeout, noStrictHostKeyChecking) : SSH`

````text
Creates an instance of a SSH client (and connects) given a host, port, login username, password and,  optionally a identity file path and the indication of use of compression. Alternatively you can provide  just a simple url where aHost = ssh://user:pass@host:port/identificationKey?timeout=1234&compression=true.
````

### SSH.cd

`SSH.cd(aPath)`

````text
Changes the remote directory to the corresponding path.
````

### SSH.close

`SSH.close()`

````text
Closes the SSH connection.
````

### SSH.delTunnelLocal

`SSH.delTunnelLocal(aLocalInterface, aLocalPort)`

````text
Removes a TCP tunnel on the local port over the SSH connection. This is the same as delTunnelLocal, but allows you to specify a local interface.
````

### SSH.delTunnelRemote

`SSH.delTunnelRemote(aRemoteInterface, aRemotePort)`

````text
Removes a TCP tunnel on the remote port over the SSH connection. This is the same as delTunnelRemote, but allows you to specify a remote interface.
````

### SSH.df

`SSH.df(aPath) : Map`

````text
Tries to return an object, for the remote provided path, with size, used space, available space,  availableForRoot space and capacityPercentage.
````

### SSH.exec

`SSH.exec(aCommand, aStdIn, shouldOutputAlso, pty, outputMap, callbackFunc) : Object`

Executes a command over the SSH connection. You can optionally provide the input and indicate that it `shouldOutputAlso`
(boolean) to stdout and if you want to allocate a `pty` (boolean). The stderr will be stored in `__stderr` and also output
if `shouldOutputAlso` = true. If `outputMap` instead of the stdout string a map with stdout, stderr and exitcode will be returned.
A `callbackFunc` can be provided, if `shouldOutputAlso` is undefined or false, that will receive, as parameters, an output stream, a error stream and an input stream. If defined the stdout and stderr won't
be available for the `outputMap` if true. Example:

```javascript
ssh.exec("someCommand", void 0, void 0, false, void 0, false, function(o, e, i) { ioStreamReadLines(o, (f) => { print("TEST | " + String(f)) }, void 0, false) });
```

### SSH.execSudo

`SSH.execSudo(aCommandWithSudo, aUser, aStdIn, shouldOutputAlso, pty, outputMap, callbackFunc) : Object`

Executes a command over the SSH connection using sudo to `aUser`. You can optionally provide the input and indicate that
it `shouldOutputAlso` (boolean) to stdout and if you want to allocate a `pty` (boolean). The stderr will be stored in
`__stderr` and also output if `shouldOutputAlso` = true. If `outputMap` instead of the stdout string a map with stdout, stderr and exitcode will be returned.
A `callbackFunc` can be provided, if `shouldOutputAlso` is undefined or false, that will receive, as parameters, an output stream, a error stream and an input stream. If defined the stdout and stderr won't
be available for the `outputMap` if true. Example:

```javascript
ssh.execSudo("someCommand", void 0, void 0, false, void 0, false, function(o, e) { ioStreamReadLines(o, (f) => { print("TEST | " + String(f)) }) });
```

### SSH.get

`SSH.get(aRemoteFilePath, aLocalFilePath, monitor) : String`

````text
Retrieves a file, using the SFTP connection, from aRemoteFilePath to aLocalFilePath. Use SSH.getBytes in case you are reading a binary file. Optionally you can provided a callback function called monitor (see more in ow.format.sshProgress)
````

### SSH.getBytes

`SSH.getBytes(aRemoteFile) : anArrayOfBytes`

````text
Returns an array of bytes with the contents of aRemoteFilePath, using the SFTP connection.
````

### SSH.getExecChannel

`SSH.getExecChannel() : Object`

````text
Obatins the internal SSH session exec channel.
````

### SSH.getFile

`SSH.getFile(aRemoteFile, aLocalFile) : anArrayOfBytes`

````text
Retrieves a remote file over the SSH connection to be stored on the local path provided. If aLocalFile is not provided the remote file contents will be returned as an array of bytes.
````

### SSH.getSftpChannel

`SSH.getSftpChannel() : Object`

````text
Obtains the internal SSH session sftp channel.
````

### SSH.listFiles

`SSH.listFiles(aPath) : Map`

````text
Returns a files array where each entry has filename, longname, filepath, size, permissions, lastModified,  createTime, isDirectory and isFile.
````

### SSH.mkdir

`SSH.mkdir(aPath)`

````text
Tries to create a remote directory for the provided aPath.
````

### SSH.put

`SSH.put(aSourceFilePath, aRemoteFilePath, monitor)`

````text
Copies a aSourceFilePath to aRemoteFilePath, using the SFTP connection. Optionally you can provided a callback function called monitor (see more in ow.format.sshProgress)
````

### SSH.putBytes

`SSH.putBytes(aRemoteFilePath, bytes, monitor)`

````text
Writes an array of bytes on aRemoteFilePath, using the SFTP connection. Optionally you can provided a callback function called monitor (see more in ow.format.sshProgress)
````

### SSH.pwd

`SSH.pwd() : String`

````text
Returns the current remote path.
````

### SSH.rename

`SSH.rename(aOriginalName, aNewName)`

````text
Renames a remote original filename to a newname.
````

### SSH.rm

`SSH.rm(aFilePath)`

````text
Removes a remote filename at the provided aFilePath.
````

### SSH.rmdir

`SSH.rmdir(aPath)`

````text
Removes a remote directory at the provided aPath.
````

### SSH.sendFile

`SSH.sendFile(aSourceFile, aRemoteFile)`

````text
Sends a source file over the SSH connection to be stored on the remote path provided.
````

### SSH.setTimeout

`SSH.setTimeout(aTimeout)`

````text
Sets aTimeout in ms for the SSH connection.
````

### SSH.sftpGet

`SSH.sftpGet(aRemoteFile, aLocalFile, monitor) : JavaStream`

````text
Retrieves a remote file over the SFTP connection to be stored on the local path provided. If aLocalFile is not provided the remote file contents will be returned as a Java Stream Optionally you can provided a callback function called monitor (see more in ow.format.sshProgress)
````

### SSH.sftpPut

`SSH.sftpPut(aSource, aRemoteFile, monitor)`

````text
Sends aSource file (if string) or a Java stream to a remote file path over a SFTP connection. Optionally you can provided a callback function called monitor (see more in ow.format.sshProgress)
````

### SSH.tunnelLocal

`SSH.tunnelLocal(aLocalPort, aRemoteHost, aRemotePort)`

````text
Creates a TCP tunnel between a local port and a remote host and port over the SSH connection.
````

### SSH.tunnelLocalBind

`SSH.tunnelLocalBind(aLocalInterface, aLocalPort, aRemoteHost, aRemotePort)`

````text
Creates a TCP tunnel, on the aLocalInterface only, between a local port and a remote host and port over the SSH connection.
````

### SSH.tunnelRemote

`SSH.tunnelRemote(aRemotePort, aLocalAddress, aLocalPort)`

````text
Creates a TCP tunnel between a local host and port to be accessed from a remote port over the SSH connection.
````

### SSH.tunnelRemoteBind

`SSH.tunnelRemoteBind(aRemoteInterface, aRemotePort, aLocalAddress, aLocalPort)`

````text
Creates a TCP tunnel, on the aRemoteInterface only, between a local host and port to be accessed from a remote  port over the SSH connection.
````
{% endraw %}
