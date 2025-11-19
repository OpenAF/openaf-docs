---
layout: default
title: Metrics Collection
parent: Medium
grand_parent: Guides
---

# Metrics Collection and Monitoring

OpenAF provides built-in metrics collection capabilities through the `ow.metrics` module, enabling you to collect, expose, and monitor application metrics in OpenMetrics format (compatible with Prometheus).

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## Overview

The `ow.metrics` module allows you to:
- **Collect custom metrics** from your applications
- **Auto-collect system metrics** (CPU, memory, threads)
- **Export to OpenMetrics format** (Prometheus-compatible)
- **Expose metrics via HTTP** for scraping
- **Track function performance** automatically

---

## Getting Started

### Basic Metrics Collection

```javascript
ow.loadMetrics();

// Add a simple counter
ow.metrics.add("requests_total", {
  help: "Total number of requests",
  type: "counter",
  value: 0
});

// Increment the counter
var current = ow.metrics.getSome("requests_total");
ow.metrics.add("requests_total", {
  value: current.value + 1
});
```

### Viewing Metrics

```javascript
// Get all metrics
var allMetrics = ow.metrics.getAll();
print(af.toYAML(allMetrics));

// Get specific metric
var requestMetric = ow.metrics.getSome("requests_total");
print("Total requests: " + requestMetric.value);

// Export as OpenMetrics format
ow.loadFormat();
var openMetrics = ow.metrics.fromObj2OpenMetrics(ow.metrics.getAll());
print(openMetrics);
```

---

## Metric Types

### Counter

Monotonically increasing value (e.g., requests, errors).

```javascript
ow.metrics.add("http_requests_total", {
  help: "Total HTTP requests",
  type: "counter",
  labels: { method: "GET", path: "/api" },
  value: 0
});

// Increment
var metric = ow.metrics.getSome("http_requests_total", { method: "GET", path: "/api" });
ow.metrics.add("http_requests_total", {
  labels: { method: "GET", path: "/api" },
  value: metric.value + 1
});
```

### Gauge

Value that can go up or down (e.g., temperature, memory usage).

```javascript
ow.metrics.add("memory_usage_bytes", {
  help: "Current memory usage in bytes",
  type: "gauge",
  value: java.lang.Runtime.getRuntime().totalMemory() - java.lang.Runtime.getRuntime().freeMemory()
});

// Update gauge
ow.metrics.add("memory_usage_bytes", {
  value: java.lang.Runtime.getRuntime().totalMemory() - java.lang.Runtime.getRuntime().freeMemory()
});
```

### Histogram

Observations in buckets (e.g., request duration).

```javascript
ow.metrics.add("http_request_duration_seconds", {
  help: "HTTP request duration in seconds",
  type: "histogram",
  buckets: [0.1, 0.5, 1.0, 2.0, 5.0],
  value: []  // Array of observations
});

// Add observation
var duration = 0.345;  // 345ms
var metric = ow.metrics.getSome("http_request_duration_seconds");
metric.value.push(duration);
ow.metrics.add("http_request_duration_seconds", { value: metric.value });
```

### Summary

Similar to histogram, calculates quantiles.

```javascript
ow.metrics.add("response_size_bytes", {
  help: "Response size in bytes",
  type: "summary",
  value: []
});

// Add observation
var size = 1024;
var metric = ow.metrics.getSome("response_size_bytes");
metric.value.push(size);
ow.metrics.add("response_size_bytes", { value: metric.value });
```

---

## Labels

Labels allow you to segment metrics by dimensions.

```javascript
// Add metric with labels
ow.metrics.add("api_requests_total", {
  help: "API requests",
  type: "counter",
  labels: {
    method: "GET",
    endpoint: "/users",
    status: "200"
  },
  value: 1
});

// Same metric, different labels
ow.metrics.add("api_requests_total", {
  labels: {
    method: "POST",
    endpoint: "/users",
    status: "201"
  },
  value: 1
});

// Retrieve specific label combination
var getUserMetric = ow.metrics.getSome("api_requests_total", {
  method: "GET",
  endpoint: "/users",
  status: "200"
});
```

---

## Automatic Metrics Collection

