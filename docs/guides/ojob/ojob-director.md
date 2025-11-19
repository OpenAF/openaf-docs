---
layout: default
title: oJob Director
parent: oJob
grand_parent: Guides
---

# oJob Director - Distributed Job Coordination

The oJob Director pattern enables distributed job execution coordination across multiple instances using OpenAF channels, ensuring jobs are executed exactly once even when multiple processes are running.

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## Overview

oJob Director provides a mechanism to:
- **Prevent duplicate execution** of jobs across multiple instances
- **Coordinate distributed workflows** through a shared channel
- **Track job execution state** with unique identifiers
- **Enable high-availability patterns** for job orchestration

### Use Cases

- Multi-instance deployments where only one should process a job
- Distributed job processing with coordination
- High-availability job schedulers
- Preventing race conditions in job execution

---

## Getting Started

### Basic Setup

```yaml
include:
  - oJobBasics.yaml
  - oJobDirector.yaml  # From oJob-common

jobs:
  - name: Initialize Director
    to: oJob Director init
    args:
      ch: myapp::coordination    # Channel name
      stamp:                      # Stamp to identify director entries
        type: director
        app: myapp

  - name: My Distributed Job
    from: oJob Director checkin
    args:
      jobName: process-data
      jobUUID: "{{uuid}}"
    exec: |
      // This code only runs if no other instance has processed this UUID
      log("Processing job with UUID: " + args.jobUUID)

      // Your job logic here
      var result = processData(args.data)

      // Mark as complete
      $job("oJob Director checkout", {
        jobName: args.jobName,
        jobUUID: args.jobUUID,
        result: result
      })
```

---

## Core Concepts

### Channel-Based Coordination

The Director uses an OpenAF channel to store job execution state:

```javascript
{
  type: "director",      // Stamp field
  app: "myapp",          // Stamp field
  name: "process-data",  // Job name
  uuid: "abc-123",       // Execution UUID
  status: "running",     // Current status
  timestamp: 1234567890, // When started
  result: {}             // Final result (when complete)
}
```

### Check-in Pattern

The **checkin** pattern prevents duplicate execution:

1. Job attempts to check in with `jobName` + `jobUUID`
2. Director checks if this combination already exists
3. If exists → job stops (already processed)
4. If new → job continues execution

---

## Director Jobs Reference

### oJob Director init

Initializes the Director coordination channel.

**Arguments:**

| Argument | Type | Default | Description |
|----------|------|---------|-------------|
| `ch` | String | `oJob::check` | Channel name for coordination |
| `stamp` | Map | `{ type: "director" }` | Identifying stamp for director entries |

**Example:**

```yaml
jobs:
  - name: Setup Director
    to: oJob Director init
    args:
      ch: production::jobs
      stamp:
        type: director
        environment: production
        region: us-east-1
```

### oJob Director checkin

Checks in a job execution. Use with `from` to prevent execution if already processed.

**Arguments:**

| Argument | Type | Required | Description |
|----------|------|----------|-------------|
| `jobName` | String | Yes | Generic job identifier |
| `jobUUID` | String | Yes | Unique execution identifier |

**Example:**

```yaml
jobs:
  - name: Process Order
    from: oJob Director checkin
    args:
      jobName: order-processing
      jobUUID: "{{orderId}}"
    exec: |
      // Only runs if this orderId hasn't been processed
      log("Processing order: " + args.orderId)
```

### oJob Director checkout

Marks a job execution as complete.

**Arguments:**

| Argument | Type | Required | Description |
|----------|------|----------|-------------|
| `jobName` | String | Yes | Generic job identifier |
| `jobUUID` | String | Yes | Unique execution identifier |
| `result` | Any | No | Result to store |

**Example:**

```yaml
exec: |
  var result = {
    status: "completed",
    itemsProcessed: 100
  }

  $job("oJob Director checkout", {
    jobName: "batch-process",
    jobUUID: args.batchId,
    result: result
  })
```

### oJob Director check

Checks if a job has already been executed without blocking.

**Arguments:**

| Argument | Type | Required | Description |
|----------|------|----------|-------------|
| `jobName` | String | Yes | Generic job identifier |
| `jobUUID` | String | Yes | Unique execution identifier |

**Returns:** Job record if exists, undefined otherwise.

**Example:**

