---
layout: default
title: ow.server
parent: Reference
grand_parent: OpenAF docs
---


## ow.server

### ow.server.auth.add

__ow.server.auth.add(aUser, aPass, aKey)__

````
Adds the aUser and aPass to the current authentication list. Optionally a 2FA aKey.
````
### ow.server.auth.check

__ow.server.auth.check(aUser, aPass) : boolean__

````
Checks if the aUser and aPass provided are authenticated with the current internal list (returns true) or not (returns false). If a 2FA authentication was provided the token should be suffix to the password.
````
### ow.server.auth.del

__ow.server.auth.del(aUser)__

````
Removes the aUSer from the current authentication list.
````
### ow.server.auth.dump

__ow.server.auth.dump() : Map__

````
Dumps the current authentication list into a Map.
````
### ow.server.auth.dumpEncrypt

__ow.server.auth.dumpEncrypt(aKey) : Map__

````
Dumps the current authentication list into an encrypted string (optionally using an encryption aKey).
````
### ow.server.auth.getExtra

__ow.server.auth.getExtra(aUser) : Object__

````
Gets the extra object associated with aUser (previously set with ow.server.auth.setExtra).
````
### ow.server.auth.initialize

__ow.server.auth.initialize(aPreviousDumpMap, aKey, aCustomFunc)__

````
Initializes with a previous dump from ow.server.auth.dump or ow.server.auth.dumpEncrypt (including an optional aKey if used). Optionally aCustomFunc can be provided as a custom authentication function that receives the provided user and password and should return true if authenticated or false otherwise.
````
### ow.server.auth.is2FA

__ow.server.auth.is2FA(aUser) : boolean__

````
Returns true if aUser has 2FA authentication, false otherwise.
````
### ow.server.auth.isLocked

__ow.server.auth.isLocked(aUser) : boolean__

````
For a given aUser returns if the user is currently considered as lock or not.
````
### ow.server.auth.loadFile

__ow.server.auth.loadFile(aFile, aKey)__

````
Loads aFile (previously saved with ow.server.auth.saveFile), optionally providing aKey, (re)initializing  the current authentication information.
````
### ow.server.auth.saveFile

__ow.server.auth.saveFile(aFile, aKey)__

````
Saves into aFile, optionally providing aKey, the current authentication information. You can use ow.server.auth.loadFile later to reload this info.
````
### ow.server.auth.setCustomFunction

__ow.server.auth.setCustomFunction(aCustomFunction)__

````
Sets a custom authentication function that receives the provided user and password and should return true if authenticated or false otherwise.
````
### ow.server.auth.setExtra

__ow.server.auth.setExtra(aUser, aX)__

````
Sets an extra object (aX) to be associated with aUser (for example, the correspondings permissions). You can later retrieve this extra object with ow.server.auth.getExtra.
````
### ow.server.auth.setLockTimeout

__ow.server.auth.setLockTimeout(aTimeout)__

````
Set the current lock timeout in seconds. Defaults to 15 minutes.
````
### ow.server.auth.setTriesToLock

__ow.server.auth.setTriesToLock(numberOfTries)__

````
Set the current number of wrong tries until a user is locked. Defaults to 3.
````
### ow.server.authAppCheck

__ow.server.authAppCheck(anAppPassword, aReceivedToken, aUserPassword, a2FAToken, useBCrypt) : boolean__

````
Checks the validity of the aReceivedToken given anAppPassword, corresponding aUserPasswork and a2FAToken returning true if it's valid or false otherwise. If useBCrypt = 1 then an extra bcrypt function will be added.

Example:

ow.loadServer();
$ch("a").expose(1234, "/a", (u, p) => {
   if (u == "a" && 
       ow.server.authAppCheck("...", p, "...", "...")) 
     return true; 
   else 
     return false;
});


````
### ow.server.authAppGen

__ow.server.authAppGen(anAppPassword, aUserPassword, a2FAToken, numRounds) : String__

