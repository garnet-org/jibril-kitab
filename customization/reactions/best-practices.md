---
icon: shield-check
---

# Best Practices

This document outlines best practices for developing, deploying, and maintaining secure and effective reactions in Jibril's runtime security system.

## <mark style="color:yellow;">Security Best Practices</mark>

### **Input Validation and Sanitization**

Always validate and sanitize input data to prevent injection attacks and ensure reliability.

```javascript
function process(data) {
  // Validate required fields
  if (!data || typeof data !== 'object') {
    Error("Invalid data object received");
    return;
  }

  // Validate process information
  if (data.process) {
    // Sanitize command strings to prevent log injection
    let cmd = data.process.cmd || "unknown";
    cmd = cmd.replace(/[\x00-\x1f\x7f-\x9f]/g, ''); // Remove control characters
    cmd = cmd.length > 500 ? cmd.substring(0, 500) + "..." : cmd;

    Info("Sanitized command: " + cmd);
  }

  // Validate file paths
  if (data.file && data.file.file) {
    let filePath = data.file.file;

    // Ensure path is absolute and doesn't contain traversal attempts
    if (!filePath.startsWith('/') || filePath.includes('../')) {
      Error("Invalid file path detected: " + filePath);
      return;
    }
  }
}
```

### **Principle of Least Privilege**

Only use the minimum privileges and capabilities required for your reaction.

```javascript
function process(data) {
  // Good: Check conditions before taking drastic actions
  if (data.metadata && data.metadata.importance === "critical") {
    // Only escalate for truly critical events
    let result = KillCurrent();
    if (result === 0) {
      Info("Critical threat terminated");
    }
  } else {
    // For non-critical events, use lighter responses
    Warn("Suspicious activity logged: " + data.process.cmd);

    // Log for later analysis instead of immediate action
    DataSet("suspicious_" + new Date().getTime(), JSON.stringify({
      process: data.process.cmd,
      timestamp: new Date().toISOString()
    }));
  }
}
```

### **Safe File Operations**

Implement secure file handling practices to prevent unauthorized access.

```javascript
function process(data) {
  // Create evidence collection with proper security
  let forensicDir = CreateTempDir("incident-*");
  if (forensicDir === "") {
    Error("Failed to create secure temporary directory");
    return;
  }

  // Validate that the directory is in expected location
  if (!forensicDir.startsWith("/tmp/")) {
    Error("Temporary directory created in unexpected location");
    return;
  }

  // Create evidence file with safe content
  let evidence = {
    timestamp: new Date().toISOString(),
    event_id: uuid,
    // Only include safe, non-sensitive data
    process_name: data.process ? data.process.exe : "unknown",
    file_accessed: data.file ? data.file.basename : "unknown"
    // Avoid including full command lines or sensitive data
  };

  let evidencePath = forensicDir + "/evidence.json";
  let writeResult = WriteFile(evidencePath, JSON.stringify(evidence, null, 2));

  if (writeResult === 0) {
    Info("Evidence collected securely at: " + evidencePath);
  } else {
    Error("Failed to write evidence: " + Errno());
  }
}
```

### **Network Security Considerations**

Be cautious with network blocking operations to avoid disrupting legitimate services.

```javascript
function process(data) {
  // Extract network information safely
  let remoteIps = [];
  let remoteDomains = [];

  if (data.background && data.background.flows && data.background.flows.protocols) {
    for (let protocol of data.background.flows.protocols) {
      if (protocol.pairs) {
        for (let pair of protocol.pairs) {
          if (pair.nodes && pair.nodes.remote) {
            // Validate IP addresses before adding
            let ip = pair.nodes.remote.address;
            if (ip && /^(\d{1,3}\.){3}\d{1,3}$/.test(ip)) {
              remoteIps.push(ip);
            }

            // Validate domain names
            if (pair.nodes.remote.names) {
              for (let domain of pair.nodes.remote.names) {
                if (domain && domain.length > 0 && domain.length < 255) {
                  remoteDomains.push(domain);
                }
              }
            }
          }
        }
      }
    }
  }

  // Apply whitelist logic to prevent blocking critical infrastructure
  let safeToBlock = [];
  let whitelist = [
    "127.0.0.1", "localhost",
    /^10\./, /^192\.168\./, /^172\.(1[6-9]|2[0-9]|3[0-1])\./,
    "company-domain.com", "trusted-partner.org"
  ];

  for (let ip of remoteIps) {
    let shouldBlock = true;

    for (let pattern of whitelist) {
      if (pattern instanceof RegExp) {
        if (pattern.test(ip)) {
          shouldBlock = false;
          break;
        }
      } else if (ip === pattern) {
        shouldBlock = false;
        break;
      }
    }

    if (shouldBlock) {
      safeToBlock.push(ip);
    }
  }

  // Only block if we have valid targets
  if (safeToBlock.length > 0) {
    Info("Blocking " + safeToBlock.length + " suspicious IPs");
    let result = NetBlockIp();
    if (result === 0) {
      Info("Network blocking successful");
    }
  }
}
```

