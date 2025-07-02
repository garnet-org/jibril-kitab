---
description: Disk Wipe [T1561]
icon: floppy-disk
---

# Disk Wipe

## Information

* Name: Disk Wipe
* ID: T1561
* Tactics: [TA0040](../)
* Sub-Technique: [T1561.002](t1561.002.md), [T1561.001](t1561.001.md)

## Introduction

Disk Wipe (T1561.001) is a sub-technique under the "Data Destruction" tactic within the MITRE ATT\&CK framework. It involves adversaries deliberately overwriting or erasing data on disk storage devices to render data unrecoverable, disrupt operations, or conceal malicious activities. Attackers may utilize disk wiping techniques as part of sabotage, espionage, or cover-up operations, often causing significant operational downtime and permanent data loss.

## Deep Dive Into Technique

Disk wiping involves systematically overwriting data on storage devices, including hard drives, solid-state drives (SSDs), and removable media, to prevent recovery. This can be accomplished through multiple execution methods and mechanisms:

* **Execution Methods:**
  * Using built-in tools and utilities:
    * Windows: `cipher.exe`, `format.exe`, `diskpart.exe`
    * Linux: `dd`, `shred`, `wipefs`, `mkfs`
  * Leveraging third-party software and specialized malware:
    * Shamoon (Disttrack)
    * WhisperGate
    * HermeticWiper
    * KillDisk malware family
  * Custom scripts and batch files that automate wiping procedures.
* **Mechanisms:**
  * Overwriting data sectors multiple times with random or zeroed data.
  * Deleting partition tables and file system metadata.
  * Corrupting Master Boot Record (MBR) or GUID Partition Table (GPT).
  * Encrypting data with unrecoverable keys or destroying encryption keys.
* **Real-World Procedures:**
  * Attackers first gain administrative privileges or root access to execute disk wipe commands.
  * Malware often delivered through spear-phishing, compromised software updates, or lateral movement within compromised networks.
  * Wiping operations often scheduled or triggered remotely by attackers after achieving their objectives.
  * Attackers may combine disk wiping with other destructive techniques such as ransomware or DDoS attacks for maximum operational impact.

## When this Technique is Usually Used

Disk wiping is commonly used in various attack scenarios and stages, including:

* **Sabotage and disruption attacks:**
  * Nation-state sponsored cyberattacks targeting critical infrastructure or government systems.
  * Hacktivist operations aiming to disrupt operations as a form of protest or retaliation.
* **Covering tracks and evasion:**
  * Attackers wiping disks to eliminate forensic evidence after exfiltrating sensitive data.
  * Cybercriminal groups erasing logs and traces of malware to hinder incident response and attribution.
* **Ransomware attacks:**
  * Attackers may threaten or actually wipe data if ransom demands are not met.
* **Espionage operations:**
  * Advanced Persistent Threat (APT) groups wiping compromised systems after completing espionage activities to minimize detection and attribution.
* **Final stage of multi-stage cyberattacks:**
  * After attackers have achieved their primary objectives (data theft, espionage, sabotage), disk wiping is employed as a destructive final step.

## How this Technique is Usually Detected

Detection of disk wiping involves monitoring and analyzing various indicators, tools, and behaviors:

* **Monitoring System Logs and Event Logs:**
  * Windows Security Event Logs (Event ID 1102 - audit log cleared).
  * System logs indicating unexpected use of disk formatting or wiping utilities (e.g., `cipher.exe`, `diskpart.exe`, `format.exe`).
* **Endpoint Detection and Response (EDR) Tools:**
  * Detection of suspicious processes and command-line arguments indicative of disk wiping activities.
  * Behavioral analysis detecting mass file deletion, partition table modification, or MBR/GPT corruption.
* **File Integrity Monitoring (FIM) and Disk Activity Monitoring:**
  * Alerts triggered by unusual or large-scale file deletions or modifications.
  * Sudden spikes in disk I/O activity, especially writes to critical system sectors.
* **Network-Based Detection:**
  * Monitoring for known malware command-and-control (C2) infrastructure and communication patterns associated with disk wiping malware.
* **Specific Indicators of Compromise (IoCs):**
  * Hashes and signatures of known disk wiping malware (Shamoon, KillDisk, WhisperGate).
  * Suspicious processes executing commands such as:
    * `cipher.exe /w:<drive>`
    * `diskpart clean`
    * Linux commands like `dd if=/dev/zero of=/dev/sda` or `shred -vfz /dev/sda`
  * Registry modifications and scheduled tasks that trigger wiping commands.

## Why it is Important to Detect This Technique

Early and accurate detection of disk wiping is crucial due to its severe and irreversible impacts on systems and networks:

* **Operational Impact:**
  * Severe disruption of business operations due to loss of critical data and system downtime.
  * Potential permanent loss of intellectual property, financial data, and sensitive customer information.
* **Financial Impact:**
  * High costs associated with data recovery attempts, system rebuilding, and business downtime.
  * Long-term financial consequences due to reputational damage and loss of customer trust.
* **Security and Compliance Impact:**
  * Loss of forensic evidence necessary for incident response and attribution.
  * Regulatory fines and compliance violations resulting from inability to recover or protect data.
* **Strategic Importance of Early Detection:**
  * Early detection can prevent widespread destruction by isolating affected systems and initiating rapid response.
  * Allows security teams to preserve forensic evidence, aiding in attribution and future prevention.
  * Enables timely activation of incident response plans, reducing overall impact and recovery time.

## Examples

Several notable real-world examples illustrate the use of disk wiping techniques in cyberattacks:

1. **Shamoon (Disttrack) Attack (2012, 2016, 2018):**
   * **Scenario:** Nation-state sponsored attackers targeted Saudi Arabian oil company Saudi Aramco and other Middle Eastern entities.
   * **Tools Used:** Shamoon malware, featuring components that overwrite MBR, partition tables, and data files.
   * **Impact:** Over 30,000 workstations rendered inoperable, causing significant operational disruption and financial loss.
2. **Sony Pictures Attack (2014):**
   * **Scenario:** Attackers compromised Sony Pictures Entertainment's network, exfiltrated sensitive data, and subsequently wiped disks.
   * **Tools Used:** Customized disk-wiping malware known as "Destover."
   * **Impact:** Severe disruption of business operations, significant data loss, and reputational damage.
3. **Ukraine Power Grid Attack (2015, 2016):**
   * **Scenario:** Cyberattack targeting Ukrainian power companies, employing disk wiping along with power disruption.
   * **Tools Used:** KillDisk malware, designed to overwrite critical system files and MBR.
   * **Impact:** Power outages affecting hundreds of thousands of citizens, extensive damage to IT infrastructure.
4. **Olympic Destroyer Attack (2018 Winter Olympics):**
   * **Scenario:** Attackers targeted the IT infrastructure supporting the Winter Olympics held in Pyeongchang, South Korea.
   * **Tools Used:** Olympic Destroyer malware, designed to delete shadow copies, event logs, and overwrite critical boot sectors.
   * **Impact:** Temporary disruption of Olympic IT systems, ticketing, and broadcasting operations.
5. **WhisperGate Attack (2022):**
   * **Scenario:** Cyberattack targeting Ukrainian government and financial institutions amid geopolitical tensions.
   * **Tools Used:** WhisperGate malware, masquerading as ransomware but actually designed to irreversibly wipe data.
   * **Impact:** Severe disruption of government and financial systems, permanent data loss, and operational downtime.

These examples underscore the destructive potential of disk wiping techniques, highlighting the importance of robust detection, prevention, and response capabilities.
