---
description: User Execution [T1204]
icon: play
---

# User Execution

## Information

* Name: User Execution
* ID: T1204
* Tactics: [TA0002](../)
* Sub-Technique: [T1204.002](t1204.002.md), [T1204.003](t1204.003.md), [T1204.001](t1204.001.md)

## Introduction

Credential Dumping (MITRE ATT\&CK ID: T1003) refers to techniques used by adversaries to obtain account login and password information from a compromised system. Attackers utilize credential dumping to escalate privileges, move laterally within a network, and maintain persistent access. This technique is crucial for attackers because valid credentials often allow them to blend in with legitimate user activity, making detection challenging.

## Deep Dive Into Technique

Credential dumping involves extracting authentication credentials from various sources within operating systems or applications. Attackers typically utilize specialized tools, scripts, or built-in system utilities to perform credential extraction. The most commonly targeted credential storage locations include:

* **Memory (RAM)**:
  * Credentials temporarily stored in memory, such as plaintext passwords, hashes, or Kerberos tickets.
  * Tools like Mimikatz, WCE (Windows Credential Editor), and ProcDump can extract credentials directly from memory.
* **Local Security Authority Subsystem Service (LSASS)**:
  * Windows LSASS.exe process stores user credentials in memory during interactive logins.
  * Attackers use tools like Mimikatz, ProcDump, or Task Manager to dump LSASS memory and extract credentials offline.
* **Windows Registry and SAM Database**:
  * Windows Security Account Manager (SAM) database stores local account password hashes.
  * Attackers can leverage tools such as reg.exe, regedit, or specialized scripts to extract and crack these hashes.
* **NTDS.dit (Active Directory Database)**:
  * Stores domain user credentials and password hashes.
  * Attackers extract this file from domain controllers using tools such as Ntdsutil.exe, Volume Shadow Copy Services (VSS), or invoke-DCsync attacks via Mimikatz.
* **Credential Manager and Browser Storage**:
  * Credentials cached by web browsers or Windows Credential Manager.
  * Attackers use scripts or tools like LaZagne or SharpWeb to extract stored credentials.

Credential dumping techniques include:

* **Memory Dumping**: Extracting credentials directly from volatile memory.
* **Offline Credential Extraction**: Copying credential storage files (SAM, NTDS.dit) offline for cracking.
* **Credential Injection**: Using extracted hashes or tickets in pass-the-hash or pass-the-ticket attacks.
* **Registry Extraction**: Reading credential data directly from registry hives.

## When this Technique is Usually Used

Credential dumping appears frequently across multiple stages and scenarios in cyber attacks, including:

* **Initial Access and Privilege Escalation**:
  * Attackers perform credential dumping immediately after initial compromise to escalate privileges and gain administrative access.
* **Lateral Movement**:
  * Credential dumping provides attackers with valid credentials to move laterally within the network without raising suspicion.
* **Persistence and Defense Evasion**:
  * Attackers maintain persistent access by reusing credentials extracted during earlier stages.
* **Reconnaissance and Data Collection**:
  * Attackers collect credentials to map user roles, privileges, and sensitive resources within the environment.
* **Exfiltration and Impact**:
  * Credential dumping enables attackers to access sensitive information, intellectual property, or critical systems, facilitating data theft or destructive actions.

## How this Technique is Usually Detected

Multiple methods and tools can detect credential dumping, including:

* **Endpoint Detection and Response (EDR)**:
  * Tools such as CrowdStrike Falcon, Carbon Black, SentinelOne, and Microsoft Defender ATP monitor suspicious memory access, LSASS dumping, and anomalous process behaviors.
* **Behavioral Analytics and SIEM Solutions**:
  * Security Information and Event Management (SIEM) tools like Splunk, QRadar, and Elastic Security detect abnormal logon patterns, suspicious process executions, and registry access.
* **Monitoring LSASS Memory Access**:
  * Detection of abnormal LSASS process memory reads or memory dumps (e.g., via Sysmon event ID 10).
* **Audit and Event Logs**:
  * Monitoring Windows Security event logs (Event ID 4624, 4672, 4688) for suspicious logins, privilege escalations, and unexpected process executions.
* **Network Traffic Analysis**:
  * Detection of anomalous Kerberos ticket requests, NTLM authentications, or abnormal SMB traffic patterns.

Indicators of Compromise (IoCs) include:

* Unusual processes accessing LSASS.exe memory.
* Presence of dumped memory files (e.g., lsass.dmp).
* Suspicious registry hive exports (SAM, SECURITY, SYSTEM).
* Execution of known credential dumping tools (Mimikatz, LaZagne, WCE).
* Abnormal account logins, unusual administrative activity, or anomalous lateral movements.

## Why it is Important to Detect This Technique

Early detection of credential dumping is crucial due to the severe consequences and wide-ranging impacts on systems and networks, including:

* **Privilege Escalation**:
  * Attackers gain administrative privileges, enabling full control over systems and data.
* **Lateral Movement**:
  * Compromised credentials allow attackers to move undetected across the network, accessing sensitive data and resources.
* **Persistence and Long-term Compromise**:
  * Attackers leverage stolen credentials to maintain persistent access, complicating remediation efforts.
* **Data Theft and Exfiltration**:
  * Credential dumping can directly lead to unauthorized access to sensitive information, intellectual property, and trade secrets.
* **Operational Disruption and Damage**:
  * Attackers with administrative credentials can disrupt critical systems, deploy ransomware, or cause system outages.
* **Reduced Detection Visibility**:
  * Legitimate credentials allow attackers to blend into normal user activity, making detection significantly harder.

## Examples

Real-world examples illustrating credential dumping include:

* **NotPetya (2017)**:
  * Malware leveraged credential dumping techniques via Mimikatz to extract credentials from LSASS memory, enabling rapid lateral movement across networks, causing widespread operational disruptions and financial losses.
* **WannaCry (2017)**:
  * Ransomware used credential dumping to harvest credentials from compromised hosts, facilitating lateral propagation throughout networks, impacting healthcare, financial, and government institutions globally.
* **APT29 (Cozy Bear)**:
  * Russian state-sponsored attackers utilized credential dumping to obtain administrative credentials, enabling persistent access and lateral movement within targeted organizations, including government agencies.
* **Ryuk Ransomware**:
  * Attackers employed credential dumping via Mimikatz and other tools to obtain domain administrator credentials, enabling widespread encryption of critical systems and data exfiltration.
* **FIN6 Cybercrime Group**:
  * Attackers targeted retail and financial institutions, performing credential dumping to escalate privileges and move laterally, ultimately stealing payment card data and financial information.

Commonly used tools and techniques within these attacks include:

* **Mimikatz**:
  * Widely used to dump credentials from memory, LSASS, and domain controllers.
* **ProcDump and Task Manager**:
  * Legitimate system utilities leveraged to dump LSASS memory for offline credential extraction.
* **Invoke-DCsync (Mimikatz)**:
  * Technique used to remotely extract credentials from Active Directory domain controllers without direct access.
* **LaZagne and SharpWeb**:
  * Tools specifically designed to extract stored passwords from browsers, email clients, and credential managers.

The impacts of these attacks include substantial financial losses, operational disruptions, reputational damage, intellectual property theft, and significant remediation efforts.
