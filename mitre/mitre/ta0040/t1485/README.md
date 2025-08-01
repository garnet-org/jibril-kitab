---
description: Data Destruction [T1485]
icon: database
---

# Data Destruction

## Information

* Name: Data Destruction
* ID: T1485
* Tactics: [TA0040](../)
* Sub-Technique: [T1485.001](t1485.001.md)

## Introduction

Data Destruction (T1485) is a tactic categorized under MITRE ATT\&CK's Impact tactic. It refers to adversaries intentionally destroying or corrupting data on victim systems to disrupt operations, cover tracks, or cause permanent damage. This technique can involve deleting files, overwriting data, corrupting file structures, or even destroying entire file systems, rendering data irrecoverable or significantly impaired. Understanding and detecting Data Destruction is critical for maintaining organizational resilience and minimizing operational disruption.

## Deep Dive Into Technique

Data Destruction involves adversaries manipulating data to ensure its permanent loss or corruption. Attackers can execute this technique using various methods and tools:

* **File Deletion**:
  * Attackers use standard operating system utilities such as `del` (Windows), `rm` (Linux/Unix), or PowerShell commands to delete files and directories.
  * Batch scripts or automated scripts can be deployed to systematically remove critical files.
* **Data Overwriting**:
  * Tools like `sdelete` (Windows Sysinternals), `shred` (Linux), or custom scripts overwrite data with random or meaningless characters, making recovery impossible or extremely difficult.
  * Attackers may overwrite Master Boot Records (MBRs) or partition tables, rendering entire disks unreadable.
* **File System Corruption**:
  * Adversaries may intentionally corrupt file system metadata or structures, causing widespread data loss.
  * Malware such as wipers (e.g., Shamoon, NotPetya, WhisperGate) specifically targets file systems and boot sectors, causing irreparable damage.
* **Disk Formatting**:
  * Attackers execute disk formatting commands (`format`, `mkfs`) to erase file systems quickly.
  * Quick formats remove file system metadata, while full formats overwrite data sectors.
* **Firmware-Level Attacks**:
  * Advanced adversaries target firmware or BIOS/UEFI, causing permanent hardware-level damage and data loss.
  * Firmware-level destruction is extremely difficult to remediate and often requires hardware replacement.

## When this Technique is Usually Used

Data Destruction can occur at various stages and scenarios of an attack lifecycle, including:

* **End-stage sabotage**:
  * Attackers execute destructive actions after completing primary objectives, aiming to disrupt or permanently damage victim infrastructure.
  * Common in state-sponsored sabotage operations or cyber warfare scenarios.
* **Ransomware attacks**:
  * Ransomware variants may threaten or execute data destruction to pressure victims into paying ransoms.
  * Attackers may delete data backups to increase leverage against victims.
* **Covering tracks**:
  * Adversaries destroy logs, files, or entire systems to eliminate forensic evidence, hindering incident response and attribution efforts.
* **Insider threats**:
  * Malicious insiders intentionally destroy data to harm an organization, retaliate, or conceal criminal activities.
* **Hacktivism**:
  * Hacktivist groups may destroy data to protest against targeted organizations, causing reputational and operational harm.

## How this Technique is Usually Detected

Detection of Data Destruction involves monitoring and identifying suspicious activities and behaviors using various tools and methods:

* **File Integrity Monitoring (FIM)**:
  * Tools like Tripwire, OSSEC, or built-in Windows File Integrity Monitoring detect unauthorized changes or deletions of critical files.
  * Alerts generated by unexpected large-scale file deletions or modifications.
* **Endpoint Detection and Response (EDR)**:
  * EDR solutions (CrowdStrike, SentinelOne, Microsoft Defender ATP) detect abnormal processes, commands, or scripts indicative of destructive actions.
  * Behavioral analytics identify unusual file deletion or disk formatting commands.
