#!/usr/bin/env python3
"""Exercise the documentation's MCP skeleton on an ephemeral loopback port."""
import argparse
import json
from pathlib import Path
import re
import shutil
import socket
import subprocess
import tempfile
import time
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

from sync_docs import ROOT


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--jar", type=Path, required=True)
    parser.add_argument("--sources", type=Path, required=True)
    parser.add_argument("--report", type=Path)
    args = parser.parse_args()
    source = (ROOT / "docs/guides/ojob/build-mcp-server.md").read_text()
    skeleton = re.search(r"(?ms)^```yaml\n(.*?)^```", source)[1]
    # Dependencies are supplied from the frozen export, never auto-installed.
    skeleton = re.sub(r"  opacks:\n(?:  - [^\n]*\n)+", "", skeleton)
    with socket.socket() as sock:
        sock.bind(("127.0.0.1", 0))
        port = sock.getsockname()[1]
    results = []
    with tempfile.TemporaryDirectory(prefix="openaf-doc-mcp-") as directory:
        work = Path(directory)
        for path in (args.sources / "ojob-common").glob("*.yaml"):
            shutil.copy2(path, work / path.name)
        (work / "example.yaml").write_text(skeleton)
        with (work / "server.log").open("w+") as log:
            proc = subprocess.Popen(["java", "-Duser.home=" + directory, "-jar", str(args.jar.resolve()),
                                     "--ojob", "-e", f"example.yaml onport={port} myConfig=value"],
                                    cwd=work, stdout=log, stderr=log)
            try:
                def rpc(method, params, identifier=1):
                    request = Request(f"http://127.0.0.1:{port}/mcp",
                        data=json.dumps({"jsonrpc": "2.0", "id": identifier, "method": method, "params": params}).encode(),
                        headers={"Content-Type": "application/json", "Accept": "application/json"})
                    with urlopen(request, timeout=3) as response:
                        return json.loads(response.read())
                for attempt in range(60):
                    try:
                        response = rpc("initialize", {"protocolVersion": "2024-11-05", "capabilities": {},
                                                      "clientInfo": {"name": "documentation-test", "version": "1"}})
                        break
                    except (URLError, TimeoutError):
                        if proc.poll() is not None:
                            raise RuntimeError("MCP server exited before accepting requests")
                        time.sleep(0.25)
                else:
                    raise RuntimeError("MCP server did not start")
                assert response["result"]["serverInfo"]["name"] == "myservice", response
                results.append("initialize")
                response = rpc("tools/list", {}, 2)
                assert [tool["name"] for tool in response["result"]["tools"]] == ["myservice-tool"], response
                results.append("tool discovery")
                response = rpc("tools/call", {"name": "myservice-tool", "arguments": {"param1": "demo"}}, 3)
                assert json.loads(response["result"]["content"][0]["text"])["message"] == "Processed demo", response
                results.append("tool result")
                response = rpc("tools/call", {"name": "unlisted-job", "arguments": {}}, 4)
                assert "error" in response or response.get("result", {}).get("isError"), response
                results.append("unknown tool rejected")
            except Exception:
                log.flush()
                log.seek(0)
                print(log.read()[-6000:])
                raise
            finally:
                proc.terminate()
                try:
                    proc.wait(timeout=10)
                except subprocess.TimeoutExpired:
                    proc.kill()
                    proc.wait()
    report = {"source": "docs/guides/ojob/build-mcp-server.md", "passed": len(results), "checks": results}
    if args.report:
        args.report.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
