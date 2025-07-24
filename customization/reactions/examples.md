---
icon: lightbulb
---

# Examples

This document provides practical, real-world examples of how to use reactions to create powerful automated security responses. Each example includes the complete YAML configuration and JavaScript code with production-ready patterns.

###

## <mark style="color:yellow;">Basic Examples</mark>

### Example 1: Crypto Miner Detection with Process Termination

This example shows how to detect and terminate cryptocurrency miners using common miner binaries.

```yaml
- kind: crypto_miner_reaction
  name: crypto_miner_terminate_and_block
  enabled: true
  version: 1.0
  description: Detect and respond to cryptocurrency miner execution
  documentation: |
    Detects crypto miner execution and terminates the process while blocking network access
  breed: file_access
  mechanism: execution
  tactic: impact
  technique: resource_hijacking
  subtechnique: compute_hijacking
  importance: critical
  times:
    - kind: times_per_proc
      max: 2
    - kind: times_per_exe
      max: 4
  arbitrary: []
  file_actions:
    - execve
  file_actions_how: any
  bases:
    - base: xmrig      # Popular Monero miner
    - base: ethminer   # Ethereum GPU miner
    - base: cgminer    # Multi-threaded ASIC/GPU miner
    - base: cpuminer   # CPU miner (minerd)
    - base: t-rex      # Nvidia GPU miner
  reactions:
    - format: js
      code: |
```

```javascript
        function process(data) {
          Info("=== CRYPTOCURRENCY MINER DETECTED ===");
          Info("Miner: " + data.file.basename);
          Info("Process: " + data.process.cmd);
          Info("PID: " + data.process.pid);

          // Terminate the miner immediately
          let killResult = KillCurrent();
          if (killResult === 0) {
            Info("Cryptocurrency miner terminated successfully");

            // Count terminated miners
            let count = parseInt(DataGet("miners_terminated") || "0") + 1;
            DataSet("miners_terminated", String(count));
            DataSet("last_miner_terminated", new Date().toISOString());

            Warn("Total miners terminated: " + count);
          } else if (killResult === 1) {
            Info("Process already exited");
          } else {
            Error("Failed to terminate miner: " + Errno());
          }

          // Block network connections to prevent mining pool communication
          let blockResult = NetBlockIp();
          if (blockResult === 0) {
            Info("Blocked network connections from miner");
          } else {
            Warn("Network blocking result: " + blockResult);
          }
        }
```

### Example 2: Sudoers File Modification Detection

This example shows how to detect and respond to privilege escalation attempts through sudoers file modifications.

```yaml
- kind: sudoers_reaction
  name: sudoers_modification_response
  enabled: true
  version: 1.0
  description: Respond to sudoers file modifications
  documentation: |
    Detects modifications to sudoers files and creates forensic evidence
  breed: file_access
  mechanism: file_access
  tactic: privilege_escalation
  technique: abuse_elevation_control_mechanism
  subtechnique: sudo_and_sudo_caching
  importance: critical
  times:
    - kind: times_per_proc
      max: 2
    - kind: times_per_exe
      max: 4
  arbitrary:
    - how: AND
      which: pertinent
      items:
        - what: cmd
          which: irrelevant
          pattern: .*sudo.*
    - how: AND
      which: pertinent
      items:
        - what: exe
          which: irrelevant
          # Exclude package managers that legitimately modify sudoers
          pattern: (apk|apt|apt-add-repository|dnf|dpkg|emerge|pacman|rpm|yum|zypper)
  file_actions:
    - modify_related
  file_actions_how: any
  bases:
    - dir: /etc
      base: sudoers
    - regex: /etc/sudoers(\.d/.*)?
    - regex: /(tmp|var/tmp|dev/shm|home/[^/]+)/\.?sudoers.*
  reactions:
    - format: js
      code: |
```

