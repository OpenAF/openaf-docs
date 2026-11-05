---
layout: default
title: Metrics Collection
parent: Medium
grand_parent: Guides
---

{% raw %}
# Metrics collection

`ow.metrics` registers **functions** that produce metric values when collected. It does not register Prometheus-style `{type, help, value}` descriptors with `add()`.

## Register and read a counter

```javascript
ow.loadMetrics();
var requests = $atomic(0);
ow.metrics.add("requests_total", () => requests.get());
requests.inc();
var selected = ow.metrics.getSome(["requests_total"]);
print(selected.requests_total); // 1
```

`getSome()` accepts an array of names and returns a map keyed by those names. `getAll()` collects every registered metric, including built-in JVM and runtime metrics. `add()` leaves an existing registration unchanged; keep mutable state in your callback rather than repeatedly registering the same name.

## Collect into a channel

```javascript
ow.loadMetrics();
$ch("myMetrics").create();
try {
  ow.metrics.startCollecting("myMetrics", 1000, ["mem", "cpu"]);
  sleep(2200, true);
  print($ch("myMetrics").getAll());
} finally {
  ow.metrics.stopCollecting("myMetrics");
  $ch("myMetrics").destroy();
}
```

Create the channel explicitly when you want in-memory storage. If the requested channel does not exist, `startCollecting()` creates an `mvs` channel backed by `metrics.db`. Stop collection before destroying the channel. Collection uses a shared scheduler; the first active collector establishes its period and selection.

## OpenMetrics and integrations

```javascript
ow.loadMetrics();
print(ow.metrics.fromObj2OpenMetrics({ queue_depth: 3 }, "app", __, __, __, true));
```

The sixth argument enables strict OpenMetrics output, including the final `# EOF`. See the [API reference](../../reference/ow_metrics.md) for metadata and conversion arguments, and the [oJob-common HTTP/REST reference](../ojob/ojob-common-reference.md) for endpoint defaults.

Use [time-series channels](../advanced/channel-timeseries.md) for labelled samples, retention and rollups. [Generic instrumentation](../advanced/instrumentation.md) and the [OpenTelemetry oPack](../opacks/opentelemetry.md) cover traces, logs and metric export.
{% endraw %}
