---
layout: default
title: Advanced MCP Server Patterns
parent: oJob
grand_parent: Guides
---

<!-- Preserve earlier section bookmarks. -->
<a id="table-of-contents"></a>
<a id="example-file-reader-tool"></a>


# Advanced MCP Server Patterns

Use the complete [MCP server skeleton](build-mcp-server.md) before adding these patterns. The server implementation is `oJobMCP.yaml` in the [pinned oJob-common snapshot](ojob-common-reference.md).

## Prerequisites

Install `oJob-common`, use an OpenAF runtime matching the [source baseline](../../source-snapshot.md), and start with a tool that needs no external service. Add optional drivers or packages only when the tool requires them.

## MCP Server Architecture

### Core Components

| Component | Contract |
| --- | --- |
| `httpdMCP` | Shortcut value is a numeric port; metadata is `((description))` |
| `stdioMCP` | Shortcut value is the server description |
| `fns` | Tool name to oJob job name mapping |
| `fnsMeta` | Metadata and input schema for each tool |
| Tool job | Validates its input and returns a result |

### Key Arguments

Both transports support tool metadata, namespacing through `toolPrefix`, and description templates through `tplDesc`. HTTP additionally supports URI, stream replies and authentication. See the [full argument reference](ojob-common-reference.md) for defaults and environment variable names.

## Implementing Custom Tools

### Basic Tool Structure

Return the business result explicitly from `exec`, and account for the transport conversion below. A plain result map gives consistent JSON-text content on both transports by default.

```yaml
jobs:
- name: Add two numbers
  check:
    in:
      a: 'check(v => isNumber(v) && isFinite(v))'
      b: 'check(v => isNumber(v) && isFinite(v))'
  exec: |
    return { sum: args.a + args.b };
```

Expose this job as a key in both `fns` and `fnsMeta`; the schema should require numeric `a` and `b`. Validate again inside the job because the schema describes the tool's input contract, while the job enforces its requirements.

### Tool Response Format

The pinned transports have different conversion rules:

| Returned job value | HTTP MCP job | STDIO MCP job |
| --- | --- | --- |
| Plain map | JSON (or configured TOON) in text content | JSON (or configured TOON) in text content |
| `{ text: "message" }` | Uses `message` as text content | Serializes the map as text content |
| `{ result: { content: [...] } }` | Unwraps the prepared MCP result | Serializes the map as text content |
| `{ _err: "message" }` | Converts to an error result | Throws into the core error-result handler |

For the HTTP job, setting `args.result` is another way to supply a prepared result through the returned job arguments. Returning a bare successful `content` envelope is serialized as data rather than passed through. The core `ow.server.mcpStdio` supports `rawToolResults`, but this oJob-common STDIO wrapper does not enable it.

```javascript
return { message: "Operation completed" };
```

Clients receive this map encoded in `content[0].text`. For a tool failure shared by both transports, return `{ _err: "Invalid identifier" }`. Do not infer failure from an `[ERROR]` prefix in ordinary text.

## Advanced Tool Patterns

### Multi-Step Tool Execution

Call a named job with `$job` and consume its returned value:

```yaml
jobs:
- name: Normalize input
  exec: |
    return { text: String(args.text).trim() };
- name: Normalize tool
  check:
    in:
      text: isString
  exec: |
    var normalized = $job("Normalize input", { text: args.text });
    return { message: normalized.text };
```

Pass only the fields needed by the child job. HTTP tool calls may receive `_httprequest`; do not accidentally forward it to an unrelated API.

### Error Handling

```yaml
jobs:
- name: Validate identifier
  exec: |
    if (!isString(args.id) || !/^[a-zA-Z0-9_-]+$/.test(args.id)) {
      return { _err: "Invalid identifier" };
    }
    return { identifier: args.id };
```

### Tools with External API Calls

`$rest().get()` returns a decoded body. Configure query parameters through the helper's options and second argument; there is no `.query(...).getResponse()` chain on the decoded result.

```javascript
var weather = $rest({ uriQuery: true, throwExceptions: true, timeout: 5000 })
  .get("https://api.example.com/weather", { city: args.city });
return { weather: weather };
```

The endpoint is a placeholder. Keep service credentials in server configuration, validate the accepted city or identifier, and handle provider-specific failures. If callers select URLs, enforce the server's permitted destinations before making a request.

## JSON-RPC Protocol Handling

### Understanding the Protocol Flow

Use `$mcp` for initialization, tool discovery and calls rather than hand-building incomplete JSON-RPC exchanges. The default server behavior supports its legacy handshake. `modern=true` explicitly enables the additional protocol era implemented in this snapshot. See [the server reference](../../reference/ow_server.md) for the exact request and response handling.

### Custom Protocol Extensions