* **Security Information and Event Management (SIEM)**:
  * SIEM platforms correlate logs from various sources (system logs, command-line auditing, event logs) to detect destructive patterns.
  * Alerts triggered by unauthorized execution of destructive commands (`rm`, `del`, `format`, `mkfs`, `shred`, etc.).
* **Backup and Recovery Systems Monitoring**:
  * Monitoring backup systems for signs of tampering or deletion attempts.
  * Detection of disabled or deleted backup processes and data.
* **Network and Host-Based Indicators of Compromise (IoCs)**:
  * Known destructive malware hashes, filenames, signatures, or behaviors.
  * Indicators such as mass file deletion commands, disk formatting attempts, or MBR overwriting.
* **User Behavior Analysis (UBA)**:
  * Detecting anomalous user activity patterns, such as sudden deletion of critical data by privileged accounts.

## Why it is Important to Detect This Technique

Early detection of Data Destruction is crucial due to its significant impacts on organizations, including:

* **Operational Disruption**:
  * Loss of critical data can halt business operations, leading to downtime, productivity losses, and financial impacts.
* **Permanent Data Loss**:
  * Without timely detection and intervention, data destruction may result in irrecoverable loss of intellectual property, customer data, or essential business records.
* **Financial Damage**:
  * Recovery and remediation costs, including forensic investigations, data recovery efforts, and hardware replacements, can be substantial.
* **Reputational Harm**:
  * Organizations suffering data destruction incidents face public scrutiny, loss of customer trust, regulatory penalties, and reduced market confidence.
* **Legal and Compliance Risks**:
  * Data destruction incidents involving sensitive or regulated data can lead to legal consequences and regulatory fines.
* **Incident Response Challenges**:
  * Early detection enables rapid containment and mitigation, reducing complexity and cost of incident response efforts.
  * Failure to detect promptly allows adversaries to erase critical forensic evidence, complicating attribution and investigation.

## Examples

Real-world examples of Data Destruction attacks illustrate techniques, tools, scenarios, and impacts:

* **Shamoon (Disttrack) Attack (2012, 2016, 2018)**:
  * **Scenario**: State-sponsored attackers targeted Saudi Aramco and other Middle Eastern organizations.
  * **Tools Used**: Shamoon malware overwrote MBRs and file systems, rendering thousands of computers unusable.
  * **Impact**: Massive operational disruption, significant financial losses, and lengthy recovery periods.
* **NotPetya Attack (2017)**:
  * **Scenario**: Cyberattack disguised as ransomware targeted Ukraine and global organizations.
  * **Tools Used**: NotPetya malware overwrote MBR, encrypted file systems irreversibly, and prevented data recovery.
  * **Impact**: Estimated global damages exceeding $10 billion; severe operational disruptions for multinational companies like Maersk, Merck, FedEx.
* **Sony Pictures Attack (2014)**:
  * **Scenario**: Attackers infiltrated Sony Pictures' network, stealing data and subsequently destroying systems.
  * **Tools Used**: Malware overwrote critical files and MBRs, permanently disabling systems.
  * **Impact**: Significant financial losses, reputational damage, loss of intellectual property, and prolonged operational disruption.
* **Olympic Destroyer (2018 Winter Olympics)**:
  * **Scenario**: Targeted cyberattack intended to disrupt the Pyeongchang Winter Olympics.
  * **Tools Used**: Olympic Destroyer malware deleted data, disabled systems, and corrupted backups.
  * **Impact**: Temporary disruption of Olympic IT infrastructure and event operations; significant reputational impact.
* **WhisperGate (2022 Ukraine Cyberattack)**:
  * **Scenario**: Cyberattack targeting Ukrainian government agencies and critical infrastructure at the onset of the Russia-Ukraine conflict.
  * **Tools Used**: WhisperGate malware overwrote MBRs and corrupted file systems, causing permanent data loss.
  * **Impact**: Disruption of government services, operational downtime, and heightened geopolitical tensions.
