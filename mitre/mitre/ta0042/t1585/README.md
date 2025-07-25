---
description: Establish Accounts [T1585]
icon: users
---

# Establish Accounts

## Information

* Name: Establish Accounts
* ID: T1585
* Tactics: [TA0042](../)
* Sub-Technique: [T1585.002](t1585.002.md), [T1585.003](t1585.003.md), [T1585.001](t1585.001.md)

## Introduction

Establish Accounts (MITRE ATT\&CK ID: T1136) is a persistence technique used by adversaries to maintain long-term access to compromised systems or networks. Attackers create or manipulate user accounts, including local, domain, cloud, or application-specific accounts, to ensure continued access even if initial entry points are discovered and mitigated. Establishing accounts allows attackers to blend into normal administrative activities, evade detection, and maintain stealthy, persistent control over targeted environments.

## Deep Dive Into Technique

Adversaries typically establish accounts through several mechanisms, exploiting existing administrative privileges or vulnerabilities to remain persistent. Technical details include:

* **Local Account Creation:**
  * Attackers use system utilities such as `net user`, `useradd`, or PowerShell cmdlets (`New-LocalUser`) to create local accounts.
  * Local accounts are often assigned administrative privileges to ensure maximum control over the compromised host.
* **Domain Account Creation:**
  * Attackers leverage Active Directory administrative tools (`net user /domain`, PowerShell Active Directory module, `dsadd`) to create domain-level accounts.
  * Such accounts provide lateral movement capabilities across multiple hosts and facilitate privilege escalation.
* **Cloud Account Creation:**
  * Attackers establish cloud accounts (AWS IAM users, Azure AD accounts, GCP accounts) to maintain persistence in cloud environments.
  * They exploit compromised cloud credentials or misconfigured identity management policies to create or modify accounts.
* **Application-specific Accounts:**
  * Attackers create or modify accounts within applications (databases, web applications, CMS platforms) to maintain persistent access at the application layer.
  * Common methods include SQL injection, API abuse, or exploiting weak application authentication mechanisms.
* **Modification of Existing Accounts:**
  * Attackers modify privileges, passwords, or access rights of existing legitimate accounts to maintain stealthy persistence.
  * Techniques include password resets, privilege escalation, and manipulation of account lockout policies.

## When this Technique is Usually Used

The Establish Accounts technique is frequently deployed during various stages and scenarios of cyberattacks, including:

* **Persistence Phase:** Attackers commonly establish accounts immediately after initial compromise to ensure ongoing access.
* **Privilege Escalation:** Attackers create accounts with elevated privileges to facilitate lateral movement and deeper network penetration.
* **Maintaining Redundancy:** Multiple accounts are often created or modified to provide backup access if primary accounts are detected and disabled.
* **Long-term Espionage Campaigns:** Nation-state actors use established accounts for long-term surveillance, allowing subtle, continuous access to sensitive data.
* **Ransomware Attacks:** Attackers establish accounts to facilitate deployment and management of ransomware payloads across victim networks.
* **Insider Threat Scenarios:** Malicious insiders or compromised insiders may create hidden accounts to maintain covert access after employment termination or revocation of privileges.

## How this Technique is Usually Detected

Detection of unauthorized account establishment involves combining proactive monitoring, log analysis, and security tooling:

* **Log Analysis:**
  * Monitor system event logs (Windows Event IDs: 4720, 4726, 4732, 4756) for unusual account creation or modification.
  * Analyze Linux `/var/log/auth.log`, `/var/log/secure`, and cloud audit logs (AWS CloudTrail, Azure AD Audit Logs) for suspicious activities.
* **Behavioral Analytics:**
  * Implement user behavior analytics (UBA) tools to detect anomalous account creation activities or privilege modifications.
  * Utilize SIEM platforms (Splunk, ELK Stack, QRadar) to correlate account creation events with other suspicious behaviors.
* **Endpoint Detection and Response (EDR):**
  * Deploy EDR solutions (CrowdStrike, Microsoft Defender ATP, SentinelOne) to detect unauthorized account creations or modifications in real-time.
  * EDR tools can flag suspicious command execution related to account management utilities and scripts.
* **Indicators of Compromise (IoCs):**
  * Unusual local or domain account names (randomized or suspicious naming conventions).
  * Accounts created at abnormal times (after-hours, weekends) or from unusual locations/IP addresses.
  * Accounts with sudden privilege escalations or modifications without corresponding change requests or documentation.
  * Presence of unauthorized cloud accounts or API keys not associated with legitimate users or services.

## Why it is Important to Detect This Technique

Detecting unauthorized account establishment early is critical due to the severe potential impacts on organizational security and operations:

* **Persistent Access:** Undetected accounts allow attackers long-term, stealthy access to sensitive information, increasing risk exposure.
* **Privilege Escalation and Lateral Movement:** Attackers often leverage established accounts to escalate privileges and move laterally, significantly expanding the scope and severity of the intrusion.
* **Data Exfiltration Risks:** Persistent access through established accounts facilitates prolonged data theft activities, leading to significant data breaches, regulatory fines, and reputational damage.
* **Operational Disruption:** Attackers with persistent accounts can deploy ransomware, sabotage critical systems, or disrupt business operations, causing downtime and financial losses.
* **Difficulty in Incident Remediation:** Undetected accounts complicate incident response efforts, as attackers can regain access even after initial remediation steps, prolonging the incident lifecycle and increasing recovery costs.

## Examples

Real-world examples illustrate how attackers leverage account establishment techniques in actual cyberattacks:

* **APT29 (Cozy Bear) Campaigns:**
  * Attackers created domain accounts with administrative privileges after initial compromise, allowing persistent access to sensitive government networks.
  * Tools used included PowerShell scripts and native Windows utilities (`net user` and `net group` commands).
  * Impact included long-term espionage, theft of sensitive diplomatic communications, and difficulty in full remediation.
* **SolarWinds Supply Chain Attack (SUNBURST):**
  * Attackers established multiple privileged accounts within victim networks, leveraging compromised SolarWinds Orion platform updates.
  * Created new accounts and manipulated existing ones to maintain persistent, stealthy access.
  * Impact included widespread espionage activity affecting numerous public and private sector organizations globally.
* **Cloud Hopper (APT10) Attacks:**
  * Attackers created cloud and domain accounts within managed service providers (MSPs) to maintain persistent access and lateral movement capabilities.
  * Tools included custom scripts, PowerShell commands, and cloud management consoles.
  * Impact involved extensive data theft, intellectual property compromise, and long-term espionage against global organizations.
* **FIN7 Financially Motivated Attacks:**
  * Attackers established local administrator accounts on compromised point-of-sale (POS) systems to maintain persistent access and facilitate financial fraud.
  * Tools used included native Windows utilities and custom malware scripts.
  * Impact included significant financial losses, theft of payment card data, and prolonged unauthorized access to victim networks.