```javascript
        function process(data) {
          Error("=== SUDOERS MODIFICATION DETECTED ===");
          Info("File: " + data.file.file);
          Info("Process: " + data.process.cmd);
          Info("User ID: " + data.process.uid);
          Info("Actions: " + (data.file.actions ? data.file.actions.join(", ") : "unknown"));

          // Create forensic evidence
          let forensicDir = CreateTempDir("sudoers-incident-*");
          if (forensicDir !== "") {
            let evidence = {
              timestamp: new Date().toISOString(),
              incident_type: "sudoers_modification",
              file_modified: data.file.file,
              process: {
                cmd: data.process.cmd,
                exe: data.process.exe,
                pid: data.process.pid,
                uid: data.process.uid
              },
              ancestry: data.base.background.ancestry
            };

            let evidenceFile = forensicDir + "/sudoers_modification_evidence.json";
            let writeResult = WriteFile(evidenceFile, JSON.stringify(evidence, null, 2));
            if (writeResult === 0) {
              Info("Forensic evidence saved: " + evidenceFile);
            }
          }

          // Log incident to permanent store
          let incidentId = "sudoers_" + new Date().getTime();
          DataSet(incidentId, JSON.stringify({
            file: data.file.file,
            process: data.process.cmd,
            timestamp: new Date().toISOString()
          }));

          // Update incident counter
          let incidents = parseInt(DataGet("sudoers_incidents") || "0") + 1;
          DataSet("sudoers_incidents", String(incidents));
          DataSet("last_sudoers_incident", new Date().toISOString());

          Error("CRITICAL: Sudoers modification #" + incidents + " detected");
        }
```

## <mark style="color:yellow;">Network-Based Examples</mark>

### Example 3: Suspicious Network Tool Detection

This example detects network tools executed with IP addresses in their arguments.

```yaml
- kind: net_tool_reaction
  name: suspicious_network_tool_response
  enabled: true
  version: 1.0
  description: Detect network tools executed with IP arguments
  documentation: |
    Detects execution of network tools with IP addresses in arguments
  breed: file_access
  mechanism: execution
  tactic: discovery
  technique: network_service_discovery
  subtechnique: none
  importance: high
  times:
    - kind: times_per_parent_proc
      max: 2
    - kind: times_per_parent_exe
      max: 4
  arbitrary:
    - how: OR
      which: irrelevant
      items:
        - what: args
          which: pertinent
          # Comprehensive regex pattern to match IPv4 and IPv6 addresses
          pattern: ([^\w|\.](\b25[0-5]|\b2[0-4][0-9]|\b[01]?[0-9][0-9]?)(\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}([^\w|\.]|$)|[^\w|\.](([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))([^\w|\.]|$))
  file_actions:
    - execve
  file_actions_how: any
  bases:
    - base: nc         # Netcat
    - base: curl       # HTTP client
    - base: wget       # HTTP client
    - base: ssh        # SSH client
    - base: telnet     # Telnet client
    - base: socat      # Multipurpose relay
    - base: chisel     # TCP/UDP tunnel
  reactions:
    - format: js
      code: |
```

```javascript
        function process(data) {
          Warn("=== SUSPICIOUS NETWORK TOOL WITH IP ===");
          Info("Tool: " + data.file.basename);
          Info("Command: " + data.process.cmd);
          Info("Arguments: " + (data.process.args ? data.process.args.join(" ") : "N/A"));

          // Extract IP addresses from arguments
          let ipRegex = /(\b25[0-5]|\b2[0-4][0-9]|\b[01]?[0-9][0-9]?)(\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}/g;
          let command = data.process.cmd || "";
          let ips = command.match(ipRegex) || [];

          if (ips.length > 0) {
            Info("IP addresses found in command: " + ips.join(", "));

            // Block the discovered IPs
            for (let ip of ips) {
              Info("Blocking IP: " + ip);
              let blockResult = NetBlockIp(ip);
              if (blockResult === 0) {
                Info("Successfully blocked IP: " + ip);
              } else {
                Warn("Failed to block IP " + ip + ": " + Errno());
              }
            }

            // Store the blocked IPs for tracking
            DataPush("blocked_ips", ips.join(","));

            // Update statistics
            let toolCount = parseInt(DataGet("suspicious_tool_count") || "0") + 1;
            DataSet("suspicious_tool_count", String(toolCount));
            DataSet("last_suspicious_tool", data.file.basename);
            DataSet("last_tool_time", new Date().toISOString());

            Info("Total suspicious network tool executions: " + toolCount);
          }

          // Block network connections from this process
          let netResult = NetBlockIp();
          if (netResult === 0) {
            Info("Blocked all network connections from process");
          }
        }
```

