---
layout: default
title: Plugins
parent: Concepts
grand_parent: OpenAF docs
nav_order: 8
---

{% raw %}
# OpenAF plugins

Plugins expose Java functionality to OpenAF's JavaScript runtime. Load a plugin with `plugin("Name")`; load JavaScript wrapper modules with their `ow.load…()` function or an oPack's documented `loadLib()` entry point.

## Core and optional plugins

| Capability | Load / documentation |
| --- | --- |
| HTTP client and WebSockets | `plugin("HTTP")`; [HTTP guide](../guides/advanced/plugin-http.md) |
| HTTP server | `plugin("HTTPServer")`; [server guide](../guides/advanced/plugin-httpserver.md) |
| SSH and SFTP | `plugin("SSH")`; [SSH guide](../guides/advanced/plugin-ssh.md) |
| ZIP archives | `plugin("ZIP")`; [ZIP guide](../guides/advanced/plugin-zip.md) |
| Threads and scheduling | `plugin("Threads")`; [Threads guide](../guides/advanced/plugin-threads.md) |
| Email | `plugin("Email")`; [Email guide](../guides/advanced/plugin-email.md) |
| XML | [Java XML plugin](../guides/advanced/plugin-xml.md) and [E4X](../guides/medium/accessing-xml-using-e4x.md) |
| SNMP / JMX | [SNMP](../guides/advanced/plugin-snmp.md), [JMX](../guides/advanced/plugin-jmx.md) |
| Spreadsheets | Install `plugin-XLS`, then `plugin("XLS")`; [spreadsheet guide](../guides/ojob/ojob-xls.md) |
| Git, SMB, SVN, Ignite and JavaFX | Separate oPacks; see the [package catalog](../guides/opacks/catalog.md) |

`HTTPd` and `HTTPws` are not core plugin names. Use `HTTPServer` for servers and the HTTP plugin's WebSocket methods. XLS and Ignite are optional packages, not part of every core installation.

## HTTP requests

For JSON APIs, `$rest()` returns the decoded result directly:

```javascript
var data = $rest({ throwExceptions: true }).get("https://api.example.com/data");
print(data);
```

Do not chain `.getResponse()` onto the object returned by `$rest().get()`. The lower-level HTTP client has its own request and response methods; see the [HTTP reference](../reference/http.md).

## SSH sessions

The constructor opens the session. Close it when the work is complete:

```javascript
plugin("SSH");
var ssh = new SSH("host.example", 22, "user", "password");
try {
  print(ssh.exec("uname -s"));
} finally {
  ssh.close();
}
```

The host and credentials are placeholders. Follow the [SSH reference](../reference/ssh.md) for private keys, host-key handling, timeouts and return options.

## ZIP archives

```javascript
plugin("ZIP");
var zip = new ZIP();
try {
  zip.putFile("hello.txt", af.fromString2Bytes("Hello\n"));
  io.writeFileBytes("example.zip", zip.generate({ compressionLevel: 9 }));
} finally {
  zip.close();
}
```

`putFile` receives bytes for the archive entry. To archive a local file, pass `io.readFileBytes(path)`. The [ZIP reference](../reference/zip.md) also documents streaming operations and resource ownership.

## Loading and troubleshooting

Install an optional package before loading its plugin, and check its JVM/native requirements. Use `opack list` to inspect installed packages and `help` in `oafc` to inspect the runtime's API. `ClassNotFoundException` usually requires checking the package's JARs, classpath and Java version.

A Java class alone is not automatically a scriptable OpenAF plugin. Follow the [core plugin guide](../guides/advanced/plugins.md) and an existing plugin implementation for Rhino bindings, constructors and exported methods.
{% endraw %}
