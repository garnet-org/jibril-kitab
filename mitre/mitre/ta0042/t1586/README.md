---
description: Compromise Accounts [T1586]
icon: users
---

# Compromise Accounts

## Information

* Name: Compromise Accounts
* ID: T1586
* Tactics: [TA0042](../)
* Sub-Technique: [T1586.001](t1586.001.md), [T1586.003](t1586.003.md), [T1586.002](t1586.002.md)

## Introduction

Compromise Accounts (MITRE ATT\&CK ID: T1586) refers to the adversary's tactic of obtaining unauthorized access to legitimate user accounts or credentials to achieve persistence, escalate privileges, or facilitate lateral movement within a targeted environment. In the MITRE ATT\&CK framework, this technique falls under the "Initial Access" tactic, representing one of the most common and effective methods adversaries use to initiate and sustain their operations.

## Deep Dive Into Technique

Adversaries typically compromise accounts through various methods, each exploiting different vulnerabilities or weaknesses:

* **Credential Theft:**
  * Phishing campaigns to harvest credentials through fake login pages or malicious attachments.
  * Credential dumping from compromised endpoints, including LSASS memory extraction, SAM database dumps, or browser-stored passwords.
  * Keylogging malware or spyware installed on targeted systems.
* **Credential Reuse:**
  * Credential stuffing attacks, leveraging credentials leaked from third-party breaches to access other systems where users reused passwords.
  * Password spraying attacks, systematically testing common passwords across multiple accounts to avoid lockouts.
* **Exploitation of Weak Authentication:**
  * Exploiting default credentials or weak passwords left unchanged by users or administrators.
  * Exploiting misconfigured authentication mechanisms, including insecure APIs or authentication bypass vulnerabilities.
* **Session Hijacking:**
  * Intercepting tokens, cookies, or session identifiers through man-in-the-middle (MITM) attacks, enabling attackers to impersonate legitimate users without direct credential knowledge.
  * Stealing OAuth tokens or API keys from compromised applications or scripts.

Once adversaries gain access to compromised accounts, they typically perform actions such as:

* Accessing sensitive data or confidential information.
* Privilege escalation by leveraging legitimate user permissions.
* Deploying additional malware or persistence mechanisms.
* Lateral movement to other accounts or systems within the same environment.
* Covering tracks by performing malicious activities under legitimate user accounts, making detection and attribution difficult.

## When this Technique is Usually Used

Compromise Accounts is a versatile technique leveraged across various attack scenarios and stages:

* **Initial Access:**
  * Phishing campaigns targeting employees to obtain initial foothold credentials.
  * Credential stuffing or password spraying attacks against exposed authentication portals.
* **Persistence:**
  * Leveraging compromised accounts to maintain long-term access to the environment without deploying additional malware.
* **Privilege Escalation:**
  * Using compromised accounts with higher privileges to elevate access within the network.
* **Defense Evasion:**
  * Conducting malicious activities using legitimate user credentials to evade detection mechanisms that rely on behavioral analytics or anomaly detection.
* **Lateral Movement:**
  * Utilizing compromised accounts to pivot internally and access additional resources or sensitive data.
* **Collection and Exfiltration:**
  * Accessing sensitive data repositories or cloud storage services using compromised user credentials.

## How this Technique is Usually Detected

Detecting compromised accounts involves monitoring and analyzing multiple indicators and behaviors:

* **Behavioral Analytics and Anomaly Detection:**
  * Unusual login times or locations (geographical anomalies).
  * Multiple failed login attempts followed by successful authentication.
  * Sudden changes in user activity patterns, such as accessing unusual resources or performing abnormal actions.
* **Log Monitoring and Analysis:**
  * Reviewing authentication logs for suspicious login events, brute-force attempts, or password spraying patterns.
  * Monitoring account lockouts and resets, which may indicate credential attacks.
* **Endpoint Detection and Response (EDR) Tools:**
  * Detecting credential dumping tools or suspicious process executions (such as Mimikatz, ProcDump).
  * Identifying attempts to access or modify sensitive files related to credential storage (e.g., SAM database, LSASS process).
* **Network Traffic Analysis:**
  * Detecting unusual network connections or data transfers indicative of session hijacking or credential exfiltration.
  * Monitoring for connections to known malicious domains or command-and-control (C2) servers.
* **Multi-factor Authentication (MFA) Alerts:**
  * Receiving alerts for MFA bypass attempts or unexpected MFA prompts.

Specific Indicators of Compromise (IoCs):

* Logs showing successful logins from multiple geographic locations within short timeframes.
* Suspicious user-agent strings or IP addresses associated with known malicious activities.
* Detection of credential theft tools such as Mimikatz, BloodHound, or CrackMapExec on endpoints.
* Unexpected password resets or MFA enrollment changes.

## Why it is Important to Detect This Technique

Timely detection of compromised accounts is critical due to the severe potential impacts on organizations, including:

* **Data Breaches and Intellectual Property Theft:**
  * Unauthorized access to sensitive or confidential data, leading to potential regulatory penalties, financial loss, and reputational damage.
* **Operational Disruption:**
  * Compromised accounts can facilitate ransomware infections, denial-of-service attacks, or sabotage of critical business operations.
* **Privilege Escalation and Lateral Movement:**
  * Adversaries often leverage compromised accounts as stepping stones to escalate privileges and move laterally within the network, significantly increasing the scope and severity of attacks.
* **Compliance and Regulatory Risks:**
  * Failure to detect and respond to compromised accounts can lead to non-compliance with regulatory standards (e.g., GDPR, HIPAA), resulting in legal penalties and financial liabilities.
* **Increased Difficulty in Incident Response:**
  * Adversaries using legitimate accounts complicate attribution, analysis, and containment efforts, prolonging incident response timelines and increasing remediation costs.

Early detection enables organizations to:

* Contain and remediate incidents promptly, minimizing damage.
* Strengthen authentication mechanisms and security policies proactively.
* Enhance overall security posture and resilience against future attacks.

## Examples

Real-world examples illustrating the compromise accounts technique include:

* **Colonial Pipeline Ransomware Attack (2021):**
  * Attack Scenario: Attackers gained initial access through a compromised VPN account with a reused password leaked in a prior breach.
  * Tools Used: Credential stuffing, DarkSide ransomware.
  * Impact: Severe operational disruption, fuel shortages, and significant financial and reputational damage.
* **SolarWinds Supply Chain Attack (2020):**
  * Attack Scenario: Attackers leveraged compromised credentials and tokens to access cloud services and internal resources, maintaining persistence and lateral movement.
  * Tools Used: Sunburst malware, compromised OAuth tokens, credential theft methods.
  * Impact: Major breach affecting multiple U.S. government agencies and private organizations, leading to extensive remediation efforts.
* **Twitter Account Breach (2020):**
  * Attack Scenario: Attackers manipulated internal administrative tools by compromising employee accounts through social engineering and credential theft.
  * Tools Used: Social engineering, credential theft, internal admin tools.
  * Impact: Unauthorized posting on high-profile accounts, financial scams, reputational damage, and regulatory scrutiny.
* **Uber Data Breach (2016):**
  * Attack Scenario: Attackers accessed Uber's private GitHub repository using compromised employee credentials, stealing sensitive data.
  * Tools Used: Credential reuse, GitHub access, AWS credential compromise.
  * Impact: Exposure of personal data of millions of users and drivers, regulatory penalties, and significant reputational harm.

These examples underscore the critical importance of detecting compromised accounts promptly to prevent severe impacts and ensure organizational security.
