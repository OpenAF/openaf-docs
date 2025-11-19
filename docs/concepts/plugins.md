---
layout: default
title: Plugins
parent: Concepts
nav_order: 8
---

# OpenAF Plugins

OpenAF plugins extend the core functionality by providing access to Java libraries and additional features through a simple JavaScript interface.

## Overview

Plugins are dynamically loaded Java components that expose specialized functionality to OpenAF scripts. They provide:

- **Java integration** - Access Java libraries from JavaScript
- **Extended functionality** - Features beyond core OpenAF
- **Performance optimization** - Native Java performance for heavy operations
- **Third-party integration** - Leverage existing Java ecosystems

---

## Loading Plugins

### Basic Syntax

```javascript
plugin("PluginName");
```

### Available Core Plugins

| Plugin | Purpose | Common Uses |
|--------|---------|-------------|
| `HTTP` | HTTP client operations | REST API calls, web requests |
| `HTTPd` | HTTP server | Web servers, REST APIs |
| `HTTPws` | WebSocket support | Real-time communication |
| `ZIP` | Archive operations | Compress/decompress files |
| `SSH` | SSH client | Remote command execution |
| `XML` | XML processing | Parse/generate XML |
| `SNMP` | SNMP client | Network monitoring |
| `SNMPServer` | SNMP server | Expose SNMP endpoints |
| `JMX` | JMX client | Java application monitoring |
| `JMXServer` | JMX server | Expose JMX beans |
| `Threads` | Threading support | Parallel execution |
| `Console` | Console operations | Terminal colors, formatting |
| `Email` | Email sending | SMTP email |
| `XLS` | Excel files | Read/write spreadsheets |
| `Ignite` | Apache Ignite | Distributed computing |
| `Beautifiers` | Code formatting | Pretty-print code |
| `BSDiff` | Binary diff/patch | Binary file operations |

---

## Common Plugin Usage

### HTTP Plugin

```javascript
plugin("HTTP");

var http = new HTTP("https://api.example.com");
var response = http.get("/endpoint");
print(response);
```

Or use the simplified `$rest()` API:

```javascript
ow.loadObj();

var data = $rest()
  .get("https://api.example.com/data")
  .getResponse();
```

### SSH Plugin

```javascript
plugin("SSH");

var ssh = new SSH("hostname", 22, "username", "password");
ssh.connect();

var output = ssh.exec("ls -la");
print(output);

ssh.disconnect();
```

### ZIP Plugin

```javascript
plugin("ZIP");

// Create ZIP
var zip = new ZIP();
zip.generate("output.zip", [
  { file: "data.txt" },
  { file: "config.json" }
]);

// Extract ZIP
zip.unzip("archive.zip", "./extracted/");
```

### XML Plugin

```javascript
plugin("XML");

// Parse XML
var xml = new XML("<root><item>value</item></root>");
var value = xml.getPath("/root/item");
print(value);

// Generate XML
var doc = new XML();
doc.addElement("root");
doc.addElement("item", "value");
print(doc.toString());
```

### Threads Plugin

```javascript
plugin("Threads");

var t = new Threads();

// Add thread function
t.addThread(function() {
  log("Thread 1 running");
  sleep(1000, true);
});

t.addThread(function() {
  log("Thread 2 running");
  sleep(1000, true);
});

// Start and wait
t.start();
```

### Email Plugin

```javascript
plugin("Email");

var email = new Email();
email.send({
  server: "smtp.example.com",
  from: "sender@example.com",
  to: ["recipient@example.com"],
  subject: "Test Email",
  body: "This is a test message"
});
```

### XLS Plugin

```javascript
plugin("XLS");

// Create Excel file
var xls = new XLS();
var sheet = xls.getSheet("Data");

xls.setCellValue(sheet, "A1", "Name");
xls.setCellValue(sheet, "B1", "Value");
xls.setCellValue(sheet, "A2", "Item 1");
xls.setCellValue(sheet, "B2", 100);

xls.writeFile("output.xlsx");
xls.close();
```

---

## Plugin Patterns

### Conditional Loading

