---
layout: default
title: ow.instrumentation
parent: Reference
grand_parent: OpenAF docs
---

## ow.instrumentation

`var ins = ow.loadInstrumentation()` loads the opt-in instrumentation module. Loading or configuring it alone does not enable capture. No exporter or HTTP server starts implicitly.

| API | Purpose |
| --- | --- |
| `configure(options)` | Merge resource, sampling, signal, and filter configuration. |
| `enable()`, `disable()`, `isEnabled(signal)` | Control or inspect capture. |
| `registerProvider(name, provider)`, `unregisterProvider(name)` | Register callbacks or remove and return a provider. |
| `startSpan(name, options)` | Create a span without changing current context. |
| `withSpan(name, options, fn)` | Run a synchronous callback with a current span and end it in `finally`; also accepts `(name, fn)`. |
| `captureContext()`, `withContext(context, fn)`, `bind(fn, context)` | Explicit context capture, restoration, and callback binding. |
| `suppress(fn)` | Exclude telemetry implementation work from capture. |
| `inject(headers, context)`, `extract(headers)` | Write/read W3C trace context. |
| `counter(name, options)`, `upDownCounter(name, options)`, `gauge(name, options)`, `histogram(name, options)` | Create metric instruments. |
| `collectMetrics(mappings)` | Sample explicitly selected existing `ow.metrics` values. |
| `channelProvider(options)` | Store records in bounded span/log/metric channels. |
| `batchProvider(send, options)` | Create a bounded queue for forwarding records. |
| `flush(timeoutMs)`, `shutdown(timeoutMs)`, `getStats()` | Flush, stop, or inspect providers; default lifecycle budget is 5,000 ms. |

Providers receive independent JSON records with API `version: 1`. Provider errors are counted and do not replace application errors. `withSpan` ends when its callback returns, including when that return value is a promise; bind asynchronous callbacks explicitly.

See the [instrumentation guide](../guides/advanced/instrumentation.md) for span methods, configuration defaults, automatic capture boundaries, retention, authenticated channel access, and forwarding limitations.
