---
icon: cog
---

# Reaction Configuration

This document explains how to configure reactions within Jibril's detection recipes (Alchemies). Reactions are defined in YAML files and integrated into the broader detection system.

## <mark style="color:yellow;">Basic Structure</mark>

Reactions are configured as part of detection recipes. Here's the basic structure:

```yaml
- kind: recipe_identifier
  name: recipe_name
  enabled: true
  version: 1.0
  description: Description of what this recipe detects
  
  # Detection configuration
  breed: detection_type
  mechanism: detection_mechanism
  tactic: mitre_tactic
  technique: mitre_technique
  importance: severity_level
  
  # Detection criteria (varies by type)
  # ... detection-specific configuration ...
  
  # Reactions configuration
  reactions:
    - format: js  # or "shell"
      code: |
        function process(data) {
          // JavaScript reaction code
        }
    - format: shell
      code: |
        #!/bin/bash
        # Shell script reaction code
```

## <mark style="color:yellow;">Reaction Configuration Options</mark>

### **format** (required)

Specifies the execution format for the reaction code.

**Valid values:**

- `js`: JavaScript execution using V8 engine (recommended)
- `shell`: Shell script execution using `/bin/sh`

**Example:**

```yaml
reactions:
  - format: js
    code: |
      function process(data) {
        Info("JavaScript reaction");
      }
  - format: shell
    code: |
      #!/bin/bash
      echo "Shell reaction"
```

### **code** (required)

Contains the actual reaction code to execute.

**For JavaScript reactions:**

- Must contain a `process(data)` function
- Function receives the complete event data as a parameter
- Has access to all helper functions and global variables

**For Shell reactions:**

- Can be any valid shell script
- Event data is provided via `REACTION_DATA` environment variable as JSON
- Should include shebang line for clarity

**JavaScript Example:**

```yaml
reactions:
  - format: js
    code: |
      function process(data) {
        // Access global variables
        Info("Event type: " + kind);
        Info("Recipe name: " + name);
        Info("Event UUID: " + uuid);
        
        // Process the event data
        if (data.process) {
          Warn("Process: " + data.process.cmd);
        }
        
        // Take action
        let result = NetBlockIp();
        if (result === 0) {
          Info("Network blocked successfully");
        }
      }
```

**Shell Example:**

```yaml
reactions:
  - format: shell
    code: |
      #!/bin/bash
      
      # Parse event data
      PROCESS_CMD=$(echo "$REACTION_DATA" | jq -r '.process.cmd')
      FILE_PATH=$(echo "$REACTION_DATA" | jq -r '.file.file // "N/A"')
      
      echo "Shell reaction triggered"
      echo "Process: $PROCESS_CMD"
      echo "File: $FILE_PATH"
      
      # Log to system log
      logger "Jibril reaction: $PROCESS_CMD accessed $FILE_PATH"
```

## <mark style="color:yellow;">Integration with Detection Types</mark>

### **File Access Reactions**

File access reactions receive detailed information about file operations.

```yaml
- kind: sensitive_file_monitor
  name: monitor_passwd_access
  enabled: true
  breed: file_access
  mechanism: file_access
  tactic: credential_access
  technique: T1003
  importance: high
  
  # File detection criteria
  bases:
    - dir: /etc
      base: passwd
  file_actions:
    - read
    - write
  file_actions_how: any
  
  reactions:
    - format: js
      code: |
        function process(data) {
          Info("Password file accessed!");
          Info("File: " + data.file.file);
          Info("Actions: " + data.file.actions.join(", "));
          Info("Process: " + data.process.cmd);
          Info("User ID: " + data.process.uid);
          
          // Terminate suspicious access
          if (data.process.uid !== 0) {
            Warn("Non-root access to passwd file - terminating");
            KillCurrent();
          }
        }
```

### **Process Execution Reactions**

Execution reactions monitor process creation and can access ancestry information.

