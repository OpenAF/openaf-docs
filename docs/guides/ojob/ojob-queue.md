---
layout: default
title: oJob Queue
parent: oJob
grand_parent: Guides
---

# oJob Queue - Queue-Based Job Processing

The oJob Queue provides a thread-based queue manager for asynchronous job execution, enabling decoupled job processing, rule-based triggering, and background task management.

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## Overview

oJob Queue enables:
- **Asynchronous job execution** - Jobs run in background thread
- **Rule-based triggering** - Conditionally trigger jobs based on rules
- **Decoupled processing** - Separate job submission from execution
- **Queue management** - Add, process, and delete queued jobs

### Use Cases

- Background task processing
- Delayed job execution
- Event-driven workflows
- Load smoothing and throttling
- Asynchronous API request handling

---

## Getting Started

### Basic Queue Setup

```yaml
include:
  - oJobQueue.yaml  # From oJob-common

jobs:
  # Initialize the queue manager
  - name: Init Queue
    to: oJob Queue Manager
    args:
      queueTimeout: 60000   # Max wait time for queue item (ms)
      queuePeriod: 5000     # Check interval when queue is empty (ms)
      queueDelete: true     # Auto-delete after processing

  # Job to be queued
  - name: Process Data
    exec: |
      log("Processing: " + stringify(args.data))
      // Your processing logic here

  # Submit jobs to queue
  - name: Submit Jobs
    exec: |
      $job("oJob Queue Add", {
        job: "Process Data",
        data: { id: 1, value: "First" }
      })

      $job("oJob Queue Add", {
        job: "Process Data",
        data: { id: 2, value: "Second" }
      })

todo:
  - Init Queue
  - Submit Jobs

ojob:
  daemon: true  # Keep running to process queue
```

---

## Queue Jobs Reference

### oJob Queue Manager

Initializes and starts the queue processing thread.

**Arguments:**

| Argument | Type | Default | Description |
|----------|------|---------|-------------|
| `queueTimeout` | Number | 60000 | Maximum time to wait for a queue item (milliseconds) |
| `queuePeriod` | Number | 5000 | Sleep time when queue is empty before checking again (milliseconds) |
| `queueDelete` | Boolean | true | Automatically delete items after processing |

**Example:**

```yaml
jobs:
  - name: Start Queue
    to: oJob Queue Manager
    args:
      queueTimeout: 30000   # 30 seconds
      queuePeriod: 2000     # Check every 2 seconds
      queueDelete: true
```

**Global Objects Created:**

- `global.__oJobQueue` - The queue instance
- `global.oJobQueue` - Queue management interface with `.add()` and `.del()`

---

### oJob Queue Add

Adds a job to the processing queue.

**Arguments:**

| Argument | Type | Required | Description |
|----------|------|----------|-------------|
| `job` | String | Yes | Name of the job to execute |
| `data` | Map | Yes | Arguments to pass to the job |
| `timeout` | Number | No | Optional timeout for this specific job |

**Example:**

```yaml
exec: |
  $job("oJob Queue Add", {
    job: "Send Email",
    data: {
      to: "user@example.com",
      subject: "Hello",
      body: "Welcome!"
    },
    timeout: 10000  // 10 second timeout
  })
```

---

### oJob Queue Delete

Manually deletes a specific queue item by index.

**Arguments:**

| Argument | Type | Required | Description |
|----------|------|----------|-------------|
| `idx` | Number | Yes | Queue item index to delete |

**Example:**

```yaml
exec: |
  // Usually not needed if queueDelete: true
  $job("oJob Queue Delete", { idx: 0 })
```

---

### oJob Queue Rules

Evaluates rules and conditionally adds jobs to the queue based on rule results.

**Arguments:**

| Argument | Type | Default | Description |
|----------|------|---------|-------------|
| `rules` | Array | [] | Array of rule objects |
| `data` | Map | {} | Data context for rule evaluation |
| `logFn` | Function | (default logger) | Custom logging function |
| `errFn` | Function | (default error logger) | Custom error function |