### Start Collecting System Metrics

```javascript
ow.loadMetrics();

// Start collecting JVM metrics every 5 seconds
ow.metrics.startCollecting(5000);
```

**Collected metrics:**
- `process_cpu_usage` - CPU usage percentage
- `jvm_memory_used_bytes` - JVM memory usage
- `jvm_memory_max_bytes` - JVM max memory
- `jvm_threads_current` - Current thread count
- `jvm_threads_daemon` - Daemon thread count

### Stop Collecting

```javascript
ow.metrics.stopCollecting();
```

### Collect Metrics for a Function

Automatically measure function execution time and call count.

```javascript
ow.loadMetrics();

// Original function
function processData(data) {
  sleep(100, true);  // Simulate work
  return data.length;
}

// Wrap with metrics
var metricsData = {
  name: "process_data",
  help: "Process data function",
  unit: "seconds"
};

var wrappedFunction = ow.metrics.collectMetrics4Fn(processData, metricsData);

// Use wrapped function
var result = wrappedFunction([1, 2, 3, 4, 5]);

// View metrics
print(af.toYAML(ow.metrics.getSome("process_data_duration_seconds")));
print(af.toYAML(ow.metrics.getSome("process_data_calls_total")));
```

---

## Exposing Metrics via HTTP

### Using oJobHTTPd

```yaml
include:
  - oJobHTTPd.yaml

ojob:
  daemon: true

jobs:
  # Start collecting system metrics
  - name: Init Metrics
    exec: |
      ow.loadMetrics();
      ow.metrics.startCollecting(5000);

  # Metrics endpoint
  - name: Metrics Endpoint
    to: HTTP Service
    args:
      port: 8080
      uri: /metrics
      execURI: |
        ow.loadFormat();

        // Get all metrics and convert to OpenMetrics
        var metrics = ow.metrics.getAll();
        var openMetrics = ow.metrics.fromObj2OpenMetrics(metrics);

        return server.replyOKText(openMetrics);

todo:
  - HTTP Start Server
  - Init Metrics
  - Metrics Endpoint
```

Access metrics at: `http://localhost:8080/metrics`

### Using oJobHTTPd Shortcuts

```yaml
include:
  - oJobHTTPd.yaml

todo:
  # Start HTTP server
  - (httpdStart): &PORT 8080

  # Enable metrics collection
  - (httpdMetrics): *PORT
    ((prefix)): myapp
    ((help)): My application metrics
```

---

## Common Patterns

### Pattern 1: Request Counting

```javascript
ow.loadMetrics();

// Initialize counter
ow.metrics.add("requests_total", {
  help: "Total requests processed",
  type: "counter",
  value: 0
});

// Increment on each request
function handleRequest(req) {
  var metric = ow.metrics.getSome("requests_total");
  ow.metrics.add("requests_total", {
    value: metric.value + 1
  });

  // Process request...
}
```

### Pattern 2: Request Duration Tracking

```javascript
function handleRequest(req) {
  var startTime = now();

  try {
    // Process request
    var result = processRequest(req);

    // Record duration
    var duration = (now() - startTime) / 1000;  // Convert to seconds

    ow.metrics.add("request_duration_seconds", {
      help: "Request duration in seconds",
      type: "histogram",
      labels: { path: req.path, status: "success" },
      buckets: [0.01, 0.05, 0.1, 0.5, 1.0],
      value: [duration]
    });

    return result;

  } catch(e) {
    // Record error duration
    var duration = (now() - startTime) / 1000;

    ow.metrics.add("request_duration_seconds", {
      labels: { path: req.path, status: "error" },
      buckets: [0.01, 0.05, 0.1, 0.5, 1.0],
      value: [duration]
    });

    throw e;
  }
}
```

### Pattern 3: Application-Specific Metrics