## <mark style="color:yellow;">Performance Best Practices</mark>

### **Efficient Data Processing**

Optimize data processing to minimize reaction execution time.

```javascript
function process(data) {
  // Cache frequently accessed data
  let processCmd = data.process ? data.process.cmd : "";
  let fileName = data.file ? data.file.basename : "";

  // Use early returns to avoid unnecessary processing
  if (!processCmd && !fileName) {
    Info("No actionable data in event");
    return;
  }

  // Efficient pattern matching
  let suspiciousPatterns = ["wget", "curl", "nc", "bash -i"];
  let isSuspicious = suspiciousPatterns.some(pattern => processCmd.includes(pattern));

  if (isSuspicious) {
    // Only perform expensive operations when necessary
    Info("Suspicious command detected: " + processCmd);

    // Batch data store operations
    let timestamp = new Date().toISOString();
    DataSet("last_suspicious", timestamp);

    let count = parseInt(DataGet("suspicious_count") || "0") + 1;
    DataSet("suspicious_count", String(count));

    // Conditional expensive operations
    if (count > 10) {
      Warn("High frequency suspicious activity - escalating");
      NetBlockIp();
    }
  }
}
```

### **Memory Management**

Use memory efficiently to prevent resource exhaustion.

```javascript
function process(data) {
  // Avoid storing large objects in the data store
  let summary = {
    timestamp: new Date().toISOString(),
    process: data.process ? data.process.exe : "unknown",
    // Don't store the entire data object
    event_type: kind
  };

  // Use string keys that are likely to be reused
  let dateKey = new Date().toDateString();
  let countKey = "events_" + dateKey;

  // Implement rotation to prevent unlimited growth
  let eventCount = parseInt(DataGet(countKey) || "0") + 1;
  DataSet(countKey, String(eventCount));

  // Clean up old data periodically
  if (eventCount % 100 === 0) {
    // Remove data older than 7 days
    let cutoff = new Date();
    cutoff.setDate(cutoff.getDate() - 7);

    let keys = JSON.parse(DataKeys());
    for (let key of keys) {
      if (key.startsWith("events_")) {
        let keyDate = new Date(key.replace("events_", ""));
        if (keyDate < cutoff) {
          DataDelete(key);
        }
      }
    }
  }
}
```

### **Concurrent Execution Optimization**

Design reactions to work efficiently when running in parallel.

```javascript
function process(data) {
  // Use unique identifiers to avoid conflicts between parallel reactions
  let reactionId = name + "_" + uuid.slice(-8);
  let lockKey = "processing_" + reactionId;

  // Simple distributed locking mechanism
  if (DataHasKey(lockKey)) {
    Info("Another instance is processing this event");
    return;
  }

  // Set processing lock
  DataSet(lockKey, new Date().toISOString());

  try {
    // Perform reaction logic
    Info("Processing event: " + uuid);

    // Use atomic operations where possible
    let globalCount = parseInt(DataGet("global_event_count") || "0") + 1;
    DataSet("global_event_count", String(globalCount));

  } finally {
    // Always clean up the lock
    DataDelete(lockKey);
  }
}
```

## <mark style="color:yellow;">Testing and Quality Assurance</mark>

### **Comprehensive Testing Strategy**

Implement thorough testing before deploying reactions to production.