**Rule Object Structure:**

```javascript
{
  rule: "expression",  // JavaScript expression to evaluate
  job: "JobName"       // Job to trigger if rule evaluates to true
}
```

**Example:**

```yaml
jobs:
  - name: Process Rules
    to: oJob Queue Rules
    args:
      data:
        temperature: 85
        pressure: 120
        alert: true

      rules:
        - rule: "{{temperature}} > 80"
          job: "High Temperature Alert"

        - rule: "{{pressure}} > 100 && {{alert}}"
          job: "Pressure Warning"

        - rule: "{{temperature}} > 100 || {{pressure}} > 150"
          job: "Critical Alert"

  - name: High Temperature Alert
    exec: |
      log("ALERT: High temperature detected: " + args.temperature)

  - name: Pressure Warning
    exec: |
      log("WARNING: Pressure is high: " + args.pressure)

  - name: Critical Alert
    exec: |
      log("CRITICAL: System in critical state!")
```

---

## Common Patterns

### Pattern 1: Background Email Queue

```yaml
include:
  - oJobQueue.yaml
  - oJobEmail.yaml

ojob:
  daemon: true

jobs:
  # Initialize queue
  - name: Init Email Queue
    to: oJob Queue Manager
    args:
      queueTimeout: 120000  # 2 minutes
      queuePeriod: 5000     # Check every 5 seconds

  # Email sender job
  - name: Send Email Job
    to: oJob Send email
    args:
      server: "{{emailServer}}"
      from: "{{emailFrom}}"
      to: "{{emailTo}}"
      subject: "{{emailSubject}}"
      output: "{{emailBody}}"

  # API endpoint that queues emails
  - name: Email API
    to: HTTP Service
    args:
      port: 8080
      uri: /api/email
      execURI: |
        var body = jsonParse(request.body)

        // Validate
        if (!isDef(body.to) || !isDef(body.subject)) {
          return server.reply("Missing required fields", 400, {})
        }

        // Queue the email
        $job("oJob Queue Add", {
          job: "Send Email Job",
          data: {
            emailServer: getEnv("SMTP_SERVER"),
            emailFrom: getEnv("EMAIL_FROM"),
            emailTo: body.to,
            emailSubject: body.subject,
            emailBody: body.body || ""
          }
        })

        return server.replyOKJSON({ status: "queued" })

todo:
  - HTTP Start Server
  - Init Email Queue
  - Email API
```

### Pattern 2: Event-Driven Processing with Rules

```yaml
include:
  - oJobQueue.yaml

ojob:
  daemon: true

jobs:
  # Initialize
  - name: Init System
    to: oJob Queue Manager

  # Receive event
  - name: Receive Sensor Event
    exec: |
      // Simulate sensor data
      var sensorData = {
        sensorId: args.sensorId,
        temperature: args.temperature,
        humidity: args.humidity,
        timestamp: nowUTC()
      }

      log("Received sensor data: " + stringify(sensorData))

      // Evaluate rules
      $job("Process Sensor Rules", sensorData)

  # Rule evaluation
  - name: Process Sensor Rules
    to: oJob Queue Rules
    args:
      data: "{{@}}"  # Pass all incoming args
      rules:
        # Temperature alerts
        - rule: "{{temperature}} > 30"
          job: "Temperature Alert"

        - rule: "{{temperature}} < 10"
          job: "Low Temperature Alert"

        # Humidity alerts
        - rule: "{{humidity}} > 80"
          job: "High Humidity Alert"

        - rule: "{{humidity}} < 20"
          job: "Low Humidity Alert"

        # Combined conditions
        - rule: "{{temperature}} > 28 && {{humidity}} > 70"
          job: "Heat Index Warning"

  # Alert jobs
  - name: Temperature Alert
    exec: |
      log("ALERT: High temperature on sensor " + args.sensorId + ": " + args.temperature + "°C")
      // Send notification, update dashboard, etc.

  - name: Low Temperature Alert
    exec: |
      log("ALERT: Low temperature on sensor " + args.sensorId + ": " + args.temperature + "°C")

  - name: High Humidity Alert
    exec: |
      log("ALERT: High humidity on sensor " + args.sensorId + ": " + args.humidity + "%")

  - name: Low Humidity Alert
    exec: |
      log("ALERT: Low humidity on sensor " + args.sensorId + ": " + args.humidity + "%")

  - name: Heat Index Warning
    exec: |
      log("WARNING: Uncomfortable heat index on sensor " + args.sensorId)

todo:
  - Init System

  # Simulate sensor events
  - name: Receive Sensor Event
    args: { sensorId: "SENSOR-1", temperature: 32, humidity: 75 }

  - name: Receive Sensor Event
    args: { sensorId: "SENSOR-2", temperature: 8, humidity: 45 }

  - name: Receive Sensor Event
    args: { sensorId: "SENSOR-3", temperature: 29, humidity: 85 }
```

