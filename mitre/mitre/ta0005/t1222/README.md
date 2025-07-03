---
description: File and Directory Permissions Modification [T1222]
icon: file
---

# File and Directory Permissions Modification

## Information

* Name: File and Directory Permissions Modification
* ID: T1222
* Tactics: [TA0005](../)
* Sub-Technique: [T1222.002](t1222.002.md), [T1222.001](t1222.001.md)

## Introduction

File and Directory Permissions Modification is a technique categorized under the MITRE ATT\&CK framework (Technique ID: T1222). Attackers manipulate the permissions and access controls of files and directories to maintain persistence, escalate privileges, restrict legitimate user access, or facilitate further malicious activities. By altering permissions, attackers can secure long-term footholds, evade detection, and disrupt normal operations.

## Deep Dive Into Technique

Attackers utilize a variety of methods and tools to modify file and directory permissions, primarily targeting access control lists (ACLs), discretionary access control lists (DACLs), and standard file permission settings. Technical details include:

* **Operating System Commands**:
  * Windows:
    * `icacls`, `cacls`, `takeown` for modifying permissions and ownership.
    * PowerShell cmdlets like `Set-Acl`, `Get-Acl`.
  * Linux/Unix:
    * `chmod`, `chown`, `chattr`, `setfacl`, `umask`.
* **Mechanisms of Execution**:
  * Altering permissions to grant elevated privileges to attacker-controlled accounts.
  * Restricting permissions to deny legitimate users or security tools access to critical files.
  * Setting immutable attributes (`chattr +i`) on files to prevent modification or deletion by legitimate administrators.
  * Adjusting ACLs to hide malicious files or directories from standard user views.
* **Real-world Procedures**:
  * Malware or attackers may create hidden directories with restricted permissions to store persistent payloads.
  * Ransomware may modify permissions to deny legitimate user access to critical data.
  * Advanced Persistent Threats (APTs) may manipulate file permissions to maintain long-term persistence and evade detection by security tools.

## When this Technique is Usually Used

Attackers commonly utilize file and directory permissions modification across multiple stages of the attack lifecycle:

* **Persistence**:
  * Ensuring continued access by modifying permissions to prevent removal or detection of malware.
* **Privilege Escalation**:
  * Exploiting weak or improperly configured permissions to escalate privileges to administrative or root levels.
* **Defense Evasion**:
  * Restricting permissions to evade detection by endpoint security products and administrative audits.
  * Hiding malicious artifacts by adjusting directory permissions to limit visibility.
* **Impact**:
  * Denying access to legitimate users as part of disruptive attacks, such as ransomware.
  * Causing downtime or loss of data availability through restrictive permission changes.

## How this Technique is Usually Detected

Detection of unauthorized file and directory permission modifications relies on various methods, tools, and indicators of compromise (IoCs):

* **Monitoring and Logging**:
  * Enable auditing of permission changes on critical files and directories (Windows Security Event Logs: event ID 4670, 4671).
  * Linux auditd logs capturing `chmod`, `chown`, `setfacl`, and `chattr` operations.
* **Endpoint Detection and Response (EDR)**:
  * Tools that monitor file system activity and alert on suspicious permission changes.
  * Behavioral analytics detecting anomalous permission modifications performed by unusual users or accounts.
* **File Integrity Monitoring (FIM)**:
  * Solutions like Tripwire, OSSEC, or built-in OS tools that alert on unauthorized permission or attribute changes.
* **Specific Indicators of Compromise (IoCs)**:
  * Sudden changes to critical system files and directories permissions.
  * Files or directories marked as immutable (`chattr +i`) without legitimate administrative activity.
  * Unusual ACL entries granting elevated privileges to unknown or unauthorized accounts.
  * Repeated failed access attempts by legitimate users or services due to permission-denied errors.

## Why it is Important to Detect This Technique

Early detection of unauthorized file and directory permissions modification is crucial due to significant potential impacts on systems and networks:

* **Persistence and Privilege Escalation**:
  * Attackers may establish persistent access or escalate privileges, leading to prolonged compromise and increased difficulty in remediation.
* **Data Integrity and Confidentiality**:
  * Unauthorized permission changes can compromise sensitive data confidentiality and integrity, exposing organizations to data breaches and compliance violations.
* **Availability and Operational Impact**:
  * Permission modifications can disrupt normal operations, causing denial of service conditions or operational downtime.
* **Detection and Response Challenges**:
  * Attackers who successfully modify permissions can evade detection by security tools, increasing the complexity and cost of incident response.
* **Regulatory and Compliance Risks**:
  * Failure to detect unauthorized permission changes can lead to non-compliance with regulatory standards (e.g., GDPR, HIPAA, PCI DSS), resulting in financial penalties and reputational damage.

## Examples

Real-world examples demonstrate the practical use and impact of file and directory permissions modification:

* **NotPetya Ransomware Attack (2017)**:
  * Scenario: NotPetya ransomware encrypted files and modified permissions to deny legitimate user access.
  * Tools and Methods: Windows utilities (`icacls`) were used to restrict file permissions, preventing recovery efforts.
  * Impact: Global disruptions, significant operational downtime, and billions of dollars in damages.
* **APT29 (Cozy Bear) Operations**:
  * Scenario: APT29 modified directory permissions and ACLs to hide persistent malware payloads and evade detection.
  * Tools and Methods: Linux commands (`chmod`, `chattr`) and Windows PowerShell scripts (`Set-Acl`) were utilized to enforce restrictive permissions.
  * Impact: Long-term espionage campaigns, data exfiltration, and persistent compromise of critical infrastructure.
* **CryptoLocker Ransomware**:
  * Scenario: CryptoLocker malware adjusted file permissions to restrict access to encrypted files, forcing victims to pay ransom.
  * Tools and Methods: Windows built-in commands (`icacls`, `cacls`) automated within malware payloads.
  * Impact: Significant financial losses, data loss, and operational disruption for affected organizations.
* **Operation Aurora (2009-2010)**:
  * Scenario: Attackers leveraged permission modifications to maintain persistence and evade detection in targeted espionage campaigns.
  * Tools and Methods: Custom scripts and built-in Windows utilities to adjust ACLs and permissions on compromised systems.
  * Impact: Intellectual property theft, prolonged compromise, and significant reputational damage to targeted companies.
