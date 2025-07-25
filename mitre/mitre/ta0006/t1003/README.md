---
description: OS Credential Dumping [T1003]
icon: key
---

# OS Credential Dumping

## Information

* Name: OS Credential Dumping
* ID: T1003
* Tactics: [TA0006](../)
* Sub-Technique: [T1003.002](t1003.002.md), [T1003.004](t1003.004.md), [T1003.007](t1003.007.md), [T1003.001](t1003.001.md), [T1003.005](t1003.005.md), T1003.008, [T1003.003](t1003.003.md), [T1003.006](t1003.006.md)

## Introduction

OS Credential Dumping (MITRE ATT\&CK ID: T1003) is a technique defined within the MITRE ATT\&CK framework, referring to the extraction of credential information from operating systems. Attackers leverage this method to obtain usernames, passwords, hashes, or tokens, enabling lateral movement, privilege escalation, and persistent access within compromised networks. Credential dumping is a critical step in many cyberattack lifecycles, allowing adversaries to impersonate legitimate users and evade detection mechanisms.

## Deep Dive Into Technique

OS Credential Dumping involves extracting credentials stored or cached within operating systems. Attackers typically target multiple credential storage locations and mechanisms, including:

* **Memory Dumps**: Extracting credentials directly from system memory (RAM), leveraging tools such as Mimikatz, Windows Credential Editor, or LSASS memory dumps.
* **SAM Database**: Dumping password hashes from the Security Account Manager (SAM) database on Windows systems, typically located at `%SystemRoot%\system32\config\SAM`.
* **NTDS.dit Extraction**: Extracting Active Directory user credentials from the NTDS.dit file, which stores domain credentials, usually via Volume Shadow Copy Service (VSS) or direct extraction.
* **Cached Credentials**: Retrieving credentials cached locally on endpoints, typically stored in registry hives.
* **Credential Managers and Vaults**: Accessing credentials stored in Windows Credential Manager, Keychain (macOS), or other OS-specific credential stores.
* **LSA Secrets Extraction**: Accessing Local Security Authority (LSA) secrets, including service account passwords and system-level credentials.
* **Kerberos Ticket Extraction**: Extracting Kerberos tickets (e.g., Ticket Granting Tickets - TGT) from memory to perform Pass-the-Ticket attacks.

Attackers commonly utilize tools such as:

* **Mimikatz**: Widely used for extracting plaintext credentials, Kerberos tickets, and hashes from memory.
* **ProcDump**: Used to create memory dumps of processes, particularly LSASS, for offline credential extraction.
* **Pwdump7, secretsdump.py (Impacket Suite)**: Tools designed specifically to dump password hashes from SAM or NTDS.dit.
* **gsecdump, Windows Credential Editor (WCE)**: Tools for extracting cached credentials and hashes from Windows systems.

## When this Technique is Usually Used

OS Credential Dumping can appear in various stages and scenarios of cyberattacks, including:

* **Initial Access and Reconnaissance**: Attackers may attempt credential dumping immediately after gaining initial access to escalate privileges quickly.
* **Privilege Escalation**: Attackers use this technique to move from lower-privileged accounts to higher-privileged accounts (e.g., from standard user to administrator).
* **Lateral Movement**: Extracted credentials are leveraged to authenticate to other systems within the network, facilitating lateral movement.
* **Persistence**: Attackers may periodically dump credentials to maintain persistent access, even after initial entry vectors have been mitigated.
* **Data Exfiltration and Objective Completion**: Leveraging credentials to access sensitive data repositories, email accounts, databases, or cloud storage.
* **Ransomware and Destructive Attacks**: Attackers often dump credentials to propagate ransomware or destructive malware across networks rapidly.

## How this Technique is Usually Detected

Detection of OS Credential Dumping involves multiple methodologies and tools, including:

