---
layout: default
title: Advanced MCP Server Patterns
parent: oJob
grand_parent: Guides
---

# Advanced MCP Server Patterns

This guide covers advanced patterns for building Model Context Protocol (MCP) servers with OpenAF, including custom tool implementations, JSON-RPC handling, and integration strategies.

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## Prerequisites

Before starting, ensure you:
- Understand basic [MCP server concepts](build-mcp-server.md)
- Have OpenAF installed with oJob-common
- Familiarity with oJob YAML structure

---

## MCP Server Architecture

The OpenAF MCP server implementation uses HTTP-based JSON-RPC 2.0 protocol to communicate with MCP clients.

### Core Components

```yaml
include:
  - oJobMCP.yaml

jobs:
  - name: My MCP Server
    to: HTTP MCP Server
    args:
      port: 8080
      uri: /mcp
      debug: false
      description:
        serverInfo:
          name: MyServer
          version: 1.0.0
      fnsMeta:
        # Tool metadata
      fns:
        # Tool implementations
```

### Key Arguments

| Argument | Type | Description |
|----------|------|-------------|
| `port` | Number | HTTP server port |
| `uri` | String | Endpoint URI (default: `/mcp`) |
| `debug` | Boolean | Enable debug logging |
| `description` | Map | Server capabilities and metadata |
| `fnsMeta` | Map | Tool/function metadata definitions |
| `fns` | Map | Tool/function implementations |

---

## Implementing Custom Tools

### Basic Tool Structure

Tools are defined in two parts:
1. **Metadata** (`fnsMeta`) - Describes the tool's interface
2. **Implementation** (`fns`) - The job that executes the tool

### Example: File Reader Tool

```yaml
include:
  - oJobMCP.yaml

jobs:
  # Tool implementation
  - name: Read File Tool
    check:
      in:
        path: isString
    exec: |
      args.result = {
        content: [{
          type: "text",
          text: io.readFileString(args.path)
        }]
      }

  # MCP Server
  - name: File Operations MCP
    to: HTTP MCP Server
    args:
      port: 3000
      uri: /mcp
      debug: true

      description:
        serverInfo:
          name: FileOps
          title: File Operations MCP Server
          version: 1.0.0
        capabilities:
          tools:
            listChanged: true

      fnsMeta:
        read_file:
          description: Reads a file and returns its contents
          inputSchema:
            type: object
            properties:
              path:
                type: string
                description: Path to the file to read
            required:
              - path

      fns:
        read_file: Read File Tool

todo:
  - HTTP Start Server
  - File Operations MCP

ojob:
  daemon: true
```

### Tool Response Format

MCP tools must return responses in this format:

```javascript
{
  content: [
    {
      type: "text",
      text: "The response text"
    }
  ],
  isError: false  // Optional, indicates if this is an error
}
```

---

## Advanced Tool Patterns

### Multi-Step Tool Execution

```yaml
jobs:
  - name: Complex Analysis Tool
    exec: |
      // Step 1: Validate input
      _$(args.data, "data").isString().$_()

      // Step 2: Process data
      var parsed = jsonParse(args.data)
      var analysis = $from(parsed)
        .select(r => ({
          key: r.name,
          value: r.value,
          analysis: r.value > 100 ? "high" : "low"
        }))

      // Step 3: Generate report
      var report = "Analysis Results:\n"
      analysis.forEach(item => {
        report += `- ${item.key}: ${item.value} (${item.analysis})\n`
      })

      // Step 4: Return formatted response
      args.result = {
        content: [{
          type: "text",
          text: report
        }]
      }
```

### Error Handling

```yaml
jobs:
  - name: Safe Tool Execution
    exec: |
      try {
        _$(args.input, "input").isString().$_()

        // Your tool logic here
        var result = processInput(args.input)

        args.result = {
          content: [{
            type: "text",
            text: stringify(result, void 0, "")
          }]
        }
      } catch(e) {
        logErr("Tool execution failed: " + e.message)
        args.result = {
          content: [{
            type: "text",
            text: "Error: " + e.message
          }],
          isError: true
        }
      }
```

