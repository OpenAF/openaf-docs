---
layout: default
title: snmpd
parent: Reference
grand_parent: OpenAF docs
---

{% raw %}
## snmpd

[Source: `06414cd9`](https://github.com/OpenAF/openaf/blob/06414cd9204e918daa1e2971ce904783299db333/src/openaf/plugins/SNMPServer.java) · [Baseline](../source-snapshot.md)

### SNMPD.addOID

`SNMPD.addOID(aOID, aFunction)`

````text
Adds a callback when the specified OID (should end in .0) gets look up. The call back aFunction receives the aOID as a parameter. See more: http://www.jitendrazaa.com/blog/java/snmp/creating-snmp-agent-server-in-java-using-snmp4j/
````

### SNMPd.SNMPd

`SNMPd.SNMPd(anAddress, aSysDesc) : SNMPd`

````text
Prepares a SNMP server listening on the given anAddress (e.g. udp:1.2.3.4/161). Optionally you can also provide a system description (aSysDesc).
````

### SNMPd.setOID

`SNMPd.setOID(aOID, aFunction)`

````text
Changes the callback for a specific OID (should end in .0). The call back aFunction receives the aOID as a parameter.
````

### SNMPd.start

`SNMPd.start(aCommunity)`

````text
Starts the SNMP server given a community name. If no community is provided, public is assumed.
````

### SNMPd.stop

`SNMPd.stop()`

````text
Stops the SNMP server.
````
{% endraw %}
