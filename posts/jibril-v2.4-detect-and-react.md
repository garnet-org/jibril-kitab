---
description: Programmable JavaScript Reactions to OS Security Events
icon: right-left-large
---

# Jibril v2.4: Detect & React

We've just released Jibril v2.4 with a new "Reactions" system that fundamentally changes how runtime security works. Instead of just detecting and alerting, you can now write JavaScript code that automatically executes in response to real-time OS security events - [https://jibril.garnet.ai/customization/reactions](../customization/reactions/)

### 🔄 From Detection to Action in Milliseconds

Gone are the days of "detect and alert." Jibril v2.4 introduces intelligent, programmable responses that execute automatically when threats are detected:

✅ **Instant Process Termination** - Stop malicious processes\
✅ **Real-time Network Blocking** - Cut off communications immediately\
✅ **Automated Evidence Collection** - Capture forensic data\
✅ **Smart Containment** - Isolate compromised systems

### 🎯 Use Cases That Matter

✨ Cryptocurrency miner detection & termination\
✨ Privilege escalation prevention\
✨ Suspicious network tool containment\
✨ System file tampering response\
✨ Multi-stage incident response workflows

### 🛡️ Production-Ready Security

Built from the ground up for enterprise environments:

* Each reaction runs in isolated contexts
* Comprehensive error handling and logging
* Performance-optimized execution (sub-second response times)
* Extensive testing and validation frameworks

### ⚙️ How it works

Jibril monitors the OS (file access, process execution, network activity, specific kernel logic) and when security events match detection rules, after being printed to enabled printers, JavaScript reactions are triggered. They run in isolated V8 contexts with direct access to system operations:

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

  # Reactions configuration
  reactions:
    - format: js  # or "shell"
      code: |
        # JavaScript function here
    - format: shell
      code: |
        # Shell script here
```

### 💻 The reaction code:

```javascript
function process(data) {
    // Multi-stage response to crypto miner detection
    if (data.file.basename.match(/^(xmrig|ethminer|cgminer)$/)) {
        Error("Crypto miner detected: " + data.process.cmd);
        
        // Immediate containment
        KillCurrent(); // Terminate process
        NetBlockIp(); // Block network
        
        // Evidence collection
        let dir = CreateTempDir("miner-incident-*");
        let evidence = {
            timestamp: new Date().toISOString(),
            process_ancestry: data.base.background.ancestry,
            command_line: data.process.cmd
        };
        WriteFile(dir + "/evidence.json", JSON.stringify(evidence));
        
        // Track incidents
        let count = parseInt(DataGet("miners_terminated") || "0") + 1;
        DataSet("miners_terminated", String(count));
        Info("Miner #" + count + " terminated and blocked");
    }
}
```

### 🔧 Technical capabilities

Jibril provides a comprehensive API with **25+ helper functions**:

* **Process management**: `KillCurrent()`, `KillParent()`, `KillProcess(pid)` with safety controls
* **Network policy**: `NetBlockIp()`, `NetBlockDomain()`, `NetBlockIpTimer()` for real-time blocking
* **File operations**: `ReadFile()`, `WriteFile()`, `CreateTempDir()` with secure permissions
* **Data persistence**: Key-value store surviving across executions
* **Emergency controls**: `PowerOff()`, `Panic()` for critical threats

Each reaction runs in isolated V8 context with error handling, executes in milliseconds, handles concurrent execution automatically, and provides audit trails.

**Examples**: https://github.com/garnet-org/jibril-wahy/tree/main/jibril/tests

### 🚀 Beyond simple automation

The programmability enables sophisticated logic:

* **Graduated responses**: Start with logging, escalate to blocking, terminate as last resort
* **Context-aware decisions**: Block external IPs but whitelist internal infrastructure
* **Cross-event correlation**: Track patterns across multiple security events
* **Custom evidence collection**: Automatically gather exactly the forensic data you need

Reactions are defined in YAML alongside detection rules, so response logic stays coupled with detection logic. Start conservative and gradually increase automation.

### 🎪 Why this approach matters

Traditional tools detect threats but still require human analysts to respond. This creates a gap where threats continue running while humans investigate. By making response programmable and immediate, you can stop threats in their tracks while maintaining human oversight.

The isolation model means reactions can safely perform powerful operations (including system shutdown) without risking the host system if JavaScript code has bugs.

### 📚 Full documentation

* [https://jibril.garnet.ai/customization/reactions](../customization/reactions/)
* [https://jibril.garnet.ai/customization/alchemies](../customization/alchemies/)
* [https://jibril.garnet.ai/customization/attenuator](../customization/attenuator.md)

### 🤝 Follow us

* Let's connect!
* Meet us at **BlackHat**!
* [https://jibril.garnet.ai](https://jibril.garnet.ai/)

**Have fun!** 🎉
