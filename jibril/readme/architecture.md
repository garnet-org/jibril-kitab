---
icon: archway
---

# Architecture

## <mark style="color:yellow;">Overview</mark> <a href="#overview" id="overview"></a>

***

Jibril is a modular runtime security tool that combines an **eBPF loader** and a **userland daemon** to monitor, detect, and respond to system behaviors. Its design emphasizes **extensibility** through **plugins**, **printers**, and **events**, all controlled by a centralized configuration file. This architecture ensures flexibility while maintaining a low resource footprint.

## <mark style="color:yellow;">Key Components</mark> <a href="#id-1-key-components" id="id-1-key-components"></a>

***

### <mark style="color:yellow;">eBPF Loader</mark>

_Foundation for kernel-level operations_

* **Binary Generation**\
  Creates optimized binaries incorporating one or more extensions
* **Extensibility**\
  Supports feature expansion through simple source tree additions
* **Core Functionality**\
  Serves dual purpose as primary loader and default extension

### <mark style="color:yellow;">Agent</mark>

_Userland processing engine_

* **Extensions**\
  Define core features and system integrations
* **Plugins**\
  Execute specialized detection and monitoring functions
* **Printers**\
  Handle output routing to logs, files, and APIs
* **Events**\
  Capture, process, and dispatch system behaviors and conditions

This modular architecture ensures both flexibility and performance, allowing Jibril to maintain comprehensive visibility while adapting to evolving security requirements.

## <mark style="color:yellow;">Execution Flow</mark> <a href="#id-2-execution-flow" id="id-2-execution-flow"></a>

***

Jibril components follow a structured execution order:

1. **Initialization:** Core libraries and packages are initialized first.
2. **Extensions:** Load features like configuration or data storage logic.
3. **Plugins:** Execute monitoring or detection tasks.
4. **Printers:** Process and output event data.
5. **Events:** Dispatch captured behaviors to active printers.

Each component runs through five lifecycle stages: `init`, `start`, `execute`, `finish`, and `exit`, ensuring stability and clear state management.

## <mark style="color:yellow;">Modular Design</mark> <a href="#id-3-modular-design-plugins-printers-and-events" id="id-3-modular-design-plugins-printers-and-events"></a>

***

### <mark style="color:yellow;">Plugins</mark> <a href="#id-31-plugins" id="id-31-plugins"></a>

Plugins add specialized functionality to Jibril, focusing on monitoring, detection, and system analysis. All plugins can be enabled or disabled in the configuration file. Examples include:

* **Hold:** Keeps Jibril running until receiving a termination signal (e.g., `SIGSTOP`).
* **Procfs:** Reads data from existing processes in `/proc`, allowing Jibril to analyze both historical and real-time process activity.
* **Net:** Monitors network flows, capturing details about active connections and traffic.
* **Detect:** Provides extensive detection capabilities, such as monitoring file modifications, unauthorized code execution, and suspicious network activity.
* **GitHub:** Integrates with GitHub repositories to summarize pull requests or changes.

### <mark style="color:yellow;">Printers</mark> <a href="#id-32-printers" id="id-32-printers"></a>

Printers define how and where events are output. They are highly configurable and support various endpoints, including:

* **Stdout:** Prints event data directly to the console for immediate visibility.
* **Varlog:** Outputs events to log files in `/var/log` for persistent storage.
* **Listendev:** Sends data to the `dashboard.listen.dev` for real-time visualization.
* **Datakeeper:** Maintains a recent history of events in memory for quick lookups by other components.

Some printers like `datakeeper` are used as infrastructure for other components, not as regular event-dispatching printers.

### <mark style="color:yellow;">Events</mark> <a href="#id-33-events" id="id-33-events"></a>

Events represent system behaviors or states that Jibril monitors and processes. They are the core of Jibril's detection and response capabilities. Some examples:

* **Network Flows**
  * `jibril:detect:flow`\
    Captures detailed information about active network flows.
* **Network Policy Drops**
  * `jibril:netpolicy:dropip`\
    Flags traffic dropped due to IP-based policies.
* **File Access:**
  * `jibril:detect:capabilities_modification`\
    Detects changes to file capabilities.
  * `jibril:detect:credentials_files_access`\
    Identifies unauthorized access to sensitive credential files.
* **Execution Monitoring:**
  * `jibril:detect:hidden_elf_exec`\
    Detects hidden ELF binary execution.
  * `jibril:detect:binary_executed_by_loader`\
    Tracks executions made by ELF loaders.
* **Network Activity:**
  * `jibril:detect:net_scan_tool_exec`\
    Flags usage of network scanning utilities.
  * `jibril:detect:net_sniff_tool_exec`\
    Identifies execution of network-sniffing tools.
* **GitHub Integration Events:**
  * `jibril:github:pull_summary`:\
    Summarizes pull requests.
  * `jibril:github:change_summary`:\
    Highlights changes in repositories.

## <mark style="color:yellow;">Configuration-Driven Behavior</mark> <a href="#id-4-configuration-driven-behavior" id="id-4-configuration-driven-behavior"></a>

***

Jibril’s flexibility comes from its configuration file, which governs how components are enabled and interact. Key configurable elements include:

* **Log Levels:** Control verbosity, ranging from minimal output (`fatal`) to detailed debugging (`debug`).
* **Daemon Mode:** Run Jibril interactively or as a background service.
* **Profiling and Health Checks:** Enable profiling to debug performance or activate health endpoints for system monitoring.
* **Extensions and Plugins:** Select which extensions, plugins, and events to load, tailoring Jibril for specific use cases.
* **Printers:** Define where and how data should be output, such as stdout, log files, or external dashboards.

These options allow Jibril to integrate seamlessly into various operational environments.

## <mark style="color:yellow;">Why Jibril’s Architecture Works</mark> <a href="#id-5-why-jibrils-architecture-works" id="id-5-why-jibrils-architecture-works"></a>

***

**Flexibility**

* Configurable plugins, printers, and events
* Enable/disable components based on specific needs
* Tailor monitoring scope to organizational requirements

**Scalability**

* Seamlessly scales from single systems to enterprise deployments
* Consistent performance across diverse environments
* Resource-efficient even in high-density infrastructures

**Efficiency**

* eBPF-powered kernel-level data collection minimizes overhead
* Structured userland execution optimizes resource utilization
* Maintains minimal footprint even under heavy monitoring loads

**Comprehensive Visibility**

* Complete coverage across network, file, and process domains
* Unified view of system activity and security events
* Detailed context for accurate threat assessment

**Enterprise Integration**

* Ready-to-use connectivity with existing security infrastructure
* Flexible output options for dashboards, SIEM systems, and logs
* API-friendly architecture for custom tool integration

## <mark style="color:yellow;">Conclusion</mark> <a href="#conclusion" id="conclusion"></a>

***

Jibril combines the power of eBPF with a modular, extensible framework to deliver advanced runtime security monitoring. Its architecture balances flexibility, efficiency, and ease of use, making it a robust solution for detecting and responding to threats in modern IT environments. Whether monitoring network flows, detecting file access anomalies, or integrating with GitHub workflows, Jibril offers the tools needed to secure your systems effectively.
