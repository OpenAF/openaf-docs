---
layout: default
title: oJob GIT
parent: oJob
grand_parent: Guides
---

# oJob GIT - Git Repository Operations

The oJob GIT utilities provide easy git repository cloning and copying operations within oJob workflows, enabling automated repository management and deployment.

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## Overview

oJob GIT enables:
- **Clone git repositories** to local folders
- **Copy repository files** without git metadata
- **Branch-specific checkouts** for deployment
- **Authenticated access** to private repositories
- **Automated deployment workflows**

### Use Cases

- Deploy code from git repositories
- Download repository files for processing
- Automated release workflows
- Repository synchronization
- CI/CD pipeline integration

---

## Getting Started

### Basic Repository Copy

```yaml
include:
  - oJobGIT.yaml

jobs:
  - name: Download Repository
    to: GIT Copy Repository
    args:
      giturl: https://github.com/OpenAF/openaf-templates
      gittarget: ./templates

todo:
  - Download Repository
```

---

## Jobs Reference

### GIT Copy Repository

Clones a git repository and copies the files (without `.git` directory) to a target folder.

**Arguments:**

| Argument | Type | Required | Default | Description |
|----------|------|----------|---------|-------------|
| `giturl` | String | Yes | - | Git repository URL |
| `gittarget` | String | Yes | - | Target folder for repository files |
| `gittemp` | String | No | `gittarget + ".tmp"` | Temporary clone folder |
| `gitbranch` | String | No | `undefined` (default branch) | Specific branch to checkout |
| `gituser` | String | No | - | Username for private repositories |
| `gitpass` | String | No | - | Password for private repositories (can be encrypted) |

**Process:**
1. Creates temporary and target folders
2. Clones repository to temporary folder
3. Removes `.git` directory
4. Moves files to target folder
5. Cleans up temporary folder

**Example:**

```yaml
jobs:
  - name: Clone Specific Branch
    to: GIT Copy Repository
    args:
      giturl: https://github.com/myorg/myrepo
      gittarget: ./deployment
      gitbranch: release-v2.0
```

---

## Common Patterns

### Pattern 1: Deploy from Git

```yaml
include:
  - oJobGIT.yaml

jobs:
  # Download repository
  - name: Download Code
    to: GIT Copy Repository
    args:
      giturl: https://github.com/myorg/myapp
      gittarget: /opt/myapp
      gitbranch: main

  # Post-deployment tasks
  - name: Install Dependencies
    deps:
      - Download Code
    exec: |
      sh("cd /opt/myapp && npm install");

  - name: Start Application
    deps:
      - Install Dependencies
    exec: |
      sh("cd /opt/myapp && npm start");

todo:
  - Download Code
  - Install Dependencies
  - Start Application
```

### Pattern 2: Private Repository Access

```yaml
include:
  - oJobGIT.yaml

jobs:
  - name: Clone Private Repo
    to: GIT Copy Repository
    args:
      giturl: https://github.com/myorg/private-repo
      gittarget: ./private-code
      gituser: "{{gitUsername}}"
      gitpass: "{{gitPassword}}"

todo:
  - name: Clone Private Repo
    args:
      gitUsername: "myuser"
      gitPassword: "ghp_myGitHubPersonalAccessToken"
```

### Pattern 3: Multi-Repository Deployment

```yaml
include:
  - oJobGIT.yaml

jobs:
  # Frontend repository
  - name: Deploy Frontend
    to: GIT Copy Repository
    args:
      giturl: https://github.com/myorg/frontend
      gittarget: /var/www/frontend
      gitbranch: production

  # Backend repository
  - name: Deploy Backend
    to: GIT Copy Repository
    args:
      giturl: https://github.com/myorg/backend
      gittarget: /opt/backend
      gitbranch: production

  # Configuration repository
  - name: Deploy Config
    to: GIT Copy Repository
    args:
      giturl: https://github.com/myorg/config
      gittarget: /etc/myapp
      gitbranch: production

todo:
  - Deploy Frontend
  - Deploy Backend
  - Deploy Config
```

### Pattern 4: Update Existing Deployment