### Tools with External API Calls

```yaml
jobs:
  - name: Weather API Tool
    check:
      in:
        city: isString
    exec: |
      ow.loadObj()

      try {
        // Call external API
        var response = $rest()
          .get("https://api.weather.example.com/current")
          .query({ city: args.city })
          .getResponse()

        if (response.status != 200) {
          throw "API returned status " + response.status
        }

        var weather = response.data

        args.result = {
          content: [{
            type: "text",
            text: templify("Weather in {{city}}: {{temp}}°C, {{condition}}", weather)
          }]
        }
      } catch(e) {
        args.result = {
          content: [{
            type: "text",
            text: "Failed to fetch weather: " + e.message
          }],
          isError: true
        }
      }
```

---

## JSON-RPC Protocol Handling

### Understanding the Protocol Flow

The MCP server handles these JSON-RPC methods:

1. **initialize** - Client handshake
2. **notifications/initialized** - Initialization complete
3. **notifications/cancelled** - Operation cancelled
4. **tools/call** - Execute a tool
5. **tools/list** - List available tools (auto-generated)

### Custom Protocol Extensions

You can extend the MCP server with custom methods:

```yaml
jobs:
  - name: Extended MCP Server
    deps:
      - HTTP Start Server
    exec: |
      var customFns = {}

      customFns["/mcp"] = req => {
        var handlers = {
          initialize: params => ({
            protocolVersion: "2024-11-05",
            serverInfo: {
              name: "CustomMCP",
              version: "1.0.0"
            }
          }),

          "tools/call": params => {
            // Custom tool handling
            if (params.name == "special_tool") {
              return {
                content: [{
                  type: "text",
                  text: "Special handling"
                }]
              }
            }

            // Default handling
            return $job(args.fns[params.name], params.arguments || {})
          },

          "custom/method": params => {
            // Your custom method
            return { status: "ok" }
          }
        }

        return ow.server.httpd.replyJSONRPC(
          global.__ojobHttp[args.port],
          req,
          handlers
        )
      }

      $ch("__oJobHTTPd::fns::" + args.port).setAll(["uri"], customFns)
```

---

## Integration Patterns

### Database-Backed Tools

```yaml
include:
  - oJobMCP.yaml
  - oJobSQL.yaml

ojob:
  sequential: true

jobs:
  # Database query tool
  - name: Query Database Tool
    check:
      in:
        sql: isString
    exec: |
      var result = $job("SQL", {
        DBURL: getEnv("DB_URL"),
        DBUser: getEnv("DB_USER"),
        DBPass: getEnv("DB_PASS"),
        sql: args.sql
      })

      args.result = {
        content: [{
          type: "text",
          text: af.toYAML(result.output)
        }]
      }

  # MCP Server with DB tools
  - name: Database MCP Server
    to: HTTP MCP Server
    args:
      port: 3001
      fnsMeta:
        query_db:
          description: Execute a SQL query
          inputSchema:
            type: object
            properties:
              sql:
                type: string
                description: SQL query to execute
            required: [sql]
      fns:
        query_db: Query Database Tool

todo:
  - HTTP Start Server
  - Database MCP Server

ojob:
  daemon: true
```

### Channel-Based State Management

```yaml
jobs:
  # Initialize shared state
  - name: Init MCP State
    exec: |
      $ch("mcp::state").create()
      $ch("mcp::state").set("sessions", {})

  # Stateful tool
  - name: Session Tool
    check:
      in:
        action: isString.oneOf(["create", "get", "delete"])
        sessionId: isString.default(__)
    exec: |
      var sessions = $ch("mcp::state").get("sessions") || {}

      switch(args.action) {
        case "create":
          var id = sha1(new Date().getTime())
          sessions[id] = { created: nowUTC(), data: {} }
          $ch("mcp::state").set("sessions", sessions)
          args.result = {
            content: [{ type: "text", text: "Session created: " + id }]
          }
          break

        case "get":
          var session = sessions[args.sessionId]
          args.result = {
            content: [{
              type: "text",
              text: session ? stringify(session) : "Session not found"
            }]
          }
          break

        case "delete":
          delete sessions[args.sessionId]
          $ch("mcp::state").set("sessions", sessions)
          args.result = {
            content: [{ type: "text", text: "Session deleted" }]
          }
          break
      }
```

