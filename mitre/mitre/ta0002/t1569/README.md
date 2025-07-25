---
description: System Services [T1569]
icon: server
---

# System Services

## Information

* Name: System Services
* ID: T1569
* Tactics: [TA0002](../)
* Sub-Technique: [T1569.001](t1569.001.md), [T1569.002](t1569.002.md)

## Introduction

System Services is a technique categorized under the MITRE ATT\&CK framework (T1569), falling within the Execution and Persistence tactics. Attackers abuse legitimate system services or create malicious services to execute malicious payloads, maintain persistence, escalate privileges, or achieve lateral movement within compromised environments. System services typically run with elevated privileges, making them attractive targets for exploitation and abuse.

## Deep Dive Into Technique

System services are background processes managed by the operating system, typically running with higher privileges than standard user processes. Attackers can exploit or abuse these services in several ways:

* **Creation of Malicious Services:**
  * Attackers leverage built-in Windows tools such as `sc.exe`, `services.msc`, or PowerShell cmdlets (`New-Service`) to create new malicious services.
  * Malicious services can be configured to execute payloads at system boot, system startup, or upon specific events, ensuring persistent access.
* **Modification of Existing Services:**
  * Attackers may hijack legitimate services by modifying the binary path or startup parameters to execute malicious payloads.
  * Common methods include modifying registry entries, such as:
    * `HKLM\SYSTEM\CurrentControlSet\Services\<ServiceName>\ImagePath`
  * Attackers may alter service permissions to maintain persistence and evade detection.
* **Service Execution Methods:**
  * Services can be configured to run binaries, scripts, or DLL files.
  * Attackers frequently utilize:
    * Executable files (.exe)
    * DLL files executed via `svchost.exe`
    * Scripts (PowerShell, batch scripts)
  * Attackers may also exploit services running under privileged accounts (SYSTEM or Administrator) to escalate privileges or perform lateral movement.
* **Service Triggers and Conditions:**
  * Windows supports service triggers that start services based on specific system events or conditions, providing attackers stealthy execution mechanisms.
  * Attackers may leverage these triggers to execute payloads only under certain conditions, reducing detection possibilities.

## When this Technique is Usually Used

Attackers commonly employ the System Services technique at various stages of cyber-attacks, including:

* **Initial Access and Execution:**
  * After initial compromise, attackers may quickly establish persistence by creating malicious services.
  * Execution of payloads through services provides stealth and reliable execution environments.
* **Persistence:**
  * System services provide attackers with a robust persistence mechanism, ensuring that malicious payloads execute automatically at system reboot or logon.
* **Privilege Escalation:**
  * Exploiting or abusing services running with elevated privileges (SYSTEM, Administrator) allows attackers to escalate privileges within compromised environments.
* **Defense Evasion:**
  * Attackers may use existing legitimate services or services with ambiguous names to evade detection.
  * Leveraging built-in Windows components to create or modify services reduces suspicion and bypasses some security controls.
* **Lateral Movement:**
  * Attackers may remotely create or modify services on other systems within compromised networks to spread laterally and establish footholds on multiple hosts.

## How this Technique is Usually Detected

Detection of malicious system services involves monitoring, logging, and analyzing service creation, modification, and execution activities. Common detection methods and tools include:

* **Event Logs and Auditing:**
  * Monitor Windows Event Logs, specifically:
    * Event ID 4697 (Service Creation)
    * Event ID 7045 (New Service Installed)
    * Event ID 7036 (Service state changes)
  * Enable auditing and logging of registry key modifications related to service configurations:
    * `HKLM\SYSTEM\CurrentControlSet\Services\`
* **Endpoint Detection and Response (EDR) Tools:**
  * Utilize EDR solutions to detect suspicious service creations, modifications, or executions.
  * EDR tools may provide behavioral analysis, anomaly detection, and real-time alerts.
* **Behavioral Analysis:**
  * Monitor for unusual service names, paths, or binaries executing from uncommon directories (e.g., temp folders, user directories).
  * Detect services executing PowerShell scripts, batch files, or uncommon binaries.
* **Threat Hunting and Indicators of Compromise (IoCs):**
  * Look for suspicious service names mimicking legitimate services (e.g., slight misspellings or unusual naming conventions).
  * Identify unusual binaries or scripts executed as services.
  * IoCs include:
    * Creation of services with random or suspicious names.
    * Services executing binaries from temporary or user-specific directories.
    * Modification of legitimate services' registry entries (ImagePath, Parameters).
    * Unexpected scheduled service executions or triggers.
* **SIEM and Centralized Logging:**
  * Aggregate and analyze logs from endpoints and servers to detect anomalous service-related activities.
  * Leverage correlation rules and alerts to identify suspicious service creations or modifications.

## Why it is Important to Detect This Technique

Early detection of malicious system services is critical due to the high impact associated with their abuse:

* **Persistent Access:**
  * Malicious services grant attackers persistent footholds within compromised environments, allowing long-term access and repeated exploitation.
* **Privilege Escalation:**
  * Exploiting services running with elevated privileges enables attackers to escalate privileges, potentially leading to full system compromise or domain-wide impacts.
* **Stealth and Evasion:**
  * Attackers leverage system services to evade detection, as services often run with legitimate privileges and are less likely to trigger immediate suspicion.
* **Lateral Movement:**
  * Malicious services can facilitate lateral movement within networks, increasing the scope and severity of breaches.
* **System Stability and Integrity:**
  * Abuse of system services can negatively impact system performance, stability, and reliability, leading to potential downtime or disruption of critical services.
* **Data Exfiltration and Damage:**
  * Attackers can leverage malicious system services to execute payloads capable of data theft, ransomware deployment, or destructive activities.

## Examples

Real-world examples of attackers leveraging the System Services technique include:

* **APT41 (Winnti Group):**
  * Utilized malicious Windows services to maintain persistence and execute payloads during targeted intrusions.
  * Created services with legitimate-sounding names or modified existing services to execute malicious DLLs via `svchost.exe`.
* **Lazarus Group:**
  * Created malicious services to execute payloads persistently, often using service names resembling legitimate Windows components.
  * Modified existing services or registry entries to hijack legitimate processes for stealthy execution.
* **FIN7/Carbanak:**
  * Employed malicious services for persistent execution of malware payloads.
  * Utilized PowerShell scripts and binaries executed via services to evade detection and maintain stealthy operations.
* **DarkSide Ransomware:**
  * Leveraged malicious services to deploy ransomware payloads across compromised networks.
  * Created services remotely to execute ransomware binaries on multiple systems simultaneously.
* **TrickBot Malware:**
  * Used malicious Windows services for persistence and lateral movement within infected networks.
  * Modified service configurations and registry entries to execute malicious payloads at system startup.

In these attack scenarios, the use of malicious system services significantly enhanced attackers' capabilities to maintain persistence, escalate privileges, evade detection, and expand their compromise scope.
