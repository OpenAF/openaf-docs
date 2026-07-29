---
layout: default
title: Testing with ow.test
parent: oJob
grand_parent: Guides
---

# Testing OpenAF code with ow.test

This guide explains how to write and organize tests for your own OpenAF scripts and oJobs using the built-in `ow.test` module. It is adapted from the testing conventions used by the OpenAF project itself to test the runtime, focused on the parts that are directly reusable in any OpenAF-based project.

## Test framework basics

OpenAF ships a built-in test utility at `ow.test`. Load it with `ow.loadTest()` at the top of any test file.

### Core API

```javascript
ow.loadTest();

// Assert equality (throws on mismatch and marks the test as failed)
ow.test.assert(actual, expected, "Descriptive failure message");

// Control output
ow.test.setOutput(true);            // print pass/fail per assertion (default: true)
ow.test.setShowStackTrace(true);    // include Java stack traces on failure

// Profiling
ow.test.profile("operationName", function() {
    someExpensiveOperation();
});
var avg = ow.test.getProfileAvg("operationName");  // average time in ms
var max = ow.test.getProfileMax("operationName");  // max time in ms

// Counters (read after tests complete)
ow.test.getCountTest();     // total tests registered
ow.test.getCountPass();     // tests that passed
ow.test.getCountFail();     // tests that failed
ow.test.getCountAssert();   // total assert() calls executed
ow.test.reset();            // reset all counters
```

See [`ow_test.md`](../../reference/ow_test.md) for the full `ow.test` API reference, including per-key profiling
(`getProfileHits`/`getProfileAvg`/`getProfileLast`/`getProfileMax`/`getProfileMin`/`profileReset`),
`getAllProfileHits`/`getAllProfileAvg`/`getAllProfileLast`, and result export via `toMarkdown()`/`toJUnitXML()`.

### Minimal test file example

```javascript
// Copyright 2024 Your Name

(function() {
    exports.testMyModuleBasic = function() {
        // ow.test is already loaded by the framework — call assert directly
        ow.loadFormat();   // load any OpenAF module you need for the test

        var result = ow.format.toHumanSize(1024);
        ow.test.assert(result, "1 KB", "toHumanSize should format 1024 bytes as 1 KB");
    };

    exports.testMyModuleEdgeCase = function() {
        ow.loadFormat();
        var result = ow.format.toHumanSize(0);
        ow.test.assert(result, "0 B", "toHumanSize should return 0 B for zero input");
    };
})();
```

Key points:
- Wrap everything in a self-executing `(function() { ... })()` so variables do not leak into the global scope.
- Export each test as `exports.testXxx = function() { ... }`.
- Each export function must be independent (no shared mutable state between tests).
- Call `ow.loadTest()` once before running any tests — do **not** repeat it inside individual test functions if a
  shared orchestrator already loaded it.
- Load any OpenAF modules your test needs (e.g. `ow.loadFormat()`, `ow.loadObj()`, `plugin("ZIP")`) at the top of the
  test function itself.

## Naming conventions

Export functions should start with `test` followed by a descriptive name in CamelCase:

```
exports.testZIP                 ✓
exports.testZIPStream           ✓
exports.testMyModuleBasic       ✓
exports.myHelperFunction        ✗  (not discovered as a test by convention-based runners)
```

Group related tests into per-area files, e.g. `tests.Cache.js`, `tests.ZIP.js`, so a whole area can be run or
skipped together.

## Orchestrating tests with oJob

A common pattern is to drive tests from an oJob YAML file so each exported test function gets its own job and
pass/fail reporting. This mirrors the pattern OpenAF itself uses to run its own test suite:

```yaml
# Copyright 2024 Your Name

jobs:
   # Initialise: load the JS test module once
   - name: MyArea::Init
     exec: |
       ow.loadTest()
       args.tests = require("tests.MyArea.js");

   # One job per exported test function
   - name: MyArea::Basic functionality
     from: MyArea::Init
     exec: |
       try {
         args.tests.testMyModuleBasic()
         log("PASS: testMyModuleBasic")
       } catch(e) {
         logErr("FAIL: testMyModuleBasic - " + e)
       }

   - name: MyArea::Edge case
     from: MyArea::Init
     exec: |
       try {
         args.tests.testMyModuleEdgeCase()
         log("PASS: testMyModuleEdgeCase")
       } catch(e) {
         logErr("FAIL: testMyModuleEdgeCase - " + e)
       }

todo:
   - MyArea::Init
   - MyArea::Basic functionality
   - MyArea::Edge case
```

After all jobs run, read the aggregate counters and write a report:

```javascript
ow.loadTest()
log("Tests: " + ow.test.getCountTest() + ", Pass: " + ow.test.getCountPass() + ", Fail: " + ow.test.getCountFail())
io.writeFileString("test-results.md", ow.test.toMarkdown())
io.writeFileString("test-results.xml", ow.test.toJUnitXML("MySuite", "My Test Suite"))
```

## Run tests locally

Any oJob YAML file that wires up your tests can be run directly:

```bash
ojob autoTest.yaml
# or, without ojob on PATH:
java -jar openaf.jar --ojob -e autoTest.yaml
```

## CI integration

To fail a CI pipeline when tests fail, check the counters (or the JUnit XML output) after the run and exit
non-zero:

```javascript
ow.loadTest()
if (ow.test.getCountFail() > 0) {
    printErr(ow.test.getCountFail() + " test(s) failed")
    exit(1)
}
```

Most CI systems (GitHub Actions, GitLab CI, Jenkins) can consume the JUnit XML produced by `ow.test.toJUnitXML()`
directly for a readable test report in the pipeline UI.

## Minimal test file template (copy-paste ready)

```javascript
// Copyright 2024 Your Name
// Tests for <module or function description>

(function() {

    exports.testMyFuncBasic = function() {
        // Load any OpenAF module you need
        // ow.loadFormat();

        // Arrange
        var input    = "hello";
        var expected = "HELLO";

        // Act
        var result = myModule.myFunc(input);

        // Assert
        ow.test.assert(result, expected, "myFunc should uppercase the input");
    };

    exports.testMyFuncNull = function() {
        var result = myModule.myFunc(null);
        ow.test.assert(result, null, "myFunc should return null for null input");
    };

    exports.testMyFuncWithCleanup = function() {
        var tmpFile = "myFunc.tmp";
        try {
            myModule.myFuncWriteFile(tmpFile, "data");
            ow.test.assert(io.fileExists(tmpFile), true, "Output file should exist");
        } finally {
            io.rm(tmpFile);
        }
    };

})();
```

## Common pitfalls

### Tests that need network access

Guard with a connectivity check and skip gracefully when the network is unavailable:

```javascript
exports.testMyHTTP = function() {
    try {
        $rest().get("http://example.com");
    } catch(e) {
        log("Skipping network test: " + e.message);
        return;
    }
    // ... assertions ...
};
```

Set reasonable timeouts with `$rest({ timeout: 5000 }).get(...)`.

### Cleanup

- Clean up temporary files with `io.rm("path")` at the end of the function, using `try/finally` so cleanup still
  runs when an assertion throws.
- Avoid hard-coded absolute paths; use paths relative to the test file's working directory.

### Viewing detailed results

```javascript
ow.loadTest()
print(ow.test.toMarkdown())               // human-readable summary + per-test table
io.writeFileString("results.xml", ow.test.toJUnitXML())  // for CI dashboards
```
