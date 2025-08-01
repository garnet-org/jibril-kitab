---
description: Subvert Trust Controls [T1553]
icon: lock
---

# Subvert Trust Controls

## Information

* Name: Subvert Trust Controls
* ID: T1553
* Tactics: [TA0005](../)
* Sub-Technique: [T1553.001](t1553.001.md), [T1553.002](t1553.002.md), [T1553.003](t1553.003.md), T1553.006, [T1553.005](t1553.005.md), [T1553.004](t1553.004.md)

## Introduction

"Subvert Trust Controls" (T1553) is a technique identified by the MITRE ATT\&CK framework that attackers leverage to undermine mechanisms of trust within systems and networks. This technique involves manipulating or abusing trust relationships, certificates, security tokens, or authentication mechanisms to gain unauthorized access, escalate privileges, maintain persistence, or evade detection. By subverting trust controls, attackers can significantly increase the effectiveness and stealth of their intrusion campaigns, often bypassing traditional security defenses and detection mechanisms.

## Deep Dive Into Technique

Subverting trust controls involves compromising or abusing the trust mechanisms that systems and applications rely upon, including digital certificates, security tokens, authentication protocols, and identity management systems. Attackers typically exploit trust relationships established between systems or entities to bypass security boundaries and gain unauthorized privileges.

Common execution methods include:

* **Certificate Manipulation and Abuse:**
  * Attackers steal or forge digital certificates to impersonate legitimate entities.
  * Compromise or misuse certificate authorities (CAs) to issue fraudulent certificates.
  * Deploy self-signed or malicious certificates to bypass secure communication checks.
* **Kerberos Ticket Manipulation (e.g., Golden Ticket, Silver Ticket attacks):**
  * Attackers compromise Kerberos authentication by forging tickets to gain persistent access.
  * Golden Ticket attacks involve compromising the Kerberos Ticket Granting Ticket (TGT) by stealing the KRBTGT hash.
  * Silver Ticket attacks involve forging service tickets using compromised service account passwords or hashes.
* **Abuse of Security Assertion Markup Language (SAML) Tokens:**
  * Attackers exploit SAML assertions to authenticate as legitimate users, bypass multi-factor authentication (MFA), and access sensitive resources.
  * Manipulation of SAML tokens through compromised identity providers or malicious token issuance.
* **Domain Trust Exploitation:**
  * Attackers exploit trust relationships between Active Directory (AD) domains or forests to escalate privileges and move laterally.
  * Abuse of implicit or explicit domain trusts to access resources in trusted domains.
* **Code Signing Abuse:**
  * Attackers sign malicious software with stolen or fraudulently obtained code-signing certificates to evade security software and bypass execution controls.

Real-world attacker procedures typically involve:

* Credential theft and reuse.
* Compromising trusted third-party vendors or managed service providers (MSPs).
* Exploiting weak or misconfigured trust relationships.
* Leveraging stolen cryptographic material (keys, certificates, tokens).

## When this Technique is Usually Used

Attackers utilize the subversion of trust controls across multiple stages of the cyber kill chain, including:

* **Initial Access:**
  * Leveraging compromised certificates or tokens to bypass authentication mechanisms and gain initial entry.
  * Exploiting trusted third-party relationships or vendor access to infiltrate victim networks.
* **Execution and Persistence:**
  * Using forged certificates or authentication tokens to execute malicious code persistently without detection.
  * Establishing persistent backdoors by abusing trust mechanisms (e.g., Kerberos Golden Tickets).
* **Privilege Escalation and Credential Access:**
  * Leveraging compromised trust mechanisms to escalate privileges within the domain or across trusted domains.
  * Manipulating trust relationships to access sensitive credentials and authentication material.
* **Defense Evasion:**
  * Evading detection by signing malicious payloads with trusted certificates.
  * Using legitimate authentication methods (e.g., SAML tokens, Kerberos tickets) to blend in with normal traffic.
* **Lateral Movement:**
  * Exploiting domain trust relationships to spread laterally across networks and domains.
  * Abusing single sign-on (SSO) mechanisms to pivot between interconnected systems.

## How this Technique is Usually Detected

Detection of subverted trust controls requires a combination of monitoring, anomaly detection, and proactive security measures:

* **Certificate and Token Monitoring:**
  * Monitor certificate issuance, usage, and revocation events.
  * Detect unexpected or unauthorized certificate authorities (CAs) and self-signed certificates.
  * Track anomalous or unauthorized use of SAML tokens or Kerberos tickets.