```yaml
exec: |
  var existing = $job("oJob Director check", {
    jobName: "import-data",
    jobUUID: args.importId
  })

  if (isDef(existing)) {
    log("Import already processed at: " + existing.timestamp)
  } else {
    log("Import is new, proceeding...")
  }
```

---

## Common Patterns

### Pattern 1: Event-Driven Processing

Process events from a queue, ensuring each event is processed exactly once:

```yaml
include:
  - oJobDirector.yaml

jobs:
  # Initialize
  - name: Init
    to: oJob Director init
    args:
      ch: events::coordination

  # Process events
  - name: Process Event
    from: oJob Director checkin
    args:
      jobName: event-processor
      jobUUID: "{{eventId}}"
    exec: |
      log("Processing event: " + args.eventId)

      // Your event processing logic
      var result = handleEvent(args.eventData)

      // Mark complete
      $job("oJob Director checkout", {
        jobName: "event-processor",
        jobUUID: args.eventId,
        result: result
      })

todo:
  - Init
  - name: Process Event
    args:
      eventId: evt-12345
      eventData: { type: "order", amount: 100 }
```

### Pattern 2: Scheduled Job with HA

Run scheduled jobs in high-availability mode:

```yaml
include:
  - oJobDirector.yaml

ojob:
  # Run every minute
  daemon: true

jobs:
  - name: Init Director
    to: oJob Director init

  - name: Hourly Cleanup
    from: oJob Director checkin
    typeArgs:
      cron: "0 * * * *"  # Every hour
    args:
      jobName: cleanup
      jobUUID: "{{ow.format.fromDate(new Date(), 'yyyyMMddHH')}}"
    exec: |
      // Generate UUID based on hour - ensures once per hour
      log("Running hourly cleanup")

      // Cleanup logic
      cleanupOldFiles()
      cleanupExpiredSessions()

      $job("oJob Director checkout", {
        jobName: "cleanup",
        jobUUID: args.jobUUID,
        result: { cleaned: true }
      })

todo:
  - Init Director
  - Hourly Cleanup
```

### Pattern 3: Distributed Batch Processing

Process batches with multiple workers:

```yaml
include:
  - oJobDirector.yaml

jobs:
  - name: Setup
    to: oJob Director init
    args:
      ch: batch::coordination

  # Batch coordinator - creates batch jobs
  - name: Create Batch Jobs
    exec: |
      var batches = [
        { batchId: "batch-001", items: [...] },
        { batchId: "batch-002", items: [...] },
        { batchId: "batch-003", items: [...] }
      ]

      batches.forEach(batch => {
        $job("Process Batch", batch)
      })

  # Batch processor - multiple workers can run this
  - name: Process Batch
    from: oJob Director checkin
    args:
      jobName: batch-processor
      jobUUID: "{{batchId}}"
    exec: |
      log("Worker " + getEnv("WORKER_ID") + " processing " + args.batchId)

      var results = args.items.map(item => processItem(item))

      $job("oJob Director checkout", {
        jobName: "batch-processor",
        jobUUID: args.batchId,
        result: {
          processed: results.length,
          worker: getEnv("WORKER_ID")
        }
      })

todo:
  - Setup
  - Create Batch Jobs
```

### Pattern 4: Retry Logic with State

```yaml
include:
  - oJobDirector.yaml

jobs:
  - name: Init
    to: oJob Director init

  - name: Retry Job
    exec: |
      var maxRetries = 3
      var attempt = 0
      var success = false

      while (attempt < maxRetries && !success) {
        attempt++
        var retryUUID = args.taskId + "-retry-" + attempt

        // Check if this retry already succeeded
        var existing = $job("oJob Director check", {
          jobName: "risky-task",
          jobUUID: retryUUID
        })

        if (isDef(existing) && existing.result.success) {
          log("Task already completed in previous retry")
          success = true
          break
        }

        // Try to execute
        try {
          $job("Execute Risky Task", {
            taskId: args.taskId,
            jobUUID: retryUUID,
            attempt: attempt
          })
          success = true
        } catch(e) {
          logErr("Attempt " + attempt + " failed: " + e.message)
          if (attempt < maxRetries) {
            sleep(1000 * attempt, true)  // Exponential backoff
          }
        }
      }

  - name: Execute Risky Task
    from: oJob Director checkin
    args:
      jobName: risky-task
      jobUUID: "{{jobUUID}}"
    exec: |
      log("Attempt " + args.attempt + " for task " + args.taskId)

      // Risky operation that might fail
      var result = doRiskyOperation(args.taskId)

      $job("oJob Director checkout", {
        jobName: "risky-task",
        jobUUID: args.jobUUID,
        result: {
          success: true,
          attempt: args.attempt,
          data: result
        }
      })
```