### Pattern 3: Batch Processing with Priority

```yaml
include:
  - oJobQueue.yaml

jobs:
  - name: Init Queue
    to: oJob Queue Manager
    args:
      queuePeriod: 1000  # Fast processing

  # Add jobs with implicit priority (FIFO)
  - name: Submit Batch
    exec: |
      var items = [
        { id: 1, priority: "high", data: "Critical data" },
        { id: 2, priority: "low", data: "Normal data" },
        { id: 3, priority: "high", data: "Important data" }
      ]

      // Sort by priority before queueing
      var sorted = $from(items)
        .sort("priority")
        .reverse()
        .select()

      sorted.forEach(item => {
        $job("oJob Queue Add", {
          job: "Process Item",
          data: item
        })
      })

  - name: Process Item
    exec: |
      log("Processing [" + args.priority + "] item " + args.id + ": " + args.data)
      sleep(1000, true)  // Simulate work
      log("Completed item " + args.id)

todo:
  - Init Queue
  - Submit Batch

ojob:
  daemon: true
```

### Pattern 4: Delayed Job Execution

```yaml
include:
  - oJobQueue.yaml

jobs:
  - name: Init Queue
    to: oJob Queue Manager

  # Schedule delayed job
  - name: Schedule Delayed Job
    exec: |
      var delayMs = args.delaySeconds * 1000

      log("Scheduling job to run in " + args.delaySeconds + " seconds")

      // Create a wrapper job that sleeps then executes
      $job("oJob Queue Add", {
        job: "Delayed Job Wrapper",
        data: {
          delay: delayMs,
          targetJob: args.targetJob,
          targetArgs: args.targetArgs
        }
      })

  - name: Delayed Job Wrapper
    exec: |
      log("Waiting " + (args.delay/1000) + " seconds before executing " + args.targetJob)
      sleep(args.delay, true)

      log("Executing delayed job: " + args.targetJob)
      $job(args.targetJob, args.targetArgs)

  # Example delayed jobs
  - name: Send Reminder
    exec: |
      log("REMINDER: " + args.message)

  - name: Cleanup Task
    exec: |
      log("Running cleanup task")

todo:
  - Init Queue

  # Schedule jobs with delays
  - name: Schedule Delayed Job
    args:
      delaySeconds: 10
      targetJob: Send Reminder
      targetArgs: { message: "Meeting in 10 minutes" }

  - name: Schedule Delayed Job
    args:
      delaySeconds: 30
      targetJob: Cleanup Task
      targetArgs: {}

ojob:
  daemon: true
```

### Pattern 5: Rate-Limited API Processing

