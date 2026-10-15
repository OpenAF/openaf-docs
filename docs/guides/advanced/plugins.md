---
layout: default
title: "OpenAF Core Java Plugins Reference Guide"
parent: Advanced
grand_parent: Guides
---

# OpenAF Core Java Plugins Reference Guide

OpenAF includes a suite of native Java plugins compiled into `openaf.jar` (`src/openaf/plugins/`). Plugins extend the JavaScript runtime with high-performance networking, enterprise protocols, multi-threading, cryptography, and terminal interfaces.

---

## Loading Plugins in OpenAF

Java plugins are dynamically loaded into JavaScript using the global `plugin(...)` function:

```javascript
// Method 1: Get the plugin Class wrapper
var Email = plugin("Email");
var email = new Email();

// Method 2: Direct instantiation
var http = new (plugin("HTTP"))();

// Method 3: Plugin with arguments
var console = new (plugin("Console"))();
```

---

## Inventory of Core Java Plugins

| Plugin Name | Java Class | Primary Capabilities | Documentation Link |
| :--- | :--- | :--- | :--- |
| **BSDiff** | `BSDiff.java` | Binary diffing and patch application using the BSDiff algorithm. | [BSDiff.md](https://github.com/OpenAF/openaf/blob/a5181af6/docs/plugins/BSDiff.md) |
| **Beautifiers** | `Beautifiers.java` | Formatting and beautifying source code (JS, JSON, XML, HTML, CSS). | [Beautifiers.md](https://github.com/OpenAF/openaf/blob/a5181af6/docs/plugins/Beautifiers.md) |
| **Console** | `Console.java` | Interactive JLine terminal console, character reading, password masking, autocompletion. | [Console.md](https://github.com/OpenAF/openaf/blob/a5181af6/docs/plugins/Console.md) |
| **Email** | `Email.java` | SMTP email client with SSL/TLS, HTML body, attachments, and authentication. | [Email.md](https://github.com/OpenAF/openaf/blob/a5181af6/docs/plugins/Email.md) |
| **FTP** | `FTP.java` | Plain FTP and TLS-secured FTPS file transfers, uploads, downloads, directory listing. | [FTP.md](https://github.com/OpenAF/openaf/blob/a5181af6/docs/plugins/FTP.md) |
| **HTTP** | `HTTP.java` | HTTP/HTTPS client with connection pooling, SSL truststores, multipart uploads, and cookies. | [HTTP.md](https://github.com/OpenAF/openaf/blob/a5181af6/docs/plugins/HTTP.md) |
| **HTTPServer** | `HTTPServer.java` | Embedded HTTP/HTTPS microservice web server, REST endpoints, file serving, WebSockets. | [HTTPServer.md](https://github.com/OpenAF/openaf/blob/a5181af6/docs/plugins/HTTPServer.md) |
| **JMX** | `JMX.java` | JMX client to inspect remote JVM MBeans, attributes, and invoke operations. | [JMX.md](https://github.com/OpenAF/openaf/blob/a5181af6/docs/plugins/JMX.md) |
| **JMXServer** | `JMXServer.java` | Embedded JMX server to expose JVM metrics and remote operations over RMI. | [JMX.md](https://github.com/OpenAF/openaf/blob/a5181af6/docs/plugins/JMX.md) |
| **SNMP** | `SNMP.java` | SNMP v1/v2c/v3 client for GET, SET, and WALK queries against network hardware. | [SNMP.md](https://github.com/OpenAF/openaf/blob/a5181af6/docs/plugins/SNMP.md) |
| **SNMPServer** | `SNMPServer.java` | Embedded SNMP agent and trap listener server. | [SNMP.md](https://github.com/OpenAF/openaf/blob/a5181af6/docs/plugins/SNMP.md) |
| **SSH** | `SSH.java` | SSH2 & SFTP client for command execution, interactive PTY, port forwarding, and file transfer. | [SSH.md](https://github.com/OpenAF/openaf/blob/a5181af6/docs/plugins/SSH.md) |
| **Threads** | `Threads.java` | Thread pool management, locks, condition variables, and synchronized blocks. | [Threads.md](https://github.com/OpenAF/openaf/blob/a5181af6/docs/plugins/Threads.md) |
| **XML** | `XML.java` | High-performance XML DOM parsing, XPath evaluations, XML-to-JSON and JSON-to-XML mapping. | [XML.md](https://github.com/OpenAF/openaf/blob/a5181af6/docs/plugins/XML.md) |
| **ZIP** | `ZIP.java` | ZIP archive creation, extraction, in-memory stream zip manipulation, and compression. | [ZIP.md](https://github.com/OpenAF/openaf/blob/a5181af6/docs/plugins/ZIP.md) |
