---
description: Adversary-in-the-Middle [T1557]
icon: lock
---

# Adversary-in-the-Middle

## Information

* Name: Adversary-in-the-Middle
* ID: T1557
* Tactics: [TA0006](../../ta0006/), [TA0009](../)
* Sub-Technique: [T1557.004](t1557.004.md), [T1557.003](t1557.003.md), [T1557.001](t1557.001.md), [T1557.002](t1557.002.md)

## Introduction

Adversary-in-the-Middle (AiTM) is a technique defined within the MITRE ATT\&CK framework (ID: T1557), categorized under the tactic "Credential Access." This attack method involves adversaries positioning themselves between two communicating parties, intercepting or manipulating the data exchanged. AiTM attacks enable adversaries to capture credentials, session tokens, sensitive information, or even modify communications without detection by either party involved.

## Deep Dive Into Technique

Adversary-in-the-Middle attacks involve intercepting legitimate network communications by placing malicious infrastructure or software between the victim and legitimate services. Adversaries achieve this through various technical methods:

* **Proxy Servers:** Attackers deploy malicious proxies that intercept and relay communications, capturing credentials or tokens in transit.
* **DNS Spoofing/Cache Poisoning:** Attackers redirect legitimate traffic to attacker-controlled infrastructure by manipulating DNS responses.
* **ARP Spoofing/Poisoning:** Attackers broadcast fraudulent ARP messages to associate their MAC address with the IP address of a legitimate host.
* **SSL/TLS Stripping:** Attackers downgrade secure HTTPS connections to insecure HTTP, enabling interception of plaintext data.
* **Rogue Wi-Fi Access Points:** Attackers set up malicious wireless access points mimicking legitimate ones to intercept wireless communications.
* **Session Hijacking:** Attackers intercept and reuse session cookies or tokens to impersonate legitimate users.
* **Phishing Websites with AiTM Proxies:** Attackers lure users to malicious websites that transparently proxy requests to legitimate services, capturing credentials and tokens.

Real-world procedures typically involve:

1. **Initial Reconnaissance:** Attackers identify targets, network infrastructure, and communication protocols.
2. **Infrastructure Setup:** Deploying malicious servers, proxies, or access points.
3. **Traffic Redirection:** Using DNS spoofing, ARP poisoning, or rogue access points to redirect victim traffic.
4. **Interception and Manipulation:** Capturing credentials, tokens, or sensitive data during transit.
5. **Credential Abuse:** Using captured credentials or tokens to access sensitive systems or data.

## When this Technique is Usually Used

Adversary-in-the-Middle attacks can appear in multiple attack scenarios and stages, including:

* **Initial Access Stage:** Capturing credentials during initial login attempts to gain unauthorized entry.
* **Credential Harvesting Campaigns:** Mass phishing campaigns leveraging AiTM proxies to collect user credentials.
* **Persistence and Privilege Escalation:** Continuously intercepting privileged user sessions to maintain access.
* **Lateral Movement:** Capturing credentials or session tokens to move across internal networks without detection.
* **Data Exfiltration Stage:** Intercepting sensitive communications or data transfers to exfiltrate information.
* **Espionage and Surveillance:** Continuously monitoring communications for intelligence gathering purposes.
* **Financial Fraud:** Intercepting financial transaction details, credentials, or tokens to conduct fraudulent transactions.

## How this Technique is Usually Detected

Detection of AiTM attacks typically involves network monitoring, traffic analysis, and endpoint security measures. Common detection methods include:

* **Network Traffic Analysis:**
  * Monitoring for abnormal DNS resolution patterns or DNS spoofing attempts.
  * Detecting unusual ARP traffic or duplicate IP-to-MAC mappings.
  * Identifying unusual SSL/TLS certificate warnings or downgrades from HTTPS to HTTP.
  * Detecting unexpected proxy servers or unusual network hops.
* **Endpoint Behavioral Analysis:**
  * Monitoring endpoint devices for unexpected certificate warnings or SSL/TLS validation errors.
  * Identifying unexpected session token reuse from different IP addresses or locations.