````
Generates an application token to be used for server communication given anAppPassword (encrypted or not), an application user password (aUserPassword encrypted or not) and an application a2FAToken. Optionally you can specify the numRounds for the bcrypt function used (if absent, bcrypt won't be used).

Example:

ow.loadServer();
$ch("a").createRemote("http://some.server:1234/a", __, (h) => {
   h.login("user", ow.server.authAppGen("...", "...", "..."));
});


````
### ow.server.checkIn

__ow.server.checkIn(aPidFile, onAlreadyRunning, onShutdown, anExitCode) : Boolean__

````
Will check if a server for the give aPidFile is running or not. Will return false if it's running  and server start shouldn't proceed. Will return true if nothing is running and server start should proceed. Optionally you can provide an onShutdown function to execute any code needed upon controlled shutdown of the server and provide an onAlreadyRunning function (that will received the corresponding aPidFile). If the onAlreadyRunning function returns false the process will exit with -1 (or the anExitCode provided), if true will continue processing. Example:

var params = processExpr();
ow.server.checkIn("server.pid", function(aPid) {
   log("there is another me " + aPid + " already running... bye!");
   if (isDefined(params.restart)) {
      log("I will kill him!");
      pidKill(ow.server.getPid(aPid), true);
      return true;
   } else {
      log("... I will die now...");
      return false;
   }
}, function() {
   log("I'm going to die....");
});

ow.server.daemon();

(available after ow.loadServer())
````
### ow.server.cluster

__ow.server.cluster(aHost, aPort, nodeTimeout, aNumberOfTries, aTryTimeout, aImplOptions, aListImplementation) : Object__

````
Creates a new instance of a simple cluster nodes management code. Each cluster node should create it's own instante providing aHost address on which it can be contacted, a corresponding aPort, a nodeTimeout in ms (defaults to 30000), a aNumberOfTries to contact a cluster node (defaults to 3), a aTryTimeout in ms waiting for a reply from another cluster node (defaults to 500ms), a custom cluster list implementation options and a custom map of functions implementing a cluster list retrieval. If no aListImplemnetation is provided it defaults to an internal file based implementation that expects the following options: LOCKTIMEOUT, how much a lock should be honored in ms (e.g. more that 60000ms and it's wierd that the lock it's still there and no other cluster node has been found); CLUSTERFILE, the filepath to the cluster file; CLUSTERFILELOCK, the filepath to the cluster file lock file.

To provide another custom aListImplementation it should contain the following methods:

  - clusterLock()                  - locking the access to the cluster nodes list
  - clusterUnLock()                - unlocking the access to the cluster nodes list
  - clusterGetList()               - returns the current cluster nodes list
  - clusterPutList(aList)          - sets a new cluster nodes list (an array with maps containing host, port and date (last contact date))
  - clusterSendMsg(aHost, aMsg)    - sends aMsg to a specific aHost or all (is aHost = "all")
  - clusterSetMsgHandler(aT, aHFn) - sets aHFn function (receives (implementationOptionsMap, aMsg) ) to handle any messages that contain { t: aT }
  - clusterCanLock(aLockName)      - asks all nodes if aLockName can be locked on cluster.locks
  - clusterCanUnLock(aLockName)    - asks all nodes if aLockName can be unlocked on cluster.locks
  - clusterLocks()                 - returns the current cluster node locks implementation (ow.server.locks)


````
### ow.server.cluster.all

__ow.server.cluster.all(aFunction, includeMe) : Object__

````
Tries to execute aFunction providing a map with all of the cluster list host + port. If the aFunction throws an exception another cluster will be used. If no cluster could be used an exception is thrown. Optionally includeMe = true enables executing on the current cluster node itself. If succcessfully returns whatever the aFunction returns.
````
### ow.server.cluster.any

__ow.server.cluster.any(aFunction, includeMe) : Object__

````
Tries to execute aFunction providing a map with one of the cluster list host + port. If the aFunction throws an exception another cluster will be used. If no cluster could be used an exception is thrown. Optionally includeMe = true enables executing on the current cluster node itself. If succcessfully returns whatever the aFunction returns.
````
### ow.server.cluster.canLock

__ow.server.cluster.canLock(aLockName) : boolean__

````
Sends messages to all other cluster nodes to reach quorum if can lock aLockName or not. Returns true if yes.
````
### ow.server.cluster.canUnLock

__ow.server.cluster.canUnLock(aLockName) : boolean__

````
Sends messages to all other cluster nodes to reach quorum if can unlock aLockName or not. Returns true if yes.
````
### ow.server.cluster.checkIn

__ow.server.cluster.checkIn()__

````
Checks in the current cluster node.
````
### ow.server.cluster.checkOut

__ow.server.cluster.checkOut()__

````
Checks out the current cluster node.
````
### ow.server.cluster.locks

__ow.server.cluster.locks() : owServerLocks__

````
Returns the current cluster node ow.server.locks instance.
````
### ow.server.cluster.sendMsg

__ow.server.cluster.sendMsg(aHostMap, aMessageMap)__

````
Sends aMessageMap to a specific aHostMap (map composed of a host and a port) or to all cluster nodes if aHostMap = "all". The aMessageMap should contain a "t" key for message topic. The topics "l", "u", "cl", "dl", "cu" and "du" are reserved for cluster lock management.
````
### ow.server.cluster.sendToOthers

__ow.server.cluster.sendToOthers(aData, aSendToOtherFn) : Object__

````
Tries to send to another cluster node aData using aSendToOtherFn that receives, as parameter, a aData and a Map with HOST and PORT of another cluster node to try. In case of failure the function should throw an exception in case of success the function should return an object that will be returned. If no result can be obtained an object with result: 0 will be returned.
````
### ow.server.cluster.setMsgHandler

__ow.server.cluster.setMsgHandler(aMessageTopic, aHandlerFunction)__

````
Sets aHandlerFunction to be called whenever the current node receives a message with aMessageTopic. The aHandlerFunction  receives the implementation options and the message.
````
### ow.server.cluster.verify

__ow.server.cluster.verify(addNewHostMap, delHostMap, customLoad)__

````
Verifies if all cluster nodes ports are reachable and updates the cluster file. If a cluster node is not reachable it will try to a specific number of times after timing out on a specific timeout (see default values in help ow.server.cluster).
````
### ow.server.cluster.whenUnLocked

__ow.server.cluster.whenUnLocked(aLockName, aFn, aTryTimeout, aNumRetries) : boolean__

````
A wrapper for ow.server.locks.lock that will try to lock aLockName after check in the cluster if it can be locked, execute the provide function and then unlock it even in case an exception is raised. Returns if the lock was successfull (true) or not (false).
````
### ow.server.clusterChsPeersImpl

__ow.server.clusterChsPeersImpl__

````
This ow.servers.cluster implementation will cluster one or more cluster servers keeping the cluster connection details on a cluster channel (defaults to __cluster::[name of cluster]). It's meant to be provided to ow.server.cluster like this:

var mts = new ow.server.cluster("1.2.3.4", 1234, __, __, __, { name: "testCluster" }, ow.server.clusterChsPeersImpl)

There are several implementation options:

   name         (String, mandatory)  The clusters name.
   serverOrPort (Number or HTTPd)    Port or http server object where the cluster node channels will be available.
   protocol     (String)             The transport protocol use to reach other cluster (defaults to http).
   path         (String)             The path where other cluster nodes channel is reachable (defaults to '/__m').
   authFunc     (Function)           Optional authentication function (see mor in ow.ch.server.peer).
   unAuthFunc   (Function)           Optional failed authentication function (see more in ow.ch.server.peer).
   maxTime      (Number)             Optional retry max time (see more in ow.ch.server.peer).
   maxCount     (Number)             Optional max count of retries (see more in ow.ch.server.peer).
   ch           (String)             The cluster local channel (defaults to "__cluster::[name of cluster]").
   chs          (Array)              Array of names of channels or maps with each channel name and path. These channels will be automatically peered and unpeered with other cluster nodes. The path, if not provided, defaults to "/[name of channel]".
   chErrs       (String)             The cluster local errors channel (default is none).


````
### ow.server.daemon

__ow.server.daemon(aTimePeriod, aPeriodicFunction)__

````
Will start an infinite cycle to keep a server running. If aTimePeriod (in ms) is not provided a default of 5 seconds will be considered. Optionally you can provide aPeriodicFunction to run every aTimePeriod. If this aPeriodicFunction returns true, the infinite cycle is broken. (available after ow.loadServer())
````
### ow.server.getPid

__ow.server.getPid(aPidFile) : String__

````
Retrieve the server pid on the given aPidFile. (available after ow.loadServer())
````
### ow.server.httpd.addHTTPCode

__ow.server.httpd.addHTTPCode(aCodeRef, aCodeNum)__

````
Adds a new HTTP aCodeNum number that will be referenced by the name aCodeRef.
````
### ow.server.httpd.addMimeType

__ow.server.httpd.addMimeType(anExtension, aMimeType)__

````
Adds a new aMimeType for the corresponding anExtension.
````
### ow.server.httpd.authBasic

__ow.server.httpd.authBasic(aRealm, aHTTPd, aReq, aAuthFunc, aReplyFunc, aUnAuthFunc) : Map__

````
Wraps a httpd reply with basic HTTP authentication for the provided aRealm on the aHTTPd server. The aReq request map should be provided along with aAuthFunc (that receives the user and password and should return true of false if authentication is successful). If authentication is successful aReplyFunc will be executed receiving aHTTPd and aReq. Otherwise an optional aUnAuthFunc will be executed also receiving aHTTPd and aReq. Example:

ow.server.httpd.route(hs, ow.server.httpd.mapRoutesWithLibs(hs, {
   "/f": function(req) { 
      return ow.server.httpd.authBasic(
         "realm", hs, req,
         function(user, pass) {
            if (user == "adm" && pass == "Password1") return true; else return false;
         },
  	    function(hss, areq) {
	       return ow.server.httpd.replyFile(hss, "/some/path", "/f", areq.uri);
	    },
	    function(hss, ar) {
	       return hss.reply("Not authorized.", "text/plain", ow.server.httpd.codes.UNAUTHORIZED);
	    }
     );
  }
}),
function(req) {
   return hs.replyOKText("nothing here...");
}
);


````
### ow.server.httpd.authOAuth

__ow.server.httpd.authOAuth(aMapOptions, aHTTPd, aRequest, aFnReply) : Map__

````
Provides OAuth 2.0 support by intersecting aRequest of aHTTPd to return aFnReply only on correctly authenticated. aMapOptions provides the OAuth configurations to follow:

aMapOptions:

   realm             (optional)  An unique realm name (defaults to 'realm')
   cookie            (optional)  The name of the cookie entry to use (defaults to 'OAF_AUTH_SESSION_ID')
   baseURL           (mandatory) The web server base url (e.g. https://myserver:8090)
   uriLogout         (optional)  The uri to use on the web server to logout (defaults to '/logout')
   uriCallBack       (optional)  The uri to use on the web server to callback (defaults to '/cb'). You should configure oauth to allow redirection to base url + callback (e.g. https://myserver:8090/cb)
   oauthAuthURL      (mandatory) The OAuth authorization_endpoint
   oauthTokenURL     (mandatory) The OAuth token_endpoint
   oauthLogoutURL    (mandatory) The OAuth end_session_endpoint
   oauthCliendId     (mandatory) The OAuth configured client id
   oauthClientSecret (mandatory) The OAuth configured client secret\  

````
### ow.server.httpd.browse.files

__ow.server.httpd.browse.files(aURI, aOptions) : Map__

````
Provides a simple file browser for the provided aURI. The aOptions map can contain the following keys:

  path     (string)   The path to use as root (defaults to ".")
  browse   (boolean)  If true the file browser will be shown (defaults to true)
  showURI  (boolean)  If true the URI will be shown in the file browser (defaults to false)
  sortTab  (boolean)  If true the table will be sorted (defaults to false)
  default  (string)   The default file to show (defaults to undefined)
  logo  	  (string)   The logo to show in the file browser (defaults to undefined)
  footer   (string)   The footer to show in the file browser (defaults to undefined)

````
### ow.server.httpd.browse.odoc

__ow.server.httpd.browse.odoc(aURI, aOptions) : Map__

````
Provides a simple oDoc browser. The aOptions map can contain the following keys:

  browse   (boolean)  If true the file browser will be shown (defaults to true)
  showURI  (boolean)  If true the URI will be shown in the file browser (defaults to false)
  sortTab  (boolean)  If true the table will be sorted (defaults to false)
  logo  	  (string)   The logo to show in the file browser (defaults to undefined)
  footer   (string)   The footer to show in the file browser (defaults to undefined)
  ttl	  (number)   The time to live for the cache (defaults to 5 minutes)

````
### ow.server.httpd.browse.opacks

__ow.server.httpd.browse.opacks(aURI, aOptions) : Map__

````
Provides a simple oPack browser. The aOptions map can contain the following keys:

  browse   (boolean)  If true the file browser will be shown (defaults to true)
  showURI  (boolean)  If true the URI will be shown in the file browser (defaults to false)
  sortTab  (boolean)  If true the table will be sorted (defaults to false)
  logo  	  (string)   The logo to show in the file browser (defaults to undefined)
  footer   (string)   The footer to show in the file browser (defaults to undefined)
  ttl	  (number)   The time to live for the cache (defaults to 5 minutes)

````
### ow.server.httpd.getFromOpenAF

__ow.server.httpd.getFromOpenAF(aResource, inBytes, anEncoding) : anArrayOfBytes__

````
Retrieves aResource, as anArrayOfBytes, from the openaf.jar. This resource can be inBytes = true or not and anEncoding can be provided.
````
### ow.server.httpd.getFromZip

__ow.server.httpd.getFromZip(aZipFile, aResource, inBytes, anEncoding) : anArrayOfBytes__

````
Retrieves aResource, as anArrayOfBytes, from aZipFile. This resource can be inBytes = true or not and anEncoding can be provided.
````
### ow.server.httpd.getHS

__ow.server.httpd.getHS(aPort) : HTTPd__

````
Returns the HTTPd object created, if any, for aPort.
````
### ow.server.httpd.getMimeType

__ow.server.httpd.getMimeType(aFilename) : String__

````
Tries to determine the mime type of aFilename and returns it. If not determined it will default to application/octet-stream.
````
### ow.server.httpd.mapRoutesWithLibs

__ow.server.httpd.mapRoutesWithLibs(aHTTPd, aMapOfRoutes) : Map__

````
Helper to use with ow.server.httpd.route to automatically add routes for JQuery, Handlebars, jLinq and Underscore from the openaf.jar.
````
### ow.server.httpd.mapWithExistingRoutes

__ow.server.httpd.mapWithExistingRoutes(aHTTPd, aMapOfRoutes) : Map__

````
Builds a map of routes taking into account the already defined routes for aHTTPd thus effectively letting add new routes.
````
### ow.server.httpd.reply

__ow.server.httpd.reply(aObject, aStatus, aMimeType, aHeadersMap) : Map__

````
Builds the map response for a HTTP server request using aObject (map, array, string or bytearray), aStatus (default to 200), aMimeType (defaults to application/octet-stream if not recognized) and aHeadersMap.
````
### ow.server.httpd.replyBrowse

__ow.server.httpd.replyBrowse(server, request, _options) : Map__

````
Provides a helper function to reply with a list of files or a file content. The _options map is used to provide the following functions:

  getList(request, _options)   : Function to get the list of files or directories
  getObj(request, _options)    : Function to get the object requested
  renderList(list, server, request, _options) : Function to render the list of files
  renderObj(obj, server, request, _options)   : Function to render the object requested
  renderEmpty(request, _options) : Function to render an empty list

````
### ow.server.httpd.replyFile

__ow.server.httpd.replyFile(aHTTPd, aBaseFilePath, aBaseURI, aURI, notFoundFunction, documentRootArray, mapOfHeaders) : Map__

````
Provides a helper aHTTPd reply that will enable the download of a file, from aBaseFilePath (a file path or java stream), given aURI part of  aBaseURI. Optionally you can also provide a notFoundFunction and an array of file strings (documentRootArraY) to replace as documentRoot. Example:

ow.server.httpd.route(hs, ow.server.httpd.mapRoutesWithLibs(hs, {
   "/stuff/to/server": r => ow.server.httpd.replyFile(hs, "/some/path/to/serve/files", "/stuff/to/server", req.uri)
}), r => hs.replyOKText("nothing here...") );
\
````
### ow.server.httpd.replyFileMD

__ow.server.httpd.replyFileMD(aHTTPd, aBaseFilePath, aBaseURI, aURI, notFoundFunction, documentRootArray, mapOfHeaders, noMaxWidth) : Map__

````
Provides a helper aHTTPd reply that will enable the parsing markdown file-based sites, from aBaseFilePath (a file path or stream), given aURI part of  aBaseURI. Optionally you can also provide a notFoundFunction and an array of file strings (documentRootArraY) to replace as documentRoot. Example:

ow.server.httpd.route(hs, ow.server.httpd.mapRoutesWithLibs(hs, {
   "/stuff/to/server": function(req) {
      return ow.server.httpd.replyFileMD(hs, "/some/path/to/serve/files", "/stuff/to/server", req.uri);
   }
}),
function(req) {
   return hs.replyOKText("nothing here...");
}
);


````
### ow.server.httpd.replyFn

__ow.server.httpd.replyFn(aFunctionName, aInstance, aRequest, aParams, dontRetError) : Map__

````
Provides a helper function to call aFunctionName over aInstance (default this) given a POST aRequest. If aFunctionName doesn't have odoc help information available you will need to provide aParams map for the expected aFunctionName arguments. If dontRetError = true any exception will be kept in the server and an empty map will be returned.
````
### ow.server.httpd.replyJSMap

__ow.server.httpd.replyJSMap(aHTTPd, aMapOrArray) : Map__

````
Provides a helper aHTTPd reply that will parse aMapOrArray into a HTML output. Example:

ow.server.httpd.route(hs, ow.server.httpd.mapRoutesWithLibs(hs, {
   "/stuff/to/server": r => ow.server.httpd.replyJSMap(hs, getOPackPaths()
}),
r => hs.replyOKText("nothing here...")
);


````
### ow.server.httpd.replyJSONRPC

__ow.server.httpd.replyJSONRPC(server, request, mapOfFunctions, logFn, debugFn) : Map__

````
Implements a JSON-RPC 2.0 endpoint using the provided mapOfFunctions. The request must be a POST with a JSON-RPC body.
Optionally you can provide logFn and debugFn functions to log errors and debug information respectively.

Example usage:
  ow.server.httpd.route(hs, {
    "/rpc": (req) => ow.server.httpd.replyJSONRPC(hs, req, { sum: (a, b) => a + b }, logErr, log) 
  })

````
### ow.server.httpd.replyMCP

__ow.server.httpd.replyMCP(server, request, mapOfFunctions, logFn, debugFn) : Map__

````
Implements a Model Context Protocol (MCP) endpoint using the provided mapOfFunctions. The request must be a POST with a MCP body.
Optionally you can provide logFn and debugFn functions to log errors and debug information respectively.
\  Example usage:
ow.server.httpd.route(hs, {
   "/mcp": req => ow.server.httpd.replyMCP(hs, req, {
	initialize                 : params => ({ serverInfo: { name: "OpenAF", title: "OpenAF test ", version: "1.0.0" }, capabilities: { prompts: { listChanged: true }, tools: { listChanged: true } } }),
	"notifications/initialized": params => ({}),
	"tools/call"               : () => ({content:[{type:"text",text:"PONG!"}],isError: false}),
	"tools/list"               : params => { cprint(params); return { tools: [{name:"ping",description:"pings",title:"ping"}] } },
	"prompts/list"             : params => ({})
  }, logErr, log),
  "/echo": req => ow.server.httpd.reply(stringify(req))
 })      *
````
### ow.server.httpd.replyRedirect

__ow.server.httpd.replyRedirect(aHTTPd, newLocation, mapOfHeaders) : Map__

````
Provides a helper aHTTPd reply that will redirect the request to the newLocation provided (HTTP code 303).
````
### ow.server.httpd.resetRoutes

__ow.server.httpd.resetRoutes(aHTTPd)__

````
Given aHTTPd it will reset all internal mapped routes to a reply HTTP code 401 to everything.
````
### ow.server.httpd.route

__ow.server.httpd.route(aHTTPd, aMapOfRoutes, aDefaultRoute, aPath, aPreRouteFunc)__

````
Adds a request router to aHTTPd given aMapOfRoutes. This router will use aPath if defined or /r otherwise. Optionally you can also specify aPreRouteFunc that will run before any routing is made.
Example:

ow.loadServer();
var hs = ow.server.httpd.start(17878);
ow.server.httpd.route(hs, ow.server.httpd.mapRoutesWithLibs(hs, {
		"/myapp": function(req, aHs) {
			return aHs.replyOKText("my stuff!!");
		}
}),
function(req) {
		return hs.replyOKText("nothing here...");
});
log("READY!");
ow.server.daemon();

(available after ow.loadServer())
````
### ow.server.httpd.setWebSocketRoute

__ow.server.httpd.setWebSocketRoute(aHTTPd, aURI)__

````
Using aHTTPd sets aURI to act as a websocket server.
````
### ow.server.httpd.start

__ow.server.httpd.start(aPort, aHost, keyStorePath, password, errorFunction, aWebSockets, aTimeout, aImpl) : Object__

````
Will prepare a HTTP server to be used returning a HTTPServer object. Optionally you can provide  aPort where you want the HTTP server to run. Otherwise a free port will be assigned. Optionally you can provide a different aImpl (implementation) for the HTTP server. If aHost is provided it will be used as the host to bind the server to. If keyStorePath and password are provided the server will be started as a secure HTTPS server. If errorFunction is provided it will be called whenever an error occurs in the server. This function will receive the error as a parameter. If aWebSockets is provided it will be used to handle WebSockets connections. If aTimeout is provided it will be used as the timeout for the server to wait for a request before closing the connection.

(available after ow.loadServer()).

aWebSockets, if used, should be a map with the following functions:

   onOpen(_ws)
   onClose(_ws, aCode, aReason, hasInitByRemote)
   onMessage(_ws, aMessage)
   onPong(_ws, aPong)
   onException(_ws, anException)


````
### ow.server.httpd.stop

__ow.server.httpd.stop(aHTTPd)__

````
Will stop the aHTTPd server running.  (available after ow.loadServer())
````
### ow.server.jmx.call

__ow.server.jmx.call(aJMXObject, objName, aOperation, param1, ...) : value__

````
Invokes aOperation on the object objName using aJMXObject connected to a server using ow.server.jmx.serverExec. Optionally you can provide extra arguments to be passed to the jmx remote operation. Example (based on ow.server.jmx.serverExec):

var jmx = ow.loadServer().jmx.localConnect("12345");
ow.server.jmx.call(jmx, "com.openaf:type=server", "increment"); // 1
ow.server.jmx.call(jmx, "com.openaf:type=server", "resetTo", 10); // 10
````
### ow.server.jmx.get

__ow.server.jmx.get(aJMXObject, objName, aProperty) : value__

````
Returns the current value of aProperty on the object objName using aJMXObject connected to a JMX server.
````
### ow.server.jmx.localConnect

__ow.server.jmx.localConnect(aPid) : JMX__

````
Tries to connect with a local aPid via JMX and returns a JMX plugin object instance. If no aPid is provided it will try to retrieve the current process pid and connect to it.
````
### ow.server.jmx.serverExec

__ow.server.jmx.serverExec(aParamsArray, aFunction)__

````
Helper function to be used with JMXServers. Receives aParamsArray passed on the JMX bean operations handling function and will call aFunction passing the parameters as arguments and converting the returned result into a JSON string to be transmitted to the calling JMX client. Example:

plugin("JMX");
var jmxs = new JMXServer("com.openaf:type=server");
jmxs.start();

var c = 0;
jmxs.addBean({"count": "long", "increment": "operation", "resetTo": "operation"},
  function(key) { if (key == "count") return c; },
  function(key, value) { if (key == "count") c = value; },
  function(op, params) { switch(op) {
     case "increment": return ow.server.jmx.serverExec(params, function() { return ++c; });
     case "resetTo"  : return ow.server.jmx.serverExec(params, function(v) { c = v; });
     }
  }
);
````
### ow.server.jmx.set

__ow.server.jmx.set(aJMXObject, objName, aProperty, aNewValue)__

````
Sets aProperty with the value aNewValue on the object objName using aJMXObject connected to a JMX server.
````
### ow.server.jsonRPC

__ow.server.jsonRPC(data, mapOfFns) : Map__

````
Processes a JSON-RPC request (data) using the provided mapOfFns where each key is the method name and the value is the function to be executed. The data should be a map with the following entries: jsonrpc (should be "2.0"), method (the method name to be executed), params (optional, the parameters to be passed to the method) and id (optional, the request id). Returns a map with the following entries: jsonrpc (should be "2.0"), id (the request id), result (the result of the method execution) or error (if the method is unknown or if the request is invalid).
````
### ow.server.jwt.decode

__ow.server.jwt.decode(aToken) : Map__

````
Tries to decode the JWT aToken provided.
````
### ow.server.jwt.genKey

__ow.server.jwt.genKey(aAlgorithm) : JavaObject__

````
Generates a key for the provided aAlgorithm (defaults to HS256). If aAlgorithm is not HS256, HS384 or HS512 the generated object will be a key pair for which you will need to user .getPrivate() for signing and .getPublic() for verify. Possible algorithms: HS256, HS384, HS512, ES256, ES384, ES512, RS256, RS384, RS512, PS256 (java >= 11), PS384 (java >= 11), PS512 (java >= 11)
````
### ow.server.jwt.sign

__ow.server.jwt.sign(aKey, aData) : String__

````
Signs a JWT using aKey (either a string or java.security.Key) returning the corresponding encoded JWT. To add specific claims use aData map where you can add custom headers and/or custom claims or used the standard fields.  Expected keys for aData:

   audience    (String)
   claims      (Map)
   expiration  (Date)
   headers     (Map)
   issuer      (String)
   id          (String)
   issuedAt    (Date)
   issuer      (String)
   notBefore   (Date)
   subject     (String)
````
### ow.server.jwt.verify

__ow.server.jwt.verify(aSecret1, aToken) : Map__

````
Verifies the JWT provided with aToken using aSecret1 (key (either a string or java.security.Key)). Returns the converted json headers and claims. If any verification fails it will throw a JavaException.
````
### ow.server.ldap

__ow.server.ldap(aServer, aUsername, aPassword) : Object__

````
Creates a ow.server.ldap object for the given aServer, aUsername and aPassword. Example:

var ldapAdServer = "ldap://ldap.forumsys.com:389";
var ldapUsername = "cn=read-only-admin,dc=example,dc=com";
var ldapPassword = "password";

var ldap = new ow.server.ldap(ldapAdServer, ldapUsername, ldapPassword);
var res = ldap.search("dc=example,dc=com", "(uid=*)");

print(beautifier(res));

````
### ow.server.ldap.close

__ow.server.ldap.close()__

````
Closes the current connection.
````
### ow.server.ldap.search

__ow.server.ldap.search(baseSearch, searchFilter) : Array__

````
Tries to return the result of using searchFilter under the baseSearh. See also ow.server.ldap
````
### ow.server.ldap.searchStrings

__ow.server.ldap.searchStrings(baseSearch, searchFilter) : Array__

````
Tries to return the result of using searchFilter under the baseSearch converting each entry to string See also ow.server.ldap
````
### ow.server.ldap.startTLS

__ow.server.ldap.startTLS()__

````
Starts TLS over the current connection.
````
### ow.server.locks

__ow.server.locks(justInternal, aCh)__

````
Creates a lock managing object instance. You can optional make it internal (using a __openAFLocks::local simple channel) or global using a __openAFLocks:global ignite channel. Optional you can also provide an already created channel aCh.
````
### ow.server.locks.clear

__ow.server.locks.clear(aLockName)__

````
Clears an existing aLockName. Note: This might also unlock an inuse lock.
````
### ow.server.locks.extendTimeout

__ow.server.locks.extendTimeout(aLockName, aTryTimeout) : Objet__

````
Tries to extend the lock timeout (or adds a timeout if doesn't exist) with aTryTimeout for aLockName.
````
### ow.server.locks.isLocked

__ow.server.locks.isLocked(aLockName) : boolean__

````
Determines if aLockName is locked (true) or not (false).
````
### ow.server.locks.lock

__ow.server.locks.lock(aLockName, aTryTimeout, aNumRetries, aLockTimeout) : boolean__

````
Locks the lock aLockName optionally using a specific aTryTimeout and aNumRetries instead of the defaults ones (see ow.server.locks.setTryTimeout and ow.server.locks.setRetries). A aLockTimeout can optionally be provided after which the lock will expire. If successfull in locking returns true, otherwiser returns false.
````
### ow.server.locks.setRetries

__ow.server.locks.setRetries(aNumber)__

````
Sets the number of tries for checking if a lock is free waiting a specific time on each (see ow.server.locks.setRetries). Defaults to 5.
````
### ow.server.locks.setTryTimeout

__ow.server.locks.setTryTimeout(aTimeout)__

````
Sets the default wait time (in ms) for each try (see ow.server.locks.setRetries) checking if a lock is free. Defaults to 500 ms.
````
### ow.server.locks.unlock

__ow.server.locks.unlock(aLockName)__

````
Tries to unlock aLockName.
````
### ow.server.locks.whenUnLocked

__ow.server.locks.whenUnLocked(aLockName, aFunction, aTryTimeout, aNumRetries) : boolean__

````
A wrapper for ow.server.locks.lock that will try to lock aLockName, execute the provide function and then unlock it even in case an exception is raised. Returns if the lock was successfull (true) or not (false).
````
### ow.server.mcpStdio

__ow.server.mcpStdio(initData, fnsMeta, fns, lgF)__

````
Processes a MCP (Model Context Protocol) request using standard input/output. The initData is a map with initial data to be sent to the client, fnsMeta is an array of function metadata and fns is a map of functions to be executed. The lgF is a function that will be used to log messages. If not provided, it will default to a function that writes logs to a file named "log.ndjson". The initData should contain the server information and capabilities. The fnsMeta should contain metadata about the functions available, such as their names and descriptions. The fns should contain the actual functions that can be called by the client. The function will listen for incoming MCP requests on standard input and respond accordingly.

Example usage:

     ow.server.mcpStdio({ 			serverInfo: { 				name: "MyServer", 				title: "My Server", 				version: "1.0.0" 			}, 			capabilities: { 				prompts: { 					listChanged: true 				}, 				tools: { 					listChanged: true 				} 			} 		}, [{ 		name: "ping", 		description: "Ping the server" 	}, { 		name: "get_user", 		description: "Get user information", 		input_schema: { 			type: "object", 			properties: { 				userId: { 					type: "string", 					description: "The ID of the user to retrieve" 				} 			}, 			required: ["userId"] 		} 	}], { 		ping: params => { 			return "Pong! Server is running." 		}, 		get_user: params => { 			return { 				name: "Alice", 				userId: params.userId 			} 		} 	})
````
### ow.server.openafServer.exec

__ow.server.openafServer.exec(aId, aScript, aServerPid)__

````
Tries to execute the given aScript locally or in the aServerPid provided (created by a ow.server.openafServer.start). Optionally you can also specify aId.
````
### ow.server.openafServer.load

__ow.server.openafServer.load(aId, aScriptFilePath, aServerPid)__

````
Tries to execute the given aScriptFilePath locally or in the aServerPid provided (created by a ow.server.openafServer.start). Optionally you can also specify aId.
````
### ow.server.openafServer.start

__ow.server.openafServer.start(aId, aPort, notLocal)__

````
Starts an internal JMX server with a give optional aId. If there is a need to access it externally  (do keep in mind security) you can provide also aPort. This server allows for the load or execution  of OpenAF scripts. In extreme cases you can use notLocal = true to make the server available outside the localhost (NOT ADVISABLE!).
````
### ow.server.openafServer.stop

__ow.server.openafServer.stop()__

````
Attempts to stop the existing server.
````
### ow.server.processArguments

__ow.server.processArguments(aRouterFunction, aMainSeparator, aSubSeparator) : Array__

````
Processes the __expr (-e or opack arguments) value for arguments splitting first by aMainSeparator (if not defined defaults to " ") and then splitting by aSubSeparator (if not defined defaults to "="). Example with  __expr = "opensomething exec count=5=123 some=1

ow.server.processArguments(function(aParam) { ... });

Will produce function calls where aParam will have the following values:

"opensomething"
"exec"
[ "count", "5", "123" ]
[ "some", "1" ]

(available after ow.loadServer())
````
### ow.server.queue

__ow.server.queue(aStamp, aName, aChName)__

````
Creates an instance to handle a queue on a channel named "queue::[aName]" or using aChName. The queue entries  will be identified on the channel with aStamp map (defaults to {}) ignoring all other entries. aStamp allows the use of generic channels with other non-queue entries. aName will default to "queue" if not provided.
````
### ow.server.queue.delete

__ow.server.queue.delete(aId)__

````
Tries to delete a queue unique entry identified by aId.
````
### ow.server.queue.increaseVisibility

__ow.server.queue.increaseVisibility(aId, aVisibilityTime)__

````
Tries to set the visibility of a queue aId to now + aVisibilityTime ms. Note: the queue aId should have been already received previously with a specific visibility time.
````
### ow.server.queue.purge

__ow.server.queue.purge()__

````
Tries to delete all queue entries.
````
### ow.server.queue.receive

__ow.server.queue.receive(aVisibilityTime, aWaitTime, aPoolTime) : Map__

````
Tries to return an object from the queue within a map composed of two entries: idx (the unique index on the queue) and obj (the object/map queued). If aVisibilityTime is defined, the returned entry identified by idx will be returned to the queue if ow.server.queue.delete is not used within aVisibilityTime defined in ms. Optionally you can also provide aWaitTime for how much to wait for an entry to be available on the queue (defaults to 2,5 seconds) and aPoolTime (defaults to 50ms) of queue pooling interval.
````
### ow.server.queue.send

__ow.server.queue.send(aObject, aId, aTTL, aPriority) : Object__

````
Sends aObject (map) to the queue. Optionally a specific unique aId can be provided and/or aTTL (time to live) for the object in the queue in ms. Optionally aPriority can be provided and will be prefixed to aId. The final unique aId will be returned and used as the sorting based for returning objects from the queue (the lowest first).
````
### ow.server.queue.size

__ow.server.queue.size() : Number__

````
Tries to return an estimative of the current queue size.
````
### ow.server.rest.parseIndexes

__ow.server.rest.parseIndexes(aBaseURI, aHTTPRequest) : Map__

````
Given aBaseURI and aHTTPRequest will parse and determine the implicit REST API indexes
````
### ow.server.rest.reply

__ow.server.rest.reply(aBaseURI, aRequest, aCreateFunc, aGetFunc, aSetFunc, aRemoveFunc, returnWithParams, anAuditFn, returnHTML) : RequestReply__

````
Provides a REST compliant HTTPServer request replier given a aBaseURI, aRequest, aCreateFunc, aGetFunc, aSetFunc and aRemoveFunc. Each function will receive a map with the provided indexes and data from the request plus the request itself. Optionally you can  specify with returnWithParams = true that each function will not return just the data map but a composed map with: data (the actual json of data), status (the HTTP code to return) and mimetype.

var hs = ow.loadServer().httpd.start(8080);
ow.server.httpd.route(hs, ow.server.httpd.mapRoutesWithLibs(hs, {
   "/rest": function(req) { return ow.server.rest.reply("/rest", req,
      function(idxs, data, r) { // Create and return a map },
      function(idxs, r)       { // Get and return a map },
      function(idxs, data, r) { // Set and return a map },
      function(idxs, r)       { // Remove and return a map }
   )}}, function(req) { return hs.replyOKText("nothing here"); });
ow.server.daemon();
\  Optionally you can also provide anAuditFn that will be called on every request with the arguments request and reply maps.


````
### ow.server.rest.replyData

__ow.server.rest.replyData(aBaseURI, aRequest, aDataArray) : RequestReply__

````
Provides a REST JSON compliant HTTPServer request replier given a aBaseURI, aRequest and aDataArray.  The data array provided will be manipulated by REST calls.

var hs = ow.loadServer().httpd.start(8080);
ow.server.httpd.route(hs, ow.server.httpd.mapRoutesWithLibs(hs, {
   "/rest": function(req) { 
      return ow.server.rest.replyData("/rest", req, myData);
   });
ow.server.daemon();
\
````
### ow.server.rest.writeIndexes

__ow.server.rest.writeIndexes(aPropsMap) : String__

````
Given a map of REST API indexes (aPropsMap) will return a corresponding URI. Note: just a shortcut for ow.obj.rest.writeIndexes.
````
### ow.server.scheduler.addEntry

__ow.server.scheduler.addEntry(aCronExpr, aFunction, waitForFinish) : String__

````
Adds a new scheduler entry with a given aCronExpr"ession" that will trigger the scheduled execution of aFunction. If waitForFinish = true it will not execute until the previous execution has finished. Returns an UUID that can be used with the function modifyEntry later, if needed.
````
### ow.server.scheduler.modifyEntry

__ow.server.scheduler.modifyEntry(aUUID, aCronExpr, aFunction, waitForFinish) : String__

````
Changes an existing scheduler entry (aUUID) with a given aCronExpr"ession" that will trigger the scheduled execution of aFunction. If waitForFinish = true it will not execute until the previous execution has finished.
````
### ow.server.scheduler.nextUUID

__ow.server.scheduler.nextUUID() : String__

````
Returns the uuid of the next entry that will be executed.
````
### ow.server.scheduler.resetSchThread

__ow.server.scheduler.resetSchThread(aErrFunction)__

````
Resets the current scheduler thread pool adding a loop cached thread that will sleep until the next execution is due. When it executes it will add a new cached thread to execute the scheduled entry by executing the entry function provided, as argument, it's uuid.
````
### ow.server.scheduler.scheduler

__ow.server.scheduler.scheduler()__

````
Creates a new instance of a cron based scheduler with its own thread pool.
````
### ow.server.scheduler.stop

__ow.server.scheduler.stop()__

````
Attempts to force stop the current scheduler thread pool.
````
### ow.server.scheduler.timeUntilNext

__ow.server.scheduler.timeUntilNext() : Number__

````
Returns the number of ms until the next scheduled execution.
````
### ow.server.simpleCheckIn

__ow.server.simpleCheckIn(aName)__

````
If aName is provided it will check for 'aName.pid'. If the pid is running it will stop the current execution unless  stop or restart is provided as a script parameter. If stop is provided as a script parameter it will stop execution and try to kill the existing pid (force stop will try to kill it anyway). If restart is provided as a script parameter it will continue execution and try to kill the existing pid.
````
### ow.server.socket.start

__ow.server.socket.start(aPort, aFunction, aBackLog, aBindAddr)__

````
Starts a thread listening on aPort with aBackLog (defaults to a queue of 50 connections in waiting) on aBindAddr (defaults to "0.0.0.0"). Whenever a connection is established aFunction will be called with the corresponding java.net.Socket and a java.net.ServerSocket. Examples:

ow.loadServer();
ow.server.socket.start(12345, (clt, srv) => {
   log("Connection from " + clt.getInetAddress().getHostAddress());    ioStreamReadLines(clt.getInputStream(), stream => {
      print(stream);
      ioStreamWrite(clt.getOutputStream(), stream);
      clt.getOutputStream().flush();
	     clt.shutdownInput();
      clt.shutdownOutput();
      return true;
   });
   log("closing...");
   clt.close();
});


````
### ow.server.socket.stop

__ow.server.socket.stop(aPort)__

````
Stops a thread socket server on aPort previously started by ow.server.socket.start.
````
### ow.server.telemetry.active

__ow.server.telemetry.active(aSendFunc, aPeriod)__

````
Setup recurrent execution of aSendFunc with the propose of sending ow.metrics for a provided aPeriod (defaults to 60000 ms).
````
### ow.server.telemetry.passive

__ow.server.telemetry.passive(aHTTPdOrPort, aURI, useOpenMetrics, openMetricsPrefix, openMetricsHelp)__

````
Setup a HTTPd server on aHTTPdOrPort (defaults to 7777) on the aURI (defaults to /healthz) to  serve ow.metrics.getAll. If the parameter "s" is present the value will be split by commas and used for ow.metrics.getSome. Optionally if useOpenMetrics = true the default of aURI becomes /metrics and the output becomes open metrics (prometheus) using openMetricsPrefix (defaults to "metrics") and uses the openMetricsHelp where each key is a open metric entry associated with map with text (description text), help (help text) and type (metrics type).
````
### ow.server.telemetry.send2nAttrMon

__ow.server.telemetry.send2nAttrMon(anAttrMonCValsURL, anAttrPrefix, anArrayOfMetricNames) : Function__

````
Returns a function to be used with ow.server.telemetry.active to send metrics to nAttrMon using the provided anAttrMonCValsURL, anAttrPrefix (e.g. "myjobname/") and, optionally, an array of metrics (anArrayOfMetricsNames)
````
### ow.server.telemetry.send2Prometheus

__ow.server.telemetry.send2Prometheus(aPrometheusGatewayURL, aPrefix, anArrayOfMetricNames) : Function__

````
Returns a function to be used with ow.server.telemetry.active to send metrics to a OpenMetrics/Prometheus gateway using the provided aPrometheusGatewayURL with aPrefix (e.g. "myjobname") and, optionally, an array of metrics (anArrayOfMetricsNames)
````
