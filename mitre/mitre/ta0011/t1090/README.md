---
description: Proxy [T1090]
icon: filter
---

# Proxy

## Information

* Name: Proxy
* ID: T1090
* Tactics: [TA0011](../)
* Sub-Technique: [T1090.002](t1090.002.md), [T1090.003](t1090.003.md), [T1090.004](t1090.004.md), [T1090.001](t1090.001.md)

## Introduction

Proxy is a technique defined in the MITRE ATT\&CK framework under tactic T1090, categorized under "Command and Control" (C2). Attackers utilize proxy techniques to obfuscate their origin, mask their network traffic, bypass network defenses, and maintain anonymity during malicious activities. By leveraging proxies, adversaries route communications through intermediary systems, complicating attribution and detection efforts.

## Deep Dive Into Technique

Proxy techniques involve routing network traffic through intermediate servers or systems to obscure the actual source of malicious activity. Attackers commonly employ several proxy types:

* **HTTP/S Proxy:**
  * Attackers route command-and-control traffic through standard HTTP or HTTPS proxies, blending malicious traffic with legitimate web traffic.
  * Can utilize public proxies or compromised web servers as intermediaries.
  * Often includes encrypted communications (HTTPS) to evade deep packet inspection (DPI).
* **SOCKS Proxy:**
  * A more versatile proxy protocol that can handle various types of network traffic beyond HTTP/HTTPS.
  * Attackers use SOCKS proxies to route traffic from compromised internal hosts to external command-and-control servers, bypassing firewall restrictions.
* **Reverse Proxy:**
  * Attackers set up servers that forward requests from infected hosts to backend command-and-control servers, hiding the true location of the attacker infrastructure.
  * Commonly employed with web-based malware and C2 frameworks like Cobalt Strike or Metasploit.
* **VPN Services and Anonymity Networks:**
  * Attackers may utilize commercial VPN services, Tor networks, or other anonymity services to mask their IP addresses and origins.
  * These services add multiple layers of encryption and routing, significantly complicating attribution efforts.

Real-world procedures typically involve the attacker deploying malware configured with proxy-aware capabilities or manually configuring compromised hosts to route traffic through attacker-controlled proxies.

## When this Technique is Usually Used

Attackers employ proxy techniques throughout various stages of the cyber attack lifecycle, including:

* **Initial Access and Reconnaissance:**
  * Masking attacker IP addresses when scanning and enumerating targeted networks.
  * Avoiding detection by intrusion detection systems (IDS) or intrusion prevention systems (IPS).
* **Command and Control (C2):**
  * Establishing stealthy communication channels between compromised hosts and attacker-controlled infrastructure.
  * Evading network monitoring and detection capabilities by blending malicious traffic with legitimate network activity.
* **Data Exfiltration:**
  * Routing stolen data through proxies to obscure the true destination of exfiltrated information.
  * Preventing defenders from tracing data leaks back to attacker-controlled endpoints.
* **Persistence and Lateral Movement:**
  * Enabling attackers to pivot through compromised hosts within a network, using proxies to conceal lateral movement activities.
  * Providing a layer of anonymity when attackers move laterally across internal network segments.

## How this Technique is Usually Detected

Detection of proxy techniques involves various approaches, tools, and indicators of compromise (IoCs):

* **Network Traffic Analysis:**
  * Identifying unusual traffic patterns, such as connections to known proxy ports (e.g., 8080, 3128, 1080).
  * Detecting inconsistencies in HTTP headers (e.g., "X-Forwarded-For") or unusual User-Agent strings.
* **Endpoint Detection and Response (EDR):**
  * Monitoring endpoint processes and network connections to identify suspicious proxy configurations or software.
  * Detecting malware or unauthorized tools configured to utilize proxy servers.
* **Log Analysis and SIEM Platforms:**
  * Correlating logs from firewalls, proxies, and web gateways to identify anomalous proxy usage.
  * Alerting on repeated attempts to connect to external proxy IP addresses or domains.
* **Threat Intelligence Feeds:**
  * Leveraging intelligence data to detect known malicious proxies, VPN services, or anonymizing networks.
  * Blocking known malicious IP addresses and domains associated with proxy infrastructure.

Specific Indicators of Compromise (IoCs):

* Unusual outbound traffic to known proxy ports (e.g., 8080, 1080, 3128).
* Presence of unauthorized proxy software or unexpected configuration changes on endpoints.
* Repeated connections to known Tor nodes or VPN exit nodes.
* Suspicious HTTP header anomalies or absence of expected headers.

## Why it is Important to Detect This Technique

Detecting proxy usage in cyber attacks is critical due to various potential impacts on systems and networks:

* **Attribution Difficulty:**
  * Proxies significantly complicate tracing the origin of attacks, hindering incident response and attribution efforts.
* **Data Exfiltration Risk:**
  * Attackers using proxies can silently exfiltrate sensitive data, intellectual property, or personally identifiable information (PII), resulting in regulatory penalties, financial losses, and reputational damage.
* **Persistence and Stealth:**
  * Proxy usage allows attackers to maintain long-term access to compromised networks, facilitating persistent threats that evade detection and remediation.
* **Bypassing Security Controls:**
  * Attackers leveraging proxies can bypass firewall rules, intrusion detection systems, and other network security measures, making detection and mitigation challenging.

Early detection of proxy techniques ensures rapid containment, reduces dwell time, and mitigates potential damage to organizational assets.

## Examples

* **APT29 (Cozy Bear) and SolarWinds Attack:**
  * Attack Scenario: APT29 leveraged proxies and VPN services extensively during the SolarWinds supply chain attack to maintain anonymity and obscure their infrastructure.
  * Tools Used: Cobalt Strike beacon configured to communicate through HTTP/S proxies.
  * Impact: Compromise of multiple high-profile organizations, including government agencies and corporations, leading to significant data breaches and espionage activities.
* **FIN7 Cybercrime Group:**
  * Attack Scenario: FIN7 utilized proxies and reverse proxies to communicate with compromised point-of-sale (POS) systems in retail and hospitality sectors.
  * Tools Used: Custom malware and C2 frameworks configured to route traffic through reverse proxies and compromised web servers.
  * Impact: Theft of millions of credit card records, causing substantial financial losses and reputational damage to targeted organizations.
* **Operation Aurora (Google and Others):**
  * Attack Scenario: Attackers used proxy servers to obfuscate command-and-control communications during targeted attacks on multiple high-profile companies, including Google.
  * Tools Used: Malware configured to communicate through HTTP proxies, leveraging encrypted channels to evade detection.
  * Impact: Theft of intellectual property and sensitive corporate information, highlighting the importance of detecting proxy-based C2 channels.
* **WannaCry Ransomware Incident:**
  * Attack Scenario: WannaCry ransomware leveraged Tor anonymity network proxies for command-and-control communications, complicating attribution efforts.
  * Tools Used: Embedded Tor clients within malware payloads.
  * Impact: Global disruption across healthcare, manufacturing, and government sectors, causing significant financial and operational impact.

These real-world examples underline the critical need for organizations to detect and mitigate proxy techniques proactively, as adversaries continually leverage proxies to evade detection, maintain persistence, and achieve their malicious objectives.
