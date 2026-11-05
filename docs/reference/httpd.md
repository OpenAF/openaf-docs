---
layout: default
title: httpd
parent: Reference
grand_parent: OpenAF docs
---

{% raw %}
## httpd

[Source: `06414cd9`](https://github.com/OpenAF/openaf/blob/06414cd9204e918daa1e2971ce904783299db333/src/openaf/plugins/HTTPServer.java) · [Baseline](../source-snapshot.md)

### HTTPd.HTTPd

`HTTPd.HTTPd(aPort, aLocalInteface, keyStorePath, keyStorePassword, logFunction, webSockets, aTimeout, aImpl)`

Creates a HTTP server instance on the provided port and optionally on the identified local interface.
If the port provided is 0 or negative a random port will be assigned. To determine what this port is
you can use the function HTTPServer.getPort().
If `aImpl` = "java" is provided the Java built-in HttpServer implementation will be used.
If `keyStorePath` is defined, the corresponding SSL Key Store will be used (connections will be https) with
the provided `keyStorePassword`. Do note that the `keyStorePath` should be included in the OpenAF classpath.
The `logFunction`, if defined, will be called by the server whenever there is any logging to be performed
by the HTTPServer. This function will receive 3 arguments. Example:

```javascript
plugin("HTTPServer");
var s = new HTTPd(8091, void 0, void 0, void 0, function(aType, aMsg, anException) {
   if(aType.toString() != "DEBUG" && anException.getMessage() != "Broken pipe")
      logErr("Type: " + aType + " | Message: " + aMsg + anException.printStackTrace());
});
s.addEcho("/echo");
s.add("/stuff", function(req) {
   print(beautifier(req));
   return s.replyOKText("Stuff!!");
});
s.setDefault("/stuff");
```

To generate a SSL key store you can use Java's keytool:

```sh
keytool -genkey -keyalg RSA -alias selfsigned -keystore keystore.jks -storepass password -validity 360 -keysize 2048 -ext SAN=DNS:localhost,IP:127.0.0.1  -validity 9999
```

And then add keystore.jks to the openaf.jar and have `keyStorePath` = "/keystore.jks".

To support websockets you need to build IWebSock object and provide a timeout. For example:

```javascript
plugin("HTTPServer");
var webSock = new Packages.com.nwu2.httpd.IWebSock({
   // onOpen callback
   oOpen: _ws => { log("Connection open") },
   // onClose callback
   oClose: (_ws, aCode, aReason, hasInitByRemote) => { log("Connection close: " + String(aReason)) },
   // onMessage callback
   oMessage: (_ws, aMessage) => { _ws.send(aMessage.getTextPayload()); },
   // onPong callback
   oPong: (_ws, aPong) => { },
   // onException callback
   oException: (_ws, anException) => { logErr(String(anException)); }
});
var s = new HTTPd(8091, "127.0.0.1", void 0, void 0, void 0, webSock, 30000); // 30 seconds timeout
s.addWS("/websocket");  // makes it available at ws://127.0.0.1:8091/websocket
```

### HTTPd.add

`HTTPd.add(aURI, aFunction)`

Adds a custom responder to the provided URI. Any call to the URI will trigger a call to
the provided function. The function will receive the request as an argument. For example:

```javascript
var hs = new HTTPd(1234);
hs.add("/example", function(req) { return hs.replyOKText(beautifier(req)); });
```

### HTTPd.addEcho

`HTTPd.addEcho(aURI)`

````text
Adds a echo responder to the provided URI. Useful for debugging http requests to  a server instance.
````

### HTTPd.addFileBrowse

`HTTPd.addFileBrowse(aURI, aFilepath)`

````text
Adds a responder to the provided URI that provides a very basic file browse to the provided aFilepath. Warning: keep in mind that this will expose files without any credential checking.
````

### HTTPd.addSession

`HTTPd.addSession(aSessionID)`

````text
Provides a simple session track mechanism adding the session ID provided. See HTTPServer.setSession to add data.
````

### HTTPd.addStatus

`HTTPd.addStatus(aURI)`

````text
Adds a status responder to the provided URI. Useful for debugging proposes
````

### HTTPd.addXDTServer

`HTTPd.addXDTServer(aURI, aAuthFunction, aOpsBrokerFunction)`

Adds a WeDo XDT server responder to the provided URI with authentication provided by the `aAuthFunction`
and operations provided by the `aOpsBrokerFunction`. For example:

```javascript
var hs = new HTTPd(1234);
hs.addXDTServer('/xdt',
  function(auth) {
     if (auth.getUser() == 'adm' && auth.getPass() == 'Password1') {
        return true;
     } else {
         return false;
     }
  },
  function(sessionId, operation, paramIn, request) {
     switch(operation) {
        case "HelloWorld":
           return {"hello": "world!"};
        case "Ping":
           return paramIn;
        default:
           return paramIn;
     }
  }
);
```

### HTTPd.delSession

`HTTPd.delSession(aSessionID)`

````text
Removes the provided session ID data from memory.
````

### HTTPd.getImpl

`HTTPd.getImpl() : string`

````text
Returns the implementation used by the HTTP server instance. Possible values are "java" for Java built-in HttpServer, "nwu2" for NWU2 HTTP server, and "nwu" for legacy NWU HTTP server.
````

### HTTPd.getPort

`HTTPd.getPort() : number`

````text
Returns the listen port of the HTTP server instance.
````

### HTTPd.getSession

`HTTPd.getSession(aSessionID) : Object`

````text
Retrieves the current data stored for the provided session ID.
````

### HTTPd.hasSession

`HTTPd.hasSession(aSessionID) : boolean`

````text
Returns true if the provided session ID was add to memory. False otherwise.
````

### HTTPd.reply

`HTTPd.reply(data, aMimetype, aHTTPCode, aMapOfHeaders) : Object`

````text
Builds a response object suitable to provide a reply to a HTTP request for a function used with the HTTPServer.add method. It will return aMimetype (string representation) with the provided data (string format) and the aHTTPCode and the map of extra HTTP headers.
````

### HTTPd.replyBytes

`HTTPd.replyBytes(data, aMimetype, aHTTPCode, aMapOfHeaders) : Object`

````text
Builds a response object suitable to provide a reply to a HTTP request for a function used with the HTTPServer.add method. It will return aMimetype (string representation) with the provided data (as an array of bytes), the aHTTPCode and the map of extra HTTP headers.
````

### HTTPd.replyOKBin

`HTTPd.replyOKBin(data, aMapOfHeaders) : Object`

````text
Builds a response object suitable to provide a reply to a HTTP request for a function used with the HTTPServer.add method. It will return application/octet-stream mimetype with the provided data (as an array of bytes) and a HTTP code of OK.  Also you can provide the map of extra HTTP headers.
````

### HTTPd.replyOKHTML

`HTTPd.replyOKHTML(data, aMapOfHeaders) : Object`

````text
Builds a response object suitable to provide a reply to a HTTP request for a function used with the HTTPServer.add method. It will return a HTML mimetype with the provided data (in string format) and a HTTP code of OK. Also you can provide the map of extra HTTP headers.
````

### HTTPd.replyOKJSON

`HTTPd.replyOKJSON(data, aMapOfHeaders) : Object`

````text
Builds a response object suitable to provide a reply to a HTTP request for a function used with the HTTPServer.add method. It will return a JSON mimetype with the provided data (in string format) and a HTTP code of OK. Also you can provide the map of extra HTTP headers.
````

### HTTPd.replyOKText

`HTTPd.replyOKText(data, aMapOfHeaders) : Object`

````text
Builds a response object suitable to provide a reply to a HTTP request for a function used with the HTTPServer.add method. It will return a text mimetype with the provided data and a HTTP code of OK. Also you can provide the map of extra HTTP headers.
````

### HTTPd.replyOKXML

`HTTPd.replyOKXML(data, aMapOfHeaders) : Object`

````text
Builds a response object suitable to provide a reply to a HTTP request for a function used with the HTTPServer.add method. It will return a XML mimetype with the provided data (in string format) and a HTTP code of OK. Also you can provide the map of extra HTTP headers.
````

### HTTPd.replyStream

`HTTPd.replyStream(stream, aMimetype, aHTTPCode, aMapOfHeaders) : Object`

````text
Builds a response object suitable to provide a reply to a HTTP request for a function used with the HTTPServer.add method. It will return aMimetype (string representation) with the provided input stream, the aHTTPCode and the map of extra HTTP headers.
````

### HTTPd.setDefault

`HTTPd.setDefault(aURI)`

Sets the default URI to redirect all requests that don't have a responder associated. For example:

```javascript
var hs = new HTTPd(1234);
hs.addEcho("/echo");
hs.setDefault("/echo");
```

### HTTPd.setSession

`HTTPd.setSession(aSessionID, anObject)`

````text
Sets the provided anObject as the session data for the session ID provided.
````

### HTTPd.stop

`HTTPd.stop()`

````text
Tries to stop the currently running HTTP server instance.
````
{% endraw %}
