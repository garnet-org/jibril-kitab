---
description: Software Discovery [T1518]
icon: lock
---

# Software Discovery

## Information

* Name: Software Discovery
* ID: T1518
* Tactics: [TA0007](../)
* Sub-Technique: [T1518.001](t1518.001.md)

## Introduction

Software Discovery (T1518) is a technique within the MITRE ATT\&CK framework categorized under the Discovery tactic. Attackers utilize this technique to enumerate installed software and applications on a compromised system, enabling them to identify potential vulnerabilities, security tools, and defensive mechanisms. Understanding the software landscape of a targeted environment allows adversaries to tailor their strategies, avoid detection, and exploit vulnerabilities effectively.

## Deep Dive Into Technique

Software Discovery involves systematically querying or analyzing the compromised system to determine installed software and applications. Attackers can achieve this through various methods and mechanisms:

* **Native Operating System Commands:**
  * Windows:
    * `wmic product get name,version`: Enumerates installed software and versions.
    * `Get-WmiObject -Class Win32_Product`: PowerShell command to retrieve installed software.
    * Registry keys inspection, such as `HKLM\Software\Microsoft\Windows\CurrentVersion\Uninstall`.
  * Linux:
    * `dpkg -l`: Lists installed Debian-based packages.
    * `rpm -qa`: Lists installed RPM-based packages.
    * `snap list`: Lists installed Snap packages.
  * macOS:
    * `system_profiler SPApplicationsDataType`: Lists installed applications and their versions.
    * Inspecting `/Applications` directory contents.
* **Third-party Tools and Utilities:**
  * Attackers may leverage legitimate system administration tools or utilities, such as:
    * Sysinternals suite (e.g., PsInfo).
    * NirSoft tools.
    * Custom scripts or binaries designed to automate enumeration.
* **Scripting and Automation:**
  * Attackers frequently automate discovery processes using scripts:
    * PowerShell scripts.
    * Bash or Python scripts.
    * Batch files (.bat) or VBScript (.vbs).
* **Accessing Configuration Files and Logs:**
  * Attackers may analyze configuration files, logs, or installation artifacts to discover software details:
    * Windows Event Logs.
    * Application-specific log files.
    * Configuration files stored in standard directories.

## When this Technique is Usually Used

Software Discovery is typically employed during multiple stages of an attack lifecycle, including:

* **Initial Reconnaissance and Discovery Phase:**
  * Immediately after gaining initial access, attackers enumerate installed software to identify vulnerabilities and exploit paths.
* **Privilege Escalation and Lateral Movement:**
  * Identifying outdated or vulnerable software enables attackers to escalate privileges or move laterally within the network.
* **Defense Evasion:**
  * Discovering installed security products (antivirus, EDR, firewalls) allows attackers to adjust their tactics, techniques, and procedures (TTPs) to evade detection.
* **Persistence and Impact:**
  * Attackers may identify software that can be leveraged for persistence, data exfiltration, or destructive impact.

## How this Technique is Usually Detected

Detection of Software Discovery techniques involves monitoring and analyzing system activities, logs, and behaviors:

* **Process and Command-Line Monitoring:**
  * Monitor execution of suspicious enumeration commands:
    * Windows: `wmic`, PowerShell commands like `Get-WmiObject`.
    * Linux: `dpkg`, `rpm`, `snap`.
    * macOS: `system_profiler` or unusual directory listings.
  * Establish alerts for command-line arguments associated with software enumeration.
* **Behavioral Analytics and Endpoint Detection and Response (EDR):**
  * EDR solutions can detect anomalous enumeration behaviors and alert security teams.
  * Behavioral analysis tools can identify unusual queries or enumeration patterns.
* **Logging and Monitoring:**
  * Enable comprehensive logging of command execution, PowerShell activities, and registry access.
  * Monitor log files for repeated or unusual enumeration activities.
* **Network-Based Detection:**
  * Network monitoring tools and IDS/IPS systems can detect unusual traffic patterns indicative of enumeration activities.
  * Detect outbound connections to known enumeration or reconnaissance servers.
* **Indicators of Compromise (IoCs):**
  * Suspicious or unauthorized execution of enumeration utilities.
  * Presence of unknown scripts or binaries performing software enumeration.
  * Unusual registry queries or access to software installation keys.

## Why it is Important to Detect This Technique

Detecting Software Discovery early is crucial for maintaining system and network security due to several potential impacts:

* **Prevention of Exploitation:**
  * Early detection prevents attackers from identifying and exploiting vulnerabilities in installed software.
* **Defense Evasion Mitigation:**
  * Identifying discovery activities can prevent attackers from bypassing security controls and defensive mechanisms.
* **Limiting Lateral Movement:**
  * Early detection reduces attackers' ability to move laterally by exploiting vulnerable software.
* **Reducing Damage and Impact:**
  * Timely detection allows security teams to respond swiftly, minimizing potential damage, data loss, and operational disruptions.
* **Improving Incident Response:**
  * Detection provides valuable intelligence during incident response, enabling defenders to better understand attacker objectives and methodologies.

## Examples

Real-world examples of Software Discovery techniques include:

* **APT29 (Cozy Bear):**
  * Known to use PowerShell commands such as `Get-WmiObject` to enumerate installed software and security tools on compromised Windows systems.
  * Impact: Enabled tailored attacks and evasion of detection mechanisms.
* **FIN7 Group:**
  * Utilized custom scripts and native Windows commands (`wmic`, registry queries) to enumerate installed software, security products, and antivirus solutions.
  * Impact: Allowed FIN7 to evade detection and effectively deploy malware and ransomware.
* **Carbanak Group:**
  * Employed enumeration commands to discover installed security software and banking applications.
  * Impact: Facilitated targeted attacks against financial institutions, resulting in significant financial losses.
* **TrickBot Malware:**
  * Leveraged PowerShell scripts to enumerate installed software, security products, and financial applications on infected hosts.
  * Impact: Enabled attackers to conduct targeted credential theft, fraud, and further exploitation.
* **Lazarus Group:**
  * Performed software enumeration using system commands and scripts, identifying vulnerable applications and security products.
  * Impact: Conducted targeted attacks, including ransomware deployment and espionage activities.

These examples highlight how threat actors consistently use Software Discovery to inform subsequent attack stages, evade detection, and maximize their operational impact.