```javascript
// Load plugin only if needed
if (needsSSH) {
  plugin("SSH");
  var ssh = new SSH(host, port, user, pass);
  // Use SSH
}
```

### Error Handling

```javascript
try {
  plugin("HTTP");
  var http = new HTTP(url);
  var response = http.get("/api");
} catch(e) {
  logErr("HTTP request failed: " + e.message);
}
```

### Resource Cleanup

```javascript
plugin("SSH");

var ssh = new SSH(host, port, user, pass);

try {
  ssh.connect();
  var result = ssh.exec(command);
  // Process result
} finally {
  ssh.disconnect();
}
```

---

## Custom Plugins

### Plugin Structure

Custom plugins follow Java conventions:

```java
package openaf.plugins;

public class MyPlugin {
    public String doSomething(String input) {
        return "Processed: " + input;
    }
}
```

### Loading Custom Plugins

```javascript
// Load from classpath
plugin("openaf.plugins.MyPlugin");

// Use plugin
var mp = new MyPlugin();
var result = mp.doSomething("test");
```

---

## Plugin Best Practices

### 1. Load Plugins Early

```javascript
// Good - load at start
plugin("HTTP");
plugin("ZIP");

// Then use throughout script
var http = new HTTP(url);
var zip = new ZIP();
```

### 2. Reuse Plugin Instances

```javascript
// Good - create once, use multiple times
plugin("SSH");
var ssh = new SSH(host, port, user, pass);
ssh.connect();

ssh.exec("command1");
ssh.exec("command2");

ssh.disconnect();

// Bad - creating multiple instances
plugin("SSH");
new SSH(host, port, user, pass).exec("command1");
new SSH(host, port, user, pass).exec("command2");
```

### 3. Use Wrapper Functions

OpenAF provides wrapper modules for common plugins:

```javascript
// Instead of direct plugin usage
plugin("HTTP");
var http = new HTTP(url);

// Use wrapper
ow.loadObj();
var data = $rest().get(url).getResponse();
```

### 4. Check Plugin Availability

```javascript
try {
  plugin("OptionalPlugin");
  // Use plugin
} catch(e) {
  log("Optional plugin not available, using fallback");
  // Fallback implementation
}
```

---

## When to Use Plugins

### Use Plugins For:

- ✅ Java library integration
- ✅ Performance-critical operations
- ✅ System-level operations (SSH, SNMP)
- ✅ Binary file handling
- ✅ Protocol implementations

### Use Built-in Functions For:

- ✅ File I/O operations
- ✅ JSON/YAML processing
- ✅ String manipulation
- ✅ Array/object operations
- ✅ Basic HTTP requests (use `$rest()`)

---

## Plugin Dependencies

### OpenWrap Modules Using Plugins

Many `ow.*` modules load plugins automatically:

- `ow.loadFormat()` → loads `Console`
- `ow.loadServer()` → loads `HTTPServer`, `Threads`
- `ow.loadObj()` → loads `HTTP`
- `ow.loadJava()` → loads `JMX`, `XML`, `ZIP`

### Checking Plugin Dependencies

```javascript
// View which plugins a module uses
var deps = af.getOPackDeps("ModuleName");
print(af.toYAML(deps));
```

---

## Troubleshooting

### Plugin Not Found

**Error:** `Plugin 'PluginName' not found`

**Solutions:**
1. Check spelling
2. Ensure OpenAF is properly installed
3. Check if plugin is available in your OpenAF version

### ClassNotFoundException

**Error:** `java.lang.ClassNotFoundException`

**Solutions:**
1. Add required JARs to classpath
2. Use `af.externalAddClasspath(path)`
3. Check plugin installation

### Version Conflicts

If you encounter version conflicts:

```javascript
// Specify exact plugin class
plugin("openaf.plugins.HTTP", "HTTP");
```

---

## See Also

- [HTTP Plugin Usage](../guides/beginner/rest-calls.md)
- [SSH Plugin Guide](../guides/beginner/ojob-ssh-basics.md)
- [XLS Plugin Guide](../guides/ojob/ojob-xls.md)
- [Threads Reference](../reference/threads.md)
