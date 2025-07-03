---
description: Persistence [TA0003]
icon: lock
---

# Persistence

## Information

* ID: TA0003

## Introduction

Persistence is a critical tactic defined in the MITRE ATT\&CK framework, representing techniques adversaries use to maintain their foothold on compromised systems and networks. After gaining initial access, attackers strive to ensure continued presence, surviving events such as system restarts, credential changes, or defensive measures. Persistence techniques allow attackers to maintain long-term access, enabling them to execute further stages of attacks, perform lateral movement, escalate privileges, or exfiltrate data over extended periods.

## Deep Dive Into Technique

Persistence techniques encompass a variety of methods attackers utilize to ensure continued access:

* **Scheduled Tasks and Cron Jobs:**
  * Attackers configure scheduled tasks (Windows Task Scheduler) or cron jobs (Unix/Linux) to trigger malicious scripts or binaries at specified intervals or events, ensuring repeated execution even after system reboots.
* **Registry Run Keys and Startup Folder:**
  * Malware or scripts can be placed in Windows registry keys such as `HKLM\Software\Microsoft\Windows\CurrentVersion\Run` or within the Windows Startup folder to execute automatically upon system boot or user login.
* **Services and Daemons:**
  * Malicious services (Windows) or daemons (Linux/Unix) can be installed and configured to run automatically, providing attackers with persistent remote access or command-and-control (C2) channels.
* **DLL Search Order Hijacking:**
  * Attackers exploit the DLL loading order in Windows applications by placing malicious DLLs in directories searched before legitimate DLLs, causing malicious code execution upon application startup.
* **Web Shells and Backdoors:**
  * Attackers deploy web shells or backdoors within compromised web servers or applications, enabling persistent remote access through HTTP requests.
* **Bootkits and Rootkits:**
  * Advanced malware implants that embed themselves into system boot processes or kernel-level operations, making detection and removal challenging.
* **Account Manipulation:**
  * Creation or modification of user accounts, including administrator-level accounts, to maintain persistent access through legitimate credentials.
* **Firmware and BIOS Modifications:**
  * Attackers modify firmware or BIOS to persist at the hardware level, surviving system reinstalls or disk replacements.

## When this Technique is Usually Used

Persistence techniques typically appear in various stages and scenarios of cyberattacks, including:

* **Post-Initial Access:**
  * Immediately after initial compromise, attackers implement persistence to ensure stable access before proceeding further into the network.
* **Privilege Escalation and Lateral Movement:**
  * Attackers establish persistence after escalating privileges or moving laterally to new systems, ensuring continued access to critical assets.
* **Long-Term Espionage and Reconnaissance Operations:**
  * Nation-state actors or advanced persistent threats (APTs) use persistence extensively to conduct long-term espionage, surveillance, or data exfiltration operations.
* **Ransomware Attacks:**
  * Attackers deploying ransomware often leverage persistence mechanisms to maintain access, allowing them to monitor victim responses, extract sensitive data, or re-infect systems after initial remediation attempts.
* **Supply Chain Attacks:**
  * Attackers embed persistent backdoors or implants within software updates or third-party services, ensuring prolonged access to multiple downstream victims.

## How this Technique is Usually Detected

Detection of persistence techniques involves multiple methods, tools, and indicators:

* **Endpoint Detection and Response (EDR) Tools:**
  * Monitor and analyze endpoint activities, registry modifications, scheduled tasks, and service creations in real-time.
* **Security Information and Event Management (SIEM) Systems:**
  * Aggregate and correlate logs from multiple sources to identify abnormal behaviors, such as unusual scheduled task execution, registry changes, or abnormal account activities.
* **File Integrity Monitoring (FIM):**
  * Detect unauthorized changes to critical system files, startup folders, cron jobs, or configuration files that indicate persistence attempts.
* **Behavioral Analysis and Threat Hunting:**
  * Proactive searches for anomalous behaviors, such as unexpected DLL loading, unusual process execution, or suspicious network connections indicative of persistent implants.
* **Indicators of Compromise (IoCs):**
  * Specific IoCs include:
    * Unrecognized scheduled tasks or cron jobs.
    * Unusual registry entries in Run keys or startup folders.
    * Unknown services or daemons running persistently.
    * Web shells or backdoors identified on web servers.
    * Suspicious DLL files located in unexpected directories.
    * Unauthorized user account creations or modifications.
    * Network traffic associated with known C2 infrastructure.
* **Memory Analysis and Forensics:**
  * Tools such as Volatility Framework or Rekall can identify hidden processes, injected code, or rootkits residing in memory.

## Why it is Important to Detect This Technique

Early detection of persistence techniques is critical due to their severe impacts and implications for security:

* **Extended Compromise Duration:**
  * Persistence allows attackers prolonged access, increasing the risk of data exfiltration, espionage, sabotage, or further lateral movement.
* **Increased Difficulty in Remediation:**
  * Persistent threats often embed themselves deeply within systems, making remediation challenging and resource-intensive.
* **Risk of Re-infection:**
  * Without detecting and removing persistent mechanisms, organizations risk repeated infections and recurring security incidents.
* **Potential for Privilege Escalation:**
  * Persistent access facilitates attackers in escalating privileges, increasing their ability to cause widespread damage or compromise sensitive information.
* **Data Breaches and Regulatory Consequences:**
  * Persistent threats significantly increase the likelihood of data breaches, potentially resulting in regulatory fines, reputational damage, and loss of customer trust.
* **Operational Disruption:**
  * Persistent threats may lead to prolonged operational disruptions, impacting productivity, revenue, and organizational stability.

## Examples

Real-world examples of persistence techniques, including attack scenarios, tools used, and impacts:

* **SolarWinds Supply Chain Attack (SUNBURST):**
  * Attackers leveraged a malicious DLL embedded into SolarWinds Orion software updates, enabling persistent, stealthy access to thousands of organizations globally.
  * Tools used: Customized DLL implant (SUNBURST), Cobalt Strike, Teardrop.
  * Impacts: Massive data breaches, espionage activities, widespread compromise of government and private sector organizations.
* **APT29 (Cozy Bear) Attacks:**
  * Russian state-sponsored threat actors used scheduled tasks, registry modifications, and web shells to maintain persistent access in targeted networks for espionage.
  * Tools used: PowerShell scripts, custom web shells, scheduled task persistence.
  * Impacts: Prolonged espionage operations, theft of sensitive government and diplomatic information.
* **FIN7 Cybercrime Operations:**
  * Cybercriminal group FIN7 established persistence using malicious Windows services, scheduled tasks, and registry entries to maintain access and conduct financial fraud operations.
  * Tools used: Carbanak malware, PowerShell scripts, malicious services.
  * Impacts: Significant financial losses, credit card data theft, operational disruptions in retail and hospitality sectors.
* **TrickBot Malware Campaigns:**
  * TrickBot malware utilized scheduled tasks, registry run keys, and modular implants to persistently infect endpoints, enabling further ransomware delivery (e.g., Ryuk, Conti).
  * Tools used: TrickBot malware, Emotet loader, scheduled tasks, registry persistence.
  * Impacts: Large-scale ransomware infections, financial losses, operational disruptions across multiple sectors.
* **LoJax UEFI Rootkit:**
  * Advanced persistent threat actors deployed LoJax, a UEFI rootkit, to embed persistence at firmware level, surviving OS reinstalls and hardware changes.
  * Tools used: LoJax rootkit, UEFI firmware modification tools.
  * Impacts: Persistent espionage capabilities, extreme difficulty in remediation, long-term compromise of targeted networks.
