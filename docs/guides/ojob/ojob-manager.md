---
layout: default
title: oJob Manager
parent: oJob
grand_parent: Guides
---

# oJob Manager - Container Job Coordination

The oJob Manager provides job execution coordination with locking mechanisms, preventing concurrent execution of the same job and tracking job execution status across distributed systems.

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## Overview

oJob Manager enables:
- **Job execution locking** - Prevent concurrent execution
- **Status tracking** - Monitor job start/end times
- **Error handling** - Track job failures
- **Distributed coordination** - Works across multiple instances
- **Container job management** - Launch jobs dynamically

### Use Cases

- Prevent duplicate job execution in clustered environments
- Track long-running job execution
- Coordinate scheduled jobs across multiple servers
- Monitor job execution history
- Manage containerized job workflows

---

## Getting Started

### Basic Job Management

```yaml
include:
  - oJobManager.yaml

jobs:
  - name: Managed Job
    from:
      - oJobManager Job Start
    to:
      - oJobManager Job End
    catch:
      - oJobManager Error
    args:
      name: my-unique-job
      timeout: 3600000  # 1 hour
    exec: |
      log("Job is running - protected by lock");

      // Your job logic here
      sleep(5000, true);

      log("Job completed");

todo:
  - oJobManager Init
  - Managed Job
```

---

## Jobs Reference

### oJobManager Init

Initializes the oJob Manager system, creating channels for job tracking and locking.

**Arguments:**

| Argument | Type | Default | Description |
|----------|------|---------|-------------|
| `chJobs` | Map | `{type:"simple", args:{}}` | Channel configuration for job tracking |
| `chLocks` | Map | `{type:"simple", args:{}}` | Channel configuration for locking |

**Creates:**
- `oJobManager-jobs` channel - Tracks job execution status
- `oJobManager-locks` channel - Manages job locks
- `global.oJobManagerLaunchJob(jobName, args)` - Function to launch jobs dynamically

**Example:**

```yaml
jobs:
  - name: Init Manager
    to: oJobManager Init
    args:
      # Use file-based channels for persistence
      chJobs:
        type: "db"
        args:
          file: "./data/jobs.db"
      chLocks:
        type: "db"
        args:
          file: "./data/locks.db"
```

---

### oJobManager Job Start

Registers and locks a job before execution. Use with `from` directive.

**Arguments:**

| Argument | Type | Required | Default | Description |
|----------|------|----------|---------|-------------|
| `name` | String | Yes | - | Unique job container name |
| `timeout` | Number | No | 3600000 (1 hour) | Lock timeout in milliseconds |

**Process:**
1. Adds job to internal tracking list
2. Attempts to acquire lock
3. Records job start time
4. Throws error if lock cannot be acquired

**Example:**

```yaml
jobs:
  - name: My Protected Job
    from: oJobManager Job Start
    args:
      name: data-processor
      timeout: 1800000  # 30 minutes
    exec: |
      // Job logic
```

---

### oJobManager Job End

Unregisters and unlocks a job after execution. Use with `to` directive.

**Arguments:**

| Argument | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | String | Yes | Unique job container name (must match Job Start) |

**Process:**
1. Retrieves job information
2. Unlocks the job
3. Records job end time
4. Updates job status to completed

**Example:**

```yaml
jobs:
  - name: My Protected Job
    to: oJobManager Job End
    args:
      name: data-processor
    exec: |
      // Job logic
```

---

### oJobManager Error

Handles job errors, unlocking and recording failure status. Use with `catch` directive.

**Arguments:** None (uses context from Job Start)

**Process:**
1. Unlocks all jobs in tracking list
2. Records error information
3. Updates job status with error details

**Example:**

```yaml
jobs:
  - name: My Protected Job
    catch: oJobManager Error
    exec: |
      // Job logic that might fail
```

---

## Common Patterns

### Pattern 1: Basic Managed Job

```yaml
include:
  - oJobManager.yaml

jobs:
  # Initialize manager
  - name: Init
    to: oJobManager Init

  # Managed job with full lifecycle
  - name: Process Data
    from: oJobManager Job Start
    to: oJobManager Job End
    catch: oJobManager Error
    args:
      name: daily-data-processor
      timeout: 7200000  # 2 hours
    exec: |
      log("Processing daily data");

      // Load data
      var data = loadData();

      // Process
      var results = processData(data);

      // Save results
      saveResults(results);

      log("Data processing completed");

todo:
  - Init
  - Process Data
```

### Pattern 2: Scheduled Job with Protection

