---
layout: default
title: oJob WatchDog
parent: oJob
grand_parent: Guides
---

# oJob WatchDog - Process Monitoring and Auto-Recovery

The oJob WatchDog provides automated monitoring and restart capabilities for daemon processes, checking process health through multiple methods and performing recovery actions when issues are detected.

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## Overview

oJob WatchDog enables:
- **PID-based monitoring** - Check if process is running
- **Log file monitoring** - Detect error patterns in logs
- **Custom health checks** - Execute custom validation logic
- **Automatic restart** - Stop and start services when issues detected
- **Scheduled checks** - Run via cron for continuous monitoring

### Use Cases

- Monitor daemon processes and restart on failure
- Detect fatal errors in log files and recover
- Check application responsiveness
- Implement custom health checks
- Build high-availability process management

---

## Getting Started

### Basic WatchDog Setup

```yaml
include:
  - oJobWatchDog.yaml

ojob:
  # Run as cron job (every 5 minutes)
  logToFile:
    logFolder: ./logs/watchdog
  logToConsole: false
  unique:
    pidFile: /var/run/mywatchdog.pid

jobs:
  - name: Monitor My Service
    to: oJob WatchDog
    args:
      # Check PID file
      checks:
        pid:
          file: /var/run/myservice.pid

      # Restart commands
      cmdToStart: systemctl start myservice
      cmdToStop: systemctl stop myservice

      # Wait times
      waitAfterStop: 2000
      waitAfterStart: 5000

      quiet: false

todo:
  - Monitor My Service
```

---

## Configuration Arguments

### Check Configuration

| Argument | Type | Description |
|----------|------|-------------|
| `checks` | Map | Map containing check configurations |
| `checks.pid.file` | String | Path to PID file to monitor |
| `checks.log.folder` | String | Folder containing log files |
| `checks.log.fileRE` | String | Regex to match log file names |
| `checks.log.stringRE` | String/Array | Regex patterns to find in logs (triggers restart) |
| `checks.log.histFile` | String | File to store history of findings |
| `checks.log.olderMin` | Number | Alert if log file older than N minutes |
| `checks.custom.exec` | String | Custom JavaScript code returning true/false |

### Action Configuration

| Argument | Type | Description |
|----------|------|-------------|
| `cmdToStop` | String | Command to stop the service |
| `execToStop` | String | JavaScript code to execute on stop |
| `jobToStop` | String | Job name to execute on stop |
| `waitAfterStop` | Number | Milliseconds to wait after stopping |
| `workDirStop` | String | Working directory for stop command |
| `timeoutStop` | Number | Timeout for stop command |
| `exitCodeStop` | Number | Expected exit code for stop command |
| `cmdToStart` | String | Command to start the service |
| `execToStart` | String | JavaScript code to execute on start |
| `jobToStart` | String | Job name to execute on start |
| `waitAfterStart` | Number | Milliseconds to wait after starting |
| `workDirStart` | String | Working directory for start command |
| `timeoutStart` | Number | Timeout for start command |
| `exitCodeStart` | Number | Expected exit code for start command |
| `quiet` | Boolean | Only log when issues detected (default: true) |

---

## Check Types

### PID File Check

Monitors a PID file and checks if the process is running.

```yaml
jobs:
  - name: Watch with PID
    to: oJob WatchDog
    args:
      checks:
        pid:
          file: /var/run/myapp.pid

      cmdToStart: /opt/myapp/bin/start.sh
      cmdToStop: /opt/myapp/bin/stop.sh
      waitAfterStart: 5000
```

**How it works:**
1. Reads PID from file
2. Checks if process exists with that PID
3. If not running → triggers stop & start

### Log File Monitoring

Monitors log files for error patterns.

```yaml
jobs:
  - name: Watch Logs
    to: oJob WatchDog
    args:
      checks:
        log:
          folder: /var/log/myapp
          fileRE: "app-\\d{4}-\\d{2}-\\d{2}\\.log"
          stringRE:
            - "OutOfMemoryError"
            - "FATAL"
            - "Database connection failed"
          histFile: /var/lib/watchdog/myapp-history.json
          olderMin: 10  # Alert if log older than 10 minutes

      cmdToStart: systemctl start myapp
      cmdToStop: systemctl stop myapp
```

**How it works:**
1. Finds latest log file matching `fileRE`
2. Searches for patterns in `stringRE`
3. Checks against `histFile` to avoid duplicate alerts
4. If pattern found → triggers restart
5. If log older than `olderMin` → triggers restart

### Custom Health Check

Execute custom validation logic.

