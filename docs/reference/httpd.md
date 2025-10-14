---
layout: default
title: httpd
parent: Reference
grand_parent: OpenAF docs
---


## httpd

### HTTPd.add

__HTTPd.add(aURI, aFunction)__

````
Adds a custom responder to the provided URI. Any call to the URI will trigger a call to  the provided function. The function will receive the request as an argument. For example:

  var hs = new HTTPd(1234);
  hs.add("/example", function(req) { hs.replyOKText(beautifier(req)); } 

````
### HTTPd.addEcho

__HTTPd.addEcho(aURI)__

````
Adds a echo responder to the provided URI. Useful for debugging http requests to  a server instance.
````
### HTTPd.addFileBrowse

__HTTPd.addFileBrowse(aURI, aFilepath)__

````
Adds a responder to the provided URI that provides a very basic file browse to the provided aFilepath. Warning: keep in mind that this will expose files without any credential checking.
````
### HTTPd.addSession

__HTTPd.addSession(aSessionID)__

````
Provides a simple session track mechanism adding the session ID provided. See HTTPServer.setSession to add data.
````
### HTTPd.addStatus

__HTTPd.addStatus(aURI)__

````
Adds a status responder to the provided URI. Useful for debugging proposes
````
### HTTPd.addXDTServer

__HTTPd.addXDTServer(aURI, aAuthFunction, aOpsBrokerFunction)__

````
Adds a WeDo XDT server responder to the provided URI with authentication provided by the aAuthFunction and operations provided by the aOpsBrokerFunction. For example:

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


````
### HTTPd.delSession

__HTTPd.delSession(aSessionID)__

````
Removes the provided session ID data from memory.
````
### HTTPd.getImpl

__HTTPd.getImpl() : string__

````
Returns the implementation used by the HTTP server instance. Possible values are "java" for Java built-in HttpServer, "nwu2" for NWU2 HTTP server, and "nwu" for legacy NWU HTTP server.
````
### HTTPd.getPort

__HTTPd.getPort() : number__

````
Returns the listen port of the HTTP server instance.
````
### HTTPd.getSession

__HTTPd.getSession(aSessionID) : Object__

````
Retrieves the current data stored for the provided session ID.
````
### HTTPd.hasSession

__HTTPd.hasSession(aSessionID) : boolean__

````
Returns true if the provided session ID was add to memory. False otherwise.
````
### HTTPd.HTTPd

__HTTPd.HTTPd(aPort, aLocalInteface, keyStorePath, keyStorePassword, logFunction, webSockets, aTimeout, aImpl)__

````
Creates a HTTP server instance on the provided port and optionally on the identified local interface. If the port provided is 0 or negative a random port will be assigned. To determine what this port is  you can use the function HTTPServer.getPort(). If aImpl = "java" is provided the Java built-in HttpServer implementation will be used. If keyStorePath is defined, the corresponding SSL Key Store will be used (connections will be https) with the provided keyStorePassword. Do note that the keyStorePath should be included in the OpenAF classpath. The logFunction, if defined, will be called by the server whenever there is any logging to be performed  by the HTTPServer. This function will receive 3 arguments. Example:

plugin("HTTPServer");
var s = new HTTPd(8091, void 0, void 0, void 0, function(aType, aMsg, anException) {
   if(aType.toString() != "DEBUG" && anException.getMessage() != "Broken pipe")
      logErr("Type: " + aType + " | Message: " + aMsg + anException.printStackTrace());
});
s.addEcho("/echo"); s.add("/stuff", function(req) {
   print(beautifier(req));
   return s.replyOKText("Stuff!!");
};
s.setDefault("/stuff");
\  To generate a SSL key store you can use Java's keytool:

keytool -genkey -keyalg RSA -alias selfsigned -keystore keystore.jks -storepass password -validity 360 -keysize 2048 -ext SAN=DNS:localhost,IP:127.0.0.1  -validity 9999

And then add keystore.jks to the openaf.jar and have keyStorePath = "/keystore.jks".

To support websockets you need to build IWebSock object and provide a timeout. For example:

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


````
### HTTPd.reply

__HTTPd.reply(data, aMimetype, aHTTPCode, aMapOfHeaders) : Object__

````
Builds a response object suitable to provide a reply to a HTTP request for a function used with the HTTPServer.add method. It will return aMimetype (string representation) with the provided data (string format) and the aHTTPCode and the map of extra HTTP headers.
````
### HTTPd.replyBytes

__HTTPd.replyBytes(data, aMimetype, aHTTPCode, aMapOfHeaders) : Object__

````
Builds a response object suitable to provide a reply to a HTTP request for a function used with the HTTPServer.add method. It will return aMimetype (string representation) with the provided data (as an array of bytes), the aHTTPCode and the map of extra HTTP headers.
````
### HTTPd.replyOKBin

__HTTPd.replyOKBin(data, aMapOfHeaders) : Object__

````
Builds a response object suitable to provide a reply to a HTTP request for a function used with the HTTPServer.add method. It will return application/octet-stream mimetype with the provided data (as an array of bytes) and a HTTP code of OK.  Also you can provide the map of extra HTTP headers.
````
### HTTPd.replyOKHTML

__HTTPd.replyOKHTML(data, aMapOfHeaders) : Object__

````
Builds a response object suitable to provide a reply to a HTTP request for a function used with the HTTPServer.add method. It will return a HTML mimetype with the provided data (in string format) and a HTTP code of OK. Also you can provide the map of extra HTTP headers.
````
### HTTPd.replyOKJSON

__HTTPd.replyOKJSON(data, aMapOfHeaders) : Object__

````
Builds a response object suitable to provide a reply to a HTTP request for a function used with the HTTPServer.add method. It will return a JSON mimetype with the provided data (in string format) and a HTTP code of OK. Also you can provide the map of extra HTTP headers.
````
### HTTPd.replyOKText

__HTTPd.replyOKText(data, aMapOfHeaders) : Object__

````
Builds a response object suitable to provide a reply to a HTTP request for a function used with the HTTPServer.add method. It will return a text mimetype with the provided data and a HTTP code of OK. Also you can provide the map of extra HTTP headers.
````
### HTTPd.replyOKXML

__HTTPd.replyOKXML(data, aMapOfHeaders) : Object__

````
Builds a response object suitable to provide a reply to a HTTP request for a function used with the HTTPServer.add method. It will return a XML mimetype with the provided data (in string format) and a HTTP code of OK. Also you can provide the map of extra HTTP headers.
````
### HTTPd.replyStream

__HTTPd.replyStream(stream, aMimetype, aHTTPCode, aMapOfHeaders) : Object__

````
Builds a response object suitable to provide a reply to a HTTP request for a function used with the HTTPServer.add method. It will return aMimetype (string representation) with the provided input stream, the aHTTPCode and the map of extra HTTP headers.
````
### HTTPd.setDefault

__HTTPd.setDefault(aURI)__

````
Sets the default URI to redirect all requests that don't have a responder associated. For example:

  var hs = new HTTPd(1234);
  hs.addEcho("/echo");
  hs.setDefault("/echo");


````
### HTTPd.setSession

__HTTPd.setSession(aSessionID, anObject)__

````
Sets the provided anObject as the session data for the session ID provided.
````
### HTTPd.stop

__HTTPd.stop()__

````
Tries to stop the currently running HTTP server instance.
````