```yaml
- kind: malicious_execution
  name: detect_reverse_shells
  enabled: true
  breed: execution
  mechanism: execution
  tactic: execution
  technique: T1059
  importance: critical
  
  # Process detection criteria
  arbitrary:
    - how: OR
      which: pertinent
      items:
        - what: cmd
          which: contains
          pattern: "nc.*-e"
        - what: cmd
          which: contains
          pattern: "bash.*-i"
        - what: cmd
          which: contains
          pattern: "/dev/tcp/"
  
  reactions:
    - format: js
      code: |
        function process(data) {
          Error("REVERSE SHELL DETECTED!");
          Info("Command: " + data.process.cmd);
          Info("PID: " + data.process.pid);
          Info("Parent PID: " + data.process.ppid);
          
          // Log the full process ancestry
          if (data.base.background.ancestry) {
            Info("Process ancestry:");
            for (let i = 0; i < data.base.background.ancestry.length; i++) {
              let ancestor = data.base.background.ancestry[i];
              Info("  " + ancestor.pid + ": " + ancestor.cmd);
            }
          }
          
          // Immediate containment
          let killResult = KillCurrent();
          let blockResult = NetBlockIp();
          
          if (killResult === 0 && blockResult === 0) {
            Info("Reverse shell contained successfully");
          }
        }
```

### **Network Activity Reactions**

Network reactions can access flow information and remote connection details.

```yaml
- kind: malicious_network
  name: block_tor_connections
  enabled: true
  breed: remote_domains
  mechanism: network_peers
  tactic: command_and_control
  technique: T1090
  importance: high
  
  # Network detection criteria
  remote_domains:
    - "*.onion"
  remote_domains_type: wildcard
  flow_actions:
    - egress
  
  reactions:
    - format: js
      code: |
        function process(data) {
          Warn("Tor connection detected");
          
          // Extract network flow information
          if (data.background && data.background.flows) {
            Info("Network flows detected:");
            let flows = data.background.flows;
            
            if (flows.protocols) {
              for (let protocol of flows.protocols) {
                Info("Protocol: " + protocol.name);
                
                if (protocol.pairs) {
                  for (let pair of protocol.pairs) {
                    if (pair.nodes && pair.nodes.remote) {
                      Info("Remote: " + pair.nodes.remote.address);
                      if (pair.nodes.remote.names) {
                        Info("Domains: " + pair.nodes.remote.names.join(", "));
                      }
                    }
                  }
                }
              }
            }
          }
          
          // Block the connection
          let result = NetBlockDomain();
          if (result === 0) {
            Info("Tor domains blocked successfully");
            
            // Log to security incident database
            DataSet("tor_blocks_" + new Date().toDateString(), 
                   String(parseInt(DataGet("tor_blocks_" + new Date().toDateString()) || "0") + 1));
          }
        }
```

## <mark style="color:yellow;">Multiple Reactions</mark>

You can define multiple reactions for a single detection recipe. They will execute in parallel:

```yaml
- kind: comprehensive_response
  name: multi_reaction_example
  enabled: true
  breed: file_access
  mechanism: file_access
  importance: high
  
  bases:
    - dir: /etc/ssh
      regex: ".*"
  file_actions:
    - write
  
  reactions:
    # Reaction 1: Immediate logging
    - format: js
      code: |
        function process(data) {
          Error("SSH configuration modified!");
          Info("File: " + data.file.file);
          Info("Process: " + data.process.cmd);
        }
    
    # Reaction 2: Network containment
    - format: js
      code: |
        function process(data) {
          Info("Implementing network containment");
          let result = NetBlockIp();
          if (result === 0) {
            Info("Network access blocked");
          }
        }
    
    # Reaction 3: Evidence collection
    - format: js
      code: |
        function process(data) {
          Info("Collecting forensic evidence");
          
          let evidence = {
            timestamp: new Date().toISOString(),
            file_modified: data.file.file,
            process: data.process.cmd,
            user_id: data.process.uid
          };
          
          let forensicDir = CreateTempDir("ssh-mod-*");
          if (forensicDir !== "") {
            WriteFile(forensicDir + "/evidence.json", 
                     JSON.stringify(evidence, null, 2));
            Info("Evidence saved to: " + forensicDir);
          }
        }
    
    # Reaction 4: System backup (shell script)
    - format: shell
      code: |
        #!/bin/bash
        echo "Creating SSH configuration backup"
        
        BACKUP_DIR="/var/backups/jibril/ssh-$(date +%Y%m%d_%H%M%S)"
        mkdir -p "$BACKUP_DIR"
        
        # Backup SSH configuration
        cp -r /etc/ssh/* "$BACKUP_DIR/" 2>/dev/null || true
        
        echo "SSH backup completed: $BACKUP_DIR"
        logger "Jibril: SSH configuration backed up to $BACKUP_DIR"
```

