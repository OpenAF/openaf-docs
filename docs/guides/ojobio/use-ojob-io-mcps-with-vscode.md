---
layout: default
title: Use ojob.io MCP servers with VS Code
parent: oJobIO
grand_parent: Guides
nav_order: 25
---

# Use ojob.io MCP servers with VS Code

The `ojob.io/ai/mcps/*.yaml` catalogue ships ready-to-run [Model Context Protocol](https://modelcontextprotocol.io/) servers that expose OpenAF capabilities over STDIO or HTTP. This guide shows how to launch them from Docker and wire them into Visual Studio Code so they can power the GitHub Copilot Agent experience.

## Prerequisites

- Docker 24+ with access to pull `openaf/ojobc:edge-t8`.
- Visual Studio Code 1.90+ with the GitHub Copilot Agent feature flag.
- A working `mcp.json` (macOS: `~/Library/Application Support/Code/User/mcp.json`, Linux: `~/.config/Code/User/mcp.json`, Windows: `%APPDATA%\Code\User\mcp.json`).

## Launch the servers over STDIO

Each MCP is distributed as a remote oJob. The runtime container understands the `OJOB` environment variable and keeps STDIO open so VS Code can speak JSON-RPC directly:

```bash
docker run -i --pull always \
  -e OJOB=ojob.io/ai/mcps/mcp-weather \
  openaf/ojobc:edge-t8
```

- Keep `-i` (interactive) — removing it will close STDIO and Copilot will disconnect.
- Supply extra configuration as additional `-e key=value` pairs. Most servers default to read-only unless you opt in with the relevant flag (`readwrite`, `rw`, etc.).
- Add `-e onport=8080` if you prefer HTTP; the same compose file will start an HTTP `/mcp` endpoint while keeping STDIO usable.

## Docker one-liners for every ojob.io MCP

- **mcp-ch** – expose OpenAF data channels.
  ```bash
  docker run -i --pull always \
    -v /mydata:/data \
    -e OJOB=ojob.io/ai/mcps/mcp-ch \
    -e chs="(_name: mydata, _type: file, _rw: true, file: /data/data.json)" \
    openaf/ojobc:edge-t8
  ```
  Use SLON syntax in `chs` to describe the channels you need (file, simple, mvs, ...).

- **mcp-db** – connect to JDBC databases (read-only by default).
  ```bash
  docker run -i --pull always \
    -e OJOB=ojob.io/ai/mcps/mcp-db \
    -e jdbc=jdbc:postgresql://hh-pgsql-public.ebi.ac.uk:5432/pfmegrnargs \
    -e user=reader \
    -e pass=NWDMCE5xdipIjRrp \
    openaf/ojobc:edge-t8
  ```
  Add `-e rw=true` to allow data-changing statements.

- **mcp-email** – send email through SMTP.
  ```bash
  docker run -i --pull always \
    -e OJOB=ojob.io/ai/mcps/mcp-email \
    -e smtpserver=smtp.gmail.com \
    -e from=sender@example.com \
    -e user=sender@example.com \
    -e pass=yourAppPassword \
    -e tls=true \
    openaf/ojobc:edge-t8
  ```

- **mcp-kube** – explore Kubernetes clusters (read-only unless `readwrite=true`).
  ```bash
  docker run -i --pull always \
    -e OJOB=ojob.io/ai/mcps/mcp-kube \
    -e url=https://my-k8s.example.com:6443 \
    -e token=$K8S_TOKEN \
    -e namespace=default \
    openaf/ojobc:edge-t8
  ```
  You can swap `token` for `user`/`pass` credentials depending on your cluster.

- **mcp-net** – DNS lookups and TCP checks.
  ```bash
  docker run -i --pull always \
    -e OJOB=ojob.io/ai/mcps/mcp-net \
    openaf/ojobc:edge-t8
  ```

- **mcp-oaf** – query OpenAF, oJob and oAFp documentation.
  ```bash
  docker run -i --pull always \
    -e OJOB=ojob.io/ai/mcps/mcp-oaf \
    openaf/ojobc:edge-t8
  ```

- **mcp-oafp** – execute oafp pipelines or inspect their docs.
  ```bash
  docker run -i --pull always \
    -e OJOB=ojob.io/ai/mcps/mcp-oafp \
    -e libs=minia \
    openaf/ojobc:edge-t8
  ```
  Use `params` (SLON map) to provide default parameters for repeated runs.

- **mcp-s3** – browse S3-compatible object storage.
  ```bash
  docker run -i --pull always \
    -e OJOB=ojob.io/ai/mcps/mcp-s3 \
    -e accessKey=AKIA... \
    -e secret=superSecretKey \
    -e region=eu-west-1 \
    -e bucket=my-bucket \
    openaf/ojobc:edge-t8
  ```
  Add `-e readwrite=true` only when you want to create, upload or delete objects.

- **mcp-shell** – carefully expose a local shell.
  ```bash
  docker run -i --pull always \
    -e OJOB=ojob.io/ai/mcps/mcp-shell \
    -e readwrite=false \
    -e shellallow=ls,cat \
    openaf/ojobc:edge-t8
  ```
  Tighten `shellallow`/`shellbanextra`, set `cwd`, and use `timeout` to avoid surprises.

- **mcp-ssh** – run shell commands on remote hosts through OpenAF SSH URLs.
  ```bash
  docker run -i --pull always \
    -e OJOB=ojob.io/ai/mcps/mcp-ssh \
    -e "ssh=ssh://user:pass@host:22/?timeout=5000" \
    openaf/ojobc:edge-t8
  ```
  As with `mcp-shell`, keep `readwrite` off unless you truly need to push changes.

- **mcp-time** – date and timezone utilities.
  ```bash
  docker run -i --pull always \
    -e OJOB=ojob.io/ai/mcps/mcp-time \
    openaf/ojobc:edge-t8
  ```

- **mcp-weather** – wttr.in-backed weather summaries.
  ```bash
  docker run -i --pull always \
    -e OJOB=ojob.io/ai/mcps/mcp-weather \
    openaf/ojobc:edge-t8
  ```
  Optional knobs: `ansi=true`, `oneline=true`, or custom `format`/`options`.

## Wire everything into GitHub Copilot Agent mode

1. Open (or create) your `mcp.json`.
2. Define each server under `mcpServers`, pointing to the Docker command above. Use the `env` block to keep secrets out of the command line.
3. Group the servers so Copilot Agent can surface them as a single capability.
4. Attach that group to the Copilot client entry.

```json
{
  "mcpServers": {
    "openaf-weather": {
      "command": "docker",
      "args": [
        "run", "-i", "--pull", "always",
        "-e", "OJOB=ojob.io/ai/mcps/mcp-weather",
        "openaf/ojobc:edge-t8"
      ],
      "transport": "stdio"
    },
    "openaf-db": {
      "command": "docker",
      "args": [
        "run", "-i", "--pull", "always",
        "-e", "OJOB=ojob.io/ai/mcps/mcp-db",
        "-e", "rw=false",
        "openaf/ojobc:edge-t8"
      ],
      "transport": "stdio",
      "env": {
        "jdbc": "jdbc:postgresql://hh-pgsql-public.ebi.ac.uk:5432/pfmegrnargs",
        "user": "reader",
        "pass": "NWDMCE5xdipIjRrp"
      }
    },
    "openaf-s3": {
      "command": "docker",
      "args": [
        "run", "-i", "--pull", "always",
        "-e", "OJOB=ojob.io/ai/mcps/mcp-s3",
        "openaf/ojobc:edge-t8"
      ],
      "transport": "stdio",
      "env": {
        "accessKey": "PUT_ACCESS_KEY_HERE",
        "secret": "PUT_SECRET_HERE",
        "region": "eu-west-1"
      }
    }
  },
  "groups": {
    "openaf-ojob": {
      "title": "OpenAF ojob.io MCPs",
      "description": "Weather, time, data, cloud and shell helpers backed by OpenAF",
      "icon": "rocket",
      "servers": [
        "openaf-weather",
        "openaf-db",
        "openaf-s3",
        "openaf-shell",
        "openaf-time",
        "openaf-net",
        "openaf-kube",
        "openaf-email"
      ]
    }
  },
  "clients": {
    "github.copilot": {
      "defaultGroups": ["openaf-ojob"]
    }
  }
}
```

- The `icon` value is optional; VS Code accepts any codicon name.
- Add the remaining `openaf-*` entries (`openaf-shell`, `openaf-email`, etc.) to `mcpServers` following the same pattern before referencing them in the group.
- Store secrets safely — for example, use a local `.env` file with `docker run --env-file` and replace the inline placeholders above.
- VS Code surfaces the group inside the Copilot Agents panel — select it once and the agent keeps those MCP tools handy for subsequent conversations.
- If you are on an older Copilot Agent build that only accepts server lists, swap `defaultGroups` for `defaultServers` and list the entries manually.

### Add servers through the VS Code UI

Prefer the UI over editing JSON? VS Code 1.90+ exposes the MCP catalog directly:

1. Press `⌘⇧P` / `Ctrl+Shift+P` to open the Command Palette.
2. Run **GitHub Copilot: Manage MCP Servers**.
3. Choose **Add MCP Server** → **Custom STDIO Command**.
4. Paste the Docker command (for example the `mcp-weather` one-liner) into the command field.
5. Give the server a friendly name (e.g. `openaf-weather`) and confirm.
6. Repeat for the remaining OpenAF MCPs.
7. Back on the **Manage MCP Servers** view, pick **Create Group** and select the newly added servers so they appear together inside Copilot Agent mode.
8. Reload VS Code if prompted, then open the Copilot Agents panel and enable the group.

Restart VS Code (or run **Developer: Reload Window**) after saving `mcp.json`. Then open GitHub Copilot Chat, pick the `OpenAF ojob.io MCPs` agent group, and try prompts such as “list the tables in the Postgres instance” or “what’s the weather in Lisbon?” — Copilot will route the request to the respective OpenAF MCP.
