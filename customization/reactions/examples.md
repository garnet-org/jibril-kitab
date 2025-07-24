---
icon: lightbulb
---

# Reaction Examples

This document provides practical, real-world examples of how to use reactions to create powerful automated security responses. Each example includes the complete YAML configuration and JavaScript code.

## <mark style="color:yellow;">Basic Examples</mark>

### Example 1: Simple Logging Reaction

This basic example logs information about file access events.

```yaml
- kind: file_access_monitor
  name: log_sensitive_files
  enabled: true
  version: 1.0
  description: Log access to sensitive files
  breed: file_access
  mechanism: file_access
  tactic: collection
  technique: T1005
  importance: medium
  bases:
    - dir: /etc
      regex: "passwd|shadow|sudoers"
  file_actions:
    - read
    - write
  file_actions_how: any
  reactions:
    - format: js
      code: |
        function process(data) {
          Info("=== SENSITIVE FILE ACCESS ===");
          Info("File: " + data.file.file);
          Info("Process: " + data.process.cmd);
          Info("User: " + data.process.uid);
          Info("Actions: " + data.file.actions.join(", "));
          Info("Timestamp: " + data.timestamp);
        }
```

### Example 2: Network Blocking Reaction

Automatically block suspicious network connections.

```yaml
- kind: malicious_network_block
  name: block_c2_domains
  enabled: true
  version: 1.0
  description: Block connections to known C2 domains
  breed: remote_domains
  mechanism: network_peers
  tactic: command_and_control
  technique: T1071
  importance: high
  remote_domains:
    - malware-c2.com
    - evil-server.net
    - suspicious-domain.org
  remote_domains_type: exact
  flow_actions:
    - egress
  reactions:
    - format: js
      code: |
        function process(data) {
          Info("Blocking malicious domain connection");
          
          // Block all domains from this event
          let result = NetBlockDomain();
          if (result === 0) {
            Info("Successfully blocked C2 domains");
            
            // Log the incident
            DataSet("last_c2_block", new Date().toISOString());
            
            // Count blocked attempts
            let count = parseInt(DataGet("c2_block_count") || "0") + 1;
            DataSet("c2_block_count", String(count));
            
            Warn("Total C2 blocks: " + count);
          } else {
            Error("Failed to block domains: " + Errno());
          }
        }
```

## <mark style="color:yellow;">Intermediate Examples</mark>

### Example 3: Process Termination with Forensics

Terminate malicious processes while collecting evidence.

```yaml
- kind: malware_execution
  name: terminate_cryptominer
  enabled: true
  version: 1.0
  description: Detect and terminate cryptocurrency miners
  breed: execution
  mechanism: execution
  tactic: impact
  technique: T1496
  importance: high
  arbitrary:
    - how: OR
      which: pertinent
      items:
        - what: cmd
          which: contains
          pattern: "xmrig|cpuminer|ethminer"
        - what: exe
          which: contains
          pattern: "miner"
  reactions:
    - format: js
      code: |
        function process(data) {
          Info("=== CRYPTOCURRENCY MINER DETECTED ===");
          Info("Command: " + data.process.cmd);
          Info("PID: " + data.process.pid);
          Info("Parent: " + data.process.ppid);
          
          // Create forensic directory
          let forensicDir = CreateTempDir("cryptominer-*");
          if (forensicDir !== "") {
            // Collect evidence
            let evidence = {
              timestamp: new Date().toISOString(),
              event_id: uuid,
              process: {
                pid: data.process.pid,
                ppid: data.process.ppid,
                cmd: data.process.cmd,
                exe: data.process.exe,
                uid: data.process.uid
              },
              ancestry: data.base.background.ancestry,
              network_flows: data.base.background.flows
            };
            
            // Write evidence to file
            let evidenceFile = forensicDir + "/miner_evidence.json";
            let writeResult = WriteFile(evidenceFile, JSON.stringify(evidence, null, 2));
            if (writeResult === 0) {
              Info("Evidence collected: " + evidenceFile);
            }
          }
          
          // Terminate the miner
          let killResult = KillCurrent();
          if (killResult === 0) {
            Info("Cryptocurrency miner terminated");
            
            // Update statistics
            let minerCount = parseInt(DataGet("miners_terminated") || "0") + 1;
            DataSet("miners_terminated", String(minerCount));
            DataSet("last_miner_kill", new Date().toISOString());
            
            Warn("Total miners terminated: " + minerCount);
          } else {
            Error("Failed to terminate miner: " + Errno());
          }
          
          // Block any network connections from this process
          let blockResult = NetBlockIp();
          if (blockResult === 0) {
            Info("Blocked miner network connections");
          }
        }
```