## <mark style="color:yellow;">Configuration Validation</mark>

Jibril validates reaction configurations at startup. Common validation errors include:

### **Missing Required Fields**

```yaml
reactions:
  - format: js
    # ERROR: Missing 'code' field
```

**Fix:**

```yaml
reactions:
  - format: js
    code: |
      function process(data) {
        Info("Valid reaction");
      }
```

### **Invalid Format**

```yaml
reactions:
  - format: python  # ERROR: Invalid format
    code: |
      print("Not supported")
```

**Fix:**

```yaml
reactions:
  - format: js  # Valid: js or shell only
    code: |
      function process(data) {
        Info("Valid format");
      }
```

### **Missing Process Function (JavaScript)**

```yaml
reactions:
  - format: js
    code: |
      # ERROR: Missing process() function
      Info("This won't work");
```

**Fix:**

```yaml
reactions:
  - format: js
    code: |
      function process(data) {
        Info("This will work");
      }
```

### **Network Helper Without netpolicy Plugin**

```yaml
reactions:
  - format: js
    code: |
      function process(data) {
        NetBlockIp(); # ERROR: Requires netpolicy plugin
      }
```

**Fix:** Ensure the netpolicy plugin is enabled in your Jibril configuration, or avoid using network helper functions.

## <mark style="color:yellow;">Performance Considerations</mark>

### **Reaction Execution**

- **Parallel Execution**: Multiple reactions for the same recipe run concurrently
- **V8 Compilation**: JavaScript reactions are pre-compiled for fast execution
- **Context Isolation**: Each reaction runs in its own isolated environment
- **Resource Management**: Automatic cleanup prevents memory leaks

### **Best Practices for Performance**

1. **Keep reactions lightweight** - Avoid complex computations
2. **Use the data store efficiently** - Don't store large objects
3. **Minimize file I/O** - Only write essential data
4. **Handle errors gracefully** - Don't let failed reactions impact others
5. **Test thoroughly** - Validate reactions before production deployment

### **Example: Optimized Reaction**

```yaml
reactions:
  - format: js
    code: |
      function process(data) {
        // Fast path for common cases
        if (!data.process || !data.process.cmd) {
          return; // Exit early if no process data
        }
        
        // Efficient data access
        let cmd = data.process.cmd;
        let isHighRisk = cmd.includes("wget") || cmd.includes("curl");
        
        if (isHighRisk) {
          // Only log essential information
          Info("High-risk process: " + cmd);
          
          // Use efficient data store operations
          let count = parseInt(DataGet("risk_count") || "0") + 1;
          DataSet("risk_count", String(count));
          
          // Take action only when necessary
          if (count > 5) {
            NetBlockIp();
          }
        }
      }
```

## <mark style="color:yellow;">Security Considerations</mark>

### **Input Validation**

Always validate data before using it in operations:

```yaml
reactions:
  - format: js
    code: |
      function process(data) {
        // Validate input data
        if (!data || !data.process) {
          Error("Invalid event data received");
          return;
        }
        
        // Sanitize strings before logging
        let cmd = data.process.cmd || "unknown";
        if (cmd.length > 1000) {
          cmd = cmd.substring(0, 1000) + "... (truncated)";
        }
        
        Info("Process: " + cmd);
      }
```

