---
description: Indicator Removal [T1070]
icon: info
---

# Indicator Removal

## Information

* Name: Indicator Removal
* ID: T1070
* Tactics: [TA0005](../)
* Sub-Technique: T1070.002, [T1070.007](t1070.007.md), [T1070.003](t1070.003.md), T1070.008, [T1070.006](t1070.006.md), [T1070.001](t1070.001.md), T1070.005, T1070.010, T1070.009, [T1070.004](t1070.004.md)

## Introduction

Indicator Removal is a technique recognized within the MITRE ATT\&CK framework, categorized under Defense Evasion (T1070). Attackers utilize this technique to evade detection by removing or altering indicators of their malicious activities. Such indicators include logs, files, registry keys, or any other artifacts that could reveal unauthorized access or malicious actions. By carefully removing these indicators, adversaries attempt to maintain persistence, avoid detection, and ensure continued access to compromised systems.

## Deep Dive Into Technique

Indicator Removal involves systematically deleting or altering artifacts that signify malicious activity. Attackers employ various methods and mechanisms to achieve this:

* **Clearing Windows Event Logs:**
  * Attackers commonly use built-in Windows utilities such as `wevtutil`, `powershell`, or `eventvwr.msc` to clear or manipulate event logs.
  * Commands like `wevtutil cl Application` or `Clear-EventLog` in PowerShell are frequently utilized.
* **Manipulation of Linux Logs:**
  * On Linux-based systems, attackers typically modify or delete log files located in `/var/log/`.
  * Tools like `shred`, `rm`, or `logrotate` can be employed to obscure or remove log entries.
* **File Deletion and Overwriting:**
  * Attackers often delete malicious files after execution or overwrite them to prevent forensic recovery.
  * Secure deletion tools (`sdelete`, `shred`) may be used to prevent recovery through forensic analysis.
* **Registry Key Manipulation:**
  * Malicious actors may remove or alter registry keys that contain evidence of malware installation or persistence mechanisms.
  * Commands such as `reg delete` or PowerShell cmdlets are commonly leveraged.
* **Timestomping:**
  * Adversaries can modify file timestamps to obscure the true timeline of their activities.
  * Tools such as `timestomp` or PowerShell scripts allow attackers to alter file creation, modification, or access timestamps.
* **Clearing Command History:**
  * Attackers remove shell history (`.bash_history`, PowerShell history) to erase evidence of executed commands.
  * Commands like `history -c`, `rm ~/.bash_history`, or PowerShell history clearing techniques are employed.

## When this Technique is Usually Used

Indicator Removal is typically employed by attackers across multiple stages of the cyber attack lifecycle, including:

* **Initial Compromise:**
  * Immediately after gaining initial access, attackers may remove indicators to avoid early detection before establishing a foothold.
* **Persistence and Privilege Escalation:**
  * Adversaries remove indicators related to privilege escalation methods and persistence mechanisms to maintain long-term access.
* **Defense Evasion:**
  * This technique is primarily categorized under defense evasion; attackers continuously remove or alter indicators throughout the attack lifecycle to evade detection and prevent forensic investigations.
* **Exfiltration and Post-Exfiltration:**
  * After data exfiltration, attackers often erase logs and artifacts related to data transfer activities to hinder attribution and forensic analysis.
* **Covering Tracks (Final Stage):**
  * Before exiting compromised systems, attackers thoroughly remove evidence to complicate incident response and forensic investigations.

## How this Technique is Usually Detected

Detection of Indicator Removal requires proactive monitoring, auditing, and advanced detection mechanisms:

* **Log Monitoring and SIEM Solutions:**
  * Continuous monitoring and correlation of log events through Security Information and Event Management (SIEM) tools like Splunk, ELK Stack, or QRadar.
  * Alerting on abnormal log clearing events (e.g., unexpected event log deletions).
* **Endpoint Detection and Response (EDR) Tools:**
  * EDR solutions such as CrowdStrike Falcon, Carbon Black, or Microsoft Defender for Endpoint detect suspicious file deletions, registry modifications, and log manipulation activities.
* **File Integrity Monitoring (FIM):**
  * Tools like Tripwire or OSSEC monitor file changes, deletions, and timestamp modifications, alerting security teams to suspicious activities.
* **Audit Policies and Logging:**
  * Implementing robust audit policies that detect attempts to clear or alter logs (e.g., Windows Security Auditing for Event Log Cleared events - Event ID 1102).
* **Behavioral Analytics and Machine Learning:**
  * Machine learning-driven security analytics platforms detect anomalies in user or system behavior, such as unusual log deletions or file manipulations.
* **Indicators of Compromise (IoCs):**
  * Specific IoCs include:
    * Unexpected clearing of Windows event logs (Event ID 1102).
    * Missing or modified logs in `/var/log/` directories.
    * Unusual deletion of registry keys related to persistence mechanisms.
    * Detection of timestomping tools or altered timestamps.
    * Presence of command history files (`.bash_history`) being cleared or truncated.

## Why it is Important to Detect This Technique

Early detection of Indicator Removal is critical due to its potential impacts on systems and networks:

* **Impedes Incident Response and Forensics:**
  * Removing indicators complicates forensic investigations and incident response processes, making attribution and remediation difficult.
* **Prolonged Undetected Persistence:**
  * Attackers who successfully remove indicators can maintain undetected persistence, allowing prolonged unauthorized access and further malicious activities.
* **Data Loss and Exfiltration:**
  * Undetected attackers can continue exfiltrating sensitive data without raising alarms, leading to severe data breaches and compliance violations.
* **Operational Disruption:**
  * Persistent undetected threats may disrupt business operations, damage reputation, and incur financial losses.
* **Compliance and Regulatory Implications:**
  * Organizations failing to detect Indicator Removal may face regulatory penalties, especially in sectors with stringent compliance requirements (e.g., healthcare, finance, government).
* **Reduced Visibility and Security Posture:**
  * Continuous indicator removal reduces overall visibility into network and system activities, weakening the organization's security posture and resilience.

## Examples

Real-world examples illustrating Indicator Removal in cyber attacks include:

* **APT29 (Cozy Bear) Attacks:**
  * Utilized PowerShell scripts to clear Windows event logs and remove artifacts post-compromise.
  * Impacted governmental and diplomatic organizations, complicating forensic investigations.
* **FIN7 Cybercrime Group:**
  * Regularly deleted log files and manipulated timestamps to evade detection during payment card data breaches.
  * Used tools like `sdelete` to securely erase malicious files after exfiltration.
* **NotPetya Malware Incident (2017):**
  * Modified Master Boot Record (MBR) and logs to prevent recovery and forensic analysis.
  * Caused global operational disruptions and significant financial losses.
* **Operation Cleaver (Iranian Cyber Espionage):**
  * Attackers systematically cleared logs and removed files after data exfiltration from critical infrastructure sectors.
  * Significantly hindered attribution and delayed remediation efforts.
* **Carbanak/FIN7 Banking Attacks:**
  * Frequently removed or altered logs and security events on compromised banking systems.
  * Enabled prolonged unauthorized access, resulting in substantial financial theft.
* **DarkHotel Threat Actor:**
  * Cleared browser history and logs after credential harvesting attacks on hotel Wi-Fi networks targeting high-profile individuals.
  * Successfully evaded detection and attribution for extended periods.