### Example 4: Escalating Response System

Implement a graduated response based on threat severity and frequency.

```yaml
- kind: escalating_response
  name: progressive_threat_response
  enabled: true
  version: 1.0
  description: Escalating response to repeated suspicious activities
  breed: file_access
  mechanism: file_access
  tactic: persistence
  technique: T1547
  importance: medium
  bases:
    - dir: /etc/systemd/system
      regex: ".*\\.service$"
  file_actions:
    - write
    - create
  reactions:
    - format: js
      code: |
        function process(data) {
          let serviceName = data.file.basename;
          let processCmd = data.process.cmd;
          
          Info("Service file modification detected: " + serviceName);
          Info("Modified by: " + processCmd);
          
          // Track incidents per process
          let incidentKey = "incidents_" + data.process.exe;
          let incidentCount = parseInt(DataGet(incidentKey) || "0") + 1;
          DataSet(incidentKey, String(incidentCount));
          
          // Escalation logic
          if (incidentCount === 1) {
            // Level 1: Log and monitor
            Info("LEVEL 1 RESPONSE: First incident - monitoring");
            DataSet("first_incident_" + data.process.exe, new Date().toISOString());
            
          } else if (incidentCount === 2) {
            // Level 2: Block network access
            Info("LEVEL 2 RESPONSE: Second incident - blocking network");
            let blockResult = NetBlockIp();
            if (blockResult === 0) {
              Info("Network access blocked for repeat offender");
            }
            
          } else if (incidentCount >= 3) {
            // Level 3: Terminate process
            Info("LEVEL 3 RESPONSE: Multiple incidents - terminating process");
            let killResult = KillCurrent();
            if (killResult === 0) {
              Info("Persistent threat terminated");
              
              // Log the escalation
              let escalationData = {
                process: processCmd,
                incident_count: incidentCount,
                escalation_level: 3,
                timestamp: new Date().toISOString()
              };
              
              WriteFile("/var/log/security/escalations.log", 
                       JSON.stringify(escalationData) + "\n");
            }
          }
          
          // Always log the current incident
          let logEntry = {
            timestamp: new Date().toISOString(),
            service_file: serviceName,
            process: processCmd,
            incident_number: incidentCount,
            response_level: Math.min(incidentCount, 3)
          };
          
          WriteFile("/var/log/security/service_modifications.log",
                   JSON.stringify(logEntry) + "\n");
        }
```

## <mark style="color:yellow;">Advanced Examples</mark>

### Example 5: Comprehensive Incident Response

A complete incident response system with evidence collection, containment, and notification.