```javascript
// Test Reaction Template
function process(data) {
  let testMode = DataGet("test_mode") === "true";

  if (testMode) {
    Info("=== RUNNING IN TEST MODE ===");

    // Test all helper functions
    testHelperFunctions();

    // Test data processing
    testDataProcessing(data);

    // Test error handling
    testErrorHandling();

    Info("=== TEST MODE COMPLETE ===");
    return;
  }

  // Normal reaction logic
  processEvent(data);
}

function testHelperFunctions() {
  // Test logging functions
  Info("Testing Info() function");
  Warn("Testing Warn() function");
  Error("Testing Error() function");

  // Test data store functions
  DataSet("test_key", "test_value");
  let retrieved = DataGet("test_key");
  Info("Data store test: " + (retrieved === "test_value" ? "PASS" : "FAIL"));
  DataDelete("test_key");

  // Test file operations (safe)
  let testContent = "Test at " + new Date().toISOString();
  let tmpDir = CreateTempDir("test-*");
  if (tmpDir !== "") {
    let testFile = tmpDir + "/test.txt";
    let writeResult = WriteFile(testFile, testContent);
    let readContent = ReadFile(testFile);
    Info("File I/O test: " + (readContent === testContent ? "PASS" : "FAIL"));
  }

  // Test error function
  let errno = Errno();
  Info("Errno test: " + (typeof errno === "string" ? "PASS" : "FAIL"));
}

function testDataProcessing(data) {
  Info("Testing data structure validation");

  // Test data presence
  Info("Data object type: " + typeof data);
  Info("Data keys: " + Object.keys(data).join(", "));

  // Test process data
  if (data.process) {
    Info("Process data available");
    Info("Process cmd: " + (data.process.cmd || "N/A"));
    Info("Process pid: " + (data.process.pid || "N/A"));
  }

  // Test file data
  if (data.file) {
    Info("File data available");
    Info("File path: " + (data.file.file || "N/A"));
    Info("File actions: " + (data.file.actions ? data.file.actions.join(", ") : "N/A"));
  }
}

function testErrorHandling() {
  Info("Testing error handling");

  // Test invalid file operations
  let invalidRead = ReadFile("/nonexistent/path");
  Info("Invalid read test: " + (invalidRead === "" ? "PASS" : "FAIL"));

  // Test invalid data store operations
  let invalidGet = DataGet("nonexistent_key");
  Info("Invalid get test: " + (invalidGet === "" ? "PASS" : "FAIL"));
}
```

### **Staging Environment Testing**

Create a comprehensive staging environment for reaction testing.

```yaml
# Staging Test Configuration
- kind: staging_test
  name: comprehensive_staging_test
  enabled: false  # Enable only in staging
  version: 1.0
  description: Comprehensive staging test for reactions
  breed: file_access
  mechanism: file_access
  importance: low

  bases:
    - dir: /tmp/staging_test
      regex: ".*"
  file_actions:
    - write
    - unlink

  reactions:
    - format: js
      code: |
```

```javascript
        function process(data) {
          Info("=== STAGING TEST EXECUTION ===");

          // Enable test mode
          DataSet("test_mode", "true");

          // Test basic functionality
          testReactionCapabilities(data);

          // Test performance under load
          testPerformance();

          // Test error scenarios
          testErrorScenarios();

          // Clean up test data
          DataDelete("test_mode");

          Info("=== STAGING TEST COMPLETE ===");
        }

        function testReactionCapabilities(data) {
          Info("Testing reaction capabilities");

          // Test all major helper functions
          let capabilities = [
            "logging", "data_store", "file_ops", "network_ops"
          ];

          for (let capability of capabilities) {
            Info("Testing capability: " + capability);

            switch (capability) {
              case "logging":
                Info("Info logging works");
                Warn("Warning logging works");
                Error("Error logging works");
                break;

              case "data_store":
                DataSet("cap_test", "success");
                let value = DataGet("cap_test");
                Info("Data store: " + (value === "success" ? "PASS" : "FAIL"));
                DataDelete("cap_test");
                break;

              case "file_ops":
                let tmpDir = CreateTempDir("cap-test-*");
                if (tmpDir !== "") {
                  let testPath = tmpDir + "/test.txt";
                  WriteFile(testPath, "test content");
                  let content = ReadFile(testPath);
                  Info("File ops: " + (content === "test content" ? "PASS" : "FAIL"));
                }
                break;

              case "network_ops":
                // Only test if netpolicy is available
                Info("Network ops capability available");
                break;
            }
          }
        }

        function testPerformance() {
          Info("Testing performance characteristics");

          let startTime = new Date().getTime();

          // Simulate typical reaction workload
          for (let i = 0; i < 100; i++) {
            DataSet("perf_test_" + i, "value_" + i);
          }

          let midTime = new Date().getTime();

          for (let i = 0; i < 100; i++) {
            DataGet("perf_test_" + i);
          }

          let endTime = new Date().getTime();

          // Clean up
          for (let i = 0; i < 100; i++) {
            DataDelete("perf_test_" + i);
          }

          let writeTime = midTime - startTime;
          let readTime = endTime - midTime;

          Info("Performance test - Write: " + writeTime + "ms, Read: " + readTime + "ms");
        }
```