### **File Path Security**

Be careful with file operations:

```yaml
reactions:
  - format: js
    code: |
      function process(data) {
        // Validate file paths
        let filePath = data.file ? data.file.file : "";
        
        // Ensure we're not writing to sensitive locations
        if (filePath.startsWith("/etc/") || filePath.startsWith("/sys/")) {
          Error("Attempted to write to sensitive location: " + filePath);
          return;
        }
        
        // Use safe temporary directories
        let tmpDir = CreateTempDir("evidence-*");
        if (tmpDir !== "") {
          let safePath = tmpDir + "/safe-evidence.json";
          WriteFile(safePath, JSON.stringify(data));
        }
      }
```

### **Network Security**

Network operations should be used judiciously:

```yaml
reactions:
  - format: js
    code: |
      function process(data) {
        // Only block external IPs, not internal infrastructure
        if (data.background && data.background.flows) {
          // Extract remote IPs
          let remoteIps = [];
          // ... extraction logic ...
          
          for (let ip of remoteIps) {
            // Don't block internal network ranges
            if (!ip.startsWith("10.") && 
                !ip.startsWith("192.168.") && 
                !ip.startsWith("172.16.")) {
              NetBlockIp(ip);
            }
          }
        }
      }
```

## <mark style="color:yellow;">Debugging and Troubleshooting</mark>

### **Logging for Debugging**

Use comprehensive logging to debug reaction issues:

```yaml
reactions:
  - format: js
    code: |
      function process(data) {
        Info("=== REACTION DEBUG START ===");
        Info("Kind: " + kind);
        Info("Name: " + name);
        Info("UUID: " + uuid);
        
        // Log data structure
        Info("Data keys: " + Object.keys(data).join(", "));
        
        if (data.process) {
          Info("Process PID: " + data.process.pid);
          Info("Process CMD: " + data.process.cmd);
        }
        
        // Test helper functions
        let testResult = DataSet("debug_test", "success");
        Info("DataSet test result: " + testResult);
        
        let retrieved = DataGet("debug_test");
        Info("DataGet test result: " + retrieved);
        
        Info("=== REACTION DEBUG END ===");
      }
```

### **Error Handling**

Implement proper error handling:

```yaml
reactions:
  - format: js
    code: |
      function process(data) {
        try {
          // Main reaction logic
          let result = NetBlockIp();
          if (result !== 0) {
            Error("Failed to block IP: " + Errno());
          }
          
          // File operations with error checking
          let writeResult = WriteFile("/tmp/reaction.log", "test");
          if (writeResult !== 0) {
            Error("Failed to write file: " + Errno());
          }
          
        } catch (error) {
          Error("Reaction error: " + error.toString());
        }
      }
```

## <mark style="color:yellow;">Testing Reactions</mark>

### **Test Configuration**

Create test reactions with disabled state:

```yaml
- kind: test_reaction
  name: my_test_reaction
  enabled: false  # Start disabled for testing
  version: 1.0
  description: Test reaction for development
  breed: file_access
  mechanism: file_access
  importance: low
  
  bases:
    - dir: /tmp/test
      base: trigger.txt
  file_actions:
    - unlink
  
  reactions:
    - format: js
      code: |
        function process(data) {
          Info("=== TEST REACTION ===");
          Info("All systems operational");
          
          // Test all helper functions safely
          DataSet("test", "success");
          let value = DataGet("test");
          Info("Data store test: " + (value === "success" ? "PASS" : "FAIL"));
          
          DataDelete("test");
          Info("=== TEST COMPLETE ===");
        }
```

### **Gradual Deployment**

1. **Test Environment**: Deploy with `enabled: false` first
2. **Limited Scope**: Start with specific file patterns or processes
3. **Monitoring**: Watch logs carefully for unexpected behavior
4. **Gradual Expansion**: Slowly expand scope and enable more reactions
5. **Production**: Only deploy fully tested reactions to production

This configuration guide provides the foundation for creating powerful, secure, and maintainable reactions within the Jibril security system.