### Multi-Tool Coordination

```yaml
jobs:
  # Tool 1: Data fetcher
  - name: Fetch Data
    check:
      in:
        source: isString
    exec: |
      var data = $rest().get(args.source).getResponse().data

      // Store for other tools
      $ch("mcp::shared").set("lastFetch", {
        data: data,
        timestamp: nowUTC()
      })

      args.result = {
        content: [{ type: "text", text: "Data fetched successfully" }]
      }

  # Tool 2: Data analyzer (uses Tool 1 data)
  - name: Analyze Data
    exec: |
      var lastFetch = $ch("mcp::shared").get("lastFetch")

      if (!lastFetch) {
        args.result = {
          content: [{ type: "text", text: "No data available. Fetch first." }],
          isError: true
        }
        return
      }

      var analysis = $from(lastFetch.data)
        .groupBy("category")
        .select(g => ({
          category: g.key,
          count: g.items.length,
          total: $from(g.items).sum("value")
        }))

      args.result = {
        content: [{
          type: "text",
          text: "Analysis:\n" + af.toYAML(analysis)
        }]
      }

  # Initialize shared channel
  - name: Init Shared
    exec: |
      $ch("mcp::shared").create()
```

---

## Security Considerations

### Input Validation

Always validate tool inputs:

```yaml
jobs:
  - name: Secure File Access
    check:
      in:
        path: isString
    exec: |
      // Prevent path traversal
      var safePath = args.path.replace(/\.\./g, "")

      // Restrict to allowed directories
      var allowedDirs = ["/data", "/public"]
      var isAllowed = allowedDirs.some(dir =>
        safePath.startsWith(dir)
      )

      if (!isAllowed) {
        args.result = {
          content: [{ type: "text", text: "Access denied" }],
          isError: true
        }
        return
      }

      // Safe to proceed
      args.result = {
        content: [{ type: "text", text: io.readFileString(safePath) }]
      }
```

### Authentication

```yaml
jobs:
  - name: Authenticated MCP Server
    deps:
      - HTTP Start Server
    exec: |
      var fns = {}

      fns["/mcp"] = req => {
        // Check authentication header
        var authHeader = req.header["authorization"]
        var expectedToken = getEnv("MCP_AUTH_TOKEN")

        if (authHeader != "Bearer " + expectedToken) {
          return ow.server.httpd.reply("Unauthorized", 401, {})
        }

        // Proceed with normal MCP handling
        return ow.server.httpd.replyJSONRPC(
          global.__ojobHttp[args.port],
          req,
          args.handlers
        )
      }

      $ch("__oJobHTTPd::fns::" + args.port).setAll(["uri"], fns)
```

### Rate Limiting

```yaml
jobs:
  - name: Rate Limited Tool
    exec: |
      $ch("mcp::ratelimit").create()

      var clientId = args.__client || "unknown"
      var limit = $ch("mcp::ratelimit").get(clientId) || { count: 0, reset: 0 }

      var now = nowUTC()
      if (now > limit.reset) {
        limit = { count: 0, reset: now + 60000 } // 1 minute window
      }

      limit.count++

      if (limit.count > 10) {
        args.result = {
          content: [{ type: "text", text: "Rate limit exceeded" }],
          isError: true
        }
        return
      }

      $ch("mcp::ratelimit").set(clientId, limit)

      // Proceed with tool logic
```

---

## Testing MCP Servers

### Manual Testing with curl