* **Endpoint Detection and Response (EDR)**: Tools such as CrowdStrike Falcon, Carbon Black, Microsoft Defender for Endpoint, and SentinelOne can detect suspicious LSASS memory access, abnormal process behaviors, and credential extraction tools.
* **Event Log Monitoring**: Monitoring Windows Security Event logs for suspicious logon attempts, failed authentication events, and unusual privilege escalation events (Event IDs such as 4624, 4625, 4672, 4688).
* **Sysmon and Advanced Logging**: Utilizing Sysinternals Sysmon to detect suspicious process creations, LSASS memory access, or file creation events related to credential dumping tools.
* **Behavioral Analysis and Anomaly Detection**: Identifying abnormal user behaviors, unexpected administrative logins, or lateral movements within the network.
* **File System and Registry Monitoring**: Detecting unauthorized access or extraction attempts from SAM, SECURITY hives, NTDS.dit, and registry keys.
* **Network Traffic Analysis**: Identifying unusual authentication patterns, SMB/RPC traffic indicative of lateral movement, and Kerberos ticket anomalies.

Indicators of Compromise (IoCs) include:

* Presence or execution of known credential dumping tools (e.g., mimikatz.exe, procdump.exe, secretsdump.py).
* Suspicious LSASS memory dumps (e.g., lsass.dmp files).
* Abnormal access or modifications to SAM, SECURITY, or NTDS.dit files.
* Unusual use of administrative privileges or account logins at abnormal times.
* Detection of PowerShell scripts or encoded commands used for credential extraction.

## Why it is Important to Detect This Technique

Early detection of OS Credential Dumping is critical due to the following impacts and risks:

* **Privilege Escalation**: Attackers rapidly escalate privileges, gaining administrative control and full access to sensitive resources.
* **Lateral Movement**: Compromised credentials facilitate movement across multiple systems and network segments, significantly increasing the attack's scope and severity.
* **Persistence and Long-term Compromise**: Extracted credentials enable attackers to maintain persistent footholds within networks, complicating remediation efforts.
* **Data Theft and Exfiltration**: Credential dumping often precedes theft of sensitive data, intellectual property, personal information, and confidential business data.
* **Ransomware and Destructive Attacks**: Credentials enable rapid propagation of ransomware, leading to significant downtime, financial loss, and reputational damage.
* **Compliance and Regulatory Impact**: Credential compromise may lead to regulatory violations, fines, and severe legal consequences.
* **Damage to Trust and Reputation**: Breaches involving credential compromise erode customer trust, corporate reputation, and stakeholder confidence.

## Examples

Real-world examples of OS Credential Dumping attacks include:

* **NotPetya Attack (2017)**:
  * **Scenario**: Ransomware-like destructive malware rapidly spread through compromised credentials extracted via Mimikatz and EternalBlue exploits.
  * **Tools Used**: Mimikatz, EternalBlue exploit, PsExec.
  * **Impact**: Global disruption, billions in damages, widespread business interruptions.
* **WannaCry Ransomware (2017)**:
  * **Scenario**: Leveraged credential dumping techniques to facilitate lateral movement within enterprise networks.
  * **Tools Used**: Mimikatz, EternalBlue exploit.
  * **Impact**: Affected over 200,000 computers globally, causing significant financial and operational disruptions.
* **APT29 (Cozy Bear) Attacks**:
  * **Scenario**: Russian-based threat actor employed credential dumping techniques extensively for espionage and data exfiltration.
  * **Tools Used**: Mimikatz, custom scripts, PowerShell-based credential dumping.
  * **Impact**: Compromise of sensitive government and private-sector information, long-term espionage campaigns.
* **FIN7 Financial Attacks**:
  * **Scenario**: Credential dumping was extensively used to escalate privileges and move laterally within financial institutions and retail chains.
  * **Tools Used**: Mimikatz, Cobalt Strike, custom PowerShell scripts.
  * **Impact**: Massive financial losses, compromise of millions of credit card records, and significant compliance violations.
* **SolarWinds Supply Chain Attack (2020)**:
  * **Scenario**: Attackers leveraged credential dumping to escalate privileges and move laterally within compromised networks.
  * **Tools Used**: Mimikatz, custom credential extraction methods, Cobalt Strike.
  * **Impact**: Extensive compromise of U.S. government agencies and Fortune 500 companies, significant national security implications.