---

## Channel Storage Options

The Director can use different channel types for coordination:

### In-Memory (Simple)

```yaml
jobs:
  - name: Init Director
    exec: |
      $ch("local::coordination").create()

      $job("oJob Director init", {
        ch: "local::coordination"
      })
```

**Pros:** Fast, simple
**Cons:** Not shared across processes

### File-Based (Persistent)

```yaml
jobs:
  - name: Init Director
    exec: |
      $ch("file::coordination").create(1, "db", {
        file: ".director-state.db"
      })

      $job("oJob Director init", {
        ch: "file::coordination"
      })
```

**Pros:** Persists across restarts, shared via filesystem
**Cons:** File locking limitations

### Ignite (Distributed)

```yaml
jobs:
  - name: Init Director
    exec: |
      plugin("Ignite")

      $ch("ignite::coordination").create(1, "ignite", {
        gridName: "myGrid",
        cacheName: "director"
      })

      $job("oJob Director init", {
        ch: "ignite::coordination"
      })
```

**Pros:** True distributed coordination, scales horizontally
**Cons:** Requires Ignite setup

### ElasticSearch (Audit Trail)

```yaml
jobs:
  - name: Init Director
    exec: |
      $ch("es::coordination").create(1, "elasticsearch", {
        index: "job-coordination",
        url: "http://localhost:9200"
      })

      $job("oJob Director init", {
        ch: "es::coordination"
      })
```

**Pros:** Built-in search, audit trail, persistence
**Cons:** Higher latency, requires ES cluster

---

## Monitoring and Troubleshooting

### View Active Jobs

```yaml
jobs:
  - name: List Active Jobs
    exec: |
      var jobs = $ch(global.oJobCheck.ch)
        .getAll()
        .filter(job => job.type == "director")

      print(af.toYAML(jobs))
```

### Clean Up Old Entries

```yaml
jobs:
  - name: Cleanup Old Jobs
    exec: |
      var cutoff = new Date().getTime() - (24 * 60 * 60 * 1000)  // 24 hours

      var jobs = $ch(global.oJobCheck.ch).getAll()

      jobs.forEach(job => {
        if (job.timestamp < cutoff) {
          $ch(global.oJobCheck.ch).unset(
            merge(global.oJobCheck.stamp, {
              name: job.name,
              uuid: job.uuid
            })
          )
        }
      })

      log("Cleaned up " + jobs.filter(j => j.timestamp < cutoff).length + " old jobs")
```

### Debug Mode

```yaml
jobs:
  - name: Debug Check-in
    exec: |
      log("Checking in: " + args.jobName + " / " + args.jobUUID)

      var existing = $ch(global.oJobCheck.ch).get(
        merge(global.oJobCheck.stamp, {
          name: args.jobName,
          uuid: args.jobUUID
        })
      )

      if (isDef(existing)) {
        log("Job already exists: " + stringify(existing))
      } else {
        log("Job is new, proceeding")

        $job("oJob Director checkin", {
          jobName: args.jobName,
          jobUUID: args.jobUUID
        })
      }
```

---

## Best Practices

### 1. Use Meaningful Job Names

```yaml
# Good
jobName: customer-import-daily
jobName: order-processing

# Bad
jobName: job1
jobName: process
```

### 2. Generate UUIDs Carefully

```yaml
# Event ID - natural unique identifier
jobUUID: "{{orderId}}"

# Time-based - for scheduled jobs
jobUUID: "{{ow.format.fromDate(new Date(), 'yyyyMMddHHmm')}}"

# Combined - for batch items
jobUUID: "{{batchId}}-{{itemId}}"

# Random - for one-time tasks
jobUUID: "{{genUUID()}}"
```

### 3. Always Checkout

```yaml
exec: |
  try {
    // Your job logic
    var result = doWork()

    // Checkout on success
    $job("oJob Director checkout", {
      jobName: args.jobName,
      jobUUID: args.jobUUID,
      result: result
    })
  } catch(e) {
    // Checkout on failure too (with error info)
    $job("oJob Director checkout", {
      jobName: args.jobName,
      jobUUID: args.jobUUID,
      result: { error: e.message, success: false }
    })
    throw e
  }
```