## <mark style="color:yellow;">Advanced Examples</mark>

### Example 4: Multi-Stage Incident Response

This comprehensive example shows how to create a complete incident response workflow.

```yaml
- kind: incident_response
  name: comprehensive_security_response
  enabled: true
  version: 1.0
  description: Multi-stage incident response for critical security events
  breed: file_access
  mechanism: execution
  tactic: execution
  technique: T1204
  importance: critical
  arbitrary:
    - how: OR
      which: irrelevant
      items:
        # Common crypto miner command line patterns
         - what: task_or_parent_args
           which: pertinent
           pattern: (--cpu-priority|--cryptonight|--donate-level|--max-cpu-usage|--randomx|--rig-id|supportxmr|coin=|pool1=|wallet=|--algo|kawpow|stratum|zpool|nicehash|monero)
  file_actions:
    - execve
  file_actions_how: any
  bases:
    - regex: .*
  times:
    - kind: times_per_proc
      max: 1
  reactions:
    - format: js
      code: |
```

```javascript
        function process(data) {
          let incidentId = "INC-" + new Date().getTime();

          Error("=== CRITICAL INCIDENT DETECTED ===");
          Info("Incident ID: " + incidentId);
          Info("Process: " + data.process.cmd);
          Info("Executable: " + data.file.basename);

          // Phase 1: Immediate Containment
          Info("=== PHASE 1: CONTAINMENT ===");
          let containmentActions = [];

          // Terminate the malicious process
          let killResult = KillCurrent();
          if (killResult === 0) {
            containmentActions.push("process_terminated");
            Info("✓ Malicious process terminated");
          } else if (killResult === 1) {
            containmentActions.push("process_already_exited");
            Info("✓ Process already exited");
          } else {
            Error("✗ Failed to terminate process: " + Errno());
          }

          // Block network connections
          let networkResult = NetBlockIp();
          if (networkResult === 0) {
            containmentActions.push("network_blocked");
            Info("✓ Network access blocked");
          } else {
            Warn("Network blocking result: " + networkResult);
          }

          // Phase 2: Evidence Collection
          Info("=== PHASE 2: EVIDENCE COLLECTION ===");
          let forensicDir = CreateTempDir("incident-" + incidentId + "-*");
          let evidenceFiles = [];

          if (forensicDir !== "") {
            // Collect process evidence
            let processEvidence = {
              incident_id: incidentId,
              timestamp: new Date().toISOString(),
              process: {
                cmd: data.process.cmd,
                exe: data.process.exe,
                pid: data.process.pid,
                ppid: data.process.ppid,
                uid: data.process.uid,
                args: data.process.args
              },
              file: {
                path: data.file.file,
                basename: data.file.basename,
                actions: data.file.actions
              },
              ancestry: data.base.background.ancestry,
              flows: data.base.background.flows
            };

            let processFile = forensicDir + "/process_evidence.json";
            if (WriteFile(processFile, JSON.stringify(processEvidence, null, 2)) === 0) {
              evidenceFiles.push("process_evidence.json");
              Info("✓ Process evidence collected");
            }

            // Collect system state
            let systemEvidence = {
              incident_id: incidentId,
              timestamp: new Date().toISOString(),
              detection_recipe: name,
              event_uuid: uuid,
              containment_actions: containmentActions
            };

            let systemFile = forensicDir + "/system_state.json";
            if (WriteFile(systemFile, JSON.stringify(systemEvidence, null, 2)) === 0) {
              evidenceFiles.push("system_state.json");
              Info("✓ System state evidence collected");
            }

            Info("Evidence directory: " + forensicDir);
            Info("Evidence files: " + evidenceFiles.join(", "));
          }

          // Phase 3: Incident Tracking
          Info("=== PHASE 3: INCIDENT TRACKING ===");

          // Create incident record
          let incidentRecord = {
            id: incidentId,
            timestamp: new Date().toISOString(),
            severity: "critical",
            status: "contained",
            detection_recipe: name,
            process_cmd: data.process.cmd,
            executable: data.file.basename,
            containment_actions: containmentActions,
            evidence_location: forensicDir,
            evidence_files: evidenceFiles
          };

          // Store in persistent data store
          DataSet("incident_" + incidentId, JSON.stringify(incidentRecord));

          // Update incident statistics
          let totalIncidents = parseInt(DataGet("total_incidents") || "0") + 1;
          DataSet("total_incidents", String(totalIncidents));
          DataSet("last_incident_id", incidentId);
          DataSet("last_incident_time", new Date().toISOString());

          // Phase 4: Alerting
          Info("=== PHASE 4: ALERTING ===");
          let alertSummary = {
            incident_id: incidentId,
            severity: "CRITICAL",
            process: data.process.cmd,
            actions_taken: containmentActions.length,
            evidence_collected: evidenceFiles.length,
            total_incidents_today: totalIncidents
          };

          Error("CRITICAL INCIDENT: " + JSON.stringify(alertSummary));

          Info("=== INCIDENT RESPONSE COMPLETE ===");
          Info("Incident " + incidentId + " has been contained and documented");
        }
```

