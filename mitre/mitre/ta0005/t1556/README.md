---
description: Modify Authentication Process [T1556]
icon: key
---

# Modify Authentication Process

## Information

* Name: Modify Authentication Process
* ID: T1556
* Tactics: [TA0006](../../ta0006/), [TA0005](../), [TA0003](../../ta0003/)
* Sub-Technique: [T1556.003](t1556.003.md), [T1556.002](t1556.002.md), [T1556.007](t1556.007.md), [T1556.008](t1556.008.md), [T1556.006](t1556.006.md), [T1556.009](t1556.009.md), [T1556.001](t1556.001.md), [T1556.005](t1556.005.md), [T1556.004](t1556.004.md)

## Introduction

Modify Authentication Process (T1556) is a technique classified within the MITRE ATT\&CK framework under the Credential Access tactic. Attackers employing this technique manipulate authentication mechanisms to bypass standard security controls, enabling unauthorized access to systems and networks. By altering or injecting malicious code into authentication processes, adversaries can evade detection, maintain persistence, and escalate privileges within compromised environments.

## Deep Dive Into Technique

Attackers utilize various methods to alter or manipulate authentication processes, including:

* **Pluggable Authentication Modules (PAM) Modification:**
  * Attackers modify PAM configuration files or modules on Linux/Unix systems to intercept authentication credentials or grant unauthorized access.
  * Malicious modules may log credentials, bypass authentication entirely, or provide backdoor access.
* **Windows Authentication Package Manipulation:**
  * On Windows systems, adversaries may alter authentication packages such as Security Support Provider (SSP) or Graphical Identification and Authentication (GINA) DLLs.
  * Malicious SSP DLLs can capture plaintext credentials or bypass authentication controls.
* **Kerberos Authentication Manipulation:**
  * Attackers target Kerberos authentication processes by modifying ticket-granting procedures, forging tickets, or downgrading encryption standards.
  * Golden Ticket attacks involve forging Kerberos Ticket Granting Tickets (TGTs) using compromised credentials or key material.
* **Multifactor Authentication (MFA) Bypass:**
  * Adversaries intercept, modify, or disable multifactor authentication mechanisms to circumvent enhanced security measures.
  * Techniques include session token theft, MFA prompt bombing, or modification of authentication workflows.
* **Web Application Authentication Manipulation:**
  * Attackers alter web authentication mechanisms by tampering with session management, cookies, tokens, or OAuth flows.
  * Methods include token replay attacks, session fixation, and JWT token manipulation.

## When this Technique is Usually Used

Attackers typically leverage the Modify Authentication Process technique in various scenarios and stages of cyber-attacks, including:

* **Credential Access and Privilege Escalation:**
  * After initial access, attackers modify authentication processes to capture additional credentials or escalate privileges within the compromised system.
* **Persistence:**
  * Modification of authentication components allows adversaries to maintain persistent access even after system restarts, patching, or credential resets.
* **Lateral Movement:**
  * Attackers exploit altered authentication mechanisms to move laterally across networks, accessing additional resources and systems without triggering alerts.
* **Defense Evasion:**
  * Manipulating authentication processes enables attackers to evade detection by bypassing standard monitoring tools, logging mechanisms, or security controls.
* **Initial Access via Web Applications:**
  * Attackers targeting web applications alter authentication workflows to gain unauthorized initial access or escalate privileges within web-based platforms.

## How this Technique is Usually Detected

Detection of Modify Authentication Process technique involves multiple monitoring methods, tools, and indicators of compromise (IoCs):

* **File Integrity Monitoring (FIM):**
  * Detect unauthorized changes to critical authentication files (e.g., PAM modules, SSP DLLs, Kerberos configuration files).
  * Tools: Tripwire, OSSEC, auditd, and built-in system integrity monitoring.
* **Log Monitoring and Analysis:**
  * Analyze authentication logs and system event logs for anomalies or unauthorized access attempts.
  * Tools: Splunk, ELK Stack, Graylog, and Windows Event Viewer.
* **Endpoint Detection and Response (EDR) Solutions:**
  * Monitor endpoints for unusual DLL loading, suspicious authentication module behaviors, or unauthorized modifications.
  * Tools: CrowdStrike Falcon, Carbon Black, Microsoft Defender for Endpoint.
* **Behavioral Analytics and Anomaly Detection:**
  * Identify abnormal authentication patterns, unusual login locations, unexpected privilege escalations, or MFA bypass attempts.
  * Tools: User and Entity Behavior Analytics (UEBA), SIEM platforms with anomaly detection capabilities.
* **Indicators of Compromise (IoCs):**
  * Unexpected changes or additions to PAM configuration files (`/etc/pam.d/`).
  * Suspicious DLLs loaded into LSASS process on Windows.
  * Unusual Kerberos ticket requests or encryption downgrades.
  * Unauthorized OAuth tokens, JWT tokens with abnormal claims, or session fixation attempts.

## Why it is Important to Detect This Technique

Early detection of Modify Authentication Process technique is critical due to its severe potential impacts on systems and networks:

* **Credential Compromise:**
  * Attackers gain access to user credentials, enabling further exploitation, lateral movement, and privilege escalation.
* **Persistence and Long-term Access:**
  * Manipulating authentication mechanisms allows attackers to maintain persistent, stealthy access, complicating remediation and increasing dwell time.
* **Privilege Escalation:**
  * Unauthorized modifications facilitate privilege escalation, allowing attackers administrative control over critical systems and resources.
* **Loss of Confidentiality and Integrity:**
  * Unauthorized access through compromised authentication processes can lead to data breaches, exposure of sensitive information, and unauthorized modifications or destruction of data.
* **Compliance and Regulatory Impact:**
  * Failure to detect and respond to authentication manipulation can result in regulatory non-compliance, legal penalties, and reputational damage.
* **Operational Disruption:**
  * Attackers leveraging authentication modifications may disrupt critical business operations, causing downtime, financial losses, and operational inefficiencies.

## Examples

Real-world examples of Modify Authentication Process technique include:

* **Linux PAM Backdoor (Operation Windigo):**
  * Attackers compromised Linux servers by installing malicious PAM modules, capturing credentials, and granting unauthorized access.
  * Impact: Thousands of servers compromised, credentials stolen, and persistent access maintained.
* **Windows SSP DLL Manipulation (Mimikatz SSP):**
  * Attackers utilized Mimikatz to inject malicious SSP DLLs into Windows LSASS processes, capturing plaintext credentials during authentication.
  * Impact: Credential compromise, lateral movement, and privilege escalation across enterprise networks.
* **Kerberos Golden Ticket Attacks (APT29, FIN7):**
  * Advanced Persistent Threat (APT) groups used Golden Ticket attacks to forge Kerberos tickets, enabling persistent administrative access to Active Directory environments.
  * Impact: Long-term, stealthy persistence, full domain compromise, and extensive lateral movement.
* **MFA Bypass (Lapsus$ Group Attacks):**
  * Attackers employed MFA prompt bombing and session token theft to bypass multifactor authentication mechanisms, compromising organizations including Microsoft and Okta.
  * Impact: High-profile breaches, sensitive data exposure, and significant reputational damage.
* **JWT Token Manipulation (Auth0 Vulnerability Exploit):**
  * Attackers exploited vulnerabilities in JWT token handling, modifying token claims to escalate privileges and access protected resources.
  * Impact: Unauthorized access to sensitive web application data, privilege escalation, and potential data breaches.
