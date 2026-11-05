---
layout: default
title: ow.net
parent: Reference
grand_parent: OpenAF docs
---

{% raw %}
## ow.net

[Source: `06414cd9`](https://github.com/OpenAF/openaf/blob/06414cd9204e918daa1e2971ce904783299db333/js/owrap.net.js) · [Baseline](../source-snapshot.md)

### ow.net.asnIndexASN2IP

`ow.net.asnIndexASN2IP(aASN, aidx) : Map`

````text
Given an aASN will try to retrieve the corresponding ASN information from the aidx. Returns a map with the ASN information. The aidx is expected to be an array with the following structure: [ { i: (index), a: (asn), s: (start), e: (end) }, ... ] where i is the index in the original aIP2ASNCache, a is the ASN number, s is the start IP in integer format and e is the end IP in integer format.
````

### ow.net.asnIndexIP2ASN

`ow.net.asnIndexIP2ASN(aIP, aidx) : Map`

````text
Given an aIP (or host) will try to retrieve the corresponding ASN information from the aidx (defaults to the one retrieved by ow.net.getIP2ASNIndex()). Returns a map with the ASN information. The aidx is expected to be an array with the following structure: [ { i: (index), a: (asn), s: (start), e: (end) }, ... ] where i is the index in the original aIP2ASNCache, a is the ASN number, s is the start IP in integer format and e is the end IP in integer format.
````

### ow.net.createIP2ASNIndex

`ow.net.createIP2ASNIndex(aFile, aIP2ASNCache, logFn, aDescFile)`

````text
Creates an ASN index from the aIP2ASNCache (defaults to the one retrieved by ow.net.getIP2ASNCache()) and saves it into aFile. If aIP2ASNCache is not provided it will be retrieved using ow.net.getIP2ASNCache(). The index is saved as a JSON array with the following structure: [ { i: (index), a: (asn), s: (start), e: (end) }, ... ] where i is the index in the original aIP2ASNCache, a is the ASN number, s is the start IP in integer format and e is the end IP in integer format. The aFile is saved as a gzip compressed JSON file. The aDescFile is optional and if provided it will create a descriptive index with the following structure: [ { i: (index), r: (area), n: (name) }, ... ] where i is the index in the original aIP2ASNCache, r is the area and n is the name. The aDescFile is also saved as a gzip compressed JSON file.
````

### ow.net.doh

`ow.net.doh(aAddr, aType, aProvider, aCache, aCacheTimeout) : String`

````text
Performs a DNS over HTTPs query with aAddr. Optionally you can provide the aType of record (defaults to 'a') and the DNS over HTTPs aProvider between 'google', 'cloudflare', 'nextdns' and 'local' (that doesn't use DoH but fallbacks to  Java's DNS resolver), or a custom DoH endpoint URL. Returns the first IP address found. If aCache is provided (optionally with aCacheTimeout in ms) the results will be cached.
````

### ow.net.getActualTime

`ow.net.getActualTime(aServer, aTimeout) : Date`

````text
Retrieves the current actual time from NTP servers. The current actual time will be returned in a Date. If aServer is provided, it will use that specific server, otherwise it will try multiple public NTP servers in sequence: 'pool.ntp.org', 'time.google.com', 'time-a.nist.gov', 'europe.pool.ntp.org'. aTimeout is optional and defaults to 5000ms.
````

### ow.net.getAddressInfo

`ow.net.getAddressInfo(aAddress) : Map`

````text
Given an IPv4 or IPv6 aAddress will return a map with hostname, address and corresponding address flags to determine which type of address it is (is it a private address? is it a loopback? is it a multicast address?)
````

### ow.net.getAddressType

`ow.net.getAddressType(aAddress) : Map`

````text
Given aAddress tries to return a map with the following flags: isValidAddress, hostname, ipv4, ipv6 and privateAddress
````

### ow.net.getCAStoredCertificates

`ow.net.getCAStoredCertificates(aPassword) : Array`

````text
Will retrieve a list of aliases, issuer DN, subject DN, expire notBefore and notAfter dates from the current Java "cacerts" file. Optionally aPassword can be provided if different from the default one.
````

### ow.net.getDNS

`ow.net.getDNS(aName, aType, aServer, aExtended) : Object`

````text
Given aName will do a DNS search for aType (defaults to "a") optionally using dns server aServer. Returns an object or an array of objects. If aExtended is true it will return a more detailed JSON object.
````

### ow.net.getDoH

`ow.net.getDoH(aAddr, aType, aProvider) : Array`

````text
Performs a DNS over HTTPs query with aAddr. Optionally you can provide the aType of record (defaults to 'a') and the DNS over HTTPs aProvider between 'google', 'cloudflare', 'nextdns' and 'local' (that doesn't use DoH but fallbacks to  Java's DNS resolver). You can also provide aProvider as the URL of a custom DNS over HTTPS endpoint.
````

### ow.net.getHost2IP

`ow.net.getHost2IP(aHost) : String`

````text
Tries to resolve aHost to an IP address using the default DNS.
````

### ow.net.getHostAddress

`ow.net.getHostAddress() : String`

````text
Returns the current host ip address.
````

### ow.net.getHostName

`ow.net.getHostName() : String`

````text
Returns the current hostname.
````

### ow.net.getIP2ASN

`ow.net.getIP2ASN(aIP, aIP2ASNCache, aTimeout) : Map`

````text
Given an aIP will try to retrieve the corresponding ASN information from the aIP2ASNCache (defaults to the one retrieved by ow.net.getIP2ASNCache()). If aIP2ASNCache is not provided it will be retrieved and cached as "ow.net.ip2asn" with aTimeout by default of 24 hours. Returns a map with the ASN information.
````

### ow.net.getIP2ASNCache

`ow.net.getIP2ASNCache() : Array`

````text
Retrieves the current IP to ASN cache from the iptoasn.com service returning as an array.
````

### ow.net.getIP2ASNIndex

`ow.net.getIP2ASNIndex(aFile) : Array`

````text
Given aFile will try to retrieve the ASN index from the file. The file is expected to be a gzip compressed JSON file with the following structure (produced with ow.net.createIP2ASNIndex()): [ { i: (index), a: (asn), s: (start), e: (end) }, ... ] where i is the index in the original aIP2ASNCache, a is the ASN number, s is the start IP in integer format and e is the end IP in integer format. Returns an array with the ASN index. Can also be used to retrieve the ASN descriptive index.
````

### ow.net.getIP2Host

`ow.net.getIP2Host(aIP) : String`

````text
Tries to reverse DNS aIP to a host address using the default DNS.
````

### ow.net.getJSSECAStoredCertificates

`ow.net.getJSSECAStoredCertificates(aPassword) : Array`

````text
Will retrieve a list of aliases, issuer DN, subject DN, expire notBefore and notAfter dates from the current Java "jssecacerts" file. Optionally aPassword can be provided if different from the default one.
````

### ow.net.getPublicIP

`ow.net.getPublicIP(aIPAddress) : Map`

````text
Uses the functionality provided by https://ifconfig.co to return a map with the apparent current public ip address, public hostname and a guess of country and city. Please be aware of the request limits of the service (around 1 request per minute).
If aIPAddress is provided it will use the functionality provided by http://ip-api.com (if aIPAddress is a empty string it will use the current public IP address). Please be also aware of non-commercial and request limits of the service (around 45 requests per minute). The details provided by each service might differ depending on how update is each of the services' databases.
````

### ow.net.getReverseDoH

`ow.net.getReverseDoH(aIP, aProvider) : Array`

````text
Tries to retrieve the reverse DNS of aIP using DNS over HTTPs. Optionally you can choose the aProvider between 'google' and 'cloudflare'.
````

### ow.net.getSSLPublicCertificates

`ow.net.getSSLPublicCertificates(aHost, aPort) : Array`

````text
Given aHost and aPort for a HTTPs connection it will retrieve the array of peer certificates available. You can retrieve the specific public key by using the method .getPublicKey for each array element. Usually you be interested on the first certificate of the returned array.
````

### ow.net.getStoredCertificates

`ow.net.getStoredCertificates(aStoreFile, aPassword) : Array`

````text
Given a Java certificate store (aStoreFile) will retrieve a list of aliases, issuer DN, subject DN, expire notBefore and notAfter dates. Optionally aPassword can be provided if different from the default one.
````

### ow.net.getTLSCertificates

`ow.net.getTLSCertificates(aHost, aPort, withJava, aPath, aPass, aSoTimeout) : Array`

````text
Tries to retreive the TLS certificates from aHost, aPort (defaults to 443). Optionally if withJava=true the original certificate Java object will also be included. If the CA certificates is in a different location you can provide aPath and the corresponding aPass. Additionally you can specificy aSoTimeout (socket timeout in ms) which defaults to 10s.
````

### ow.net.getWhoIs

`ow.net.getWhoIs(aQuery, aInitServer) : Map`

````text
Tries to perform a whois aQuery for a domain or an ip address. Optionally you can provide aInitServer (defaults to whois.iana.org)
````

### ow.net.host4URL

`ow.net.host4URL(aURL) : String`

````text
Given aURL it will return the corresponding host:port.
````

### ow.net.ipv4SubNetInRange

`ow.net.ipv4SubNetInRange(aTestAddress, aCIDRorAddress, aMask) : boolean`

````text
Given IPv4 aTestAddress and a aCIDR or anAddress with aMask will return true if the aTestAddress is part of the subnet represented by aCIDR or aAddress + aMask (false otherwise).
````

### ow.net.ipv4SubNetInfo

`ow.net.ipv4SubNetInfo(aCIDRorAddress, aMask) : Map`

````text
Given an IPv4 aCIDR or anAddress with aMask will return a map with the corresponding subnet info including netmask, broadcast address, address count, low & high address, etc...
````

### ow.net.isHost

`ow.net.isHost(aHost) : boolean`

````text
Tries to determine if aHost seems a syntactic valid host.
````

### ow.net.isIPv4

`ow.net.isIPv4(aIP) : boolean`

````text
Tries to determine if aIP is a syntactic valid IPv4.
````

### ow.net.isIPv6

`ow.net.isIPv6(aIP) : boolean`

````text
Tries to determine if aIP is a syntactic valid IPv6.
````

### ow.net.isURL

`ow.net.isURL(aURL) : boolean`

````text
Tries to determine if aURL seems a syntactic valid URL.
````

### ow.net.path4URL

`ow.net.path4URL(aURL) : String`

````text
Given aURL it will return the corresponding path.
````

### ow.net.sendTCPPacket

`ow.net.sendTCPPacket(aHost, aPort, aMsg, dontWait) : Bytes`

````text
Tries to send a string or array of bytes aMsh to aHost and aPort using TCP. If dontWait=true it won't wait for a response.
````

### ow.net.sendUDPPacket

`ow.net.sendUDPPacket(aHost, aPort, aMsg, dontWait, bufferSize) : Bytes`

````text
Tries to send a string or array of bytes aMsh to aHost and aPort using UDP. If dontWait=true it won't wait for a response that is stored in a buffer (where bufferSize = 1024 bytes, by default).
````

### ow.net.testHost

`ow.net.testHost(aAddress, aTimeout) : Map`

````text
Uses the java implementation (e.g. usually ICMP ping) for testing reachability to an aAddress. It timeouts after aTimeout (defaults to 4000ms). Returns a map with the "time" spent trying to get an answer from aAddress and a boolean "reachable" with the result.
````

### ow.net.testPort

`ow.net.testPort(aAddress, aPort, aCustomTimeout) : boolean`

````text
Tries to connect to aPort (e.g. 1234) on aAddress (e.g. 1.2.3.4). If the connection is successfull it will disconnect and return true, otherwise it will return false. If aCustomTimeout (in ms) is defined, it will use that value as the timeout instead of the 1,5 seconds by default.
````

### ow.net.testPortLatency

`ow.net.testPortLatency(aHost, aPort, aCustomTimeout) : Number`

````text
Test establishing a TCP socket connection with aHost on aPort. Optionally aCustomTimeout can be provided (defaults to 60000 ms). The test will be timed and the time in ms will be returned. If returned a time < 0 then an error occurred or the  host:port couldn't be reached.
````

### ow.net.testPublicPort

`ow.net.testPublicPort(aPort) : Map`

````text
Uses the functionality provided by http://ifconfig.co to return a map with the result of testing if aPort is within public  reach from your apparent current public ip address. Please be aware of the request limits of the service (around 1 request per minute).
````

### ow.net.testURLLatency

`ow.net.testURLLatency(aURL, aCustomTimeout) : Number`

````text
Test sending a HTTP(s) GET to aURL. Optionally aCustomTimeout can be provided. The test will be timed and the time in ms will be returned. If returned a time < 0 then an error occurred or the host:port couldn't be reached.
````
{% endraw %}
