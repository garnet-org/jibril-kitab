---
description: Privilege Escalation [TA0004]
icon: shield
---

# Privilege Escalation

## Information

* ID: TA0004

## Introduction

Privilege Escalation, as defined by the MITRE ATT\&CK framework, refers to techniques an attacker employs to gain higher-level permissions on a compromised system or network. Attackers initially gaining limited access privileges often seek to escalate their permissions to administrator or root-level accounts, enabling them to bypass access controls, execute unauthorized commands, access sensitive data, or establish persistence within the environment. Privilege escalation is a critical step in many cyber-attacks, significantly increasing the attacker’s control over targeted systems.

## Deep Dive Into Technique

Privilege escalation techniques can be broadly categorized into two types:

* **Vertical Privilege Escalation:** Elevating privileges from a lower-level account (e.g., standard user) to a higher-level account (e.g., administrator/root).
* **Horizontal Privilege Escalation:** Gaining access to accounts or resources at the same privilege level, typically belonging to other users.

Attackers commonly leverage vulnerabilities and misconfigurations to escalate privileges, including:

* **Exploitation of Vulnerabilities:**
  * Kernel exploits (e.g., Dirty COW, Kernel Exploits targeting Windows).
  * Vulnerable software applications (e.g., outdated versions of third-party software with known vulnerabilities).
  * Misconfigured services or daemons (e.g., services running with overly permissive privileges).
* **Credential Theft and Reuse:**
  * Capturing credentials from memory using tools like Mimikatz.
  * Extracting credentials from configuration files, scripts, or repositories.
  * Credential reuse across multiple systems or services.
* **Misuse of Legitimate Features:**
  * Abuse of sudo privileges in Unix/Linux systems.
  * Exploitation of scheduled tasks or cron jobs configured with higher privileges.
  * Manipulation of Windows services or DLL hijacking.
* **Abuse of Access Control Misconfigurations:**
  * Incorrect file permissions allowing unauthorized access or modification.
  * Misconfigured Active Directory permissions, enabling attackers to escalate privileges within domain environments.

Real-world procedures typically involve reconnaissance to identify potential privilege escalation paths, exploitation of identified vulnerabilities or misconfigurations, and finally, persistence establishment once escalated privileges are obtained.

## When this Technique is Usually Used

Privilege escalation commonly appears across multiple stages and scenarios of cyber-attacks, including:

* **Initial Compromise Stage:** After gaining initial foothold through phishing, malware execution, or exploitation of publicly exposed services, attackers escalate privileges to gain deeper system control.
* **Internal Reconnaissance Stage:** Attackers escalate privileges to access sensitive internal resources, perform lateral movement, or gather intelligence.
* **Persistence and Defense Evasion Stage:** Elevated privileges allow attackers to establish persistence mechanisms (e.g., creating hidden administrative accounts, modifying system configurations to evade detection).
* **Exfiltration Stage:** Higher privileges facilitate easy access to sensitive data, simplifying data exfiltration.

Typical attack scenarios include:

* Targeted phishing attacks leading to user-level access, followed by privilege escalation to administrator.
* Web application compromises exploiting vulnerabilities, followed by escalation to database administrative privileges.
* Insider threats escalating privileges to access sensitive corporate information or systems.

## How this Technique is Usually Detected

Detection of privilege escalation techniques involves a combination of monitoring strategies, tools, and indicators of compromise (IoCs):

* **Endpoint Detection and Response (EDR) Solutions:**
  * Monitoring suspicious process executions, privilege escalations, and abnormal access patterns.
  * Detection of known privilege escalation exploits and tools (e.g., Mimikatz, Metasploit modules).
* **Security Information and Event Management (SIEM) Solutions:**
  * Correlation of logs from operating systems, applications, and network devices to detect anomalous privilege changes.
  * Alerting on suspicious account creations, modifications, or privilege assignments.
* **File Integrity Monitoring (FIM):**
  * Detecting unauthorized modifications to critical system files, configurations, and permissions.
* **Behavioral Analytics:**
  * Identifying abnormal behaviors such as unusual login patterns, privilege escalation attempts, and atypical process executions.
* **Specific Indicators of Compromise (IoCs):**
  * Unexpected creation of privileged accounts or groups.
  * Unusual scheduled tasks or cron jobs with elevated privileges.
  * Unexpected modifications to sudoers file or Windows registry keys related to privilege escalation.
  * Detection of privilege escalation tools (e.g., PowerSploit, Empire, LinPEAS, WinPEAS scripts).
  * Evidence of exploitation attempts in system logs, such as kernel panic logs, crash dumps, or error messages related to known exploits.

## Why it is Important to Detect This Technique

Early detection of privilege escalation is crucial due to its significant impacts on systems and networks:

* **Increased Attack Surface:** Elevated privileges enable attackers to access sensitive data, critical infrastructure, and additional systems within the network.
* **Persistence and Stealth:** Attackers with escalated privileges can establish persistent footholds, making detection and remediation more challenging.
* **Data Exfiltration and Intellectual Property Theft:** Privileged access allows attackers to easily extract sensitive information, intellectual property, or personally identifiable information (PII).
* **Operational Disruption:** Attackers may leverage elevated privileges to disrupt critical services, modify configurations, or deploy ransomware.
* **Compliance and Regulatory Implications:** Failure to detect and respond promptly to privilege escalation can lead to regulatory penalties, reputational damage, and loss of customer trust.

Detecting privilege escalation early enables rapid containment and remediation, minimizes damage, reduces operational disruption, and maintains organizational security posture.

## Examples

Real-world examples showcasing privilege escalation include:

* **Dirty COW (CVE-2016-5195):**
  * Attack Scenario: Linux kernel vulnerability allowed attackers to overwrite read-only memory mappings, escalating privileges from standard user to root.
  * Tools Used: Publicly available exploit code, Metasploit modules.
  * Impact: Full administrative control over vulnerable Linux systems, leading to potential data theft, persistence establishment, and lateral movement.
* **Windows Print Spooler Vulnerability (PrintNightmare, CVE-2021-34527):**
  * Attack Scenario: Vulnerability in Windows Print Spooler service enabled authenticated users to execute arbitrary code with SYSTEM-level privileges.
  * Tools Used: Exploit scripts released publicly, Metasploit modules.
  * Impact: Complete system compromise, lateral movement within Active Directory environments, widespread ransomware deployments.
* **Mimikatz Credential Theft:**
  * Attack Scenario: Attackers use Mimikatz to extract plaintext passwords, hashes, and Kerberos tickets from memory.
  * Tools Used: Mimikatz, PowerSploit, Empire Framework.
  * Impact: Attacker gains administrative credentials, enabling lateral movement, persistence, and data exfiltration.
* **Sudo Privilege Escalation (CVE-2021-3156, Baron Samedit):**
  * Attack Scenario: Heap-based buffer overflow in sudo allowed attackers with standard privileges to escalate to root.
  * Tools Used: Publicly available exploit code, Metasploit modules.
  * Impact: Complete administrative control over Unix/Linux systems, potential for persistence, lateral movement, and sensitive data access.
* **DLL Hijacking in Windows:**
  * Attack Scenario: Attackers exploit DLL search order vulnerabilities to load malicious DLLs with higher privileges.
  * Tools Used: Custom malicious DLLs, Metasploit, custom scripts.
  * Impact: Privilege escalation, persistence establishment, stealthy lateral movement, and data exfiltration.

These examples illustrate the diverse methods attackers use to escalate privileges, highlighting the critical need for effective detection, prevention, and response strategies.