```yaml
include:
  - oJobManager.yaml

ojob:
  daemon: true

jobs:
  - name: Init Manager
    to: oJobManager Init

  # Runs every hour but won't overlap
  - name: Hourly Cleanup
    typeArgs:
      cron: "0 * * * *"
    from: oJobManager Job Start
    to: oJobManager Job End
    catch: oJobManager Error
    args:
      name: hourly-cleanup
      timeout: 3000000  # 50 minutes (less than 1 hour)
    exec: |
      log("Running cleanup");

      // Cleanup logic
      cleanupOldFiles();
      cleanupExpiredSessions();
      cleanupLogs();

      log("Cleanup completed");

todo:
  - Init Manager
  - Hourly Cleanup
```

### Pattern 3: Distributed Channel Storage

```yaml
include:
  - oJobManager.yaml

jobs:
  # Use Ignite for distributed locking
  - name: Init Distributed Manager
    to: oJobManager Init
    args:
      chJobs:
        type: "ignite"
        args:
          gridName: "jobGrid"
          cacheName: "jobs"
      chLocks:
        type: "ignite"
        args:
          gridName: "jobGrid"
          cacheName: "locks"

  # Multiple instances can run this - only one executes
  - name: Process Orders
    from: oJobManager Job Start
    to: oJobManager Job End
    catch: oJobManager Error
    args:
      name: order-processor
      timeout: 600000  # 10 minutes
    exec: |
      log("Processing orders - instance: " + getEnv("INSTANCE_ID"));

      // Process orders
      var orders = getOrders();
      orders.forEach(order => processOrder(order));

      log("Orders processed");

todo:
  - Init Distributed Manager
  - Process Orders
```

### Pattern 4: Dynamic Job Launching

```yaml
include:
  - oJobManager.yaml

jobs:
  - name: Init
    to: oJobManager Init

  # Parent job that launches child jobs
  - name: Process Batches
    exec: |
      var batches = [
        { batchId: "batch-001", items: [...] },
        { batchId: "batch-002", items: [...] },
        { batchId: "batch-003", items: [...] }
      ];

      batches.forEach(batch => {
        // Launch job dynamically
        global.oJobManagerLaunchJob("Process Batch", batch);
      });

  # Child job that gets launched
  - name: Process Batch
    from: oJobManager Job Start
    to: oJobManager Job End
    catch: oJobManager Error
    args:
      name: "batch-{{batchId}}"
      timeout: 1800000
    exec: |
      log("Processing batch: " + args.batchId);

      args.items.forEach(item => {
        processItem(item);
      });

      log("Batch completed: " + args.batchId);

todo:
  - Init
  - Process Batches
```

### Pattern 5: Job Status Monitoring

```yaml
include:
  - oJobManager.yaml

jobs:
  - name: Init
    to: oJobManager Init

  # Monitor job status
  - name: Monitor Jobs
    typeArgs:
      cron: "*/5 * * * *"  # Every 5 minutes
    exec: |
      var jobs = $ch("oJobManager-jobs").getAll();

      log("Active Jobs: " + jobs.length);

      jobs.forEach(job => {
        var duration = isDef(job.endTime)
          ? (job.endTime - job.startTime)
          : (nowUTC() - job.startTime);

        var status = isDef(job.endTime)
          ? (job.inError ? "ERROR" : "COMPLETED")
          : "RUNNING";

        log(
          "Job: " + job.name +
          " | Status: " + status +
          " | Duration: " + Math.round(duration / 1000) + "s"
        );

        // Alert on long-running jobs
        if (status == "RUNNING" && duration > 3600000) {
          logWarn("Long-running job detected: " + job.name);
        }
      });

  # Cleanup old job records
  - name: Cleanup Old Records
    exec: |
      var cutoff = nowUTC() - (24 * 60 * 60 * 1000);  // 24 hours

      var jobs = $ch("oJobManager-jobs").getAll();

      jobs.forEach(job => {
        if (isDef(job.endTime) && job.endTime < cutoff) {
          $ch("oJobManager-jobs").unset({
            name: job.name,
            startTime: job.startTime
          });
        }
      });

todo:
  - Init
  - Monitor Jobs
```

---

## Error Handling

### Automatic Error Handling

```yaml
jobs:
  - name: Safe Job
    from: oJobManager Job Start
    to: oJobManager Job End
    catch: oJobManager Error  # Automatically handles errors
    args:
      name: safe-job
    exec: |
      // This error will be caught and recorded
      if (someCondition) {
        throw "Job failed due to condition";
      }

      // Job logic
```

### Custom Error Handling