* **Kerberos Authentication Monitoring:**
  * Monitor and analyze Kerberos logs for unusual ticket-granting ticket (TGT) requests and service ticket issuance.
  * Detect anomalous Kerberos ticket lifetimes, encryption types, or unusual user/service combinations indicative of Golden or Silver Ticket attacks.
* **Domain Trust Relationship Auditing:**
  * Regularly audit Active Directory trust relationships for unauthorized or unexpected changes.
  * Monitor cross-domain authentication attempts and access patterns.
* **Behavioral Analytics and Anomaly Detection:**
  * Deploy User and Entity Behavior Analytics (UEBA) solutions to detect abnormal authentication patterns or unusual access behaviors.
  * Identify anomalies in authentication timing, location, frequency, or methods.
* **Endpoint and Network Security Tools:**
  * Utilize endpoint detection and response (EDR) tools to detect maliciously signed binaries or unusual certificate usage.
  * Network Intrusion Detection Systems (NIDS) and Intrusion Prevention Systems (IPS) to identify suspicious authentication traffic patterns.

Indicators of Compromise (IoCs) include:

* Unexpected or unauthorized certificates or certificate authorities.
* Presence of forged SAML tokens or Kerberos tickets.
* Unusual Active Directory trust relationships or modifications.
* Suspicious authentication events originating from unusual sources or times.
* Malicious binaries signed with stolen or revoked certificates.

## Why it is Important to Detect This Technique

Early detection of subverted trust controls is crucial because of the substantial risks and impacts on organizations, including:

* **Privilege Escalation and Unauthorized Access:**
  * Attackers can rapidly escalate privileges, gaining administrative or system-level access to sensitive resources.
* **Persistence and Long-term Compromise:**
  * Compromised trust mechanisms enable attackers to maintain persistent, stealthy footholds within victim environments, complicating remediation efforts.
* **Evasion of Security Controls:**
  * Attackers bypass traditional security measures (e.g., antivirus, firewall, authentication controls) by leveraging trusted certificates or tokens.
* **Data Exfiltration and Intellectual Property Theft:**
  * Compromised trust controls facilitate unauthorized access to sensitive data, enabling attackers to exfiltrate intellectual property, trade secrets, or personally identifiable information (PII).
* **Operational Disruption and Reputational Damage:**
  * Successful attacks leveraging trust subversion can lead to significant operational disruptions, regulatory penalties, compliance violations, and severe reputational harm.
* **Propagation and Lateral Movement:**
  * Exploited trust relationships enable attackers to move laterally across interconnected systems, domains, and networks, expanding the scope and severity of an incident.

## Examples

Real-world examples of attacks involving subverted trust controls include:

* **SolarWinds Supply Chain Attack (2020):**
  * Attackers compromised SolarWinds' software build environment, embedding malicious code into legitimate software updates.
  * Malicious updates were digitally signed with SolarWinds' legitimate certificates, bypassing security controls and detection mechanisms.
  * Impacted numerous government agencies and private organizations, leading to extensive data breaches and espionage.
* **Operation ShadowHammer (ASUS Live Update Attack, 2019):**
  * Attackers compromised ASUS's software update infrastructure, distributing malware signed with ASUS's legitimate digital certificates.
  * Malicious updates installed backdoors on thousands of customer devices, evading antivirus detection and security controls.
* **NotPetya Ransomware (2017):**
  * Attackers leveraged compromised Ukrainian accounting software (M.E.Doc) to distribute malware signed with legitimate certificates.
  * Malware rapidly propagated across networks and domains using compromised trust relationships and credential theft, causing widespread disruption and financial damage.
* **Golden Ticket Attack (Kerberos):**
  * Attackers compromised Active Directory domain controllers, extracting the KRBTGT account hash.
  * Forged Kerberos Golden Tickets allowed persistent, stealthy, and privileged access within victim networks, bypassing authentication controls.
* **APT29 (Cozy Bear) Abuse of SAML Tokens:**
  * Attackers compromised identity providers to forge SAML authentication tokens, bypassing MFA and gaining unauthorized access to cloud resources.
  * Enabled persistent access and lateral movement within targeted organizations' cloud environments.

These examples highlight the critical importance of detecting and mitigating the subversion of trust controls to prevent substantial security breaches, operational disruptions, and financial losses.
