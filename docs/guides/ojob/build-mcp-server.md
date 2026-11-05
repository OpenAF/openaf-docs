---
layout: default
title: Build MCP servers with oJob
parent: oJob
grand_parent: Guides
---

# Build Model Context Protocol servers

OpenAF can expose [Model Context Protocol](https://modelcontextprotocol.io/) tools through regular oJobs. The [mini-a MCP examples](https://github.com/OpenAF/mini-a/tree/main/mcps) are maintained separately. The shared server runtime is supplied by the oJob-common oPack as `oJobMCP.yaml`. This guide distils the key pieces so you can author your own MCP server and test it locally or over HTTP.

## Understand the shared MCP runtime

`oJob-common/oJobMCP.yaml` publishes two shortcuts that do most of the heavy lifting:

- `httpdMCP` starts an HTTP JSON-RPC endpoint (defaults to `/mcp`) and wires requests to jobs you expose.
- `stdioMCP` speaks MCP over STDIO, allowing you to run the server as a child process.

Both variants expect:

- `description.serverInfo` with `name`, `title` and `version`.
- `fnsMeta`: MCP tool metadata (JSON Schema, annotations, etc.).
- `fns`: the mapping between MCP tool names and oJob job names.

Your YAML file only needs to prepare these maps and include the shortcut.

## Start from the MCP skeleton

Install `oJob-common` with `opack install oJob-common`. Create `mcp-myservice.yaml` in your working directory. This example calls the underlying named jobs so the CLI port can be converted to a number explicitly. If you use the `(httpdMCP)` shortcut instead, its value is the numeric port and `((description))` is the server metadata:

```yaml
# Author: You
help:
  text   : A STDIO/HTTP MCP server for MyService
  expects:
  - name     : onport
    desc     : If defined starts an HTTP MCP server on the provided port
    example  : "8888"
    mandatory: false
  - name     : myConfig
    desc     : Example extra parameter
    example  : "value"
    mandatory: true

init:
  mcp:
    description:
      serverInfo:
        name: myservice
        title: OpenAF MCP MyService
        version: 1.0.0
    fnsMeta:
      myservice-tool:
        name: myservice-tool
        description: Performs the main operation
        inputSchema:
          type: object
          properties:
            param1:
              type: string
              description: Example parameter
          required: [param1]
        annotations:
          title: MyService Tool
          readOnlyHint: true
          idempotentHint: true
    fns:
      myservice-tool: MyService Tool

todo:
- Init MyService
- Start MCP

ojob:
  opacks:
  - openaf     : 20261030
  - oJob-common: 20261030
  daemon      : true
  sequential  : true
  catch       : printErr(String(exception))
  argsFromEnvs: true
  logToConsole: false

include:
- oJobMCP.yaml

jobs:
- name : Init MyService
  check:
    in:
      myConfig: isString
  exec : | #js
    // Initialise SDK clients, cache credentials, etc.
    global.myServiceConfig = args

- name: Start MCP
  exec: |
    var config = clone(args.init.mcp);
    if (isDef(args.onport)) {
      config.port = _$(args.onport, "onport").toNumber()
        .check(v => isNumber(v) && Math.floor(v) === v && v >= 1 && v <= 65535).$_();
      $job("HTTP Start Server", config, "myservice-http");
      $job("HTTP MCP Server", config, "myservice-http");
    } else {
      $job("STDIO MCP Server", config);
    }

- name : MyService Tool
  check:
    in:
      param1: isString
  exec : | #js
    if (!isDef(global.myServiceConfig)) return { _err: "Service not initialised" }
    return { message: `Processed ${args.param1}` }


- name : Cleanup MyService
  type : shutdown
  exec : | #js
    delete global.myServiceConfig
```

Key points:

- Keep the `help` section up to date so users know which arguments are required.
- The `todo` block initializes the service and calls `Start MCP`, which chooses HTTP or STDIO using `onport`.
- `fnsMeta` entries must describe your tools with valid JSON Schema; `fns` maps the tool names to the job that should run.
- Always add a shutdown job for cleanup — it runs when the MCP exits.

## Tips for implementing tools

- Return a map with `_err` for an explicit tool failure, or throw an error. A string beginning with `[ERROR]` is ordinary text unless your client adds its own convention.
- Use `check.in` validations so bad inputs fail fast.
- For read/write operations, consider a flag (e.g. `allowWrite`) to prevent accidental changes, similar to `mcp-ssh.yaml`.
- Inspect other MCPs (database, time, SSH, etc.) in `mini-a/mcps/` for real-world patterns.

## Smoke-test the server with oJob

Run in STDIO mode during development:

```bash
ojob mcp-myservice.yaml myConfig=value
```

Run as an HTTP server:

```bash
ojob mcp-myservice.yaml onport=12345 myConfig=value
```

Both rely on the named jobs from `oJob-common/oJobMCP.yaml`. If you need extra HTTP middleware, add it before the `httpdMCP` call.

## Test with `$mcp` inside OpenAF

`openaf/js/openaf.js` ships the `$mcp` client helper. You can use it from the REPL or inside your scripts:

```javascript
var client = $mcp({
  cmd   : "ojob mcp-myservice.yaml myConfig=value",
  debug : false,
  strict: true
})

client.initialize()

log(client.listTools()) // -> { tools: [...] }

var result = client.callTool("myservice-tool", { param1: "demo" })
log(result)

client.destroy()
```

For HTTP mode, switch to `type: "remote"` and provide `url: "http://localhost:12345/mcp"`.

## Test with `oafp in=mcp`

`oafp` can act as a CLI MCP client (see `oafp/src/docs/USAGE.md`):

- List tools exposed by your STDIO server:

  ```bash
  oafp in=mcp inmcptoolslist=true data="(cmd: 'ojob mcp-myservice.yaml myConfig=value')"
  ```

- Invoke a tool via STDIO:

  ```bash
  oafp in=mcp data="(cmd: 'ojob mcp-myservice.yaml myConfig=value', tool: 'myservice-tool', params: (param1: 'demo'))"
  ```

- Invoke the same tool over HTTP:

  ```bash
  oafp in=mcp data="(type: remote, url: 'http://localhost:12345/mcp', tool: 'myservice-tool', params: (param1: 'demo'))"
  ```

Set `inmcplistprompts=true` to inspect available prompts (if you expose any) or use the other connection fields (`__timeout__`, `__clientInfo__`, …) listed in the `oafp` usage document.

## Tool blacklist

You can prevent specific tools from being accessible to callers by providing a `blacklist` array in the MCP client options:

```javascript
var client = $mcp({
  cmd      : "ojob mcp-myservice.yaml myConfig=value",
  blacklist: ["dangerous-tool", "internal-only-tool"]
})
client.initialize()
// "dangerous-tool" will not appear in listTools() or be callable
```

The blacklist is applied at the client side — listed tool names are filtered out from `listTools` responses and calls to them are blocked before being forwarded to the server.

## Dummy mode and oJob-based servers

`$mcp` and `$jsonrpc` support two additional server types for testing and oJob integration:

### Dummy mode

A dummy server returns empty/no-op responses to all tool calls. Useful for integration testing:

```javascript
var client = $mcp({ type: "dummy" })
client.initialize()
// all tool calls return empty results — no real process is spawned
```

### oJob-based servers

Point `$mcp` directly at an oJob YAML file as the server:

```javascript
var client = $mcp({
  type  : "ojob",
  ojob  : "mcp-myservice.yaml",
  args  : { myConfig: "value" }
})
client.initialize()
```

A default command directory can also be set so relative process paths resolve correctly:

```javascript
var client = $mcp({
  cmd    : "ojob mcp-myservice.yaml myConfig=value",
  cmdDir : "/path/to/mcps"
})
```

## Per-call options

Both `$jsonrpc` and `$mcp` accept optional per-call options to override tool execution parameters on individual calls:

```javascript
var result = client.callTool("myservice-tool", { param1: "demo" }, {
  timeout: 30000   // override timeout for this call only
})
```

## TOON output format

TOON is a structured-data notation. Use the `toon` output format to encode a value as text:

```javascript
$output(myData, { __format: "toon" })
```

For the HTTP server, a returned map with a `text` string becomes the MCP text content:

```javascript
return { text: af.toTOON(myData) };
```

## Server info with getInfo

Both JSON-RPC and MCP client objects expose a `getInfo()` method to retrieve server metadata after initialisation:

```javascript
var client = $mcp({ cmd: "ojob mcp-myservice.yaml myConfig=value" })
client.initialize()

var info = client.getInfo()
log(info)   // -> { name: "mini-a-myservice", version: "1.0.0", ... }
```

## Ping support (stdio)

The MCP stdio server now handles `ping` requests automatically, returning the expected `pong` response for liveness checks. No additional configuration is required.

## Where to go next

- Browse the [mini-a MCP catalog](https://github.com/OpenAF/mini-a/tree/main/mcps) for inspiration.
- Use the [advanced MCP guide](mcp-server-advanced.md) for input validation, state and testing.
- Consult the [oJob-common source reference](ojob-common-reference.md) for shared server options.

## October protocol and authentication additions

The [server API reference](../../reference/ow_server.md) documents shared protocol helpers, stdio serving, and HTTP replies. Modern stateless protocol support is negotiated explicitly by clients; see [`$mcp`](../../reference/scope.md#mcp). For delegated client login, use the [localhost OAuth guide](../advanced/mcp-oauth.md).

## HTTP authentication and tool exposure

In the [pinned oJob-common source](ojob-common-reference.md), HTTP authentication is **opt-in**. Set `OJOB_MCP_AUTH_TOKEN` in the server environment or supply `((authtoken))` to require a bearer token. Without a configured token or external validation service, the endpoint accepts unauthenticated requests.

`((authapiurl))` delegates validation to an HTTP service and takes precedence over `authtoken`. It forwards the incoming authentication header and MCP context headers. A 2xx response accepts the credential; other statuses, errors and timeouts reject it. The default timeout is 5,000 ms. The validation cache is disabled by default (`authapicachettl=0`); when enabled its default maximum is 1,000 entries (`authapicachemax`). See the [MCPAuthd guide](../opacks/mcpauthd.md) for a companion service.

Expose each tool in both `fns` and `fnsMeta`. Clients cannot select arbitrary oJob names by passing a tool name. HTTP tool arguments include `_httprequest` with the authentication header scrubbed. Treat tool input as untrusted and validate its domain-specific values inside the job.

`toolPrefix` changes exposed names while keeping the original map keys. `tplDesc=true` expands description templates using server arguments. `modern=true` opts into the additional protocol era implemented by this source revision; legacy behavior remains the default. `audit=true` logs tool arguments, so enable it with an appropriate data-retention policy.

## Tool result conversion

The skeleton returns `{ message: "Processed demo" }`. Both transports encode that map as JSON text inside MCP `result.content[0].text` by default. Parse that text to recover the map. Server flags can select TOON instead of JSON.

The HTTP job additionally recognizes a returned `text` string field and unwraps a returned `result` field as a prepared MCP result. The STDIO job in this oJob-common snapshot does not enable the core `rawToolResults` option, so returning an MCP `content` envelope from a tool serializes that envelope as data. See [advanced response patterns](mcp-server-advanced.md#tool-response-format).