```bash
# Initialize connection
curl -X POST http://localhost:3000/mcp \
  -H "Content-Type: application/json" \
  -d '{
    "jsonrpc": "2.0",
    "method": "initialize",
    "params": {
      "protocolVersion": "2024-11-05",
      "clientInfo": { "name": "test-client" }
    },
    "id": 1
  }'

# Call a tool
curl -X POST http://localhost:3000/mcp \
  -H "Content-Type: application/json" \
  -d '{
    "jsonrpc": "2.0",
    "method": "tools/call",
    "params": {
      "name": "read_file",
      "arguments": { "path": "/data/test.txt" }
    },
    "id": 2
  }'
```

### Automated Testing

```yaml
include:
  - oJobTest.yaml

jobs:
  - name: Test MCP Tool
    exec: |
      ow.loadObj()

      // Call the initialize method
      var initResp = $rest()
        .post("http://localhost:3000/mcp", {
          jsonrpc: "2.0",
          method: "initialize",
          params: { protocolVersion: "2024-11-05" },
          id: 1
        })
        .getResponse()

      ow.test.assert(initResp.status, 200, "Initialize failed")

      // Call a tool
      var toolResp = $rest()
        .post("http://localhost:3000/mcp", {
          jsonrpc: "2.0",
          method: "tools/call",
          params: {
            name: "test_tool",
            arguments: { input: "test" }
          },
          id: 2
        })
        .getResponse()

      ow.test.assert(toolResp.status, 200, "Tool call failed")
      ow.test.assert(toolResp.data.result.content[0].text, "expected output", "Wrong output")

todo:
  - (test): Test MCP Tool
    ((job)): Test MCP Tool
  - (testGenMD): __
    ((file)): test-results.md
```

---

## Performance Optimization

### Caching Tool Results

```yaml
jobs:
  - name: Cached API Tool
    exec: |
      $ch("mcp::cache").create()

      var cacheKey = sha1(stringify(args))
      var cached = $ch("mcp::cache").get(cacheKey)

      if (cached && (nowUTC() - cached.timestamp < 300000)) {
        // Cache hit, less than 5 minutes old
        args.result = cached.result
        return
      }

      // Cache miss, fetch data
      var data = $rest().get(args.url).getResponse().data

      var result = {
        content: [{ type: "text", text: stringify(data) }]
      }

      $ch("mcp::cache").set(cacheKey, {
        result: result,
        timestamp: nowUTC()
      })

      args.result = result
```

### Parallel Tool Execution

```yaml
jobs:
  - name: Batch Processing Tool
    check:
      in:
        items: isArray
    exec: |
      ow.loadObj()

      var results = $do(() => {
        return args.items.map(item => {
          return $do(() => processItem(item))
        })
      }).map(p => p.catch(e => ({ error: e.message })))

      args.result = {
        content: [{
          type: "text",
          text: af.toYAML(results)
        }]
      }
```

---

## Debugging

### Enable Debug Logging

```yaml
jobs:
  - name: Debug MCP Server
    to: HTTP MCP Server
    args:
      port: 3000
      debug: true  # Enables detailed logging
      fns:
        # ... your tools
```

### Custom Logging

```yaml
jobs:
  - name: Logged Tool
    exec: |
      log("Tool called with args: " + stringify(args))

      try {
        // Tool logic
        var result = doSomething(args.input)

        log("Tool succeeded with result: " + stringify(result))

        args.result = {
          content: [{ type: "text", text: stringify(result) }]
        }
      } catch(e) {
        logErr("Tool failed: " + e.message)
        $err(e)

        args.result = {
          content: [{ type: "text", text: "Error: " + e.message }],
          isError: true
        }
      }
```

---

## See Also

- [Building an MCP Server](build-mcp-server.md)
- [Using oJob.io MCPs with VS Code](../ojobio/use-ojob-io-mcps-with-vscode.md)
- [oJob Reference](../../concepts/oJob.html)
- [ow.server Reference](../../reference/ow_server.md)