```yaml
include:
  - oJobQueue.yaml

ojob:
  daemon: true

jobs:
  # Initialize with rate limiting
  - name: Init Rate Limited Queue
    to: oJob Queue Manager
    args:
      queueTimeout: 60000
      queuePeriod: 2000     # Process every 2 seconds (rate limiting)
      queueDelete: true

  # API call job (rate limited by queue)
  - name: Call External API
    exec: |
      ow.loadObj()

      log("Calling API for: " + args.endpoint)

      try {
        var response = $rest()
          .get(args.apiBase + args.endpoint)
          .getResponse()

        log("API success: " + args.endpoint)

        // Store result
        if (isDef(args.resultHandler)) {
          $job(args.resultHandler, {
            endpoint: args.endpoint,
            data: response.data
          })
        }

      } catch(e) {
        logErr("API failed for " + args.endpoint + ": " + e.message)
      }

  # Result handler
  - name: Store API Result
    exec: |
      log("Storing result for " + args.endpoint)
      // Store in database, channel, file, etc.

  # Bulk API submission
  - name: Submit API Calls
    exec: |
      var endpoints = [
        "/users/1",
        "/users/2",
        "/posts/1",
        "/posts/2",
        "/comments/1"
      ]

      endpoints.forEach(endpoint => {
        $job("oJob Queue Add", {
          job: "Call External API",
          data: {
            apiBase: "https://jsonplaceholder.typicode.com",
            endpoint: endpoint,
            resultHandler: "Store API Result"
          }
        })
      })

      log("Queued " + endpoints.length + " API calls")

todo:
  - Init Rate Limited Queue
  - Submit API Calls
```

---

## Advanced Techniques

### Queue Monitoring

```yaml
jobs:
  - name: Monitor Queue
    typeArgs:
      cron: "*/30 * * * * *"  # Every 30 seconds
    exec: |
      if (isDef(global.__oJobQueue)) {
        var size = global.__oJobQueue.size()
        var stats = {
          queueSize: size,
          timestamp: new Date().toISOString()
        }

        log("Queue stats: " + stringify(stats))

        // Alert if queue is too large
        if (size > 100) {
          logWarn("Queue size is large: " + size)
        }
      }
```

### Custom Error Handling

```yaml
jobs:
  - name: Process with Error Handling
    exec: |
      try {
        // Your processing logic
        doSomething(args.data)

      } catch(e) {
        logErr("Job failed: " + e.message)

        // Re-queue with retry count
        var retryCount = args.retryCount || 0

        if (retryCount < 3) {
          log("Re-queuing (attempt " + (retryCount + 1) + ")")

          $job("oJob Queue Add", {
            job: "Process with Error Handling",
            data: merge(args, {
              retryCount: retryCount + 1
            })
          })
        } else {
          logErr("Max retries exceeded, moving to dead letter queue")
          $job("Move to Dead Letter", args)
        }
      }

  - name: Move to Dead Letter
    exec: |
      // Store failed jobs for manual review
      $ch("failed-jobs").set(genUUID(), {
        job: args,
        timestamp: nowUTC(),
        error: args.lastError
      })
```

### Dynamic Rule Loading

```yaml
jobs:
  - name: Load Rules from Config
    exec: |
      // Load rules from file or database
      var rulesConfig = io.readFileYAML("rules.yaml")

      // Process events with loaded rules
      $job("Process Event", {
        event: args.event,
        rules: rulesConfig.rules
      })

  - name: Process Event
    exec: |
      $job("oJob Queue Rules", {
        data: args.event,
        rules: args.rules
      })
```

---

## Best Practices

### 1. Use Daemon Mode

Always use daemon mode when running queue-based oJobs:

```yaml
ojob:
  daemon: true
```

### 2. Handle Job Failures

```yaml
jobs:
  - name: Safe Job
    exec: |
      try {
        // Your logic
      } catch(e) {
        logErr("Job failed: " + e.message)
        // Handle error appropriately
      }
```

### 3. Monitor Queue Size

```yaml
jobs:
  - name: Queue Health Check
    typeArgs:
      cron: "* * * * *"  # Every minute
    exec: |
      var size = global.__oJobQueue.size()
      if (size > 1000) {
        log("WARNING: Queue backlog is large: " + size)
        // Send alert
      }
```

### 4. Use Meaningful Job Names

