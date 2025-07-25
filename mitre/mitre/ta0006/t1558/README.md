---
description: Steal or Forge Kerberos Tickets [T1558]
icon: key
---

# Steal or Forge Kerberos Tickets

## Information

* Name: Steal or Forge Kerberos Tickets
* ID: T1558
* Tactics: [TA0006](../)
* Sub-Technique: T1558.005, T1558.004, [T1558.001](t1558.001.md), [T1558.002](t1558.002.md), [T1558.003](t1558.003.md)

## Introduction

Stealing or forging Kerberos tickets is a common adversarial technique categorized under MITRE ATT\&CK framework as T1558.003 ("Steal or Forge Kerberos Tickets: Kerberoasting"). This technique involves attackers exploiting the Kerberos authentication protocol to obtain valid user credentials or tickets, enabling lateral movement, privilege escalation, and persistence within Active Directory environments. Attackers leverage weaknesses in Kerberos implementations or misconfigurations to impersonate legitimate users, evade detection, and maintain prolonged unauthorized access.

## Deep Dive Into Technique

Kerberos is a widely used authentication protocol designed for secure client-server communication over insecure networks. Attackers target Kerberos tickets, specifically Ticket Granting Tickets (TGT) and Service Tickets (ST), to gain unauthorized access. Common methods include:

* **Kerberoasting**:
  * Attackers request service tickets (ST) for Kerberos-enabled services registered with Service Principal Names (SPNs).
  * Extracted tickets are encrypted using the service account's password hash.
  * Offline brute-force or dictionary attacks are performed against these hashes to recover plaintext credentials.
* **Golden Ticket Attack**:
  * Attackers exploit compromised Key Distribution Center (KDC) account hashes (KRBTGT account).
  * Forged TGTs grant attackers unrestricted access to domain resources, bypassing standard authentication mechanisms.
* **Silver Ticket Attack**:
  * Attackers compromise service account hashes to forge Service Tickets (ST) directly.
  * Provides access to specific services without requiring interaction with KDC, making detection challenging.
* **Pass-the-Ticket (PtT)**:
  * Attackers steal valid Kerberos tickets from compromised systems' memory (e.g., via Mimikatz, Rubeus).
  * Stolen tickets are reused to authenticate as legitimate users without requiring plaintext credentials.

Technical mechanisms utilized by attackers include:

* Memory scraping tools (e.g., Mimikatz, Rubeus) to extract tickets from memory.
* Offline cracking tools (e.g., Hashcat, John the Ripper) for dictionary or brute-force attacks against ticket hashes.
* Manipulation of Kerberos protocol weaknesses and Active Directory misconfigurations.

## When this Technique is Usually Used

Attackers commonly use Kerberos ticket stealing and forging techniques during multiple stages of cyber-attacks, including:

* **Privilege Escalation**:
  * Attackers escalate privileges by compromising accounts with higher privileges through Kerberoasting or Golden Ticket attacks.
* **Lateral Movement**:
  * Stolen tickets enable attackers to move laterally across domain-joined systems without triggering authentication alerts.
* **Persistence**:
  * Golden or Silver tickets provide persistent access, allowing attackers to maintain long-term footholds within compromised environments.
* **Credential Access**:
  * Attackers extract credentials to further expand access or escalate privileges within the organization's infrastructure.

Typical scenarios include:

* Advanced Persistent Threat (APT) groups targeting enterprise environments.
* Internal penetration testing and red teaming engagements.
* Cybercriminals targeting financial institutions, government agencies, and large corporations.

## How this Technique is Usually Detected

Detection of stolen or forged Kerberos tickets involves a combination of monitoring, auditing, and analysis techniques, including:

* **Event Log Monitoring**:
  * Monitor Windows Security Event Logs for suspicious Kerberos-related events:
    * Event ID 4768 (Kerberos Authentication Ticket Request).
    * Event ID 4769 (Kerberos Service Ticket Request).
    * Event ID 4770 (Kerberos Service Ticket Renewal Request).
    * Event ID 4771 (Kerberos Pre-Authentication Failure).
