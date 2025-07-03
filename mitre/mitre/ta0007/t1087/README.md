---
description: Account Discovery [T1087]
icon: users
---

# Account Discovery

## Information

* Name: Account Discovery
* ID: T1087
* Tactics: [TA0007](../)
* Sub-Technique: [T1087.002](t1087.002.md), [T1087.001](t1087.001.md), T1087.003, [T1087.004](t1087.004.md)

## Introduction

Account Discovery (MITRE ATT\&CK Technique ID: T1087) is an adversarial technique used by attackers to identify and enumerate valid user accounts, groups, and system accounts within a targeted system or network. This technique falls under the Discovery tactic within the MITRE ATT\&CK framework, enabling adversaries to gain situational awareness and plan subsequent attack steps. By discovering accounts, attackers can better understand the target's structure, identify privileged accounts, and tailor their strategies for lateral movement and privilege escalation.

## Deep Dive Into Technique

Attackers typically perform Account Discovery to enumerate and analyze user and group accounts across various systems and environments. This technique can be executed through multiple methods, tools, and mechanisms:

* **Operating System Commands and Utilities**:
  * Windows:
    * `net user` – Lists local user accounts.
    * `net localgroup` – Enumerates local groups and members.
    * `net group /domain` – Lists domain groups.
    * `net user /domain` – Lists domain users.
    * PowerShell commands:
      * `Get-LocalUser`
      * `Get-ADUser`
      * `Get-ADGroup`
  * Linux/Unix:
    * `cat /etc/passwd` – Enumerates local user accounts.
    * `cat /etc/group` – Lists local groups and their members.
    * Commands like `id`, `groups`, `whoami` to enumerate current user privileges.
* **Active Directory Enumeration**:
  * LDAP queries to enumerate users and groups.
  * Tools such as BloodHound, PowerView, SharpHound, and ADRecon for detailed enumeration and visualization.
* **Cloud Environment Enumeration**:
  * Enumerating cloud accounts and roles using cloud-provider CLI tools (AWS CLI, Azure CLI, GCP CLI).
  * Using compromised credentials to list cloud IAM roles, users, and permissions.
* **Third-Party Tools and Scripts**:
  * PowerSploit, PowerView, ADRecon, BloodHound, and Impacket scripts for automated account discovery and enumeration.

Attackers often leverage legitimate administrative tools and built-in utilities, making this technique stealthy and difficult to detect without proper monitoring and logging.

## When this Technique is Usually Used

Attackers utilize Account Discovery at various stages within the cyber kill chain, primarily during the reconnaissance and lateral movement phases:

* **Initial Reconnaissance**:
  * After initial compromise, attackers enumerate accounts to understand the target environment.
  * Identifying privileged accounts to target for further exploitation.
* **Privilege Escalation**:
  * Enumerating accounts to discover potential vulnerabilities or weak credentials.
  * Identifying accounts with higher privileges for further exploitation.
* **Lateral Movement**:
  * Enumerating user accounts and groups to identify potential lateral movement paths.
  * Identifying administrative accounts or service accounts to pivot across systems.
* **Persistence and Credential Access**:
  * Discovering accounts to maintain persistent access to compromised systems.
  * Identifying accounts suitable for credential theft and reuse.
* **Cloud Infrastructure Attacks**:
  * Enumerating cloud IAM users, roles, and permissions to escalate privileges in cloud environments.
  * Targeting cloud accounts for lateral movement and data exfiltration.

## How this Technique is Usually Detected

Detection of Account Discovery involves monitoring, logging, and analyzing system activities, command execution, and anomalous user behavior. Detection methods and indicators include:

* **Monitoring Command-Line Activity**:
  * Detecting execution of account enumeration commands (`net user`, `net group`, PowerShell cmdlets, Linux commands like `cat /etc/passwd`).
  * Monitoring command-line arguments and scripting activities indicative of enumeration.
* **Analyzing Logs and Audit Trails**:
  * Windows Security event logs (Event ID 4798, 4799 for local group enumeration; 4661, 4662 for Active Directory enumeration).
  * Linux auditd logs and syslog entries indicating enumeration commands or file access (`/etc/passwd`, `/etc/group`).
* **Behavioral Analytics and Anomaly Detection**:
  * Identifying abnormal enumeration activity patterns from user accounts.
  * Detecting unusual LDAP queries or Active Directory enumeration activities.
* **Endpoint Detection and Response (EDR) Tools**:
  * Using EDR solutions to monitor and alert on suspicious enumeration activities.
  * Integrating threat hunting queries and analytics to detect enumeration behaviors.
* **Network Traffic Analysis**:
  * Detecting unusual LDAP queries, SMB enumeration, or cloud API calls indicative of account discovery.
  * Monitoring network traffic for enumeration tools and scripts (e.g., BloodHound, PowerView).
* **Specific Indicators of Compromise (IoCs)**:
  * Presence of enumeration scripts and tools (e.g., PowerView, ADRecon, BloodHound, SharpHound).
  * Suspicious command-line parameters or scripts executed on endpoints.
  * Unusual access to sensitive files (`/etc/passwd`, `/etc/group`) or Active Directory objects.

## Why it is Important to Detect This Technique

Early detection of Account Discovery is critical to preventing attackers from gaining valuable intelligence and escalating their privileges. Importance includes:

* **Preventing Privilege Escalation**:
  * Early detection limits attackers' ability to identify high-value privileged accounts and reduces the risk of privilege escalation.
* **Reducing Lateral Movement Opportunities**:
  * Detecting enumeration activities prevents attackers from identifying lateral movement paths, limiting their ability to pivot across the network.
* **Protecting Sensitive Information**:
  * Enumeration often precedes data exfiltration or targeted attacks; detection helps protect sensitive data and intellectual property.
* **Reducing Dwell Time**:
  * Early detection reduces attacker dwell time, minimizing damage and potential impact on business operations.
* **Enhancing Incident Response Capability**:
  * Detecting enumeration activities provides valuable indicators for incident responders, enabling faster containment and remediation.
* **Improving Security Posture and Awareness**:
  * Identifying enumeration attempts provides insight into attacker behavior, allowing organizations to strengthen defenses and improve overall security posture.

## Examples

Real-world examples demonstrating Account Discovery include:

* **APT29 (Cozy Bear)**:
  * Utilized PowerShell scripts and PowerSploit's PowerView module to enumerate Active Directory users, groups, and permissions.
  * Leveraged enumeration results to identify privileged accounts and escalate privileges within compromised networks.
* **FIN6 Cybercrime Group**:
  * Used built-in Windows commands (`net user`, `net localgroup`) and PowerShell scripts to discover administrator accounts.
  * Identified accounts suitable for lateral movement within point-of-sale (POS) environments, resulting in significant financial losses.
* **Ryuk Ransomware Attacks**:
  * Performed extensive account enumeration via built-in Windows utilities and third-party tools such as BloodHound.
  * Targeted domain administrator accounts for lateral movement and rapid ransomware deployment across victim networks.
* **Cloud Hopper Attacks (APT10)**:
  * Conducted enumeration of cloud IAM users, roles, and permissions using compromised credentials and cloud-provider CLI tools.
  * Escalated privileges and moved laterally within cloud environments, resulting in extensive data exfiltration and intellectual property theft.
* **Emotet and TrickBot Malware Campaigns**:
  * Leveraged scripts and built-in commands to enumerate local and domain user accounts.
  * Identified high-value targets and accounts for further exploitation by ransomware operators such as Ryuk and Conti.

These examples highlight attackers' frequent reliance on Account Discovery as a foundational step in successful intrusion campaigns, emphasizing the importance of robust detection and response capabilities.