```yaml
jobs:
  - name: Custom Error Job
    from: oJobManager Job Start
    args:
      name: custom-error-job
    exec: |
      try {
        // Job logic
        riskyOperation();

        // Manual end on success
        $job("oJobManager Job End", { name: args.name });

      } catch(e) {
        logErr("Job failed: " + e.message);

        // Custom error handling
        sendAlert("Job failed: " + args.name);

        // Manual error handling
        $job("oJobManager Error", { name: args.name, e: e });

        throw e;
      }
```

---

## Job Status Tracking

### Query Job Status

```yaml
jobs:
  - name: Check Job Status
    exec: |
      var jobName = "my-job";

      // Get current job status
      var jobs = $ch("oJobManager-jobs").getAll();
      var myJob = jobs.filter(j => j.name == jobName)[0];

      if (isDef(myJob)) {
        print("Job: " + myJob.name);
        print("Started: " + myJob.startDate);

        if (isDef(myJob.endTime)) {
          print("Ended: " + myJob.endDate);
          print("Duration: " + (myJob.endTime - myJob.startTime) + "ms");
          print("Status: " + (myJob.inError ? "Failed" : "Success"));

          if (myJob.inError) {
            print("Error: " + myJob.error);
          }
        } else {
          print("Status: Running");
          print("Running for: " + (nowUTC() - myJob.startTime) + "ms");
        }
      } else {
        print("Job not found or not running");
      }
```

### Job History Report

```yaml
jobs:
  - name: Job History
    exec: |
      var jobs = $ch("oJobManager-jobs").getAll();

      // Group by job name
      var grouped = $from(jobs)
        .groupBy("name")
        .select(g => ({
          name: g.key,
          totalRuns: g.items.length,
          successfulRuns: g.items.filter(j => !j.inError).length,
          failedRuns: g.items.filter(j => j.inError).length,
          avgDuration: $from(g.items)
            .filter("endTime")
            .average("endTime", "startTime")
        }))

      print(af.toYAML(grouped));
```

---

## Advanced Techniques

### Timeout Handling

```yaml
jobs:
  - name: Job with Timeout
    from: oJobManager Job Start
    to: oJobManager Job End
    catch: oJobManager Error
    args:
      name: timeout-job
      timeout: 300000  # 5 minutes
    exec: |
      var startTime = nowUTC();
      var timeout = args.timeout || 300000;

      // Long-running operation
      while (hasMoreWork()) {
        // Check timeout
        if (nowUTC() - startTime > timeout - 10000) {
          logWarn("Job approaching timeout, stopping gracefully");
          break;
        }

        doWork();
      }
```

### Conditional Job Execution

```yaml
jobs:
  - name: Conditional Job
    exec: |
      // Check if job is already running
      var jobs = $ch("oJobManager-jobs").getAll();
      var running = jobs.filter(j =>
        j.name == "my-job" && isUnDef(j.endTime)
      );

      if (running.length > 0) {
        log("Job already running, skipping");
        return;
      }

      // Start job
      $job("My Protected Job");
```

### Job Dependencies

```yaml
jobs:
  - name: Job A
    from: oJobManager Job Start
    to: oJobManager Job End
    catch: oJobManager Error
    args:
      name: job-a
    exec: |
      // Job A logic

  - name: Job B
    deps:
      - Job A  # Waits for Job A to complete
    from: oJobManager Job Start
    to: oJobManager Job End
    catch: oJobManager Error
    args:
      name: job-b
    exec: |
      // Job B logic (runs after Job A)
```

---

## Complete Example: Batch Processing System