```yaml
include:
  - oJobGIT.yaml

jobs:
  # Backup current version
  - name: Backup Current
    exec: |
      var timestamp = ow.format.fromDate(new Date(), "yyyyMMdd-HHmmss");
      var backupPath = "/opt/backups/myapp-" + timestamp;

      if (io.fileExists("/opt/myapp")) {
        log("Backing up to: " + backupPath);
        io.cp("/opt/myapp", backupPath);
      }

  # Download new version
  - name: Download Update
    deps:
      - Backup Current
    to: GIT Copy Repository
    args:
      giturl: https://github.com/myorg/myapp
      gittarget: /opt/myapp
      gitbranch: "{{version}}"

  # Verify deployment
  - name: Verify Deployment
    deps:
      - Download Update
    exec: |
      if (!io.fileExists("/opt/myapp/package.json")) {
        throw "Deployment verification failed";
      }
      log("Deployment verified successfully");

todo:
  - name: Backup Current
  - name: Download Update
    args:
      version: "v2.0.0"
  - name: Verify Deployment
```

### Pattern 5: Scheduled Repository Sync

```yaml
include:
  - oJobGIT.yaml

ojob:
  daemon: true

jobs:
  # Sync repository
  - name: Sync Repository
    typeArgs:
      cron: "0 */6 * * *"  # Every 6 hours
    to: GIT Copy Repository
    args:
      giturl: https://github.com/myorg/data-repo
      gittarget: /data/repo
      gitbranch: main

  # Process updated data
  - name: Process Data
    deps:
      - Sync Repository
    exec: |
      log("Processing updated repository data");
      var files = io.listFiles("/data/repo").files;
      files.forEach(file => {
        log("Processing: " + file.filename);
        // Process file
      });

todo:
  - Sync Repository
  - Process Data
```

### Pattern 6: Template Repository

```yaml
include:
  - oJobGIT.yaml

jobs:
  # Download template repository
  - name: Download Template
    to: GIT Copy Repository
    args:
      giturl: https://github.com/OpenAF/openaf-templates
      gittarget: ./templates
      gitbranch: main

  # Apply template
  - name: Apply Template
    deps:
      - Download Template
    exec: |
      var templateName = args.template || "basic";
      var templatePath = "./templates/" + templateName;

      if (!io.fileExists(templatePath)) {
        throw "Template not found: " + templateName;
      }

      log("Applying template: " + templateName);

      // Copy template to project
      io.cp(templatePath, "./myproject");

      // Customize template
      var config = io.readFileYAML("./myproject/config.yaml");
      config.projectName = args.projectName;
      io.writeFileYAML("./myproject/config.yaml", config);

      log("Template applied successfully");

todo:
  - Download Template
  - name: Apply Template
    args:
      template: "web-service"
      projectName: "MyWebService"
```

---

## Security Considerations

### Use Personal Access Tokens

For private repositories, use personal access tokens instead of passwords:

```yaml
jobs:
  - name: Clone with Token
    to: GIT Copy Repository
    args:
      giturl: https://github.com/myorg/private-repo
      gittarget: ./repo
      gituser: "myusername"
      gitpass: "ghp_MyPersonalAccessToken123"
```

### Encrypt Credentials

Use OpenAF's encryption for sensitive credentials:

```bash
# Encrypt password
openaf -c "print(af.encrypt('mypassword', 'mykey'))"
```

```yaml
jobs:
  - name: Clone with Encrypted Password
    exec: |
      var decryptedPass = af.decrypt(args.encryptedPass, getEnv("GIT_KEY"));

      $job("GIT Copy Repository", {
        giturl: args.giturl,
        gittarget: args.gittarget,
        gituser: args.gituser,
        gitpass: decryptedPass
      });
```

### Store Credentials in Environment

```yaml
jobs:
  - name: Clone from Env
    to: GIT Copy Repository
    args:
      giturl: https://github.com/myorg/private-repo
      gittarget: ./repo
      gituser: "{{env.GIT_USER}}"
      gitpass: "{{env.GIT_TOKEN}}"
```

```bash
export GIT_USER="myusername"
export GIT_TOKEN="ghp_MyToken123"
ojob deploy.yaml
```

---

## Error Handling

### Handling Clone Failures

```yaml
jobs:
  - name: Safe Clone
    exec: |
      try {
        $job("GIT Copy Repository", {
          giturl: args.giturl,
          gittarget: args.gittarget,
          gitbranch: args.gitbranch
        });

        log("Repository cloned successfully");

      } catch(e) {
        logErr("Failed to clone repository: " + e.message);

        // Try fallback branch
        if (args.gitbranch != "main") {
          log("Trying fallback branch: main");

          $job("GIT Copy Repository", {
            giturl: args.giturl,
            gittarget: args.gittarget,
            gitbranch: "main"
          });
        } else {
          throw e;
        }
      }
```

