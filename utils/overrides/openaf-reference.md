# OpenAF core guide

This guide connects the core APIs to their detailed references and runnable examples. It follows the [pinned source baseline](../../source-snapshot.md); inspect installed help when using an older runtime.

## Core Helper Functions

### $$ - Enhanced Object Inspection

```javascript
var user = { name: "Ana", address: { city: "Lisbon" } };
print($$(user).get("address.city"));
$$(user).set("address.country", "PT");
print($$(user).isMap());
```

`get()` returns the value at the path. `getI()` performs case-insensitive lookup. Use a fresh wrapper for independent operations. See [Sigil helpers](sigil.md) and the [source API reference](../../reference/scopesigil.md).

### _$ - Parameter Validation

```javascript
var port = _$("8080", "port").toNumber()
  .check(v => isNumber(v) && isFinite(v) && Math.floor(v) === v && v >= 1 && v <= 65535)
  .$_();
var label = _$(undefined, "label").isString().default("untitled");
```

Conversions return a builder; `.$_()` and `.default(...)` return the final value. Use one combined predicate when all rules must hold. The source has compatibility quirks in chaining and some helpers; follow the [validation guide](../medium/parameter-validation.md#snapshot-compatibility). Methods such as `inRange`, `isEmail`, `minLength` and `hasKeys` are not available on this builder.

## OpenWrap Extensions

Load wrapper modules explicitly before using them. The table links directly to source-generated API entries.

| Module | Loader | Detailed reference |
| --- | --- | --- |
| Formatting | `ow.loadFormat()` | [ow.format](../../reference/ow_format.md) |
| Objects and HTTP | `ow.loadObj()` | [ow.obj](../../reference/ow_obj.md) |
| Channels | `ow.loadCh()` | [ow.ch](../../reference/ow_ch.md) |
| AI providers | `ow.loadAI()` | [ow.ai](../../reference/ow_ai.md) |
| Network | `ow.loadNet()` | [ow.net](../../reference/ow_net.md) |
| Java utilities | `ow.loadJava()` | [ow.java](../../reference/ow_java.md) |
| Server utilities | `ow.loadServer()` | [ow.server](../../reference/ow_server.md) |
| Templates | `ow.loadTemplate()` | [ow.template](../../reference/ow_template.md) |
| Tests | `ow.loadTest()` | [ow.test](../../reference/ow_test.md) |
| Metrics | `ow.loadMetrics()` | [ow.metrics](../../reference/ow_metrics.md) |

### ow.format - Formatting Utilities

```javascript
ow.loadFormat();
print(ow.format.toBytesAbbreviation(1048576));
print(ow.format.fromDate(new Date(), "yyyy-MM-dd HH:mm:ss"));
```

For terminal capabilities, colors and widgets see [CLI behavior](cli.md), [console usage](console.md), and [desktop and terminal views](desktop.md).

### ow.obj - Object Utilities and REST Client

```javascript
var result = $rest({ throwExceptions: true, timeout: 5000 })
  .get("https://api.example.com/items");
print(result);
```

The endpoint is a placeholder. `$rest` returns the decoded body; do not chain response-wrapper methods on it. Use the lower-level [HTTP API](plugin-http.md) when you need transport details.

### ow.ch - Channels

```javascript
$ch("example").create();
try {
  $ch("example").set({ id: 1 }, { id: 1, name: "Ana" });
  print($ch("example").get({ id: 1 }));
} finally {
  $ch("example").destroy();
}
```

Channel types control persistence and backend behavior. Subscribers run asynchronously; use `waitForJobs()` where completion matters. See [channel concepts](../../concepts/OpenAF-Channels.md) and [optional backends](../medium/openaf-channel-implementations-through-opacks.md).

#### Graph channels

Use the `graph` type for nodes and edges, with file or backing-channel storage. Navigation helpers provide neighbors, traversal and shortest paths. See [graph channels](channel-graph.md) for key formats, edge identity, saves and read-only behavior.

#### Time-series channels

Use `timeseries` for labelled numeric samples, retention, rollups and OpenMetrics integration. See [time-series channels](channel-timeseries.md) for timestamp rules, selectors and storage options.

### ow.ai - AI APIs

Use `$llm` or the documented provider interfaces. Configure the provider, model and credentials for your account; model availability is not guaranteed by a source revision. See [LLM concepts](../../concepts/llm.md), [provider APIs](ow-ai-gpttypes.md), [decision contracts](llm-decisions-contracts.md), [schema hooks](openai-schema-hooks.md), and [MCP servers](../ojob/build-mcp-server.md).

## nLinq - Query Processing

```javascript
var people = [{ name: "Ana", age: 31 }, { name: "Rui", age: 17 }];
var adults = $from(people).greaterEquals("age", 18).sort("name").select();
print(adults);
```

`$from` queries in-memory collections. Do not assume that a fluent query creates a bounded-memory stream. Use [oafp's documented streaming inputs](../oafp/oafp-usage.md) for record processing. See [nLinq concepts](../../concepts/OpenAF-nLinq.md).

## Security Features

Use the [secret-store API](../../reference/ow_sec.md) and your configured repository/bucket for credentials. OpenAF is not Node.js: read environment variables with `getEnv`, not `process.env`. Review [oJob security](../ojob/ojob-security.md) and the [JDBC URL policy](jdbc-url-policy.md) when accepting configuration or SQL connection options from callers.

## Server Management

The core HTTP server plugin is `HTTPServer`. [Server helpers](../../reference/ow_server.md) wrap routing, responses and request handling. [oJob-common HTTP and REST modules](../ojob/ojob-common-reference.md) provide reusable jobs, including file browsing and health/metrics endpoints.

## Template Engine

```javascript
print($t("Hello {{name}}", { name: "Ana" }));
```

`$t` expands Handlebars templates from a context map. Follow the [templating cheat sheet](../cheat-sheet/templating.md) for helpers and escaping, and [SQL template examples](generating-sql-with-openaf-templates.md) for a larger application.

## Testing Framework

```javascript
ow.loadTest();
ow.test.assert(2 + 2, 4, "arithmetic");
```

Test failure paths as well as successful output. The [authoring testing guide](../ojob/authoring-testing.md) and [testing reference](../ojob/testing-openaf.md) cover fixtures, assertions, reports and integration boundaries.

## Python Integration

Follow the [Python integration guide](python-integration.md) for subprocess execution, input/output variables, server mode and CLI entry points. Python must be available in the environment where the script runs. Starting a Python server or an external process introduces resource ownership; shut it down in cleanup code.

## Parsing Utilities

```javascript
var config = af.fromYAML("name: Ana\ncount: 2\n");
print(af.toYAML(config));
print(af.toSLON(config));
```

See [JSON and YAML file I/O](../beginner/reading-writing-json-and-yaml.md), [JSON extraction](json-extraction-and-prompts.md), [JSON Schema](json-schema.md), and the [core reference](../../reference/afbase.md).

### Data Formats and Streams

Streams, strings and byte arrays have different lifetimes and types. Close streams you open, and use byte conversion methods for binary plugin APIs. [ZIP](plugin-zip.md), [HTTP](plugin-http.md), and [oafp format options](../oafp/oafp-usage.md) document their input contracts. TOON is a structured-data notation; `af.toTOON` / `af.fromTOON` encode and decode it.

## Data Validation

Use [JSON Schema](json-schema.md) for structural constraints and [parameter validation](../medium/parameter-validation.md) for explicit JavaScript predicates. A schema, example, or model output is not by itself a validation step: invoke the validator and handle failures.

## Additional Core Shortcuts & Utilities

The [dollar-function guide](openaf-dollar-functions.md) covers `$sh`, `$rest`, `$job`, `$do`, `$sec`, `$output` and related helpers. The [scope reference](../../reference/scope.md) contains the extracted signatures. Prefer `syncFn` when the synchronized callback's return value is needed; `sync` does not forward that value.

## Metrics API (ow.metrics)

`ow.metrics.add(name, callback)` registers a callback, and `getSome([names])` returns a map of collected values. See [metrics collection](../medium/metrics-collection.md) for counters, channel collection and strict OpenMetrics output, and [OpenTelemetry](../opacks/opentelemetry.md) for export integrations.

## $path – JMESPath Inspired Query & Transform

```javascript
var names = $path({ users: [{ name: "Ana" }, { name: "Rui" }] }, "users[].name");
print(names);
```

See the [scope reference](../../reference/scope.md#path) for supported functions and options. In oafp, input, main and output query stages have different positions in the pipeline; see [processor concepts](../../concepts/oafp.md).

## Terminal Visualization & Live Dashboards

Use [console and terminal APIs](console.md), [desktop windows](desktop.md), and [oafp charts](../oafp/oafp-usage.md). Interactive examples depend on terminal capabilities or GUI providers and cannot be established by a headless build alone.

## Additional ow.* Highlights

See [instrumentation](instrumentation.md), [Java path integration](path-java.md), [ODoc](odoc.md), [JQ](jq.md), and [package management](opacks.md). Optional integrations are indexed in the [oPack catalog](../opacks/catalog.md).

## Putting It Together: Authoring a New oJob from Scratch

Start with [script-to-oJob authoring](../ojob/script-to-ojob.md), choose a recipe from the [authoring examples](../ojob/authoring-recipes.md), and use the [YAML reference](../ojob/ojob-yaml-reference.md) for lifecycle and argument behavior. Keep external effects in explicit jobs and test them with suitable fixtures.
