---
description: Archive Collected Data [T1560]
icon: database
---

# Archive Collected Data

## Information

* Name: Archive Collected Data
* ID: T1560
* Tactics: [TA0009](../)
* Sub-Technique: [T1560.001](t1560.001.md), [T1560.003](t1560.003.md), [T1560.002](t1560.002.md)

## Introduction

Archive Collected Data (T1560) is a technique within the MITRE ATT\&CK framework categorized under the "Collection" tactic. Attackers often archive data collected from compromised systems to facilitate easier exfiltration, concealment, or to compress large data sets. Archiving makes data easier to manage, transfer, and evade detection by security tools that monitor file transfers based on file types or sizes. Common archiving methods include ZIP, RAR, TAR, GZIP, and 7zip formats, sometimes combined with encryption to further obscure the data.

## Deep Dive Into Technique

Attackers typically use built-in system tools or third-party utilities to archive data before exfiltration. The archiving process can involve:

* **Native OS Utilities**:
  * Windows: `zip`, `tar`, `makecab`, `compress`, PowerShell's `Compress-Archive`.
  * Linux/Unix: `tar`, `gzip`, `zip`, `bzip2`, `xz`.
* **Third-party Archiving Tools**:
  * WinRAR, 7-Zip, WinZip, PeaZip.
* **Encryption and Password Protection**:
  * Attackers commonly encrypt archives with passwords to evade detection by network defenses.
  * Encryption methods include AES encryption integrated within archive utilities.
* **Automated Scripts and Batch Files**:
  * Attackers frequently automate archiving and exfiltration through scripts (Bash, PowerShell, batch scripts).
  * Automation allows attackers to quickly and efficiently collect and compress large volumes of data.
* **Compression for Stealth**:
  * Compression reduces file size, making exfiltration quicker and less noticeable.
  * Compressed archives may evade detection by security solutions that rely on file type or size thresholds.
* **Obfuscation Techniques**:
  * Renaming archive files to benign-looking names or extensions (e.g., `.jpg`, `.dat`, `.tmp`) to evade detection.
  * Splitting archives into smaller segments to bypass data exfiltration monitoring.

## When this Technique is Usually Used

Attackers employ the Archive Collected Data technique across various stages of the cyber-attack lifecycle, typically during:

* **Collection Stage**:
  * After identifying valuable data, attackers archive it to streamline exfiltration.
  * Archiving helps attackers manage large data sets efficiently.
* **Exfiltration Stage**:
  * Compressed archives allow attackers to move data out of the network more quickly and quietly.
  * Smaller file sizes reduce the likelihood of triggering alarms or data transfer thresholds.
* **Persistence and Lateral Movement Stages**:
  * Attackers may archive and store sensitive data on compromised systems for later exfiltration.
  * Archived data can be moved laterally across systems within the victim's network to consolidate exfiltration points.
* **Data Theft and Espionage Scenarios**:
  * Espionage-focused adversaries archive large volumes of sensitive documents, emails, intellectual property, or financial information for targeted exfiltration.
  * Cybercriminals archive personally identifiable information (PII), payment card data, or credentials for sale or further exploitation.

## How this Technique is Usually Detected

Detection of the Archive Collected Data technique involves monitoring system activities, file changes, and network behaviors. Common detection methods and indicators include:

* **Endpoint Monitoring and Logging**:
  * Monitoring process creation events for archive tools (`zip.exe`, `rar.exe`, `7z.exe`, `tar`, `gzip`, etc.).
  * Identifying unusual command-line parameters associated with archiving tools.
  * Detecting scripts or batch files executing archive commands.
* **File System Auditing**:
  * Monitoring for sudden appearance of large archive files on endpoints or servers.
  * Detecting archives with unusual file names, extensions, or locations.
  * Identifying large volumes of sensitive data being compressed into archives.
* **Network Traffic Analysis**:
  * Monitoring outbound network traffic for large file transfers or transfers of archive file types.
  * Analyzing encrypted or password-protected archives leaving the network.
  * Detecting unusual data transfer patterns, such as segmented archive uploads.
* **Security Tools and Solutions**:
  * Endpoint Detection and Response (EDR) solutions that monitor and alert on archiving activities.
  * Data Loss Prevention (DLP) tools configured to detect sensitive or confidential data being archived and prepared for exfiltration.
  * Security Information and Event Management (SIEM) tools correlating events related to file archiving and exfiltration attempts.
* **Specific Indicators of Compromise (IoCs)**:
  * Presence of archive utilities not commonly used in the environment.
  * Unexpected scripts or batch files containing archiving commands.
  * Suspiciously named archives (e.g., random strings, misleading extensions).
  * Archives located in temporary directories or hidden folders.

## Why it is Important to Detect This Technique

Timely detection of the Archive Collected Data technique is crucial for limiting damage and preventing data loss. Key impacts and reasons for early detection include:

* **Preventing Data Exfiltration**:
  * Detecting and interrupting the archiving process can prevent attackers from successfully exfiltrating sensitive information.
  * Early detection allows incident response teams to contain and remediate the threat before substantial data loss occurs.
* **Reducing Operational and Financial Damage**:
  * Early detection minimizes the amount of sensitive or proprietary data stolen, reducing potential financial, reputational, and legal impacts.
  * Prevents attackers from leveraging stolen data for ransom, blackmail, or resale.
* **Identifying and Responding to Ongoing Intrusions**:
  * Detecting archiving activity can reveal ongoing intrusion campaigns, allowing defenders to understand attacker objectives, tactics, and targets.
  * Helps incident responders identify the scope and scale of the compromise.
* **Compliance and Regulatory Requirements**:
  * Organizations subject to compliance mandates (e.g., GDPR, HIPAA, PCI-DSS) must detect and prevent unauthorized data access and exfiltration.
  * Failure to detect and respond to this technique can lead to regulatory penalties, legal liabilities, and reputational harm.
* **Improving Overall Security Posture**:
  * Detection and analysis of archiving activities provide insights into attacker behaviors and targets, enabling defenders to strengthen security controls and policies.
  * Enhances organizational readiness and resilience against future cyber threats.

## Examples

Real-world examples demonstrating the Archive Collected Data technique include:

* **APT29 (Cozy Bear)**:
  * Used `7-zip` and `WinRAR` utilities to compress and encrypt stolen data before exfiltration.
  * Attackers archived sensitive governmental and diplomatic documents, facilitating stealthy exfiltration over encrypted channels.
* **FIN7 Cybercrime Group**:
  * Leveraged PowerShell scripts to archive payment card data and personally identifiable information (PII) from compromised retail and hospitality organizations.
  * Archived data was then exfiltrated and sold on underground marketplaces, causing significant financial and reputational damage to victims.
* **DarkSide Ransomware**:
  * Archived critical business data before encrypting victim systems, threatening to release sensitive information publicly if ransom demands were not met.
  * Attackers used automated scripts to archive and exfiltrate data rapidly, increasing pressure on victims to pay ransom.
* **Operation Aurora (Chinese Espionage Campaign)**:
  * Attackers compressed intellectual property, source code, and sensitive documents before exfiltration.
  * Utilized native utilities (`zip`, `rar`) and encrypted archives to evade detection by network monitoring and DLP solutions.
* **Conti Ransomware Group**:
  * Archived and exfiltrated sensitive data from healthcare, government, and corporate victims.
  * Threatened public data leaks if ransom demands were not met, leveraging archived data as leverage in extortion schemes.

These examples illustrate the widespread use of Archive Collected Data across diverse threat actors, motivations, and industries, highlighting the critical importance of detection and mitigation strategies.
