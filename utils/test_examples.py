#!/usr/bin/env python3
"""Run selected real documentation fences with an explicitly supplied OpenAF JAR.

All writes happen in a temporary working directory. No provider accounts,
optional oPacks, remote services, deployment or installed-runtime updates.
"""
import argparse
import hashlib
import json
from pathlib import Path
import re
import subprocess
import tempfile

from sync_docs import ROOT


def blocks(path, language="javascript"):
    text = (ROOT / path).read_text()
    return re.findall(r"(?ms)^```" + language + r"\s*\n(.*?)^```\s*$", text)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--jar", type=Path, required=True)
    parser.add_argument("--report", type=Path)
    args = parser.parse_args()
    jar = args.jar.resolve()
    prefix = 'ow.loadTest(); function expectError(fn) { var failed=false; try { fn(); } catch(e) { failed=true; } ow.test.assert(failed,true,"invalid input must throw"); }\n'
    cases = []

    def add(name, path, indexes, assertion=""):
        snippets = blocks(path)
        cases.append((name, path, prefix + "\n".join(snippets[i] for i in indexes) + "\n" + assertion))

    add("validation success and failure", "docs/guides/medium/parameter-validation.md", list(range(7)),
        'ow.test.assert(validPort("443"),443,"converted port"); expectError(()=>validPort("70000")); expectError(()=>validPort("NaN")); expectError(()=>greet(123));')
    add("Sigil path operations and validation", "utils/overrides/sigil.md", [0, 1, 2],
        'ow.test.assert(user.meta.level,5,"nested property"); ow.test.assert(createUser("Ana",30).age,30,"user"); expectError(()=>createUser("",30)); expectError(()=>createUser("Ana",5));')
    add("ZIP bytes roundtrip", "docs/concepts/plugins.md", [2],
        'var checkZip=new ZIP(io.readFileBytes("example.zip")); try { ow.test.assert(af.fromBytes2String(checkZip.getFile("hello.txt")),"Hello\\n","zip entry"); } finally { checkZip.close(); }')
    add("metrics registration and strict OpenMetrics", "docs/guides/medium/metrics-collection.md", [0, 2],
        'ow.test.assert(selected.requests_total,1,"metric callback"); ow.test.assert(ow.metrics.fromObj2OpenMetrics({queue_depth:3},"app",__,__,__,true).trim().endsWith("# EOF"),true,"OpenMetrics EOF");')
    add("metrics channel lifecycle", "docs/guides/medium/metrics-collection.md", [1],
        'ow.test.assert($ch().list().indexOf("myMetrics"),-1,"channel cleanup");')
    add("H2 query and cleanup", "docs/guides/opacks/jdbc-drivers.md", [2],
        'var probe=new DB("org.h2.Driver","jdbc:h2:mem:probe","sa",""); try { ow.test.assert(probe.q("select 1 as answer").results[0].ANSWER,1,"H2 result"); } finally { probe.close(); }')
    add("graph keys traversal and persistence", "docs/guides/advanced/channel-graph.md", [0, 2, 3],
        'ow.test.assert($ch("g").size(),5,"graph entries"); ow.test.assert(g.path("g","a.md","concept:x").length,3,"path"); $ch("g").destroy(); $ch("g").create(true,"graph",{file:"graph.json",create:false}); ow.test.assert($ch("g").size(),5,"persisted graph"); $ch("g").destroy();')
    add("time-series samples and persistence", "docs/guides/advanced/channel-timeseries.md", [0, 1],
        'ow.test.assert($ch("m").get({metric:"cpu",labels:{host:"a"}}).v,0.6,"latest sample"); $ch("m").destroy(); $ch("m").create(true,"timeseries",{file:"metrics.ndjson"}); ow.test.assert($ch("m").size(),4,"persisted samples"); $ch("m").destroy();')

    results = []
    with tempfile.TemporaryDirectory(prefix="openaf-doc-examples-") as work:
        for index, (name, source, code) in enumerate(cases):
            script = Path(work) / f"example-{index}.js"
            script.write_text('try {\n' + code + '\nprint("DOC_TEST_PASS"); } catch(e) { printErr(String(e)); exit(1); }\n')
            proc = subprocess.run(["java", "-Duser.home=" + work, "-jar", str(jar), "-f", str(script)], cwd=work,
                                  capture_output=True, text=True, timeout=60)
            passed = proc.returncode == 0 and "DOC_TEST_PASS" in proc.stdout
            results.append({"name": name, "source": source, "passed": passed,
                            **({} if passed else {"stdout": proc.stdout[-2000:], "stderr": proc.stderr[-2000:]})})
            print(f'{"PASS" if passed else "FAIL"}: {name}')
        # The processor bundled in this core snapshot is explicitly distinct
        # from the standalone oafp development build.
        for name, parameters, expected in [
            ("jq array selection", 'in=json data=[1,2,3] jq=map(.+1) out=json', [2, 3, 4]),
            ("jq record output", 'in=json data=[1,2] jq=.[] out=ndjson', [1, 2]),
            ("oafp H2 input", 'in=db data="select 1 as answer" indbjdbc=jdbc:h2:mem:docs indbuser=sa indbpass= out=json', [{"ANSWER": 1}]),
        ]:
            proc = subprocess.run(["java", "-Duser.home=" + work, "-jar", str(jar), "-c", 'if (isDef(__flags.OAFP)) __flags.OAFP.libs=[]; load(getOpenAFJar()+"::js/oafp.js")', "-e", parameters],
                                  cwd=work, capture_output=True, text=True, timeout=60)
            try:
                actual = [json.loads(line) for line in proc.stdout.splitlines() if line.strip()] if "out=ndjson" in parameters else json.loads(proc.stdout)
                passed = proc.returncode == 0 and actual == expected
            except ValueError:
                passed = False
            results.append({"name": name, "source": "OpenAF bundled processor", "passed": passed,
                            **({} if passed else {"stdout": proc.stdout[-2000:], "stderr": proc.stderr[-2000:]})})
            print(f'{"PASS" if passed else "FAIL"}: {name}')
    report = {"jar_sha256": hashlib.sha256(jar.read_bytes()).hexdigest(), "results": results,
              "passed": sum(r["passed"] for r in results), "total": len(results)}
    if args.report:
        args.report.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))
    raise SystemExit(int(report["passed"] != report["total"]))


if __name__ == "__main__":
    main()
