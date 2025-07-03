---
description: Process Injection [T1055]
icon: syringe
---

# Process Injection

## Information

* Name: Process Injection
* ID: T1055
* Tactics: [TA0005](../../ta0005/), [TA0004](../)
* Sub-Technique: [T1055.011](t1055.011.md), [T1055.003](t1055.003.md), [T1055.013](t1055.013.md), [T1055.004](t1055.004.md), [T1055.002](t1055.002.md), [T1055.014](t1055.014.md), [T1055.012](t1055.012.md), [T1055.009](t1055.009.md), [T1055.005](t1055.005.md), [T1055.008](t1055.008.md), [T1055.015](t1055.015.md), [T1055.001](t1055.001.md)

## Introduction

Process Injection (T1055) is a widely recognized adversary tactic categorized under the MITRE ATT\&CK framework's "Defense Evasion" and "Privilege Escalation" tactics. It involves injecting malicious code or payloads into legitimate processes, allowing attackers to execute arbitrary code within another process's memory space. By doing so, adversaries can evade detection, bypass security controls, escalate privileges, and maintain persistence within compromised systems. This technique leverages trusted processes, making detection challenging without specialized monitoring and analysis.

## Deep Dive Into Technique

Process Injection encompasses various technical methods and mechanisms through which attackers insert malicious code into legitimate processes. Attackers typically follow these steps:

1. **Target Process Selection**:
   * Attackers typically select high-privilege or trusted system processes (e.g., explorer.exe, svchost.exe, lsass.exe) to evade suspicion.
2. **Code Injection Methods**:
   * **DLL Injection**:
     * Malicious Dynamic Link Libraries (DLLs) are loaded into legitimate processes using methods like CreateRemoteThread API calls.
     * Tools: Metasploit, Cobalt Strike, custom scripts.
   * **Process Hollowing (RunPE)**:
     * Starts a legitimate process in a suspended state, replaces the original code with malicious payload, then resumes execution.
     * Often used by malware like Dridex, Ursnif, TrickBot.
   * **Thread Execution Hijacking**:
     * Hijacks existing threads within a process to execute malicious code.
     * Techniques include SetThreadContext and SuspendThread/ResumeThread APIs.
   * **Reflective DLL Injection**:
     * Loads DLLs directly from memory without writing them to disk, bypassing traditional antivirus detection.
     * Commonly leveraged by penetration testing frameworks like Metasploit and Cobalt Strike.
   * **AtomBombing**:
     * Exploits Windows Atom Tables to inject code into legitimate processes without using traditional injection APIs.
     * Demonstrated by malware samples like Dridex.
   * **Process Doppelgänging and Herpaderping**:
     * Advanced techniques leveraging NTFS transactions or file system manipulation to inject code stealthily and evade detection.
     * Used by sophisticated threat actors and APT groups.
3. **Common APIs and System Calls**:
   * Windows APIs commonly used include:
     * VirtualAllocEx
     * WriteProcessMemory
     * CreateRemoteThread
     * NtQueueApcThread
     * SetThreadContext
     * ResumeThread
     * NtMapViewOfSection

Attackers often combine these methods with obfuscation and encryption to further evade detection mechanisms.

## When this Technique is Usually Used

Process Injection is commonly utilized across various attack scenarios and stages, including:

* **Initial Access and Execution**:
  * Immediately after initial compromise, attackers inject payloads into legitimate processes to establish stealthy persistence and evade initial detection.
* **Privilege Escalation**:
  * Injecting code into higher-privileged processes to escalate privileges and gain administrative or SYSTEM-level access.
* **Defense Evasion**:
  * Embedding malicious code into trusted processes bypasses antivirus, endpoint detection and response (EDR), and application whitelisting solutions.
* **Persistence and Lateral Movement**:
  * Injected code allows attackers to maintain persistent access to compromised systems and move laterally within a network.
* **Credential Access**:
  * Injecting into sensitive processes like lsass.exe enables credential harvesting and memory scraping.