* **Security Tools and Solutions:**
  * Intrusion Detection/Prevention Systems (IDS/IPS) configured to detect ARP spoofing, DNS spoofing, and SSL stripping.
  * Endpoint Detection and Response (EDR) tools monitoring endpoint activities and behaviors.
  * Network Security Monitoring (NSM) solutions analyzing network traffic patterns and anomalies.
  * Security Information and Event Management (SIEM) systems aggregating and correlating logs for suspicious activity.
* **Specific Indicators of Compromise (IoCs):**
  * Multiple MAC addresses associated with a single IP address.
  * Unusual or unknown SSL/TLS certificates presented to clients.
  * Sudden or repeated SSL/TLS downgrade attempts.
  * DNS resolution anomalies or unexpected DNS server responses.
  * Presence of unauthorized or rogue wireless access points.
  * Suspicious proxy server IP addresses or domains found in network traffic logs.

## Why it is Important to Detect This Technique

Detecting AiTM attacks early is crucial due to their severe potential impacts on systems, networks, and organizations:

* **Credential Compromise:** Attackers can capture sensitive credentials, leading to unauthorized access and privilege escalation.
* **Data Breaches:** Sensitive or confidential data intercepted during transit can lead to significant data breaches.
* **Financial Losses:** Financial credentials or transaction details captured by attackers can lead to direct financial theft or fraud.
* **Operational Disruption:** Interception or manipulation of communications may disrupt critical business operations and services.
* **Reputation Damage:** Data breaches or unauthorized access incidents can severely damage organizational reputation and customer trust.
* **Regulatory and Compliance Issues:** Failure to detect and mitigate AiTM attacks can result in regulatory fines, penalties, or legal consequences.
* **Persistent Threats:** Undetected AiTM attacks can enable persistent attacker presence within networks, complicating incident response and recovery efforts.

Early detection enables rapid response, containment, and mitigation, significantly reducing the potential damage and long-term impacts.

## Examples

Real-world examples illustrating AiTM attacks, scenarios, tools used, and impacts include:

* **Evilginx2 Phishing Proxy Attacks (2022):**
  * **Attack Scenario:** Attackers used Evilginx2, an AiTM phishing toolkit, to intercept credentials and session tokens targeting Microsoft 365 accounts.
  * **Tools Used:** Evilginx2 phishing proxy, malicious web infrastructure.
  * **Impact:** Attackers successfully bypassed multi-factor authentication (MFA), capturing session cookies and gaining unauthorized access to sensitive email accounts and corporate resources.
* **Operation Emmental (2014):**
  * **Attack Scenario:** Cybercriminals targeted European banking customers using AiTM attacks, intercepting mobile banking authentication codes.
  * **Tools Used:** Malicious DNS servers, rogue SSL certificates, phishing emails, malicious mobile apps.
  * **Impact:** Attackers successfully bypassed two-factor authentication (2FA) systems, resulting in financial losses and compromised banking credentials.
* **Retefe Banking Trojan (2015–2018):**
  * **Attack Scenario:** Attackers redirected victims' banking traffic to malicious proxy servers using DNS hijacking.
  * **Tools Used:** Retefe malware, DNS manipulation, rogue SSL certificates.
  * **Impact:** Attackers intercepted online banking credentials, leading to unauthorized financial transactions and significant monetary losses for victims.
* **Wi-Fi Pineapple Rogue Access Point Attacks:**
  * **Attack Scenario:** Attackers deployed Wi-Fi Pineapple devices as rogue access points to intercept wireless communications in public or corporate environments.
  * **Tools Used:** Wi-Fi Pineapple hardware, rogue wireless infrastructure.
  * **Impact:** Attackers captured sensitive information, credentials, and session tokens from unsuspecting users, enabling unauthorized access to corporate networks and personal accounts.

These examples highlight the diverse methods adversaries use to execute AiTM attacks, emphasizing the importance of robust detection, prevention, and mitigation strategies.