```yaml
- kind: advanced_incident_response
  name: comprehensive_malware_response
  enabled: true
  version: 1.0
  description: Full incident response for malware detection
  breed: execution
  mechanism: execution
  tactic: execution
  technique: T1204
  importance: critical
  arbitrary:
    - how: OR
      which: pertinent
      items:
        - what: cmd
          which: contains
          pattern: "powershell.*-enc.*"
        - what: cmd
          which: contains
          pattern: "curl.*|.*wget.*"
        - what: exe
          which: contains
          pattern: "/tmp/.*"
  reactions:
    - format: js
      code: |
        function process(data) {
          let incidentId = "INC-" + new Date().getTime();
          
          Info("=== CRITICAL INCIDENT DETECTED ===");
          Info("Incident ID: " + incidentId);
          Info("Command: " + data.process.cmd);
          
          // Phase 1: Immediate Containment
          Info("Phase 1: Immediate Containment");
          
          // Block all network traffic from this process
          let networkBlocked = NetBlockIp();
          let containmentActions = [];
          
          if (networkBlocked === 0) {
            containmentActions.push("network_blocked");
            Info("✓ Network traffic blocked");
          }
          
          // Terminate the malicious process
          let processKilled = KillCurrent();
          if (processKilled === 0) {
            containmentActions.push("process_terminated");
            Info("✓ Malicious process terminated");
          }
          
          // Phase 2: Evidence Collection
          Info("Phase 2: Evidence Collection");
          
          let forensicDir = CreateTempDir("incident-" + incidentId + "-*");
          let evidenceCollected = [];
          
          if (forensicDir !== "") {
            // Collect process information
            let processEvidence = {
              pid: data.process.pid,
              ppid: data.process.ppid,
              cmd: data.process.cmd,
              exe: data.process.exe,
              args: data.process.args,
              uid: data.process.uid,
              start_time: data.process.start,
              ancestry: data.base.background.ancestry
            };
            
            WriteFile(forensicDir + "/process_info.json", 
                     JSON.stringify(processEvidence, null, 2));
            evidenceCollected.push("process_info");
            
            // Collect network information
            if (data.base.background.flows) {
              WriteFile(forensicDir + "/network_flows.json", 
                       JSON.stringify(data.base.background.flows, null, 2));
              evidenceCollected.push("network_flows");
            }
            
            // Collect system state
            let systemState = {
              timestamp: new Date().toISOString(),
              hostname: "system-hostname", // Would be dynamic in real scenario
              incident_id: incidentId,
              detection_recipe: name,
              event_uuid: uuid
            };
            
            WriteFile(forensicDir + "/system_state.json", 
                     JSON.stringify(systemState, null, 2));
            evidenceCollected.push("system_state");
            
            Info("✓ Evidence collected in: " + forensicDir);
            Info("✓ Evidence types: " + evidenceCollected.join(", "));
          }
          
          // Phase 3: Incident Tracking
          Info("Phase 3: Incident Tracking");
          
          // Update incident database
          let incidentRecord = {
            id: incidentId,
            timestamp: new Date().toISOString(),
            severity: "critical",
            status: "contained",
            process: data.process.cmd,
            containment_actions: containmentActions,
            evidence_location: forensicDir,
            evidence_types: evidenceCollected
          };
          
          // Store incident in data store
          DataSet("incident_" + incidentId, JSON.stringify(incidentRecord));
          
          // Update incident counters
          let totalIncidents = parseInt(DataGet("total_incidents") || "0") + 1;
          DataSet("total_incidents", String(totalIncidents));
          DataSet("last_incident", incidentId);
          DataSet("last_incident_time", new Date().toISOString());
          
          // Write to central incident log
          WriteFile("/var/log/security/incidents.log", 
                   JSON.stringify(incidentRecord) + "\n");
          
          // Phase 4: Alerting and Reporting
          Info("Phase 4: Alerting");
          
          let alertSummary = {
            incident_id: incidentId,
            severity: "CRITICAL",
            process: data.process.cmd,
            actions_taken: containmentActions.length,
            evidence_collected: evidenceCollected.length,
            total_incidents_today: totalIncidents
          };
          
          // Log alert (in real scenario, this might trigger external notifications)
          Error("CRITICAL INCIDENT ALERT: " + JSON.stringify(alertSummary));
          
          // Emergency shutdown for critical threats
          if (data.process.cmd.includes("rm -rf") || 
              data.process.cmd.includes("format")) {
            Warn("DESTRUCTIVE COMMAND DETECTED - INITIATING EMERGENCY SHUTDOWN");
            PowerOff();
          }
          
          Info("=== INCIDENT RESPONSE COMPLETE ===");
          Info("Incident ID: " + incidentId + " - Status: CONTAINED");
        }
```

### Example 6: Threat Intelligence Integration

Integrate with threat intelligence data for enhanced decision making.

