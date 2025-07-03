---
description: Hijack Execution Flow [T1574]
icon: play
---

# Hijack Execution Flow

## Information

* Name: Hijack Execution Flow
* ID: T1574
* Tactics: [TA0003](../../ta0003/), [TA0004](../../ta0004/), [TA0005](../)
* Sub-Technique: [T1574.007](t1574.007.md), [T1574.011](t1574.011.md), [T1574.001](t1574.001.md), [T1574.014](t1574.014.md), [T1574.008](t1574.008.md), [T1574.006](t1574.006.md), [T1574.005](t1574.005.md), [T1574.010](t1574.010.md), [T1574.013](t1574.013.md), [T1574.009](t1574.009.md), [T1574.002](t1574.002.md), [T1574.004](t1574.004.md), [T1574.012](t1574.012.md)

## Introduction

Hijack Execution Flow is a technique categorized under the MITRE ATT\&CK framework (T1574) used by adversaries to manipulate or intercept the normal execution flow of programs or processes. Attackers exploit vulnerabilities or leverage legitimate system features to redirect execution paths, allowing malicious code to run undetected or escalate privileges. This technique encompasses various methods including DLL injection, DLL search order hijacking, and process hollowing, and is frequently leveraged to maintain persistence, evade detection, or escalate privileges within compromised systems.

## Deep Dive Into Technique

Hijack Execution Flow involves manipulating the intended execution path of software or operating system processes to execute attacker-controlled code. Below are common methods and mechanisms:

1. **DLL Injection**
   * Attackers insert malicious code into a legitimate running process by injecting a Dynamic Link Library (DLL).
   * Common injection techniques:
     * Remote thread injection via Windows API calls (`CreateRemoteThread`, `WriteProcessMemory`).
     * Reflective DLL injection (loading DLLs directly into memory without disk writes).
     * Process hollowing (starting a legitimate process in suspended mode and replacing its code).
2. **DLL Search Order Hijacking**
   * Exploits the Windows DLL search order mechanism.
   * Attackers place malicious DLLs in directories searched before legitimate DLL locations.
   * Commonly exploited directories include application directories, current working directories, and system paths.
3. **Executable File Manipulation**
   * Attackers overwrite or modify legitimate executables or scripts to execute malicious code.
   * Techniques include binary patching, script modification, or replacing legitimate files with trojanized versions.
4. **Dynamic Linker Hijacking (Linux/Unix Systems)**
   * Attackers manipulate environment variables (e.g., `LD_PRELOAD`, `LD_LIBRARY_PATH`) to load malicious libraries before legitimate ones.
   * Allows attackers to intercept library calls and execute malicious code transparently.
5. **Thread Execution Hijacking**
   * Attackers manipulate threads of legitimate processes to execute malicious code, often through code injection or API hooking.

## When this Technique is Usually Used

Attackers typically leverage Hijack Execution Flow during multiple stages of an attack lifecycle, including:

* **Execution Stage**
  * Execute malicious payloads within the context of legitimate processes, bypassing security controls.
* **Persistence Stage**
  * Maintain persistent access by embedding malicious code into legitimate processes or libraries that execute automatically on system startup.
* **Privilege Escalation Stage**
  * Exploit trusted processes or services running with higher privileges to escalate permissions.
* **Defense Evasion Stage**
  * Conceal malicious activities by embedding within legitimate processes, reducing visibility and detection.
* **Credential Access Stage**
  * Hijack execution flow of processes handling credentials (e.g., browsers, email clients) to intercept sensitive information.
* **Lateral Movement Stage**
  * Inject malicious code into legitimate network management or remote administration tools to move laterally within the network.

## How this Technique is Usually Detected

Detection of Hijack Execution Flow techniques involves multiple approaches and indicators:

* **Behavioral Monitoring**
  * Monitor abnormal process behaviors, such as unexpected DLL loads, unusual parent-child process relationships, and suspicious API calls.
* **Endpoint Detection and Response (EDR) Tools**
  * Identify suspicious process injections, memory modifications, or DLL load events.
  * Examples: CrowdStrike Falcon, Carbon Black, Microsoft Defender for Endpoint.
* **File Integrity Monitoring (FIM)**
  * Detect unauthorized modifications to critical system files, executables, or libraries.
  * Tools: Tripwire, OSSEC, AIDE.
* **System and Application Logs**
  * Analyze logs for unusual DLL loading events, unexpected process creations, or environmental variable manipulations.
* **Memory Forensics**
  * Inspect memory dumps for injected code, abnormal thread activity, or suspicious memory allocations.
* **Specific Indicators of Compromise (IoCs)**
  * Suspicious DLLs located in unusual paths or directories.
  * Unexpected environment variable settings (e.g., `LD_PRELOAD`, `LD_LIBRARY_PATH`).
  * Processes with unusual loaded modules or threads executing from suspicious memory regions.
  * Changes in registry keys related to DLL search order (`SafeDllSearchMode`).

## Why it is Important to Detect This Technique

Early detection of Hijack Execution Flow is crucial due to its severe potential impacts on systems and networks:

* **Persistence and Long-term Compromise**
  * Attackers use this technique to establish persistent footholds, complicating incident remediation.
* **Privilege Escalation and System Control**
  * Allows attackers to escalate privileges and gain full control over compromised systems.
* **Credential Theft and Sensitive Data Exfiltration**
  * Facilitates interception of sensitive information, credentials, and intellectual property.
* **Defense Evasion**
  * Enables attackers to evade detection by embedding malicious code within legitimate processes, complicating forensic analysis.
* **Operational Disruption and Data Integrity**
  * Malicious code execution can disrupt critical business operations, corrupt data, or degrade system performance.
* **Regulatory and Compliance Risks**
  * Failure to detect and mitigate these attacks can lead to regulatory fines, legal liabilities, and reputational damage.

## Examples

Real-world examples of Hijack Execution Flow technique usage include:

* **APT29 (Cozy Bear)**
  * Utilized DLL injection techniques to embed malicious payloads into legitimate processes, maintaining persistence and evading detection.
  * Tools used: Cobalt Strike Beacon, custom DLL loaders.
  * Impact: Persistent espionage, credential theft, and sensitive data exfiltration.
* **FIN7 Group**
  * Employed DLL search order hijacking by placing malicious DLLs in directories of legitimate applications, loading malicious code into trusted processes.
  * Tools used: Carbanak malware, custom DLL injection scripts.
  * Impact: Financial data theft, unauthorized transactions, and significant financial losses for targeted organizations.
* **PlugX Malware**
  * Frequently uses DLL sideloading (a variant of DLL search order hijacking) to execute malicious payloads through trusted software.
  * Attack scenario: Attackers bundle a legitimate executable with a malicious DLL, tricking the legitimate process into loading the malicious DLL.
  * Impact: Persistent remote access, espionage, and lateral movement within victim networks.
* **Operation ShadowHammer (ASUS Supply Chain Attack)**
  * Attackers compromised ASUS Live Update utility, injecting malicious code into legitimate executables distributed to users.
  * Technique: Executable file manipulation and DLL hijacking.
  * Impact: Widespread compromise, credential theft, and espionage targeting specific users.
* **NotPetya Ransomware**
  * Leveraged DLL hijacking mechanisms to propagate rapidly across networks, infecting critical systems and causing extensive operational disruption.
  * Tools used: Modified EternalBlue exploit, DLL hijacking methods.
  * Impact: Massive global disruption, data destruction, and billions of dollars in economic damage.