```yaml
# Good
job: "Send Welcome Email"
job: "Process Payment"

# Bad
job: "Job1"
job: "Process"
```

### 5. Set Appropriate Timeouts

```yaml
jobs:
  - name: Init Queue
    to: oJob Queue Manager
    args:
      queueTimeout: 30000   # Match your job execution time
      queuePeriod: 5000     # Balance responsiveness vs CPU usage
```

### 6. Clean Up Resources

```yaml
jobs:
  - name: Cleanup
    exec: |
      // Cleanup code
      if (isDef(global.__oJobQueue)) {
        global.__oJobQueue.stop()
      }

ojob:
  shutdown:
    - Cleanup
```

---

## Complete Example: Order Processing System

```yaml
include:
  - oJobQueue.yaml
  - oJobBasics.yaml

ojob:
  daemon: true
  logToFile:
    logFolder: ./logs

jobs:
  # Initialize queue
  - name: Init Order Queue
    to: oJob Queue Manager
    args:
      queueTimeout: 60000
      queuePeriod: 2000

  # Receive orders (e.g., from webhook)
  - name: Receive Order
    exec: |
      var order = {
        orderId: args.orderId || genUUID(),
        customer: args.customer,
        items: args.items,
        total: args.total,
        timestamp: nowUTC()
      }

      log("Order received: " + order.orderId)

      // Evaluate business rules
      $job("Evaluate Order Rules", order)

  # Business rules
  - name: Evaluate Order Rules
    to: oJob Queue Rules
    args:
      data: "{{@}}"
      rules:
        # All orders go through validation
        - rule: "true"
          job: "Validate Order"

        # High-value orders
        - rule: "{{total}} > 1000"
          job: "Flag High Value Order"

        # Bulk orders
        - rule: "{{items}}.length > 10"
          job: "Flag Bulk Order"

  # Processing jobs
  - name: Validate Order
    exec: |
      log("Validating order: " + args.orderId)

      // Validation logic
      if (!isDef(args.customer) || args.items.length == 0) {
        $job("oJob Queue Add", {
          job: "Reject Order",
          data: args
        })
        return
      }

      // Valid - queue for processing
      $job("oJob Queue Add", {
        job: "Process Order",
        data: args
      })

  - name: Process Order
    exec: |
      log("Processing order: " + args.orderId)

      // Process order
      sleep(2000, true)  // Simulate processing

      $job("oJob Queue Add", {
        job: "Send Confirmation",
        data: args
      })

  - name: Flag High Value Order
    exec: |
      log("High-value order flagged: " + args.orderId + " ($" + args.total + ")")
      // Notify manager, apply special handling

  - name: Flag Bulk Order
    exec: |
      log("Bulk order flagged: " + args.orderId + " (" + args.items.length + " items)")
      // Route to bulk processing team

  - name: Reject Order
    exec: |
      logErr("Order rejected: " + args.orderId)
      // Send rejection email

  - name: Send Confirmation
    exec: |
      log("Sending confirmation for order: " + args.orderId)
      // Send email confirmation

  # Monitoring
  - name: Monitor System
    typeArgs:
      cron: "*/30 * * * * *"
    exec: |
      var queueSize = global.__oJobQueue.size()
      log("System status - Queue size: " + queueSize)

todo:
  - Init Order Queue
  - Monitor System

  # Simulate orders
  - name: Receive Order
    args:
      orderId: "ORD-001"
      customer: "Acme Corp"
      items: [{ sku: "A1", qty: 2 }]
      total: 500

  - name: Receive Order
    args:
      orderId: "ORD-002"
      customer: "Big Company"
      items: [{ sku: "B1", qty: 50 }]
      total: 5000
```

---

## See Also

- [oJob Director](ojob-director.md) - Distributed job coordination
- [oJob Basics](common-browse.md) - Basic oJob utilities
- [oJob Reference](../../concepts/oJob.html)
- [OpenAF Channels](../../concepts/OpenAF-Channels.html)