Prefer documented metadata and tool options. Adding arbitrary properties to a response does not establish client support for an extension. Keep compatibility tests for each client and protocol version you deploy.

## Integration Patterns

### Database-Backed Tools

Install the matching [JDBC driver](../opacks/jdbc-drivers.md), use bound parameters for caller-supplied values, and close each connection in `finally` unless a deliberate pool owns it. The [JDBC URL policy](../advanced/jdbc-url-policy.md) also applies to tool-created connections. A read-only annotation describes a tool; the query implementation must enforce read-only behavior.

### Channel-Based State Management

Create shared channels during server initialization and destroy them during shutdown, not on each call. Use stable structured keys and avoid storing incoming HTTP request objects as state.

```yaml
jobs:
- name: Init tool state
  exec: |
    $ch("tool-state").create();
- name: Increment tool counter
  exec: |
    var count = syncFn(() => {
      var previous = $ch("tool-state").get({ id: "calls" });
      var next = isDef(previous) ? previous.value + 1 : 1;
      $ch("tool-state").set({ id: "calls" }, { value: next });
      return next;
    }, "tool-state-counter");
    return { count: count };
- name: Close tool state
  type: shutdown
  exec: |
    $ch("tool-state").destroy();
```

Add `Init tool state` before the server shortcut in `todo`. `syncFn` forwards the callback result; `sync` does not. This lock coordinates threads in this JVM, not independent server processes.

### Multi-Tool Coordination

Use server-side jobs for shared logic and keep each exposed tool's input/output contract independent. Do not invoke a tool by accepting arbitrary job names from its caller: the `fns`/`fnsMeta` maps define the exposed set.

## Security Considerations

### Input Validation

Use one complete predicate for compound constraints; see [validation compatibility](../medium/parameter-validation.md#snapshot-compatibility). The server rejects prototype-manipulating argument keys, but application-level checks still belong to the tool.

### Authentication

HTTP authentication is opt-in. Configure `authtoken` / `OJOB_MCP_AUTH_TOKEN`, or use `authapiurl` for delegated validation. Delegated validation takes precedence over a static token and accepts only 2xx responses. Errors and timeouts reject the request. See [authentication details](build-mcp-server.md#http-authentication-and-tool-exposure) and [MCPAuthd](../opacks/mcpauthd.md).

### Rate Limiting

This module does not promise a general per-client rate limiter. Enforce request limits in your HTTP gateway or an explicitly tested server policy. The delegated-auth cache bounds validation results; it is not a request-rate limit.

## Testing MCP Servers

### Manual Testing with curl

For protocol-aware testing, prefer the following `$mcp` client. Low-level HTTP tests need the exact headers, request sequence and transport behavior of the selected protocol mode; a successful HTTP status alone does not establish a successful tool result.

### Automated Testing

Run the [skeleton](build-mcp-server.md) on port 12345, then execute:

```javascript
ow.loadTest();
var client = $mcp({ type: "remote", url: "http://localhost:12345/mcp" });
try {
  client.initialize();
  var tools = client.listTools();
  ow.test.assert(tools.tools.some(t => t.name === "myservice-tool"), true, "tool listed");
  var result = client.callTool("myservice-tool", { param1: "demo" });
  ow.test.assert(jsonParse(result.content[0].text).message, "Processed demo", "tool result");
} finally {
  client.destroy();
}
```

Adapt client authentication when the server requires it. Also test missing or invalid arguments, unknown tool names, failed authentication and provider timeouts in a local fixture. Keep STDIO stdout reserved for protocol output; use stderr for diagnostics.

## Performance Optimization

### Caching Tool Results

Create the cache once. Key it from validated business inputs and any tenant/auth scope that changes the result. Define a maximum entry count and expiration policy; a channel does not automatically turn a timestamp field into TTL eviction. Avoid caching failures indefinitely.

### Parallel Tool Execution

Parallelize only independent work and protect shared state explicitly. Set transport/provider timeouts and ensure cleanup when one task fails. See [authoring concurrency recipes](authoring-recipes.md) for the supported asynchronous primitives.

## Debugging

### Enable Debug Logging

Use `debug=true` only in a suitable diagnostic environment. `audit=true` logs tool names and arguments; it is disabled by default. HTTP client IPs are best-effort proxy-header values, not direct socket addresses.

### Custom Logging

Keep diagnostics separate from tool results. For STDIO servers, write diagnostics to stderr and keep `logToConsole: false` as in the skeleton. Avoid logging credentials or full incoming request maps.

## See Also

- [Build MCP servers](build-mcp-server.md)
- [oJob-common reference](ojob-common-reference.md)
- [MCP OAuth](../advanced/mcp-oauth.md)
- [Source-generated server API](../../reference/ow_server.md)