```javascript
ow.loadMetrics();

// Database connection pool
ow.metrics.add("db_connections_active", {
  help: "Active database connections",
  type: "gauge",
  value: 0
});

ow.metrics.add("db_connections_idle", {
  help: "Idle database connections",
  type: "gauge",
  value: 10
});

// Update metrics
function updateConnectionMetrics() {
  var active = getActiveConnections();
  var idle = getIdleConnections();

  ow.metrics.add("db_connections_active", { value: active });
  ow.metrics.add("db_connections_idle", { value: idle });
}

// Queue depth
ow.metrics.add("queue_depth", {
  help: "Current queue depth",
  type: "gauge",
  value: 0
});

function updateQueueMetrics() {
  var depth = global.__oJobQueue ? global.__oJobQueue.size() : 0;
  ow.metrics.add("queue_depth", { value: depth });
}
```

### Pattern 4: Error Tracking

```javascript
ow.loadMetrics();

// Error counter
ow.metrics.add("errors_total", {
  help: "Total errors by type",
  type: "counter",
  labels: { type: "", severity: "" },
  value: 0
});

function recordError(errorType, severity) {
  var metric = ow.metrics.getSome("errors_total", {
    type: errorType,
    severity: severity
  }) || { value: 0 };

  ow.metrics.add("errors_total", {
    labels: { type: errorType, severity: severity },
    value: metric.value + 1
  });
}

// Usage
try {
  doSomething();
} catch(e) {
  recordError("database_error", "critical");
  logErr(e);
}
```

---

## Complete Example: Web Service with Metrics

```yaml
include:
  - oJobHTTPd.yaml

ojob:
  daemon: true
  opacks:
    - oJob-common

jobs:
  # Initialize metrics
  - name: Init Metrics
    exec: |
      ow.loadMetrics();

      // Start system metrics collection
      ow.metrics.startCollecting(5000);

      // Initialize custom metrics
      ow.metrics.add("api_requests_total", {
        help: "Total API requests",
        type: "counter",
        labels: { method: "", path: "", status: "" },
        value: 0
      });

      ow.metrics.add("api_request_duration_seconds", {
        help: "API request duration",
        type: "histogram",
        labels: { method: "", path: "" },
        buckets: [0.01, 0.05, 0.1, 0.5, 1.0, 2.0, 5.0],
        value: []
      });

      ow.metrics.add("active_requests", {
        help: "Currently active requests",
        type: "gauge",
        value: 0
      });

  # API endpoint
  - name: API Handler
    to: HTTP Service
    args:
      port: 8080
      uri: /api/data
      execURI: |
        var startTime = now();
        var method = request.method;
        var path = request.uri;

        // Increment active requests
        var active = ow.metrics.getSome("active_requests");
        ow.metrics.add("active_requests", { value: active.value + 1 });

        try {
          // Process request
          var data = { message: "Hello, World!", timestamp: new Date() };

          // Record success metrics
          var duration = (now() - startTime) / 1000;

          // Increment request counter
          var counter = ow.metrics.getSome("api_requests_total", {
            method: method,
            path: path,
            status: "200"
          }) || { value: 0 };

          ow.metrics.add("api_requests_total", {
            labels: { method: method, path: path, status: "200" },
            value: counter.value + 1
          });

          // Record duration
          var hist = ow.metrics.getSome("api_request_duration_seconds", {
            method: method,
            path: path
          }) || { value: [] };

          hist.value.push(duration);
          ow.metrics.add("api_request_duration_seconds", {
            labels: { method: method, path: path },
            buckets: [0.01, 0.05, 0.1, 0.5, 1.0, 2.0, 5.0],
            value: hist.value
          });

          // Decrement active requests
          active = ow.metrics.getSome("active_requests");
          ow.metrics.add("active_requests", { value: active.value - 1 });

          return server.replyOKJSON(data);

        } catch(e) {
          // Record error metrics
          var duration = (now() - startTime) / 1000;

          var counter = ow.metrics.getSome("api_requests_total", {
            method: method,
            path: path,
            status: "500"
          }) || { value: 0 };

          ow.metrics.add("api_requests_total", {
            labels: { method: method, path: path, status: "500" },
            value: counter.value + 1
          });

          // Decrement active requests
          active = ow.metrics.getSome("active_requests");
          ow.metrics.add("active_requests", { value: active.value - 1 });

          return server.reply("Internal Server Error", 500, {});
        }

  # Metrics endpoint
  - name: Metrics Endpoint
    to: HTTP Service
    args:
      port: 8080
      uri: /metrics
      execURI: |
        ow.loadFormat();

        var metrics = ow.metrics.getAll();
        var openMetrics = ow.metrics.fromObj2OpenMetrics(metrics);

        return server.replyOKText(openMetrics);

  # Health endpoint
  - name: Health Endpoint
    to: HTTP Service
    args:
      port: 8080
      uri: /health
      execURI: |
        return server.replyOKJSON({ status: "healthy", timestamp: new Date() });

todo:
  - HTTP Start Server
  - Init Metrics
  - API Handler
  - Metrics Endpoint
  - Health Endpoint
```

