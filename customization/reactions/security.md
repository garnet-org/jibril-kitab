---
description: Reactions are designed with security as a primary concern.
icon: user-secret
---

# Security

## <mark style="color:yellow;">Security & Isolation</mark>

### **JavaScript Isolation**

* Each reaction runs in a separate V8 context
* Memory isolation prevents code interference
* Helper functions provide controlled system access
* No direct system call access

### **Network Policy Integration**

* Network blocking functions require netpolicy plugin
* Automatic validation of network helper usage
* Graceful degradation when netpolicy unavailable

### **File System Security**

* Temporary directories created with 0700 permissions
* Restricted to safe temporary locations
* Automatic cleanup after execution

### **Error Handling**

* Comprehensive error codes for all operations
* Detailed error messages for debugging
* Graceful failure modes

## <mark style="color:yellow;">Security Considerations</mark>

### **Input Validation**

Always validate data before using it in operations:

```javascript
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

```javascript
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

```javascript
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