* **Data Exfiltration and Command and Control (C2)**:
  * Injected payloads facilitate covert network communication, data exfiltration, and remote command execution.

## How this Technique is Usually Detected

Detection of process injection requires multiple strategies and specialized tools, including:

* **Behavioral Monitoring and Endpoint Detection and Response (EDR)**:
  * Monitoring suspicious API calls (e.g., VirtualAllocEx, WriteProcessMemory, CreateRemoteThread).
  * Detecting unusual process behaviors, such as unexpected DLL loads or abnormal memory allocations.
* **Memory Forensics and Analysis**:
  * Analyzing process memory dumps to identify injected code or anomalous memory regions.
  * Tools: Volatility, Rekall, Redline.
* **API Hooking and Monitoring**:
  * Monitoring and logging API calls indicative of injection attempts.
  * Tools: Sysmon, Process Monitor, Endpoint Security Tools.
* **Event Log Monitoring**:
  * Reviewing Windows Security Event Logs for suspicious process creations, privilege escalations, or unexpected process behaviors.
* **Indicators of Compromise (IoCs)**:
  * Suspicious DLLs or executables loaded into legitimate processes.
  * Unusual parent-child process relationships (e.g., PowerShell spawning explorer.exe).
  * Anomalous network connections initiated by legitimate processes.
  * Suspicious registry modifications or persistence mechanisms.
* **Anomaly Detection and Threat Hunting**:
  * Proactive threat hunting for suspicious behaviors, unusual process memory patterns, or unexpected API usage.

## Why it is Important to Detect This Technique

Early detection of Process Injection is critical due to its potential severe impacts on systems and networks, including:

* **Persistence and Long-term Compromise**:
  * Allows attackers to maintain covert access, making remediation challenging.
* **Privilege Escalation and Credential Theft**:
  * Facilitates unauthorized administrative access, credential harvesting, and lateral movement within networks.
* **Evasion of Traditional Security Controls**:
  * Bypasses antivirus, application whitelisting, and other endpoint protections, increasing risk exposure.
* **Data Exfiltration and Intellectual Property Theft**:
  * Enables attackers to exfiltrate sensitive data undetected, leading to significant financial, regulatory, and reputational impacts.
* **Operational Disruption and Damage**:
  * Injected code can disrupt legitimate processes, degrade system performance, or cause application crashes.
* **Facilitation of Further Attacks**:
  * Injected payloads often serve as beachheads for further exploitation, ransomware deployment, or destructive attacks.

Early detection and response significantly reduce attackers' dwell time, limit damage, and improve incident response effectiveness.

## Examples

Real-world examples demonstrating Process Injection:

* **Dridex Malware**:
  * Utilizes AtomBombing and process hollowing to inject payloads into legitimate Windows processes.
  * Impact: Credential theft, financial fraud, persistent access.
* **TrickBot Trojan**:
  * Employs reflective DLL injection and process hollowing to evade detection and maintain persistence.
  * Impact: Banking credential theft, ransomware deployment (Ryuk, Conti).
* **Cobalt Strike Framework**:
  * Widely used penetration testing and adversary emulation tool leveraging reflective DLL injection to deliver payloads into memory without disk artifacts.
  * Impact: Persistent access, lateral movement, data exfiltration.
* **APT32 (OceanLotus)**:
  * Leveraged advanced process injection techniques (DLL injection, process hollowing) in targeted espionage campaigns against government and private sector entities.
  * Impact: Intellectual property theft, espionage, long-term stealth persistence.
* **FIN7 Cybercrime Group**:
  * Utilized process injection to deploy Carbanak malware, enabling stealthy financial data theft from banking institutions.
  * Impact: Millions of dollars in financial losses, sensitive data exfiltration.
* **NotPetya Ransomware**:
  * Used process injection to propagate rapidly and encrypt data across enterprise networks.
  * Impact: Massive operational disruptions, billions in damages globally.

These examples illustrate the diverse scenarios, tools, and impacts associated with Process Injection, underscoring the importance of robust detection and mitigation strategies.