**Test the service:**

```bash
# Make requests
curl http://localhost:8080/api/data

# View metrics
curl http://localhost:8080/metrics
```

---

## Prometheus Integration

### Prometheus Configuration

```yaml
# prometheus.yml
scrape_configs:
  - job_name: 'openaf-app'
    scrape_interval: 15s
    static_configs:
      - targets: ['localhost:8080']
        labels:
          environment: 'production'
          app: 'myapp'
```

### Query Examples

```promql
# Request rate
rate(api_requests_total[5m])

# Request duration 99th percentile
histogram_quantile(0.99, rate(api_request_duration_seconds_bucket[5m]))

# Error rate
rate(api_requests_total{status="500"}[5m])

# Memory usage
jvm_memory_used_bytes / jvm_memory_max_bytes * 100
```

---

## Best Practices

### 1. Use Meaningful Names

```javascript
// Good
ow.metrics.add("http_requests_total", ...)
ow.metrics.add("database_query_duration_seconds", ...)

// Bad
ow.metrics.add("requests", ...)
ow.metrics.add("time", ...)
```

### 2. Include Help Text

```javascript
ow.metrics.add("api_requests_total", {
  help: "Total number of API requests processed",  // Always include
  type: "counter",
  value: 0
});
```

### 3. Use Appropriate Types

- **Counter**: Monotonically increasing (requests, errors)
- **Gauge**: Can go up/down (connections, queue size, temperature)
- **Histogram**: Distribution of values (latencies, sizes)
- **Summary**: Similar to histogram, for quantiles

### 4. Limit Label Cardinality

```javascript
// Good - bounded label values
labels: { method: "GET", status: "200" }

// Bad - unbounded label values (user IDs, timestamps)
labels: { user_id: "12345", timestamp: "2024-01-01T00:00:00Z" }
```

### 5. Use Base Units

```javascript
// Seconds, not milliseconds
"request_duration_seconds"

// Bytes, not kilobytes
"memory_usage_bytes"

// Ratio (0-1), not percentage
"cpu_usage_ratio"
```

### 6. Clean Up Old Metrics

```javascript
// Periodically remove stale metrics
function cleanupMetrics() {
  var allMetrics = ow.metrics.getAll();

  Object.keys(allMetrics).forEach(name => {
    if (isStale(allMetrics[name])) {
      delete allMetrics[name];
    }
  });
}
```

---

## Troubleshooting

### Metrics Not Appearing

Check if metrics module is loaded:
```javascript
ow.loadMetrics();
```

Verify metric was added:
```javascript
var metric = ow.metrics.getSome("my_metric");
if (!isDef(metric)) {
  log("Metric not found!");
}
```

### OpenMetrics Format Issues

Test conversion:
```javascript
ow.loadFormat();
var metrics = ow.metrics.getAll();
try {
  var om = ow.metrics.fromObj2OpenMetrics(metrics);
  print(om);
} catch(e) {
  logErr("Conversion failed: " + e.message);
}
```

### High Memory Usage

Limit histogram/summary samples:
```javascript
var metric = ow.metrics.getSome("durations");
if (metric.value.length > 1000) {
  metric.value = metric.value.slice(-1000);  // Keep last 1000
  ow.metrics.add("durations", { value: metric.value });
}
```

---

## See Also

- [ow.metrics Reference](../../reference/ow_metrics.md)
- [oJobHTTPd Guide](../ojob/common-browse.md#oJobHTTPd)
- [OpenMetrics Specification](https://openmetrics.io/)
- [Prometheus Documentation](https://prometheus.io/docs/)
