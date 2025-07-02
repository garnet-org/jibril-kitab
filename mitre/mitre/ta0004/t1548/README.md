---
description: Abuse Elevation Control Mechanism [T1548]
icon: lock
---

# Abuse Elevation Control Mechanism

## Information

* Name: Abuse Elevation Control Mechanism
* ID: T1548
* Tactics: [TA0004](../), [TA0005](../../ta0005/)
* Sub-Technique: [T1548.002](t1548.002.md), [T1548.003](t1548.003.md), [T1548.001](t1548.001.md), [T1548.005](t1548.005.md), [T1548.004](t1548.004.md), [T1548.006](t1548.006.md)

## Introduction

Abuse Elevation Control Mechanism (Technique ID: T1548) in the MITRE ATT\&CK framework involves adversaries exploiting system mechanisms designed to elevate privileges to gain higher-level permissions. These mechanisms, intended for legitimate administrative use, can be misused by attackers to escalate privileges, execute malicious code, and maintain persistence. Leveraging these controls allows adversaries to bypass access restrictions, potentially leading to full system compromise.

## Deep Dive Into Technique

Adversaries utilize various elevation control mechanisms to escalate privileges and execute malicious activities. Some of the most common methods and mechanisms include:

* **Setuid and Setgid Binaries (T1548.001):**
  * Attackers exploit binaries with setuid or setgid bits set, allowing execution with elevated privileges.
  * Abuse occurs when adversaries manipulate or replace these binaries to run unauthorized commands or scripts with root-level permissions.
* **Bypass User Account Control (UAC) (T1548.002):**
  * Attackers exploit Windows UAC bypass techniques to gain administrative privileges without triggering standard alerts.
  * Techniques include DLL hijacking, registry manipulation, and abusing trusted Windows executables.
* **Sudo and Sudo Caching (T1548.003):**
  * Attackers abuse sudo privileges or cached credentials on Linux/Unix systems.
  * Exploitation involves manipulating sudoers files, exploiting misconfigured permissions, or leveraging cached sudo authentication tokens.
* **Elevated Execution with Prompt (T1548.004):**
  * Attackers leverage mechanisms prompting users for credentials, tricking users into elevating malicious processes.
  * Techniques include social engineering or GUI spoofing to deceive users into granting elevated privileges.
* **Abuse of Elevation Control via Accessibility Features (T1548.005):**
  * Adversaries exploit accessibility tools (e.g., sticky keys, screen magnifier) that run with elevated privileges.
  * Attackers replace legitimate accessibility executables with malicious payloads to obtain elevated privileges.

Real-world procedures typically involve:

* Identifying vulnerable binaries or configurations through enumeration tools (e.g., LinEnum, WinPEAS).
* Modifying or replacing legitimate executables or scripts with malicious counterparts.
* Executing privilege escalation exploits leveraging system misconfigurations.
* Maintaining persistence by regularly re-abusing elevation mechanisms.

## When this Technique is Usually Used

Adversaries commonly employ Abuse Elevation Control Mechanism during multiple stages of an attack lifecycle, including:

* **Privilege Escalation Stage:**
  * Attackers escalate privileges from standard user accounts to administrative/root accounts to gain deeper system access.
  * Exploiting misconfigured permissions, binaries, or policies to elevate privileges.
* **Persistence Stage:**
  * Attackers leverage elevation mechanisms to establish long-term persistence and evade detection.
  * Modifying or creating binaries with elevated permissions to remain persistent even after system reboots.
* **Execution Stage:**
  * Attackers execute malicious payloads with elevated privileges, enabling advanced reconnaissance, lateral movement, and data exfiltration activities.
* **Defense Evasion Stage:**
  * Attackers abuse legitimate elevation mechanisms to bypass security controls, evade antivirus detection, and disable monitoring tools.

## How this Technique is Usually Detected

Detection methods and tools to identify Abuse Elevation Control Mechanism include:

* **Audit and Monitoring Tools:**
  * Sysmon (Windows) for process creation monitoring, registry modification detection.
  * Auditd (Linux) for tracking execution of privileged binaries, sudo usage, and changes to permission bits.
