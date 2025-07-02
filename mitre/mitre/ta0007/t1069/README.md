---
description: Permission Groups Discovery [T1069]
icon: lock
---

# Permission Groups Discovery

## Information

* Name: Permission Groups Discovery
* ID: T1069
* Tactics: [TA0007](../)
* Sub-Technique: [T1069.003](t1069.003.md), [T1069.002](t1069.002.md), [T1069.001](t1069.001.md)

## Introduction

Permission Groups Discovery (T1069.001) is a reconnaissance technique categorized within the MITRE ATT\&CK framework under the Discovery tactic. Attackers utilize this method to enumerate local or domain permission groups, allowing them to gather critical information about user privileges, roles, and access rights within a compromised environment. By identifying permission groups, adversaries can strategically plan lateral movement, privilege escalation, and persistence within targeted networks.

## Deep Dive Into Technique

Permission Groups Discovery involves enumerating group memberships and permissions assigned to users or services within a Windows, Linux, or Active Directory environment. Attackers typically use built-in system commands, scripting languages, or specialized tools to query this information.

Common execution methods include:

* **Windows Environments:**
  * `net localgroup`: Lists local groups and their members.
  * `net group /domain`: Enumerates domain groups.
  * `whoami /groups`: Displays group memberships of the current user.
  * PowerShell cmdlets such as `Get-ADGroup`, `Get-LocalGroup`, and `Get-ADGroupMember`.
  * Using Windows Management Instrumentation (WMI) queries for group enumeration.
* **Linux Environments:**
  * `groups`: Lists groups for the current user.
  * `id`: Provides detailed information about the user's identity, including group memberships.
  * Inspecting `/etc/group` file directly to enumerate existing groups and their members.
* **Third-party Tools and Frameworks:**
  * BloodHound: Graphically maps Active Directory relationships and permissions.
  * PowerView: PowerShell-based toolkit for enumerating Active Directory objects and permissions.
  * ADRecon: Tool designed specifically to enumerate Active Directory environments, including permission groups.

Attackers leverage this information to:

* Identify privileged accounts and groups for targeted attacks.
* Map organizational structures and administrative hierarchies.
* Discover potential paths for lateral movement or privilege escalation.

## When this Technique is Usually Used

Permission Groups Discovery typically occurs in various stages of a cyberattack lifecycle, including:

* **Initial Reconnaissance:**
  * Early-stage reconnaissance after initial access to map the internal network structure and identify high-value targets.
* **Privilege Escalation:**
  * Identifying privileged groups (e.g., Domain Admins, Enterprise Admins, local Administrators) to escalate privileges strategically.
* **Lateral Movement:**
  * Determining accounts and groups with access to sensitive or critical systems to facilitate lateral movement.
* **Persistence:**
  * Understanding group memberships to establish persistent mechanisms or backdoors with appropriate privileges.
* **Credential Access:**
  * Identifying groups with elevated privileges to target their credentials for further exploitation.

## How this Technique is Usually Detected

Detection methods for Permission Groups Discovery include monitoring and logging specific commands, access patterns, and behaviors that indicate enumeration activities:

* **Command-Line Monitoring:**
  * Detecting execution of enumeration commands such as `net localgroup`, `net group /domain`, `whoami /groups`, `id`, and `groups`.
* **PowerShell Logging:**
  * Enabling script block logging, module logging, and transcription to detect PowerShell-based enumeration activities (e.g., PowerView).
* **Windows Event Logs:**
  * Monitoring relevant security events (e.g., Event ID 4798, 4799 for group membership changes, Event ID 4688 for process creation) to detect suspicious enumeration activity.
* **Endpoint Detection and Response (EDR) Tools:**
  * Utilizing behavioral analytics to detect unusual enumeration patterns and suspicious scripts.
* **Network Monitoring and IDS/IPS:**
  * Detecting unusual LDAP queries or SMB traffic patterns indicative of group enumeration activities.

Specific Indicators of Compromise (IoCs):

* Frequent or unusual execution of enumeration commands from unexpected hosts or users.
* Suspicious scripts or binaries (e.g., PowerView.ps1, BloodHound collectors) found on endpoints.
* Sudden spikes in LDAP queries or SMB traffic originating from non-administrative users or hosts.

## Why it is Important to Detect This Technique

Early detection of Permission Groups Discovery is crucial due to its significant impact on the security posture of an organization:

* **Privilege Escalation Risk:**
  * Attackers often use permission group information to identify and escalate privileges, gaining administrative control over systems or networks.
* **Lateral Movement Facilitation:**
  * Enumerating permission groups helps attackers identify pathways for lateral movement, rapidly spreading through internal networks and compromising multiple systems.
* **Data Exfiltration and Exposure:**
  * Identifying high-privileged groups allows attackers to access sensitive data, intellectual property, or confidential business information, leading to potential data breaches.
* **Persistence and Long-Term Compromise:**
  * Attackers leverage group enumeration to establish persistent footholds within the environment, complicating remediation efforts.
* **Operational Disruption:**
  * Unauthorized access to privileged groups can lead to system downtime, data corruption, or sabotage, causing significant operational and financial impacts.

Early detection allows security teams to proactively respond, limit damage, and disrupt attacker activities before significant harm occurs.

## Examples

Real-world examples demonstrating Permission Groups Discovery include:

* **APT29 (Cozy Bear):**
  * Utilized PowerShell scripts (PowerView) to enumerate Active Directory groups and identify privileged accounts during the SolarWinds compromise.
  * Impact: Gained persistent access to sensitive government and corporate networks, leading to extensive data exfiltration.
* **FIN6 Group:**
  * Conducted permission group enumeration using built-in Windows commands (`net group`, `net localgroup`) following initial access via spear-phishing.
  * Impact: Facilitated lateral movement and privilege escalation, resulting in large-scale theft of payment card data from retail and hospitality sectors.
* **Ryuk Ransomware Attacks:**
  * Attackers used BloodHound and PowerView to map Active Directory permission groups, identifying Domain Admin accounts and groups for targeted ransomware deployment.
  * Impact: Large-scale ransomware infections causing severe operational disruptions and financial losses to healthcare, government, and private-sector organizations.
* **NotPetya Malware:**
  * Leveraged built-in enumeration tools (`whoami /groups`, `net localgroup`) to identify privileged accounts and propagate rapidly across compromised networks.
  * Impact: Global disruption to multinational corporations, causing billions of dollars in damages.

These examples illustrate how attackers routinely utilize Permission Groups Discovery to enable high-impact cyberattacks, highlighting the importance of proactive detection and response strategies.