```yaml
- kind: threat_intel_reaction
  name: intel_driven_blocking
  enabled: true
  version: 1.0
  description: Use threat intelligence for smart blocking decisions
  breed: remote_domains
  mechanism: network_peers
  tactic: command_and_control
  technique: T1071
  importance: high
  flow_actions:
    - egress
  reactions:
    - format: js
      code: |
        function process(data) {
          Info("Analyzing network connection with threat intelligence");
          
          // Extract connection details
          let remoteIps = [];
          let remoteDomains = [];
          
          if (data.background && data.background.flows && 
              data.background.flows.protocols) {
            for (let protocol of data.background.flows.protocols) {
              if (protocol.pairs) {
                for (let pair of protocol.pairs) {
                  if (pair.nodes && pair.nodes.remote) {
                    if (pair.nodes.remote.address) {
                      remoteIps.push(pair.nodes.remote.address);
                    }
                    if (pair.nodes.remote.names) {
                      remoteDomains = remoteDomains.concat(pair.nodes.remote.names);
                    }
                  }
                }
              }
            }
          }
          
          // Threat intelligence lookup simulation
          // In real scenario, this would query actual threat intel APIs
          let threatScore = 0;
          let threatIndicators = [];
          
          // Check domains against known malicious patterns
          for (let domain of remoteDomains) {
            if (domain.includes("bit.ly") || domain.includes("tinyurl.com")) {
              threatScore += 3;
              threatIndicators.push("url_shortener");
            }
            if (domain.match(/[0-9]{8,}\.com$/)) {
              threatScore += 5;
              threatIndicators.push("dga_domain");
            }
            if (domain.includes("onion")) {
              threatScore += 7;
              threatIndicators.push("tor_domain");
            }
          }
          
          // Check IPs against suspicious ranges
          for (let ip of remoteIps) {
            if (ip.startsWith("10.") || ip.startsWith("192.168.")) {
              // Private IP - could be lateral movement
              threatScore += 2;
              threatIndicators.push("private_ip");
            }
          }
          
          // Process-based indicators
          let processCmd = data.process ? data.process.cmd : "";
          if (processCmd.includes("curl") || processCmd.includes("wget")) {
            threatScore += 2;
            threatIndicators.push("download_tool");
          }
          
          // Risk-based response
          Info("Threat Score: " + threatScore);
          Info("Indicators: " + threatIndicators.join(", "));
          
          let responseAction = "none";
          
          if (threatScore >= 10) {
            // High threat - immediate blocking and termination
            responseAction = "block_and_kill";
            Error("HIGH THREAT DETECTED - Score: " + threatScore);
            
            let blockResult = NetBlockIp();
            let killResult = KillCurrent();
            
            if (blockResult === 0 && killResult === 0) {
              Info("High threat contained - network blocked and process killed");
            }
            
          } else if (threatScore >= 5) {
            // Medium threat - network blocking only
            responseAction = "block_network";
            Warn("MEDIUM THREAT DETECTED - Score: " + threatScore);
            
            let blockResult = NetBlockIp();
            if (blockResult === 0) {
              Info("Medium threat contained - network blocked");
            }
            
          } else if (threatScore >= 1) {
            // Low threat - monitoring only
            responseAction = "monitor";
            Info("LOW THREAT DETECTED - Score: " + threatScore + " - Monitoring");
          }
          
          // Update threat intelligence database
          let intelRecord = {
            timestamp: new Date().toISOString(),
            event_id: uuid,
            remote_ips: remoteIps,
            remote_domains: remoteDomains,
            threat_score: threatScore,
            indicators: threatIndicators,
            response_action: responseAction,
            process: processCmd
          };
          
          DataSet("intel_" + uuid, JSON.stringify(intelRecord));
          
          // Update statistics
          let totalAnalyzed = parseInt(DataGet("total_analyzed") || "0") + 1;
          DataSet("total_analyzed", String(totalAnalyzed));
          
          if (threatScore > 0) {
            let threatsDetected = parseInt(DataGet("threats_detected") || "0") + 1;
            DataSet("threats_detected", String(threatsDetected));
            
            Warn("Threat detection rate: " + threatsDetected + "/" + totalAnalyzed);
          }
          
          // Log to threat intelligence file
          WriteFile("/var/log/security/threat_intel.log", 
                   JSON.stringify(intelRecord) + "\n");
        }
```