### Cleanup on Failure

```yaml
jobs:
  - name: Clone with Cleanup
    exec: |
      var targetPath = "/opt/myapp";
      var backupPath = targetPath + ".backup";

      try {
        // Backup existing if present
        if (io.fileExists(targetPath)) {
          io.mv(targetPath, backupPath);
        }

        // Clone repository
        $job("GIT Copy Repository", {
          giturl: args.giturl,
          gittarget: targetPath,
          gitbranch: args.gitbranch
        });

        // Remove backup on success
        if (io.fileExists(backupPath)) {
          io.rm(backupPath);
        }

      } catch(e) {
        logErr("Clone failed: " + e.message);

        // Restore backup
        if (io.fileExists(backupPath)) {
          log("Restoring backup");
          io.rm(targetPath);
          io.mv(backupPath, targetPath);
        }

        throw e;
      }
```

---

## Advanced Techniques

### Shallow Clone for Large Repositories

While `GIT Copy Repository` doesn't directly support shallow clones, you can use the GIT plugin directly:

```yaml
jobs:
  - name: Shallow Clone
    exec: |
      plugin("GIT");

      var git = new GIT();
      var temp = "./temp-clone";

      try {
        // Shallow clone (depth 1)
        git.clone(args.giturl, temp, false, args.gitbranch, void 0, void 0, 1);

        // Copy files without .git
        io.rm(temp + "/.git");
        io.cp(temp, args.gittarget);

        log("Shallow clone completed");

      } finally {
        io.rm(temp);
      }
```

### Submodule Handling

```yaml
jobs:
  - name: Clone with Submodules
    exec: |
      plugin("GIT");

      var git = new GIT();
      var temp = "./temp-clone";

      try {
        // Clone with submodules
        git.clone(args.giturl, temp, true, args.gitbranch);

        // Remove .git directories
        io.rm(temp + "/.git");
        sh("find " + temp + " -name .git -type d -exec rm -rf {} +");

        // Move to target
        io.cp(temp, args.gittarget);

        log("Cloned with submodules");

      } finally {
        io.rm(temp);
      }
```

### Version Tagging

```yaml
jobs:
  - name: Clone Specific Tag
    to: GIT Copy Repository
    args:
      giturl: https://github.com/myorg/myrepo
      gittarget: /opt/myapp
      gitbranch: "refs/tags/v1.2.3"

  - name: Record Version
    deps:
      - Clone Specific Tag
    exec: |
      var versionInfo = {
        tag: "v1.2.3",
        deployedAt: nowUTC(),
        deployedBy: getEnv("USER")
      };

      io.writeFileJSON("/opt/myapp/version.json", versionInfo);
```

---

## Complete Example: Automated Deployment