```yaml
jobs:
  - name: Watch with Custom Check
    to: oJob WatchDog
    args:
      checks:
        custom:
          exec: |
            ow.loadObj();

            try {
              // Check HTTP endpoint
              var response = $rest()
                .get("http://localhost:8080/health")
                .getResponse();

              if (response.status != 200) {
                log("Health check failed: status " + response.status);
                return false;
              }

              // Check response content
              if (response.data.status != "healthy") {
                log("Service reports unhealthy status");
                return false;
              }

              // All checks passed
              return true;

            } catch(e) {
              logErr("Health check error: " + e.message);
              return false;
            }

      cmdToStart: docker start myapp
      cmdToStop: docker stop myapp
      waitAfterStop: 3000
      waitAfterStart: 10000
```

**Custom check returns:**
- `true` = Service is healthy, no action
- `false` = Service is unhealthy, trigger restart

---

## Common Patterns

### Pattern 1: Application Server Monitoring

```yaml
include:
  - oJobWatchDog.yaml

ojob:
  logToFile:
    logFolder: /var/log/watchdog
    HKhowLongAgoInMinutes: 10080  # Keep 1 week
  logToConsole: false
  unique:
    pidFile: /var/run/watchdog-appserver.pid
  checkStall:
    everySeconds: 30
    killAfterSeconds: 300

jobs:
  - name: Watch Application Server
    to: oJob WatchDog
    args:
      checks:
        pid:
          file: /opt/appserver/run/app.pid

        log:
          folder: /opt/appserver/logs
          fileRE: "server-\\d{4}-\\d{2}-\\d{2}\\.log"
          stringRE:
            - "OutOfMemoryError"
            - "StackOverflowError"
            - "Could not initialize class"
            - "FATAL"
          histFile: /var/lib/watchdog/appserver-hist.json
          olderMin: 15

        custom:
          exec: |
            // Check HTTP health endpoint
            ow.loadObj();
            try {
              var res = $rest({ throwExceptions: false })
                .get("http://localhost:8080/actuator/health")
                .getResponse();
              return (res.status == 200);
            } catch(e) {
              return false;
            }

      cmdToStop: /opt/appserver/bin/shutdown.sh
      workDirStop: /opt/appserver
      timeoutStop: 30000
      waitAfterStop: 5000

      cmdToStart: /opt/appserver/bin/startup.sh
      workDirStart: /opt/appserver
      timeoutStart: 60000
      waitAfterStart: 15000

      quiet: false

todo:
  - Watch Application Server
```

### Pattern 2: Database Process Monitoring

```yaml
include:
  - oJobWatchDog.yaml

jobs:
  - name: Watch Database
    to: oJob WatchDog
    args:
      checks:
        pid:
          file: /var/lib/postgresql/postmaster.pid

        custom:
          exec: |
            // Try to connect to database
            plugin("DB");
            try {
              var db = new DB(
                "jdbc:postgresql://localhost:5432/testdb",
                "dbuser",
                "dbpass"
              );
              db.q("SELECT 1");
              db.close();
              return true;
            } catch(e) {
              logErr("Database connection failed: " + e.message);
              return false;
            }

      cmdToStop: systemctl stop postgresql
      waitAfterStop: 5000

      cmdToStart: systemctl start postgresql
      waitAfterStart: 10000
```

### Pattern 3: Docker Container Monitoring

```yaml
include:
  - oJobWatchDog.yaml

jobs:
  - name: Watch Docker Container
    to: oJob WatchDog
    args:
      checks:
        custom:
          exec: |
            // Check container status
            var containerName = "myapp-container";

            var res = sh("docker ps --filter name=" + containerName + " --format '{{.Status}}'");

            if (res.stdout.indexOf("Up") < 0) {
              log("Container not running: " + containerName);
              return false;
            }

            // Check container health
            var health = sh("docker inspect --format='{{.State.Health.Status}}' " + containerName);

            if (health.stdout.trim() == "unhealthy") {
              log("Container unhealthy: " + containerName);
              return false;
            }

            return true;

      cmdToStop: docker stop myapp-container
      waitAfterStop: 5000

      cmdToStart: docker start myapp-container
      waitAfterStart: 10000
```

### Pattern 4: Multi-Service Monitoring

```yaml
include:
  - oJobWatchDog.yaml

jobs:
  # Monitor web server
  - name: Watch Web Server
    to: oJob WatchDog
    args:
      checks:
        pid:
          file: /var/run/nginx.pid
        custom:
          exec: |
            try {
              return $rest().get("http://localhost:80").getResponse().status == 200;
            } catch(e) {
              return false;
            }
      cmdToStart: systemctl start nginx
      cmdToStop: systemctl stop nginx

  # Monitor application
  - name: Watch Application
    to: oJob WatchDog
    args:
      checks:
        pid:
          file: /var/run/app.pid
        log:
          folder: /var/log/app
          fileRE: "app\\.log"
          stringRE: "FATAL"
      cmdToStart: systemctl start myapp
      cmdToStop: systemctl stop myapp

  # Monitor database
  - name: Watch Database
    to: oJob WatchDog
    args:
      checks:
        custom:
          exec: |
            try {
              return sh("pg_isready").exitcode == 0;
            } catch(e) {
              return false;
            }
      cmdToStart: systemctl start postgresql
      cmdToStop: systemctl stop postgresql

todo:
  - Watch Web Server
  - Watch Application
  - Watch Database
```

