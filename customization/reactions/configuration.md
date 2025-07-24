---
icon: square-sliders
---

# Configuration

This document explains how to configure reactions within Jibril's detection recipes. Reactions are defined in YAML files (the Alchemies) and integrated into the broader detection system.

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
  subtechnique: mitre_subtechnique
  importance: severity_level

  # Detection criteria (varies by type)
  # ... detection-specific configuration ...

  # Reactions configuration
  reactions:
    - format: js  # or "shell"
      code: |
        # JavaScript function here
    - format: shell
      code: |
        # Shell script here
```

## <mark style="color:yellow;">Reaction Configuration Options</mark>

### **format** (required)

Specifies the execution format for the reaction code.

**Valid values:**

* `js`: JavaScript execution using V8 engine (recommended)
* `shell`: Shell script execution using `/bin/sh`

**Example:**

```javascript
reactions:
  - format: js
    code: |
      function process(data) {
        Info("JavaScript reaction");
      }
  - format: shell
    code: |
      echo "Shell reaction"
```

### **code** (required)

Contains the actual reaction code to execute.

**For JavaScript reactions:**

* Must contain a `process(data)` function
* Function receives the complete event data as a parameter
* Has access to all helper functions and global variables

**For Shell reactions:**

* Can be any valid shell script
* Event data is provided via `REACTION_DATA` environment variable as JSON

**JavaScript Example:**

```yaml
reactions:
  - format: js
    code: |
```

```javascript
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
```

```bash
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
- kind: passwd_usage
  name: passwd_usage
  enabled: false
  version: 1.0
  description: Passwd related command usage
  documentation: |
    https://garnet.gitbook.io/jibril/detections/execution/passwd_usage
  breed: file_access
  mechanism: execution
  tactic: persistence
  technique: account_manipulation
  subtechnique: local_account
  importance: high
  times:
    - kind: times_per_parent_proc
      max: 2
    - kind: times_per_parent_exe
      max: 4
    - kind: times_per_full_ancestry
      max: 4
  arbitrary: []
  file_actions:
    - execve
  file_actions_how: any
  bases:
    - dir: /etc
      base: passwd
  reactions:
    - format: js
      code: |
```

```javascript
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
- kind: net_suspicious_tool_exec
  name: net_suspicious_tool_exec_critical
  enabled: false
  version: 1.0
  description: Network suspicious tool execution detected (with IP address argument)
  documentation: |
    https://garnet.gitbook.io/jibril/detections/execution/net_suspicious_tool_exec
  breed: file_access
  mechanism: execution
  tactic: discovery
  technique: network_service_discovery
  subtechnique: none
  importance: critical
  times:
    - kind: times_per_parent_proc
      max: 2
    - kind: times_per_parent_exe
      max: 4
    - kind: times_per_full_ancestry
      max: 4
  arbitrary:
    - how: OR
      which: irrelevant
      items:
        - what: args
          which: pertinent
          # Match if IPv4 or IPv6 addresses appear in the command arguments.
          pattern: ([^\w|\.](\b25[0-5]|\b2[0-4][0-9]|\b[01]?[0-9][0-9]?)(\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}([^\w|\.]|$)|[^\w|\.](([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))([^\w|\.]|$))
  file_actions:
    - execve
  file_actions_how: any
  bases:
    - base: nc # TCP/UDP client/listener.
    - base: ncat # Nmap's TCP/UDP client/listener.
  reactions:
  # yaml-embedded-languages: javascript
  - format: js
    code: |
```

```javascript
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
  name: malicious_network_01
  enabled: false
  version: 1.0
  description: Access to malicious domains
  documentation: not available
  breed: remote_domains
  mechanism: network_peers
  tactic: command_and_control
  technique: application_layer_protocol
  subtechnique: web_protocols
  importance: critical
  times:
    - kind: times_per_proc
      max: 2
    - kind: times_per_exe
      max: 4
    - kind: times_per_full_ancestry
      max: 4
  arbitrary: []
  flow_actions:
    - ingress
    - egress
  flow_actions_how: any
  remote_domains_type: suffix
  remote_domains:
    - onion
  reactions:
    - format: js
      code: |
```

```javascript
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
  tactic: mitre_tactic
  technique: mitre_technique
  subtechnique: mitre_sub_technique
  importance: high
  bases:
    - dir: /etc/ssh
  file_actions:
    - write
  reactions:
    # Reaction 1: Immediate logging
    - format: js
      code: |
        # JavaScript function here

    # Reaction 2: Network containment
    - format: js
      code: |
        # JavaScript function here

    # Reaction 3: Evidence collection
    - format: js
      code: |
        # JavaScript function here

    # Reaction 4: System backup (shell script)
    - format: shell
      code: |
        # Shell script here
```

## <mark style="color:yellow;">Debugging and Troubleshooting</mark>

### **Logging for Debugging**

Use comprehensive logging to debug reaction issues:

```yaml
reactions:
  - format: js
    code: |
```

```javascript
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
```

```javascript
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
        # JavaScript function here
```

```javascript
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