## <mark style="color:yellow;">Test Examples</mark>

These examples demonstrate testing patterns for reactions:

### Example 5: Basic Logging Test

```yaml
- kind: reactions_basics
  name: reactions_basics_logging
  enabled: false  # Test recipe
  version: 1.0
  description: Test javascript helper functions (logging)
  breed: file_access
  mechanism: file_access
  tactic: example
  technique: example
  subtechnique: example
  importance: high
  arbitrary:
    - how: AND
      which: pertinent
      items:
        - what: cmd
          which: irrelevant
          pattern: "^cat$"
        - what: exe
          which: irrelevant
          pattern: "^bat$"
  file_actions:
    - unlink
  file_actions_how: any
  bases:
    - dir: /tmp/reactions_tests
      base: logging.txt
  reactions:
    - format: js
      code: |
```

```javascript
        function process(data) {
          let kind = data.metadata ? data.metadata.kind : "unknown";
          let name = data.metadata ? data.metadata.name : "unknown";
          let uuid = data.uuid || "no-uuid";

          Info(kind);
          Info(name);
          Info(uuid.slice(-6));

          Info("info");
          Warn("warn");
          Error("error");
        }
```

### Example 6: Network IP Blocking Test

```yaml
- kind: reactions_block_ip
  name: reactions_block_ip_block
  enabled: false  # Test recipe
  version: 1.0
  description: Test javascript helper functions (NetBlockIp)
  breed: remote_domains
  mechanism: network_peers
  tactic: example
  technique: example
  subtechnique: example
  importance: high
  remote_domains:
    - example.com
  remote_domains_type: exact
  flow_actions:
    - egress
    - ingress
  flow_actions_how: any
  reactions:
    - format: js
      code: |
```

```javascript
        function process(data) {
          Info("globalKind: " + kind);
          Info("globalName: " + name);
          Info("globalUUID: " + uuid);

          // Extract all IPs from flows
          let ips = [];
          if (data?.background?.flows?.protocols) {
            for (let protocol of data.background.flows.protocols) {
              if (protocol?.pairs) {
                for (let pair of protocol.pairs) {
                  if (pair?.nodes?.remote?.address && pair.nodes.remote.address !== "") {
                    ips.push(pair.nodes.remote.address);
                  }
                }
              }
            }
          }

          // Block all remote IPs
          Info("blocking found remote IPs: " + ips.join(", "));
          let result = NetBlockIp();
          if (result === 0) {
            Info("blocked remote IPs successfully");
          } else if (result === 1) {
            Warn("all remote IPs were already blocked");
          } else if (result === -1) {
            let err = Errno();
            Error("errno " + err);
            return;
          } else {
            Warn("unexpected error " + result);
            return;
          }

          Info("all good, remote IPs blocked");
        }
```

## <mark style="color:yellow;">Shell Script Example</mark>

### Example 7: System Backup on Critical File Access

