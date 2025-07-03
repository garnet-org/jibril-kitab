---
description: Brute Force [T1110]
icon: lock
---

# Brute Force

## Information

* Name: Brute Force
* ID: T1110
* Tactics: [TA0006](../)
* Sub-Technique: [T1110.001](t1110.001.md), [T1110.002](t1110.002.md), [T1110.003](t1110.003.md), [T1110.004](t1110.004.md)

## Introduction

Brute Force is a common attack technique referenced in the MITRE ATT\&CK framework under technique ID T1110. This technique involves systematically attempting numerous username/password combinations or cryptographic keys to gain unauthorized access to systems, services, or encrypted data. Attackers leverage automated tools and scripts to quickly cycle through large sets of credentials, exploiting weak authentication mechanisms and poor password hygiene practices.

## Deep Dive Into Technique

Brute Force attacks are executed by systematically enumerating possible combinations of credentials or encryption keys until the correct one is found. Attackers typically automate this process using specialized tools or custom scripts.

Key execution methods and mechanisms include:

* **Credential Guessing**:\
  Attackers attempt common or default usernames/passwords, dictionary words, or previously leaked credentials.
* **Credential Stuffing**:\
  Attackers reuse stolen credentials from previous breaches against multiple systems or services.
* **Password Spraying**:\
  Attackers attempt a small number of common passwords across many accounts to avoid triggering account lockouts.
* **Cryptographic Key Brute Forcing**:\
  Attackers systematically attempt to guess encryption keys or hashes through exhaustive enumeration.

Common tools used in brute force attacks:

* Hydra
* Medusa
* John the Ripper
* Hashcat
* Ncrack
* Burp Suite Intruder module
* Custom scripts (Python, Bash, PowerShell)

Attackers may leverage botnets or cloud infrastructure to distribute the brute force attempts across multiple IP addresses, making detection and blocking more challenging.

## When this Technique is Usually Used

Brute Force attacks can appear at various stages of the cyber-attack lifecycle, including:

* **Initial Access**:
  * Gaining unauthorized entry into external-facing services (SSH, FTP, RDP, web applications).
  * Exploiting weak or default credentials on publicly available systems.
* **Privilege Escalation**:
  * Attempting to brute force local administrator or root passwords after initial compromise.
  * Targeting internal services or databases to escalate privileges.
* **Lateral Movement**:
  * Brute forcing credentials of other accounts on internal networks to move laterally between systems.
* **Credential Access**:
  * Cracking password hashes or encrypted data obtained from compromised systems.
  * Attempting to access password-protected files or databases.

Attackers commonly use brute force attacks when:

* Password complexity policies are weak or nonexistent.
* Multi-factor authentication (MFA) is not enforced.
* Account lockout policies are absent or improperly configured.
* Credential reuse is prevalent among users.

## How this Technique is Usually Detected

Detection of brute force attacks typically involves monitoring authentication logs, analyzing network traffic patterns, and using specialized security tools. Common detection methods and indicators include:

* **Log Analysis**:
  * Repeated failed login attempts from the same IP address or multiple IP addresses.
  * High frequency of authentication failures within short time frames.
  * Unusual login attempts at odd hours or from unexpected geographic locations.
* **Network Monitoring**:
  * Detection of anomalous traffic patterns and spikes in authentication requests.
  * Monitoring for excessive connection attempts to specific services (SSH, RDP, web login endpoints).
* **Endpoint Detection and Response (EDR)**:
  * Alerts triggered by suspicious authentication behaviors or credential access attempts.
* **Security Information and Event Management (SIEM)**:
  * Correlation rules to identify brute force attempts based on aggregated log data.
* **Intrusion Detection Systems (IDS) and Intrusion Prevention Systems (IPS)**:
  * Signature-based or behavioral detection of brute force traffic patterns.
* **Indicators of Compromise (IoCs)**:
  * Multiple failed login attempts recorded in system logs (e.g., Windows Security logs, Linux auth logs).
  * Unusual IP addresses repeatedly attempting authentication.
  * Account lockout events or sudden changes in account status.
  * Presence of brute force tools or scripts on compromised hosts.

## Why it is Important to Detect This Technique

Timely detection of brute force attacks is critical due to the significant impacts they can have on systems, networks, and organizations. Potential impacts and reasons for early detection include:

* **Unauthorized Access**:
  * Successful brute force attacks can lead to unauthorized access to sensitive data, systems, and applications.
  * Attackers gaining administrative privileges can escalate to further compromise or lateral movement.
* **Data Breaches and Exfiltration**:
  * Stolen credentials can facilitate data theft, intellectual property compromise, or exposure of sensitive information.
* **Operational Disruption**:
  * Account lockouts resulting from brute force attempts can disrupt legitimate user access and business operations.
* **Compliance and Regulatory Risks**:
  * Failure to detect brute force attacks can result in regulatory fines, legal action, and reputational damage.
* **Indicator of Larger Attack Campaigns**:
  * Brute force activity may indicate the early stages of a larger targeted attack or advanced persistent threat (APT).
* **Resource Exhaustion**:
  * High-volume brute force attacks can consume significant network bandwidth, processing power, and system resources, impacting performance and availability.

## Examples

Real-world examples demonstrating brute force attacks, tools used, and resulting impacts:

* **Mirai Botnet (2016)**:
  * Attack Scenario: Mirai malware infected IoT devices through brute forcing default credentials.
  * Tools Used: Mirai botnet malware, automated scripts targeting weak/default passwords.
  * Impacts: Massive DDoS attacks against major DNS providers and websites, causing widespread internet outages and service disruptions.
* **GitHub Account Takeover (2013)**:
  * Attack Scenario: Attackers performed brute force credential stuffing against GitHub user accounts using leaked credentials from other breaches.
  * Tools Used: Custom scripts, automated credential stuffing tools.
  * Impacts: Unauthorized access to user repositories, potential exposure of sensitive source code and intellectual property.
* **RDP Brute Force Attacks (Ongoing Campaigns)**:
  * Attack Scenario: Attackers target exposed Remote Desktop Protocol (RDP) services using automated credential guessing.
  * Tools Used: Hydra, Ncrack, custom scripts, botnets.
  * Impacts: Unauthorized remote access, ransomware deployment, lateral movement within compromised networks, data theft.
* **Credential Spraying against Cloud Services (Multiple Incidents)**:
  * Attack Scenario: Attackers use password spraying techniques against cloud-based email and collaboration services (e.g., Microsoft 365, Google Workspace).
  * Tools Used: Custom scripts, Burp Suite, credential spraying frameworks.
  * Impacts: Unauthorized access to sensitive corporate emails, data exfiltration, phishing attacks, business email compromise (BEC).
* **SSH Brute Force Attacks (Commonly Observed)**:
  * Attack Scenario: Attackers systematically attempt common username/password combinations against SSH servers.
  * Tools Used: Hydra, Medusa, automated scripts.
  * Impacts: Compromise of Linux/Unix servers, unauthorized access, installation of malware, creation of backdoors, lateral movement.

These examples underscore the broad applicability of brute force attacks across various platforms, services, and industries, highlighting the necessity of robust detection and mitigation strategies.
