---
layout: default
title: Build MCP servers with oJob
parent: oJob
grand_parent: Guides
---

# Build Model Context Protocol servers

OpenAF can expose [Model Context Protocol](https://modelcontextprotocol.io/) tools through regular oJobs. The `https://github.com/openaf/mini-a/mcps` directory in the distribution contains working examples (`mcp-db.yaml`, `mcp-ch.yaml`, …) and the shared runtime lives in `https://github.com/openaf/oJob-common/oJobMCP.yaml`. This guide distils the key pieces so you can author your own MCP server and test it locally or over HTTP.

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

Create a new file under `mini-a/mcps/`, e.g. `mcp-myservice.yaml`, following the structure below (adapted from `mini-a/mcps/CREATING.md`):

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

todo:
- Init MyService
- (if    ): "isDef(args.onport)"
  ((then)):
  - (httpdMCP): &MCPSERVER
      description:
        serverInfo:
          name   : mini-a-myservice
          title  : OpenAF MCP MyService
          version: 1.0.0
    ((fnsMeta)): &MCPFNSMETA
      myservice-tool:
        name       : myservice-tool
        description: Performs the main operation
        inputSchema:
          type      : object
          properties:
            param1:
              type       : string
              description: Example parameter
          required: [ param1 ]
        annotations:
          title         : MyService Tool
          readOnlyHint  : true
          idempotentHint: true
    ((fns    )): &MCPFNS
      myservice-tool: MyService Tool
  ((else)):
  - (stdioMCP): *MCPSERVER
    ((fnsMeta)): *MCPFNSMETA
    ((fns    )): *MCPFNS

ojob:
  opacks:
  - openaf     : 20250915
  - oJob-common: 20250914
  daemon      : true
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

- name : MyService Tool
  check:
    in:
      param1: isString
  exec : | #js
    if (!isDef(global.myServiceConfig)) return "[ERROR] Service not initialised"
    return {
      content: [{
        type: "text",
        text: `Processed ${args.param1}`
      }]
    }

- name : Cleanup MyService
  type : shutdown
  exec : | #js
    delete global.myServiceConfig
```

Key points:

- Keep the `help` section up to date so users know which arguments are required.
- The `todo` block first runs any initialisation job(s) and then chooses between HTTP or STDIO mode using the `onport` argument.
- `fnsMeta` entries must describe your tools with valid JSON Schema; `fns` maps the tool names to the job that should run.
- Always add a shutdown job for cleanup — it runs when the MCP exits.

## Tips for implementing tools

- Return errors as strings that start with `[ERROR] …`. The existing MCP tooling looks for that pattern.
- Use `check.in` validations so bad inputs fail fast.
- For read/write operations, consider a flag (e.g. `allowWrite`) to prevent accidental changes, similar to `mcp-ssh.yaml`.
- Inspect other MCPs (database, time, SSH, etc.) in `mini-a/mcps/` for real-world patterns.

## Smoke-test the server with oJob

Run in STDIO mode during development:

```bash
ojob mcps/mcp-myservice.yaml myConfig=value
```

Run as an HTTP server:

```bash
ojob mcps/mcp-myservice.yaml onport=12345 myConfig=value
```

Both rely on the shortcuts from `oJob-common/oJobMCP.yaml`. If you need extra HTTP middleware, add it before the `httpdMCP` call.

## Test with `$mcp` inside OpenAF

`openaf/js/openaf.js` ships the `$mcp` client helper. You can use it from the REPL or inside your scripts:

```javascript
var client = $mcp({
  cmd   : "ojob mcps/mcp-myservice.yaml myConfig=value",
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
  oafp in=mcp inmcptoolslist=true data="(cmd: 'ojob mcps/mcp-myservice.yaml myConfig=value')"
  ```

- Invoke a tool via STDIO:

  ```bash
  oafp in=mcp data="(cmd: 'ojob mcps/mcp-myservice.yaml myConfig=value', tool: 'myservice-tool', params: (param1: 'demo'))"
  ```

- Invoke the same tool over HTTP:

  ```bash
  oafp in=mcp data="(type: remote, url: 'http://localhost:12345/mcp', tool: 'myservice-tool', params: (param1: 'demo'))"
  ```

Set `inmcplistprompts=true` to inspect available prompts (if you expose any) or use the other connection fields (`__timeout__`, `__clientInfo__`, …) listed in the `oafp` usage document.

## Where to go next

- Browse the catalog in `https://github.com/openaf/mini-a/mcps/README.md` for inspiration.
- Revisit `https://github.com/openaf/mini-a/mcps/CREATING.md` whenever you need the full checklist.
- Extend `https://github.com/openaf/oJob-common/oJobMCP.yaml` if you need new shared behaviours (additional logging, authentication, etc.).