* **Endpoint Detection and Response (EDR) Solutions:**
  * Real-time monitoring and alerting for unusual privilege escalations or suspicious binary modifications.
  * Detection of abnormal process execution chains (e.g., non-standard binaries spawning elevated processes).
* **File Integrity Monitoring (FIM) Tools:**
  * Monitoring changes to critical system files, binaries, and sudoers files for unauthorized modifications.
* **Behavioral Analytics and SIEM Correlation Rules:**
  * Correlation rules detecting suspicious processes or binaries executed with elevated privileges.
  * Alerting on abnormal usage of accessibility features or commands associated with UAC bypass.

Specific Indicators of Compromise (IoCs) to monitor include:

* Unexpected changes to sudoers files or setuid/setgid binaries.
* Unusual UAC bypass registry modifications or DLL hijacking attempts.
* Suspicious accessibility executable replacements (e.g., sethc.exe, utilman.exe).
* Abnormal processes spawned from accessibility features or elevated binaries.
* Suspicious command-line executions involving privilege escalation tools (e.g., PowerSploit, LinPEAS, WinPEAS).

## Why it is Important to Detect This Technique

Detecting Abuse Elevation Control Mechanism is crucial due to its significant impacts on systems and networks, including:

* **Unauthorized Privilege Escalation:**
  * Attackers gaining administrator/root privileges can fully compromise systems, disable security controls, and access sensitive data.
* **Persistence and Long-term Compromise:**
  * Elevated privileges enable attackers to establish persistent footholds, making remediation challenging and increasing compromise duration.
* **Defense Evasion and Detection Difficulty:**
  * Abuse of legitimate elevation mechanisms allows attackers to bypass traditional security measures, complicating detection and response efforts.
* **Data Loss and Exfiltration Risks:**
  * Elevated privileges grant attackers unrestricted access to sensitive information, facilitating data theft, espionage, or sabotage.
* **Operational Disruption and System Damage:**
  * Attackers with elevated access can disrupt operations, delete or modify critical files, and cause system instability or outages.

Early detection is essential to:

* Limit adversary capabilities and prevent further escalation or lateral movement.
* Minimize potential damage, data loss, or operational disruption.
* Facilitate quicker incident response, containment, and remediation actions.

## Examples

Real-world examples demonstrating Abuse Elevation Control Mechanism include:

* **UAC Bypass via DLL Hijacking:**
  * Attack Scenario: An attacker exploits a DLL hijacking vulnerability in a trusted Windows executable (e.g., fodhelper.exe) to bypass UAC prompts.
  * Tools Used: Metasploit Framework, PowerSploit, Empire.
  * Impact: Attacker gains administrative privileges, enabling installation of malware, persistence establishment, and lateral movement.
* **Setuid Binary Exploitation (Linux):**
  * Attack Scenario: An attacker identifies a misconfigured setuid binary (e.g., /usr/bin/find) allowing command execution with root privileges.
  * Tools Used: LinPEAS, GTFOBins, custom scripts.
  * Impact: Attacker achieves root-level access, enabling full system compromise, data exfiltration, and persistence.
* **Accessibility Feature Abuse (Sticky Keys Exploit):**
  * Attack Scenario: An attacker replaces the Windows accessibility executable (sethc.exe) with cmd.exe to gain SYSTEM-level privileges at login screen.
  * Tools Used: Windows built-in commands, PowerShell scripts, custom payloads.
  * Impact: Attacker gains persistent, elevated access to the compromised system, facilitating further exploitation and lateral movement.
* **Sudo Privilege Escalation via Misconfigured Sudoers File:**
  * Attack Scenario: An attacker exploits overly permissive sudoers configurations (e.g., NOPASSWD permissions) to execute arbitrary commands as root.
  * Tools Used: Enumeration scripts (LinEnum, LinPEAS), custom shell scripts.
  * Impact: Attacker gains root privileges, enabling complete control over the compromised Linux system, data theft, and further network infiltration.
