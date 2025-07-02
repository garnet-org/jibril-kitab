---
description: Use Alternate Authentication Material [T1550]
icon: key
---

# Use Alternate Authentication Material

## Information

* Name: Use Alternate Authentication Material
* ID: T1550
* Tactics: [TA0005](../), [TA0008](../../ta0008/)
* Sub-Technique: [T1550.003](t1550.003.md), [T1550.004](t1550.004.md), [T1550.002](t1550.002.md), [T1550.001](t1550.001.md)

## Introduction

The "Use Alternate Authentication Material" technique (T1550) in the MITRE ATT\&CK framework refers to adversaries leveraging stolen or forged authentication credentials or tokens, rather than traditional username and password combinations. Attackers may use alternate authentication mechanisms such as pass-the-hash (PtH), pass-the-ticket (PtT), or forged web session cookies to authenticate to services and resources. This technique bypasses standard authentication processes and often evades detection methods that rely solely on monitoring traditional credential usage.

## Deep Dive Into Technique

This technique involves attackers utilizing alternate authentication materials to gain access to systems, services, or resources without needing clear-text passwords. Common execution methods and mechanisms include:

* **Pass-the-Hash (PtH)**:
  * Attackers use hashed credentials (NTLM hashes) to authenticate without knowing the plaintext password.
  * Typically exploited in Windows environments, especially Active Directory infrastructures.
  * Tools frequently used include Mimikatz, Impacket, Metasploit's psexec module, and CrackMapExec.
* **Pass-the-Ticket (PtT)**:
  * Attackers steal Kerberos tickets from compromised systems and reuse them to authenticate to other resources within the domain.
  * Commonly leveraged in Windows domain environments where Kerberos authentication is widely used.
  * Mimikatz, Rubeus, and Impacket are well-known tools for executing PtT attacks.
* **Overpass-the-Hash (Pass-the-Key)**:
  * Attackers leverage NTLM hashes to request Kerberos tickets, enabling lateral movement across Kerberos-protected resources.
  * Tools such as Mimikatz and Rubeus facilitate this method.
* **Forged Web Session Cookies or Tokens**:
  * Attackers steal or forge session cookies or tokens to impersonate legitimate users in web-based applications.
  * Commonly observed in web application attacks, leveraging XSS or session hijacking techniques.
  * Tools and scripts to automate cookie theft and replay include Burp Suite, Cookie Cadger, and browser extensions.
* **Golden Ticket and Silver Ticket Attacks**:
  * Attackers forge Kerberos Ticket Granting Tickets (TGTs) or service tickets by compromising domain controllers or service accounts.
  * Golden Ticket attacks involve compromised KRBTGT accounts, while Silver Ticket attacks target service account credentials.
  * Mimikatz and Impacket are primary tools for conducting these attacks.

## When this Technique is Usually Used

Adversaries commonly utilize alternate authentication material in various attack scenarios and stages, including:

* **Credential Access and Privilege Escalation**:
  * After initial compromise, attackers extract hashes or tickets to escalate privileges and access high-value resources.
* **Lateral Movement**:
  * Attackers use stolen hashes or Kerberos tickets to move laterally across network resources without triggering traditional authentication alerts.
* **Persistence**:
  * Attackers maintain persistent access by leveraging forged authentication materials, allowing continued access even after passwords are changed.
* **Defense Evasion**:
  * Alternate authentication methods bypass standard password-based monitoring, making detection more challenging.
* **Command-and-Control (C2) Operations**:
  * Attackers may use forged web tokens or session cookies to access web-based administrative consoles or cloud resources, facilitating covert C2 channels.

## How this Technique is Usually Detected

Detection of alternate authentication material usage typically involves a combination of monitoring, logging, and alerting mechanisms. Key detection methods include:

* **Event Log Monitoring**:
  * Monitor Windows Security Event Logs (Event IDs 4624, 4768, 4769, 4776) for unusual authentication patterns or anomalies.
  * Analyze Kerberos ticket-related events for anomalies, such as unusual ticket lifetimes or ticket requests from unexpected hosts.