```yaml
include:
  - oJobGIT.yaml
  - oJobEmail.yaml

ojob:
  logToFile:
    logFolder: /var/log/deployments

jobs:
  # Load configuration
  - name: Load Config
    exec: |
      args.config = io.readFileYAML("/etc/deploy-config.yaml");

  # Pre-deployment checks
  - name: Pre-Deploy Checks
    deps:
      - Load Config
    exec: |
      // Check disk space
      var df = sh("df -h /opt").stdout;
      log("Disk space:\n" + df);

      // Check if service is running
      var status = sh("systemctl is-active myapp || true").stdout.trim();
      args.serviceWasRunning = (status == "active");

      if (args.serviceWasRunning) {
        log("Service is currently running, will be restarted");
      }

  # Stop service
  - name: Stop Service
    deps:
      - Pre-Deploy Checks
    exec: |
      if (args.serviceWasRunning) {
        log("Stopping service");
        sh("systemctl stop myapp");
        sleep(2000, true);
      }

  # Backup current version
  - name: Backup Current Version
    deps:
      - Stop Service
    exec: |
      if (io.fileExists("/opt/myapp")) {
        var timestamp = ow.format.fromDate(new Date(), "yyyyMMdd-HHmmss");
        var backupPath = "/opt/backups/myapp-" + timestamp;

        log("Creating backup: " + backupPath);
        io.mkdir("/opt/backups");
        io.cp("/opt/myapp", backupPath);

        args.backupPath = backupPath;
      }

  # Deploy new version
  - name: Deploy New Version
    deps:
      - Backup Current Version
    to: GIT Copy Repository
    args:
      giturl: "{{config.repository.url}}"
      gittarget: /opt/myapp
      gitbranch: "{{version}}"
      gituser: "{{config.repository.user}}"
      gitpass: "{{config.repository.token}}"

  # Post-deployment configuration
  - name: Post-Deploy Config
    deps:
      - Deploy New Version
    exec: |
      // Copy environment-specific config
      io.cp("/etc/myapp/production.conf", "/opt/myapp/config/app.conf");

      // Set permissions
      sh("chown -R myapp:myapp /opt/myapp");
      sh("chmod +x /opt/myapp/bin/*.sh");

  # Install dependencies
  - name: Install Dependencies
    deps:
      - Post-Deploy Config
    exec: |
      log("Installing dependencies");
      sh("cd /opt/myapp && npm install --production");

  # Run migrations
  - name: Run Migrations
    deps:
      - Install Dependencies
    exec: |
      log("Running database migrations");
      sh("cd /opt/myapp && npm run migrate");

  # Start service
  - name: Start Service
    deps:
      - Run Migrations
    exec: |
      log("Starting service");
      sh("systemctl start myapp");
      sleep(5000, true);

  # Verify deployment
  - name: Verify Deployment
    deps:
      - Start Service
    exec: |
      ow.loadObj();

      // Wait for service to be ready
      var ready = false;
      var attempts = 0;

      while (!ready && attempts < 30) {
        try {
          var response = $rest({ throwExceptions: false })
            .get("http://localhost:8080/health")
            .getResponse();

          if (response.status == 200) {
            ready = true;
            log("Service is healthy");
          }
        } catch(e) {}

        if (!ready) {
          sleep(1000, true);
          attempts++;
        }
      }

      if (!ready) {
        throw "Service failed health check after deployment";
      }

  # Send notification
  - name: Notify Success
    deps:
      - Verify Deployment
    to: oJob Send email
    args:
      server: "{{config.email.server}}"
      from: "deployments@example.com"
      to: ["team@example.com"]
      subject: "Deployment successful: {{version}}"
      output: |
        Deployment completed successfully.

        Version: {{version}}
        Time: {{ow.format.fromDate(new Date(), "yyyy-MM-dd HH:mm:ss")}}
        Server: {{getEnv("HOSTNAME")}}

  # Rollback on failure
  - name: Rollback
    exec: |
      if (isDef(args.backupPath)) {
        logErr("Deployment failed, rolling back to: " + args.backupPath);

        sh("systemctl stop myapp || true");
        io.rm("/opt/myapp");
        io.cp(args.backupPath, "/opt/myapp");
        sh("systemctl start myapp");

        log("Rollback completed");
      }

todo:
  - Load Config
  - Pre-Deploy Checks
  - Stop Service
  - Backup Current Version
  - name: Deploy New Version
    args:
      version: "v2.1.0"
    onError: Rollback
  - Post-Deploy Config
  - Install Dependencies
  - Run Migrations
  - Start Service
  - Verify Deployment
  - Notify Success
```

---

## Best Practices

### 1. Always Use Branches or Tags

```yaml
# Good - specific version
gitbranch: "v1.2.3"
gitbranch: "release-2024-01"

# Risky - moving target
gitbranch: "main"
```

### 2. Backup Before Deployment

```yaml
jobs:
  - name: Backup First
    exec: |
      if (io.fileExists(args.gittarget)) {
        var backup = args.gittarget + ".backup";
        io.cp(args.gittarget, backup);
      }
```

### 3. Verify After Clone

```yaml
jobs:
  - name: Verify Clone
    deps:
      - GIT Copy Repository
    exec: |
      if (!io.fileExists(args.gittarget + "/package.json")) {
        throw "Clone verification failed";
      }
```

### 4. Clean Temporary Folders

The job handles this automatically, but if using custom logic:

```yaml
try {
  // Clone operations
} finally {
  io.rm(tempFolder);
}
```

### 5. Use Environment Variables for Secrets

Don't hardcode credentials in oJob files.

---

## See Also

- [oJob Basics](common-browse.md)
- [oJob Reference](../../concepts/oJob.html)
- [Git Plugin Documentation](../../reference/plugins/git.md)