## <mark style="color:yellow;">Operational Best Practices</mark>

### **Monitoring and Alerting**

Implement comprehensive monitoring for reaction health and effectiveness.

```javascript
function process(data) {
  let startTime = new Date().getTime();

  try {
    // Main reaction logic
    performReactionLogic(data);

    // Track success metrics
    let successCount = parseInt(DataGet("reaction_success_count") || "0") + 1;
    DataSet("reaction_success_count", String(successCount));

  } catch (error) {
    // Track failure metrics
    let failureCount = parseInt(DataGet("reaction_failure_count") || "0") + 1;
    DataSet("reaction_failure_count", String(failureCount));

    Error("Reaction failed: " + error.toString());

    // Alert on high failure rates
    let totalAttempts = successCount + failureCount;
    if (totalAttempts > 100 && (failureCount / totalAttempts) > 0.1) {
      Error("ALERT: Reaction failure rate exceeds 10%");
    }

  } finally {
    // Track performance metrics
    let executionTime = new Date().getTime() - startTime;
    let avgTimeKey = "avg_execution_time";
    let currentAvg = parseFloat(DataGet(avgTimeKey) || "0");
    let newAvg = (currentAvg * 0.9) + (executionTime * 0.1); // Rolling average
    DataSet(avgTimeKey, String(newAvg));

    if (executionTime > 5000) { // Alert on slow reactions
      Warn("Slow reaction execution: " + executionTime + "ms");
    }
  }
}
```

### **Configuration Management**

Maintain reaction configurations with proper version control and rollback capabilities.

```yaml
# Production Deployment Template
- kind: production_reaction
  name: managed_security_response
  enabled: true
  version: 2.1.0  # Always version your reactions
  description: |
    Production security response reaction

    Change Log:
    v2.1.0 - Added enhanced error handling and performance monitoring
    v2.0.0 - Implemented graduated response system
    v1.0.0 - Initial implementation

    Deployment Notes:
    - Requires netpolicy plugin enabled
    - Tested in staging environment
    - Approved by security team

  breed: execution
  mechanism: execution
  tactic: execution
  technique: T1059
  importance: high

  # Configuration parameters (document all settings)
  arbitrary:
    - how: OR
      which: pertinent
      items:
        - what: cmd
          which: contains
          pattern: "malicious_pattern"

  reactions:
    - format: js
      code: |
```

```javascript
        // Production Reaction - Version 2.1.0
        function process(data) {
          // Configuration constants
          const VERSION = "2.1.0";
          const MAX_EXECUTION_TIME = 5000; // 5 seconds
          const FAILURE_THRESHOLD = 0.1; // 10%

          Info("Production reaction v" + VERSION + " executing");

          // Implement production logic with full error handling
          try {
            executeProductionLogic(data);
          } catch (error) {
            handleProductionError(error, data);
          }
        }

        function executeProductionLogic(data) {
          // Validated production logic
          Info("Executing validated production response");

          // Implementation details...
        }

        function handleProductionError(error, data) {
          Error("Production reaction error: " + error.toString());

          // Log error details for debugging
          let errorRecord = {
            timestamp: new Date().toISOString(),
            version: "2.1.0",
            error: error.toString(),
            event_uuid: uuid,
            data_summary: {
              has_process: !!data.process,
              has_file: !!data.file,
              event_type: kind
            }
          };

          WriteFile("/var/log/jibril/reaction-errors.log", 
                   JSON.stringify(errorRecord) + "\n");
        }
```

### **Documentation**

Maintain comprehensive documentation for all reactions.

