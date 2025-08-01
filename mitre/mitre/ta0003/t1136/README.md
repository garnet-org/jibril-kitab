---
description: Create Account [T1136]
icon: users
---

# Create Account

## Information

* Name: Create Account
* ID: T1136
* Tactics: [TA0003](../)
* Sub-Technique: [T1136.001](t1136.001.md), [T1136.002](t1136.002.md), [T1136.003](t1136.003.md)

## Introduction

The "Create Account" technique (T1136) within the MITRE ATT\&CK framework involves adversaries creating new user accounts or modifying existing ones to maintain persistence and facilitate lateral movement within compromised systems and networks. Attackers typically leverage this technique to establish a foothold, evade detection, and maintain long-term access, often granting themselves elevated privileges or covert channels for future exploitation.

## Deep Dive Into Technique

Attackers can utilize several methods to create or modify accounts across various platforms and operating systems. Common execution methods include:

* **Windows Environments:**
  * Using built-in commands such as `net user`, `net localgroup`, or PowerShell cmdlets (`New-LocalUser`, `Add-LocalGroupMember`).
  * Directly modifying registry keys or manipulating Security Account Manager (SAM) databases.
  * Leveraging Active Directory utilities (`dsadd`, `New-ADUser`) to create domain-level accounts.
* **Linux/Unix Environments:**
  * Executing commands such as `useradd`, `adduser`, or `passwd` to create and manage accounts.
  * Directly editing `/etc/passwd`, `/etc/shadow`, and `/etc/group` files to manually add accounts or modify existing ones.
  * Utilizing scripts or cron jobs to automate account creation or privilege escalation.
* **Cloud Environments:**
  * Creating new cloud platform accounts (e.g., AWS IAM users, Azure Active Directory accounts, Google Cloud IAM accounts) to maintain persistence and facilitate further access.
  * Modifying permissions and roles associated with existing cloud accounts to escalate privileges or maintain stealthy access.

Adversaries often combine these account creation techniques with privilege escalation methods, ensuring they maintain control even after initial access vectors are mitigated.

## When this Technique is Usually Used

The "Create Account" technique is commonly leveraged throughout various stages of the cyber attack lifecycle, including:

* **Persistence:**
  * Attackers create new accounts to maintain ongoing access after initial compromise, ensuring continued entry even if initial exploits or malware are detected and remediated.
* **Privilege Escalation:**
  * Creating privileged accounts or modifying existing account permissions to elevate privileges and gain administrative-level access.
* **Defense Evasion:**
  * Establishing new accounts to evade detection by blending in with legitimate users, thereby avoiding suspicion from security monitoring tools.
* **Lateral Movement:**
  * Using newly created or modified accounts to move laterally across internal systems, networks, or cloud environments without raising alarms.
* **Credential Access:**
  * Creating accounts with specific privileges to access sensitive data, credentials, or resources, enabling further exploitation or data exfiltration.

## How this Technique is Usually Detected

Detection of unauthorized account creation or modification involves monitoring and analyzing multiple data sources and security mechanisms, including:

* **System and Audit Logs:**
  * Monitoring Windows Event Logs (e.g., Event IDs 4720 for account creation, 4732 for addition to privileged groups).
  * Linux/Unix audit logs (`/var/log/auth.log`, `/var/log/secure`, auditd logs) to detect account creation or modification events.
* **SIEM and Log Management Systems:**
  * Utilizing Security Information and Event Management (SIEM) solutions to correlate account creation events across multiple systems and detect anomalous patterns or unauthorized account creations.
* **Endpoint Detection and Response (EDR) Tools:**
  * Leveraging EDR solutions to detect suspicious commands, scripts, or binaries associated with account creation activities.
* **Cloud Security Monitoring:**
  * Monitoring cloud platform logs (AWS CloudTrail, Azure AD audit logs, Google Cloud audit logs) for suspicious IAM user creation or permission changes.
* **Behavioral Analytics and Anomaly Detection:**
  * Using User and Entity Behavior Analytics (UEBA) tools to detect abnormal account creation activities, such as creation during unusual hours, by unusual users, or with anomalous privileges.
* **Indicators of Compromise (IoCs):**
  * Presence of unfamiliar user accounts or groups on systems.
  * Unusual account naming conventions (e.g., random or nonsensical usernames).
  * Unexpected privilege escalation or changes in user permissions.
  * Suspicious commands in audit logs (`net user`, `useradd`, `dsadd`, etc.).

## Why it is Important to Detect This Technique

Early detection of unauthorized account creation or modification is crucial due to the severe potential impacts on organizations, including:

* **Long-term Persistence:**
  * Undetected accounts enable prolonged attacker presence, increasing risk of data theft, espionage, sabotage, or ransomware deployment.
* **Privilege Escalation and Lateral Movement:**
  * Unauthorized privileged accounts enable attackers to escalate privileges, move laterally, and compromise additional systems and data.
* **Data Exfiltration and Breaches:**
  * Attackers may leverage created accounts to access sensitive data, intellectual property, or personally identifiable information, leading to severe financial and reputational damage.
* **Compliance and Regulatory Risks:**
  * Failure to detect unauthorized account creation can result in regulatory non-compliance, penalties, and legal liabilities.
* **Operational Disruption:**
  * Unauthorized accounts with elevated privileges can disrupt critical business operations, damage infrastructure, or cause service outages.

## Examples

Real-world examples of the "Create Account" technique include:

* **APT29 (Cozy Bear):**
  * Attackers leveraged PowerShell scripts to create local administrative accounts on compromised Windows systems, enabling persistent access and lateral movement within targeted networks.
* **FIN7 Cybercrime Group:**
  * Utilized scripts and batch files (`net user` commands) to create hidden administrative accounts on compromised point-of-sale (POS) systems, facilitating long-term access and data exfiltration of payment information.
* **Lazarus Group:**
  * Created new privileged user accounts on compromised Linux servers by editing `/etc/passwd` and `/etc/shadow` files directly, enabling persistent access and further lateral movement within victim networks.
* **Cloud Hopper Campaign (APT10):**
  * Attackers created new accounts and modified existing account permissions within cloud service providers and managed service providers (MSPs), enabling persistent access and espionage activities targeting multiple client organizations.
* **DarkSide Ransomware Operators:**
  * Created new domain administrator accounts within compromised Active Directory environments, facilitating lateral movement, privilege escalation, and eventual ransomware deployment across enterprise networks.
