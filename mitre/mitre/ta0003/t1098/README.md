---
description: Account Manipulation [T1098]
icon: users
---

# Account Manipulation

## Information

* Name: Account Manipulation
* ID: T1098
* Tactics: [TA0003](../), [TA0004](../../ta0004/)
* Sub-Technique: [T1098.003](t1098.003.md), [T1098.006](t1098.006.md), [T1098.007](t1098.007.md), [T1098.004](t1098.004.md), [T1098.005](t1098.005.md), [T1098.001](t1098.001.md), [T1098.002](t1098.002.md)

## Introduction

Account Manipulation (T1098) is a technique categorized within the MITRE ATT\&CK framework under the tactic of Persistence, Privilege Escalation, and Defense Evasion. Attackers leverage this technique to maintain persistent access to compromised systems, elevate their privileges, or evade detection by altering, creating, or deleting user and system accounts. Manipulating accounts allows adversaries to blend into legitimate administrative activities, making detection challenging and enabling prolonged access within targeted environments.

## Deep Dive Into Technique

Account Manipulation involves attackers modifying existing user accounts or creating new accounts to maintain persistence, escalate privileges, or evade detection. Technical execution methods and mechanisms include:

* **Creating New Accounts:**
  * Attackers may create local or domain accounts, such as standard user accounts or administrative accounts, to maintain access.
  * On Windows systems, adversaries may use command-line utilities such as:
    * `net user <username> <password> /add`
    * PowerShell cmdlets: `New-LocalUser`, `New-ADUser`
  * On Linux/Unix systems:
    * Commands like `useradd`, `adduser`, and editing `/etc/passwd` or `/etc/shadow` directly.
* **Modifying Existing Accounts:**
  * Attackers may alter account permissions, privileges, or group memberships to escalate privileges or maintain access.
  * Windows:
    * Commands such as `net localgroup administrators <username> /add`
    * PowerShell scripts to modify Active Directory group memberships or user attributes.
  * Linux/Unix:
    * Commands such as `usermod`, editing `/etc/group`, or directly manipulating PAM configurations.
* **Deleting or Disabling Accounts:**
  * Attackers may disable or delete accounts to disrupt legitimate administrative activities or hide their tracks.
  * Windows:
    * `net user <username> /delete`
    * PowerShell cmdlets: `Remove-LocalUser`, `Remove-ADUser`
  * Linux/Unix:
    * Commands such as `userdel` or editing system files directly.
* **Manipulating Account Attributes:**
  * Attackers may alter account attributes (e.g., password expiration, login scripts, home directories) to facilitate persistence or privilege escalation.
  * Windows Active Directory:
    * Using tools like Active Directory Users and Computers (ADUC), PowerShell, or direct LDAP queries.
  * Linux/Unix:
    * Modifying files like `/etc/passwd`, `/etc/shadow`, and `/etc/login.defs`.

## When this Technique is Usually Used

Account Manipulation is commonly employed during various stages and scenarios of cyberattacks:

* **Persistence:**
  * Attackers create or modify accounts to ensure persistent access even after system reboots or credential changes.
  * Commonly used after initial compromise (post-exploitation).
* **Privilege Escalation:**
  * Attackers modify existing accounts or create new accounts with elevated privileges to gain administrative control.
  * Often occurs immediately after initial foothold establishment or lateral movement.
* **Defense Evasion:**
  * Attackers manipulate accounts to blend into legitimate administrative activities, making detection challenging.
  * Deleting or disabling accounts may also be used to disrupt defensive operations or hide attacker presence.
* **Credential Access:**
  * Attackers may alter account password policies or attributes to facilitate easier credential harvesting.
* **Impact Stage:**
  * Attackers may disable or delete legitimate accounts to disrupt organizational operations or hinder incident response.

## How this Technique is Usually Detected

Detection of Account Manipulation involves monitoring and analyzing various system logs, configurations, and behaviors. Common detection methods, tools, and indicators of compromise (IoCs) include:

* **Windows Event Logs:**
  * Security logs (Event IDs):
    * `4720`: User account created
    * `4722`: User account enabled
    * `4725`: User account disabled
    * `4726`: User account deleted
    * `4732`, `4733`: Security-enabled local group membership changes
    * `4738`: User account attributes changed
  * System logs for unusual service account creations or modifications.