```javascript
/**
 * Advanced Incident Response Reaction
 *
 * Purpose: Provides comprehensive incident response capabilities including
 *          containment, evidence collection, and alerting.
 *
 * Triggers: Executes on critical security events detected by Jibril
 *
 * Dependencies:
 *   - netpolicy plugin (for network blocking)
 *   - Write access to /var/log/security/
 *   - Temporary directory creation permissions
 *
 * Configuration:
 *   - importance: critical (required for execution)
 *   - breed: execution, file_access, or network_peers
 *
 * Outputs:
 *   - Forensic evidence in temporary directories
 *   - Incident logs in /var/log/security/incidents.log
 *   - Real-time alerts via error logging
 *
 * Error Handling:
 *   - Graceful degradation on helper function failures
 *   - Comprehensive error logging
 *   - Rollback capabilities for network blocks
 *
 * Performance:
 *   - Target execution time: < 2 seconds
 *   - Memory usage: < 50MB temporary storage
 *   - Network calls: Minimal, only for blocking
 *
 * Testing:
 *   - Unit tests in staging environment
 *   - Integration tests with full event pipeline
 *   - Performance benchmarks under load
 *
 * Maintenance:
 *   - Review quarterly for effectiveness
 *   - Update threat intelligence patterns monthly
 *   - Monitor performance metrics continuously
 *
 * Version History:
 *   v1.0 - Initial implementation
 *   v1.1 - Added performance monitoring
 *   v2.0 - Enhanced evidence collection
 *
 * Author: Security Team
 * Last Updated: 2025-07-23
 * Next Review: 2025-10-23
 */
function process(data) {
  // Implementation follows documented specifications
  implementIncidentResponse(data);
}
```

## <mark style="color:yellow;">Compliance and Auditing</mark>

### **Audit Trail Implementation**

Maintain comprehensive audit trails for all reaction activities.

```javascript
function process(data) {
  // Create audit record for all reaction executions
  let auditRecord = {
    timestamp: new Date().toISOString(),
    reaction_name: name,
    reaction_kind: kind,
    event_uuid: uuid,
    event_metadata: {
      importance: data.metadata ? data.metadata.importance : "unknown",
      tactic: data.metadata ? data.metadata.tactic : "unknown",
      technique: data.metadata ? data.metadata.technique : "unknown"
    },
    actions_taken: [],
    data_accessed: [],
    files_created: [],
    network_operations: []
  };

  try {
    // Log data access
    if (data.process) {
      auditRecord.data_accessed.push("process_data");
    }
    if (data.file) {
      auditRecord.data_accessed.push("file_data");
    }
    if (data.background && data.background.flows) {
      auditRecord.data_accessed.push("network_flow_data");
    }

    // Execute reaction with audit logging
    if (shouldTerminateProcess(data)) {
      let killResult = KillCurrent();
      auditRecord.actions_taken.push({
        action: "process_termination",
        result: killResult === 0 ? "success" : "failed",
        error: killResult !== 0 ? Errno() : null
      });
    }

    if (shouldBlockNetwork(data)) {
      let blockResult = NetBlockIp();
      auditRecord.actions_taken.push({
        action: "network_blocking",
        result: blockResult === 0 ? "success" : "failed",
        error: blockResult !== 0 ? Errno() : null
      });
      auditRecord.network_operations.push("ip_blocking");
    }

    // Document evidence collection
    let evidenceDir = CreateTempDir("audit-evidence-*");
    if (evidenceDir !== "") {
      let evidencePath = evidenceDir + "/reaction_evidence.json";
      WriteFile(evidencePath, JSON.stringify(data, null, 2));

      auditRecord.files_created.push({
        path: evidencePath,
        purpose: "evidence_collection",
        size: JSON.stringify(data).length
      });
    }

    auditRecord.status = "completed";

  } catch (error) {
    auditRecord.status = "failed";
    auditRecord.error = error.toString();
    Error("Reaction execution failed: " + error.toString());
  }

  // Write audit record
  let auditPath = "/var/log/jibril/reaction-audit.log";
  WriteFile(auditPath, JSON.stringify(auditRecord) + "\n");

  // Store audit record in data store for reporting
  DataSet("audit_" + uuid, JSON.stringify(auditRecord));
}

function shouldTerminateProcess(data) {
  // Implement business logic for process termination decisions
  return data.metadata && data.metadata.importance === "critical";
}

function shouldBlockNetwork(data) {
  // Implement business logic for network blocking decisions
  return data.background && data.background.flows && 
         data.metadata && data.metadata.importance === "high";
}
```