### Pattern 5: Advanced Stop/Start with Jobs

```yaml
include:
  - oJobWatchDog.yaml

jobs:
  # Custom stop logic
  - name: Custom Stop Service
    exec: |
      log("Graceful shutdown initiated");

      // Save state
      $ch("service-state").set("shutdown", {
        time: nowUTC(),
        reason: "watchdog"
      });

      // Notify monitoring
      notifyMonitoring("Service stopping");

      // Stop service
      sh("systemctl stop myservice");

      log("Service stopped");

  # Custom start logic
  - name: Custom Start Service
    exec: |
      log("Starting service");

      // Pre-start checks
      if (!io.fileExists("/opt/service/config.yml")) {
        throw "Config file missing";
      }

      // Start service
      sh("systemctl start myservice");

      // Wait for ready
      var ready = false;
      var attempts = 0;
      while (!ready && attempts < 30) {
        sleep(1000, true);
        try {
          ready = $rest().get("http://localhost:8080/health")
            .getResponse().status == 200;
        } catch(e) {}
        attempts++;
      }

      if (!ready) {
        throw "Service failed to become ready";
      }

      log("Service started and ready");

      // Notify monitoring
      notifyMonitoring("Service started");

  # WatchDog using custom jobs
  - name: Watch Service
    to: oJob WatchDog
    args:
      checks:
        pid:
          file: /var/run/myservice.pid

      jobToStop: Custom Stop Service
      waitAfterStop: 2000

      jobToStart: Custom Start Service
      waitAfterStart: 5000

todo:
  - Watch Service
```

---

## Cron Integration

### Run Every 5 Minutes

```bash
# crontab -e
*/5 * * * * cd /opt/watchdog && ojob watchdog.yaml
```

### Run Every Minute (More Responsive)

```bash
# crontab -e
* * * * * cd /opt/watchdog && ojob watchdog.yaml
```

### Run with Environment

```bash
# crontab -e
*/5 * * * * cd /opt/watchdog && source /etc/profile && ojob watchdog.yaml
```

---

## Logging and Notifications

### Log to File

```yaml
ojob:
  logToFile:
    logFolder: /var/log/watchdog
    HKhowLongAgoInMinutes: 10080  # Keep 1 week
    setLogOff: false
  logToConsole: false
  logJobs: false
```

### Send Email Notifications

```yaml
include:
  - oJobWatchDog.yaml
  - oJobEmail.yaml

jobs:
  - name: Watch with Email Alerts
    exec: |
      # Run watchdog check
      var checkPassed = true;

      try {
        $job("oJob WatchDog", {
          checks: {
            pid: { file: "/var/run/myapp.pid" }
          },
          cmdToStart: "systemctl start myapp",
          cmdToStop: "systemctl stop myapp"
        });
      } catch(e) {
        checkPassed = false;

        # Send alert email
        $job("oJob Send email", {
          server: getEnv("SMTP_SERVER"),
          from: "watchdog@example.com",
          to: ["admin@example.com"],
          subject: "WatchDog Alert: Service Restarted",
          output: "The watchdog has detected an issue and restarted myapp.\n\nError: " + e.message
        });
      }
```

### Slack Notifications

```yaml
jobs:
  - name: Notify Slack
    exec: |
      ow.loadObj();

      $rest().post("https://hooks.slack.com/services/YOUR/WEBHOOK/URL", {
        text: ":warning: WatchDog Alert",
        blocks: [{
          type: "section",
          text: {
            type: "mrkdwn",
            text: "*Service*: " + args.service + "\n*Action*: " + args.action + "\n*Time*: " + new Date()
          }
        }]
      });

  - name: Watch with Slack
    exec: |
      try {
        $job("oJob WatchDog", {
          checks: { pid: { file: "/var/run/myapp.pid" }},
          cmdToStart: "systemctl start myapp",
          cmdToStop: "systemctl stop myapp"
        });
      } catch(e) {
        $job("Notify Slack", {
          service: "myapp",
          action: "restarted"
        });
      }
```

---

## Best Practices

### 1. Use Unique PID Files

Ensure the watchdog itself doesn't run multiple times:

```yaml
ojob:
  unique:
    pidFile: /var/run/watchdog-myservice.pid
    killPrevious: false
```

### 2. Implement Stall Detection

Prevent watchdog from hanging:

```yaml
ojob:
  checkStall:
    everySeconds: 30
    killAfterSeconds: 300
```

### 3. Use Appropriate Wait Times

```yaml
args:
  waitAfterStop: 5000    # Allow process to fully stop
  waitAfterStart: 15000  # Allow service to initialize
```

### 4. Test Your Commands

```bash
# Test stop command
/opt/myapp/bin/stop.sh

# Test start command
/opt/myapp/bin/start.sh

# Verify they work before using in watchdog
```

### 5. Monitor the Watchdog

```yaml
jobs:
  - name: Watchdog Health
    exec: |
      # Send periodic heartbeat
      io.writeFileString("/var/run/watchdog-heartbeat.txt", new Date().toISOString());
```

### 6. Use History Files for Log Monitoring

```yaml
args:
  checks:
    log:
      histFile: /var/lib/watchdog/history.json
```

This prevents reacting to the same error multiple times.

### 7. Combine Multiple Checks

```yaml
args:
  checks:
    pid:
      file: /var/run/app.pid
    log:
      folder: /var/log/app
      stringRE: "FATAL"
    custom:
      exec: |
        # Custom health check
        return checkHealth();
```

---

## Troubleshooting

### WatchDog Not Running

Check cron logs:
```bash
grep CRON /var/log/syslog
```

Check watchdog logs:
```bash
tail -f /var/log/watchdog/*.log
```

### Service Not Restarting

Enable verbose logging:
```yaml
args:
  quiet: false
```

Check command output:
```yaml
args:
  cmdToStart: bash -x /path/to/start.sh  # Debug mode
```

### Multiple Restarts

Check for overly sensitive checks:
```yaml
args:
  checks:
    log:
      histFile: /var/lib/watchdog/history.json  # Prevents duplicates
```

Add cooldown period:
```yaml
jobs:
  - name: Watch with Cooldown
    exec: |
      var lastRestart = $ch("watchdog-state").get("lastRestart") || 0;
      var now = new Date().getTime();

      if (now - lastRestart < 300000) {  # 5 minutes
        log("Cooldown active, skipping check");
        return;
      }

      $job("oJob WatchDog", { ... });

      $ch("watchdog-state").set("lastRestart", now);
```

---

## Complete Example

```yaml
include:
  - oJobWatchDog.yaml

ojob:
  logToFile:
    logFolder: /var/log/watchdog/myapp
    HKhowLongAgoInMinutes: 10080
  logToConsole: false
  logJobs: false
  unique:
    pidFile: /var/run/watchdog-myapp.pid
    killPrevious: false
  checkStall:
    everySeconds: 30
    killAfterSeconds: 180

jobs:
  - name: Monitor My Application
    to: oJob WatchDog
    args:
      # Multiple check types
      checks:
        pid:
          file: /opt/myapp/run/app.pid

        log:
          folder: /opt/myapp/logs
          fileRE: "application-\\d{4}-\\d{2}-\\d{2}\\.log"
          stringRE:
            - "OutOfMemoryError"
            - "FATAL ERROR"
            - "Unable to connect to database"
          histFile: /var/lib/watchdog/myapp-errors.json
          olderMin: 10

        custom:
          exec: |
            ow.loadObj();
            try {
              var health = $rest({ timeout: 5000 })
                .get("http://localhost:8080/health")
                .getResponse();

              return (health.status == 200 && health.data.status == "UP");
            } catch(e) {
              logErr("Health check failed: " + e.message);
              return false;
            }

      # Stop procedure
      execToStop: |
        log("Initiating graceful shutdown");
        sh("/opt/myapp/bin/shutdown.sh");
      waitAfterStop: 10000
      timeoutStop: 30000

      # Start procedure
      execToStart: |
        log("Starting application");
        sh("/opt/myapp/bin/startup.sh");

        # Wait for application to be ready
        var ready = false;
        for (var i = 0; i < 60 && !ready; i++) {
          sleep(1000, true);
          try {
            ready = $rest().get("http://localhost:8080/health")
              .getResponse().status == 200;
          } catch(e) {}
        }

        if (!ready) {
          logErr("Application failed to start within 60 seconds");
        } else {
          log("Application started successfully");
        }
      waitAfterStart: 5000
      timeoutStart: 90000

      quiet: false

todo:
  - Monitor My Application
```

---

## See Also

- [oJob Basics](common-browse.md) - Basic oJob utilities
- [oJob Reference](../../concepts/oJob.html)
- [OpenAF Channels](../../concepts/OpenAF-Channels.html)