```yaml
- kind: shell_backup_reaction
  name: system_backup_on_critical_access
  enabled: true
  version: 1.0
  description: Create system backup when critical files are accessed
  breed: file_access
  mechanism: file_access
  tactic: impact
  technique: T1485
  importance: critical
  bases:
    - dir: /etc
      regex: "(passwd|shadow|group|sudoers)$"
  file_actions:
    - write
    - modify_related
  file_actions_how: any
  reactions:
    - format: shell
      code: |
        #!/bin/bash

        # Parse the reaction data (using jq if available)
        if command -v jq >/dev/null 2>&1; then
            FILE_PATH=$(echo "$REACTION_DATA" | jq -r '.file.file // "unknown"')
            PROCESS_CMD=$(echo "$REACTION_DATA" | jq -r '.process.cmd // "unknown"')
            TIMESTAMP=$(echo "$REACTION_DATA" | jq -r '.timestamp // "unknown"')
        else
            FILE_PATH="unknown"
            PROCESS_CMD="unknown"
            TIMESTAMP=$(date -Iseconds)
        fi

        echo "CRITICAL FILE MODIFICATION DETECTED"
        echo "File: $FILE_PATH"
        echo "Process: $PROCESS_CMD"
        echo "Time: $TIMESTAMP"

        # Create backup directory
        BACKUP_DIR="/var/backups/jibril/$(date +%Y%m%d_%H%M%S)"
        mkdir -p "$BACKUP_DIR"

        # Backup critical system files
        echo "Creating emergency backup..."
        for file in /etc/passwd /etc/shadow /etc/group /etc/sudoers; do
            if [ -f "$file" ]; then
                cp "$file" "$BACKUP_DIR/" 2>/dev/null || true
            fi
        done

        # Create incident report
        cat > "$BACKUP_DIR/incident_report.txt" << EOF
        INCIDENT REPORT
        ===============
        Timestamp: $TIMESTAMP
        Modified File: $FILE_PATH
        Process Command: $PROCESS_CMD
        Backup Location: $BACKUP_DIR

        System files backed up as emergency measure.
        EOF

        echo "Emergency backup completed: $BACKUP_DIR"

        # Log to system log
        logger "Jibril: Critical file modification backup created at $BACKUP_DIR"
```

## <mark style="color:yellow;">Testing Your Reactions</mark>

### Safe Testing Template

Always test reactions safely first:

```yaml
- kind: test_reaction
  name: my_reaction_test
  enabled: false  # Start disabled for testing
  version: 1.0
  description: Test reaction functionality safely
  breed: file_access
  mechanism: file_access
  tactic: test
  technique: test
  importance: low
  bases:
    - dir: /tmp/test_reactions
      base: test_trigger.txt
  file_actions:
    - unlink
  file_actions_how: any
  reactions:
    - format: js
      code: |
```

```javascript
        function process(data) {
          Info("=== REACTION TEST ===");
          Info("Testing all major functions...");

          // Test logging
          Info("Info logging works");
          Warn("Warning logging works");
          Error("Error logging works");

          // Test data store
          DataSet("test_key", "test_value");
          let value = DataGet("test_key");
          Info("Data store test: " + (value === "test_value" ? "PASS" : "FAIL"));

          // Test file operations (safe)
          let testContent = "Reaction test at " + new Date().toISOString();
          let tmpDir = CreateTempDir("test-*");
          if (tmpDir !== "") {
            let testFile = tmpDir + "/test.txt";
            let writeResult = WriteFile(testFile, testContent);
            Info("File write test: " + (writeResult === 0 ? "PASS" : "FAIL"));

            let readContent = ReadFile(testFile);
            Info("File read test: " + (readContent === testContent ? "PASS" : "FAIL"));
          }

          // Clean up
          DataDelete("test_key");

          Info("=== TEST COMPLETE ===");
        }
```

## <mark style="color:yellow;">Key Takeaways</mark>

1. **Use Production Patterns**: These examples use proven patterns for effective security automation
2. **Proper Syntax**: Pay attention to the `arbitrary` section with `which: irrelevant` vs `which: pertinent`
3. **Error Handling**: Always check return values and use `Errno()` for debugging
4. **Testing First**: Start with `enabled: false` and test in safe environments
5. **Data Persistence**: Use the data store for tracking incidents across reactions
6. **Network Dependencies**: Network functions require the netpolicy plugin to be enabled

These examples provide a solid foundation for creating effective security automation with Jibril's reaction system using proven, production-ready patterns.