* **Endpoint Detection and Response (EDR)**:
  * Utilize EDR solutions that detect credential dumping tools (e.g., Mimikatz) and anomalous credential usage patterns.
  * Look for suspicious process behavior or command-line arguments indicative of credential theft or ticket forgery.
* **Network Traffic Analysis**:
  * Inspect network traffic for unusual authentication requests, such as Kerberos ticket requests from unexpected systems or NTLM authentication anomalies.
  * Identify anomalous SMB, RPC, or Kerberos protocol traffic indicative of PtH or PtT attacks.
* **Behavioral Analytics and SIEM Solutions**:
  * Implement behavioral analytics to detect abnormal user authentication behavior, such as simultaneous logins from geographically dispersed locations or unusual access patterns.
  * SIEM platforms can correlate logs and network data to identify authentication anomalies.
* **Indicators of Compromise (IoCs)**:
  * Presence of known credential theft tools (e.g., Mimikatz, Rubeus, Impacket scripts).
  * Unusual authentication events, such as successful logins without preceding failed attempts.
  * Kerberos tickets with unusually long lifetimes or unusual encryption types.
  * Suspicious logins from unexpected systems or IP addresses.

## Why it is Important to Detect This Technique

Early detection of alternate authentication material usage is critical due to its potentially severe impacts on systems and networks, including:

* **Privilege Escalation and Domain Compromise**:
  * Attackers leveraging this technique often escalate privileges rapidly, gaining administrative or domain-level access.
* **Lateral Movement and Network-Wide Compromise**:
  * Using alternate authentication materials enables attackers to move laterally undetected, increasing the scope and damage of breaches.
* **Persistence and Long-Term Access**:
  * Attackers can maintain persistent access through forged tickets or hashes, even after password resets, complicating incident response and remediation.
* **Data Exfiltration and Sensitive Information Theft**:
  * With elevated privileges, attackers can access sensitive data, intellectual property, or confidential information, leading to significant financial, legal, and reputational damage.
* **Operational Disruption and Downtime**:
  * Compromise of critical systems and services can result in operational disruptions, downtime, and significant recovery costs.
* **Regulatory and Compliance Risks**:
  * Failure to detect and respond to such attacks timely can result in regulatory scrutiny, fines, and compliance violations.

## Examples

Real-world examples of attacks leveraging alternate authentication material include:

* **NotPetya Attack (2017)**:
  * Attackers utilized credential theft and pass-the-hash techniques to propagate rapidly within compromised networks.
  * Tools used included Mimikatz and custom scripts to extract and reuse hashed credentials, facilitating lateral movement.
  * Impact included widespread disruption, operational downtime, and estimated damages exceeding billions of dollars globally.
* **Operation Wocao (2019)**:
  * Attackers employed pass-the-hash and pass-the-ticket techniques extensively to move laterally within targeted networks.
  * Utilized Mimikatz and Impacket scripts to extract and reuse authentication hashes and Kerberos tickets.
  * Resulted in prolonged espionage activities, data theft, and persistent compromise of multiple organizations.
* **APT29 (Cozy Bear) Operations**:
  * Frequently leveraged forged Kerberos tickets (Golden and Silver tickets) and pass-the-ticket attacks to maintain persistent, stealthy access.
  * Tools used included Mimikatz, Rubeus, and custom-developed malware to extract and reuse authentication tickets.
  * Enabled long-term espionage, data exfiltration, and persistent compromise of governmental and private sector targets.
* **Cloud Hopper Campaign (APT10)**:
  * Attackers stole and reused web-based authentication tokens and session cookies to gain persistent access to cloud services and managed service providers (MSPs).
  * Tools such as customized scripts, Burp Suite, and Cookie Cadger facilitated token theft and reuse.
  * Impact included extensive espionage, data theft, and persistent compromise of cloud infrastructure and customer environments.
* **SolarWinds Supply Chain Attack (2020)**:
  * Attackers utilized forged SAML tokens and stolen authentication material to access cloud-based resources and email platforms.
  * Techniques included stealing and replaying authentication tokens, bypassing multi-factor authentication (MFA).
  * Resulted in significant espionage activities, data exfiltration, and widespread compromise of U.S. government agencies and private sector organizations.