* **Behavioral Analysis**:
  * Identify anomalous patterns in ticket requests, such as unusual user-service combinations or abnormal ticket lifetimes.
  * Detect excessive ticket requests from single sources or unusual ticket encryption types.
* **Endpoint Detection and Response (EDR)**:
  * Deploy EDR solutions capable of detecting and alerting on memory scraping tools (e.g., Mimikatz, Rubeus execution).
  * Monitor process injection, credential dumping behaviors, and unusual process execution patterns.
* **Network Traffic Analysis**:
  * Analyze network traffic for unusual Kerberos protocol behaviors or abnormal communication patterns with domain controllers.
  * Identify anomalous authentication requests or unexpected ticket renewals.
* **Indicators of Compromise (IoCs)**:
  * Presence of known credential dumping tools (e.g., Mimikatz, Rubeus) on endpoints.
  * Suspicious Kerberos ticket requests involving high-privilege accounts or critical services.
  * Detection of forged tickets with anomalous ticket properties (e.g., unusually long lifetimes, non-standard encryption types).

## Why it is Important to Detect This Technique

Timely detection of stolen or forged Kerberos tickets is crucial due to significant potential impacts, including:

* **Privilege Escalation and Domain Compromise**:
  * Attackers gaining administrative privileges can fully compromise network infrastructure, leading to catastrophic security breaches.
* **Data Exfiltration and Intellectual Property Theft**:
  * Unauthorized access allows attackers to steal sensitive information, intellectual property, customer data, or proprietary business information.
* **Persistent and Stealthy Access**:
  * Forged tickets (Golden or Silver) enable attackers to maintain stealthy, long-term persistence within compromised environments, complicating remediation efforts.
* **Reputational Damage and Regulatory Consequences**:
  * Undetected breaches can result in significant reputational harm, regulatory fines, and legal liabilities due to compromised sensitive data.
* **Operational Disruption**:
  * Attackers leveraging Kerberos tickets can disrupt business operations, causing downtime, service interruptions, and financial losses.

Early detection is vital to minimize damage, reduce attacker dwell time, and enable effective incident response and remediation activities.

## Examples

Real-world examples of Kerberos ticket stealing and forging techniques include:

* **NotPetya Malware (2017)**:
  * Utilized credential dumping tools (e.g., Mimikatz) to extract Kerberos tickets from compromised hosts.
  * Enabled lateral movement across domain-joined systems, causing widespread operational disruption and significant financial losses.
* **APT29 (Cozy Bear) Attacks**:
  * Leveraged Kerberoasting attacks to compromise Active Directory accounts.
  * Extracted service tickets to perform offline cracking, escalating privileges, and maintaining persistence within targeted environments.
* **Operation Skeleton Key (2015)**:
  * Attackers compromised domain controllers to inject malicious code, allowing universal authentication bypass via forged Kerberos tickets.
  * Enabled attackers to authenticate as any user without valid credentials, maintaining persistent access and evading detection.

Commonly used tools and frameworks:

* **Mimikatz**:
  * Widely used credential dumping tool capable of extracting Kerberos tickets from memory and forging Golden or Silver tickets.
* **Rubeus**:
  * C#-based tool designed specifically for Kerberos interaction, enabling Kerberoasting, ticket extraction, and forging attacks.
* **Impacket Suite**:
  * Python-based collection of scripts facilitating Kerberos attacks such as GetUserSPNs.py (Kerberoasting), secretsdump.py (credential extraction), and ticketer.py (Golden/Silver ticket creation).

Impacts observed from these attacks include:

* Unauthorized access to sensitive data and intellectual property.
* Extensive network compromise and lateral movement.
* Persistent attacker presence requiring extensive remediation efforts.
* Significant financial, operational, and reputational damages.