* **Linux/Unix Logs:**
  * `/var/log/auth.log`, `/var/log/secure` for account creation, deletion, or modifications.
  * Monitoring changes to files such as `/etc/passwd`, `/etc/shadow`, `/etc/group`.
* **Active Directory Monitoring:**
  * Tools like Microsoft Defender for Identity, Azure AD Audit Logs, and third-party solutions (Splunk, Elastic Security, CrowdStrike Falcon, SentinelOne).
  * LDAP queries and monitoring of unusual account attribute changes.
* **Endpoint Detection and Response (EDR) and SIEM Tools:**
  * Real-time monitoring for suspicious account activities.
  * Alerting on unusual account creation, modification, or deletion events.
* **Behavioral Analytics:**
  * Detecting anomalous account behaviors, such as logins from unusual locations or times, sudden privilege escalations, or account creations/deletions outside normal administrative hours.
* **Indicators of Compromise (IoCs):**
  * Unexpected or unauthorized accounts appearing in user directories or Active Directory.
  * Sudden privilege escalation of existing accounts.
  * Disabled or deleted legitimate administrative accounts without proper authorization.
  * Unusual logins or account modifications from suspicious or unknown sources.

## Why it is Important to Detect This Technique

Early detection of Account Manipulation is critical due to its significant impacts on security posture, operational integrity, and organizational trust. Possible impacts and reasons for importance include:

* **Persistent Access:**
  * Undetected manipulated accounts enable attackers to retain long-term access, increasing risk of prolonged breaches and data exfiltration.
* **Privilege Escalation:**
  * Attackers gaining elevated privileges can perform further malicious actions, including lateral movement, data theft, ransomware deployment, or sabotage of critical systems.
* **Operational Disruption:**
  * Deletion or disabling of legitimate accounts disrupts business operations, leading to service outages, productivity loss, and potential financial harm.
* **Difficulty of Remediation:**
  * Manipulated accounts complicate incident response and remediation efforts, making it challenging to fully eradicate attacker presence.
* **Compliance and Regulatory Implications:**
  * Failure to detect and respond to account manipulation may lead to breaches of compliance standards (e.g., GDPR, HIPAA, PCI DSS), resulting in legal penalties and reputational damage.
* **Increased Risk of Insider Threats:**
  * Manipulated accounts may be leveraged to mimic insider behaviors, complicating attribution and response.

## Examples

Real-world examples of Account Manipulation in attack scenarios include:

* **APT29 (Cozy Bear):**
  * Utilized account manipulation techniques to maintain persistent access within targeted networks by creating new domain administrator accounts and modifying existing accounts.
  * Tools used: PowerShell scripts, custom malware, and legitimate administrative utilities.
  * Impact: Persistent espionage activities, data theft, and prolonged breaches.
* **FIN7 Cybercrime Group:**
  * Created new Windows administrative accounts after initial compromise to maintain persistent access and evade detection.
  * Tools used: PowerShell scripts, Cobalt Strike, and built-in Windows utilities (`net user`, `net localgroup`).
  * Impact: Financial data theft, unauthorized access to payment card data, and significant financial losses for targeted organizations.
* **NotPetya Ransomware Attack:**
  * Manipulated Active Directory accounts to escalate privileges and propagate rapidly across networks.
  * Tools used: Mimikatz, built-in Windows commands, and credential theft techniques.
  * Impact: Massive global disruption, significant financial damages, and operational downtime across multiple industries.
* **Operation Cloud Hopper (APT10):**
  * Leveraged account manipulation by creating new accounts and altering existing ones within managed service providers (MSPs) to gain persistent access to customer networks.
  * Tools used: Custom malware, PowerShell scripts, and legitimate administrative tools.
  * Impact: Espionage, intellectual property theft, and prolonged unauthorized access.
* **Insider Threat Scenarios:**
  * Malicious insiders manipulating or creating unauthorized accounts to exfiltrate sensitive data or disrupt organizational operations.
  * Tools used: Standard administrative tools, scripting languages, and direct system configuration edits.
  * Impact: Data breaches, operational disruptions, reputational harm, and financial losses.