### 4. Include Metadata in Stamps

```yaml
jobs:
  - name: Init
    to: oJob Director init
    args:
      stamp:
        type: director
        application: myapp
        version: "1.0.0"
        environment: production
        datacenter: us-east-1
```

### 5. Implement Cleanup

```yaml
ojob:
  daemon: true

jobs:
  # Cleanup old jobs daily
  - name: Daily Cleanup
    typeArgs:
      cron: "0 2 * * *"  # 2 AM daily
    exec: |
      $job("Cleanup Old Jobs", {
        olderThanHours: 48
      })
```

---

## Complete Example: Order Processing System

```yaml
include:
  - oJobDirector.yaml
  - oJobBasics.yaml

ojob:
  daemon: true
  logToFile:
    logFolder: ./logs

jobs:
  # Initialize
  - name: Init System
    to: oJob Director init
    args:
      ch: orders::coordination
      stamp:
        type: director
        app: order-processor
        version: "2.0"

  # Create distributed channel
  - name: Setup Channels
    exec: |
      plugin("Ignite")
      $ch("orders::coordination").create(1, "ignite", {
        gridName: "orderGrid"
      })

  # Receive order event
  - name: Receive Order
    exec: |
      // Simulate receiving order from queue/webhook
      var order = {
        orderId: args.orderId || "ORD-" + genUUID(),
        customer: "ACME Corp",
        items: [
          { sku: "WIDGET-1", qty: 10 },
          { sku: "GADGET-2", qty: 5 }
        ],
        total: 1500.00
      }

      log("Received order: " + order.orderId)

      // Process it
      $job("Process Order", order)

  # Process order (distributed)
  - name: Process Order
    from: oJob Director checkin
    args:
      jobName: order-processing
      jobUUID: "{{orderId}}"
    exec: |
      log("Processing order: " + args.orderId)

      try {
        // Validate
        $job("Validate Order", args)

        // Reserve inventory
        $job("Reserve Inventory", args)

        // Charge payment
        $job("Process Payment", args)

        // Create shipment
        $job("Create Shipment", args)

        // Mark complete
        $job("oJob Director checkout", {
          jobName: "order-processing",
          jobUUID: args.orderId,
          result: {
            status: "completed",
            total: args.total,
            timestamp: nowUTC()
          }
        })

        log("Order completed: " + args.orderId)

      } catch(e) {
        logErr("Order failed: " + args.orderId + " - " + e.message)

        // Mark as failed
        $job("oJob Director checkout", {
          jobName: "order-processing",
          jobUUID: args.orderId,
          result: {
            status: "failed",
            error: e.message,
            timestamp: nowUTC()
          }
        })

        // Could trigger compensation/rollback here
        throw e
      }

  - name: Validate Order
    exec: |
      // Validation logic
      if (!isDef(args.customer)) throw "Missing customer"
      if (!isArray(args.items) || args.items.length == 0) {
        throw "No items in order"
      }

  - name: Reserve Inventory
    exec: |
      // Inventory reservation logic
      log("Reserved inventory for order: " + args.orderId)

  - name: Process Payment
    exec: |
      // Payment processing logic
      log("Processed payment for order: " + args.orderId)

  - name: Create Shipment
    exec: |
      // Shipment creation logic
      log("Created shipment for order: " + args.orderId)

  # Monitoring
  - name: Show Status
    typeArgs:
      cron: "*/5 * * * *"  # Every 5 minutes
    exec: |
      var jobs = $ch("orders::coordination").getAll()

      var stats = {
        total: jobs.length,
        completed: jobs.filter(j => j.result && j.result.status == "completed").length,
        failed: jobs.filter(j => j.result && j.result.status == "failed").length,
        processing: jobs.filter(j => !isDef(j.result)).length
      }

      log("Order Stats: " + stringify(stats))

todo:
  - Setup Channels
  - Init System
  - Show Status
  # Simulate receiving orders
  - name: Receive Order
    args: { orderId: "ORD-001" }
```

---

## See Also

- [oJob Queue](ojob-queue.md) - Queue-based job processing
- [oJob Basics](common-browse.md) - Basic oJob utilities
- [OpenAF Channels](../../concepts/OpenAF-Channels.html)
- [oJob Reference](../../concepts/oJob.html)
