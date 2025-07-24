---
description: Immediate, programmable responses to security detection events.
icon: eye
---

# Overview

The **Reactions** feature is Jibril's powerful automation system that enables immediate, programmable responses to security detection events. When a security event is detected by Jibril's monitoring mechanisms, reactions can automatically execute custom code to respond, remediate, or gather additional intelligence.

## <mark style="color:yellow;">Overview</mark>

Reactions transform Jibril from a passive monitoring tool into an active security defense system. Instead of merely alerting on suspicious activities, reactions can take immediate action:

* **Block malicious network traffic** in real-time
* **Terminate suspicious processes** before they cause harm
* **Collect forensic evidence** automatically
* **Isolate compromised systems** from the network
* **Trigger emergency procedures** during critical incidents

## <mark style="color:yellow;">How Reactions Work</mark>

When Jibril detects a security event through its monitoring mechanisms (file access, process execution, network activity, etc.), the following workflow occurs:

1. **A Security Threat is Detected**:\
   An event from the OS matches a configured detection recipe
2. **Event Detection**:\
   Security event is reported in all configured and enabled printers
3. **Reaction Trigger**:\
   All reactions associated with that recipe are triggered in parallel
4. **Context Injection**:\
   The complete event context (process ancestry, network flows, file details, etc.) is made available to the reaction
5. **Code Execution**:\
   The reaction code executes in an isolated environment with access to powerful helper functions
6. **Response Actions**:\
   The reaction can take various actions like blocking IPs, killing processes, or logging additional information

## <mark style="color:yellow;">Supported Formats</mark>

Reactions support two execution formats:

### JavaScript (Recommended)

* **Runtime**: Google V8 JavaScript engine with isolated contexts
* **Performance**: Fast compilation and execution
* **Features**: Rich set of built-in helper functions
* **Isolation**: Each reaction runs in its own secure context
* **Data Access**: Full access to event data through JSON objects

### Shell Scripts

* **Runtime**: Standard `/bin/sh` shell execution
* **Flexibility**: Full system access with shell commands
* **Environment**: Event data provided as `JSON` via `REACTION_DATA` environment variable
* **Security**: Executed in temporary directories with restricted permissions

## <mark style="color:yellow;">Key Capabilities</mark>

### **Logging & Monitoring**

```javascript
Info("Detected suspicious file access");
Warn("High risk network connection identified");
Error("Critical security violation detected");
```

### **Network Policy Enforcement**

```javascript
// Block malicious IPs automatically
NetBlockIp("192.168.1.100");

// Block domains associated with threats
NetBlockDomain("malicious-site.com");

// Block all remote IPs from the current event
NetBlockIp(); // Uses event context
```

### **Process Management**

```javascript
// Terminate the offending process
KillCurrent();

// Stop the parent process if compromised
KillParent();

// Kill specific process by PID
KillProcess(1234);
```

### **File System Operations**

```javascript
// Read configuration files
let config = ReadFile("/etc/app/config.json");

// Write forensic evidence
WriteFile("/var/log/security/incident.log", evidenceData);

// Get file metadata
let fileInfo = Stat("/suspicious/file");
```

### **Persistent Data Storage**

```javascript
// Store incident data across reactions
DataSet("incident_count", "5");
DataPush("blocked_ips", "192.168.1.100");

// Retrieve historical data
let count = DataGet("incident_count");
let blockedIps = DataKeys(); // Get all stored keys
```

### **Emergency Actions**

```javascript
// System shutdown in critical situations
PowerOff();

// Trigger kernel panic for immediate halt
Panic();
```

## <mark style="color:yellow;">Event Context</mark>

Every reaction receives comprehensive context about the security event that triggered it:

### **Global Variables**

* `kind`: The type of detection event (e.g., "file\_access", "execution")
* `name`: The name of the detection recipe that triggered
* `uuid`: Unique identifier for this specific event
* `data`: Complete JSON object containing all event details

### **Event Data Structure**

```javascript
{
  "uuid": "event-unique-identifier",
  "timestamp": "2025-07-23T10:30:00Z",
  "metadata": {
    "kind": "file_access",
    "name": "suspicious_file_access",
    "importance": "high",
    "tactic": "name_of_tactic",
    "technique": "name_of_technique"
    "subtechnique": "name_of_sub_technique"
  },
  "base": {
    "background": {
      "ancestry": [...], // Process chain
      "flows": {...}     // Network connections
    }
  },
  "file": {
    "file": "/etc/passwd",
    "actions": ["read", "write"],
    "basename": "passwd"
  }
}
```

## <mark style="color:yellow;">Integration with Detection Recipes</mark>

Reactions are defined within detection recipes using YAML configuration (Alchemies):

```javascript
- kind: malicious_file_access
  name: detect_passwd_tampering
  # ... detection criteria ...
  reactions:
    - format: js
      code: |
        function process(data) {
          Info("Password file accessed by: " + data.process.cmd);

          // Block the process
          let result = KillCurrent();
          if (result === 0) {
            Info("Malicious process terminated");
          }

          // Log to incident database
          DataSet("last_passwd_access", new Date().toISOString());
        }
```
