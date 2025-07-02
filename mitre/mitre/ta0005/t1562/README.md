---
description: Impair Defenses [T1562]
icon: shield
---

# Impair Defenses

## Information

* Name: Impair Defenses
* ID: T1562
* Tactics: [TA0005](../)
* Sub-Technique: T1562.009, [T1562.002](t1562.002.md), [T1562.004](t1562.004.md), T1562.012, T1562.006, T1562.007, T1562.010, T1562.003, [T1562.001](t1562.001.md), T1562.011, [T1562.008](t1562.008.md)

## Introduction

Impair Defenses (MITRE ATT\&CK ID: T1562) is a technique categorized under the MITRE ATT\&CK framework's "Defense Evasion" tactic. Attackers employ this technique to disable or circumvent security tools, processes, or mechanisms within targeted environments. The primary goal is to prevent detection or response to malicious activities, allowing attackers to maintain persistence, escalate privileges, or further infiltrate network resources without interference.

## Deep Dive Into Technique

The Impair Defenses technique encompasses various methods attackers use to disable or weaken security mechanisms, including antivirus software, firewalls, intrusion detection/prevention systems, logging capabilities, and security monitoring tools. The following are common execution methods and mechanisms:

* **Disable or Modify Antivirus/Antimalware Software:**
  * Attackers may terminate antivirus processes or services, alter configurations, or remove critical files.
  * Techniques include:
    * Using taskkill commands to terminate antivirus processes.
    * Modifying registry keys to disable antivirus protection.
    * Uninstalling antivirus software through scripts or administrative tools.
* **Disable or Alter Firewall and Network Security Devices:**
  * Attackers disable or modify firewall rules to allow unauthorized traffic.
  * Methods include:
    * Using netsh commands or PowerShell scripts to disable Windows firewall.
    * Modifying firewall configuration files or registry entries to weaken security posture.
* **Disabling Security Tools and Services:**
  * Stopping or disabling services related to security monitoring and logging.
  * Examples include:
    * Stopping Windows Defender Advanced Threat Protection (ATP) or Endpoint Detection and Response (EDR) agents.
    * Disabling security event logging via registry modifications or group policy alterations.
* **Tampering with Logging and Monitoring Capabilities:**
  * Attackers may clear logs, disable logging services, or modify log configurations to evade detection.
  * Common mechanisms include:
    * Clearing Windows Event Logs (e.g., using wevtutil or PowerShell).
    * Disabling Sysmon or other monitoring agents to reduce visibility.
* **Kernel-Level Manipulation:**
  * Advanced adversaries may employ rootkits or kernel-level drivers to impair defenses at a low level.
  * Techniques include:
    * Loading malicious kernel drivers to intercept or block security software functionality.
    * Using rootkits to hide processes, files, or network connections from security tools.

## When this Technique is Usually Used

The Impair Defenses technique can be employed across various stages of the cyber kill chain and is particularly prevalent in the following scenarios:

* **Initial Access and Execution Stage:**
  * Immediately after gaining initial foothold, attackers disable antivirus or other endpoint protection to execute malware payloads without detection.
* **Persistence and Privilege Escalation Stage:**
  * Attackers disable or weaken security tools to establish persistent backdoors or escalate privileges without triggering alerts.
* **Defense Evasion and Lateral Movement Stage:**
  * Attackers disable logging and monitoring solutions to move laterally undetected within the network.
* **Exfiltration Stage:**
  * Attackers disable network monitoring and firewall rules to facilitate undetected data exfiltration.
* **Cleanup and Cover-Up Stage:**
  * Attackers clear or disable logs and monitoring tools to erase evidence of malicious activity, complicating forensic investigations.

## How this Technique is Usually Detected

Detection of Impair Defenses techniques relies heavily on monitoring system configurations, processes, logs, and security tool statuses. Effective detection methods and indicators of compromise (IoCs) include:

* **Endpoint Detection and Response (EDR) Tools:**
  * Monitor for sudden termination of antivirus or security processes.
  * Detect modifications in registry keys and configuration files related to security tools.
* **Security Information and Event Management (SIEM) Systems:**
  * Correlate events indicating disabled or altered firewall rules, antivirus services, or logging mechanisms.
  * Detect abnormal event log clearing or disabling actions (e.g., usage of wevtutil commands).
* **File Integrity Monitoring (FIM):**
  * Alert on unauthorized changes to critical security-related files, configurations, or registry entries.
* **Behavioral Analysis and Anomaly Detection:**
  * Monitor for unusual administrative commands or scripts (e.g., netsh, taskkill, PowerShell scripts) executed by unexpected or unauthorized users.
  * Detect anomalies in kernel-level activities, such as loading unsigned or malicious kernel drivers.
* **Specific Indicators of Compromise (IoCs):**
  * Unexpected disabling of Windows Defender, antivirus solutions, or EDR agents.
  * Unusual registry modifications (e.g., disabling security notifications, logging, or antivirus protection).
  * Commands or scripts used to clear event logs (e.g., "wevtutil cl", "Clear-EventLog").
  * Detection of rootkit artifacts or malicious kernel drivers loaded into memory.

## Why it is Important to Detect This Technique

Detecting Impair Defenses techniques is crucial due to their significant impact on organizational security posture. Early detection prevents attackers from gaining prolonged undetected access, escalating privileges, or exfiltrating sensitive data. The importance of timely detection includes:

* **Preventing Further Compromise:**
  * Early detection stops attackers from disabling critical security mechanisms, reducing the risk of deeper infiltration and lateral movement.
* **Maintaining Visibility:**
  * Ensuring security monitoring and logging remain functional helps security teams detect and respond effectively to threats.
* **Reducing Damage and Loss:**
  * Quick identification and response minimize potential damage, data loss, or financial impact resulting from prolonged attacker presence.
* **Facilitating Incident Response and Forensics:**
  * Preserving logs and security tool functionality ensures investigators have sufficient data to reconstruct events, attribute attacks, and remediate vulnerabilities.
* **Compliance and Regulatory Requirements:**
  * Timely detection and response to security incidents involving impaired defenses are often mandated by regulatory frameworks and industry standards.

## Examples

Real-world examples of Impair Defenses techniques include:

* **TrickBot Malware:**
  * Attack Scenario: TrickBot disables Windows Defender by modifying registry keys and stopping related services.
  * Tools/Methods Used: PowerShell scripts, registry modifications, service termination.
  * Impact: Reduced endpoint protection, enabling further malware deployment (e.g., Ryuk ransomware).
* **APT28 (Fancy Bear) Attacks:**
  * Attack Scenario: APT28 disables Windows event logging to evade detection while performing lateral movement.
  * Tools/Methods Used: wevtutil command line utility, custom scripts.
  * Impact: Reduced visibility into attacker activities, complicating incident response and attribution.
* **FIN7 Cybercrime Group:**
  * Attack Scenario: FIN7 disables antivirus software and endpoint protection agents before deploying malware payloads.
  * Tools/Methods Used: Custom PowerShell scripts, taskkill commands, registry modifications.
  * Impact: Successful deployment of data-stealing malware, leading to significant financial losses.
* **DarkSide Ransomware Attacks:**
  * Attack Scenario: DarkSide ransomware operators disable endpoint security tools and clear logs prior to ransomware execution.
  * Tools/Methods Used: PowerShell scripts, batch scripts, registry edits, and wevtutil.
  * Impact: Successful ransomware deployment, encrypted critical systems, and operational disruption.
* **Turla APT Group:**
  * Attack Scenario: Turla employs rootkits and kernel-level drivers to disable or evade antivirus and security software detection.
  * Tools/Methods Used: Kernel-mode rootkits, malicious kernel drivers.
  * Impact: Long-term persistence, espionage activities, and significant data exfiltration without detection.