```yaml
include:
  - oJobManager.yaml
  - oJobBasics.yaml

ojob:
  daemon: true
  logToFile:
    logFolder: ./logs

jobs:
  # Initialize manager with persistent channels
  - name: Init System
    to: oJobManager Init
    args:
      chJobs:
        type: "db"
        args:
          file: "./data/jobs.db"
      chLocks:
        type: "db"
        args:
          file: "./data/locks.db"

  # Main batch coordinator
  - name: Batch Coordinator
    typeArgs:
      cron: "0 2 * * *"  # 2 AM daily
    exec: |
      log("Starting daily batch processing");

      // Launch batch jobs
      global.oJobManagerLaunchJob("Extract Data");
      global.oJobManagerLaunchJob("Transform Data");
      global.oJobManagerLaunchJob("Load Data");

  # Extract phase
  - name: Extract Data
    from: oJobManager Job Start
    to: oJobManager Job End
    catch: oJobManager Error
    args:
      name: extract-data
      timeout: 1800000  # 30 minutes
    exec: |
      log("Extracting data from sources");

      // Extract logic
      var data = extractFromDatabase();
      saveToStaging(data, "extracted");

      log("Data extraction completed");

  # Transform phase
  - name: Transform Data
    deps:
      - Extract Data
    from: oJobManager Job Start
    to: oJobManager Job End
    catch: oJobManager Error
    args:
      name: transform-data
      timeout: 3600000  # 1 hour
    exec: |
      log("Transforming data");

      // Transform logic
      var data = loadFromStaging("extracted");
      var transformed = transformData(data);
      saveToStaging(transformed, "transformed");

      log("Data transformation completed");

  # Load phase
  - name: Load Data
    deps:
      - Transform Data
    from: oJobManager Job Start
    to: oJobManager Job End
    catch: oJobManager Error
    args:
      name: load-data
      timeout: 1800000  # 30 minutes
    exec: |
      log("Loading data to target");

      // Load logic
      var data = loadFromStaging("transformed");
      loadToTarget(data);

      log("Data load completed");

  # Monitor batch progress
  - name: Monitor Batch
    typeArgs:
      cron: "*/10 * * * *"  # Every 10 minutes
    exec: |
      var jobs = $ch("oJobManager-jobs").getAll();

      var batchJobs = jobs.filter(j =>
        j.name.indexOf("extract") >= 0 ||
        j.name.indexOf("transform") >= 0 ||
        j.name.indexOf("load") >= 0
      );

      if (batchJobs.length > 0) {
        log("Batch Status:");

        batchJobs.forEach(job => {
          var status = isDef(job.endTime)
            ? (job.inError ? "FAILED" : "COMPLETED")
            : "RUNNING";

          var duration = isDef(job.endTime)
            ? (job.endTime - job.startTime)
            : (nowUTC() - job.startTime);

          log("  " + job.name + ": " + status +
              " (" + Math.round(duration / 1000) + "s)");
        });
      }

  # Daily cleanup
  - name: Cleanup Old Jobs
    typeArgs:
      cron: "0 3 * * *"  # 3 AM daily
    exec: |
      var cutoff = nowUTC() - (7 * 24 * 60 * 60 * 1000);  // 7 days

      var jobs = $ch("oJobManager-jobs").getAll();
      var removed = 0;

      jobs.forEach(job => {
        if (isDef(job.endTime) && job.endTime < cutoff) {
          $ch("oJobManager-jobs").unset({
            name: job.name,
            startTime: job.startTime
          });
          removed++;
        }
      });

      log("Removed " + removed + " old job records");

todo:
  - Init System
  - Batch Coordinator
  - Monitor Batch
  - Cleanup Old Jobs
```

---

## Best Practices

### 1. Use Meaningful Job Names

```yaml
# Good - descriptive and unique
name: customer-data-sync-{{customerId}}
name: daily-report-generator

# Bad - generic
name: job1
name: process
```

### 2. Set Appropriate Timeouts

```yaml
# Short jobs
timeout: 300000  # 5 minutes

# Long-running jobs
timeout: 7200000  # 2 hours

# Very long jobs
timeout: 14400000  # 4 hours
```

### 3. Always Use Error Handling

```yaml
catch: oJobManager Error  # Required for proper cleanup
```

### 4. Clean Up Old Records

```yaml
# Regularly remove completed job records
jobs:
  - name: Cleanup
    typeArgs:
      cron: "0 4 * * *"
    exec: |
      cleanupOldJobRecords();
```

### 5. Monitor Job Health

```yaml
# Regular monitoring
jobs:
  - name: Health Check
    typeArgs:
      cron: "*/15 * * * *"
    exec: |
      checkForStuckJobs();
      alertOnLongRunning();
```

---

## Troubleshooting

### Job Won't Start (Lock Acquisition Fails)

**Problem:** Job throws "Can't lock to execute job" error

**Solutions:**
1. Check if another instance is running the job
2. Verify lock timeout hasn't expired
3. Check channel connectivity
4. Manually unlock if stuck:

```yaml
jobs:
  - name: Force Unlock
    exec: |
      if (isDef(global.__oJobManager)) {
        global.__oJobManager.jobLocks.unlock(args.jobName);
        log("Unlocked: " + args.jobName);
      }
```

### Jobs Not Completing

**Problem:** Jobs remain in "running" state

**Solutions:**
1. Ensure `oJobManager Job End` is called
2. Check for exceptions that bypass the `to` clause
3. Use `catch` to handle errors properly

### Channel Issues

**Problem:** Jobs not tracked across restarts

**Solutions:**
Use persistent channels:

```yaml
chJobs:
  type: "db"
  args:
    file: "./jobs.db"
```

---

## See Also

- [oJob Director](ojob-director.md) - Distributed job coordination
- [oJob Queue](ojob-queue.md) - Queue-based processing
- [oJob Basics](common-browse.md)
- [OpenAF Channels](../../concepts/OpenAF-Channels.html)