## <mark style="color:yellow;">Shell Script Examples</mark>

### Example 7: Shell Script Reaction

Sometimes shell scripts provide more flexibility for system operations.

```yaml
- kind: shell_based_response
  name: system_backup_on_threat
  enabled: true
  version: 1.0
  description: Create system backup when critical files are modified
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
  reactions:
    - format: shell
      code: |
        #!/bin/bash
        
        # Parse the reaction data
        FILE_PATH=$(echo "$REACTION_DATA" | jq -r '.file.file')
        PROCESS_CMD=$(echo "$REACTION_DATA" | jq -r '.process.cmd')
        TIMESTAMP=$(echo "$REACTION_DATA" | jq -r '.timestamp')
        
        echo "CRITICAL FILE MODIFICATION DETECTED"
        echo "File: $FILE_PATH"
        echo "Process: $PROCESS_CMD"
        echo "Time: $TIMESTAMP"
        
        # Create backup directory
        BACKUP_DIR="/var/backups/jibril/$(date +%Y%m%d_%H%M%S)"
        mkdir -p "$BACKUP_DIR"
        
        # Backup critical system files
        echo "Creating emergency backup..."
        cp /etc/passwd "$BACKUP_DIR/"
        cp /etc/shadow "$BACKUP_DIR/"
        cp /etc/group "$BACKUP_DIR/"
        cp /etc/sudoers "$BACKUP_DIR/"
        
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
        
        # Optional: Send alert email (if mail is configured)
        if command -v mail >/dev/null 2>&1; then
            echo "Critical file modification detected on $(hostname)" | \
            mail -s "JIBRIL SECURITY ALERT" admin@company.com
        fi
```

## <mark style="color:yellow;">Testing Your Reactions</mark>

### Safe Testing Environment

Always test reactions in a safe environment first. Here's an example test reaction:

```yaml
- kind: test_reaction
  name: reaction_test
  enabled: false  # Start with disabled
  version: 1.0
  description: Test reaction functionality
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
  reactions:
    - format: js
      code: |
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
          let writeResult = WriteFile("/tmp/reaction_test.log", testContent);
          Info("File write test: " + (writeResult === 0 ? "PASS" : "FAIL"));
          
          let readContent = ReadFile("/tmp/reaction_test.log");
          Info("File read test: " + (readContent.includes("Reaction test") ? "PASS" : "FAIL"));
          
          // Clean up
          DataDelete("test_key");
          
          Info("=== TEST COMPLETE ===");
        }
```

### Test Script

Create this test script to trigger your test reaction:

```bash
#!/bin/bash
# test_reaction.sh

# Create test directory
mkdir -p /tmp/test_reactions

# Create the trigger file
touch /tmp/test_reactions/test_trigger.txt

# Wait a moment
sleep 1

# Remove the file to trigger the reaction
rm /tmp/test_reactions/test_trigger.txt

echo "Test trigger sent - check Jibril logs for reaction output"
```

## <mark style="color:yellow;">Best Practices Summary</mark>

1. **Start Simple**: Begin with basic logging reactions before implementing complex logic
2. **Test Thoroughly**: Always test in a safe environment first
3. **Error Handling**: Check return values and use `Errno()` for debugging
4. **Logging**: Log all significant actions for audit trails
5. **Data Persistence**: Use the data store for maintaining state across reactions
6. **Performance**: Keep reactions lightweight to avoid impacting system performance
7. **Security**: Validate all inputs and avoid exposing sensitive information in logs
8. **Documentation**: Document your reactions clearly for maintenance

These examples provide a foundation for building powerful automated security responses with Jibril's reaction system. Adapt and extend them based on your specific security requirements and environment.
